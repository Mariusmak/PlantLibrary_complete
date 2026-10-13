# Batch packages — lane A7 (read-only analysis, 2026-10-13)

*Lane `A7` of the PlantLibrary master rework program, Phase A. Read-only: no package, skill, source or instance
file was changed; the only write is this file. Pins: TARGET `SW_Development` master `8702e0a` (PlantLibrary_PyApp
`35ddc63`, Server `f1a31b9`, SharedContracts `d43f7a2`, Dashboard `7795fc8`, AndroidApp `5d6410f`, Workspace
`6b4b88b`); SOURCE-C `C:/Programmierung/Orchestrator_System` main `2e7adb3`; instance 2
`C:/Programs/AI_Orchestrator_2` (its `config.yaml` and its `src/` read, nothing else). TARGET paths are written
`<Repository>/<path>:<line>` with `SW_Development/` for the superproject; SOURCE paths are absolute. "Package" means
one of the seven live packages: six `implementation/System_V1_Implementation` plus
`PlantLibrary_Workspace/implementation/System_Design_Architecture` (SDA).*

## §0 Summary

1. All seven live packages parse with **0 errors** under the Conductor parser at `2e7adb3`; every batch
   classification equals the step-2a/2b ledger of 2026-09-15. The checker exits 1 only because four frozen packages
   are in its glob (§7.1).
2. Nothing the Conductor changed since 2026-09-16 invalidates the six step-5 bindings: the parser gained an additive,
   gate-only AM-51 set and a more tolerant model-tuple reader; `intake.py` is byte-identical on instance 2 and main;
   instance 2's `config.yaml` already lacks `max_scope_targets` and `soak` (§7.5).
3. Bind risk is concentrated in one place. PyApp's paused execution at `PY1-B08` pins `plan_contract_sha256`, so
   any B4 change to PyApp's batch order, goals, `**Model:**`, primary rows or `**Requires:**` owes an operator
   stop and re-intake. STATE.md, the non-status cells, heading tails, `DRIVER_SCRIPT.md` and README edits do not
   change that hash (F-A7-09).
4. Several classifications are clean but wrong. `SV1-B06` and `SDA-B03`/`B04`/`B08` read `will_run` because the
   parser drops their range tokens or unbackticked prerequisites. `WD1-B01`/`B02`/`B04` and `PY1-B03` read
   `already_done` with no row done, because a blocked row with a recorded blocker counts as resolved. The
   attended batches' "operator at the screen" sentences carry no token (F-A7-06, F-A7-07).
5. The model column is complete: 185 rows and 60 batches, all `opus/sol`, `sonnet/terra` or `haiku/luna`.
   `haiku/luna` (9 open rows, 4 batches) has no model on the current roster, and SDA's `MODEL_RECOMMENDATION.md`
   contradicts the column. This is recorded, not decided (Q-A7-01).
6. Row skills a worker cannot load: 38 rows name a skill their suite's `.claude/skills` does not carry
   (`android-validation` ×14 in AndroidApp, for example), and SDA names three skills that exist nowhere. This
   belongs to B1.
7. The `DRIVER_SCRIPT.md` files can retire as pointer stubs. No frozen MVP evidence cites a V1 or SDA driver, and
   only the package READMEs, two suite READMEs, two stale `run_next_batch.py` scripts and the DTI-08 hold do. The
   methodology's own `DRIVER_SCRIPT_TEMPLATE.md` is the precedent.
8. The sequencers: `IMPLEMENTATION_PLAN.md` still uniquely carries the Wave C order, the §5 operator decisions, the
   §6 environment gotchas and the §7 backlog (two items with no row anywhere). `SUITE_HANDOFFS.md` is a
   write-target of three todo Workspace rows. `V1_IMPLEMENTATION_SEQUENCE.md` is a fourth, unnoticed sequencer
   (§7.4).
9. Three rows are GUI-adjacent-only (PY-V1-DS-04, WD-V1-DS-07, AN-V1-DS-06, done) and are left alone. The token,
   impeccable and DESIGN.md rows and the whole SDA package are what B5/B6 supersede or absorb (§7.3).

## §1 Coverage

| Item | Status | Reason |
|---|---|---|
| `SW_Development/rework/PROMPT_master-rework-kickoff_2026-10-13.md` §1, §2, §4 | read | brief rule 6 |
| `SW_Development/rework/PROMPTS_master-rework-runbook_2026-10-13.md` §2–§3.1, §Q | partly read | lane list and rule digest only |
| `SW_Development/rework/REGISTER_deferred-validations_2026-10-13.md` header | read | row shape for pointers |
| SOURCE-C `.claude/skills/plan-batch/SKILL.md` (1.5.1) | read | whole file |
| SOURCE-C `.claude/skills/run-batch/SKILL.md` (282 lines) | read | whole file |
| SOURCE-C `src/conductor/batch_package.py` | partly read | 36–135, 175–215, 354–512, 515–1045, 1045–1334; dataclass bodies 136–175, 215–353 skipped |
| SOURCE-C `src/conductor/batch_discovery.py` | read | whole file |
| SOURCE-C `src/conductor/intake.py` | partly read | 258–386, 700–848 (`preview_batch_package`, `_select_start_batch`, `_confirm_batch_package`) |
| SOURCE-C `src/conductor/batch_coordinator.py` | partly read | `select_next` 1540–1596, retry verdict 1980–2000, plan-hash sites by grep |
| SOURCE-C `config.example.yaml`, `docs/handbook/09-second-instance.md`, `05-configuration-reference.md` | partly read | grep for `max_scope_targets`, `soak`, `batch_package_roots`; ladder lines 193–205; validation 120–180; intake 455–462 |
| SOURCE-C `scripts/harness/regression_scope.py`, `closeout.py` | partly read | `resolve_ledger` 1290–1325; closeout 690–705 |
| SOURCE-C git history since 2026-09-16 for parser, intake, skills, config | read | `git --no-optional-locks log/show` |
| SOURCE-C `tests/test_batch_package_out_of_band_marker.py` | partly read | docstring only (convention; nothing run) |
| Instance 2 `config.yaml` | partly read | validation block 85–103, vendors 103–140, intake roots 500–517 |
| Instance 2 `src/conductor/{batch_package,batch_discovery,intake,config}.py` | partly read | diff against main only; `config.py` grep |
| `SW_Development/.claude/skills/plan-batch/SKILL.md` (1.4.0) | read | full diff against 1.5.1 |
| `SW_Development/.claude/skills/run-batch/SKILL.md` (408 lines) | partly read | grep for the closeout / `max-targets` route |
| `SW_Development/scripts/harness/check_batch_packages.py` | read | whole file, then run once (§7.1) |
| `SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | partly read | §0–§4, §7–§8 (2a/2b), §11 (step 5), Appendices B–D, §L, §N read; §5–§6, §9–§10, §12–§15 and Appendix A not read (Appendix A is the checker, read as a file) |
| `SW_Development/onboarding/REGISTER_package-census_2026-09-15.md` | partly read | "Instance 2 registration, step 5" read; "Census at step 0" not read (superseded by the runbook's §1b) |
| `SW_Development/onboarding/AUDIT_skill-assumptions_2026-09-15.md` | partly read | grep only (D-d row, Dashboard row) |
| `SW_Development/handovers/HANDOVER_batch-package-schema-drift_2026-09-15.md` | partly read | headings and lines 1–20; its findings are superseded by the runbook's §1c |
| `SW_Development/IMPLEMENTATION_PLAN.md` | partly read | 1–30 and 177–394 read; §2–§3 (51–176, the 2026-08-04 fixes, all marked done) not read |
| `PlantLibrary_Workspace/WORKSPACE_STATE.md` | read | whole file |
| Workspace V1 `SUITE_HANDOFFS.md` | read | whole file |
| Workspace V1 `V1_IMPLEMENTATION_SEQUENCE.md` | partly read | 1–40, 95–105 |
| Workspace V1 `SKILLS.md` | not read | only line 133 by grep; lane A1's subject |
| Seven packages: `TASK_CHECKLIST.md` | read | every row's ID, status, skill, design_context, baseline_id, area, task, validation, risk, effort and model; header comments |
| Seven packages: `BATCH_PLAN.md` | partly read | every `## Batch` heading, `**Primary rows:**`, `**Model:**` and `**Requires:**`; Goal, Blockers and Notes prose not read |
| Seven packages: `STATE.md` | partly read | heading map; PyApp 1–44 and 147–228; SDA 1–14 and 118–145; dated blocker and deferral lines by grep |
| Seven packages: `SCOPE.md` | read | all seven, whole |
| Seven packages: `CONTEXT_INDEX.md` | partly read | headings and stale-reference grep; SDA 1–21 |
| Seven packages: `DRIVER_SCRIPT.md` | partly read | citation grep only; the `_ACT_STATE.md` lines from §N GC-7053 not re-read |
| Seven packages: `TASK_CONTEXT.md` | partly read | grep only (no anchor read in full; the parser's 0 errors prove that coverage and metadata agree) |
| Seven packages: `validation/` | partly read | listings; PyApp `KNOWN_FAILURES.md` read |
| SDA `MODEL_RECOMMENDATION.md` | partly read | summary and per-batch table |
| Package `README.md`, suite `README.md`, `scripts/run_next_batch.py` (Dashboard, Workspace V1) | partly read | citation grep; Workspace script docstring |
| Workspace `methodology/` (DTI-08 notes, `DRIVER_SCRIPT_TEMPLATE.md`) | partly read | lines cited in F-A7-15 |
| Hygiene decisions (superproject, PyApp, Workspace) | partly read | grep for the sequencer exemptions |

## §2 Findings

**F-A7-01 — the seven live packages are bind-clean, and the checker's red exit is noise.** The single run (§7.1)
printed `OK` for all seven with the same classifications the step-2a/2b ledger recorded
(`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:907-908`). The exit code is 1 only
because `PATTERNS` (`SW_Development/scripts/harness/check_batch_packages.py:23-27`) also globs the four frozen
packages (`System_Integration_MVP`, `System_Tooling`, `Cross_Platform_Strategy`, `PlantLibrary_System_Description`)
and `main` returns 1 on any error (`:72`). One ledger miscount: §L 2b says AndroidApp has "nine batches
`will_run`" (`…runbook…:908`), but the census shows ten (`AN1-B01`…`AN1-B08`, `AN1-B11`, `AN1-B13`). *Meaning:* B4
starts from a clean parse. B7 should make the checker's exit code reflect the live set only.

**F-A7-02 — the census measures main's parser, not instance 2's.** From `SW_Development`, the base interpreter
imports `conductor` from `C:\Programmierung\Orchestrator_System\src\conductor\__init__.py` (an editable install).
So the `CONDUCTOR_SRC` fallback (`SW_Development/scripts/harness/check_batch_packages.py:15-20`) never fires,
despite the docstring's "run with the interpreter of a Conductor instance" (`:3-5`). Instance 2's
`src/conductor/batch_package.py` (dated 2026-10-03) lacks only main's AM-51 additions, with zero removed lines
(diff: `336a337,344`, `795a804,856`, `1044a1106`, `1194a1257,1258`, `1262a1327,1328`). Importing without `-B` also
writes `__pycache__` into the imported `src` tree, which is SOURCE-C or the instance. This run used
`PYTHONDONTWRITEBYTECODE=1 python -B`. *Meaning:* B4's static proof should run the checker twice, once on main and
once with `PYTHONPATH=C:\Programs\AI_Orchestrator_2\src`, and always with `-B`.

**F-A7-03 — no parser, intake or discovery change since 2026-09-16 breaks a binding.** The commits that touched
the bind path since the onboarding are below. *Meaning:* the step-5 bindings stand (§7.5).
- `f904c8d` (2026-09-29): `parse_model_tuple` reads only the leading tuple
  (`C:/Programmierung/Orchestrator_System/src/conductor/batch_package.py:188-211`). This makes the `**Model:**`
  lines with trailing commentary parse to `opus/sol` and `sonnet/terra`
  (`PlantLibrary_Server/implementation/System_V1_Implementation/BATCH_PLAN.md:123`,
  `PlantLibrary_Workspace/implementation/System_V1_Implementation/BATCH_PLAN.md:155`). Before, the Codex slot read
  garbage.
- `6526c93` (2026-10-07): `_parse_own_records` (`…batch_package.py:810-861`). Gate-only; `_classify` and
  `_resolve_row` never read it (`:336-344` comment).
- `e19b37e` (2026-10-06): `git_root` decodes UTF-8 (`…batch_discovery.py:156-179`). The PlantLibrary paths are
  ASCII.
- `intake.py` is byte-identical on instance 2 and main (`cmp`).
- plan-batch 1.5.0/1.5.1 changed only §7 (`C:/Programmierung/Orchestrator_System/.claude/skills/plan-batch/SKILL.md:204-218`).

**F-A7-04 — instance 2's config is already in main's shape.** Its `validation` block
(`C:/Programs/AI_Orchestrator_2/config.yaml:94-102`) has no `max_scope_targets` and no `soak`. Main refuses a
config that still carries `max_scope_targets`
(`C:/Programmierung/Orchestrator_System/docs/handbook/05-configuration-reference.md:198,209`). A
`config.yaml.pre-n4-20260929.bak` sits beside it, so the change landed around 2026-09-29. The §L step-6 note
("needs its config to drop `max_scope_targets` and the `soak` block",
`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:912`) is therefore met on the config
side. The hold that remains is the policy hold `S-2`/`ob-21`. The suites still state the 600 cap: PyApp's
`scripts/harness/scope_cap.py` and the step-3 `CLAUDE.md` text (`…runbook…:909`). *Meaning:* B2/B7 retire the cap
text. B8 records that the config precondition is met.

**F-A7-05 — the closeout route drifted under the onboarding.** Main's run-batch §6.2 makes the closeout one command,
`scripts/harness/closeout.py` (`C:/Programmierung/Orchestrator_System/.claude/skills/run-batch/SKILL.md:174-190`).
The drift shows in four places:
- PyApp's step-4 port holds `regression_scope.py`, `run_validation.py`, `run_chunks.py`, `reclaim_scratch.py` and
  `scope_cap.py`, but no `closeout.py`.
- The TARGET run-batch still teaches the `--max-targets` route
  (`SW_Development/.claude/skills/run-batch/SKILL.md:209-232`).
- plan-batch 1.5.1's self-review asks every batch for a `closeout.py --predict` estimate
  (`…plan-batch/SKILL.md:208-215`), which no suite can produce today.
- Main's `resolve_ledger` dropped the "an empty foreign ledger serves everyone" fallback
  (`C:/Programmierung/Orchestrator_System/scripts/harness/regression_scope.py:1298-1321`). PyApp's ledger prose
  still describes that fallback
  (`PlantLibrary_PyApp/implementation/System_V1_Implementation/validation/KNOWN_FAILURES.md:9-18`). The local ledger
  itself still resolves first (`regression_scope.py:1302-1304`).

*Meaning:* every B4 amendment records the 1.5.1 closeout-budget item as not runnable until B7 ports `closeout.py`.
Server needs its own `validation/KNOWN_FAILURES.md` when its harness is ported.

**F-A7-06 — four kinds of `**Requires:**` text the parser cannot see.** A token counts only when it is backticked,
matches `^[A-Z0-9]+(?:-[A-Z0-9]+)+$`, and is not the batch itself or one of its primary rows
(`…batch_package.py:108`, `:1187-1193`). The four kinds, each with its effect:
- **(a) In-package ranges are dropped.** `` `SV1-B00..B04` ``
  (`PlantLibrary_Server/implementation/System_V1_Implementation/BATCH_PLAN.md:126`) is dropped, so `SV1-B06`
  classifies `will_run` while `SV1-B01`…`B04` are `blocked`. `` `SDA-DEC-01..05` `` (SDA `BATCH_PLAN.md:19`) is also
  dropped, but harmlessly: those rows are SDA-B00's own primaries.
- **(b) Unbackticked in-package keys are invisible.** SDA `BATCH_PLAN.md:86` ("SDA-B01 done"), `:105`, `:143`,
  `:161` and `:179`. As a result `SDA-B03`, `SDA-B04` and `SDA-B08` read `will_run`, as SDA's own
  `STATE.md:120-137` records and leaves.
- **(c) Cross-suite tokens resolve `UNKNOWN` and dispatch anyway** (`…batch_package.py:939-971`; intake warnings
  `…intake.py:316-321`). They appear in `PY1-B03`, `SC1-B00`, `SC1-B02`, `WD1-B01`, `WD1-B02`, `WD1-B04`, `WD1-B06`,
  `AN1-B03`, `AN1-B07`, `AN1-B10`, `AN1-B14`, `SY1-B02`, `SY1-B04` and `SY1-B07`. Cross-suite ranges are dropped
  outright: `` `SV-OPENAPI-02..05` `` (`PlantLibrary_SharedContracts/…/BATCH_PLAN.md:60`) and `` `SV1-B01..B04` ``
  (`PlantLibrary_Workspace/…/System_V1_Implementation/BATCH_PLAN.md:54`).
- **(d) "The operator at the screen" sentences carry no token.** `PlantLibrary_PyApp/…/BATCH_PLAN.md:163` and
  `:185`, `PlantLibrary_Dashboard/…/BATCH_PLAN.md:173`, `PlantLibrary_AndroidApp/…/BATCH_PLAN.md:274`. So `PY1-B06`,
  `PY1-B00` and `WD1-B00` classify `will_run`. D7's aim, that attended batches "classify honestly"
  (`…onboarding-runbook…:216`), is met only by their last place in plan order.

**F-A7-07 — a blocked row with a recorded blocker counts as resolved, so its batch reads `already_done`.**
`_resolve_row` returns `RESOLVED` for `blocked` plus a recorded blocker (`…batch_package.py:897-898`). `_classify`
then says `already_done`, and `select_next` skips it (`…batch_coordinator.py:1582-1588`). run-batch §3.4 states the
same rule (`…run-batch/SKILL.md:54-56`). Today that happens to:
- `WD1-B01`, `WD1-B02`, `WD1-B04` (`PlantLibrary_Dashboard/…/BATCH_PLAN.md:18,33,61`; the rows are recorded blocked
  at `…/STATE.md:158-173`);
- `PY1-B03` (`PlantLibrary_PyApp/…/BATCH_PLAN.md:77`; recorded at `…/STATE.md:197-204`).

None of their rows is `done`. A later Dashboard intake therefore starts past the whole live-data wave. *Meaning:*
PlantLibrary's `blocked` means "not yet startable"; the Conductor reads a recorded block as "parked and closed".
This needs a recorded convention (Q-A7-03), not a parser fix.

**F-A7-08 — in some packages the plan order breaks the dependency order.** The forward walk parks at the first
`blocked` batch (`select_next`, `…batch_coordinator.py:1582-1589`; `needs_attention`, `…intake.py:749-752`).
- **PyApp:** `PY1-B05` (`PlantLibrary_PyApp/…/BATCH_PLAN.md:96`) Requires `PY1-B04` (`:105`), which comes after it
  (`:110`). `PY1-B01` and `PY1-B02` precede their prerequisite `PY1-B00` (recorded in `…/STATE.md:186-192`).
- **Workspace V1:** `SY1-B05` (`…/BATCH_PLAN.md:95`) precedes `SY1-B07` (`:146`). The package's own `SCOPE.md:31-33`
  and Appendix B.5 (`…onboarding-runbook…:845`) say `SY1-B07` runs first; §N GC-6082 already noted the gap.
- **AndroidApp:** `AN1-B13`, which is independent (`…/BATCH_PLAN.md:226`), sits behind `AN1-B09`, which is blocked
  (`:192`).

*Meaning:* only the Workspace reorder is both needed and bind-safe. PyApp's reorder touches the held contract
(F-A7-09).

**F-A7-09 — PyApp's held execution pins its plan contract.** At confirm, the Conductor records
`plan_contract_sha256` (`…intake.py:756-767`). The hash covers batch order, key, goal, `**Model:**`, primary IDs and
Requires tokens. It does not cover heading tails, statuses or STATE prose (`…batch_package.py:1005-1018`). A retry
refuses once the hash moves (`…batch_coordinator.py:1993-1996`). PyApp's four required files have not changed
since `0be0e5a`: the later commits `73e56e2` and `faa6072` touched only package `INDEX.md`/`planning` files. *Meaning:*
B4 must either leave PyApp's contract fields alone or register a stop and re-intake at `PY1-B08` as an operator
act (B8). Server, SharedContracts, Dashboard, AndroidApp and Workspace V1 are bound with no execution, so a contract
change there owes nothing. SDA is unbound.

**F-A7-10 — 38 rows name a skill the worker cannot load from its cwd.** Step 1 measured no parent-folder skill
discovery from a suite cwd (`SW_Development/onboarding/AUDIT_skill-assumptions_2026-09-15.md:79`), and the `skill`
column is the only way a row activates a skill (`…run-batch/SKILL.md:79-90`). The suites' `.claude/skills` hold only
the five batch skills, plus `gui-validation` and `impeccable` (PyApp), `impeccable` (AndroidApp), and six suite
skills without `android-validation` (Workspace). Rows naming a missing skill:
- AndroidApp: `android-validation` ×14, `design-adoption:android` ×2, `verify-stack` ×1.
- Dashboard: `webapp-testing` ×6, `verify-stack` ×2, `design-adoption:dashboard` ×2, `impeccable:audit` ×1.
- PyApp: `verify-stack` ×1, `design-adoption:pyapp` ×2, `sync-contracts:adopt` ×1.
- Server: `sync-contracts:review` ×5.
- SharedContracts: `sync-contracts:wave` ×2.
- Workspace V1: `SY1-SMOKE-01` needs `android-validation`.

SDA also names `screenshot-capture`, `visual-review` and `external-audit:<cmd>`, which exist in no tree
(`PlantLibrary_Workspace/implementation/System_Design_Architecture/TASK_CHECKLIST.md:12,52,53,55`). *Meaning:* B1
mirrors the row-gated skills into the suites that name them. B4 changes no skill cell, except where Q-G-07 retires
`design-adoption`; then the 6 cells and their anchors change together (`…batch_package.py:1220-1240`).

**F-A7-11 — the model column is complete, and the roster gap is recorded here, not decided.** All 185 rows
(20/36/10/22/39/16/42) and all 60 batches name one of the three pairs plan-batch allows
(`C:/Programmierung/Orchestrator_System/.claude/skills/plan-batch/SKILL.md:101-110`, §7 `:201`).
- The parser is config-free (`…batch_package.py:188-211`). The coordinator maps `sol` to `gpt-5.6-sol` by suffix
  (`…batch_coordinator.py:1718`). The Claude tier names are the config ladder keys `fable/opus/sonnet/haiku`
  (`C:/Programmierung/Orchestrator_System/config.example.yaml:195-198`), where `fable` tuples are reserved for
  planning batches.
- Against the roster Fable 5.1 / Opus 5.5 / Sonnet 5.5, `haiku/luna` has no model. Nine rows are affected:
  `SC-V1-DOC-01`, `SY1-SEQ-01`, `SY1-DSG-01` and `SDA-DOC-01`…`06`. Four batches: `SC1-B03`, `SY1-B01`, `SY1-B03`
  and `SDA-B05`. Fable 5.1 has no plan-batch token.
- `SDA-DOC-01`…`04` are `risk: M` on `haiku/luna`, against the guidance (`…plan-batch/SKILL.md:107-108`).
- SDA's `MODEL_RECOMMENDATION.md` says "Haiku 4.5 is not recommended for executing any batch"
  (`…/System_Design_Architecture/MODEL_RECOMMENDATION.md:27`) and Sonnet for `SDA-B05` (`:40`). It contradicts the
  column.
- Codex is disabled on instance 2 (`C:/Programs/AI_Orchestrator_2/config.yaml:127-128`), so the right-hand half of
  every pair is unused.

**F-A7-12 — the status vocabulary is clean, but SDA's header advertises an illegal value.** No row uses a value
outside the six (`…batch_package.py:79-81`). SDA's comment still lists `skipped`
(`…/System_Design_Architecture/TASK_CHECKLIST.md:12`), and a row set to it would fail the bind parse (`:663-672`).

**F-A7-13 — SDA is stale against both G1 and the rework.**
- G1's D5 accepted the five `SDA-DEC-*` recommendations on 2026-09-15 (`…onboarding-runbook…:214`), but the
  package still records them as open (`…/System_Design_Architecture/STATE.md:21-25`), and the rows remain `gated`.
- The accepted `SDA-DEC-01` answer ("sibling folders (no `design/` restructure)", `SW_Development/IMPLEMENTATION_PLAN.md:284`)
  contradicts `Q-G-01` (a), "SharedContracts `design/`".
- `CONTEXT_INDEX.md:10` still calls `DRIVER_SCRIPT.md` the "Active execution prompt", and the file has no "Do not
  read as V1 context" section (run-batch §4.6, `…run-batch/SKILL.md:96-104`).
- `validation/` holds only `.gitkeep`.
- 36 of SDA's 42 validation cells are neither a command nor an artifact path.

*Meaning:* SDA's fate is a question (Q-A7-06). The package is unbound, so either answer carries no bind risk.

**F-A7-14 — many validation cells fall short of plan-batch §3.** That section requires a runnable command or a
concrete artifact path (`…plan-batch/SKILL.md:88-90`). Counting open rows (not `done` or `deferred`) whose cell
names neither (a heuristic: no backticks, no `validation/`):

| Package | Open rows short |
|---|---|
| AndroidApp | 30 |
| SDA | 36 |
| PyApp | 14 |
| Server | 10 |
| Dashboard | 8 |
| Workspace V1 | 8 |
| SharedContracts | 3 |

Kickoff rule 4 forbids widening these cells in Phase B. *Meaning:* B4 records pointers only, and C1 amends.
AndroidApp's `AN-V1-TEST-03` already owns its bare "UI tests" cleanup
(`PlantLibrary_AndroidApp/…/TASK_CHECKLIST.md:62`).

**F-A7-15 — who cites `DRIVER_SCRIPT.md`, and what a retirement must leave behind.**
- **Run instructions:**
  - Every package README carries a run line: PyApp `README.md:47` and `:62`; Server `:43` and `:59`;
    SharedContracts `:39` and `:54`; Dashboard `:42` and `:57`; AndroidApp `:48` and `:65`; Workspace V1 `:79` and
    `:94`; SDA `:49` and `:67`.
  - Two suite READMEs: `PlantLibrary_SharedContracts/README.md:25`, `PlantLibrary_Dashboard/README.md:22`.
  - Two stale scripts: `PlantLibrary_Dashboard/scripts/run_next_batch.py:5,79` and
    `PlantLibrary_Workspace/implementation/System_V1_Implementation/scripts/run_next_batch.py:6-8,129`. The second
    derives status from `_ACT_STATE.md`, which no live package has.
- **Other references:** SDA `CONTEXT_INDEX.md:10`; Server `openapi/README.md:10` and `scripts/export_openapi.py:9`
  (comments citing the hard scope); and the record lines in each STATE.md and hygiene decision.
- **Frozen MVP evidence cites no V1 or SDA driver.** A path-qualified grep over all seven repositories finds only
  the READMEs above and `PlantLibrary_Workspace/docs/Fable5_Prompt_Improvements`.
- **DTI-08 is waiting on this.** The methodology's relocation into the Kit waits until `SDA/README.md` and
  `SDA/DRIVER_SCRIPT.md` stop citing the in-place methodology
  (`PlantLibrary_Workspace/methodology/Design_Template_Initiative/HANDOVER.md:191`;
  `…/METHODOLOGY_RECONCILIATION.md:141-143`).
- **Nothing in the bind path needs the file.** The parser requires only four files (`…batch_package.py:53-58`), and
  run-batch accepts `SCOPE.md` in its place (`…run-batch/SKILL.md:24-26`).
- **Precedent:** `PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/DRIVER_SCRIPT_TEMPLATE.md:1-14`, a
  pointer plus a table mapping each section to its new owner.

**F-A7-16 — the sequencers are four files, and one of them is a row-maintained package organ.**
- **`SUITE_HANDOFFS.md`** is written by three todo rows: `SY1-SEQ-01`, `SY1-SEQ-02` and `SY1-DSG-01` name it in their
  `file(s)` cells (`PlantLibrary_Workspace/implementation/System_V1_Implementation/TASK_CHECKLIST.md:26,29,30`), and
  their anchors instruct updating it (`…/TASK_CONTEXT.md:50,75,175,359`). `SCOPE.md:22` and `CONTEXT_INDEX.md:6`
  point at it, and a hygiene decision exempts it (`PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md:152`).
- **`IMPLEMENTATION_PLAN.md`** is exempt and allowlisted (`SW_Development/hygiene/HYGIENE_DECISIONS.md:183,195`).
- **`WORKSPACE_STATE.md`** is exempt (`PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md:146`) and already
  bannered "superseded" (`PlantLibrary_Workspace/WORKSPACE_STATE.md:3`).
- **The fourth, which the brief did not name, is `V1_IMPLEMENTATION_SEQUENCE.md`** (2026-07-16, `8d5e1be`). It maps
  Sol/Terra/Luna to Opus 4.8 / Sonnet 5 / Haiku 4.5 (`…/V1_IMPLEMENTATION_SEQUENCE.md:10-14`) and ends at `SY1-B05`
  without the `SY1-B07` security gate (`:97-104`).

**F-A7-17 — live content only the stale sequencers carry.**
- `IMPLEMENTATION_PLAN.md` §4 orders Wave C as `SV1-B01 → SV1-B02 → SV1-B04 → SV1-B03`
  (`SW_Development/IMPLEMENTATION_PLAN.md:222-225`), against Server's plan order `B03` before `B04`
  (`PlantLibrary_Server/…/BATCH_PLAN.md:73,92`).
- `SV1-B00` "may stop after `SV-OPENAPI-01`" (`:191-193`).
- §5.2 names two security sign-offs (`:294-304`), and §5.3 asks for the `VGAP-020`/`SD-GAP-008` scope confirmation
  (`:306-314`).
- §6 lists environment gotchas (`:343-356`).
- §7's backlog (`:358-371`): Android cleartext/HTTPS and Gradle 9 have no row anywhere (grep of the AndroidApp
  package finds none). The Server setup guide is half-covered: `SV-OPS-INSTALL-01` names `deploy/SETUP_GUIDE.md`
  (`PlantLibrary_Server/…/TASK_CHECKLIST.md:52`). The remaining items are the enrichment proposal, the Fable5
  business follow-through and "keep the MVP folders".
- `SUITE_HANDOFFS.md:72-86` holds the release-ledger and security-gate rules, otherwise only in the SY1 rows.
- `WORKSPACE_STATE.md` carries nothing live; it is all MVP-era.

**F-A7-18 — the dated STATE lines are load-bearing, so B4's decision text must not name rows beside those words.**
`_parse_state_signals` records any row ID that shares a dated line, or a dated section, with
"blocked"/"blocker"/"deferred" (`…batch_package.py:752-801`). No deferred row carries a date in its `baseline_id`,
so the in-row fallback never fires (`:873-884`). The deferrals stand only on dated STATE lines
(`PlantLibrary_Dashboard/…/STATE.md:179-183`, `PlantLibrary_Server/…/STATE.md:229-232`). *Meaning:* B4 must leave
those lines as they are. Its own decision lines should name **batch keys**, not row IDs, next to those words,
unless they intend to record a blocker or a deferral.

**F-A7-19 — the Conductor already has an out-of-band marker.** The convention is the literal heading tail
`*(out-of-band; no Conductor)*` (`C:/Programmierung/Orchestrator_System/tests/test_batch_package_out_of_band_marker.py:1-16`).
It is enforced by a Conductor-repo check, not at dispatch. The heading tail lies outside the plan-contract hash,
and `(done)` detection is a plain substring test (`…batch_package.py:545`). *Meaning:* marking the attended
batches costs nothing, even in PyApp.

**F-A7-20 — `baseline_id` uses free labels.** Some cells are not a gap ID, a decision ID, a deferral or
`GAP(<short>)` (`…plan-batch/SKILL.md:73-83`): `release` (`PY-V1-REL-01`/`02`), `quality` (`WD-V1-QA-01`),
`registers` (`SY1-REL-03`), `contract-loop` (11 rows) and `plan V1-n` (AndroidApp). They are traceable, and the
parser does not care. *Meaning:* record only; editing them is churn without a gain.

## §3 Candidates

| ID | Source path @ pin | What | Verdict | Target repo and path | Lane | Q |
|---|---|---|---|---|---|---|
| RC-A7-01 | `C:/Programmierung/Orchestrator_System/src/conductor/batch_package.py` @ `2e7adb3` | The real parser as the census engine | adapt: keep PlantLibrary's checker, but (1) run with `-B`/`PYTHONDONTWRITEBYTECODE`; (2) select the parser explicitly (main vs `C:\Programs\AI_Orchestrator_2\src`) and print which one ran; (3) exit on the live set only; (4) print `plan_contract_sha256` and `status_snapshot_sha256` per package so B4/B8 can diff against the held PyApp execution | `SW_Development/scripts/harness/check_batch_packages.py` | B7 (B4 uses) | — |
| RC-A7-02 | `C:/Programmierung/Orchestrator_System/tests/test_batch_package_out_of_band_marker.py` @ `2e7adb3` (docstring) | The heading marker `*(out-of-band; no Conductor)*` for batches a headless worker must not take | adopt verbatim: append to the attended batches' headings (`PY1-B06`, `PY1-B00`, `WD1-B00`, `AN1-B10`, `SY1-B04`); hash-neutral | the five `BATCH_PLAN.md` headings | B4 | Q-A7-02 |
| RC-A7-03 | `C:/Programmierung/Orchestrator_System/.claude/skills/plan-batch/SKILL.md` @ `2e7adb3` (1.5.1) | §7 additions: no `cites:` under `validation/`; closeout-budget prediction; no proof surface in runbooks | adopt verbatim (B1 syncs the skill); B4 records the closeout-budget item as not runnable until `closeout.py` exists in the suite | `SW_Development/.claude/skills/plan-batch/` and six mirrors | B1, B4 | — |
| RC-A7-04 | `C:/Programmierung/Orchestrator_System/.claude/skills/run-batch/SKILL.md` @ `2e7adb3` §6.2 | One-command closeout (`closeout.py`) | record only here (A1/A2 own it); it decides whether PyApp's step-4 port is current | suites' `scripts/harness/` | B7 | — |
| RC-A7-05 | `C:/Programmierung/Orchestrator_System/scripts/harness/regression_scope.py:1298-1321` @ `2e7adb3` | A package-local ledger is required; an empty foreign ledger no longer serves others | adapt: Server gets an empty `validation/KNOWN_FAILURES.md` with the ledger header at its harness port (PyApp precedent); PyApp's ledger prose `:9-18` is updated to the current rule | `PlantLibrary_Server/implementation/System_V1_Implementation/validation/KNOWN_FAILURES.md`; PyApp's ledger | B7 | — |
| RC-A7-06 | `PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/DRIVER_SCRIPT_TEMPLATE.md:1-14` (TARGET's own) | Pointer plus section→owner table for a superseded driver | keep PlantLibrary's: the shape for the seven `DRIVER_SCRIPT.md` stubs | seven `DRIVER_SCRIPT.md` | B4 | Q-A7-05 |
| RC-A7-07 | `C:/Programmierung/Orchestrator_System/src/conductor/batch_coordinator.py:1540-1590` @ `2e7adb3` | `select_next`: forward-only cursor, `pinned_key`, `deferred` set-aside | record only: why the plan order matters (F-A7-08) and how an operator reaches an earlier batch | — | B4, C1 | — |
| RC-A7-08 | `C:/Programmierung/Orchestrator_System/config.example.yaml:195-198` and `batch_coordinator.py:1718` @ `2e7adb3` | Tier-name ladder (`fable/opus/sonnet/haiku`) and suffix normalization of plan tokens | record only: the evidence for Q-A7-01 | — | C1 | Q-A7-01 |
| RC-A7-09 | `C:/Programmierung/Orchestrator_System/docs/handbook/09-second-instance.md:382-440` @ `2e7adb3` | `onboard-instance` / `onboard-repository` `--check` replace hand steps 7–8 | record only: an operator act after the program, never run in it; B8 names it where the runbook's step 7 re-onboards Server | `SW_Development/onboarding/…runbook…` §13 | B8 | — |
| RC-A7-10 | `C:/Programmierung/Orchestrator_System/src/conductor/intake.py:705-767` @ `2e7adb3` | Confirm records `plan_contract_sha256`; a contract move refuses a retry | record only: the basis of the PyApp edit constraint | — | B4, B8 | Q-A7-04 |

## §4 Questions for the operator

| ID | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A7-01 | Nine open rows and four batches carry `haiku/luna`, which no roster model (Fable 5.1 / Opus 5.5 / Sonnet 5.5) matches. What does B4 do with the cells? | (a) Leave them. Record once per package STATE that the tier pair is a role and the executor picks the roster model (run-batch §4.7); C1 decides any re-tiering with the operator. (b) Re-tier them to `sonnet/terra` in B4. (c) Re-tier and also add `fable` tokens for planning batches. | Cells stay schema-valid either way. The roster can change again. Re-tiering moves the plan-contract hash of batch `**Model:**` lines for no runtime gain while nothing executes. | B4's model-column step (it can run either way; only the STATE text differs) |
| Q-A7-02 | How are attended batches (`PY1-B06`, `PY1-B00`, `WD1-B00`, `AN1-B10`, `SY1-B04`) marked so a headless worker never takes them? | (a) Append the Conductor's `*(out-of-band; no Conductor)*` heading marker and record it in STATE; statuses unchanged. (b) Flip their rows to `gated` with a dated reason. (c) Leave them as they are. | (a) changes no status, contract hash or validation cell, and reuses a shipped convention. (b) makes the operator flip rows back before every attended run. | B4 marker edits |
| Q-A7-03 | `WD1-B01`/`B02`/`B04` and `PY1-B03` read `already_done` because their blocked rows are recorded. Change anything? | (a) No status change. Record the mechanical reading in each STATE. The hand-back run-next table names their real prerequisite. A later intake uses an explicit `start_batch_key`, and the rows flip `blocked → todo` when the prerequisite lands. (b) Flip those rows to `gated` now. | (a) keeps statuses truthful and touches nothing while nothing runs. (b) still parks the worker later. | B4 STATE text; C1 run-next table |
| Q-A7-04 | May B4 change PyApp's plan contract (e.g. move `PY1-B04` before `PY1-B05`) while instance 2 holds the `PY1-B08` execution? | (a) No. Record the order defect in STATE and leave PyApp's contract fields alone, so no re-intake is owed. (b) Yes; B8 registers a stop plus re-intake at `PY1-B08` as an operator act when the hold lifts. | The cursor parks at `PY1-B01` (blocked on attended `PY1-B00`) long before `PY1-B05`, so the reorder buys nothing until `PY1-B00` has run. | B4 PyApp edits; B8 |
| Q-A7-05 | How does `DRIVER_SCRIPT.md` retire in the seven packages? | (a) Reduce each to a pointer stub: title kept; "superseded by `run-batch` + `SCOPE.md`"; a section→owner table; the last full version's commit. Repoint the README run lines to `/run-batch <package path> [key]`. (b) `git rm` plus a reference sweep. | (a) keeps every STATE and hygiene-decision mention resolvable, clears GC-7053's contradiction, and unblocks DTI-08 once SDA's README is repointed. Methodology 4.x set the precedent. | B4 DRIVER_SCRIPT step; B8 §N GC-7053 |
| Q-A7-06 | SDA's fate, given G1's D5 answers and the rework's Q-G-01 (Configuration in SharedContracts `design/`)? | (a) Supersede it by B5/B6. One dated STATE decision; open rows set `deferred` with that rationale (validation cells untouched; no renumbering; files kept; never bound). Record that D5's `SDA-DEC-01` answer is overtaken by Q-G-01. (b) Keep it live. Record D5's five answers in its Decisions table, flip the DEC rows `done`, backtick its Requires, bind it as a second Workspace project. | B5/B6 do, through the Kit, what SDA's AUTH/TOK/CON/ENF/DOC families planned. Two live design tracks would duplicate rows (plan-batch §2.1). | B4 SDA edits; B6 scoping; waits Q-G-01 |
| Q-A7-07 | Where does the living run-next table live after Q-G-05? | (a) In `SUITE_HANDOFFS.md`, re-shaped to the hand-back shape (§7.4) and still maintained by the SY1 checkpoint rows. The runbook's hand-back section is the one-time resume map pointing at it. `IMPLEMENTATION_PLAN.md`, `WORKSPACE_STATE.md` and `V1_IMPLEMENTATION_SEQUENCE.md` are archived. (b) The runbook's hand-back section is the table, and the SY1 rows' `file(s)` cells and anchors are amended to it. | Three todo rows and the Workspace scope already write `SUITE_HANDOFFS.md`. The Workspace hard scope cannot write the superproject. | B4 sequencer step; B3 archive; C1 |
| Q-A7-08 | How does B6 relate to the functional screen rows (AndroidApp `SHELL`…`MORE`, PyApp `UX-*`, Dashboard `QUERY-*`)? | (a) B6 leaves them. Its visual or IA changes that overlap a todo row go into that row's anchor as a note. B6's own work lands as new rows in its design-migration package. (b) B6 absorbs them (statuses deferred, superseded by B6 rows). | Those rows carry data and behaviour scope B6 does not own. Absorbing them would move product scope into a design lane. | B6 scoping |

## §5 Reusable things this brief did not name

- `PlantLibrary_Workspace/implementation/System_V1_Implementation/V1_IMPLEMENTATION_SEQUENCE.md:28-40`. Its
  execution-table shape (`Order | Batch | Subsystem | Status / dependency | Model | … | Run-batch command`) is the
  best existing run-next shape in TARGET; §7.4 reuses it.
- `SW_Development/scripts/harness/migrate_checklist_schema.py`, the step-2a migration script. It is the tool for any
  future column change; it preserves CRLF and refuses a second run (`…onboarding-runbook…:343-351`).
- `PlantLibrary_PyApp/tests/test_batch_package_contract.py`, which step 4 created as a local checker of the
  Conductor's bind contract (`…onboarding-runbook…:910`). Its assertions are the list a static B4 proof should
  restate in the superproject checker. It is not to be run in this program.
- `plan_contract_sha256` and `status_snapshot_sha256` (`…batch_package.py:1005-1045`), as a static fingerprint for
  "did B4 move a bound package's contract?" (RC-A7-01).
- The PyApp-side `IMPORTABLE_SOURCE_TREES` table (`PlantLibrary_PyApp/scripts/harness/regression_scope.py:273,406`).
  Main still hard-codes `src/`, with no such table in `C:/Programmierung/Orchestrator_System/scripts/harness/regression_scope.py`.
  Any re-port from main has to carry the promotion again. It is a candidate for upstreaming, recorded only (GC-1132).

## §6 Claims to verify

1. **The checker measures main's parser, not instance 2's.** From `C:\Programmierung\SW_Development` run
   `python -B -c "import conductor; print(conductor.__file__)"`. Expected:
   `C:\Programmierung\Orchestrator_System\src\conductor\__init__.py`.
2. **`SV1-B06` reads `will_run` only because its range token is dropped.** Run
   `grep -n 'SV1-B00\.\.B04' PlantLibrary_Server/implementation/System_V1_Implementation/BATCH_PLAN.md`; expected:
   line 126. Then `PYTHONDONTWRITEBYTECODE=1 python -B scripts/harness/check_batch_packages.py`; expected: the
   Server line shows `SV1-B06=will_run` next to `SV1-B01`…`SV1-B04=blocked`.
3. **Instance 2's parser lacks only main's additions.** Run
   `diff C:/Programs/AI_Orchestrator_2/src/conductor/batch_package.py C:/Programmierung/Orchestrator_System/src/conductor/batch_package.py | grep -c '^<'`.
   Expected: `0`.

## §7 Deliverables

### §7.1 Checker output

Command (run once, from `C:\Programmierung\SW_Development`, no bytecode written):
`PYTHONDONTWRITEBYTECODE=1 python -B scripts/harness/check_batch_packages.py`. It reads the packages and prints.
The parser it imported is SOURCE-C main's (F-A7-02). Exit code: **1**, caused by the four frozen packages only.

| Package | Result | Batches | Rows | `will_run` | `already_done` | `blocked` | `not_yet_detailed` |
|---|---|---|---|---|---|---|---|
| PlantLibrary_PyApp V1 | OK | 9 | 20 | 4 | 2 | 3 | 0 |
| PlantLibrary_Server V1 | OK | 7 | 36 | 3 | 0 | 4 | 0 |
| PlantLibrary_SharedContracts V1 | OK | 4 | 10 | 3 | 1 | 0 | 0 |
| PlantLibrary_Dashboard V1 | OK | 8 | 22 | 4 | 4 | 0 | 0 |
| PlantLibrary_AndroidApp V1 | OK | 15 | 39 | 10 | 3 | 2 | 0 |
| PlantLibrary_Workspace V1 | OK | 8 | 16 | 5 | 2 | 1 | 0 |
| PlantLibrary_Workspace SDA | OK | 9 | 42 | 4 | 0 | 5 | 0 |
| Workspace `System_Integration_MVP` (frozen) | 25 errors | — | — | no-15-column 1, missing primary row 24 | | | |
| Workspace `System_Tooling` (frozen) | 6 errors | — | — | no-15-column 1, missing primary row 5 | | | |
| Workspace `strategy/Cross_Platform_Strategy` (frozen) | 30 errors | — | — | no-15-column 1, missing primary row 29 | | | |
| Workspace `system_description/PlantLibrary_System_Description` (frozen) | 62 errors | — | — | no-15-column 1, duplicate 46, missing primary row 15 | | | |

Totals for the live set: 60 batches, 185 rows, 0 errors. The per-batch classifications printed are identical to
the step-2a/2b ledger (`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:907-908`).

### §7.2 Per-package edit table (for lane B4)

**Conventions for every edit below.**
- **STATE.md decision lines** use plan-batch §5.4's shape
  (`C:/Programmierung/Orchestrator_System/.claude/skills/plan-batch/SKILL.md:160-162`), dated the day B4 runs:
  `**<date> — plan amendment (rework B4: <short>, no code run).** <what + why + authority>`. They are appended
  under "Continuation updates".
- **No row ID beside "blocked", "blocker" or "deferred"** in a decision line unless it intends a record (F-A7-18).
- **Line endings:** each file is written back with its own (`git ls-files --eol`; most package files are CRLF).
- **Never touched:** validation cells.
- **Re-run the checker after every package**, twice (F-A7-02). Expected: 0 errors, classifications unchanged
  except where a row below says otherwise.

**A. Edits common to all seven packages**

| File | Wrong or missing (cite) | Exact edit | STATE.md decision text (one line) | Risk to the instance-2 bind |
|---|---|---|---|---|
| `DRIVER_SCRIPT.md` | Legacy; its procedural sections contradict `SCOPE.md` and run-batch: `_ACT_STATE.md` lines, §N GC-7053 at `…onboarding-runbook…:934`. plan-batch forbids generating one (`…plan-batch/SKILL.md:188-190`); run-batch supersedes its procedure (`…run-batch/SKILL.md:33-36`). | Per Q-A7-05 (a): replace the body with a stub. Keep the H1. Add "Superseded 2026-10-1x by the `run-batch` skill (procedure) and `SCOPE.md` (hard scope, standing invariants); full text at `<last commit>`". Add a section→owner table modelled on `PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/DRIVER_SCRIPT_TEMPLATE.md:1-14`. No deletion. | `… (rework B4: DRIVER_SCRIPT.md retired to a pointer, no code run).** DRIVER_SCRIPT.md reduced to a pointer to run-batch + SCOPE.md (Q-A7-05); last full text at <sha>; closes §N GC-7053.` | None: not a required file (`…batch_package.py:53-58`); run-batch accepts `SCOPE.md` (`…run-batch/SKILL.md:24-26`); not hashed. |
| `README.md` (package) | The run line names the driver (F-A7-15). | Replace `Execute implementation/<pkg>/DRIVER_SCRIPT.md` with `/run-batch implementation/<pkg> [<batch-key>]`. Change the file-table row to "`DRIVER_SCRIPT.md` — legacy pointer". | (covered by the line above) | None. |
| `STATE.md` | plan-batch 1.5.1 §7's closeout-budget item cannot run in any suite (F-A7-05). | One decision line, no other change. | `… (rework B4: plan-batch 1.5.1 adopted, no code run).** Self-review item "predicted closeout fits closeout_budget_s" is not runnable until scripts/harness/closeout.py exists in this suite (B7); every other 1.5.1 item applies.` | None. |
| `STATE.md` | Validation cells short of plan-batch §3 (F-A7-14); rule 4 forbids widening them now. | One decision line naming the deferred-register IDs B4 adds for this package. | `… (rework B4: validation cells pointed at, no code run).** N open rows' validation cells are left as written (kickoff rule 4) and pointed at by REGISTER_deferred-validations DV-<ids>; C1 amends them.` | None. |
| `STATE.md` | `haiku/luna` has no roster model (F-A7-11). Only in SharedContracts, Workspace V1 and SDA. | Per Q-A7-01 (a): one decision line; cells unchanged. | `… (rework B4: model tiers vs roster, no code run).** Tier pairs are roles (plan-batch §3); haiku/luna rows execute on the roster model the operator assigns; no cell changed (Q-A7-01).` | None (no cell change). Option (b) would move the plan-contract hash of the batch `**Model:**` lines. |

**B. Package-specific edits**

| Package · file | Wrong or missing (cite) | Exact edit | STATE.md decision text (one line) | Risk to the instance-2 bind |
|---|---|---|---|---|
| PyApp · `BATCH_PLAN.md:150`, `:176` | `PY1-B06` and `PY1-B00` are attended, but their operator Requires is invisible, so they read `will_run` (F-A7-06 d). | Per Q-A7-02 (a): append ` *(out-of-band; no Conductor)*` to both `## Batch` headings. | `… (rework B4: attended batches marked out of band, no code run).** PY1-B06 and PY1-B00 headings carry the Conductor's out-of-band marker; the operator sentence in their Requires is not a parser token.` | None: heading tail not hashed (`…batch_package.py:1005-1018`). The held `PY1-B08` execution is unaffected. |
| PyApp · `BATCH_PLAN.md:96-110` | `PY1-B05` precedes `PY1-B04`, which it Requires (F-A7-08). | Per Q-A7-04 (a): no move. | `… (rework B4: plan-order defect recorded, no code run).** PY1-B05 precedes its prerequisite PY1-B04 in plan order; left in place while instance 2 holds the PY1-B08 execution (Q-A7-04).` | None. Option (b) changes the contract and owes a stop and re-intake at `PY1-B08` (B8, operator). |
| PyApp · `STATE.md` | `PY1-B03` reads `already_done` with no row done (F-A7-07). | Per Q-A7-03 (a): decision line only. | `… (rework B4: mechanical reading of PY1-B03 recorded, no code run).** PY1-B03 classifies already_done because both primaries carry recorded blocks; a later intake names its start batch explicitly; rows return to todo when SC1-B00/SC1-B02 land.` | None. |
| PyApp · `validation/KNOWN_FAILURES.md:9-18` | The prose cites the retired empty-foreign-ledger fallback (F-A7-05). | Route to B7, not B4: rewrite the "why" paragraph to main's `resolve_ledger` (`regression_scope.py:1298-1321`) when the harness is re-ported. Table header unchanged. | (B7's) | None for the bind. The local ledger still resolves first. |
| Server · `BATCH_PLAN.md:126` | `` `SV1-B00..B04` `` is dropped, so `SV1-B06` reads `will_run` (F-A7-06 a). | Replace the first sentence with: ``**Requires:** `SV1-B00`, `SV1-B01`, `SV1-B02`, `SV1-B03`, `SV1-B04` done or explicitly deferred with notes (CI row covers whatever landed).`` | `… (rework B4: SV1-B06 Requires expanded, no code run).** The range token SV1-B00..B04 was invisible to the parser; five individual tokens now make SV1-B06 classify blocked until its prerequisites resolve.` | Server is bound with no execution, so the contract change owes nothing. Expected census: `SV1-B06=blocked`. |
| Server · `STATE.md` | IMPLEMENTATION_PLAN Wave C runs `SV1-B04` before `SV1-B03` (F-A7-17); the plan order is the reverse. No Requires links them. | No reorder; carry the preference into the hand-back table. | `… (rework B4: Wave C preference recorded, no code run).** IMPLEMENTATION_PLAN.md §4 preferred SV1-B04 before SV1-B03; plan order kept (no dependency); the hand-back run-next table carries the preference.` | None. |
| Server · `validation/` | No `KNOWN_FAILURES.md`; main's harness requires a package-local one (F-A7-05). | Route to B7 at the Server harness port (onboarding step 7): an empty ledger with the header, as PyApp has. | (B7's) | None for the bind; a closeout would fail without it. |
| Server · `openapi/README.md:10`, `scripts/export_openapi.py:9` | The comments cite `DRIVER_SCRIPT.md`'s hard scope. | Repoint to `SCOPE.md`. Outside the package: route to the next Server lane touching docs (B2/B3). | (none) | None. |
| SharedContracts · `BATCH_PLAN.md:60` | `` `SV-OPENAPI-02..05` `` is dropped (F-A7-06 c). | Optional: write the first sentence as `` Server `SV-OPENAPI-02`, `SV-OPENAPI-03`, `SV-OPENAPI-04`, `SV-OPENAPI-05` done for the families being published. `` | `… (rework B4: SC1-B02 Requires expanded, no code run).** The cross-suite range is written as four tokens so intake warns on each (UNKNOWN) instead of dropping them.` | Bound, no execution: owes nothing. The classification stays `will_run`. |
| SharedContracts · `README.md:25` (suite) | The suite README calls the driver "the execution prompt". | Repoint to `run-batch` (`/run-batch implementation/System_V1_Implementation [key]`). | (covered by A) | None. |
| Dashboard · `BATCH_PLAN.md:163` | `WD1-B00` is attended (F-A7-06 d). | Append ` *(out-of-band; no Conductor)*`. | `… (rework B4: attended batch marked out of band, no code run).** WD1-B00 heading carries the out-of-band marker.` | None. |
| Dashboard · `STATE.md` | `WD1-B01`, `WD1-B02`, `WD1-B04` read `already_done` with no row done (F-A7-07). | Per Q-A7-03 (a): decision line only. | `… (rework B4: mechanical reading of WD1-B01/B02/B04 recorded, no code run).** These batches classify already_done because every primary carries a recorded block; intake must name WD1-B01 explicitly once SC1-B02 lands and the rows return to todo.` | None. |
| Dashboard · `README.md:22` (suite), `scripts/run_next_batch.py:5,79` | Stale driver pointer and a stale sequencer script (F-A7-15). | README: repoint to run-batch. Script: route to B3 (banner or retire per Q-G-05; the superproject census replaces it). | (none) | None. |
| AndroidApp · `BATCH_PLAN.md:265` | `AN1-B10` is attended (F-A7-06 d). | Append ` *(out-of-band; no Conductor)*`. | `… (rework B4: attended batch marked out of band, no code run).** AN1-B10 heading carries the out-of-band marker.` | None. |
| AndroidApp · `BATCH_PLAN.md:192,226` | `AN1-B13` (independent) sits behind blocked `AN1-B09` (F-A7-08). | Record only. AndroidApp runs out of band until onboarding step 8 (F-6). | `… (rework B4: plan-order note, no code run).** AN1-B13 is independent but sits behind AN1-B09; the forward walk would park first; no move while this suite runs out of band.` | None. |
| AndroidApp · row skills | 17 rows name skills absent from the suite (F-A7-10). | Route to B1 (mirror `android-validation`, `verify-stack` and the design gate the rows name). No cell edit. | (B1's) | None for the bind; it is a worker park at preflight. |
| Workspace V1 · `BATCH_PLAN.md:95-146` | `SY1-B05` precedes `SY1-B07` against `SCOPE.md:31-33` and Appendix B.5 (F-A7-08). | Move the whole `## Batch SY1-B07` section (heading through Notes) above `## Batch SY1-B05`. No text change. | `… (rework B4: SY1-B07 moved before SY1-B05, no code run).** Plan order now matches SCOPE.md's standing ordering and onboarding Appendix B.5 (§N GC-6082).` | Bound, no execution: owes nothing. Classifications unchanged (`SY1-B07` will_run, `SY1-B05` blocked). |
| Workspace V1 · `BATCH_PLAN.md:78` | `SY1-B04` is all-gated with only cross-suite tokens, so it reads `will_run`. It is the attended cross-platform smoke. | Append ` *(out-of-band; no Conductor)*`. | `… (rework B4: SY1-B04 marked out of band, no code run).** The attended V1 smoke heading carries the out-of-band marker.` | None. |
| Workspace V1 · `SUITE_HANDOFFS.md` | A 2026-08-04 snapshot that predates the 2a/2b reorder and the instance-2 bindings (`:14`). | Per Q-A7-07 (a): re-shape to §7.4's hand-back shape. It is not a required file. | `… (rework B4: SUITE_HANDOFFS.md re-shaped, no code run).** Run-next table regenerated from the census in the hand-back shape; IMPLEMENTATION_PLAN.md and V1_IMPLEMENTATION_SEQUENCE.md superseded (Q-G-05, Q-A7-07).` | None. |
| Workspace V1 · `V1_IMPLEMENTATION_SEQUENCE.md`, `scripts/run_next_batch.py` | Stale sequencers (F-A7-16; the script reads `_ACT_STATE.md`). | Route to B3: a banner, or archive per Q-G-05. | (covered by the line above) | None. |
| SDA · whole package | Stale against G1 and the rework (F-A7-13). | Per Q-A7-06 (a): one decision line. Each open row then gets `deferred` in its status cell, with one dated STATE line per row ("`<ID>` deferred: superseded by rework B5/B6 …"), so the deferral resolves (F-A7-18). Validation cells untouched. | `… (rework B4: package superseded by the rework design lanes, no code run).** SDA's AUTH/TOK/CON/ENF/DOC/ASSET/PAR/QA families are carried by B5 (Design Configuration) and B6 (GUI rework); G1's D5 answers are recorded as overtaken by Q-G-01; the package is never bound.` | None: unbound. |
| SDA · `BATCH_PLAN.md:86,105,124,143,161,179` | Only if Q-A7-06 (b). Unbackticked in-package prerequisites read `will_run` (F-A7-06 b). | Backtick each key in the first sentence: `` `SDA-B01` done. `` (`:86`); `` `SDA-B02` and `SDA-B03` done (…). `` (`:105`); `` `SDA-B04` done (…); `SDA-DEC-01` recorded. `` (`:124`); `` `SDA-B03` done; … `` (`:143`); `` `SDA-B02`, `SDA-B03`, `SDA-B04`, `SDA-B05`, `SDA-B06` done; … `` (`:161`); `` `SDA-B01`, `SDA-B02`, `SDA-B03`, `SDA-B04`, `SDA-B05`, `SDA-B06`, `SDA-B07` done, or … `` (`:179`). | `… (rework B4: SDA Requires made parseable, no code run).** In-package prerequisites now backticked; SDA-B03/B04/B08 classify blocked honestly.` | None (unbound). |
| SDA · `TASK_CHECKLIST.md:12` | The header lists `skipped` and three nonexistent skills (F-A7-12, F-A7-10). | Replace the status list with the six-value set. Name the skill values as "historical; no such skill exists". | (covered by the SDA decision) | None; a row set to `skipped` would break the parse. |
| SDA · `CONTEXT_INDEX.md:10`, `README.md:49,67`, `MODEL_RECOMMENDATION.md` | Calls the driver "Active execution prompt"; no "Do not read as V1 context" section; model guidance contradicts the column (F-A7-11, F-A7-13). | Row 10 → "`DRIVER_SCRIPT.md` — legacy pointer". Add a `## Do not read as context` section. README run line → run-batch with the package **path** (D4). Banner at the top of `MODEL_RECOMMENDATION.md`: "superseded by the `model` column (plan-batch §3)". | (covered by the SDA decision) | None. Repointing `README.md` and `DRIVER_SCRIPT.md` releases DTI-08's precondition. |

**What B4's static proof must show** (no Conductor call):
1. **0 parser errors on all seven packages**, under main's parser and under instance 2's (`PYTHONPATH` at
   `C:\Programs\AI_Orchestrator_2\src`), both with `-B`.
2. **Classifications are unchanged** except `SV1-B06 → blocked`, plus SDA's changes if Q-A7-06 is answered.
3. **PyApp's contract is untouched:** its `plan_contract_sha256` is unchanged, computed by the parser on the tree
   before and after B4.
4. **Each package's git toplevel is its suite folder:**
   `git -C <package> rev-parse --show-toplevel` = `C:/Programmierung/SW_Development/PlantLibrary_<Suite>`.
5. **The tree is clean in each suite** at the moment of proof. Intake reads the disk, and a 422 after a clean census
   means an uncommitted edit (`…onboarding-runbook…:590-591`).

### §7.3 GUI rows

"Touches UI" here means the row changes or checks a rendered surface, tokens, theme, components, design docs or
design adoption, or carries a visual leg in its validation. Rows are never deleted or renumbered. Where a status
change is proposed, it is a STATE decision with a dated rationale, and the validation cell stays.

Relations used in the table:
- **supersedes**: B5/B6 deliver the same outcome by another route. The row is deferred with a dated rationale
  pointing at the B5/B6 deliverable.
- **absorbs**: B5/B6 do the row's work inside their own deliverable. The row closes later against that evidence.
- **leaves**: the row stays as planned.
- **needs a validation deferred**: the row's visual leg can only run after B6, and the deferred register gets a
  pointer row "after B6".

| ID | Package | Status | What it says (checklist task, abridged) | Lane B6 relation |
|---|---|---|---|---|
| PY-V1-UX-01 | PyApp | todo | Toolbar sync indicator states from `AppState` signals; contract first | leaves (functional; Q-A7-08); visual leg needs a validation deferred after B6 |
| PY-V1-UX-02 | PyApp | todo | Garden picker backed by `/gardens`, manual fallback offline | leaves (Q-A7-08) |
| PY-V1-UX-03 | PyApp | todo | "Harvest" event preset reusing `plant_event` | leaves |
| PY-V1-SYNC-ERROR-01 | PyApp | done | User-actionable sync error messages | leaves (done; never edited) |
| PY-V1-SYNC-REFRESH-01 | PyApp | done | Refresh or prompt list views after pull | leaves (done) |
| PY-V1-DS-01 | PyApp | blocked | Opportunistic SDA-B02 token inversion | supersedes (B5's Configuration plus emitted Qt artifacts replace the SDA pipeline); defer with rationale (PyApp: status snapshot only, plan contract unchanged) |
| PY-V1-DS-02 | PyApp | gated | `/impeccable audit` + `critique` over the sync-era UI | absorbs (B6's census and gap map are the audit input); needs a validation deferred (audit of the running app after B6) |
| PY-V1-DS-03 | PyApp | todo | Adopt tokens 1.2.0 in `design_tokens.py`; light/dark spot-check vs mockup | absorbs (B5 emits the stack artifacts, B6 applies them); needs a validation deferred (gui-validation spot-check); skill cell `design-adoption:pyapp+gui-validation` changes only per Q-G-07 |
| PY-V1-DS-04 | PyApp | done | Token value-diff script | leaves (done; any Kit check that replaces it is a new row) |
| PY-V1-WALK-01 | PyApp | todo | Live server/OIDC/sync walkthrough (gui-validation) | leaves; needs a validation deferred (re-run after B6 changes visuals) |
| PY-V1-REL-01 | PyApp | gated | PyInstaller packaged smoke | leaves |
| WD-V1-WALK-01 | Dashboard | todo | Live browser walkthrough of all 11 routes, screenshots | leaves; needs a validation deferred (after B6) |
| WD-V1-WALK-02 | Dashboard | todo | One UI-driven edit persisting across refresh and re-login | leaves; needs a validation deferred |
| WD-V1-QUERY-01…05, -07, WD-V1-AUTH-01 | Dashboard | blocked | Live-data reactivation of plants, locations, add wizard, search, sources/settings, tag facet; sign-out + 401 redirect | leaves (data wiring; Q-A7-08); visual legs ("live spot-check") need a validation deferred after B6 |
| WD-V1-QUERY-06 | Dashboard | deferred | Statistics history (deferred 2026-07-10) | leaves |
| WD-V1-DS-01 | Dashboard | blocked | Opportunistic switch to SharedContracts-central TS/CSS token artifacts | supersedes (B5 emits web-css from the Configuration) |
| WD-V1-DS-02 | Dashboard | todo | Author `PRODUCT.md` + `DESIGN.md` from contracts and tokens | absorbs (B5's anchoring writes the design doc layer; B6 workspace holds the product context) |
| WD-V1-DS-03 | Dashboard | todo | Install impeccable + CLAUDE.md "Design System" gating | absorbs (B5 installs impeccable and the Kit skills in Dashboard) |
| WD-V1-DS-04 | Dashboard | deferred | Contract pin, raw-literal lint, page conformance matrix | leaves (deferred); B6's mechanical design checks cover the intent; no status change |
| WD-V1-DS-05 | Dashboard | gated | `/impeccable audit` over live-validated pages | absorbs (B6 census and gap map); needs a validation deferred |
| WD-V1-DS-06 | Dashboard | todo | Adopt tokens 1.2.0: regenerate theme, role bindings, light/dark spot-check | absorbs (B5 + B6, Dashboard first per Q-G-08 (a)); needs a validation deferred (webapp-testing spot-check) |
| WD-V1-DS-07 | Dashboard | done | Token value-diff script | leaves (done) |
| WD-V1-QA-01 | Dashboard | gated | Accessibility, dark parity, long-content resilience | leaves; needs a validation deferred after B6 |
| WD-V1-TEST-01 | Dashboard | todo | Playwright mocked project, two smoke specs | leaves |
| WD-V1-TEST-02 | Dashboard | todo | Env-gated live Playwright: Keycloak login, all routes, screenshots | leaves; needs a validation deferred (screenshots after B6) |
| AN-V1-SHELL-01 | AndroidApp | todo | App scaffold: headers, safe-area, section cards, nav a11y labels | leaves (Q-A7-08); B6 IA overlaps the most here, so route notes to the anchor; visual leg needs a validation deferred |
| AN-V1-HOME-01, -02 | AndroidApp | todo | Home sections, sync health; quick add / quick log, snackbars | leaves; visual leg deferred |
| AN-V1-PLANTS-01 | AndroidApp | todo | Plants list: search, filter, sort, thumbnails, badges | leaves; visual leg deferred |
| AN-V1-DETAIL-01, -02 | AndroidApp | todo | Detail depth; not-found / tombstone / offline states | leaves |
| AN-V1-ADD-01…03 | AndroidApp | gated | Add wizard restructure; server search + manual fallback; enrichment status | leaves |
| AN-V1-ADD-04 | AndroidApp | todo | Offline quick-capture garden inbox | leaves |
| AN-V1-CARE-01…04 | AndroidApp | todo | Tasks grouping; event presets; offline UX invariants; reminder notifications | leaves |
| AN-V1-MEDIA-01, -02 | AndroidApp | todo | Detail gallery, upload state; pending-upload queue | leaves |
| AN-V1-SYNC-01, -02 | AndroidApp | todo | Rejected-outbox screen; conflict detail | leaves |
| AN-V1-SETTINGS-01, AN-V1-MORE-01 | AndroidApp | todo | Settings V1; More V1 | leaves |
| AN-V1-DS-01 | AndroidApp | gated | Opportunistic switch to generated `Tokens.kt` | supersedes (B5 emits Compose artifacts once that stack is proven emittable, A4) |
| AN-V1-DS-02 | AndroidApp | todo | Author `PRODUCT.md` + `DESIGN.md` | absorbs (B5/B6) |
| AN-V1-DS-03 | AndroidApp | todo | Install impeccable + gating section | absorbs (B5; impeccable already mirrored in AndroidApp, so the row may close on evidence) |
| AN-V1-DS-04 | AndroidApp | todo | `/impeccable audit` over validated MVP screens | absorbs (B6 census); needs a validation deferred |
| AN-V1-DS-05 | AndroidApp | todo | Adopt tokens 1.2.0 in `Color.kt`; previews/screenshots light+dark | absorbs (B5/B6); needs a validation deferred (android-validation) |
| AN-V1-DS-06 | AndroidApp | done | `Color.kt` value-diff script | leaves (done) |
| AN-V1-QA-01 | AndroidApp | gated | Accessibility, dark parity, performance | leaves; needs a validation deferred after B6 |
| AN-V1-ACC-01 | AndroidApp | gated | Android share of the cross-platform V1 smoke (walkthrough evidence) | leaves; needs a validation deferred (after B6 and the functional waves) |
| SY1-DSG-01 | Workspace V1 | todo | Checkpoint on SDA-B01/B02 progress and the opportunistic token switches | supersedes (the checkpoint's object becomes B5/B6; its done-when is re-anchored by a C1 amendment, not edited now) |
| SY1-SMOKE-01 | Workspace V1 | gated | Cross-platform V1 smoke incl. GUI, browser and emulator driving | leaves; needs a validation deferred |
| SDA-BOOT-01 | SDA | done | Bootstrap | leaves (done) |
| SDA-DEC-01…05 | SDA | gated | Folder layout, PyApp inversion, parity tooling, icon set, font policy | Q-A7-06: (a) supersedes. `DEC-01` is overtaken by Q-G-01; `DEC-02`…`05` become B5/B6 design decisions recorded in the Configuration |
| SDA-AUTH-01…04 | SDA | todo | Consolidate design authority into SharedContracts | supersedes (B5: the Configuration in SharedContracts `design/` per Q-G-01) |
| SDA-TOK-01…05 | SDA | todo | Token pipeline, generator, suite switches | supersedes (B5: Kit import + emit-stack; the stacks per A4) |
| SDA-CON-01…05 | SDA | todo | Contract set authoring (page/pattern contracts, terminology) | absorbs (B6: screen contracts under methodology 4.1.0) |
| SDA-ENF-01…06 | SDA | todo | Enforcement and CI (lints, drift hashes, conformance matrix) | supersedes (Kit static checks + design gate) |
| SDA-DOC-01…06 | SDA | todo | Instruction-file layer (`CLAUDE.md`, `DESIGN.md`) | absorbs (B5 rule blocks; B2 instruction files) |
| SDA-ASSET-01…04 | SDA | todo | Asset and data contracts, parity scenario | absorbs (B6; icon and font decisions inside the Configuration) |
| SDA-PAR-01…03 | SDA | gated / todo | Parity baseline capture, visual review, reconciliation | absorbs (B6 mockups and gap map); needs a validation deferred (screenshots, after B6) |
| SDA-QA-01, -02, SDA-ACCEPT-01 | SDA | todo | Final QA, anchoring, acceptance | supersedes (B6 closure and C1 hand-back) |

### §7.4 Sequencers

**What only they carry today**

| Content | Where (cite) | Carried anywhere else? | Goes to |
|---|---|---|---|
| Cross-suite dependency chain Server → SharedContracts → clients → hardening → smoke → security gate → release | `SW_Development/IMPLEMENTATION_PLAN.md:183-269`; `PlantLibrary_Workspace/…/SUITE_HANDOFFS.md:36-70` | Partly, in the batch Notes; never as one order | hand-back §H.2 |
| Wave C order `SV1-B01 → B02 → B04 → B03 → SC1-B02 → SY1-B02` | `IMPLEMENTATION_PLAN.md:222-225` | No (the Server plan order differs) | hand-back §H.2; Server STATE line (§7.2) |
| "`SV1-B00` may stop after `SV-OPENAPI-01`; that row is the only hard prerequisite of `SC1-B00`" | `IMPLEMENTATION_PLAN.md:191-193` | No | hand-back §H.2 note on `SV1-B00` |
| Model role meanings (Sol/Terra/Luna) | `IMPLEMENTATION_PLAN.md:179-181`; `V1_IMPLEMENTATION_SEQUENCE.md:10-14` (outdated models) | Yes, now the `model` column (plan-batch §3) | dropped (superseded); the roster mapping is Q-A7-01 |
| Operator-only decisions: SDA-DEC (§5.1), the two named security sign-offs `AN-V1-SEC-01` / `SV-V1-SEC-01` (§5.2), `VGAP-020` scope confirmation before `SV1-B00` (§5.3) | `IMPLEMENTATION_PLAN.md:271-314` | §5.2/§5.3 only as a "carried" note (`…onboarding-runbook…:219-221`) | hand-back §H.3, and as `Q-` rows in the operator register for C1 |
| Environment gotchas: Docker `desktop-linux` context, the api container has no test runner, disposable `python:3.14-slim`, GUI focus | `IMPLEMENTATION_PLAN.md:343-356` | Partly, in `PlantLibrary_Server/CLAUDE.md` and the gui-validation skill | the suite `CLAUDE.md` files (B2); hand-back §H.5 points there |
| Unplanned backlog: Android cleartext/HTTPS, Server setup guide, Gradle 9, server-side enrichment proposal, Fable5 business follow-through, MVP folders kept read-only | `IMPLEMENTATION_PLAN.md:358-371` | HTTPS and Gradle 9: no row (grep). Setup guide: half in `SV-OPS-INSTALL-01`. The rest: no | a `REGISTER_unplanned-backlog_<date>.md` under `rework/` (Q-G-05 (a), with `Todo.md`'s live ideas); each item marked "needs plan-batch in <suite>" for C1 |
| Binding rules recap (contract-first regen, Android gate, Dashboard honesty, PyApp offline, release ledger, security gate) | `SUITE_HANDOFFS.md:72-86` | Contract, Dashboard and PyApp rules are in the `SCOPE.md` files; the release ledger and security gate are only here and in SY1 rows | hand-back §H.5 (pointers), and kept in `SUITE_HANDOFFS.md` under Q-A7-07 (a) |
| Run-next table | `SUITE_HANDOFFS.md:19-34` (2026-08-04 snapshot) | No current one | `SUITE_HANDOFFS.md` re-shaped (Q-A7-07 (a)) |
| MVP-era suite status, blockers, methodology convention, folder rename note | `PlantLibrary_Workspace/WORKSPACE_STATE.md:7-63` | Nothing live (MVP closed 2026-07-15; `SD-GAP-005` is `SV-OPS-BACKUP-01`'s baseline; `SD-GAP-006` closed by `SC-DOC-01`) | archive (Q-G-05 (a)) |
| V1 order with run-batch commands per batch | `PlantLibrary_Workspace/…/V1_IMPLEMENTATION_SEQUENCE.md:28-104` | Superseded; it misses `SY1-B07` | archive; its table shape is reused below |

**Shape of the runbook's hand-back section that replaces them** (evidence for Q-G-05). The headings are below. The
section is written by C1 and lives in the master runbook. Under Q-A7-07 (a), only §H.1 is copied into
`SUITE_HANDOFFS.md` as the row-maintained living table.

- `## H. Hand-back — what runs next` (one paragraph: row statuses are the truth; this section is derived from the
  census of `<date>` at `<commit>`, regenerated by `scripts/harness/check_batch_packages.py`; it replaces
  `IMPLEMENTATION_PLAN.md`, `WORKSPACE_STATE.md` and `V1_IMPLEMENTATION_SEQUENCE.md`)
- `### H.1 Run-next table`, with these columns:

  | Order | Package (path) | Batch | Classification (census) | Route | Model | Waits on | Deferred validations |
  |---|---|---|---|---|---|---|---|
  | `<wave>.<n>` | `PlantLibrary_<Suite>/implementation/<pkg>` | `<KEY> — <title>` | `will_run` / `blocked` / `already_done*` (`*` = recorded-block reading, F-A7-07) | `instance 2` / `out of band` / `attended` | the batch's `**Model:**` pair | tokens incl. cross-suite and operator acts | `DV-<nn>` ids |

  The Route column states what the parser cannot know. Rows are grouped by wave A–F.
- `### H.2 Cross-suite order` (the dependency chain with its wave labels; the Wave C preference; the `SV1-B00`
  early-handoff note; "`SY1-B07` before `SY1-B05`").
- `### H.3 Operator decisions on the path` (security sign-offs, `VGAP-020` confirmation, open `Q-` rows, and
  instance-2 acts such as a re-intake if Q-A7-04 (b) or the S-2 hold lift).
- `### H.4 Backlog without rows` (a pointer to the `rework/` backlog register; each item's target suite; "needs
  plan-batch").
- `### H.5 Binding rules and environment` (pointers to the `SCOPE.md` files and suite `CLAUDE.md`; the release
  ledger and security gate rules restated once).
- `### H.6 Instance 2` (bound projects and ids from `SW_Development/onboarding/REGISTER_package-census_2026-09-15.md`;
  PyApp held at `PY1-B08`; the stated precondition for each next intake).
- `### H.7 Archived sequencers` (old path → archive path, with the hygiene decision id).

### §7.5 Instance 2's bind contract

**What the Conductor requires today (`2e7adb3`; instance 2 identical on these paths except the AM-51 additions)**

| Check | Where | Requirement |
|---|---|---|
| Root allowlist | `C:/Programmierung/Orchestrator_System/src/conductor/batch_discovery.py:39-57,67-84` | The configured root exists and is a directory. The package path is relative to the root id (`pyapp` → `…\PlantLibrary_PyApp\implementation`, `C:/Programs/AI_Orchestrator_2/config.yaml:505-517`), never absolute, and does not escape the root by `..` or a reparse point. |
| Package exists and parses clean | `…batch_discovery.py:129-136` | A directory whose `parse_package` returns no errors. Required files: `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md` (`…batch_package.py:53-58`). `SCOPE.md`, `CONTEXT_INDEX.md`, `DRIVER_SCRIPT.md` and `validation/` are not checked. |
| Parse-clean means | `…batch_package.py:610-700, 1146-1240` | A 15-column header (case-insensitive, exact count); every row has 15 cells; status in the six-value set; unique IDs; safe output paths in validation options; every batch has a Goal; primary rows exist and are assigned to one batch; no known ID after the first sentence of Requires/Primary rows; one anchor per row whose `skill`/`design_context` equal the row's. |
| Not bound twice | `…batch_discovery.py:138-144` | No other project binds the same package path. |
| Inside the submitted repo | `…batch_discovery.py:146-151` | The package lies inside `repo`, which is the suite folder (`SW_Development/onboarding/REGISTER_package-census_2026-09-15.md:64-68`). |
| Git root | `…batch_discovery.py:156-179`; `…intake.py:285-291` | `git rev-parse --show-toplevel` from the package resolves, and becomes the worker cwd. For PlantLibrary that is the submodule, not `SW_Development`. Two projects on one git root raise the shared-tree acknowledgement (`…intake.py:715-720`): this matters for Workspace V1 + SDA. |
| Intake preview | `…intake.py:260-359` | Parses again; selects a start batch (the first not `already_done`, or the requested one unless its Requires are `PROVEN_UNMET`, `:361-378`); snapshots the file hashes; warns on each `UNKNOWN` requirement. |
| Confirm | `…intake.py:705-767` | The package content hash equals the preview's (else `PackageDriftError`). Records `plan_contract_sha256` and `status_snapshot_sha256` on the execution. |
| After confirm | `…batch_coordinator.py:1993-1996`, `:6130-6135` | A moved plan contract refuses the exact retry, or re-anchors only when attributable. A status change does not refuse. |

**What a B4 static check must prove without calling the instance:**
1. **Parse-clean under both parsers.** All seven packages, with `-B`, under main's parser and instance 2's.
2. **Every required file is committed and the suite tree is clean.** Intake hashes the disk.
3. **Each git toplevel is the suite folder.**
4. **Each package path is `<root>\<relative>`** with relative `System_V1_Implementation` (SDA:
   `System_Design_Architecture`), under the root that `config.yaml:505-517` names.
5. **PyApp's plan contract is unchanged** against the tree at `0be0e5a`, or a re-intake is registered for B8
   (Q-A7-04).
6. **No batch reads `not_yet_detailed`**, and every change in classification is explained by a STATE decision.

**Does anything since 2026-09-16 invalidate the step-5 bindings? No.**
- **Parser:** `f904c8d` is tolerant only. `6526c93` is additive and gate-only. The census is unchanged.
- **Discovery:** `e19b37e` is UTF-8 only.
- **Intake:** byte-identical.
- **Config:** `max_scope_targets` was retired at `CD2-B389` and is already absent from instance 2. `quiet_windows`
  (`8fc01da`) defaults to `[]`. `closeout_lease_path` is present on instance 2 (`config.yaml:102`).

What did change sits beside the bind, not in it:
- the closeout route (`closeout.py`, F-A7-05);
- the one-command onboarding verbs `onboard-instance` / `onboard-repository` (handbook 09 step 8,
  `C:/Programmierung/Orchestrator_System/docs/handbook/09-second-instance.md:382-440`), which a re-onboarding of
  Server at runbook step 7 would use;
- instance 2's role as the staging instance (`S-2`; `…onboarding-runbook…:912`).

None of these needs a re-bind. They need a harness port (B7) and operator acts after the program.

### §7.6 The §N notes

| Census row (§N, `SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:929-934`) | What lane B8 must do | Home |
|---|---|---|
| `GC-1132` — PyApp `IMPORTABLE_SOURCE_TREES` promotion unreviewed (`PlantLibrary_PyApp/scripts/harness/regression_scope.py:273,406`) | **Operator act + file edit.** The operator reviews the one table entry against PyApp's importable trees. B8 writes the dated outcome line into `ONBOARDING_harness-port.md` and appends "reviewed" to §L step 4. Note for B7: main's `regression_scope.py` still has no such table, so a re-port must carry it again. | `PlantLibrary_PyApp/implementation/System_V1_Implementation/validation/ONBOARDING_harness-port.md`; onboarding runbook §L step 4 |
| `GC-2006` — AndroidApp "unit tests pass" is vacuous (0 test sources) | **Nothing to edit.** Owned by `AN-V1-TEST-01`…`03` (todo). B8 confirms that the hand-back run-next table and the deferred register carry the fact. | AndroidApp checklist rows; `SW_Development/rework/REGISTER_deferred-validations_2026-10-13.md` |
| `GC-6082` — D7 reorder and `SCOPE.md` invariants; two items unchecked | **File edit, done by B4** (B8 verifies statically): `SY1-B07` moved before `SY1-B05` (§7.2). The second unchecked item is answered here. The attended batches' first-sentence operator Requires exist (PyApp `BATCH_PLAN.md:163,185`; Dashboard `:173`; AndroidApp `:274`) but carry no token (F-A7-06 d), so the out-of-band marker (Q-A7-02) is what makes them honest. SDA plan order: `SDA-B00`…`B08` numeric; moot under Q-A7-06 (a). | Workspace V1 `BATCH_PLAN.md`/`STATE.md`; onboarding runbook §N row |
| `GC-2431` — SharedContracts `CONTRACT_VERSION.md` 1.2.0 vs `CLIENT_MANIFEST.md` 1.1.0 | **Nothing.** Owned by `SC-SYNC-REGEN-01`/`SC-VER-01` (`SC1-B00`). A generated file is never hand-edited. | SharedContracts V1 package |
| `GC-2437` — PyApp `.gitignore` dead lines | **File edit (trivial)**: delete `PlantLibrary_PyApp/.gitignore:11-14`, verified still present on 2026-10-13. Whichever lane next commits PyApp's `.gitignore` does it (B3 or B8). | `PlantLibrary_PyApp/.gitignore` |
| `GC-7053` — `DRIVER_SCRIPT.md` reads and appends `_ACT_STATE.md` | **Closed by B4's pointer stubs** (Q-A7-05 (a)). B8 flips the §N row to "closed by B4 `<commit>`" and checks that no `_ACT_STATE.md` instruction remains in the seven files. | the seven `DRIVER_SCRIPT.md`; onboarding runbook §N |

Also owed in B8, from this audit:
- In §L step 6, record that instance 2's `config.yaml` already lacks `max_scope_targets` and `soak` (F-A7-04).
- Correct §L 2b's AndroidApp count from nine to ten `will_run` (F-A7-01).
