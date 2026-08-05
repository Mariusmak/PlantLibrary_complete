# Agent Skill Bridge

This workspace keeps Claude skill sources under `../.Claude/skills` and
Codex runtime skills under `../.codex/skills`.

Codex loads workspace skills from `.codex/skills`, so any Claude skill that
should also be available to Codex must be mirrored or adapted there. This
folder records that bridge for future agent maintenance.

Run `python scripts/harness/check_harness_parity.py` before committing any
change under `.claude/` or `.codex/`. It requires every mirrored skill file to
match byte-for-byte except the explicit runtime-specific
`validate-real-stack/SKILL.md`, and checks that agent definition stems exist in
both runtime trees. Exits nonzero on any drift; this is a manual pre-commit
step, not a hook — nothing runs it automatically. (Trimmed from the
Orchestrator_System original: this workspace has no CLAUDE.md/AGENTS.md
shared-block contract to verify.)

## Codex-enabled skills

| Skill | Claude source | Codex runtime path | Status |
| --- | --- | --- | --- |
| `plan-batch` | `../.Claude/skills/plan-batch` | `../.codex/skills/plan-batch` | mirrored (v1.3.1) |
| `real-stack-testing` | `../.Claude/skills/real-stack-testing` | `../.codex/skills/real-stack-testing` | mirrored, progressive references |
| `run-batch` | `../.Claude/skills/run-batch` | `../.codex/skills/run-batch` | mirrored |
| `sync-contracts` | `../.Claude/skills/sync-contracts` | `../.codex/skills/sync-contracts` | mirrored |
| `ui-ux-pro-max` | `../.Claude/skills/ui-ux-pro-max` | `../.codex/skills/ui-ux-pro-max` | Codex-adapted |
| `validate-real-stack` | `../.Claude/skills/validate-real-stack` | `../.codex/skills/validate-real-stack` | runtime-adapted; shared runner |
| `verify-stack` | `../.Claude/skills/verify-stack` | `../.codex/skills/verify-stack` | mirrored |

## Agent roster

| Agent | Claude definition | Codex definition | Model (Claude / Codex) |
| --- | --- | --- | --- |
| `real-stack-validator` | `../.claude/agents/real-stack-validator.md` | `../.codex/agents/real-stack-validator.toml` | `sonnet` low / `gpt-5.6-terra` low |
| `batch-plan-auditor` | `../.claude/agents/batch-plan-auditor.md` | `../.codex/agents/batch-plan-auditor.toml` | `sonnet` medium / `gpt-5.6-terra` medium |
| `batch-closeout-reviewer` | `../.claude/agents/batch-closeout-reviewer.md` | `../.codex/agents/batch-closeout-reviewer.toml` | `sonnet` high / `gpt-5.6-terra` high |

The Conductor-specific `v5-section-reader` agent was deliberately **not**
ported from `Orchestrator_System` — this workspace has no single large
normative proposal; the skills' section-reader wording is a no-op here.

## Maintenance notes

- Keep `SKILL.md` front matter trigger text aligned when new Claude skills are
  added or renamed.
- Keep `real-stack-testing` and its references byte-identical across runtimes
  within this workspace. Keep the `validate-real-stack` runner byte-identical
  while preserving runtime-specific skill frontmatter and delegation
  instructions.
- Cross-workspace status (2026-08-05): `plan-batch`, `run-batch`, and
  `real-stack-testing` have deliberately diverged from the
  `C:\Programmierung\Orchestrator_System` copies (the Orchestrator versions
  evolved around its local validation harness scripts, which do not exist
  here). Only the intra-workspace `.claude`/`.codex` mirrors are kept
  byte-identical; the shared subagent-delegation wording is tracked by hand
  across workspaces. This workspace's plan-batch is versioned on its own
  line (1.3.1 ≙ Orchestrator's 1.4.0 additions).
- Codex cannot spawn subagents. The `.codex/agents/*.toml` files are
  parity-mirrored role definitions only; the mirrored skills reference agents
  exclusively behind "if this invocation can spawn agents" wording with a
  mandatory inline fallback, which is what keeps the skill mirrors
  byte-identical across runtimes.
- Preserve Codex-specific instructions when a skill uses Codex tool names,
  shell examples, or runtime paths.
- Do not mirror `__pycache__` files; they are interpreter artifacts, not skill
  source.
