"""Check the harness mirrors of the superproject and its submodules for drift.

PlantLibrary variant, trimmed from the Orchestrator_System original and
extended for the multi-root layout (RC-A2-08, RC-A1-21, Q-A2-04 (a) assumed;
AUDIT_skills-and-agents §7.7 items 1, 2, 5, 8). Four checks:

1. Codex compare (``--with-codex-compare``, on by default until B7-2 switches
   it): the superproject's ``.claude/skills`` against ``.codex/skills`` file by
   file, ``validate-real-stack/SKILL.md`` allowed to differ, and the agent stem
   pairing ``.claude/agents/*.md`` <-> ``.codex/agents/*.toml``.
2. Suite mirrors: in each present submodule folder named by ``.gitmodules``,
   the shared skill folders (``SHARED_SKILLS`` plus the suite's row of
   ``SUITE_EXTRA_SKILLS``) and every superproject ``.claude/agents/*.md`` must
   equal the superproject's copy. A suite skill folder of the same name that is
   not in that set is listed, not compared (RC-A1-22 moves it in at B1).
3. Run-batch commit contract: every ``run-batch/SKILL.md`` copy under any
   ``.claude/skills`` or ``.codex/skills`` of a present repository holds the
   four commit-proposal strings and neither retired string.
4. Roots: a submodule folder that is absent or not checked out is skipped with
   a printed line, so a standalone suite clone does not fail.

Every content compare normalizes CRLF to LF first (the ``run-batch/SKILL.md``
mirrors are mixed in every repository; working-tree endings follow checkout).
``__pycache__/`` is ignored. ``--self-test`` is a static mode over temporary
copies: it plants one drift per check, proves each is reported, proves that a
CRLF<->LF flip is not reported, restores the copy, then checks the real tree.

Read-only, stdlib only, dependency-free so it runs in either coding harness on
Windows. Exit 0 pass, 1 drift, 2 could not run.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import tempfile  # noqa: E402
from dataclasses import dataclass, field  # noqa: E402
from pathlib import Path  # noqa: E402


ALLOWED_SKILL_DIFFERENCES = frozenset({"validate-real-stack/SKILL.md"})
SHARED_SKILLS = (
    "plan-batch",
    "real-stack-testing",
    "run-batch",
    "test-driven-development",
    "validate-real-stack",
)
# RC-A1-22 (B1, after Q-A1-04 / Q-G-07): PlantLibrary-only skills mirrored into a
# suite join its row here in the same commit that mirrors them.
SUITE_EXTRA_SKILLS: dict[str, tuple[str, ...]] = {}
RUN_BATCH_REQUIRED = (
    "Propose the commit — never mutate Git",
    "Do not run `git add`, `git commit`, `git push`, `git reset`",
    "Commit: proposed for orchestrator",
    "CONDUCTOR_BATCH_COMMIT_PROPOSAL: <canonical-json>",
)
RUN_BATCH_FORBIDDEN = (
    "Commit: skipped: sandbox-protected Git metadata",
    "Commit command:",
)
IGNORED_PARTS = frozenset({"__pycache__"})
VERDICT = "harness parity"


@dataclass(frozen=True)
class ParityResult:
    """The deterministic diagnostics produced by one parity comparison."""

    diagnostics: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.diagnostics


@dataclass
class Report:
    diagnostics: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    suites: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.diagnostics


def repository_root() -> Path:
    """Return the superproject root independently of the current directory."""

    return Path(__file__).resolve().parents[2]


def _lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def _file_inventory(root: Path) -> dict[str, bytes]:
    if not root.is_dir():
        raise FileNotFoundError(f"missing directory: {root}")
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file() and not IGNORED_PARTS.intersection(path.relative_to(root).parts)
    }


def _agent_stems(root: Path, suffix: str) -> set[str]:
    if not root.is_dir():
        raise FileNotFoundError(f"missing directory: {root}")
    return {path.stem for path in root.glob(f"*{suffix}") if path.is_file()}


def compare_trees(root: Path) -> ParityResult:
    """The superproject's ``.claude``/``.codex`` compare: skills by LF content, agents by stem."""

    claude_skills = _file_inventory(root / ".claude" / "skills")
    codex_skills = _file_inventory(root / ".codex" / "skills")
    diagnostics: list[str] = []

    for relative_path in sorted(set(claude_skills) | set(codex_skills)):
        in_claude = relative_path in claude_skills
        in_codex = relative_path in codex_skills
        if not in_claude:
            diagnostics.append(f"skill missing from Claude: {relative_path}")
        elif not in_codex:
            diagnostics.append(f"skill missing from Codex: {relative_path}")
        elif (
            _lf(claude_skills[relative_path]) != _lf(codex_skills[relative_path])
            and relative_path not in ALLOWED_SKILL_DIFFERENCES
        ):
            diagnostics.append(f"skill byte-different: {relative_path}")

    claude_agents = _agent_stems(root / ".claude" / "agents", ".md")
    codex_agents = _agent_stems(root / ".codex" / "agents", ".toml")
    for stem in sorted(claude_agents - codex_agents):
        diagnostics.append(f"agent missing from Codex: {stem}")
    for stem in sorted(codex_agents - claude_agents):
        diagnostics.append(f"agent missing from Claude: {stem}")

    return ParityResult(tuple(diagnostics))


def submodule_folders(root: Path) -> list[str]:
    gitmodules = root / ".gitmodules"
    if not gitmodules.is_file():
        return []
    names = []
    for line in gitmodules.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*path\s*=\s*(.+?)\s*$", line)
        if match:
            names.append(match.group(1))
    return sorted(names)


def compare_suite(
    root: Path, suite: str, extra_skills: dict[str, tuple[str, ...]]
) -> tuple[list[str], list[str]]:
    """One suite's shared skill folders and agents against the superproject's (LF content)."""

    diagnostics: list[str] = []
    notes: list[str] = []
    super_skills = root / ".claude" / "skills"
    suite_skills = root / suite / ".claude" / "skills"
    compared = tuple(SHARED_SKILLS) + tuple(extra_skills.get(suite, ()))
    for skill in compared:
        source = super_skills / skill
        mirror = suite_skills / skill
        if not source.is_dir():
            diagnostics.append(f"{suite}: superproject has no skill folder {skill}")
            continue
        if not mirror.is_dir():
            diagnostics.append(f"{suite}: missing shared skill folder {skill}")
            continue
        expected = _file_inventory(source)
        actual = _file_inventory(mirror)
        for relative in sorted(set(expected) | set(actual)):
            if relative not in actual:
                diagnostics.append(f"{suite}: skill file missing: {skill}/{relative}")
            elif relative not in expected:
                diagnostics.append(f"{suite}: skill file not in the superproject: {skill}/{relative}")
            elif _lf(expected[relative]) != _lf(actual[relative]):
                diagnostics.append(f"{suite}: skill differs from the superproject's: {skill}/{relative}")
    if suite_skills.is_dir():
        uncompared = sorted(
            p.name
            for p in suite_skills.iterdir()
            if p.is_dir() and p.name not in compared and (super_skills / p.name).is_dir()
        )
        if uncompared:
            notes.append(f"{suite}: same-name skill folders listed, not compared: {', '.join(uncompared)}")

    super_agents = root / ".claude" / "agents"
    suite_agents = root / suite / ".claude" / "agents"
    for agent in sorted(super_agents.glob("*.md")):
        mirror = suite_agents / agent.name
        if not mirror.is_file():
            diagnostics.append(f"{suite}: agent missing: {agent.name}")
        elif _lf(mirror.read_bytes()) != _lf(agent.read_bytes()):
            diagnostics.append(f"{suite}: agent differs from the superproject's: {agent.name}")
    if suite_agents.is_dir():
        extra = sorted(
            p.name for p in suite_agents.glob("*.md") if not (super_agents / p.name).is_file()
        )
        if extra:
            notes.append(f"{suite}: suite-only agents listed, not compared: {', '.join(extra)}")
    return diagnostics, notes


def check_run_batch_contract(repository: Path, label: str) -> list[str]:
    """The commit-proposal strings in every run-batch copy of one repository (RC-A1-21)."""

    diagnostics: list[str] = []
    for harness in (".claude", ".codex"):
        path = repository / harness / "skills" / "run-batch" / "SKILL.md"
        if not path.is_file():
            continue
        text = _lf(path.read_bytes()).decode("utf-8", "replace")
        where = f"{label}{harness}/skills/run-batch/SKILL.md"
        for needle in RUN_BATCH_REQUIRED:
            if needle not in text:
                diagnostics.append(f"run-batch commit contract: {where} lacks {needle!r}")
        for needle in RUN_BATCH_FORBIDDEN:
            if needle in text:
                diagnostics.append(f"run-batch commit contract: {where} carries retired {needle!r}")
    return diagnostics


def check_all(
    root: Path,
    with_codex_compare: bool = True,
    extra_skills: dict[str, tuple[str, ...]] | None = None,
) -> Report:
    extras = SUITE_EXTRA_SKILLS if extra_skills is None else extra_skills
    report = Report()
    if with_codex_compare:
        report.diagnostics.extend(compare_trees(root).diagnostics)
    else:
        report.notes.append("codex compare off (--no-with-codex-compare)")
    report.diagnostics.extend(check_run_batch_contract(root, ""))
    for suite in submodule_folders(root):
        folder = root / suite
        if not (folder.is_dir() and (folder / ".git").exists()):
            report.skipped.append(suite)
            continue
        report.suites.append(suite)
        diagnostics, notes = compare_suite(root, suite, extras)
        report.diagnostics.extend(diagnostics)
        report.notes.extend(notes)
        report.diagnostics.extend(check_run_batch_contract(folder, f"{suite}/"))
    return report


def _print_report(report: Report, with_codex_compare: bool) -> int:
    for suite in report.skipped:
        print(f"{VERDICT}: skipped {suite} (submodule folder not present)")
    for note in report.notes:
        print(f"{VERDICT}: note: {note}")
    for diagnostic in report.diagnostics:
        print(f"{VERDICT}: FAIL: {diagnostic}")
    scope = (
        f"{1 + len(report.suites)} repositories (superproject + {len(report.suites)} suites,"
        f" {len(report.skipped)} skipped); codex compare {'on' if with_codex_compare else 'off'};"
        f" {len(SHARED_SKILLS)} shared skills + agents per suite; run-batch commit contract"
    )
    if report.ok:
        print(f"{VERDICT}: pass — {scope}")
        return 0
    print(f"{VERDICT}: fail — {len(report.diagnostics)} diagnostics; {scope}")
    return 1


def _copy_mirrors(source_root: Path, target_root: Path) -> None:
    ignore = shutil.ignore_patterns("__pycache__")
    target_root.mkdir(parents=True)
    shutil.copy2(source_root / ".gitmodules", target_root / ".gitmodules")
    for harness in (".claude", ".codex"):
        for part in ("skills", "agents"):
            if (source_root / harness / part).is_dir():
                shutil.copytree(source_root / harness / part, target_root / harness / part, ignore=ignore)
    for suite in submodule_folders(source_root):
        folder = source_root / suite
        if not (folder.is_dir() and (folder / ".git").exists()):
            continue
        (target_root / suite).mkdir()
        (target_root / suite / ".git").write_text("gitdir: self-test copy\n", encoding="utf-8")
        for harness in (".claude", ".codex"):
            for part in ("skills", "agents"):
                if (folder / harness / part).is_dir():
                    shutil.copytree(folder / harness / part, target_root / suite / harness / part, ignore=ignore)


def _flip_line_endings(data: bytes) -> bytes:
    if b"\r\n" in data:
        return data.replace(b"\r\n", b"\n")
    return data.replace(b"\n", b"\r\n")


def run_self_test(source_root: Path, with_codex_compare: bool) -> int:
    """Plant one drift per check in a temporary copy, prove each is caught, restore, pass."""

    suites = [
        s
        for s in submodule_folders(source_root)
        if (source_root / s).is_dir() and (source_root / s / ".git").exists()
    ]
    if not suites:
        print(f"{VERDICT} self-test: error — no submodule folder present to plant suite drifts in")
        return 2
    suite = suites[0]
    failures: list[str] = []
    detected: list[str] = []
    with tempfile.TemporaryDirectory(prefix="harness-parity-") as temporary:
        copy = Path(temporary) / "repository"
        _copy_mirrors(source_root, copy)
        baseline = check_all(copy, with_codex_compare)
        base_set = set(baseline.diagnostics)

        def plant(name: str, path: Path, mutate, expected: str, *, extras=None, absent=False) -> None:
            backup = Path(temporary) / "backup"
            was_dir = path.is_dir()
            original = b""
            if was_dir:
                shutil.copytree(path, backup)
            else:
                original = path.read_bytes()
            mutate(path)
            result = check_all(copy, with_codex_compare, extras)
            new = [d for d in result.diagnostics if d not in base_set]
            if absent:
                ok = not new and expected in result.skipped
                label = f"{name}: skipped {expected}, no diagnostic"
            else:
                ok = any(expected in d for d in new)
                label = f"{name}: {expected}"
            (detected if ok else failures).append(label)
            if was_dir:
                if path.exists():
                    shutil.rmtree(path)
                shutil.copytree(backup, path)
                shutil.rmtree(backup)
            else:
                path.write_bytes(original)
            restored = check_all(copy, with_codex_compare)
            if set(restored.diagnostics) != base_set:
                failures.append(f"{name}: restored copy differs from the baseline")

        skills = copy / suite / ".claude" / "skills"
        agents = copy / suite / ".claude" / "agents"
        append = lambda p: p.write_bytes(p.read_bytes() + b"\n<!-- temporary one-sided drift -->\n")  # noqa: E731

        if with_codex_compare:
            plant("codex compare", copy / ".claude" / "skills" / "run-batch" / "SKILL.md", append,
                  "skill byte-different: run-batch/SKILL.md")
        plant("suite skill", skills / "plan-batch" / "SKILL.md", append,
              f"{suite}: skill differs from the superproject's: plan-batch/SKILL.md")
        plant("suite skill folder", skills / "test-driven-development", shutil.rmtree,
              f"{suite}: missing shared skill folder test-driven-development")
        first_agent = sorted((copy / ".claude" / "agents").glob("*.md"))[0].name
        plant("suite agent", agents / first_agent, append,
              f"{suite}: agent differs from the superproject's: {first_agent}")
        plant("suite agent missing", agents / first_agent, lambda p: p.unlink(),
              f"{suite}: agent missing: {first_agent}")
        plant("extra-skill table", skills / "plan-batch" / "SKILL.md", lambda p: None,
              f"{suite}: missing shared skill folder systematic-debugging",
              extras={suite: ("systematic-debugging",)})
        plant("run-batch required string", skills / "run-batch" / "SKILL.md",
              lambda p: p.write_bytes(p.read_bytes().replace(b"Commit: proposed for orchestrator", b"Commit: x")),
              f"{suite}/.claude/skills/run-batch/SKILL.md lacks 'Commit: proposed for orchestrator'")
        plant("run-batch retired string", copy / ".codex" / "skills" / "run-batch" / "SKILL.md",
              lambda p: p.write_bytes(p.read_bytes() + b"\nCommit command:\n"),
              ".codex/skills/run-batch/SKILL.md carries retired 'Commit command:'")
        plant("multi-root skip", copy / suite / ".git", lambda p: p.unlink(), suite, absent=True)

        # A CRLF<->LF flip of a mirrored file is not drift.
        target = skills / "run-batch" / "SKILL.md"
        original = target.read_bytes()
        target.write_bytes(_flip_line_endings(original))
        flipped = check_all(copy, with_codex_compare)
        if set(flipped.diagnostics) != base_set:
            failures.append("LF normalization: a CRLF<->LF flip was reported as drift")
        else:
            detected.append("LF normalization: a CRLF<->LF flip of run-batch/SKILL.md is not drift")
        target.write_bytes(original)

    for line in detected:
        print(f"{VERDICT} self-test: ok: {line}")
    for line in failures:
        print(f"{VERDICT} self-test: FAILED: {line}")
    if failures:
        print(f"{VERDICT} self-test: fail — {len(failures)} of {len(failures) + len(detected)} plants")
        return 1
    print(
        f"{VERDICT} self-test: pass — {len(detected)} plants proven (suite {suite});"
        " restored copy equals the baseline"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="plant one drift per check in a temporary copy, then check the real tree",
    )
    parser.add_argument(
        "--with-codex-compare",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="compare the superproject's .claude with .codex (default on until B7-2)",
    )
    arguments = parser.parse_args()
    root = repository_root()
    if not (root / ".claude" / "skills").is_dir():
        print(f"{VERDICT}: error — could not run: no .claude/skills under {root}")
        return 2
    try:
        if arguments.self_test:
            self_code = run_self_test(root, arguments.with_codex_compare)
            real_code = _print_report(check_all(root, arguments.with_codex_compare), arguments.with_codex_compare)
            return max(self_code, real_code)
        return _print_report(check_all(root, arguments.with_codex_compare), arguments.with_codex_compare)
    except FileNotFoundError as error:
        print(f"{VERDICT}: error — could not run: {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
