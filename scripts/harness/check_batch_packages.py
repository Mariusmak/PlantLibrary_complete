"""Census of every PlantLibrary batch package through the Conductor's real parser.

A static check (RC-A2-09): each package folder is handed to
``conductor.batch_package.parse_package`` and the result is printed; nothing
is written. The verdict names its parser, because the parser decides it
(F-A7-02: an editable install of the Conductor's main checkout shadows any
fallback, so a run judged by main's parser, not instance 2's, unless told).

Parser resolution, in this order:

1. ``--parser-src <path>`` -- a ``src`` folder holding ``conductor/``, put first
   on ``sys.path``; the run refuses (exit 2) if the imported module is not
   under it. Instance 2's is ``C:\\Programs\\AI_Orchestrator_2\\src``.
2. the ``conductor`` package importable by this interpreter;
3. ``CONDUCTOR_SRC``, else instance 2's ``src``, as a last fallback.

Provenance printed: the parser module's file path; the git checkout and commit
it lies in (read with ``git --no-optional-locks`` only), or the instance's
``_sync_stamp.json`` when the parser is a synced copy without git.

Bytecode is never written (``sys.dont_write_bytecode`` is set before the
import; run the interpreter with ``-B`` as well). The seven live packages and
any unclassified package are counted; the four frozen Workspace packages are
listed and never change the exit code.

Exit 0 every counted package parses with 0 errors, 1 a counted package has
errors or a live package is missing, 2 could not run (no parser).
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import collections  # noqa: E402
import importlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import subprocess  # noqa: E402
from pathlib import Path  # noqa: E402

INSTANCE_2_SRC = Path(r"C:\Programs\AI_Orchestrator_2\src")
ROOT = Path(__file__).resolve().parents[2]
VERDICT = "batch-packages"

# (repository folder, package path) relative to the superproject.
LIVE_PACKAGES = (
    "PlantLibrary_AndroidApp/implementation/System_V1_Implementation",
    "PlantLibrary_AndroidApp/implementation/Design_Migration_V1",
    "PlantLibrary_Dashboard/implementation/System_V1_Implementation",
    "PlantLibrary_PyApp/implementation/System_V1_Implementation",
    "PlantLibrary_Server/implementation/System_V1_Implementation",
    "PlantLibrary_SharedContracts/implementation/System_V1_Implementation",
    "PlantLibrary_Workspace/implementation/System_V1_Implementation",
    "PlantLibrary_Workspace/implementation/System_Design_Architecture",
)
FROZEN_PACKAGES = (
    "PlantLibrary_Workspace/implementation/System_Integration_MVP",
    "PlantLibrary_Workspace/implementation/System_Tooling",
    "PlantLibrary_Workspace/strategy/Cross_Platform_Strategy",
    "PlantLibrary_Workspace/system_description/PlantLibrary_System_Description",
)
# Folders scanned: every child of these that holds a TASK_CHECKLIST.md.
SCAN_PARENTS = (
    ("PlantLibrary_*", "implementation"),
    ("PlantLibrary_Workspace", "strategy"),
    ("PlantLibrary_Workspace", "system_description"),
)
KINDS = (
    "no 15-column",
    "declares missing primary row",
    "outside the first sentence",
    "missing required file",
    "has no goal",
    "no context anchor",
    "does not match checklist",
    "invalid status",
    "cells, expected",
    "duplicate",
    "unsafe output path",
)


class CouldNotRun(Exception):
    """No parser could be imported: exit 2."""


def _git(directory: Path, *arguments: str) -> str | None:
    try:
        completed = subprocess.run(
            ["git", "-C", str(directory), "--no-optional-locks", *arguments],
            capture_output=True,
            check=False,
        )
    except OSError:
        return None
    if completed.returncode != 0:
        return None
    return completed.stdout.decode("utf-8", "replace").strip()


def load_parser(parser_src: str | None):
    """Import ``conductor.batch_package`` per the resolution order; return the module."""

    if parser_src:
        source = Path(parser_src).resolve()
        if not (source / "conductor" / "batch_package.py").is_file():
            raise CouldNotRun(f"--parser-src {source} holds no conductor/batch_package.py")
        sys.path.insert(0, str(source))
        module = importlib.import_module("conductor.batch_package")
        imported = Path(module.__file__).resolve()
        if source not in imported.parents:
            raise CouldNotRun(
                f"--parser-src {source} was shadowed: conductor imported from {imported}"
            )
        return module
    try:
        return importlib.import_module("conductor.batch_package")
    except ImportError:
        fallback = Path(os.environ.get("CONDUCTOR_SRC", str(INSTANCE_2_SRC)))
        if not (fallback / "conductor" / "batch_package.py").is_file():
            raise CouldNotRun(
                "no conductor package importable and no fallback src at "
                f"{fallback}; pass --parser-src <src>"
            ) from None
        sys.path.insert(0, str(fallback))
        return importlib.import_module("conductor.batch_package")


def provenance(module) -> list[str]:
    module_file = Path(module.__file__).resolve()
    lines = [f"parser: {module_file}"]
    package_dir = module_file.parent
    toplevel = _git(package_dir, "rev-parse", "--show-toplevel")
    if toplevel:
        head = _git(package_dir, "rev-parse", "--short", "HEAD") or "unreadable"
        branch = _git(package_dir, "rev-parse", "--abbrev-ref", "HEAD") or "?"
        dirty = _git(package_dir, "status", "--porcelain", "--", str(module_file))
        state = "parser file differs from HEAD" if dirty else "parser file clean at HEAD"
        lines.append(f"parser checkout: {toplevel} @ {head} ({branch}; {state})")
    else:
        lines.append("parser checkout: not a git checkout")
    stamp = package_dir / "_sync_stamp.json"
    if stamp.is_file():
        try:
            data = json.loads(stamp.read_text(encoding="utf-8-sig"))
            commit = str(data.get("synced_from_commit", "?"))[:7]
            lines.append(
                f"parser stamp: {data.get('version', '?')} synced from {commit}"
                f" at {data.get('synced_at', '?')}"
            )
        except (OSError, ValueError) as error:
            lines.append(f"parser stamp: unreadable ({error})")
    elif not toplevel:
        lines.append("parser commit: not readable (no git checkout, no _sync_stamp.json)")
    return lines


def package_folders() -> list[Path]:
    folders: set[Path] = set()
    for repository_glob, parent in SCAN_PARENTS:
        for repository in ROOT.glob(repository_glob):
            base = repository / parent
            if not base.is_dir():
                continue
            for child in base.iterdir():
                if child.is_dir() and (child / "TASK_CHECKLIST.md").is_file():
                    folders.add(child)
    return sorted(folders)


def main() -> int:
    arguments = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    arguments.add_argument(
        "--parser-src",
        metavar="PATH",
        help="a src folder holding conductor/ (e.g. instance 2's) to judge with",
    )
    options = arguments.parse_args()
    try:
        module = load_parser(options.parser_src)
    except CouldNotRun as error:
        print(f"{VERDICT}: error — could not run: {error}")
        return 2
    for line in provenance(module):
        print(line)
    parse_package = module.parse_package

    counted_errors = 0
    counted = 0
    batches = rows = 0
    listed: list[tuple[str, int]] = []
    seen: set[str] = set()
    for folder in package_folders():
        short = folder.relative_to(ROOT).as_posix()
        seen.add(short)
        frozen = short in FROZEN_PACKAGES
        tag = "frozen, not counted" if frozen else ("live" if short in LIVE_PACKAGES else "unclassified, counted")
        result = parse_package(str(folder))
        if isinstance(result, list):
            kinds: collections.Counter[str] = collections.Counter()
            for error in result:
                kinds[next((k for k in KINDS if k in error.message), error.message[:60])] += 1
            print(f"{short} [{tag}]: {len(result)} errors -> {dict(kinds)}")
            details = [
                e.message
                for e in result
                if not any(k in e.message for k in ("no 15-column", "declares missing"))
            ]
            for message in details[:8]:
                print(f"    {message[:160]}")
            if len(details) > 8:
                print(f"    … {len(details) - 8} more")
            if frozen:
                listed.append((short, len(result)))
            else:
                counted += 1
                counted_errors += len(result)
        else:
            classes = ", ".join(f"{b.key}={b.classification}" for b in result.batches)
            print(
                f"{short} [{tag}]: OK {len(result.batches)} batches {len(result.rows)} rows :: {classes}"
            )
            if frozen:
                listed.append((short, 0))
            else:
                counted += 1
                batches += len(result.batches)
                rows += len(result.rows)

    missing_live = [p for p in LIVE_PACKAGES if p not in seen]
    for short in missing_live:
        print(f"{short} [live]: missing (no folder with TASK_CHECKLIST.md)")
    listed_errors = sum(n for _, n in listed)
    parser_path = Path(module.__file__).resolve()
    summary = (
        f"{counted} counted packages ({batches} batches, {rows} rows parsed clean);"
        f" {len(listed)} frozen packages listed, {listed_errors} errors there not counted;"
        f" parser {parser_path}"
    )
    if counted_errors or missing_live:
        print(
            f"{VERDICT}: fail — {counted_errors} errors, {len(missing_live)} live packages missing; {summary}"
        )
        return 1
    print(f"{VERDICT}: pass — 0 errors in {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
