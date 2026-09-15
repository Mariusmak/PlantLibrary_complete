# Agent Skill Bridge

This workspace keeps Claude skill sources under `../.Claude/skills` and
Codex runtime skills under `../.codex/skills`.

Codex loads workspace skills from `.codex/skills`, so any Claude skill that
should also be available to Codex must be mirrored or adapted there. This
folder records that bridge for future agent maintenance.

Run `python scripts/harness/check_harness_parity.py` at Harness_V1 batch
close, and mandatorily any time `CLAUDE.md`, `AGENTS.md`, or the v5 proposal
changes. It requires every mirrored skill file to match byte-for-byte except
the explicit runtime-specific `validate-real-stack/SKILL.md`, checks that
agent definition stems exist in both runtime trees, diffs the CLAUDE.md/
AGENTS.md shared block (everything above each file's runtime-specific
section — `## Claude subagent roster` in CLAUDE.md, `## Codex skill runtime`
in AGENTS.md), and verifies the v5-proposal facts cited in CLAUDE.md (line
count, Section Map range) against the real proposal file. Exits nonzero on
any drift; this is a manual pre-close/pre-commit step, not a hook — nothing
runs it automatically.

## Codex-enabled skills

| Skill | Claude source | Codex runtime path | Status |
| --- | --- | --- | --- |
| `plan-batch` | `../.Claude/skills/plan-batch` | `../.codex/skills/plan-batch` | mirrored (v1.4.0) |
| `real-stack-testing` | `../.Claude/skills/real-stack-testing` | `../.codex/skills/real-stack-testing` | mirrored, progressive references |
| `run-batch` | `../.Claude/skills/run-batch` | `../.codex/skills/run-batch` | mirrored |
| `validate-real-stack` | `../.Claude/skills/validate-real-stack` | `../.codex/skills/validate-real-stack` | runtime-adapted; shared runner |

## Agent roster

| Agent | Claude definition | Codex definition | Model (Claude / Codex) |
| --- | --- | --- | --- |
| `real-stack-validator` | `../.claude/agents/real-stack-validator.md` | `../.codex/agents/real-stack-validator.toml` | `sonnet` low / `gpt-5.6-terra` low |
| `v5-section-reader` | `../.claude/agents/v5-section-reader.md` | `../.codex/agents/v5-section-reader.toml` | `haiku` low / `gpt-5.6-luna` low |
| `batch-plan-auditor` | `../.claude/agents/batch-plan-auditor.md` | `../.codex/agents/batch-plan-auditor.toml` | `sonnet` medium / `gpt-5.6-terra` medium |
| `batch-closeout-reviewer` | `../.claude/agents/batch-closeout-reviewer.md` | `../.codex/agents/batch-closeout-reviewer.toml` | `sonnet` high / `gpt-5.6-terra` high |

## Maintenance notes

- Keep `SKILL.md` front matter trigger text aligned when new Claude skills are
  added or renamed.
- Keep `real-stack-testing` and its references byte-identical across runtimes
  within this repository. Keep the `validate-real-stack` runner byte-identical
  while preserving runtime-specific skill frontmatter and delegation
  instructions.
- Cross-workspace status (2026-08-05): `plan-batch`, `run-batch`, and
  `real-stack-testing` have deliberately diverged from the
  `C:\Programmierung\SW_Development` (PlantLibrary) copies — this repository's
  versions evolved around `scripts/harness/` (long-validation runner, scoped
  regression matrix), which PlantLibrary does not have. Only the
  intra-repository `.claude`/`.codex` mirrors are parity-enforced; the shared
  subagent-delegation wording is tracked by hand across workspaces
  (PlantLibrary's plan-batch 1.3.1 ≙ this repository's 1.4.0 additions).
  PlantLibrary carries `batch-plan-auditor` and `batch-closeout-reviewer` but
  deliberately not the Conductor-specific `v5-section-reader`.
- Preserve Codex-specific instructions when a skill uses Codex tool names,
  shell examples, or runtime paths.
- Do not mirror `__pycache__` files; they are interpreter artifacts, not skill
  source.
- Chapter-8 retrofit (2026-08-19, `AUDIT_token-efficiency_2026-08-18.md` §7
  P-1…P-6): `design-adoption`, `gui-validation`, `sync-contracts`,
  `verify-stack`, `webapp-testing`, and `ui-ux-pro-max` relocated out of both
  `.claude/skills/` and `.codex/skills/` (copy-verified first) to
  `C:\Programmierung\SW_Development\PlantLibrary_Workspace\.claude\skills\`,
  the PlantLibrary-gated workspace they were unused here — their bridge rows
  above are removed accordingly.
- Codex cannot spawn subagents. The `.codex/agents/*.toml` files are
  parity-mirrored role definitions: the parity checker requires every
  `.claude/agents/*.md` stem to have a `.toml` counterpart, and Codex's
  `validate-real-stack` skill references its role by name, but no Codex
  session actually forks one today. The mirrored skills (`plan-batch`,
  `run-batch`) therefore reference agents only behind "if this invocation can
  spawn agents" wording with a mandatory inline fallback — that phrasing is
  what lets the skill mirrors stay byte-identical across runtimes.
- Chapter-8 graphify drop (2026-08-19, `AUDIT_graphify-value_2026-08-18.md`
  Decision, D-2026-08-18-01): the `## graphify` sections that used to sit
  between the shared block and each file's runtime-specific section were
  removed from both CLAUDE.md and AGENTS.md (archived, not deleted, per
  AM-8 — `graphify-out/` moved off-repo; the graphify hook entries in
  `.claude/settings.json` and `.codex/hooks.json` and the git hooks
  installed by `scripts/install_graphify_hooks.ps1` were removed too). The
  shared-block end marker for CLAUDE.md is now `## Claude subagent roster`
  (`check_harness_parity.py`'s `INSTRUCTION_SHARED_END_MARKER`); AGENTS.md's
  stays `## Codex skill runtime`, unchanged.
