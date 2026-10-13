# scripts/harness — the superproject's static guards

This page **is** the inventory of the superproject's harness scripts, and each script's page is its
section below. Every script here is a static check or a one-off migration tool: Python stdlib only,
read-only unless its section says otherwise, no bytecode written, and none of them launches an app, a
build or a test of any kind. The checks cover the superproject and every submodule folder named in
`.gitmodules` that is present; an absent submodule folder is skipped with a printed line, never failed.

Written at step `B7-1` of the master rework program
(`rework/PROMPTS_master-rework-runbook_2026-10-13.md` §3.3) on 2026-10-13, on base `55a0a28`; its run
evidence is `rework/EVIDENCE_harness-guards_2026-10-13.md`. Refreshed at step `B7-3` on 2026-10-13
(`Q-B1-02` (a), RC-A2-18): the parity section re-verified after the Codex freeze (`B7-2`) and the
suite-skill table (`B1-2`), one section per script, and the scratch section added (`Q-A2-06` (a)). Rules
adapted from the Conductor's `docs/harness/README.md` (Orchestrator_System @ `2e7adb3`, read-only).
Procedure for keeping it true: the `harness-upkeep` skill.

## The folder's rules

1. **One section per script.** Every file in this folder has exactly one row in the inventory and one
   section below; this page is the folder's one page. A script added here gets both in its own commit.
2. **The section template.** Every section has these headings in this order: **Purpose**,
   **Invocation** (the exact argv and every flag), **Reads and writes**, **Exit codes and verdict
   line**, **Register and lane**, **Open debts**, **Owner**, ending with "Verified at `<sha>`": the
   commit whose code the section was checked against. Re-read the code before moving the sha; never
   move it without.
3. **One verdict line, three exit codes.** A check prints its findings, then exactly one verdict line
   `<name>: pass — …`, `<name>: fail — …` or `<name>: error — could not run: …`, and exits 0 (pass),
   1 (findings) or 2 (could not run), like the hygiene kit's checker.
4. **Static and read-only.** A check never fixes what it finds. It reads git facts with
   `git --no-optional-locks` only and never runs a git write command, in this repository, a submodule
   or the Conductor checkout. It sets `sys.dont_write_bytecode` before any import; run it with
   `python -B` from the superproject root as well.
5. **The truth rule.** A section describes what the script does at its verified commit. A section that
   is no longer true is a defect. A step that changes a script updates its section, and the verified
   commit, in the same commit.
6. **No proof surface.** This page names the static checks only. A batch row's proof is its
   `validation` cell, never a line of this page, and this page names no test runner and no test
   invocation.
7. **Self-checks are static.** A `--self-test` mode works on temporary copies outside the repository,
   plants one defect per check, proves each is reported, and then checks the real tree. It is a mode of
   the checker, not a test.
8. **Procedures are skills.** An operator procedure that drives a harness is a skill, named here as
   "Procedure: the `<skill>` skill" and nothing more: `harness-upkeep` for this folder, `scratch-gate`
   for a suite's scratch (section "Scratch per repository").

## The inventory

| Script | Purpose | Kind | Verified at |
|---|---|---|---|
| `check_harness_parity.py` | the Codex freeze, bridge coverage, the suite mirrors and the run-batch commit contract | check | `bbe6a38` |
| `check_package_newlines.py` | one line-ending style per package contract file | check | `a25b62e` |
| `check_batch_packages.py` | every package through the Conductor's parser, with the parser's provenance | check | `a25b62e` |
| `migrate_checklist_schema.py` | one-off V3 → 15-column checklist migration; **writes** | migration (closed) | not re-verified |

## `check_harness_parity.py`

**Purpose.** Six checks over the seven repositories:

1. *Codex freeze* — in every repository with a `FROZEN_AT` row, every file under `.codex/` equals its
   pinned SHA-256 (CRLF→LF-normalized bytes from `git show <freeze commit>:<path>`); an added, removed
   or changed file is a diagnostic. Exempt: the four Kit skill folders (`design-gate`, `design-audit`,
   `gallery-governance`, `impeccable`), `settings.local.json`, `__pycache__/`. `AGENTS.md` carries its
   one-line banner exactly once (line 1 or directly under the first heading) and, with the banner and
   the installer-owned marker blocks (`repo-hygiene`, `design-kit`) removed, equals its pinned digest.
2. *Bridge coverage* — every superproject `.claude/skills/*` folder is a frozen bridge row (status
   `frozen`, `runtime-adapted` or `Kit-installed`) or a row of the `## Claude-only skills` table in
   `.agents/README.md`.
3. *Suite mirrors* — in each present suite, the five shared skills (`plan-batch`,
   `real-stack-testing`, `run-batch`, `test-driven-development`, `validate-real-stack`), the suite's
   `SUITE_EXTRA_SKILLS` row and every superproject `.claude/agents/*.md` equal the superproject's copy.
   A same-name suite folder outside that set is listed as a note, not compared; a suite-only folder
   with no superproject counterpart is neither.
4. *Run-batch commit contract* — every `run-batch/SKILL.md` under `.claude/skills` or `.codex/skills`
   of a present repository holds the four commit-proposal strings and neither retired string.
5. *Codex compare* — only with `--with-codex-compare`: the superproject's `.claude/skills` against
   `.codex/skills` (`validate-real-stack/SKILL.md` may differ) and the agent stem pairing
   `.md`↔`.toml`. Off by default since the freeze; kept for an unfreeze.
6. *Roots* — an absent or not-checked-out submodule folder is skipped with a printed line.

Every content compare normalizes CRLF to LF; `__pycache__/` is ignored.

**Invocation.** `python -B scripts/harness/check_harness_parity.py [flags]` from the superproject root.

| Flag | Effect |
|---|---|
| (none) | checks 1–4 and 6 on the working trees, then the verdict |
| `--self-test` | plants one defect per check in a temporary copy (suite skill, folder and agent drift, the extra-skill table, both run-batch strings, the freeze plants for `.codex/` and `AGENTS.md` including the exempt edits and CRLF↔LF flips that must not count, bridge coverage, the multi-root skip; the codex compare too when it is on), proves each, then checks the real tree |
| `--with-codex-compare` / `--no-with-codex-compare` | check 5 on or off; default off |
| `--print-freeze-table REPO=COMMIT` | prints the freeze pins of one repository (`.` or a suite folder) from `git show COMMIT:<path>`; the only mode that calls git; its output goes into the pin tables, never edited by hand |

**Reads and writes.** Reads the working-tree `.claude/`, `.codex/` and `AGENTS.md` of all seven
repositories, `.gitmodules` and `.agents/README.md`; `--print-freeze-table` reads git objects. Writes
nothing (the self-test's copy lives in the system temp folder and is removed).

**Exit codes and verdict line.** 0 · 1 · 2. `harness parity: note: …` lines (pending freezes, the bridge
coverage state, listed folders), `harness parity: FAIL: …` per diagnostic, then
`harness parity: pass — 7 repositories (superproject + 6 suites, 0 skipped); codex freeze green in 7 of 7 (0 pending); codex compare off; bridge coverage checked; 5 shared skills + agents per suite; run-batch commit contract`
(or `fail — <n> diagnostics; …`, or `error — could not run: …`).

**Register and lane.** RC-A2-08, RC-A1-21, RC-A1-18…20 (the freeze), RC-A1-22 (`SUITE_EXTRA_SKILLS`);
`Q-A2-04` (a), `Q-G-09` (a), `Q-A3-01` (a). Lane `B7` (`B7-1` wrote it, `B7-2` added the freeze and the
bridge coverage); `B1-2` filled `SUITE_EXTRA_SKILLS`.

**Open debts.** None recorded. The unfreeze recipe is in the script's docstring and in
`.agents/README.md`.

**Owner.** Lane `B7` of the master rework; after the program, whoever changes a mirrored skill, an agent
or the bridge README (the `harness-upkeep` skill). Verified at `bbe6a38` (re-read at `B7-3`).

## `check_package_newlines.py`

**Purpose.** Package contract files (`README.md`, `SCOPE.md`, `CONTEXT_INDEX.md`, `BATCH_PLAN.md`,
`TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`) hold one line-ending style each. A package is a
git-tracked folder holding a tracked `BATCH_PLAN.md`. The seven live packages (and any unclassified one)
are counted; frozen MVP, `Archive_PreMVP`, archive and the frozen Workspace trees are listed, not
counted.

**Invocation.** `python -B scripts/harness/check_package_newlines.py` (no flags).

**Reads and writes.** `git ls-files` per repository; tracked files only, `.tmp/` never; the working-tree
bytes. Writes nothing, fixes nothing.

**Exit codes and verdict line.** 0 · 1 · 2; `package-newlines: pass — 0 mixed contract files in 7
counted packages …`.

**Register and lane.** RC-A2-13 · `B7`.

**Open debts.** None recorded.

**Owner.** Lane `B7`; a step that adds, freezes or archives a package edits the classification table at
the top of the script in the same commit. Verified at `a25b62e` (`B7-1`).

## `check_batch_packages.py`

**Purpose.** Census of every package through the Conductor's own parser
(`conductor.batch_package.parse_package`), printing the parser's provenance first: module path, its git
checkout and commit, or the instance's `_sync_stamp.json`. The seven live packages are counted; the four
frozen Workspace packages are listed.

**Invocation.** `python -B scripts/harness/check_batch_packages.py [--parser-src <src>]`.

| Flag | Effect |
|---|---|
| (none) | the importable `conductor`, else `CONDUCTOR_SRC`, else instance 2's `src` |
| `--parser-src <src>` | a `src` folder holding `conductor/`, put first on the path; refused (exit 2) if another install shadows it |

**Reads and writes.** The package folders under each suite's `implementation/` and Workspace
`strategy/`, `system_description/`; the parser module; git facts of the parser checkout. Writes nothing.

**Exit codes and verdict line.** 0 · 1 · 2; `batch-packages: pass — 0 errors in 7 counted packages (…);
… parser <path>`.

**Register and lane.** RC-A2-09; F-A7-02 · `B7`, used by `B4`.

**Open debts.** None recorded.

**Owner.** Lane `B7`; the classification table at the top changes with a package added, frozen or
archived. Verified at `a25b62e` (`B7-1`).

## `migrate_checklist_schema.py`

**Purpose.** One-off migration of a package's `TASK_CHECKLIST.md` from the 14-column V3 schema to the
Conductor's 15-column schema, keeping the file's line endings (onboarding runbook Appendix B). **Writes**
the checklist it is given; refuses an already-migrated one. Not a check.

**Invocation.** See its docstring.

**Reads and writes.** The named checklist and `BATCH_PLAN.md` · rewrites the named `TASK_CHECKLIST.md`.

**Exit codes and verdict line.** See its docstring.

**Register and lane.** Onboarding steps 2a/2b · closed.

**Open debts.** None; kept for history.

**Owner.** None (closed). Not re-verified at `B7-1` or `B7-3`.

## Scratch per repository

Each suite's rule is its `CLAUDE.md` "Scratch policy"; this table restates it for orientation only, and
the suite text wins. The superproject's scripts write no scratch.

| Repository | Scratch layout (as its `CLAUDE.md` states it) | Reclaim script | Gate procedure | Kit `scratch` module |
|---|---|---|---|---|
| superproject | none: no `.tmp/` ignore, no scratch paragraph, no scratch user | none | none | off; stays off until a step here needs scratch (`Q-A2-06` (a)) |
| PlantLibrary_PyApp | `.tmp/` only, gitignored; closeout ledgers and chunk artifacts in `.tmp/chunks/<run-id>/`; test basetemps `.tmp/p/<slug>`; per closeout generation `.tmp/p/<run-id>/` (`scope.json`, `ledger.jsonl`, `classification.json`) and `.tmp/chunks/<run-id>/chunk-manifest.json` | `scripts/harness/reclaim_scratch.py`, the `7ad02b1` port: report and `--reclaim`; no sweep, no lock (a re-port waits, `Q-A2-01` (a)) | Procedure: the `scratch-gate` skill (`.claude/skills/scratch-gate/`, Claude-only) | decided on, `D-2026-10-13-04` (`e17d7ba`); the pin stays kit `0.2.1`, `Modules none` until `B3-8`'s `0.3.0` re-pin runs the installer with it |
| PlantLibrary_Server | `.tmp/` only, gitignored; `.tmp/chunks/<run-id>/`; test basetemps `.tmp/p/<slug>` | none until its harness port (onboarding step 7, `Q-A2-01` (a)) | Procedure: the `scratch-gate` skill (Claude-only); it stops at its step 0 while the script is absent | decided on, `D-2026-10-13-04` (`d6a6497`); enabled at `B3-8` |
| PlantLibrary_SharedContracts | `.tmp/` only, gitignored; `.tmp/chunks/<run-id>/`; test basetemps `.tmp/p/<slug>` | none | none | decided on, `D-2026-10-13-04` (`72e5a38`); enabled at `B3-8` |
| PlantLibrary_Dashboard | `.tmp/` only, gitignored; a `.tmp/chunks/<run-id>/` closeout line for a harness the suite does not have (F-A2-18) | none | none | decided on, `D-2026-10-13-04` (`604d1d0`); enabled at `B3-8` |
| PlantLibrary_AndroidApp | as Dashboard (F-A2-18) | none | none | decided on, `D-2026-10-13-04` (`2353b6c`); enabled at `B3-8` |
| PlantLibrary_Workspace | as Dashboard (F-A2-18) | none | none | decided on, `D-2026-10-13-04` (`41fd24c`); enabled at `B3-8` |

Everywhere: nothing runs elevated, and no scratch or output path points outside the repository. The
kit's module, once on, checks only that the scratch root is ignored by git and that no retired scratch
name is recreated; the interior of `.tmp/` is the suite's.

## Which check after which edit

| The edit | The check(s) |
|---|---|
| any file under `.claude/skills/**` or `.claude/agents/**`, in the superproject or a suite | `check_harness_parity.py` |
| a skill folder added to the superproject's `.claude/skills/` | its row in `.agents/README.md` (bridge or `## Claude-only skills`) in the same commit, then `check_harness_parity.py` (bridge coverage) |
| `.agents/README.md` | `check_harness_parity.py` (bridge coverage), then the hygiene checker |
| a mirror of a PlantLibrary-only skill added to a suite (RC-A1-22) | add the skill to that suite's `SUITE_EXTRA_SKILLS` row in the same commit, then `check_harness_parity.py` |
| anything under `.codex/**`, or `AGENTS.md` outside its installer-owned blocks | nothing may change there (the freeze); `check_harness_parity.py` reports it; restore from the freeze commit |
| any `run-batch/SKILL.md` copy | `check_harness_parity.py` (the commit-contract strings) |
| a suite's `scripts/harness/reclaim_scratch.py` added or re-ported | that suite's `scratch-gate/SKILL.md` updated in the same commit (its flags, sweep and lock), then `check_harness_parity.py` and the suite's hygiene checker |
| any package contract file (`README.md`, `SCOPE.md`, `CONTEXT_INDEX.md`, `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`) | `check_package_newlines.py`, then `check_batch_packages.py` |
| a package's batch order, goals, `**Model:**`, primary rows, `**Requires:**` or checklist rows | `check_batch_packages.py` twice: with the default parser and with `--parser-src` at instance 2's `src` |
| a new package, or a package frozen or archived | the classification tables at the top of `check_package_newlines.py` and `check_batch_packages.py`, in the same commit |
| any markdown file, `CLAUDE.md`, `AGENTS.md` or a repository's `hygiene/` files | that repository's hygiene checker (`scripts/hygiene/repo_hygiene_check.py check`) |
| a script in this folder | its section above (rule 5); for `check_harness_parity.py`, also its `--self-test` |

## Known limits

- Since the freeze (`B7-2`) the `.claude`↔`.codex` compare is off by default and covers the superproject
  only when switched on; every repository's `.codex/` and `AGENTS.md` are checked against their freeze
  pins instead.
- Bridge coverage reads the superproject's `.claude/skills/` only. A suite-only skill folder (the
  `scratch-gate` copies in PyApp and Server, the Design Template Kit's skills in the client suites) has
  no superproject counterpart and is neither compared nor listed; the Kit's skills have the Kit's own
  parity check, and the `scratch-gate` copies are recorded in `.agents/README.md`'s Claude-only table.
- The suite compare covers the five shared skills, each suite's `SUITE_EXTRA_SKILLS` row and the
  agents; a same-name folder outside that set is listed, not compared.
- The two package checks classify live and frozen packages by fixed tables; a package neither table
  names is counted, so a new package is guarded by default.
