"""Migrate a PlantLibrary batch package's ``TASK_CHECKLIST.md`` from the
14-column ``_V3`` schema to Conductor's 15-column schema (onboarding runbook
``PROMPTS_conductor-onboarding-runbook_2026-09-15.md`` Appendix B).

For each data row this:

1. Restores a row that is exactly one cell short of the 14-column V3 width,
   but only when the missing cell is on the closed ``KNOWN_MISSING_CELL_FIXES``
   list below (F-4). Any other short row is a hard error -- guessing which
   cell dropped out is not this script's job.
2. Rewrites the header and separator row to the 15-column Conductor form
   (Appendix B.1).
3. Appends the row's ``model`` cell: the row's owning batch's tier pair from
   ``--model-map`` (batches are read from ``BATCH_PLAN.md``'s existing
   ``**Primary rows:**`` lines), except a row whose own ``risk`` cell is
   ``H``, which always gets ``opus/sol`` regardless of its batch's pair (D8).
4. Rewrites the leading ``<!-- ... -->`` schema-comment block's
   ``Columns (V3 schema): ...`` lines to the 15-column line plus the
   ``model:`` tier-pair line (Appendix B.2).

The file is read and written as bytes; its line-ending convention (CRLF or
LF, whichever the file already uses) is detected once and reused for every
line this script rewrites or inserts, so untouched lines are byte-identical
and rewritten lines match their neighbours. Running it a second time against
an already-migrated checklist (15-column header present) is refused.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

V3_COLUMNS: tuple[str, ...] = (
    "ID",
    "status",
    "skill",
    "design_context",
    "baseline_id",
    "area",
    "file(s)",
    "task",
    "context",
    "requirements",
    "done-when",
    "validation",
    "risk",
    "effort",
)
CONDUCTOR_COLUMNS: tuple[str, ...] = V3_COLUMNS + ("model",)

HEADER_LINE = "| " + " | ".join(CONDUCTOR_COLUMNS) + " |"
SEPARATOR_LINE = "|" + "---|" * len(CONDUCTOR_COLUMNS)

# Appendix B.2, pasted verbatim (four physical lines).
SCHEMA_COMMENT_LINES: tuple[str, ...] = (
    "Columns (Conductor schema, 15): ID | status | skill | design_context | baseline_id | area |",
    "file(s) | task | context | requirements | done-when | validation | risk | effort | model",
    "model: opus/sol | sonnet/terra | haiku/luna — the Claude tier and its Codex match, always",
    "together; a blank cell inherits the batch's **Model:** line.",
)

# Closed list (F-4): row ID -> (V3 column name that is missing, value to
# insert). Extend per package as a migration discovers its own unambiguous
# case; never widen this to a heuristic.
KNOWN_MISSING_CELL_FIXES: dict[str, tuple[str, str]] = {
    "PY-V1-REL-02": ("area", "packaging"),
}

_BACKTICK_TOKEN = re.compile(r"`([^`]+)`")
_ID_TOKEN = re.compile(r"^[A-Z0-9]+(?:-[A-Z0-9]+)+$")
_BATCH_HEADING = re.compile(r"^## Batch (?P<key>[A-Z][A-Z0-9-]+)\b")
_PRIMARY_ROWS_LABEL = re.compile(r"^\*\*Primary rows:\*\*(?P<rest>.*)$")
_ANY_BOLD_LABEL = re.compile(r"^\*\*[^*:\n]+:\*\*")
_SCHEMA_HEADING = re.compile(r"^Columns \(.*schema.*\):\s*$")


def split_checklist_cells(line: str) -> list[str]:
    """Split a Markdown table row on structural pipes only.

    Mirrors ``conductor.batch_package.split_checklist_cells``: a ``|`` is a
    cell boundary unless escaped (``\\|``), inside a backtick span, or inside
    a Markdown link destination ``](...)``.
    """

    cells: list[str] = []
    buffer: list[str] = []
    in_code = False
    in_link_dest = False
    i = 0
    n = len(line)
    while i < n:
        char = line[i]
        if char == "\\" and i + 1 < n and line[i + 1] == "|":
            buffer.append("|")
            i += 2
            continue
        if char == "`":
            in_code = not in_code
            buffer.append(char)
            i += 1
            continue
        if not in_code and char == "]" and i + 1 < n and line[i + 1] == "(":
            in_link_dest = True
            buffer.append(char)
            i += 1
            continue
        if in_link_dest and char == ")":
            in_link_dest = False
            buffer.append(char)
            i += 1
            continue
        if char == "|" and not in_code and not in_link_dest:
            cells.append("".join(buffer))
            buffer = []
            i += 1
            continue
        buffer.append(char)
        i += 1
    cells.append("".join(buffer))
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [cell.strip() for cell in cells]


def _is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-+:?", cell) for cell in cells)


def parse_primary_row_batches(batch_plan_text: str) -> dict[str, str]:
    """Map each checklist row ID to its owning batch key.

    Reads only ``## Batch <KEY>`` headings and the ``**Primary rows:**``
    field that follows (continuation lines included, the same shape
    Conductor's own parser accepts) -- everything the model map needs, and
    nothing that a pending ``**Model:**``/reorder edit would change.
    """

    owner: dict[str, str] = {}
    current_key: str | None = None
    in_primary = False
    for raw_line in batch_plan_text.split("\n"):
        line = raw_line.rstrip("\r")
        heading = _BATCH_HEADING.match(line)
        if heading is not None:
            current_key = heading.group("key")
            in_primary = False
            continue
        if current_key is None:
            continue
        primary = _PRIMARY_ROWS_LABEL.match(line)
        if primary is not None:
            for token in _BACKTICK_TOKEN.findall(primary.group("rest")):
                stripped = token.strip()
                if _ID_TOKEN.match(stripped):
                    owner[stripped] = current_key
            in_primary = True
            continue
        if _ANY_BOLD_LABEL.match(line) is not None or not line.strip():
            in_primary = False
            continue
        if in_primary:
            for token in _BACKTICK_TOKEN.findall(line):
                stripped = token.strip()
                if _ID_TOKEN.match(stripped):
                    owner[stripped] = current_key
    return owner


def detect_newline(raw: bytes) -> bytes:
    return b"\r\n" if b"\r\n" in raw else b"\n"


def _load_model_map(raw_arg: str) -> dict[str, str]:
    candidate = Path(raw_arg)
    if candidate.is_file():
        return json.loads(candidate.read_text(encoding="utf-8"))
    return json.loads(raw_arg)


def migrate(package_dir: Path, model_map: dict[str, str]) -> list[str]:
    """Perform the migration in place. Returns a list of error messages; a
    non-empty list means nothing was written."""

    checklist_path = package_dir / "TASK_CHECKLIST.md"
    batch_plan_path = package_dir / "BATCH_PLAN.md"

    raw = checklist_path.read_bytes()
    newline = detect_newline(raw)
    nl = newline.decode("ascii")
    text = raw.decode("utf-8-sig")
    lines = text.split(nl) if nl == "\r\n" else text.split("\n")
    # Guard the split against a file whose *body* mixes the rare opposite
    # newline: normalize any stray '\r' left over from a naive '\n' split.
    lines = [line.rstrip("\r") if nl == "\n" else line for line in lines]

    header_index: int | None = None
    for index, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = split_checklist_cells(line)
        lowered = [cell.lower() for cell in cells]
        if lowered == [col.lower() for col in CONDUCTOR_COLUMNS]:
            return ["checklist already has the 15-column Conductor header -- refusing to run twice"]
        if lowered == [col.lower() for col in V3_COLUMNS]:
            header_index = index
            break

    if header_index is None:
        return ["no 14-column V3 checklist header found"]

    if not batch_plan_path.is_file():
        return [f"missing {batch_plan_path}"]
    batch_plan_text = batch_plan_path.read_text(encoding="utf-8-sig")
    row_owner = parse_primary_row_batches(batch_plan_text)

    out_lines = list(lines)
    out_lines[header_index] = HEADER_LINE

    sep_index = header_index + 1
    if sep_index >= len(lines):
        return ["header is the last line -- no separator row"]
    if not _is_separator_row(split_checklist_cells(lines[sep_index])):
        return ["no separator row after the header"]
    out_lines[sep_index] = SEPARATOR_LINE

    errors: list[str] = []
    row_index = sep_index + 1
    while row_index < len(lines) and lines[row_index].strip().startswith("|"):
        line = lines[row_index]
        cells = split_checklist_cells(line)
        if _is_separator_row(cells):
            row_index += 1
            continue
        if len(cells) == len(V3_COLUMNS) - 1:
            row_id = cells[0] if cells else "<unknown>"
            fix = KNOWN_MISSING_CELL_FIXES.get(row_id)
            if fix is None:
                errors.append(
                    f"line {row_index + 1}: row {row_id!r} has {len(cells)} cells, "
                    f"expected {len(V3_COLUMNS)} -- no known unambiguous repair"
                )
                row_index += 1
                continue
            column_name, value = fix
            insert_at = V3_COLUMNS.index(column_name)
            cells = cells[:insert_at] + [value] + cells[insert_at:]
        if len(cells) != len(V3_COLUMNS):
            errors.append(
                f"line {row_index + 1}: row has {len(cells)} cells, expected {len(V3_COLUMNS)}"
            )
            row_index += 1
            continue
        row_id = cells[0]
        risk = cells[V3_COLUMNS.index("risk")].strip().upper()
        if risk == "H":
            model_cell = "opus/sol"
        else:
            batch_key = row_owner.get(row_id)
            if batch_key is None:
                errors.append(
                    f"line {row_index + 1}: row {row_id!r} is not a primary row of any "
                    "BATCH_PLAN.md batch -- cannot assign a model tier"
                )
                row_index += 1
                continue
            model_cell = model_map.get(batch_key)
            if model_cell is None:
                errors.append(
                    f"line {row_index + 1}: batch {batch_key!r} (row {row_id!r}) has no "
                    "entry in --model-map"
                )
                row_index += 1
                continue
        new_cells = list(cells) + [model_cell]
        out_lines[row_index] = "| " + " | ".join(new_cells) + " |"
        row_index += 1

    if errors:
        return errors

    joined = nl.join(out_lines)

    comment_match = re.search(r"<!--.*?-->", joined, re.DOTALL)
    if comment_match is None:
        return ["no schema comment block (<!-- ... -->) found at the top of the checklist"]
    comment_text = comment_match.group(0)
    comment_lines = comment_text.split(nl) if nl == "\r\n" else comment_text.split("\n")

    heading_at: int | None = None
    for index, line in enumerate(comment_lines):
        if _SCHEMA_HEADING.match(line.strip()):
            heading_at = index
            break
    if heading_at is None:
        return ["no 'Columns (... schema):' heading found in the comment block"]
    # The column-list line is the next non-blank line after the heading.
    list_at = heading_at + 1
    while list_at < len(comment_lines) and not comment_lines[list_at].strip():
        list_at += 1
    if list_at >= len(comment_lines):
        return ["schema heading has no following column-list line"]

    new_comment_lines = (
        comment_lines[:heading_at] + list(SCHEMA_COMMENT_LINES) + comment_lines[list_at + 1 :]
    )
    new_comment_text = nl.join(new_comment_lines)
    joined = joined[: comment_match.start()] + new_comment_text + joined[comment_match.end() :]

    checklist_path.write_bytes(joined.encode("utf-8"))
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package_dir", type=Path, help="Package folder holding TASK_CHECKLIST.md + BATCH_PLAN.md")
    parser.add_argument(
        "--model-map",
        required=True,
        help="JSON file path or inline JSON object: {\"<BATCH-KEY>\": \"<tier>/<tier>\", ...}",
    )
    args = parser.parse_args()

    try:
        model_map = _load_model_map(args.model_map)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: could not load --model-map: {exc}", file=sys.stderr)
        return 1

    errors = migrate(args.package_dir, model_map)
    if errors:
        for message in errors:
            print(f"error: {message}", file=sys.stderr)
        return 1

    print(f"migrated {args.package_dir / 'TASK_CHECKLIST.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
