#!/usr/bin/env python3
"""Repo Hygiene Template Kit — the checker (KIT_SPEC.md §7).

One file, Python 3 stdlib only. Three modes:

    check        the rules of KIT_SPEC.md §1–§5 and §10 over a repository;
                 exit 0 (no violations), 1 (violations), 2 (could not run)
    census       per declared root, a markdown table ``file · class ·
                 git-created · compliance`` and totals; read-only; exit 0 or 2
    --self-test  copy the configured tree to a temporary directory, plant one
                 defect per rule of the file, index, proof-surface and block
                 checks, prove each is reported, remove the copy, re-check the
                 original; exit 0 or 1

Every project fact — roots, exemptions, holds, allowlists — is read at run
time from ``<repo>/hygiene/CONSUMED_HYGIENE.md`` (the pin, §7.2) and
``<repo>/hygiene/HYGIENE_DECISIONS.md`` (the decision record, §6). Nothing
here names a project. The two regex families below are copied character for
character from the SOURCE harness the kit is derived from (``SOURCE_HARNESS.md``):
the naming patterns from ``tests/test_docs_naming_hygiene.py`` and the
proof-surface detectors from ``tests/test_prompt_proof_surface_hygiene.py``,
both at the pinned commit.

``check`` and ``census`` write nothing. ``--self-test`` writes only inside a
temporary directory it creates under the system temp location and removes.
Files are read as UTF-8 with undecodable bytes replaced; CRLF, LF and mixed
files are all legal; the only normalisation is the rule-block comparison's
(``\\r\\n`` → ``\\n``, §5). Paths are printed repository-relative with ``/``.

Entry points: ``run_check(repo_root, config_dir)`` (the pytest wrapper's) and
``main(argv)``.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

sys.dont_write_bytecode = True

CONFIG_DIR_NAME = "hygiene"
PIN_NAME = "CONSUMED_HYGIENE.md"
RECORD_NAME = "HYGIENE_DECISIONS.md"
INDEX_NAME = "INDEX.md"
BUILT_IN_EXEMPT = frozenset({"INDEX.md", "README.md"})
INSTRUCTION_FILES = ("CLAUDE.md", "AGENTS.md")
BEGIN_MARKER = "<!-- repo-hygiene:begin -->"
END_MARKER = "<!-- repo-hygiene:end -->"

ROOT_KINDS = ("planning", "proposal", "handovers", "general")
ROOT_PATTERNS = ("standard", "date-anywhere")
MODULES = ("root-allowlist", "scratch")
TREE_CLASSES = ("frozen", "pinned", "generated", "legacy")
DIRECTIVES = (
    "exempt-name",
    "exempt-subfolder",
    "exempt-tree",
    "held-name",
    "held-line",
    "release",
    "enum-add",
    "allowlist",
    "allowlist-remove",
    "retired-name",
    "forbidden-path",
    "scratch-root",
)
PIN_FIELDS = (
    "Kit version",
    "Kit path",
    "SOURCE harness",
    "Pinned on",
    "Modules",
    "Pytest wrapper",
    "Rule block",
    "Sanctioned launcher",
    "Prompt file floor",
)

# --- KIT_SPEC.md §1.1 — verbatim from SOURCE tests/test_docs_naming_hygiene.py ---
TYPE_ENUM = (
    "PROPOSAL", "PROMPT", "PROMPTS", "PLAN", "EVIDENCE", "AUDIT", "REGISTER",
    "MATRIX", "SNAPSHOT", "HANDOVER", "FINDING",
)
STANDARD_PATTERN_SOURCE = (
    r"^(PROPOSAL|PROMPT|PROMPTS|PLAN|EVIDENCE|AUDIT|REGISTER|MATRIX|SNAPSHOT"
    r"|HANDOVER|FINDING)_.+_\d{4}-\d{2}-\d{2}\.md$"
)
DATE_ANYWHERE_PATTERN = re.compile(r"^(HANDOVER|FINDING)_.*\d{4}-\d{2}-\d{2}.*\.md$")


def standard_pattern(extra_types: tuple[str, ...] = ()) -> re.Pattern[str]:
    """The standard pattern, its alternation extended by ``enum-add`` entries."""

    alternation = "|".join(TYPE_ENUM + tuple(extra_types))
    return re.compile(r"^(" + alternation + r")_.+_\d{4}-\d{2}-\d{2}\.md$")


def set_folder_pattern(extra_types: tuple[str, ...] = ()) -> re.Pattern[str]:
    """§1.8: the standard pattern without ``.md`` — a dated set folder."""

    alternation = "|".join(TYPE_ENUM + tuple(extra_types))
    return re.compile(r"^(" + alternation + r")_.+_\d{4}-\d{2}-\d{2}$")


assert standard_pattern().pattern == STANDARD_PATTERN_SOURCE, "enum drifted from SOURCE"

# --- KIT_SPEC.md §4 — verbatim from SOURCE tests/test_prompt_proof_surface_hygiene.py ---
_ARGV_BARE_TESTS_ROOT = re.compile(r"pytest(?:\s+\S+)*?\s+tests/?(?:\s|`|$)")
_ARGV_BROAD_FLAGS = re.compile(r"(--ignore=|(?<=\s)-x(?=\s|`|$)|--lf\b|--ff\b)")
_PROSE_WHOLE_SUITE = re.compile(
    r"(re)?run (the )?(full|whole|entire)( non-gui| offline)? suite"
    r"|(full|whole|entire) suite to completion",
    re.I,
)
_NEGATION = re.compile(r"\b(do not|don't|never|not|no|forbid|prohibit)\b", re.I)

# --- markdown shapes the two hygiene/ files use (§6, §7.2) ---
_TABLE_ROW = re.compile(r"^\s*\|(.*)\|\s*$")
_TABLE_SEPARATOR_CELL = re.compile(r"^:?-{2,}:?$")
_ROOTS_HEADING = re.compile(r"^##\s+Deliverable roots\b", re.I)
_ENTRY_HEADING = re.compile(r"^###\s+D-(\d{4}-\d{2}-\d{2}-\d{2})\s+[—–-]+\s+\S")
_ENTRY_PREFIX = re.compile(r"^###\s+D-")
_HEADING = re.compile(r"^#{1,6}\s")
_DIRECTIVE = re.compile(r"^\s*[-*]\s+([a-z][a-z0-9]*(?:-[a-z0-9]+)*):(?:\s+(.*?))?\s*$")
_FENCE = re.compile(r"^\s*(```|~~~)")
_DRIVE = re.compile(r"^[A-Za-z]:")


class ConfigError(Exception):
    """The pin or the record is missing or unparseable — exit 2."""


# ---------------------------------------------------------------------------
# results
# ---------------------------------------------------------------------------


@dataclass(frozen=True, order=True)
class Violation:
    path: str
    line_number: int
    rule: str
    detail: str

    @property
    def line(self) -> str:
        where = self.path if not self.line_number else f"{self.path}:{self.line_number}"
        return f"{where}: {self.rule} — {self.detail}"


@dataclass
class CheckResult:
    violations: list[Violation] = field(default_factory=list)
    held: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    exit_code: int = 0

    @property
    def verdict(self) -> str:
        if self.errors:
            return "repo-hygiene: error — could not run: " + "; ".join(self.errors)
        n, m, k = len(self.violations), len(self.held), len(self.skipped)
        if n:
            text = f"repo-hygiene: fail — {n} violations, {m} held"
        elif m:
            text = f"repo-hygiene: pass with holds — 0 violations, {m} held"
        else:
            text = "repo-hygiene: pass — 0 violations, 0 held"
        if k:
            text += f", {k} skipped"
        return text

    @property
    def lines(self) -> list[str]:
        out = [v.line for v in sorted(self.violations)]
        out += [f"held: {h}" for h in sorted(self.held)]
        out += [f"skipped: {s}" for s in self.skipped]
        out.append(self.verdict)
        return out

    def add(self, path: str, rule: str, detail: str, line_number: int = 0) -> None:
        self.violations.append(Violation(path, line_number, rule, detail))


# ---------------------------------------------------------------------------
# configuration: the pin (§7.2) and the decision record (§6)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Root:
    path: str  # repository-relative, "/"-separated, no trailing slash
    kind: str
    pattern: str


@dataclass
class Pin:
    fields: dict[str, str]
    roots: list[Root]
    modules: frozenset[str]
    rule_block: bool
    launcher: str
    floor: int


@dataclass(frozen=True)
class Directive:
    name: str
    value: str
    note: str
    line_number: int


@dataclass
class Record:
    directives: list[Directive]
    exempt_basenames: set[str] = field(default_factory=set)
    exempt_paths: set[str] = field(default_factory=set)
    exempt_subfolders: dict[str, int] = field(default_factory=dict)
    exempt_trees: dict[str, str] = field(default_factory=dict)  # path -> class
    held: dict[str, str] = field(default_factory=dict)  # path -> note
    held_at: dict[str, int] = field(default_factory=dict)  # path -> the held-name line in force
    held_lines: set[tuple[str, int]] = field(default_factory=set)
    enum_add: list[str] = field(default_factory=list)
    allowlist: set[str] = field(default_factory=set)
    retired: set[str] = field(default_factory=set)
    forbidden: list[str] = field(default_factory=list)
    scratch_root: str = ".tmp"
    problems: list[Violation] = field(default_factory=list)


def read_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8", errors="replace")


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == "`" and value[-1] == "`":
        value = value[1:-1]
    return value.strip()


def normalise_relative(value: str) -> str:
    """``\\`` or ``/`` in, ``/`` out; no leading ``./``, no trailing ``/``."""

    value = _unquote(value).replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    return value.rstrip("/")


def is_inside_repository(rel: str) -> bool:
    if not rel or rel.startswith("/") or _DRIVE.match(rel):
        return False
    parts = rel.split("/")
    return ".." not in parts and "" not in parts and "." not in parts


def _tables(lines: list[str]) -> list[tuple[int, list[list[str]]]]:
    """Every contiguous markdown table: (line index of its first row, rows)."""

    tables: list[tuple[int, list[list[str]]]] = []
    current: list[list[str]] | None = None
    start = 0
    for index, line in enumerate(lines):
        match = _TABLE_ROW.match(line)
        if not match:
            if current is not None:
                tables.append((start, current))
                current = None
            continue
        cells = [cell.strip() for cell in match.group(1).split("|")]
        if current is None:
            current, start = [], index
        if all(_TABLE_SEPARATOR_CELL.match(cell) or cell == "" for cell in cells):
            continue
        current.append(cells)
    if current is not None:
        tables.append((start, current))
    return tables


def load_pin(path: Path) -> Pin:
    if not path.is_file():
        raise ConfigError(f"pin not found: {path.as_posix()}")
    lines = read_text(path).splitlines()
    tables = _tables(lines)

    fields: dict[str, str] = {}
    field_table = next(
        (rows for _, rows in tables if rows and len(rows[0]) >= 2
         and rows[0][0].lower() == "field" and rows[0][1].lower() == "value"),
        None,
    )
    if field_table is None:
        raise ConfigError(f"{path.name}: no `| Field | Value |` table")
    for row in field_table[1:]:
        if len(row) >= 2:
            fields[row[0].strip("*` ").lower()] = _unquote(row[1])
    missing = [name for name in PIN_FIELDS if name.lower() not in fields]
    if missing:
        raise ConfigError(f"{path.name}: missing pin row(s): {', '.join(missing)}")

    roots_at = next((i for i, line in enumerate(lines) if _ROOTS_HEADING.match(line)), None)
    if roots_at is None:
        raise ConfigError(f"{path.name}: no `## Deliverable roots` section")
    roots_table = next(
        (rows for start, rows in tables if start > roots_at and rows
         and rows[0][0].lower() == "root"),
        None,
    )
    if roots_table is None:
        raise ConfigError(f"{path.name}: no `| Root | Kind | Pattern |` table under `## Deliverable roots`")
    roots: list[Root] = []
    for row in roots_table[1:]:
        row = row + ["", ""]
        rel = normalise_relative(row[0])
        if not is_inside_repository(rel):
            raise ConfigError(f"{path.name}: root {row[0]!r} is not a folder inside the repository")
        kind = _unquote(row[1]).lower() or _infer_kind(rel)
        if kind not in ROOT_KINDS:
            raise ConfigError(f"{path.name}: root {rel}: unknown kind {kind!r}")
        pattern = _unquote(row[2]).lower() or ("date-anywhere" if kind == "handovers" else "standard")
        if pattern not in ROOT_PATTERNS:
            raise ConfigError(f"{path.name}: root {rel}: unknown pattern {pattern!r}")
        if any(existing.path == rel for existing in roots):
            raise ConfigError(f"{path.name}: root {rel} declared twice")
        roots.append(Root(rel, kind, pattern))

    modules_value = fields["modules"].lower()
    modules: set[str] = set()
    if modules_value not in ("", "none"):
        for name in (part.strip() for part in modules_value.split(",")):
            if name not in MODULES:
                raise ConfigError(f"{path.name}: Modules: unknown module {name!r}")
            modules.add(name)
    rule_block = fields["rule block"].lower()
    if rule_block not in ("on", "off"):
        raise ConfigError(f"{path.name}: Rule block must be `on` or `off`, not {rule_block!r}")
    if fields["pytest wrapper"].lower() not in ("yes", "no"):
        raise ConfigError(f"{path.name}: Pytest wrapper must be `yes` or `no`")
    launcher = fields["sanctioned launcher"]
    if launcher.lower() in ("none", "—", "-"):
        launcher = ""
    if "/" in launcher or "\\" in launcher:
        raise ConfigError(f"{path.name}: Sanctioned launcher must be a basename, not {launcher!r}")
    try:
        floor = int(fields["prompt file floor"])
    except ValueError:
        raise ConfigError(f"{path.name}: Prompt file floor must be an integer ≥ 0") from None
    if floor < 0:
        raise ConfigError(f"{path.name}: Prompt file floor must be an integer ≥ 0")
    return Pin(fields, roots, frozenset(modules), rule_block == "on", launcher, floor)


def _infer_kind(rel: str) -> str:
    last = rel.rsplit("/", 1)[-1].lower()
    return last if last in ("planning", "proposal", "handovers") else "general"


def load_record(path: Path, repo_root: Path, label: str) -> Record:
    if not path.is_file():
        raise ConfigError(f"decision record not found: {path.as_posix()}")
    lines = read_text(path).splitlines()
    record = Record(directives=[])
    seen_ids: set[str] = set()
    in_fence = False
    in_entry = False

    def problem(number: int, detail: str) -> None:
        record.problems.append(Violation(label, number, "record", detail))

    for number, line in enumerate(lines, start=1):
        if _FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if _HEADING.match(line):
            heading = _ENTRY_HEADING.match(line)
            if heading:
                entry_id = heading.group(1)
                if entry_id in seen_ids:
                    problem(number, f"duplicate entry id D-{entry_id}")
                seen_ids.add(entry_id)
                in_entry = True
            elif _ENTRY_PREFIX.match(line):
                problem(number, "entry heading is not `### D-YYYY-MM-DD-nn — <title>`")
                in_entry = False
            else:
                in_entry = False
            continue
        if not in_entry:
            continue
        match = _DIRECTIVE.match(line)
        if not match:
            continue
        name = match.group(1)
        raw = match.group(2) or ""
        value, _, note = raw.partition(" — ")
        directive = Directive(name, _unquote(value), note.strip(), number)
        record.directives.append(directive)
        if name not in DIRECTIVES:
            problem(number, f"unknown directive {name!r}")
            continue
        _apply_directive(directive, record, repo_root, problem)
    # A held name must exist while held (§6): judged once the whole record is folded, only for
    # holds still active, on the held-name line in force — a hold ended by a release needs no file.
    for rel, number in record.held_at.items():
        if not (repo_root / rel).is_file():
            problem(number, f"held-name {rel} does not exist")
    return record


def _apply_directive(d: Directive, record: Record, repo_root: Path, problem) -> None:
    name, value = d.name, d.value
    if not value:
        problem(d.line_number, f"{name}: empty value")
        return
    if name in ("exempt-name", "exempt-subfolder", "exempt-tree", "held-name", "release"):
        rel = normalise_relative(value)
        if name == "exempt-name" and "/" not in rel:
            record.exempt_basenames.add(rel)
            return
        if not is_inside_repository(rel):
            problem(d.line_number, f"{name}: {value!r} is not a repository-relative path")
            return
        target = repo_root / rel
        if name == "exempt-name":
            record.exempt_paths.add(rel)
        elif name == "exempt-subfolder":
            if not target.is_dir():
                problem(d.line_number, f"exempt-subfolder {rel} does not exist")
            record.exempt_subfolders[rel] = d.line_number
        elif name == "exempt-tree":
            tree_class = d.note.split(";")[0].split()[0].lower() if d.note.strip() else ""
            if tree_class not in TREE_CLASSES:
                problem(d.line_number, f"exempt-tree {rel}: note must name a class — {', '.join(TREE_CLASSES)}")
            if not target.exists():
                problem(d.line_number, f"exempt-tree {rel} does not exist")
            record.exempt_trees[rel] = tree_class or "legacy"
        elif name == "held-name":
            if "cited by" not in d.note:
                problem(d.line_number, f"held-name {rel}: note must read `<group>; cited by <citer>; target on release: <name>`")
            record.held[rel] = d.note
            record.held_at[rel] = d.line_number  # existence is judged after the fold (load_record)
        elif name == "release":
            if rel not in record.held:
                problem(d.line_number, f"release {rel}: no earlier held-name for this path")
            else:
                del record.held[rel]
                del record.held_at[rel]
        return
    if name == "held-line":
        path_part, sep, line_part = value.rpartition(":")
        rel = normalise_relative(path_part)
        if not sep or not line_part.isdigit() or not is_inside_repository(rel):
            problem(d.line_number, f"held-line: {value!r} is not `<path>:<line>`")
            return
        record.held_lines.add((rel, int(line_part)))
        return
    if name == "enum-add":
        if not re.fullmatch(r"[A-Z]+", value):
            problem(d.line_number, f"enum-add: {value!r} is not an uppercase TYPE")
        elif value in TYPE_ENUM or value in record.enum_add:
            problem(d.line_number, f"enum-add: {value} is already in the enum")
        else:
            record.enum_add.append(value)
        return
    if name == "allowlist":
        record.allowlist.add(value)
    elif name == "allowlist-remove":
        if value not in record.allowlist:
            problem(d.line_number, f"allowlist-remove: {value!r} was never allowed")
        record.allowlist.discard(value)
    elif name == "retired-name":
        record.retired.add(value)
    elif name == "forbidden-path":
        record.forbidden.append(value)
    elif name == "scratch-root":
        if "/" in value or "\\" in value:
            problem(d.line_number, f"scratch-root must be a folder name, not {value!r}")
        else:
            record.scratch_root = value


# ---------------------------------------------------------------------------
# locating the repository (§7.3)
# ---------------------------------------------------------------------------


def find_repository(start: Path) -> Path | None:
    """The nearest ancestor of ``start`` holding ``hygiene/CONSUMED_HYGIENE.md``."""

    for candidate in (start, *start.parents):
        if (candidate / CONFIG_DIR_NAME / PIN_NAME).is_file():
            return candidate
    return None


def find_git_root(start: Path) -> Path | None:
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def relative_label(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


# ---------------------------------------------------------------------------
# scanning a root (§1, §2)
# ---------------------------------------------------------------------------


@dataclass
class RootScan:
    root: Root
    exists: bool
    md_files: list[str] = field(default_factory=list)  # basenames, sorted
    other_files: list[str] = field(default_factory=list)
    set_folders: list[str] = field(default_factory=list)
    exempt_subfolders: list[str] = field(default_factory=list)
    nested_roots: list[str] = field(default_factory=list)
    subfolders: list[str] = field(default_factory=list)
    index_text: str | None = None


class Rules:
    """The configuration folded into what the checks ask."""

    def __init__(self, repo_root: Path, pin: Pin, record: Record) -> None:
        self.repo_root = repo_root
        self.pin = pin
        self.record = record
        extra = tuple(record.enum_add)
        self.standard = standard_pattern(extra)
        self.set_folder = set_folder_pattern(extra)
        self.root_paths = {root.path for root in pin.roots}

    def is_exempt(self, rel: str) -> bool:
        base = rel.rsplit("/", 1)[-1]
        if base in BUILT_IN_EXEMPT or base in self.record.exempt_basenames:
            return True
        if rel in self.record.exempt_paths:
            return True
        return self.under_exempt_tree(rel) is not None

    def under_exempt_tree(self, rel: str) -> str | None:
        for tree in self.record.exempt_trees:
            if rel == tree or rel.startswith(tree + "/"):
                return tree
        return None

    def is_held(self, rel: str) -> bool:
        return rel in self.record.held

    def name_matches(self, root: Root, basename: str) -> bool:
        pattern = DATE_ANYWHERE_PATTERN if root.pattern == "date-anywhere" else self.standard
        return bool(pattern.match(basename))

    def classify(self, root: Root, basename: str) -> str:
        rel = f"{root.path}/{basename}"
        if basename == INDEX_NAME:
            return "index"
        if self.is_exempt(rel):
            return "exempt"
        if self.is_held(rel):
            return "held"
        return "compliant" if self.name_matches(root, basename) else "candidate"

    def scan(self, root: Root) -> RootScan:
        folder = self.repo_root / root.path
        scan = RootScan(root, folder.is_dir())
        if not scan.exists:
            return scan
        for entry in sorted(folder.iterdir(), key=lambda p: p.name):
            rel = f"{root.path}/{entry.name}"
            if entry.is_file():
                if entry.suffix == ".md":
                    scan.md_files.append(entry.name)
                else:
                    scan.other_files.append(entry.name)
            elif entry.is_dir():
                if rel in self.root_paths:
                    scan.nested_roots.append(entry.name)
                elif rel in self.record.exempt_subfolders:
                    scan.exempt_subfolders.append(entry.name)
                elif self.set_folder.match(entry.name):
                    scan.set_folders.append(entry.name)
                else:
                    scan.subfolders.append(entry.name)
        index = folder / INDEX_NAME
        if index.is_file():
            scan.index_text = read_text(index)
        return scan


# ---------------------------------------------------------------------------
# the checks (§7.4 check)
# ---------------------------------------------------------------------------


def _pattern_hint(root: Root) -> str:
    if root.pattern == "date-anywhere":
        return "does not match <HANDOVER|FINDING>_<topic with YYYY-MM-DD>.md (pattern date-anywhere)"
    return "does not match <TYPE>_<topic>_<YYYY-MM-DD>.md (pattern standard)"


def check_roots(rules: Rules, result: CheckResult) -> list[RootScan]:
    scans: list[RootScan] = []
    for root in rules.pin.roots:
        scan = rules.scan(root)
        scans.append(scan)
        if not scan.exists:
            result.add(root.path, "root-missing", "declared root does not exist")
            continue
        for basename in scan.md_files:
            rel = f"{root.path}/{basename}"
            klass = rules.classify(root, basename)
            if klass == "candidate":
                result.add(rel, "name", _pattern_hint(root))
            elif klass == "held":
                result.held.append(f"{rel} — {rules.record.held[rel]}")
        if scan.index_text is None:
            result.add(f"{root.path}/{INDEX_NAME}", "index-missing", f"root {root.path} has no {INDEX_NAME}")
        else:
            for basename in scan.md_files:
                if rules.classify(root, basename) in ("index", "exempt"):
                    continue
                if basename not in scan.index_text:
                    result.add(f"{root.path}/{basename}", "index", f"not listed in {root.path}/{INDEX_NAME}")
            for folder in scan.set_folders:
                if folder not in scan.index_text:
                    result.add(f"{root.path}/{folder}/", "index", f"set folder not listed in {root.path}/{INDEX_NAME}")
    return scans


def _argv_names_a_proof_surface(line: str, launcher: str) -> bool:
    if "pytest" not in line or (launcher and launcher in line):
        return False
    return bool(_ARGV_BARE_TESTS_ROOT.search(line) or _ARGV_BROAD_FLAGS.search(line))


def _prose_demands_a_whole_suite(line: str) -> bool:
    match = _PROSE_WHOLE_SUITE.search(line)
    if match is None:
        return False
    return not _NEGATION.search(line[: match.start()])


def check_proof_surface(rules: Rules, scans: list[RootScan], result: CheckResult) -> None:
    pin_label = f"{CONFIG_DIR_NAME}/{PIN_NAME}"
    scanned = 0
    for scan in scans:
        if not scan.exists or scan.root.kind not in ("planning", "general"):
            continue
        for basename in scan.md_files:
            if not (basename.startswith("PROMPT_") or basename.startswith("PROMPTS_")):
                continue
            scanned += 1
            rel = f"{scan.root.path}/{basename}"
            text = read_text(rules.repo_root / scan.root.path / basename)
            for number, line in enumerate(text.splitlines(), start=1):
                if (rel, number) in rules.record.held_lines:
                    continue
                if _argv_names_a_proof_surface(line, rules.pin.launcher):
                    result.add(rel, "proof-argv", line.strip(), number)
                if _prose_demands_a_whole_suite(line):
                    result.add(rel, "proof-prose", line.strip(), number)
    # A floor of 0 is a pinned declaration backed by a decision entry (KIT_SPEC.md §4), never a default:
    # the scan above still runs over every prompt file present; only the count has nothing to reach.
    if scanned < rules.pin.floor:
        result.add(
            pin_label, "proof-floor",
            f"scanned {scanned} PROMPT_/PROMPTS_ files in planning and general roots; the pin's floor is {rules.pin.floor}",
        )


def marked_block(text: str) -> tuple[list[str] | None, str]:
    """The lines from the begin marker to the end marker, after ``\\r\\n`` → ``\\n``."""

    lines = text.replace("\r\n", "\n").split("\n")
    begins = [i for i, line in enumerate(lines) if line.strip() == BEGIN_MARKER]
    ends = [i for i, line in enumerate(lines) if line.strip() == END_MARKER]
    if len(begins) != 1 or len(ends) != 1:
        return None, f"expected exactly one marker pair, found {len(begins)} begin / {len(ends)} end"
    if ends[0] < begins[0]:
        return None, "end marker precedes begin marker"
    return lines[begins[0]: ends[0] + 1], ""


def check_rule_block(rules: Rules, result: CheckResult) -> None:
    if not rules.pin.rule_block:
        result.skipped.append("rule-block — off in pin")
        return
    blocks: dict[str, list[str]] = {}
    for name in INSTRUCTION_FILES:
        path = rules.repo_root / name
        if not path.is_file():
            result.add(name, "block-missing", "file absent")
            continue
        block, reason = marked_block(read_text(path))
        if block is None:
            result.add(name, "block-missing", reason)
        else:
            blocks[name] = block
    if len(blocks) != 2:
        return
    claude, agents = blocks["CLAUDE.md"], blocks["AGENTS.md"]
    if claude == agents:
        return
    for number, (a, b) in enumerate(zip(claude, agents), start=1):
        if a != b:
            result.add("AGENTS.md", "block-parity", f"differs from CLAUDE.md at block line {number}: CLAUDE.md={a!r} AGENTS.md={b!r}")
            return
    result.add("AGENTS.md", "block-parity", f"differs from CLAUDE.md in length: {len(claude)} lines vs {len(agents)}")


def _git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str] | None:
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    try:
        return subprocess.run(
            ["git", "-C", str(repo_root), *args],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120, env=env,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None


def check_modules(rules: Rules, result: CheckResult) -> None:
    record = rules.record
    if "root-allowlist" in rules.pin.modules:
        entries = {p.name for p in rules.repo_root.iterdir()} - {".git"}
        for entry in sorted(entries - record.allowlist):
            result.add(entry, "allowlist", "root entry not in the allowlist (decision record)")
        for entry in sorted(entries & record.retired):
            result.add(entry, "retired", "retired name recreated at the repository root")
        for path in record.forbidden:
            if Path(path).exists():
                result.add(path, "forbidden-path", "forbidden path exists")
    if "scratch" in rules.pin.modules:
        name = record.scratch_root
        if name in record.retired:
            result.add(name, "scratch", "the scratch root is also a retired name")
        proc = _git(rules.repo_root, "check-ignore", "-q", "--", name + "/")
        if proc is None or proc.returncode not in (0, 1):
            result.skipped.append("scratch — git could not answer check-ignore")
        elif proc.returncode == 1:
            result.add(name, "scratch", f"scratch root {name}/ is not ignored by git")
        if "root-allowlist" not in rules.pin.modules:
            entries = {p.name for p in rules.repo_root.iterdir()}
            for entry in sorted(entries & record.retired):
                result.add(entry, "retired", "retired scratch name recreated at the repository root")


def validate_roots(repo_root: Path, pin: Pin) -> None:
    for root in pin.roots:
        parts = root.path.split("/")
        for depth in range(1, len(parts) + 1):
            ancestor = repo_root.joinpath(*parts[:depth])
            if (ancestor / ".git").exists():
                raise ConfigError(f"root {root.path} lies inside a submodule ({'/'.join(parts[:depth])})")


def run_check(repo_root: os.PathLike[str] | str, config_dir: os.PathLike[str] | str | None = None,
              *, disable_modules: bool = False) -> CheckResult:
    """The check mode as a call: violations, held, skipped, errors, exit_code."""

    repo = Path(repo_root).resolve()
    config = Path(config_dir).resolve() if config_dir else repo / CONFIG_DIR_NAME
    result = CheckResult()
    try:
        pin = load_pin(config / PIN_NAME)
        record = load_record(config / RECORD_NAME, repo, relative_label(config / RECORD_NAME, repo))
        validate_roots(repo, pin)
    except ConfigError as exc:
        result.errors.append(str(exc))
        result.exit_code = 2
        return result
    result.violations.extend(record.problems)
    rules = Rules(repo, pin, record)
    scans = check_roots(rules, result)
    check_proof_surface(rules, scans, result)
    check_rule_block(rules, result)
    if not disable_modules:
        check_modules(rules, result)
    result.exit_code = 1 if result.violations else 0
    return result


# ---------------------------------------------------------------------------
# census (§7.4 census)
# ---------------------------------------------------------------------------


def git_created(repo_root: Path, rel: str, is_dir: bool = False) -> str:
    """§1.3: the first commit that added the path, followed across renames; UNKNOWN, never a guess."""

    args = ["log", "--diff-filter=A", "--format=%ad", "--date=short"]
    if not is_dir:
        args.append("--follow")
    proc = _git(repo_root, *args, "--", rel)
    if proc is None or proc.returncode != 0:
        return "UNKNOWN"
    dates = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    return dates[-1] if dates else "UNKNOWN"


def run_census(repo_root: os.PathLike[str] | str, config_dir: os.PathLike[str] | str | None = None) -> tuple[list[str], int]:
    repo = Path(repo_root).resolve()
    config = Path(config_dir).resolve() if config_dir else repo / CONFIG_DIR_NAME
    try:
        pin = load_pin(config / PIN_NAME)
        record = load_record(config / RECORD_NAME, repo, relative_label(config / RECORD_NAME, repo))
        validate_roots(repo, pin)
    except ConfigError as exc:
        return [f"repo-hygiene census: error — could not run: {exc}"], 2
    rules = Rules(repo, pin, record)
    out: list[str] = ["# repo-hygiene census", ""]
    totals = {"files": 0, "compliant": 0, "candidates": 0, "exempt": 0, "held": 0, "set folders": 0}
    for root in pin.roots:
        scan = rules.scan(root)
        out.append(f"## {root.path} (kind {root.kind}, pattern {root.pattern})")
        out.append("")
        if not scan.exists:
            out.append("root-missing — declared root does not exist")
            out.append("")
            continue
        out.append("| file | class | git-created | compliance |")
        out.append("|---|---|---|---|")
        counts = {"files": 0, "compliant": 0, "candidates": 0, "exempt": 0, "held": 0, "set folders": 0}
        for basename in scan.md_files:
            klass = rules.classify(root, basename)
            compliance = {"index": "n/a", "exempt": "n/a"}.get(
                klass, "yes" if rules.name_matches(root, basename) else "no")
            out.append(f"| {basename} | {klass} | {git_created(repo, f'{root.path}/{basename}')} | {compliance} |")
            counts["files"] += 1
            if klass == "compliant":
                counts["compliant"] += 1
            elif klass == "candidate":
                counts["candidates"] += 1
            elif klass == "held":
                counts["held"] += 1
            else:
                counts["exempt"] += 1
        for basename in scan.other_files:
            out.append(f"| {basename} | other | {git_created(repo, f'{root.path}/{basename}')} | n/a |")
            counts["files"] += 1
        for folder in scan.set_folders:
            out.append(f"| {folder}/ | set-folder | {git_created(repo, f'{root.path}/{folder}', True)} | yes |")
            counts["set folders"] += 1
        for folder in scan.exempt_subfolders:
            out.append(f"| {folder}/ | exempt | {git_created(repo, f'{root.path}/{folder}', True)} | n/a |")
        for folder in scan.subfolders:
            out.append(f"| {folder}/ | subfolder | {git_created(repo, f'{root.path}/{folder}', True)} | n/a |")
        out.append("")
        out.append("totals: " + ", ".join(f"{v} {k}" for k, v in counts.items()))
        out.append("")
        for key in totals:
            totals[key] += counts[key]
    out.append("## Repository totals")
    out.append("")
    out.append("totals: " + ", ".join(f"{v} {k}" for k, v in totals.items()))
    out.append("")
    if record.exempt_trees:
        out.append("## Exempt trees")
        out.append("")
        out.append("| file | class |")
        out.append("|---|---|")
        for tree, klass in record.exempt_trees.items():
            base = repo / tree
            if base.is_file():
                files = [base]
            elif base.is_dir():
                files = sorted(p for p in base.rglob("*.md") if p.is_file())
            else:
                files = []
            for path in files:
                out.append(f"| {relative_label(path, repo)} | {klass} |")
        out.append("")
    return out, 0


# ---------------------------------------------------------------------------
# --self-test (§7.4): mutate a temporary copy, prove a failure, restore, pass
# ---------------------------------------------------------------------------


def _tree_digest(repo: Path, config: Path, pin: Pin, record: Record) -> str:
    digest = hashlib.sha256()
    paths: list[Path] = [config / PIN_NAME, config / RECORD_NAME]
    paths += [repo / name for name in INSTRUCTION_FILES]
    for root in pin.roots:
        folder = repo / root.path
        if folder.is_dir():
            paths += sorted(p for p in folder.rglob("*") if p.is_file())
    for path in paths:
        if path.is_file():
            digest.update(path.as_posix().encode("utf-8", "replace"))
            digest.update(path.read_bytes())
    return digest.hexdigest()


def _copy_configured_tree(repo: Path, config: Path, pin: Pin, record: Record, target: Path) -> None:
    """The parts of the tree the check reads: config, roots, directive paths, the instruction files."""

    shutil.copytree(config, target / CONFIG_DIR_NAME, dirs_exist_ok=True)
    for root in pin.roots:
        source = repo / root.path
        if source.is_dir():
            shutil.copytree(source, target / root.path, dirs_exist_ok=True)
    for rel in [*record.exempt_subfolders, *record.exempt_trees, *record.held]:
        source, destination = repo / rel, target / rel
        if destination.exists():
            continue
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
        elif source.is_file():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
    for name in INSTRUCTION_FILES:
        if (repo / name).is_file():
            shutil.copy2(repo / name, target / name)


def _has(result: CheckResult, rule: str, path: str) -> bool:
    return any(v.rule == rule and v.path == path for v in result.violations)


def _rmtree(path: Path) -> None:
    def make_writable(function, target, _excinfo):
        os.chmod(target, 0o700)
        function(target)

    shutil.rmtree(path, onexc=make_writable)


def run_self_test(repo_root: os.PathLike[str] | str, config_dir: os.PathLike[str] | str | None = None) -> tuple[list[str], int]:
    repo = Path(repo_root).resolve()
    config = Path(config_dir).resolve() if config_dir else repo / CONFIG_DIR_NAME
    try:
        pin = load_pin(config / PIN_NAME)
        record = load_record(config / RECORD_NAME, repo, relative_label(config / RECORD_NAME, repo))
        validate_roots(repo, pin)
    except ConfigError as exc:
        return [f"repo-hygiene self-test: fail — could not run: {exc}"], 1
    if not pin.roots:
        return ["repo-hygiene self-test: fail — no declared root to plant in"], 1
    before = _tree_digest(repo, config, pin, record)
    out: list[str] = []
    defects = 0
    ok = True
    temp = Path(tempfile.mkdtemp(prefix="repo-hygiene-selftest-"))
    try:
        _copy_configured_tree(repo, config, pin, record, temp)
        copy_config = temp / CONFIG_DIR_NAME

        def check_copy() -> CheckResult:
            return run_check(temp, copy_config, disable_modules=True)

        def plant(rel: str, text: str, rule: str, label: str) -> bool:
            nonlocal defects
            path = temp / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
            found = _has(check_copy(), rule, rel)
            path.unlink()
            if found:
                defects += 1
                out.append(f"self-test: {rule} detected — {label}")
            else:
                out.append(f"repo-hygiene self-test: fail — {rule} not detected ({label})")
            return found

        first = pin.roots[0]
        planning = next((r for r in pin.roots if r.kind in ("planning", "general") and (repo / r.path).is_dir()), None)
        indexed = next((r for r in pin.roots if (repo / r.path / INDEX_NAME).is_file()), None)

        rel = f"{first.path}/undated-self-test-note.md"
        ok &= plant(rel, "# planted by --self-test\n", "name", rel)

        if indexed is None:
            out.append("repo-hygiene self-test: fail — index not plantable (no declared root has an INDEX.md)")
            ok = False
        else:
            rel = f"{indexed.path}/PLAN_self-test-unlisted_2026-01-01.md"
            ok &= plant(rel, "# planted by --self-test\n", "index", rel)
            folder = f"{indexed.path}/PLAN_self-test-set_2026-01-01"
            set_path = temp / folder
            set_path.mkdir(parents=True, exist_ok=True)
            (set_path / "00_INTRO.md").write_text("# planted by --self-test\n", encoding="utf-8", newline="\n")
            found = _has(check_copy(), "index", folder + "/")
            _rmtree(set_path)
            if found:
                defects += 1
                out.append(f"self-test: index detected — {folder}/ (set folder without an index line)")
            else:
                out.append(f"repo-hygiene self-test: fail — index not detected ({folder}/ set folder)")
                ok = False

        if planning is None:
            out.append("repo-hygiene self-test: fail — proof-argv/proof-prose not plantable (no planning or general root)")
            ok = False
        else:
            rel = f"{planning.path}/PROMPT_self-test-argv_2026-01-01.md"
            ok &= plant(rel, "# planted by --self-test\n\npython -m pytest -q tests\n", "proof-argv", f"{rel}:3")
            rel = f"{planning.path}/PROMPTS_self-test-prose_2026-01-01.md"
            ok &= plant(rel, "# planted by --self-test\n\nAlso run the full non-GUI suite to completion.\n", "proof-prose", f"{rel}:3")

        if not pin.rule_block:
            out.append("skipped: block-parity — rule block off in pin, nothing to plant")
        else:
            agents = temp / "AGENTS.md"
            block = None
            if agents.is_file() and (temp / "CLAUDE.md").is_file():
                block, _ = marked_block(read_text(agents))
            if not block or len(block) < 3:
                out.append("repo-hygiene self-test: fail — block-parity not plantable (no marked block with an interior in AGENTS.md)")
                ok = False
            else:
                original = agents.read_bytes()
                text = original.decode("utf-8", errors="replace")
                newline_at = text.index("\n", text.index(BEGIN_MARKER)) + 1
                agents.write_bytes((text[:newline_at] + "x" + text[newline_at:]).encode("utf-8"))
                found = _has(check_copy(), "block-parity", "AGENTS.md")
                if found:
                    defects += 1
                    out.append("self-test: block-parity detected — AGENTS.md (one byte changed inside the marked block)")
                else:
                    out.append("repo-hygiene self-test: fail — block-parity not detected (AGENTS.md)")
                    ok = False
                if "\r\n" in text:
                    flipped = text.replace("\r\n", "\n")
                else:
                    flipped = text.replace("\n", "\r\n")
                agents.write_bytes(flipped.encode("utf-8"))
                result = check_copy()
                agents.write_bytes(original)
                if _has(result, "block-parity", "AGENTS.md") or _has(result, "block-missing", "AGENTS.md"):
                    out.append("repo-hygiene self-test: fail — a line-endings-only difference in AGENTS.md was reported")
                    ok = False
                else:
                    out.append("self-test: line-endings-only difference not reported — AGENTS.md (as §5 requires)")
    finally:
        _rmtree(temp)

    after = _tree_digest(repo, config, pin, record)
    original = run_check(repo, config)
    out.append(f"self-test: original re-checked — {original.verdict}")
    if before != after:
        out.append("repo-hygiene self-test: fail — original tree changed during the self-test")
        return out, 1
    if original.exit_code != 0:
        out.extend(original.lines[:-1])
        out.append("repo-hygiene self-test: fail — original does not pass")
        return out, 1
    if not ok:
        return out, 1
    out.append(f"repo-hygiene self-test: pass — {defects} defects detected, original unchanged")
    return out, 0


# ---------------------------------------------------------------------------
# command line
# ---------------------------------------------------------------------------


def _parse(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="repo_hygiene_check.py",
        description="Repo Hygiene Template Kit checker — check (default), census, or --self-test.",
    )
    parser.add_argument("mode", nargs="?", choices=("check", "census"), default="check")
    parser.add_argument("--self-test", action="store_true", help="mutate a temporary copy, prove each rule fires, restore")
    parser.add_argument("--repo", help="the repository root (default: found from the current directory)")
    parser.add_argument("--config", help="a hygiene/ configuration directory elsewhere (default: <repo>/hygiene)")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    try:  # the same bytes on every platform: UTF-8 out, even through a Windows pipe
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
    except (AttributeError, ValueError):
        pass
    args = _parse(sys.argv[1:] if argv is None else argv)
    if args.mode == "census" and args.self_test:
        print("repo-hygiene: error — could not run: --self-test does not combine with census")
        return 2
    cwd = Path.cwd()
    if args.repo:
        repo = Path(args.repo).resolve()
        if not repo.is_dir():
            print(f"repo-hygiene: error — could not run: --repo {args.repo} is not a directory")
            return 2
    elif args.config:
        repo = find_git_root(cwd) or cwd
    else:
        found = find_repository(cwd)
        if found is None:
            print(f"repo-hygiene: error — could not run: no {CONFIG_DIR_NAME}/{PIN_NAME} in {cwd.as_posix()} or any parent")
            return 2
        repo = found
    config = Path(args.config).resolve() if args.config else repo / CONFIG_DIR_NAME

    if args.self_test:
        lines, code = run_self_test(repo, config)
    elif args.mode == "census":
        lines, code = run_census(repo, config)
    else:
        result = run_check(repo, config)
        lines, code = result.lines, result.exit_code
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main())
