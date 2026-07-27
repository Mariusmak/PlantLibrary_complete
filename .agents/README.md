# Agent Skill Bridge

This workspace keeps Claude skill sources under `../.Claude/skills` and
Codex runtime skills under `../.codex/skills`.

Codex loads workspace skills from `.codex/skills`, so any Claude skill that
should also be available to Codex must be mirrored or adapted there. This
folder records that bridge for future agent maintenance.

## Codex-enabled skills

| Skill | Claude source | Codex runtime path | Status |
| --- | --- | --- | --- |
| `plan-batch` | `../.Claude/skills/plan-batch` | `../.codex/skills/plan-batch` | mirrored (v1.2.0) |
| `real-stack-testing` | `../.Claude/skills/real-stack-testing` | `../.codex/skills/real-stack-testing` | mirrored, progressive references |
| `run-batch` | `../.Claude/skills/run-batch` | `../.codex/skills/run-batch` | mirrored |
| `sync-contracts` | `../.Claude/skills/sync-contracts` | `../.codex/skills/sync-contracts` | mirrored |
| `ui-ux-pro-max` | `../.Claude/skills/ui-ux-pro-max` | `../.codex/skills/ui-ux-pro-max` | Codex-adapted |
| `validate-real-stack` | `../.Claude/skills/validate-real-stack` | `../.codex/skills/validate-real-stack` | runtime-adapted; shared runner |
| `verify-stack` | `../.Claude/skills/verify-stack` | `../.codex/skills/verify-stack` | mirrored |

## Validation workers

| Runtime | Definition | Model |
| --- | --- | --- |
| Claude Code | `../.claude/agents/real-stack-validator.md` | `sonnet`, low effort |
| Codex | `../.codex/agents/real-stack-validator.toml` | `gpt-5.6-terra`, low effort |

## Maintenance notes

- Keep `SKILL.md` front matter trigger text aligned when new Claude skills are
  added or renamed.
- Keep `real-stack-testing` and its references byte-identical across runtimes
  and workspaces. Keep the `validate-real-stack` runner byte-identical while
  preserving runtime-specific skill frontmatter and delegation instructions.
- Preserve Codex-specific instructions when a skill uses Codex tool names,
  shell examples, or runtime paths.
- Do not mirror `__pycache__` files; they are interpreter artifacts, not skill
  source.
