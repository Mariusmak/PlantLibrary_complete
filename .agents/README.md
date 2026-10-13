# Agent Skill Bridge — PlantLibrary superproject

This repository keeps its Claude skill sources under `../.claude/skills` and
agent definitions under `../.claude/agents`; the Codex runtime copies under
`../.codex/` are frozen. This file is PlantLibrary's own bridge record:
what is frozen, what is Claude-only and why, and where each skill comes from.
Rewritten at step `B1-1` of the master rework program
(`rework/PROMPTS_master-rework-runbook_2026-10-13.md` §3.3) on 2026-10-13.

**Codex is frozen since 2026-10-13** (`D-2026-10-13-03`, step `B7-2`, on
`Q-G-09` (a)): `.codex/**` and `AGENTS.md` outside its installer-owned marker
blocks are kept, never deleted, and are not edited or mirrored. A skill or
agent changed or added since then lives under `.claude/` only. The freeze is
block-aware: the `repo-hygiene` block (and, from `B5`, the `design-kit`
block) of `AGENTS.md` stays live, written by its installer, and the hygiene
checker keeps it equal to `CLAUDE.md`'s; the four Kit skill folders under
`.codex/skills/` are the Design Template Kit's and exempt. Each suite is
frozen by its own decision entry (`D-2026-10-13-02` in PyApp, AndroidApp,
Dashboard and Server; `D-2026-10-13-03` in Workspace and SharedContracts).

**To unfreeze** codex in a repository: a later decision entry there;
re-mirror `.claude/**` (and `CLAUDE.md`'s text outside the blocks into
`AGENTS.md`) for every change since its freeze commit; remove the
`AGENTS.md` banner; flip the `frozen` statuses below back to `mirrored`; set
the repository's `FROZEN_AT` row in `scripts/harness/check_harness_parity.py`
to `None` and drop its pins; for the superproject, make
`--with-codex-compare` the default again.

Run `python -B scripts/harness/check_harness_parity.py` after any edit to a
skill, an agent definition, this file, `.codex/**` or `AGENTS.md`; the
`harness-upkeep` skill names which check follows which edit. It checks the
Codex freeze in all seven repositories, that every `.claude/skills/*` folder
of this repository is a frozen row of the bridge table or a row of the
Claude-only table below, that each suite's shared skills and agents equal
this repository's, and the run-batch commit-proposal strings. Exits nonzero
on any drift; nothing runs it automatically.

## Codex bridge (frozen)

| Skill | Claude source | Codex runtime path | Status |
| --- | --- | --- | --- |
| `plan-batch` | `../.claude/skills/plan-batch` | `../.codex/skills/plan-batch` | frozen (2026-10-13, D-2026-10-13-03) at 1.4.0; the Claude copy is 1.5.1-pl since B1-1 |
| `run-batch` | `../.claude/skills/run-batch` | `../.codex/skills/run-batch` | frozen (2026-10-13, D-2026-10-13-03); the Claude copy gained the §7 newline rule at B1-1 |
| `real-stack-testing` | `../.claude/skills/real-stack-testing` | `../.codex/skills/real-stack-testing` | frozen (2026-10-13, D-2026-10-13-03); the Claude copy's item 7 changed at B1-1 |
| `validate-real-stack` | `../.claude/skills/validate-real-stack` | `../.codex/skills/validate-real-stack` | runtime-adapted; shared runner; frozen (2026-10-13, D-2026-10-13-03) |
| `test-driven-development` | `../.claude/skills/test-driven-development` | `../.codex/skills/test-driven-development` | frozen (2026-10-13, D-2026-10-13-03); the Claude copy was re-based on the Conductor's OP-SK-A text at B1-1 |
| `systematic-debugging` | `../.claude/skills/systematic-debugging` | `../.codex/skills/systematic-debugging` | frozen (2026-10-13, D-2026-10-13-03); the Claude copy was re-based on the Conductor's OP-SK-A text at B1-1 |
| `android-validation` | `../.claude/skills/android-validation` | `../.codex/skills/android-validation` | frozen (2026-10-13, D-2026-10-13-03) |
| `design-adoption` | `../.claude/skills/design-adoption` | `../.codex/skills/design-adoption` | frozen (2026-10-13, D-2026-10-13-03); retired 2026-10-13 at `B5-7` for `design-gate` (Q-G-07 (a)): the Claude copy is a pointer, the Codex copy keeps the frozen text |
| `gui-validation` | `../.claude/skills/gui-validation` | `../.codex/skills/gui-validation` | frozen (2026-10-13, D-2026-10-13-03) |
| `sync-contracts` | `../.claude/skills/sync-contracts` | `../.codex/skills/sync-contracts` | frozen (2026-10-13, D-2026-10-13-03) |
| `ui-ux-pro-max` | `../.claude/skills/ui-ux-pro-max` | `../.codex/skills/ui-ux-pro-max` | frozen (2026-10-13, D-2026-10-13-03); superproject only (the Kit wizard's fallback root, RC-A1-24) |
| `verify-stack` | `../.claude/skills/verify-stack` | `../.codex/skills/verify-stack` | frozen (2026-10-13, D-2026-10-13-03) |
| `webapp-testing` | `../.claude/skills/webapp-testing` | `../.codex/skills/webapp-testing` | frozen (2026-10-13, D-2026-10-13-03) |

## Agent roster

| Agent | Claude definition | Codex definition | Model (Claude / Codex) |
| --- | --- | --- | --- |
| `batch-closeout-reviewer` | `../.claude/agents/batch-closeout-reviewer.md` | `../.codex/agents/batch-closeout-reviewer.toml` | `opus` high, maxTurns 30 / `gpt-5.6-terra` high (frozen) |
| `batch-plan-auditor` | `../.claude/agents/batch-plan-auditor.md` | `../.codex/agents/batch-plan-auditor.toml` | `sonnet` high, maxTurns 24 / `gpt-5.6-terra` medium (frozen) |
| `real-stack-validator` | `../.claude/agents/real-stack-validator.md` | `../.codex/agents/real-stack-validator.toml` | `sonnet` low, maxTurns 16 / `gpt-5.6-terra` low (frozen) |

The three Claude definitions are the Conductor's (`Orchestrator_System` @
`2e7adb3`, RC-A1-04…06), adopted verbatim at B1-1. They preload
`real-stack-testing` (all three) and `plan-batch` (the auditor), so those
skills and the agents change in one commit. The validator's foreground rule
promises up to 3,600,000 ms; `../.claude/settings.json` sets
`BASH_MAX_TIMEOUT_MS` to match. The Conductor's `v5-section-reader` is not
taken: it reads the Conductor's v5 proposal, and no PlantLibrary package has
a Section-Mapped authority document (RC-A1-07).

## Suite copies

The six suites mirror the shared skills (`plan-batch`, `real-stack-testing`,
`run-batch`, `test-driven-development`, `validate-real-stack`) and the three
agents from this repository; the parity check compares them. The copies
below are not compared yet.

| Skill | Suite copy | Superproject source | Status |
| --- | --- | --- | --- |
| shared skills and agents | each suite's `.claude/skills/` and `.claude/agents/` | `../.claude/skills/`, `../.claude/agents/` | changed here at B1-1; refreshed at B1-2 (the mirror compare is red until then) |
| `gui-validation` | `PlantLibrary_PyApp/.claude/skills/gui-validation` (a 38-line pointer that does not resolve) | `../.claude/skills/gui-validation` | refreshed at B1-2 (Q-A1-04, Q-B7-01) |
| `design-adoption` | `PlantLibrary_Workspace/.claude/skills/design-adoption` | `../.claude/skills/design-adoption` | refreshed at B1-2 (Q-A1-04, Q-B7-01); the same pointer since `B5-7` (Q-G-07 (a)) |
| `gui-validation` | `PlantLibrary_Workspace/.claude/skills/gui-validation` | `../.claude/skills/gui-validation` | refreshed at B1-2 (Q-A1-04, Q-B7-01) |
| `sync-contracts` | `PlantLibrary_Workspace/.claude/skills/sync-contracts` | `../.claude/skills/sync-contracts` | refreshed at B1-2 (Q-A1-04, Q-B7-01) |
| `ui-ux-pro-max` | `PlantLibrary_Workspace/.claude/skills/ui-ux-pro-max` | `../.claude/skills/ui-ux-pro-max` | refreshed at B1-2 (Q-A1-04, Q-B7-01) |
| `verify-stack` | `PlantLibrary_Workspace/.claude/skills/verify-stack` (149 lines, behind this copy's 188) | `../.claude/skills/verify-stack` | refreshed at B1-2 (Q-A1-04, Q-B7-01) |
| `webapp-testing` | `PlantLibrary_Workspace/.claude/skills/webapp-testing` | `../.claude/skills/webapp-testing` | refreshed at B1-2 (Q-A1-04, Q-B7-01) |

## Claude-only skills

Skills added under `.claude/skills/` after the 2026-10-13 freeze; no Codex
copy. The bridged skills whose Claude copy changed after the freeze are
marked in the bridge table above; their Codex copies keep the frozen text.

| Skill | Claude source | Source @ pin, licence | Added at |
| --- | --- | --- | --- |
| `harness-upkeep` | `../.claude/skills/harness-upkeep` | the Conductor's operator skill `harness-upkeep` 0.1.0 (`Orchestrator_System` @ `2e7adb3`), rewritten for this repository's checks as 0.1.0-pl (RC-A1-12); original, no third-party licence | B1-1 |
| `code-quality-review` | `../.claude/skills/code-quality-review` | the Conductor's (`Orchestrator_System` @ `2e7adb3`, OP-SK-A); its reference adapted from wshobson/agents @ `156b7a5`; MIT (`LICENSE`). Adapted (RC-A1-15): Python suites only, deliverable root parameterised to `hygiene/CONSUMED_HYGIENE.md`, Conductor settings, dependency and loop terms dropped; operator session only | B1-3 |
| `security-audit` | `../.claude/skills/security-audit` | the Conductor's (`Orchestrator_System` @ `2e7adb3`, OP-SK-A); `references/` adapted from trailofbits/skills @ `82fe822`; CC-BY-SA-4.0 (`NOTICE`, the PlantLibrary changes listed there); `SKILL.md` original. Adapted (RC-A1-15): deliverable root parameterised, scratch outside the tree, no executable PoC, Kotlin/TS via the generic references; operator session only | B1-3 |
| `pathfinder` | `../.claude/skills/pathfinder` | the Conductor's (`Orchestrator_System` @ `2e7adb3`, OP-SK-A), adapted from thedotmack/claude-mem @ `039c616`; Apache-2.0 (`LICENSE`, `NOTICE`, the PlantLibrary modifications listed there). Adapted (RC-A1-15): read exclusions and deliverable root are this repository's; operator session only | B1-3 |
| `scratch-gate` | `PlantLibrary_PyApp/.claude/skills/scratch-gate`, `PlantLibrary_Server/.claude/skills/scratch-gate` (suite copies; none in this repository, which has no reclaim script and no `.tmp/` ignore) | the Conductor's operator skill `scratch-gate` 0.1.0 (`Orchestrator_System` @ `2e7adb3`), adapted as 0.1.0-pl (RC-A1-13, RC-A2-24): PyApp's `7ad02b1` `reclaim_scratch.py` port (no sweep, no lock); Server's copy stops at its step 0 until the Server harness port (`Q-A2-01` (a)); original, no third-party licence; operator session only | B7-3 |

Declined at B1-3: `dependency-audit` (the Conductor's, Trail of Bits-derived, CC-BY-SA-4.0) is not installed - deferred until Gradle coverage is decided (`Q-A1-02` (a), RC-A1-16): it cannot read PlantLibrary_AndroidApp's Gradle dependencies, and its GitHub route sends the `gh` token to `api.github.com`.

## Provenance of the bridged skills

| Skill | Claude source | Source @ pin, licence |
| --- | --- | --- |
| `plan-batch` | `../.claude/skills/plan-batch` | the Conductor's 1.5.1 (`Orchestrator_System` @ `2e7adb3`) with its §7 closeout-budget item replaced by 1.4.0's cap item (RC-A1-02, Q-A1-01 (a)); original |
| `run-batch` | `../.claude/skills/run-batch` | the Conductor's text before its one-command closeout (`e21e7f0`), plus its §7 newline rule (`ab49005`); §6 kept as PlantLibrary's (Q-A1-01 (a)); original |
| `real-stack-testing` | `../.claude/skills/real-stack-testing` | the Conductor's, item 7 adapted (RC-A1-03); original |
| `validate-real-stack` | `../.claude/skills/validate-real-stack` | the Conductor's, identical (RC-A1-27); original |
| `test-driven-development` | `../.claude/skills/test-driven-development` | obra/superpowers `8ca22db`, edited by the Conductor (OP-SK-A) and at B1-1 (stack-neutral commands, RC-A1-08); MIT (`LICENSE`) |
| `systematic-debugging` | `../.claude/skills/systematic-debugging` | obra/superpowers `8ca22db`, edited by the Conductor (OP-SK-A) and at B1-1 (stack-neutral commands; keeps `condition-based-waiting-example.ts` and `find-polluter.sh`, RC-A1-09); MIT (`LICENSE`) |
| `webapp-testing` | `../.claude/skills/webapp-testing` | third-party; upstream not named in the copy (`SKILL.md` front matter: `license: Complete terms in LICENSE.txt`); Apache-2.0, `LICENSE.txt` "Copyright 2026 Anthropic, PBC."; no upstream pin in the copy; added here at `bdcb8f4` (2026-07-17) with a PlantLibrary_Dashboard section (`Q-B1-01` (a), B1-3) |
| `ui-ux-pro-max` | `../.claude/skills/ui-ux-pro-max` | third-party; no licence file in the copy; origin per `SKILL.md` (front matter `name: ui-ux-pro-max`, "UI/UX Pro Max - Design Intelligence"; no upstream URL, author, version or pin); added here at `0b3a0c0` (2026-07-14) (`Q-B1-01` (a), B1-3) |
| `android-validation`, `design-adoption`, `gui-validation`, `sync-contracts`, `verify-stack` | `../.claude/skills/<name>` | PlantLibrary originals |

## Not installed here

- `runbook` (the Conductor's draft 0.1.0, its open `OP-RB` act): not
  installed in any PlantLibrary repository; record only (`Q-A5-01` (a),
  RC-A5-19). `OP-RB`'s copy into `PlantLibrary_Workspace` stays held until
  lane `B1` closes and decides the skill for all seven repositories.
- `instance-sync`: not taken; it syncs a deployed Conductor instance
  (RC-A1-14).
- `dependency-audit` (third-party-derived): declined at `B1-3`, deferred
  until Gradle coverage is decided (`Q-A1-02` (a), RC-A1-16); see the line
  under the Claude-only table. `code-quality-review`, `security-audit` and
  `pathfinder` were installed at `B1-3` (Claude-only table).
- `design-gate`, `design-audit`, `gallery-governance`, `impeccable`:
  installed by the Design Template Kit into the client suites at `B5`, never
  by hand, and not into this repository (RC-A1-10, RC-A1-11).
- `scratch-gate`: not in this repository (no reclaim script, no `.tmp/`
  ignore); its PyApp and Server copies are in the Claude-only table
  (RC-A1-13, RC-A2-24, `B7-3`).

## Maintenance notes

- `../.claude/settings.json` is tracked (`Q-A1-03` (a)): the git-safety deny
  list, 14 Bash entries each with its PowerShell twin, and
  `BASH_MAX_TIMEOUT_MS` 3600000. Operator-personal allows stay in the
  untracked `settings.local.json`.
- Every skill file is written back as bytes with its own line endings
  (`run-batch/SKILL.md` is mixed); every parity compare normalizes CRLF to
  LF first.
- Keep `SKILL.md` front matter trigger text aligned when a skill is added or
  renamed; a new skill gets its row here in the same commit.
- Do not mirror `__pycache__` files; they are interpreter artifacts, not
  skill source.
- Codex cannot spawn subagents, so the shared skills reference agents only
  behind "if this invocation can spawn agents" wording with a mandatory
  inline fallback.
