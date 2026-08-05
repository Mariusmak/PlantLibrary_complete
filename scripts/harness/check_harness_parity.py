"""Check the mirrored Claude and Codex harness trees for unintended drift.

PlantLibrary workspace variant, trimmed from the Orchestrator_System original:
it byte-checks the `.claude`/`.codex` skill mirrors and the agent stem pairing
only — this workspace has no CLAUDE.md/AGENTS.md shared-block contract or
proposal-fact citations to verify. The one allowed runtime-specific skill file
is deliberately listed below. Keep this checker dependency-free so it can run
in either coding harness on Windows.

This is a manual pre-commit step, not a hook — nothing runs it automatically.
"""

from __future__ import annotations

import argparse
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path


ALLOWED_SKILL_DIFFERENCES = frozenset({"validate-real-stack/SKILL.md"})


@dataclass(frozen=True)
class ParityResult:
    """The deterministic diagnostics produced by one parity comparison."""

    diagnostics: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.diagnostics


def repository_root() -> Path:
    """Return the repository root independently of the current directory."""

    return Path(__file__).resolve().parents[2]


def _file_inventory(root: Path) -> dict[str, bytes]:
    if not root.is_dir():
        raise FileNotFoundError(f"missing directory: {root}")
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def _agent_stems(root: Path, suffix: str) -> set[str]:
    if not root.is_dir():
        raise FileNotFoundError(f"missing directory: {root}")
    return {path.stem for path in root.glob(f"*{suffix}") if path.is_file()}


def compare_trees(root: Path) -> ParityResult:
    """Compare skills by bytes and agents by their runtime-independent stems."""

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
            claude_skills[relative_path] != codex_skills[relative_path]
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


def _print_result(result: ParityResult) -> int:
    if result.ok:
        print("harness parity: pass")
        return 0
    for diagnostic in result.diagnostics:
        print(f"harness parity: FAIL: {diagnostic}")
    return 1


def run_self_test(source_root: Path) -> int:
    """Prove a temporary one-sided edit fails, then restore it and pass."""

    with tempfile.TemporaryDirectory(prefix="harness-parity-") as temporary:
        temporary_root = Path(temporary) / "repository"
        shutil.copytree(source_root / ".claude", temporary_root / ".claude")
        shutil.copytree(source_root / ".codex", temporary_root / ".codex")

        target = temporary_root / ".claude" / "skills" / "run-batch" / "SKILL.md"
        original = target.read_bytes()
        target.write_bytes(original + b"\n<!-- temporary one-sided drift -->\n")
        drift_result = compare_trees(temporary_root)
        expected = "skill byte-different: run-batch/SKILL.md"
        if drift_result.ok or expected not in drift_result.diagnostics:
            print("harness parity self-test: failed to detect one-sided drift")
            return 1

        target.write_bytes(original)
        restored_result = compare_trees(temporary_root)
        if not restored_result.ok:
            print("harness parity self-test: restored copy did not pass")
            return 1

    print(f"harness parity self-test: detected {expected}; restored copy: pass")
    return _print_result(compare_trees(source_root))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="run temporary-copy drift proof")
    arguments = parser.parse_args()
    root = repository_root()
    return run_self_test(root) if arguments.self_test else _print_result(compare_trees(root))


if __name__ == "__main__":
    raise SystemExit(main())
