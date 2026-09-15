# Conductor onboarding runbook — `SW_Development` on instance 2 (steps `0` … `9`)

*Written 2026-09-15 (evening), after the second Conductor instance (`C:\Programs\AI_Orchestrator_2`,
GUI `http://127.0.0.1:8797`) was set up per handbook chapter 09 and
`HANDOVER_batch-package-schema-drift_2026-09-15.md` recorded why none of the PlantLibrary batch
packages can be bound. One track, one sequence: this file is the authority for **what to paste, in
which order, with which model and reasoning**. It was written from measurements taken on
2026-09-15 with Conductor's own parser (`src/conductor/batch_package.py` at `ff15306`, the code
instance 2 runs — every key file hashes identical to `main`), not from the handover's prose.*

## 0. What this is, and what it is not

| | |
|---|---|
| Scope | Bring the six `PlantLibrary_*` suites under `C:\Programmierung\SW_Development` to a state where their **live** batch packages parse, bind and execute on Conductor instance 2; refresh the skill mirrors, `CLAUDE.md`/`AGENTS.md` and scratch policy each suite needs for `run-batch` / `plan-batch` at their current version; decide what is obsolete; prove one batch end to end; then route the remaining work (Conductor-driven where it can be, out of band where it cannot yet) |
| Working directories | **`C:\Programmierung\SW_Development`** (the superproject) for housekeeping, audits and the register. **The suite folder** (`C:\Programmierung\SW_Development\PlantLibrary_<Suite>`) for every package migration, every `/plan-batch`, every out-of-band `/run-batch` — that is the git root of the package and the exact cwd a Conductor worker gets (`workdir = git root of the bound package`). **`C:\Programmierung\Orchestrator_System`** only for step `8` (a Conductor proposal) |
| Normative sources | Conductor's parser and closeout: `src/conductor/batch_package.py` (`CHECKLIST_COLUMNS`, `STATUS_VOCABULARY`, `_parse_state_signals`, `_classify`), `src/conductor/batch_discovery.py` (`resolve_and_validate`), `src/conductor/gui.py` (`POST/PATCH /api/v1/projects`, `POST /api/v1/intake/batch-package`), `src/conductor/validation.py` (`ValidationPlanner.scope`) and `scripts/harness/regression_scope.py` (`STANDING_CHECK_PREFIXES`, `unmapped touched path`) · the skills at their current version: `.claude/skills/plan-batch/SKILL.md` §3–§7, `.claude/skills/run-batch/SKILL.md` §1–§8 (identical bytes in both repos as of 2026-09-15) · `docs/handbook/09-second-instance.md` steps 7–10 · `IMPLEMENTATION_PLAN.md` (2026-08-04, the program sequencing: waves A–F, §5 decisions, §7 unplanned backlog) · the handover named above |
| Ledger of record | §L at the end of this file. Flip a step there in the same commit as the step's output. Decisions from gates `G1`/`G2` are recorded in §4's "decided" column, same commit |
| What this file never does | Name a proof surface. A prompt states scope, constraints, done-when and the commit line; what counts as proof is the row's `validation` cell plus the executing skill's standing legs. The skills are copied byte-identical from the dev repo and are never edited here — a limitation of a skill is raised as a Conductor proposal (step `8`), never patched in a mirror |

## 1. Where things stand (measured 2026-09-15)

### 1a. Instance 2

| surface | observed | consequence |
|---|---|---|
| Process | up, pid `18016`, listening on `8797` (GUI) and `8798` (RPC); instance 1 on `8787`; `data_dir` `C:\Conductor2\data` | both instances share one Claude subscription — expect the five-hour window to fill faster while both dispatch |
| Code | `src\conductor\*.py` byte-identical to `main` at `ff15306` for `batch_package`, `batch_discovery`, `validation`, `core`, `gui`, `batch_coordinator`, `execution_table` | every rule this runbook cites is the rule the instance enforces |
| Vendors | `claude` enabled (creds `C:\Conductor2\creds\claude`), `codex` **disabled**, `cursor` disabled; worker account `conductor_worker`, `on_shared_account: refuse` | the `.codex/` mirrors matter for parity only; the Claude worker must find `/run-batch` from the suite folder (F-7) |
| Intake roots | six roots, one per suite, each `…\PlantLibrary_<Suite>\implementation` (ids `pyapp`, `server`, `androidapp`, `dashboard`, `sharedcontracts`, `workspace`) | anything outside `implementation\` (e.g. `Workspace\strategy\…`) is never offered |
| Projects | seven rows: `default` (archived) and six named after the suites, **all unbound** (`batch_package_path = NULL`); `PlantLibrary_PyApp` is the active one | see F-5: these six cannot be bound after the fact |
| Validation config | `validation.enabled: true`, `max_scope_targets: 600`, `parallel_ordinary: 1` | the AM-18 coordinator closeout runs — which needs the harness in the suite (F-6) |

### 1b. The package census

Run with Conductor's real parser over every folder that carries a checklist (Appendix A reproduces
it). "cols" is the checklist header width; Conductor requires exactly **15**.

| Package (relative to `SW_Development\PlantLibrary_`) | cols | rows | statuses | batches (done-marked) | parser errors | verdict |
|---|---|---|---|---|---|---|
| `PyApp\implementation\System_V1_Implementation` | 14 | 19 | todo 10 · blocked 4 · done 3 · gated 2 · **1 malformed row** | 9 (1) | 24 — no 15-col table, 22 phantom "missing primary row", 1 requires-lint (`PY1-B04`) | **live — migrate; pilot suite** |
| `Server\implementation\System_V1_Implementation` | 14 | 36 | done 7 · todo 26 · deferred 3 | 8 (0) | 35 — schema, 33 phantom, `SV1-B05` has no goal | **live — migrate; the V1 critical path (`SV1-B00`)** |
| `AndroidApp\implementation\System_V1_Implementation` | 14 | 39 | done 4 · todo 26 · gated 9 | 15 (2) | 44 — schema, 40 phantom, 3 requires-lint (`AN1-B08` ×2, `AN1-B11`) | **live — migrate; out of band until step `8` lands** |
| `Dashboard\implementation\System_V1_Implementation` | 14 | 22 | todo 9 · blocked 8 · deferred 2 · gated 2 · done 1 | 9 (1) | 26 — schema, 22 phantom, `WD1-B03` has no goal, 2 requires-lint (`WD1-B04`, `WD1-B06`) | **live — migrate; out of band until step `8` lands** |
| `SharedContracts\implementation\System_V1_Implementation` | 14 | 10 | done 3 · todo 7 | 4 (1) | 11 — schema, 10 phantom | **live — migrate; out of band until step `8` lands** |
| `Workspace\implementation\System_V1_Implementation` | 14 | 16 | done 7 · todo 3 · gated 6 | 8 (2) | 18 — schema, 16 phantom, 1 requires-lint (`SY1-B05`) | **live — migrate; the coordination package** |
| `Workspace\implementation\System_Design_Architecture` | 13 | 42 | done 1 · gated 7 · todo 34 | 9 (0) | 8 — schema (no `baseline_id`, no `model`) | live but **gated on `SDA-DEC-01..05`** (open since 2026-07-08, non-gating for V1 per D-V1-11) — migrate, bind only after the decisions |
| `Workspace\implementation\System_Integration_MVP` | 11 | 26 | done 26 | 18 (18) | 25 — older schema | **terminal** (MVP closed 2026-07-15) — do not migrate |
| `Workspace\implementation\System_Tooling` | 14 | 5 | done 5 | 2 (2) | 6 — schema | **terminal** — do not migrate |
| `Workspace\strategy\Cross_Platform_Strategy` | 11 | 29 | done 29 | 7 (7) | 30 | **terminal**, outside every intake root — leave |
| `Workspace\system_description\PlantLibrary_System_Description` | 9 | 17 | done 17 | 16 (16) | 62 (incl. 46 duplicate `### Intent/Output/Validation` pseudo-anchors) | **terminal, frozen** — leave |
| `<Suite>\implementation\MVP\` (5×), `PyApp\implementation\Archive_PreMVP\` | — | — | — | — | not packages at this level (files sit under `MVP\package\`) | **terminal evidence chain** — keep read-only (`IMPLEMENTATION_PLAN.md` §7 already decided this) |
| `Workspace\implementation\Server_VM_Setup\` | — | — | — | — | two prompt documents, no package | not a Conductor concern |
| `Workspace\methodology\Design_Template_Initiative\` | — | — | — | — | `STATE.md` only; Phase 6 of a separate initiative whose pilot is the Conductor GUI itself | not a batch package; **its uncommitted edits block every Conductor attempt in the Workspace suite** (F-9) |

"Phantom" errors are the one root cause fanning out: with a 14-column header the table is never
recognised, so every primary-row reference in `BATCH_PLAN.md` reads as missing. They vanish with the
column fix. What does **not** vanish is listed under F-2…F-4 and F-11.

### 1c. Findings — read before pasting anything

- **F-1 Schema drift (the handover's finding, confirmed and widened).** `CHECKLIST_COLUMNS` is
  `ID | status | skill | design_context | baseline_id | area | file(s) | task | context | requirements | done-when | validation | risk | effort | model`,
  matched case-insensitively against the header row, exact count. Six live packages are at 14
  (no `model`), `System_Design_Architecture` at 13 (no `baseline_id`, no `model`). The parser
  tolerates an **empty** row `model` cell (it falls back to the batch's `**Model:**` line), but
  plan-batch §7 requires every row **and** batch to name a pair (`opus/sol` · `sonnet/terra` ·
  `haiku/luna`), so the migration fills both. Status vocabulary is unchanged
  (`todo | needs-reverify | blocked | gated | deferred | done`); every existing status is legal.
- **F-2 Requires-placement lint, seven tokens in six batches** (independent of F-1, fires on
  `BATCH_PLAN.md` prose today): `PY1-B04`→`PY1-B05`; `AN1-B08`→`AN1-B09`, `AN1-B10`;
  `AN1-B11`→`AN1-B09`; `WD1-B04`→`WD1-B05`; `WD1-B06`→`WD1-B05`; `SY1-B05`→`SY1-B07`. A
  backticked batch/row ID after the first sentence of `**Requires:**` or `**Primary rows:**` is
  refused. Fix by folding the real prerequisite into the first sentence or moving the commentary
  to `**Notes:**`. The same lint is silent on a line with no sentence-ending punctuation — do not
  "fix" it by deleting the full stop.
- **F-3 Two headless removed batches.** `SV1-B05` and `WD1-B03` were removed on 2026-07-10 (PA-08)
  but still carry `## Batch` headings without a `**Goal:**` → "has no goal" today, and after F-1
  they would classify `not_yet_detailed` (no primary rows) and park the cursor "awaiting
  plan-batch detail" the moment it reaches them. Demote each to a `### Removed batch …` heading
  (the parser only reads `## Batch <KEY>`), keep the text as the record.
- **F-4 One malformed row.** `PY-V1-REL-02` (PyApp checklist line 40) has 13 cells, not 14 — a
  cell was dropped when the row was authored. Restore it before adding the 15th column, or the row
  is silently skipped with a "cells, expected 15" error.
- **F-5 Binding is create-only; the handover's step 4 is wrong.** `PATCH /api/v1/projects/{id}`
  accepts only `name`, `policy`/`policy_yaml`, `archived`. A package is bound **only** at
  `POST /api/v1/projects` with `batch_root_id` + `batch_relative_path` (both or neither), validated
  through `resolve_and_validate`: the folder must parse with zero errors, must not be bound to
  another project, and must lie inside the submitted `repo`. The six registered projects therefore
  cannot be bound; they are archived (an active project cannot be archived — activate the new one
  first) and recreated bound. One project binds exactly one package; two packages in one suite
  (Workspace V1 + SDA) means two projects on one git root — allowed, warned about, and never
  auto-serialised.
- **F-6 The closeout harness is Conductor-repo-specific — the finding the handover's "step 7
  check" would have surfaced.** With `validation.enabled: true` the coordinator runs
  `python scripts/harness/regression_scope.py <touched paths> --format json --max-targets 600`
  **in the project's git root** (`ValidationPlanner.scope`), then `run_validation.py` per chunk;
  the worker-route legs in run-batch §6 5a/6 name the same three scripts plus
  `scripts/harness/duration_history.json` and `.tmp/chunks/`. No suite has any of them
  (`SW_Development\scripts\harness\` holds only the parity checker). And the harness is
  **pytest-only by construction**: a touched path with no importing `tests/test_*.py` is refused as
  `unmapped touched path`; repo-root `.md/.txt` and `implementation/`, `.claude/`, `.codex/`,
  `scripts/` route to sentinels named after Orchestrator tests (`tests/test_repo_hygiene.py`,
  `tests/test_batch_package_parser.py`, …) that only exist in the dev repo. Consequences:
  (i) **today no suite can close a batch under Conductor** — every closeout would park at the
  planning seam (`HARNESS_PLANNING_FAILED`/`UNMAPPED`); (ii) for the pytest suites (**PyApp**,
  **Server**) a suite-local harness port with suite-named sentinels is sufficient and is planned
  as steps `4` and `7`; (iii) for **Dashboard** (Vite/Vitest/Playwright), **AndroidApp** (Gradle),
  **SharedContracts** (generators) no port can work — every product path is unmapped by design —
  so those suites run **out of band** (`/run-batch` in a VS Code session, the way every batch so
  far was run) until Conductor gains a non-pytest closeout route, which is step `8`'s proposal.
  `validation.enabled: false` ("pre-AM-18 behaviour, worker-run closeout") was considered and
  **rejected**: it only moves the same three scripts from the coordinator to the worker, and the
  worker is bound to the skill text that names them.
- **F-7 Worker cwd is the suite, and the suites carry no batch skills.** `execution_table.py`
  tells the worker to "execute … through the workspace /run-batch skill" from "the current
  directory", and the task's `workdir` is the git root of the bound package — the **submodule**
  (`PlantLibrary_PyApp`, …), never `SW_Development`. The refreshed mirrors sit only in
  `SW_Development\.claude\skills` and `.codex\skills`; the submodules carry none of `run-batch`,
  `plan-batch`, `real-stack-testing`, `validate-real-stack`, `test-driven-development`, and no
  `.claude\agents\` (PyApp mirrors `gui-validation` + `impeccable`, Android `impeccable`, Workspace
  six suite skills — untracked). Whether Claude Code discovers a parent folder's `.claude\skills`
  from a submodule cwd is **unverified**; the fact that earlier sessions mirrored suite skills
  *into* PyApp says it did not. Step `1` measures it; the default plan mirrors the five batch
  skills and the three agents into every live suite.
- **F-8 `CLAUDE.md` / `AGENTS.md`.** AndroidApp, Dashboard, SharedContracts and Workspace have
  none at their root. Server's pair is runtime-only (Docker context, test recipe) — nothing about
  the package location, scratch policy or progress truth. PyApp's `CLAUDE.md` is rich but still
  points at the archived `Improvements/GUI_Improvements_V3/DRIVER_SCRIPT_V3.md`. `.tmp/` is
  gitignored in PyApp only; Conductor's worker and the harness both expect a reclaimable
  gitignored scratch root at the git root.
- **F-9 Uncommitted state that will park the first attempt.** Superproject: the step-7 skill
  refresh (`.claude/skills/{plan-batch,run-batch,real-stack-testing,validate-real-stack}`,
  `.codex/skills/…`, `.claude/agents/*`, `.agents/README.md`) is **modified, uncommitted**, and
  `.codex/agents/batch-plan-auditor.toml` + `real-stack-validator.toml` were **not** refreshed
  (they lag the dev repo's AM-52 premise-verdict wording). `PlantLibrary_Workspace` submodule:
  five dirty paths from the Design Template Initiative (`RUNBOOK_GUI_REWORK.md`, `STATE.md`, two
  evidence files, untracked `.claude/`). Conductor parks a green batch whose tree holds foreign
  dirt (`unattributed_dirty`); nothing runs in Workspace until this is committed.
- **F-10 Terminal packages under the intake root.** `System_Integration_MVP` and `System_Tooling`
  sit directly under the `workspace` root, so intake will always list them and a bind attempt
  will always fail. Leave them unmigrated (they are the MVP evidence chain the V1 registers cite);
  say so in `Workspace\implementation\README.md` so nobody retries.
- **F-11 Latent checks that go live the moment the table parses.** (a) Every checklist row needs a
  `### <ROW-ID>` anchor in `TASK_CONTEXT.md` whose first non-blank line carries
  `` `skill: …` `` and `` `design_context: …` `` equal to the row's cells — PyApp's anchors have
  the form; the others are unmeasured until F-1 is fixed. (b) A `blocked` row counts as recorded
  only with a dated `STATE.md` line naming the ID together with "blocked"/"blocker" (or under a
  `## Blockers` heading); a `deferred` row needs a dated line with "deferred" plus a rationale, or
  the rationale in its own `task` cell — otherwise the row is `PROVEN_UNMET` and its batch
  classifies `blocked`. (c) `gated` primary rows do **not** block a batch by themselves: the batch
  still classifies `will_run`, the worker refuses the gated rows, and the execution parks on
  "human action needed". Cross-suite `Requires:` tokens (`SC1-B02` in an Android plan) resolve
  `UNKNOWN` = dispatch-eligible, so the only thing that keeps the wave order across suites is the
  operator activating one project at a time in wave order (§3 "Out-of-band lane"). (d) The batch
  cursor is **forward-only** in plan order; a package whose first `will_run` batch is an attended
  live walkthrough (`PY1-B00`, `WD1-B00`) hands that batch to a headless worker first. The
  migration therefore reorders each plan "Conductor-suitable first, attended last" (a plan
  amendment, recorded in `STATE.md`), and the intake `start_batch_key` picks the canary.

## 2. How to use this runbook

1. **One fresh session per step.** No step is resumed inside another session's context.
2. Set the model and reasoning from the step's own line **before** pasting.
3. `cwd` is stated per step; it is not always the same folder (see §0).
4. Paste the fenced block **exactly as it stands**. It is the whole prompt.
5. The **Watch** paragraph under a block is for you, not for the paste.
6. Every session here can spawn agents (VS Code entry point). The skills' "if this invocation can
   spawn agents" resolves to **yes**; the three project agents (`real-stack-validator`,
   `batch-closeout-reviewer`, `batch-plan-auditor`) exist in `SW_Development\.claude\agents` and,
   after step `3`, in every live suite. A session takes the inline fallback only after a real
   refused or dead Agent call and says so in its report.
7. Package files are committed in the **suite** repo; the superproject then gets a gitlink bump
   (`git add PlantLibrary_<Suite>` + commit). Sessions in this runbook may commit — they are
   ordinary sessions, not `run-batch` workers. The one exception is step `6`'s canary, where the
   worker proposes and Conductor commits.
8. Flip the step in §L in the same commit as its output.
9. Instance 2 stays **up with dispatch paused** (`POST /api/v1/projects/{id}/batch/pause`) from
   step `5` until step `6` says otherwise. Nothing in steps `0`–`4` touches the instance.

## 3. Step map — the sequence and its state

| Step | What it does | Model · reasoning | cwd | State |
|---|---|---|---|---|
| `0` | Freeze and commit what is dirty; refresh the two stale `.codex/agents` files; add the census script; open the register | **Sonnet 5 · standard** | `SW_Development` | todo |
| `1` | The skill-assumption audit the handover left undone (handbook step 7 items 1–2), with F-6/F-7 measured rather than argued | **Opus 5 · high** | `SW_Development` | todo |
| `G1` | Operator gate: decisions D1–D8 (§4) | you | — | open |
| `2a` | Schema migration recipe + PyApp package (the pilot): 15 columns, models, F-2/F-3/F-4, `SCOPE.md`, batch reorder, zero parser errors | **Sonnet 5 · thinking** | `PlantLibrary_PyApp` | todo |
| `2b` | The same recipe over Server, SharedContracts, Dashboard, AndroidApp, Workspace V1 and SDA | **Sonnet 5 · standard** | each suite folder in turn (one session per suite is allowed) | todo |
| `3` | Per-suite `CLAUDE.md`/`AGENTS.md`, skill + agent mirrors into the suites, `.tmp/` policy, README notes for the terminal packages | **Sonnet 5 · standard** | `SW_Development` | todo |
| `4` | The PyApp harness port (`scripts/harness/{regression_scope,run_validation,run_chunks}.py` + suite sentinels) proven on a synthetic touched-path set | **Opus 5 · high** (Fable 5 if available) | `PlantLibrary_PyApp` | todo |
| `5` | Register bound projects on instance 2, archive the unbound six, intake PyApp with `start_batch_key`, dispatch paused | your hands + **Sonnet 5 · standard** printing and checking | PowerShell, `SW_Development` | todo |
| `6` | The canary: `PY1-B08` through instance 2, attended; any park becomes a `FINDING_*` file, never an improvised widening | your hands + **Sonnet 5 · thinking** as the diagnosis helper | PowerShell / `PlantLibrary_PyApp` | todo |
| `G2` | Operator gate on the canary's findings: Server next, and whether step `8` is raised now | you | — | open |
| `7` | Server: harness port (the step-`4` recipe), bind, `SV1-B00` under Conductor — the V1 critical path | **Opus 5 · high** for the port; the batch runs on its own `**Model:**` (`opus/sol`) | `PlantLibrary_Server` | todo |
| `8` | The Conductor proposal: a per-project closeout adapter for non-pytest suites, routed into the master runbook's §18 gate | **Fable 5 · high** (or Opus 5 · high) | `Orchestrator_System` | todo |
| `9` | The out-of-band lane: Dashboard / AndroidApp / SharedContracts / Workspace batches by `/run-batch <suite folder> <key>` in wave order, until step `8` lands | per batch, from its `**Model:**` line (Sol → Opus 5 · high, Terra → Sonnet 5 · standard, Luna → Haiku 4.5 or Sonnet 5) | the suite folder | rolling |

Dependencies: `0` → `1` → `G1` → `2a` → `2b` → `3` → `4` → `5` → `6` → `G2` → `7`; `8` any time
after `G1` (it needs the audit, not the canary); `9` any time after `2b` + `3` for the suite in
question. Steps `2b` and `3` may run in parallel sessions on different suites.

## 4. Decisions the operator owns — gate `G1` (after step `1`)

Recommended answers are written in; overwrite the "decided" column, in the step-`1` commit or a
follow-up commit of your own, before pasting `2a`.

| ID | Decision | Recommendation (why) | decided |
|---|---|---|---|
| D1 | Which packages migrate to the 15-column schema | The **seven live** packages (six `System_V1_Implementation` + `System_Design_Architecture`). The four terminal packages and every `MVP\`/`Archive_PreMVP\` folder stay as they are, read-only, with a README note (F-10; `IMPLEMENTATION_PLAN.md` §7 already refused deletion) | |
| D2 | How to handle the closeout harness (F-6) | **Port** the three harness scripts with suite-named sentinels into **PyApp** first (step `4`), then **Server** (step `7`). Non-pytest suites run **out of band** (step `9`) until the step-`8` proposal ships a non-pytest route. Rejected: `validation.enabled: false` (moves the gap, does not close it); editing the skill mirrors (parity rule, "a prompt never overrides a skill") | |
| D3 | Where the batch skills live | Mirror `run-batch`, `plan-batch`, `real-stack-testing`, `validate-real-stack`, `test-driven-development` and the three agents into **every live suite**'s `.claude\` (and `.codex\` for parity), byte-identical, checked by the parity script — **unless** step `1` proves parent-folder discovery works from a submodule cwd, in which case only the agents are mirrored | |
| D4 | Project topology on instance 2 | One project per package, named `<Suite>` (`PlantLibrary_PyApp` binds `pyapp/System_V1_Implementation`, …). Workspace binds `System_V1_Implementation` now and gets a second project `PlantLibrary_Workspace-SDA` only after D5. Archive the six unbound projects. Active project = **PyApp** for the canary, then **Server** (`SV1-B00` is the critical path) | |
| D5 | `SDA-DEC-01..05` (design track; open since July) | Accept the five recommendations as written in `System_Design_Architecture\STATE.md` (sibling folders · fully generated tokens · native per-platform capture · Material Symbols · system font). Non-gating either way; deciding unblocks `SDA-B01..B08` for the out-of-band lane | |
| D6 | Canary batch | **`PY1-B08`** (`PY-V1-TEST-02`, `PY-V1-TEST-03`, `PY-V1-DOC-01`: headless app-e2e tier + docs; skill `none`, pure pytest, no Docker, no GUI driving). `PY1-B00` and `PY1-B06` need a human at the screen (`gui-validation`) and are unsuitable for a headless worker | |
| D7 | Batch order inside each plan (F-11 d) | Reorder "Conductor-suitable first, attended last" during migration; attended batches (`PY1-B00`, `WD1-B00`, every `gui-validation`/`android-validation` batch) get an explicit `**Requires:**` sentence naming the operator, so they classify honestly. Recorded as a dated plan amendment in each `STATE.md` | |
| D8 | Model defaults for the migration | Per batch from `IMPLEMENTATION_PLAN.md` §4 role assignments: Sol → `opus/sol`, Terra → `sonnet/terra`, Luna → `haiku/luna`; rows inherit their batch's pair except `risk: H` rows → `opus/sol`. Batches §4 does not name default to `sonnet/terra` (Appendix B lists every batch) | |

Carried, not decided here (they belong to the program, not the onboarding): the two named
security sign-offs (`AN-V1-SEC-01`, `SV-V1-SEC-01`), the release-scope confirmation of
`VGAP-020`/`SD-GAP-008` before `SV1-B00`, and the §7 backlog items of `IMPLEMENTATION_PLAN.md`
(Android HTTPS, server setup guide, Gradle 9). Each is a `/plan-batch` in its suite, later.

## 5. Step `0` — freeze, commit, and open the register

**Sonnet 5 · standard.** Housekeeping with exact targets; nothing to judge.

```text
This repository (C:\Programmierung\SW_Development, a git superproject with six submodules) is
being onboarded onto a second Conductor instance. Read
onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md §1 (findings F-9 and F-10) and
§5, then do the following in order, without waiting for approval between steps.

1. Verify the starting state and print it: git status --short here; git -C
   PlantLibrary_Workspace status --short; git submodule status. Expected: the superproject has
   the refreshed skill mirrors modified and uncommitted; PlantLibrary_Workspace has five dirty
   paths (methodology\Design_Template_Initiative\{RUNBOOK_GUI_REWORK.md,STATE.md}, two files
   under evidence\, and an untracked .claude\ folder); the other five submodules are clean on
   main. If anything else is dirty, stop and report — do not commit foreign work.
2. In PlantLibrary_Workspace: commit the five paths as they are (they are the operator's own
   in-progress Design Template Initiative work, not yours to change) with the message
   dti: commit in-progress Phase 6 records (13c/13d evidence, GUI-rework runbook, suite skills)
   Then bump the gitlink in the superproject later, in step 5 below.
3. Refresh the two stale Codex agent files by copying byte-for-byte from the dev repo:
   C:\Programmierung\Orchestrator_System\.codex\agents\batch-plan-auditor.toml and
   real-stack-validator.toml → .codex\agents\. Do not copy v5-section-reader (Conductor-only).
   Run python scripts\harness\check_harness_parity.py and make it exit 0.
4. Create scripts\harness\check_batch_packages.py with exactly the content of the runbook's
   Appendix A. Run it with C:\Programs\AI_Orchestrator_2\.venv\Scripts\python.exe (if that
   interpreter does not exist, use C:\Programmierung\Orchestrator_System\.venv\Scripts\python.exe
   and say so). Paste its full table into onboarding\REGISTER_package-census_2026-09-15.md
   under a heading "Census at step 0" — the numbers must match runbook §1b (24/35/44/26/11/18/8
   errors for the seven live packages); if they do not, report the difference and stop.
5. Extend onboarding\INDEX.md (it already lists the runbook) with the register line, then
   commit in the superproject:
   git add onboarding scripts\harness\check_batch_packages.py .codex\agents .claude .codex
   .agents PlantLibrary_Workspace
   with the message
   onboarding: step 0 — skill mirrors and agents refreshed, census script, register opened
6. Flip step 0 in the runbook §L to done with the commit hash (amend nothing; a second small
   commit "onboarding: ledger step 0" is fine).

Constraints: no edits under any submodule other than the Workspace commit in item 2; no edit to
any SKILL.md (mirrors are copied, never edited); no Conductor REST call; no change to
config.yaml of either instance.
Done when: both commits exist, git status is clean in the superproject and in all six
submodules, the parity checker exits 0, and the census file records the seven expected error
counts.
```

**Watch:** if the parity checker reports `validate-real-stack/SKILL.md` as the only difference,
that is the one allowed runtime-specific file — exit 0 is still expected. If it reports anything
else, the copy in item 3 was incomplete.

## 6. Step `1` — the skill-assumption audit (handbook step 7, items 1–2, done properly)

**Opus 5 · high.** The handover deferred this check; the runbook already knows two of its answers
(F-6, F-7) and wants them **measured** and the rest **found**. Judgment about what a skill
assumes is the whole job.

```text
This repository will be driven by Conductor instance 2 (C:\Programs\AI_Orchestrator_2, handbook
C:\Programmierung\Orchestrator_System\docs\handbook\09-second-instance.md step 7). Read
onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md §1c (F-6, F-7, F-8) first; then
read .claude\skills\run-batch\SKILL.md and .claude\skills\plan-batch\SKILL.md end to end, and
.claude\skills\validate-real-stack\SKILL.md and real-stack-testing\SKILL.md once.

Produce onboarding\AUDIT_skill-assumptions_2026-09-16.md (use today's date) with:
1. Every path, file, script, config key or convention the four skills assume exists in the
   repository they run in — one table row each: assumption · where the skill states it · which
   of the six suites satisfies it today (check each suite's tree directly, not from memory) ·
   consequence when absent (park at which seam, or a skipped leg) · owner step in the runbook.
   Include at least: scripts/harness/{run_validation,regression_scope,run_chunks}.py and
   duration_history.json; a reclaimable gitignored scratch root and the .tmp/chunks/ ledger
   path; validation.max_scope_targets read from config.yaml/config.example.yaml (which file, in
   which folder, when the worker cwd is a suite); tests/acceptance; a KNOWN_FAILURES ledger and
   --active-package; a package SCOPE.md or DRIVER_SCRIPT.md hard-scope section; CONTEXT_INDEX.md;
   DESIGN.md for design_context: required; ruff/mypy or the suite equivalents; the
   notify_telegram.py enqueue (which repo root, which instance's outbox); the three agents;
   the PlantLibrary suite-name shorthand of run-batch §1.
2. Measured, not argued: (a) from cwd C:\Programmierung\SW_Development\PlantLibrary_PyApp,
   whether a fresh claude session lists /run-batch and /plan-batch as available skills while the
   suite's own .claude\skills holds neither (parent-folder discovery). Record the exact command,
   the Claude Code version, and the observation. (b) The same from
   C:\Programmierung\SW_Development\PlantLibrary_Server. (c) Whether scripts/harness/
   regression_scope.py from the dev repo, copied unchanged into a scratch copy of PlantLibrary_
   PyApp (under .tmp\, not committed), accepts a touched-path set of one file under app\ plus
   implementation\System_V1_Implementation\TASK_CHECKLIST.md — record the refusal text verbatim.
   This is the evidence for runbook D2/D3; the runbook's default (mirror the skills into every
   suite; port the harness for PyApp and Server) stands unless (a)/(b) prove discovery works.
3. Per suite, a short list of what CLAUDE.md/AGENTS.md must state so the two skills can run
   (build/test commands, scratch policy, package location, the progress-truth rule, standing
   invariants such as PyApp's offline startup smoke) — the input for step 3, not the text itself.
4. A "recommendations for G1" section that either confirms each of D1–D8 in runbook §4 or
   proposes a change with one sentence of evidence.
If this invocation can spawn agents, delegate the six per-suite tree checks of item 1 to a
read-only agent each and merge their tables; if it cannot, do them inline and say so.
Constraints: read-only except the audit file, onboarding\INDEX.md and the runbook's §L row for
step 1; no edit to any SKILL.md, no harness file committed, no Conductor call.
Done when: the audit exists with all four sections, INDEX.md lists it, and the commit
onboarding: step 1 — skill-assumption audit
is on main in the superproject, with step 1 flipped in §L in that commit.
```

**Watch:** item 2(a)/(b) is the one measurement that can change the plan. If discovery from the
parent works, D3 shrinks to "agents only" and step `3` gets shorter; nothing else moves. If the
session cannot start a nested `claude` process, it says so and D3 keeps its default.

## 7. Step `2a` — the migration recipe, proven on PyApp

**Sonnet 5 · thinking.** Mostly mechanical, but the recipe is written once here and reused six
times; the reorder (D7) and the model defaults (D8) need a careful reading of the plan.

```text
cwd: C:\Programmierung\SW_Development\PlantLibrary_PyApp. Migrate
implementation\System_V1_Implementation to Conductor's current batch-package schema. Read
..\onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md §1c (F-1…F-4, F-11) and
Appendix B (the recipe and the model table) first, and the gate decisions in its §4. Do not
read the Conductor proposal or any MVP-era document; the package's own files and
.claude\skills\plan-batch\SKILL.md §3–§4 are the whole authority.

Do, in this order:
1. Write scripts\migrate_checklist_schema.py under ..\scripts\harness\ (superproject, so 2b can
   reuse it): given a package folder and a batch→model map, it (a) restores any row whose cell
   count is off by one only when the missing cell is unambiguous — here PY-V1-REL-02, line 40,
   whose `area` cell is missing (insert `packaging`); every other short row is an error;
   (b) rewrites the header and separator to the 15-column form of Appendix B; (c) appends the
   row's model cell from the map (batch pair; `risk: H` → opus/sol); (d) rewrites the schema
   comment block at the top to the 15-column line and the three pairs. It must preserve the
   file's line endings byte-for-byte elsewhere (read bytes, detect CRLF, write bytes) and refuse
   to run twice.
2. Run it on this package. Then by hand in BATCH_PLAN.md: add a **Model:** line to every batch
   (Appendix B table); fix PY1-B04's Requires (fold `PY1-B05` into the first sentence or move
   the "gates nothing" commentary to **Notes:**); apply D7 — reorder the sections so that the
   Conductor-suitable batches come first (PY1-B08, PY1-B01, PY1-B02, PY1-B03, PY1-B05, PY1-B04)
   and the attended ones last (PY1-B06, PY1-B00), each attended batch getting a first-sentence
   **Requires:** naming the operator at the screen; keep PY1-B07 (done) where it is.
3. Create SCOPE.md from DRIVER_SCRIPT.md's Hard scope and standing-invariant sections (the
   offline startup smoke stays a standing invariant) and add at its top: "Procedure: the
   run-batch skill; DRIVER_SCRIPT.md is legacy — its procedural sections are superseded." Do not
   delete DRIVER_SCRIPT.md.
4. Add .tmp/ to .gitignore if absent (it is present here — verify) and a
   "**2026-09-16 — plan amendment (Conductor schema migration, no code run).**" entry to
   STATE.md naming: the column and model additions (D8), the F-2 fix, the reorder (D7), the
   restored PY-V1-REL-02 cell, and the four blocked rows whose blockers this entry now records
   on one dated line each ("<ID> blocked: <reason from the row>") so the parser sees them.
5. Prove it: run ..\scripts\harness\check_batch_packages.py (instance-2 interpreter) — this
   package must show 0 errors and print one classification per batch. Expected: PY1-B07
   already_done; PY1-B08 will_run first in plan order; PY1-B03/PY1-B05 blocked (their Requires
   name todo batches); no batch not_yet_detailed. Fix anchor mismatches the census now surfaces
   (F-11 a) in TASK_CONTEXT.md, never by editing the checklist's skill/design_context cells.
6. Commit in this suite:
   PyApp: migrate System_V1_Implementation to the 15-column Conductor schema (models, SCOPE.md, reorder)
   then in ..\ the gitlink bump plus the migration script:
   onboarding: step 2a — schema migration recipe + PyApp package migrated
   and flip step 2a in the runbook §L.

Constraints: never change a row's status, task, done-when or validation text; never renumber
or reuse an ID; never edit a done row's meaning (supersede, do not edit); no product code; no
Conductor call. If the reorder would put a batch before one it Requires, keep the dependency
order and say so.
Done when: 0 parser errors, the classification list is in the report, both commits exist, the
tree is clean, and §L shows 2a done.
```

**Watch:** the census must be run with Conductor's parser, never with a hand-written table
reader — the CRLF normalisation, the `\|` cell escaping and the first-sentence lint all live in
that module. A "0 errors" from anything else is not evidence.

## 8. Step `2b` — the other six live packages

**Sonnet 5 · standard.** The recipe exists; this is repetition with per-package specifics. One
session per suite is fine; the block is written once and pasted with the suite line changed.

```text
cwd: C:\Programmierung\SW_Development\<PlantLibrary_Server | PlantLibrary_SharedContracts |
PlantLibrary_Dashboard | PlantLibrary_AndroidApp | PlantLibrary_Workspace>. Apply the step-2a
migration recipe (..\scripts\harness\migrate_checklist_schema.py, and the hand edits listed in
..\onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md Appendix B) to this suite's
implementation\System_V1_Implementation — and, in the Workspace suite only, also to
implementation\System_Design_Architecture (13 columns: insert `baseline_id` after
design_context with the value the anchor or proposal names, `GAP(sda)` where none exists, then
`model`).

Per-package specifics (from Appendix B): Server — SV1-B05 is a removed batch: demote its
heading to `### Removed batch SV1-B05 …`, keep the text; three deferred rows need their dated
rationale line in STATE.md if the row's task cell does not already carry one. SharedContracts —
nothing beyond the recipe. Dashboard — WD1-B03 removed: demote; WD1-B04 and WD1-B06 Requires
lint (`WD1-B05`); eight blocked rows need one dated blocker line each in STATE.md; WD1-B00 is
attended (D7, last). AndroidApp — AN1-B08 (`AN1-B09`, `AN1-B10`) and AN1-B11 (`AN1-B09`)
Requires lint; nine gated rows stay gated (their gates are real: SC1-B02, SDA-B02, AN1-B09,
sign-off) — give every batch whose primaries are all gated a first-sentence **Requires:** naming
the gate so it classifies blocked, not will_run; android-validation batches are attended (D7).
Workspace V1 — SY1-B05 Requires lint (`SY1-B07`); SY1-B07 runs before SY1-B05 by design
(keep the order, say so in Notes). SDA — SDA-B00 is a human decision gate: Requires
"`SDA-DEC-01..05` recorded in STATE.md" in the first sentence.

Then: SCOPE.md from DRIVER_SCRIPT.md (or from System_Tooling's SCOPE.md shape), .tmp/ in
.gitignore, the dated plan-amendment entry in STATE.md, the census at 0 errors with one
classification per batch in the report, the suite commit
<Suite>: migrate <package> to the 15-column Conductor schema (models, SCOPE.md, reorder)
the superproject gitlink bump
onboarding: step 2b — <Suite> migrated
and the §L flip (2b is done when all five suites report; note each suite on the row).
Constraints as in step 2a: no status/task/validation text changes, no renumbering, no product
code, no Conductor call.
```

**Watch:** Android and Dashboard carry the most `gated`/`blocked` rows. A batch that ends up
`will_run` with only gated primaries is a park waiting to happen (F-11 c) — the census's
classification column is the check, and "blocked" is the honest answer for those batches today.

## 9. Step `3` — `CLAUDE.md`/`AGENTS.md`, mirrors, scratch policy, README notes

**Sonnet 5 · standard.** Handbook step 7 item 3, six times, from the step-`1` audit's per-suite
list. Mechanical once the audit says what each file must state.

```text
cwd: C:\Programmierung\SW_Development. Read onboarding\AUDIT_skill-assumptions_<date>.md §3
and the runbook's §4 decisions D1 and D3, then for each of the six suites:

1. Mirrors (D3): copy byte-for-byte from this superproject into <Suite>\.claude\skills\ the five
   folders run-batch, plan-batch, real-stack-testing, validate-real-stack,
   test-driven-development, and into <Suite>\.claude\agents\ the three agent files; the same
   five skills into <Suite>\.codex\skills\ and the three .toml files into <Suite>\.codex\agents\.
   Never overwrite a suite's own skills (impeccable, gui-validation, …). If the audit's item 2
   proved parent-folder discovery, mirror the agents only and say so.
2. CLAUDE.md and AGENTS.md at the suite root (create, or extend without rewriting what is
   there): the build/test commands the audit lists; the scratch policy — `.tmp/` at the git
   root, gitignored, reclaimable, `.tmp/chunks/` for closeout ledgers, pytest basetemps under
   `.tmp/p/<slug>` (Python suites); the batch-package location
   `implementation/System_V1_Implementation/` (Workspace: plus System_Design_Architecture) and
   the rule that progress truth lives in TASK_CHECKLIST.md row statuses; the standing invariants
   from SCOPE.md by reference; the one-line pointer that this suite may be driven by Conductor
   instance 2 (worker cwd = this folder, worker commits are proposed, never made by the worker).
   PyApp: replace the reference to Improvements/GUI_Improvements_V3/DRIVER_SCRIPT_V3.md with the
   archived path or drop it. Server: keep the Docker sections intact and add the missing
   sections. Keep CLAUDE.md and AGENTS.md saying the same things (AGENTS.md may say "read
   CLAUDE.md first" plus the Codex-specific lines).
3. `.tmp/` in every suite's .gitignore; create the empty folder only where a tool needs it.
4. In PlantLibrary_Workspace\implementation\README.md add a "Conductor" paragraph: which packages
   are live (System_V1_Implementation, System_Design_Architecture after SDA-DEC), which are
   terminal and must never be bound (System_Integration_MVP, System_Tooling), and that
   strategy\ and system_description\ are outside the intake root by design. In each of the five
   suites' implementation\README.md add the equivalent two lines (live package; MVP\ folder is
   terminal evidence).
5. Run scripts\harness\check_harness_parity.py (exit 0) and, in each suite, the same parity
   idea by a byte compare of the mirrored folders against the superproject (print the result).
6. Commit per suite
   <Suite>: CLAUDE.md/AGENTS.md for Conductor-driven batches, skill and agent mirrors, .tmp policy
   then the superproject bump
   onboarding: step 3 — suite guides, mirrors and scratch policy
   and flip §L.
Constraints: no edit to any SKILL.md; no package file edits (2a/2b own them); no Conductor call.
Done when: every live suite has the mirrors (or the agents-only set, if measured), a CLAUDE.md
and AGENTS.md meeting item 2, `.tmp/` ignored, the README notes in place, all commits made,
trees clean.
```

**Watch:** mirrored skills must stay byte-identical to the dev repo's. The only tolerated
difference is `validate-real-stack/SKILL.md` between `.claude` and `.codex` (runtime-specific).
Any suite-specific need goes into `CLAUDE.md` or `SCOPE.md`, never into a skill file.

## 10. Step `4` — the PyApp harness port

**Opus 5 · high** (Fable 5 · high if available). This is the one step with real design judgment:
Conductor's harness is tied to the dev repo's test names, and the port has to keep every
fail-closed rule while renaming what it points at.

```text
cwd: C:\Programmierung\SW_Development\PlantLibrary_PyApp. Give this suite the closeout harness
a Conductor-driven batch needs, per runbook F-6 and decision D2, and prove it.

Inputs, read before designing: C:\Programmierung\Orchestrator_System\scripts\harness\
{regression_scope.py, run_validation.py, run_chunks.py} as they stand; ..\onboarding\
AUDIT_skill-assumptions_<date>.md item 2(c) (the recorded refusal); this suite's tests\ layout,
pyproject.toml and CLAUDE.md; .claude\skills\run-batch\SKILL.md §6 items 5a–8 (the exact
argv shapes the worker will emit — the port must accept them unchanged).

Design constraints: (1) run_validation.py and run_chunks.py are copied unchanged — they are
generic. (2) regression_scope.py is copied and then adapted only in its declared tables: the
sentinel tests behind STANDING_CHECK_PREFIXES and ROOT_DOC_STANDING_CHECKS must name tests that
exist in this suite — write them: tests\test_repo_hygiene.py (repo-root allowlist) and
tests\test_batch_package_contract.py (parses implementation\System_V1_Implementation with a
copy of Conductor's parser rules? No — with Conductor's parser imported from the instance-2
interpreter is not portable; instead assert the 15-column header, the status vocabulary, the
anchor/skill agreement and the Requires-lint with a small local checker, so the sentinel fails
when the package would fail Conductor's bind); the HARNESS_STANDING_CHECKS tuple names those
two; every other rule (unmapped touched path, non-collectible target, the cap, the chunk
ceiling, the ledger resolution) stays verbatim. (3) Decide and record what --active-package
resolves to when the suite has no central KNOWN_FAILURES ledger — read resolve_ledger and
state the behaviour; never fabricate a ledger; if an empty package-local ledger file is the
supported shape, create it under implementation\System_V1_Implementation\validation\ and say
which rule allows it. (4) duration_history.json: omit the file; the skill says the flag is
omitted when the file is absent. (5) Scratch: .tmp\chunks\ and .tmp\p\ under this git root;
document in CLAUDE.md.

Prove it, in the foreground, and put the transcript in implementation\System_V1_Implementation\
validation\ONBOARDING_harness-port.md: (a) python scripts\harness\regression_scope.py
app\services\sync_service.py implementation\System_V1_Implementation\TASK_CHECKLIST.md
--format json --max-targets 600 --artifact .tmp\p\hp\scope.json --summary-only → exit 0 and a
non-empty target list; (b) --plan-chunks on that scope with --max-seconds 300 → a manifest
whose exact-coverage invariant holds; (c) python scripts\harness\run_chunks.py --manifest …
--ledger .tmp\p\hp\ledger.jsonl --envelope-seconds 480 (tool timeout 600000) → exit 0 or the
documented exit 3 loop to completion, every chunk green or its red named; (d) the two sentinel
tests pass on their own; (e) a deliberately unmapped path (a .qss file under resources\ that no
test names) is refused with the verbatim unmapped-touched-path text — that refusal is the
proof the fail-closed rule survived the port.
Commit
PyApp: closeout harness (regression_scope/run_validation/run_chunks) with suite sentinels
plus the superproject bump onboarding: step 4 — PyApp harness port, and flip §L.
Constraints: no edit to any SKILL.md; nothing under .claude\; no change to the package's batch
rows; no Conductor call; never run pytest elevated; never point a basetemp outside the repo.
If the port cannot keep a fail-closed rule, stop and write onboarding\FINDING_harness-port-
<topic>_<date>.md instead of weakening the rule.
```

**Watch:** (e) is the assertion that matters. A port that makes everything green by widening the
mapping has recreated exactly the silent-skip the harness exists to prevent. A `.qss` or `.md`
under `resources\` that no test names **must** refuse.

## 11. Step `5` — register, bind, intake, hold

**Your hands + Sonnet 5 · standard** (it prints and checks each call; you run them). Every call
is loopback REST on instance 2. Nothing dispatches: the project's batch execution is paused
before the first confirm.

```text
cwd: C:\Programmierung\SW_Development (PowerShell for the calls). Read
onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md §1a, F-5, decision D4 and
Appendix C. Print each call below one at a time with its expected response, wait for the
operator's pasted output, check it, then print the next. Never run the calls yourself; never
touch instance 1 (port 8787); never edit config.yaml.

Sequence:
1. GET /api/v1/projects on http://127.0.0.1:8797 — confirm the seven rows of §1a and that
   every batch_package_path is null. Confirm git status is clean in the superproject and all
   six submodules (steps 2a–4 committed) — a dirty suite is a park at the first attempt.
2. POST /api/v1/projects with name "PlantLibrary_PyApp-V1", repo
   "C:\Programmierung\SW_Development\PlantLibrary_PyApp", batch_root_id "pyapp",
   batch_relative_path "System_V1_Implementation" → 200 with a non-null batch_package_path
   (any 422 quotes the parser: fix in the suite, commit, retry — never here).
3. POST /api/v1/projects/{new id}/activate; then PATCH each of the six old projects with
   {"archived": true} (the previously active PlantLibrary_PyApp last, after step 3 moved
   activity). GET /api/v1/projects → exactly one active project, the new one.
4. Repeat 2 (without activate) for Server, SharedContracts, Dashboard, AndroidApp and
   Workspace V1 with their root ids and "System_V1_Implementation"; a suite whose package
   still fails validation is skipped and named in the report — not fixed here. Do not create
   the SDA project (D4/D5).
5. Pause dispatch for the PyApp project: POST /api/v1/projects/{id}/batch/pause. Then intake:
   POST /api/v1/intake/batch-package with project_id and start_batch_key "PY1-B08"; confirm
   the preview through the GUI (Intake → the preview → confirm) or the confirm endpoint the
   handbook chapter 02 names; GET /api/v1/projects/{id}/batch-execution → current_batch_key
   PY1-B08, status paused, attention_reason empty.
6. Write the ids and the responses (redacted of nothing — there are no secrets here) into
   onboarding\REGISTER_package-census_2026-09-15.md under "Instance 2 registration, step 5",
   commit onboarding: step 5 — projects bound on instance 2, PyApp intake held at PY1-B08, flip §L.
Done when: six bound projects (or fewer, each absence explained), one active, the six old ones
archived, PyApp's execution paused at PY1-B08 with an empty attention_reason.
```

**Watch:** the create call validates the package with the same parser as the census; a 422 here
after a 0-error census means the tree at the path differs from what was committed (an
uncommitted edit, or a CRLF rewrite). Compare digests before retrying.

## 12. Step `6` — the canary: `PY1-B08` through instance 2, attended

**Your hands + Sonnet 5 · thinking** as the diagnosis helper in a separate session. The batch
itself runs on the worker at the batch's own `**Model:**` (`sonnet/terra`); you do not paste a
prompt into the worker.

```text
cwd: C:\Programmierung\SW_Development\PlantLibrary_PyApp (helper session). Instance 2 holds
PY1-B08 paused for project PlantLibrary_PyApp-V1. Read the runbook §1a, F-6, F-7, F-11 and
C:\Programmierung\Orchestrator_System\docs\handbook\06-monitoring-and-troubleshooting.md
(park shapes) before the operator resumes.

Preconditions the operator verifies and pastes: tree clean here; Claude worker credentials of
instance 2 fresh (C:\Conductor2\creds\claude\.credentials.json mtime within 24 h — otherwise
reauth first, handbook step 6); five-hour capacity below 70 %; validation runs list empty.
Then the operator resumes: POST /api/v1/projects/{id}/batch/resume, and watches
GET …/batch-execution every ~60 s plus the GUI batch view.

Your job: interpret each state change; when the execution parks or asks, walk back from
attention_reason to the seam (worker prompt · skill discovery · row validation · READY_FOR_
CLOSEOUT handoff · coordinator scope planning · chunk execution · recording attempt · commit
proposal) using the instance-2 log C:\Conductor2\data\conductor.log and the worker console
under C:\Conductor2\data\console-logs; name the seam and the exact text. A park is recorded,
never fixed live: write onboarding\FINDING_canary-<seam>_<date>.md (what happened, the log
lines, which runbook finding predicted it or did not, the smallest fix and where it belongs —
suite, mirror, harness port, or a Conductor proposal for step 8), add it to INDEX.md and stop.
If the batch closes: confirm the three rows are done in TASK_CHECKLIST.md, the evidence file
exists under validation\, Conductor's commit is on main in this suite with only the proposed
paths, and the cursor moved to the next will_run batch; then pause dispatch again (the next
batch is not the canary) and write onboarding\EVIDENCE_canary-py1-b08_<date>.md.
Commit whichever file you wrote with onboarding: step 6 — canary <closed | parked at <seam>>,
bump the gitlink if the suite changed, flip §L.
Constraints: no edit to the package while the attempt is live (an uncommitted edit parks it
unattributed_dirty); no answer to a Conductor question without the operator; no Git mutation
in the suite while the attempt runs.
```

**Watch:** the memory index of the dev repo lists a dozen park shapes with their walk-backs
(`Conductor instance debugging`, `Batch park: …`). Most common at a first attempt: skill not
found (F-7), harness planning failed (F-6), `unattributed_dirty` (F-9), and a worker asking a
question the operator must answer in the GUI within the AM-30 window.

## 13. Step `7` — Server: harness port, bind, `SV1-B00`

**Opus 5 · high** for the port (the step-`4` prompt with the suite line changed and Server's
sentinels: `tests\` is pytest with an in-memory SQLite conftest, no Docker needed for the default
suite). Then step `5`'s calls 2, 3 (activate Server, deactivate PyApp) and 5 with
`start_batch_key "SV1-B00"`, then step `6`'s watch. `SV1-B00`'s own `**Model:**` is `opus/sol`.
Before the resume, confirm the D-carried release-scope item (`VGAP-020`/`SD-GAP-008` stays in V1
scope) — it sizes this batch. Its done-when adds: `SV-OPENAPI-01` done, which unblocks
`SharedContracts SC1-B00` (out of band, step `9`).

## 14. Step `8` — the Conductor proposal for non-pytest suites

**Fable 5 · high** (Opus 5 · high otherwise). cwd `C:\Programmierung\Orchestrator_System`. This
is a design proposal into the Conductor track; it is executed there under its own runbook, never
here.

```text
Write implementation/Conductor_V2/proposal/PROPOSAL_per-project-closeout-adapter_<date>.md and
its INDEX.md line, for the next §18 gate of the master runbook
(planning/PROMPTS_master-continuation-runbook_2026-09-05.md). Inputs, read first:
C:\Programmierung\SW_Development\onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md
§1c F-6 and the step-6/7 findings; C:\Programmierung\SW_Development\onboarding\
AUDIT_skill-assumptions_<date>.md; src/conductor/validation.py (ValidationPlanner.scope, the
manifest re-validation), scripts/harness/regression_scope.py (STANDING_CHECK_PREFIXES,
_require_collectible_pytest_target, discover_targets); BATCH_PLAN.md batches CD2-B287…B298
(the multi-project tranche, only B286 done) and the memory-relevant v5 sections via the
v5-section-reader agent: §7.14 (closeout), §12.1 (validation config), AM-18/AM-19, AC23.

Problem to solve, stated as measured: a project whose test runner is not pytest (Vitest +
Playwright, Gradle, code generators) cannot close a batch, because the scope route refuses
every product path as unmapped and the chunk contract admits only pytest argv. Propose, as an
amendment with a config example, a state table and acceptance criteria in v5's own shape: a
per-project closeout adapter declared in the project's tree (a `scripts/harness/closeout.toml`
or the shape you argue for) that maps touched paths to runner commands with the same
fail-closed properties (unmapped → refuse; immutable manifest; per-chunk ceiling; exit-code
classification; no retries), with pytest as the shipped default adapter so the dev repo is
unchanged; how the worker-route legs in run-batch §6 would name it; what the sandbox batch
CD2-B287 must prove; and the explicit non-goals. Include the alternative you reject
(`validation.enabled: false` per project) with the reason from F-6.
Constraints: proposal only — no code, no v5 edit, no package row; naming per the deliverable
rule; commit
docs(proposal): per-project closeout adapter for non-pytest suites
and report the one line the master runbook's §18 gate needs.
```

## 15. Step `9` — the out-of-band lane (rolling)

Until step `8` lands, Dashboard, AndroidApp, SharedContracts and (the checkpoints of) Workspace
run the way every batch so far ran: one fresh VS Code session per batch, in the suite folder, at
the batch's `**Model:**`. The order is `IMPLEMENTATION_PLAN.md` §4 with the Conductor lanes
removed:

| Wave | Run (cwd = the suite folder) | Model line |
|---|---|---|
| A | `SharedContracts SC1-B00` as soon as `SV-OPENAPI-01` is done (step `7`); then `Workspace SY1-B01` | Sol · Luna |
| B (parallel, any time after `2b`+`3`) | `SharedContracts SC1-B03` · `Dashboard WD1-B06`, `WD1-B08` · `AndroidApp AN1-B11`, `AN1-B13` · `Dashboard WD1-B00` and `PyApp PY1-B00`, `PY1-B06` attended at the screen | Luna · Terra · Terra · Terra |
| C | `Server SV1-B01 → B02 → B04 → B03` (Conductor after step `7`) → `SharedContracts SC1-B02` → `Workspace SY1-B02` | Terra/Sol · Sol · Terra |
| D | `Dashboard WD1-B01 → B02` · `AndroidApp AN1-B01 → … → B07` · PyApp remainder under Conductor | Terra; Sol on `AN1-B03`, `AN1-B06` |
| E (optional, after D5) | `Workspace SDA-B01 … B08` — bind as a second Workspace project once `SDA-B00` is closed | per batch |
| F | `SV1-B06` · `WD1-B05` · `PY1-B05` · `AN1-B09` → `AN1-B10` + `SY1-B04` → `SY1-B07` → `SY1-B05` | Sol |

The paste for one out-of-band batch is exactly:

```text
/run-batch C:\Programmierung\SW_Development\PlantLibrary_<Suite>\implementation\<Package> <KEY>
Out of band, not through Conductor: run-batch proposes the commit; the operator makes it in
the suite and bumps the gitlink in the superproject. If this invocation can spawn agents, use
validate-real-stack and batch-closeout-reviewer as the skill says. Stop after the report.
```

Its done-when is the skill's: rows done or recorded blocked, the evidence file under
`validation\`, the proposed commit made by the operator, and — the one line this runbook adds —
§L's step `9` row extended with `<KEY> done <date>`.

## Appendix A — the census script (`scripts\harness\check_batch_packages.py`)

Runs Conductor's own parser over every PlantLibrary package folder and prints one line per
package: error count and kinds, or `OK` with one classification per batch. Run with
`C:\Programs\AI_Orchestrator_2\.venv\Scripts\python.exe scripts\harness\check_batch_packages.py`
from `C:\Programmierung\SW_Development`.

```python
"""Census of every PlantLibrary batch package through Conductor's real parser.

Run with the interpreter of a Conductor instance (its venv has the ``conductor``
package installed) or with the dev repo's venv; ``CONDUCTOR_SRC`` may point at
a ``src`` folder as a fallback.
"""

from __future__ import annotations

import collections
import glob
import os
import sys

_FALLBACK_SRC = os.environ.get("CONDUCTOR_SRC", r"C:\Programs\AI_Orchestrator_2\src")
try:
    from conductor.batch_package import parse_package
except ImportError:
    sys.path.insert(0, _FALLBACK_SRC)
    from conductor.batch_package import parse_package

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PATTERNS = (
    r"PlantLibrary_*\implementation\*",
    r"PlantLibrary_Workspace\strategy\*",
    r"PlantLibrary_Workspace\system_description\*",
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


def main() -> int:
    folders = sorted(
        path
        for pattern in PATTERNS
        for path in glob.glob(os.path.join(ROOT, pattern))
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, "TASK_CHECKLIST.md"))
    )
    worst = 0
    for folder in folders:
        short = os.path.relpath(folder, ROOT)
        result = parse_package(folder)
        if isinstance(result, list):
            kinds: collections.Counter[str] = collections.Counter()
            for error in result:
                kinds[next((k for k in KINDS if k in error.message), error.message[:60])] += 1
            worst = max(worst, len(result))
            print(f"{short}: {len(result)} errors -> {dict(kinds)}")
            details = [
                e.message
                for e in result
                if not any(k in e.message for k in ("no 15-column", "declares missing"))
            ]
            for message in details[:8]:
                print(f"    {message[:160]}")
            if len(details) > 8:
                print(f"    … {len(details) - 8} more")
        else:
            classes = ", ".join(f"{b.key}={b.classification}" for b in result.batches)
            print(f"{short}: OK {len(result.batches)} batches {len(result.rows)} rows :: {classes}")
    return 1 if worst else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Appendix B — the migration recipe

**B.1 The header and separator** (paste exactly; case-insensitive match, exact count):

```markdown
| ID | status | skill | design_context | baseline_id | area | file(s) | task | context | requirements | done-when | validation | risk | effort | model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

**B.2 The schema comment** at the top of each checklist replaces the `Columns (V3 schema)` line:

```text
Columns (Conductor schema, 15): ID | status | skill | design_context | baseline_id | area |
file(s) | task | context | requirements | done-when | validation | risk | effort | model
model: opus/sol | sonnet/terra | haiku/luna — the Claude tier and its Codex match, always
together; a blank cell inherits the batch's **Model:** line.
```

**B.3 Batch sections** carry one `**Model:**` line after `**Primary rows:**`:

```markdown
**Model:** `sonnet/terra`
```

**B.4 Model defaults per batch** (D8; source `IMPLEMENTATION_PLAN.md` §4 and `Todo.md`'s wave
table; unlisted batches default to `sonnet/terra`):

| Suite | `opus/sol` | `sonnet/terra` | `haiku/luna` |
|---|---|---|---|
| PyApp | `PY1-B03`, `PY1-B05` | `PY1-B00`, `PY1-B01`, `PY1-B02`, `PY1-B04`, `PY1-B06`, `PY1-B08`; `PY1-B07` (done) | — |
| Server | `SV1-B00`, `SV1-B02`, `SV1-B03`, `SV1-B06` | `SV1-B01`, `SV1-B04`, `SV1-B07` | — |
| SharedContracts | `SC1-B00`, `SC1-B02` | — | `SC1-B01` (done), `SC1-B03` |
| Dashboard | `WD1-B05` | `WD1-B00`, `WD1-B01`, `WD1-B02`, `WD1-B04`, `WD1-B06`, `WD1-B08`; `WD1-B07` (done) | — |
| AndroidApp | `AN1-B03`, `AN1-B06`, `AN1-B09`, `AN1-B10`; `AN1-B14` (done) | `AN1-B01`, `AN1-B02`, `AN1-B04`, `AN1-B05`, `AN1-B07`, `AN1-B08`, `AN1-B11`, `AN1-B13`; `AN1-B12` (done) | `AN1-B00` (done) |
| Workspace V1 | `SY1-B04`, `SY1-B05`, `SY1-B07`; `SY1-B06` (done) | `SY1-B02`; `SY1-B00` (done) | `SY1-B01`, `SY1-B03` |
| SDA | `SDA-B01`, `SDA-B02`, `SDA-B07`, `SDA-B08` | `SDA-B00`, `SDA-B03`, `SDA-B04`, `SDA-B06` | `SDA-B05` |

Rows: the batch's pair, except `risk: H` rows → `opus/sol`. A `done` row still gets a cell (the
column must be complete); use the batch's pair.

**B.5 Hand edits per package** (F-2, F-3, F-4, F-11):

| Package | Edit |
|---|---|
| PyApp | `PY-V1-REL-02` line 40: insert the missing `area` cell (`packaging`) between `release` and the file cell · `PY1-B04` Requires: `PY1-B05` out of the second sentence · reorder per D7 · four `blocked` rows (`PY-V1-REFDATA-01`, `PY-V1-CLIENT-01`, `PY-V1-TAGS-01`, `PY-V1-DS-01`) get one dated `… blocked: …` line each in `STATE.md` |
| Server | `SV1-B05` heading → `### Removed batch SV1-B05 — …` · three `deferred` rows: dated `deferred` rationale line each in `STATE.md` unless the task cell already carries date + rationale |
| SharedContracts | recipe only |
| Dashboard | `WD1-B03` heading demoted · `WD1-B04`, `WD1-B06` Requires (`WD1-B05`) · eight `blocked` rows: dated blocker lines · two `deferred` rows: rationale lines · `WD1-B00` attended, last |
| AndroidApp | `AN1-B08` (`AN1-B09`, `AN1-B10`), `AN1-B11` (`AN1-B09`) Requires · batches whose primaries are all `gated`: first-sentence `**Requires:**` naming the gate · `android-validation` batches attended, last |
| Workspace V1 | `SY1-B05` Requires (`SY1-B07`) · keep `SY1-B07` before `SY1-B05` in plan order |
| SDA | insert `baseline_id` (13 → 15) · `SDA-B00` Requires the five decisions |

**B.6 `SCOPE.md`** (per package, from `DRIVER_SCRIPT.md`): `# SCOPE — <package>` · "Procedure:
the run-batch skill; DRIVER_SCRIPT.md is legacy" · `## Hard scope` (touchable paths; read-only
paths — generated clients, sibling suites) · `## Standing invariants` (PyApp: offline startup
smoke at every batch close; Server: the live compose check where a change affects runtime
behaviour; Dashboard: `npm run build` green; Android: `gradlew assembleDebug` green;
SharedContracts: generated clients regenerate byte-stable) · `## Scratch` (`.tmp/` at the git
root).

**B.7 Proof**: `check_batch_packages.py` → `OK` for the package and one classification per batch;
no `not_yet_detailed`; every batch whose primaries are all gated/blocked classifies `blocked`.

## Appendix C — instance-2 REST calls (PowerShell, loopback only)

```powershell
$B = 'http://127.0.0.1:8797'
Invoke-RestMethod "$B/api/v1/projects" | ConvertTo-Json -Depth 4

# create bound (F-5: the only way to bind)
$body = @{ name='PlantLibrary_PyApp-V1'; repo='C:\Programmierung\SW_Development\PlantLibrary_PyApp';
           batch_root_id='pyapp'; batch_relative_path='System_V1_Implementation' } | ConvertTo-Json
Invoke-RestMethod -Method Post "$B/api/v1/projects" -ContentType 'application/json' -Body $body

Invoke-RestMethod -Method Post "$B/api/v1/projects/<id>/activate"
Invoke-RestMethod -Method Patch "$B/api/v1/projects/<old id>" -ContentType 'application/json' -Body '{"archived": true}'

# hold, intake at the canary, inspect
Invoke-RestMethod -Method Post "$B/api/v1/projects/<id>/batch/pause"
$intake = @{ project_id='<id>'; start_batch_key='PY1-B08' } | ConvertTo-Json
Invoke-RestMethod -Method Post "$B/api/v1/intake/batch-package" -ContentType 'application/json' -Body $intake
Invoke-RestMethod "$B/api/v1/projects/<id>/batch-execution" | ConvertTo-Json -Depth 6
Invoke-RestMethod -Method Post "$B/api/v1/projects/<id>/batch/resume"
```

Root ids: `pyapp`, `server`, `androidapp`, `dashboard`, `sharedcontracts`, `workspace`. Relative
path for every live V1 package: `System_V1_Implementation`; SDA: `System_Design_Architecture`.

## Appendix D — what is open, what is obsolete (the Workspace question, answered)

| Folder | State | Do |
|---|---|---|
| `implementation\System_V1_Implementation` | live: `SY1-B00`, `SY1-B06` done; `SY1-B01` two of three rows done (`SY1-SEQ-01` open); `SY1-B02..B05`, `SY1-B07` gated on the suites | migrate (2b), bind as `PlantLibrary_Workspace`, run its checkpoints out of band in wave order |
| `implementation\System_Design_Architecture` | live, gated on `SDA-DEC-01..05` (D5); 34 todo, 7 gated, 1 done; non-gating for V1 | migrate (2b); bind as a second Workspace project only after D5 |
| `implementation\System_Integration_MVP` | terminal — `SYS-B00..B16` done, MVP closed 2026-07-15 with the acceptance package | never bind; README note (step 3) |
| `implementation\System_Tooling` | terminal — `WST-B01`, `WST-B02` done 2026-07-10 | never bind; README note |
| `implementation\Server_VM_Setup` | two prompt documents | nothing |
| `strategy\Cross_Platform_Strategy` | terminal, closed 2026-07-06; outside the intake root | nothing |
| `system_description\PlantLibrary_System_Description` | terminal, frozen | nothing |
| `methodology\Design_Template_Initiative` | separate initiative, Phase 6; next step `X1` is a Conductor_V2 §18 gate in the dev repo | commit its dirty files (step 0); otherwise untouched here |
| `methodology\GUI_Improvement_Methodology` | templates v4.0.0 | nothing |
| `MVP_Reconciliation\`, `docs\`, `prompts\` | inputs of the V1 proposal | nothing |
| `WORKSPACE_STATE.md` | stale (2026-07-06) — superseded by `IMPLEMENTATION_PLAN.md` and `SUITE_HANDOFFS.md` (2026-08-04) | one line at its top pointing at both (step 3, optional) |

## L. Track ledger — flip as you go

| Step | What | Status |
|---|---|---|
| `0` | freeze + commit, agents refreshed, census script, register | done — `f6ffcd4` (superproject); `5147569` (PlantLibrary_Workspace) |
| `1` | skill-assumption audit (measured F-6/F-7) | done — `AUDIT_skill-assumptions_2026-09-15.md`; F-7 confirmed (no parent-folder discovery), F-6 confirmed with verbatim refusals |
| `G1` | decisions D1–D8 | open |
| `2a` | recipe + PyApp migrated, 0 errors | todo |
| `2b` | Server · SharedContracts · Dashboard · AndroidApp · Workspace V1 · SDA migrated | todo |
| `3` | suite guides, mirrors, scratch policy, README notes | todo |
| `4` | PyApp harness port proven (incl. the unmapped-path refusal) | todo |
| `5` | projects bound, unbound six archived, PyApp held at `PY1-B08` | todo |
| `6` | canary | todo |
| `G2` | canary findings gate | open |
| `7` | Server harness + `SV1-B00` under Conductor | todo |
| `8` | Conductor proposal: per-project closeout adapter | todo |
| `9` | out-of-band lane | rolling — `<KEY> done <date>` appended here |
