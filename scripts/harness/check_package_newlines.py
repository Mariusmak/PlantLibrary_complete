"""Check that no batch-package contract file mixes CRLF and LF line endings.

A static guard (RC-A2-13), adapted from the Conductor's package newline rule
(``tests/test_repo_hygiene.py:216-275`` at ``2e7adb3``): a package write must
keep the file's existing line-ending style (kickoff rule 8, run-batch §7), so a
contract file holding both styles is the trace of a text-mode rewrite.

Scope. The superproject and every submodule folder named in ``.gitmodules``
that is present (holds a ``.git`` entry). Per repository, the git-tracked
files are read with ``git --no-optional-locks ls-files``; untracked files and
anything under ``.tmp/`` are never scanned. A package is a tracked folder that
holds a tracked ``BATCH_PLAN.md``. Its contract files are the tracked ones of
``CONTRACT_FILE_NAMES``, read as bytes from the working tree.

Counted versus listed. The seven live packages (``LIVE_PACKAGES``) and any
package this file does not classify are counted. Frozen MVP packages,
``Archive_PreMVP`` packages, archive packages and the frozen Workspace trees
are listed with their counts but never change the exit code.

Read-only: nothing is written, nothing is fixed. Stdlib only.
Exit 0 no mixed contract file in a counted package, 1 at least one,
2 could not run (no git, a repository that does not answer).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

sys.dont_write_bytecode = True

CONTRACT_FILE_NAMES = (
    "README.md",
    "SCOPE.md",
    "CONTEXT_INDEX.md",
    "BATCH_PLAN.md",
    "TASK_CHECKLIST.md",
    "TASK_CONTEXT.md",
    "STATE.md",
)

# (repository folder, package path) of the seven live packages; "." is the superproject.
LIVE_PACKAGES = frozenset(
    {
        ("PlantLibrary_AndroidApp", "implementation/System_V1_Implementation"),
        ("PlantLibrary_AndroidApp", "implementation/Design_Migration_V1"),
        ("PlantLibrary_Dashboard", "implementation/System_V1_Implementation"),
        ("PlantLibrary_Dashboard", "implementation/Design_Migration_V1"),
        ("PlantLibrary_PyApp", "implementation/System_V1_Implementation"),
        ("PlantLibrary_PyApp", "implementation/Design_Migration_V1"),
        ("PlantLibrary_Server", "implementation/System_V1_Implementation"),
        ("PlantLibrary_SharedContracts", "implementation/System_V1_Implementation"),
        ("PlantLibrary_Workspace", "implementation/System_V1_Implementation"),
        ("PlantLibrary_Workspace", "implementation/System_Design_Architecture"),
    }
)

# Frozen Workspace trees that are neither MVP nor archive by name (AUDIT_batch-packages §7.1).
FROZEN_PREFIXES: dict[tuple[str, str], str] = {
    ("PlantLibrary_Workspace", "implementation/System_Tooling"): "frozen Workspace package",
    ("PlantLibrary_Workspace", "strategy/"): "frozen Workspace strategy tree",
    ("PlantLibrary_Workspace", "system_description/"): "frozen Workspace system_description tree",
}

VERDICT = "package-newlines"


@dataclass
class PackageReport:
    repository: str
    path: str
    status: str  # "live", "unclassified (counted)" or a not-counted reason
    counted: bool
    files: int = 0
    crlf_files: int = 0
    lf_files: int = 0
    mixed: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)


class CouldNotRun(Exception):
    """A repository or git did not answer: exit 2."""


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def repositories(root: Path) -> tuple[list[tuple[str, Path]], list[str]]:
    """The superproject plus each present submodule folder; and the skipped ones."""

    present: list[tuple[str, Path]] = [(".", root)]
    skipped: list[str] = []
    gitmodules = root / ".gitmodules"
    names: list[str] = []
    if gitmodules.is_file():
        for line in gitmodules.read_text(encoding="utf-8").splitlines():
            match = re.match(r"\s*path\s*=\s*(.+?)\s*$", line)
            if match:
                names.append(match.group(1))
    for name in sorted(names):
        folder = root / name
        if folder.is_dir() and (folder / ".git").exists():
            present.append((name, folder))
        else:
            skipped.append(name)
    return present, skipped


def tracked_files(repository: Path) -> list[str]:
    try:
        completed = subprocess.run(
            ["git", "-C", str(repository), "--no-optional-locks", "ls-files", "-z"],
            capture_output=True,
            check=False,
        )
    except OSError as error:
        raise CouldNotRun(f"git not runnable: {error}") from error
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", "replace").strip()
        raise CouldNotRun(f"git ls-files failed in {repository}: {message}")
    return [p for p in completed.stdout.decode("utf-8").split("\0") if p]


def mixed_newline_line(data: bytes) -> int | None:
    """The 1-based line of the first newline whose ending is the minority style.

    Same rule as the Conductor's: only CRLF, only bare LF, or no newline at all
    is not mixed (``None``); both styles is mixed, the majority is whichever
    occurs more often (CRLF on a tie), and the first disagreeing line is named.
    """

    endings: list[bool] = []
    index = 0
    while True:
        newline_at = data.find(b"\n", index)
        if newline_at == -1:
            break
        endings.append(newline_at > index and data[newline_at - 1] == 0x0D)
        index = newline_at + 1
    crlf_count = sum(1 for is_crlf in endings if is_crlf)
    lf_count = len(endings) - crlf_count
    if crlf_count == 0 or lf_count == 0:
        return None
    majority_is_crlf = crlf_count >= lf_count
    for line_number, is_crlf in enumerate(endings, start=1):
        if is_crlf != majority_is_crlf:
            return line_number
    return None


def classify(repository: str, package: str) -> tuple[str, bool]:
    if (repository, package) in LIVE_PACKAGES:
        return "live", True
    parts = PurePosixPath(package).parts
    if any(part == "Archive_PreMVP" for part in parts):
        return "Archive_PreMVP (not counted)", False
    if any(part.lower() == "archive" for part in parts):
        return "archive (not counted)", False
    if any(part == "MVP" or part.endswith("_MVP") for part in parts):
        return "frozen MVP (not counted)", False
    for (repo, prefix), reason in FROZEN_PREFIXES.items():
        if repo == repository and (package == prefix.rstrip("/") or package.startswith(prefix.rstrip("/") + "/")):
            return f"{reason} (not counted)", False
    return "unclassified (counted)", True


def scan_repository(name: str, folder: Path) -> list[PackageReport]:
    tracked = [p for p in tracked_files(folder) if not p.startswith(".tmp/")]
    tracked_set = set(tracked)
    packages = sorted(
        {str(PurePosixPath(p).parent) for p in tracked if PurePosixPath(p).name == "BATCH_PLAN.md"}
    )
    reports: list[PackageReport] = []
    for package in packages:
        status, counted = classify(name, package)
        report = PackageReport(name, package, status, counted)
        for file_name in CONTRACT_FILE_NAMES:
            relative = file_name if package == "." else f"{package}/{file_name}"
            if relative not in tracked_set:
                continue
            path = folder / relative
            if not path.is_file():
                report.missing.append(relative)
                continue
            data = path.read_bytes()
            report.files += 1
            if b"\r\n" in data:
                report.crlf_files += 1
            else:
                report.lf_files += 1
            line = mixed_newline_line(data)
            if line is not None:
                report.mixed.append(f"{relative}:{line}")
        reports.append(report)
    return reports


def main() -> int:
    argparse.ArgumentParser(description=__doc__.splitlines()[0]).parse_args()
    root = repository_root()
    present, skipped = repositories(root)
    reports: list[PackageReport] = []
    try:
        for name, folder in present:
            reports.extend(scan_repository(name, folder))
    except CouldNotRun as error:
        print(f"{VERDICT}: error — could not run: {error}")
        return 2

    for name in skipped:
        print(f"{VERDICT}: skipped {name} (submodule folder not present)")
    for report in reports:
        label = report.path if report.repository == "." else f"{report.repository}/{report.path}"
        print(
            f"  {label}: {report.status} · {report.files} contract files"
            f" (CRLF {report.crlf_files}, LF {report.lf_files}) · mixed {len(report.mixed)}"
        )
        for item in report.mixed:
            print(f"      mixed: {item}")
        for item in report.missing:
            print(f"      tracked but missing on disk: {item}")

    counted = [r for r in reports if r.counted]
    listed = [r for r in reports if not r.counted]
    live_found = {(r.repository, r.path) for r in reports if r.status == "live"}
    absent_live = sorted(
        f"{repo}/{path}"
        for repo, path in LIVE_PACKAGES
        if (repo, path) not in live_found and repo not in skipped
    )
    for label in absent_live:
        print(f"      live package not found: {label}")
    counted_mixed = sum(len(r.mixed) for r in counted)
    counted_missing = sum(len(r.missing) for r in counted)
    listed_mixed = sum(len(r.mixed) for r in listed)
    counted_files = sum(r.files for r in counted)
    summary = (
        f"{len(counted)} counted packages ({counted_files} contract files) over"
        f" {len(present)} repositories, {len(skipped)} skipped; {len(listed)} not-counted"
        f" packages listed ({listed_mixed} mixed there)"
    )
    if counted_mixed or counted_missing or absent_live:
        print(
            f"{VERDICT}: fail — {counted_mixed} mixed contract files, {counted_missing} missing,"
            f" {len(absent_live)} live packages not found; {summary}"
        )
        return 1
    print(f"{VERDICT}: pass — 0 mixed contract files in {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
