# Harnesses and scripts — lane A2 (read-only analysis, 2026-10-13)

*Lane `A2` of the PlantLibrary master rework program, Phase A (`PROMPT_master-rework-kickoff_2026-10-13.md` §1, §2).
Read-only: nothing under SOURCE-C (`C:\Programmierung\Orchestrator_System` @ `2e7adb3`) or SOURCE-K
(`C:\Programmierung\Repo_Hygiene_Template_Kit` 0.2.1; `C:\Programmierung\Design_Template_Kit` @ `f08e588` read for one
comparison) was written; no script was executed; git reads only (`--no-optional-locks` in SOURCE-C). TARGET pins:
superproject `8702e0a`, Workspace `6b4b88b`, PyApp `35ddc63`, AndroidApp `5d6410f`, Dashboard `7795fc8`, Server
`f1a31b9`, SharedContracts `d43f7a2`. Citations: absolute paths for sources; `SW_Development/…` for the superproject and
`PlantLibrary_<Suite>/…` for submodules. Every behavioural claim about a script is from reading it, never from running it.*

## §0 Summary

1. The Conductor harness is nine files (`scripts/harness/*`); four of them were ported to PyApp at onboarding step 4 from Conductor `7ad02b1` (2026-09-16). Three copies are content-identical to that pin; `regression_scope.py` differs only in the declared tables and the `_module_for_path` promotion (measured, §6 claim 1).
2. Since the port the Conductor harness moved 24 commits (+9,690 / −1,241 lines): `closeout.py` (3,402 lines, one-command closeout, born 2026-09-18) and `durations_flush.py` are new. The `max_scope_targets` cap that PyApp's `scope_cap.py` serves was retired upstream on 2026-09-19 (`35429ea`).
3. No current Conductor harness file can be copied unchanged into a PlantLibrary suite. `reclaim_scratch.py` now loads `src/conductor/scratch_sweep.py`. `closeout.py` reads `config.yaml`, calls the instance REST API and imports `conductor.batch_package`. `regression_scope.py` still hard-codes `src/`. `run_validation.py` reads `pyproject.toml` on every command, so it would break in the four suites that have none.
4. The Conductor's answer to "harness for any repository" is proposal A: a `.conductor/project.yaml` layout plus `pytest`/`command`/`gradle`/`npm`/`contracts` profiles. Its harness half (`CD2-B543`…`B547`, rows `CD-V2-HRN-195`…`-208`) is all `todo`. The gradle/npm/contracts steps for SharedContracts, Dashboard and Android (`ob-25`) are deliberately not written yet. Onboarding step 8 (a PlantLibrary-written adapter proposal) has been overtaken by proposal A.
5. Recommendation (Q-A2-01): keep PyApp's `7ad02b1` port as it is through Phase B and re-port once, as one set, after proposal A's harness half ships. Phase B ports only static guards.
6. The hygiene kit already covers naming, INDEX, roots, the prompt proof-surface guard, the rule block, the decision record, the root allowlist and scratch. B7 must not port the Conductor's `test_prompt_proof_surface_hygiene.py`, `test_docs_naming_hygiene.py` or the root-allowlist part of `test_repo_hygiene.py` a second time. Four guards the kit does not cover:
   - the package-file mixed-newline guard;
   - suite mirror parity;
   - docs link/anchor integrity across all repositories;
   - the parser-backed package census.
7. Finding: the superproject's `check_harness_parity.py` compares only the superproject's own `.claude`/`.codex`. Every suite's `CLAUDE.md` says that checker guards the suite mirrors, and nothing does. The mirrors are byte-identical today (measured).
8. Finding: `run-batch` §6 item 1 (mirrored into all six suites) mandates `scripts/harness/run_validation.py` for any command over 60 s, but only PyApp has the script.
9. Living-documentation standard: zero TARGET pages carry its head/foot shape. The one corpus it would fit, `system_description/`, is a frozen exempt tree. Recommendation: adopt only the mechanical link/anchor subset, through the Workspace's existing `check_markdown_links.py` (Q-A2-05).

## §1 Coverage

| Item | Status | Reason |
|---|---|---|
| Kickoff prompt §1, §2 | read | required first |
| SOURCE-C `scripts/harness/check_harness_parity.py` | read | docstring, `check_all`, the six checks' heads, self-test |
| SOURCE-C `scripts/harness/closeout.py` | partly read | 3,402 lines; header, constants, CLI, preflight methods (`:818-960`), config readers, the `conductor` coupling sites; generation logic not read |
| SOURCE-C `scripts/harness/regression_scope.py` | partly read | 6,178 lines; header, all declared tables (`:246-400`), `_module_for_path`, `_require_collectible_pytest_target` site; packer/classifier bodies not read |
| SOURCE-C `scripts/harness/run_chunks.py` | partly read | header/exit codes, lease section (`:733-760`), CLI lease flag |
| SOURCE-C `scripts/harness/run_validation.py` | partly read | header, sibling loader, preflight call site |
| SOURCE-C `scripts/harness/reclaim_scratch.py` | partly read | docstring, pinned parents, sweep-library coupling, basetemp readers |
| SOURCE-C `scripts/harness/durations_flush.py` | read | 91 lines |
| SOURCE-C `scripts/harness/session_profile.py` | partly read | header only (operator tool, no caller) |
| SOURCE-C `scripts/harness/duration_history*.json` | not read | data files; only their role (from `docs/harness/README.md` H09) |
| SOURCE-C `scripts/design/*` (7 `.mjs` + `lib/`) | partly read | headers; six compared EOL-normalized against Kit `anchoring-kit/checks/` (identical); `check-parity.mjs` is Conductor-local |
| SOURCE-C `tests/test_prompt_proof_surface_hygiene.py` | read | 155 lines |
| SOURCE-C `tests/test_docs_naming_hygiene.py` | read | 109 lines |
| SOURCE-C `tests/test_repo_hygiene.py` | read | 289 lines |
| SOURCE-C `tests/test_docs_links_and_sources.py` | partly read | docstring, constants, the rule function list; bodies not read |
| SOURCE-C `tests/test_harness_docs*.py` | not read | does not exist: planned as `tests/test_harness_docs_hygiene.py` by batch `QF-4` (`docs/harness/README.md:40-44`) |
| SOURCE-C `tests/test_package_premises*.py` | read (by its real name) | real name `tests/test_batch_package_row_premises.py`; docstring |
| SOURCE-C `tests/test_deliverable_naming*.py` | read (by its real name) | real name is `test_docs_naming_hygiene.py` |
| SOURCE-C INDEX / CONTEXT_INDEX guards | read | no dedicated test; `CONTEXT_INDEX.md` is touched only by the mixed-newline guard (`test_repo_hygiene.py:216-275`) and the parity checker's proposal facts |
| SOURCE-C other hygiene-shaped tests (`test_skill_mirror_parity.py`, `test_batch_package_scope_allowlist.py`, `test_batch_package_out_of_band_marker.py` via `HARNESS_STANDING_CHECKS`, `test_conftest_hygiene.py`, `test_scratch_guard_helper.py`, `test_regression_scope_parity.py`, `test_check_plan_contract_stable.py`, `test_owed_register.py`, `test_section_map_generator.py`, `test_ops_hygiene.py`, `suite_guard.py`) | partly read | docstrings only — enough to classify |
| SOURCE-C `docs/harness/README.md` | read | 258 lines |
| SOURCE-C `docs/harness/*.md` (17 pages) | not read | listed only; the README's inventory and rules carry what this lane needs |
| SOURCE-C `docs/authoring/standard.md` | partly read | authority, scope, style, page shape, behaviour/confidence, locators, traceability, lifecycle; figure/diagram/viewer sections skimmed by heading |
| SOURCE-C `CLAUDE.md` harness/scratch/session/living-docs sections | read | `:101-157`, `:180-218`, `:250-257` |
| SOURCE-C skills `scratch-gate`, `harness-upkeep` | read | 68 and 52 lines |
| SOURCE-C `config.example.yaml` validation keys | partly read | grep of the closeout keys |
| SOURCE-C planning on "closeout adapter" / "non-pytest" | partly read | grep hits; proposal A §3.3, table rows `:296-319`; `PROMPTS_project-onboarding-to-e3_2026-09-30.md` §0-§1 and ledger; `PLAN_conductor-native_2026-10-10.md:75-81`; `BATCH_PLAN.md` B543-B547 headings; `TASK_CHECKLIST.md:1211-1224` |
| SOURCE-K `KIT_SPEC.md` | partly read | §4, §7, §10, §13 |
| SOURCE-K `checker/repo_hygiene_check.py` | partly read | function list; md5 against all seven TARGET copies |
| TARGET `SW_Development/scripts/harness/check_harness_parity.py` | read | 133 lines |
| TARGET `SW_Development/scripts/harness/check_batch_packages.py` | read | 76 lines |
| TARGET `SW_Development/scripts/harness/migrate_checklist_schema.py` | partly read | header |
| TARGET `SW_Development/scripts/hygiene/repo_hygiene_check.py` | partly read | md5 only (identical to kit) |
| TARGET `PlantLibrary_PyApp/scripts/harness/*` | read for tables, diffed whole | `regression_scope.py` tables `:246-345` and port header `:29-46`; all four diffed against Conductor `7ad02b1` |
| TARGET `PlantLibrary_PyApp/scripts/harness/scope_cap.py` | read | 63 lines |
| TARGET `PlantLibrary_PyApp/tests/test_batch_package_contract.py` | partly read | docstring and function list |
| TARGET `PlantLibrary_PyApp/tests/test_repo_hygiene.py` | read | 154 lines |
| TARGET `PlantLibrary_PyApp/tests/test_repo_hygiene_kit.py` | read | 40 lines |
| TARGET `PlantLibrary_PyApp/tests/acceptance/test_harness_port.py` | partly read | test list and pins |
| TARGET `PlantLibrary_PyApp/…/validation/KNOWN_FAILURES.md` | read | 27 lines |
| TARGET `PlantLibrary_PyApp/…/validation/ONBOARDING_harness-port.md` | read | 311 lines |
| TARGET `PlantLibrary_PyApp/pyproject.toml` `[tool.plantlibrary.closeout]` | read | `:77-…` |
| TARGET `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` §9-§10, §13-§14, §L, §N | read | `:437-548`, `:636-679`, `:900-934` |
| TARGET other suites' `scripts/`, `tests/` top level | read (listing) | static listing; heads of `run_next_batch.py` ×2, `check_markdown_links.py`, `check_contract_version_drift.py`, `validate_contracts.py` |
| TARGET suites' `CLAUDE.md` scratch / cap / mirror paragraphs | partly read | grep |
| TARGET seven `hygiene/CONSUMED_HYGIENE.md` pins | partly read | the field rows and roots |
| Added: suite mirror byte-compare (5 skills × 6 suites, 3 agents × 6 suites) | measured | `md5sum` over the trees, read-only |
| Added: Conductor parser changes since 2026-09-15 (`src/conductor/batch_package.py`) | partly read | `git log`; `f904c8d` diff |
| Added: machine closeout lease directory `C:\ProgramData\Conductor\leases\` | listed | exists, a lease file present (the Conductor holds the slot) |

## §2 Findings

**F-A2-01 — PyApp's port is exactly what its transcript claims, at `7ad02b1`.** `run_validation.py`, `run_chunks.py` and `reclaim_scratch.py` are content-identical, EOL-normalized, to `git show 7ad02b1:scripts/harness/<f>`. `regression_scope.py` differs in 48 lines: the three tables plus the `_module_for_path` loop. Sources:
- `PlantLibrary_PyApp/scripts/harness/regression_scope.py:29-46` (port header);
- `PlantLibrary_PyApp/scripts/harness/regression_scope.py:273`, `:316`, `:324-327`, `:406`;
- `PlantLibrary_PyApp/implementation/System_V1_Implementation/validation/ONBOARDING_harness-port.md:11-16`, `:59-86`.

Meaning for TARGET: the port is sound and reviewable. Its pin is `7ad02b1`, not `2e7adb3`.

**F-A2-02 — The Conductor harness has drifted far from the port pin.** Since `7ad02b1` the Conductor has 24 commits on the four ported files (regression_scope 19, run_chunks 7, run_validation 6, reclaim_scratch 2). `closeout.py` (born `a0f5056`, 2026-09-18) and `durations_flush.py` are new. `C:\Programmierung\Orchestrator_System\docs\harness\README.md:86-92` gives the inventory sizes. Meaning: a re-port is a new port, not a refresh. The `UNCHANGED_COPIES` sha256 pins in `PlantLibrary_PyApp/tests/acceptance/test_harness_port.py:35` would all move.

**F-A2-03 — The Conductor's `run-batch` closes through one command; PlantLibrary's still has the legs.** The Conductor's version is at `C:\Programmierung\Orchestrator_System\.claude\skills\run-batch\SKILL.md:174-190`: run `closeout.py`; no widening flag; exits 0/1/2/3. The superproject's `run-batch` still spells out `regression_scope.py`/`run_chunks.py` legs and `--max-targets <cap>` (`SW_Development/.claude/skills/run-batch/SKILL.md:209-305`). Meaning: lane B1's choice of `run-batch` decides which harness each pytest suite needs. Adopting the Conductor's skill without `closeout.py` would leave PyApp and Server with an instruction that names a missing script.

**F-A2-04 — The closeout cap is retired upstream; PyApp still serves it.**
- The Conductor's `config.example.yaml` holds no `max_scope_targets`. The last change touching it is `35429ea` (2026-09-19, "CD2-B389: the product consumes the harness and restates nothing"). Budget keys now read `closeout_budget_s`, `foreground_ceiling_s` and `envelope_grace_s` (`C:\Programmierung\Orchestrator_System\config.example.yaml:113`, `:135`, `:138`).
- PyApp keeps `scope_cap.py` (`PlantLibrary_PyApp/scripts/harness/scope_cap.py:24-25`) and `[tool.plantlibrary.closeout] max_scope_targets = 600` (`PlantLibrary_PyApp/pyproject.toml:77`).
- Five suites' `CLAUDE.md` carry a "Closeout cap" paragraph, e.g. `PlantLibrary_Server/CLAUDE.md:99-102`. The onboarding §L step 6 note already says instance 2's sync must drop `max_scope_targets` (`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:912`).

Meaning: `scope_cap.py` and the cap paragraphs retire together with any re-port. Until then they are consistent with the PlantLibrary `run-batch`.

**F-A2-05 — Current `reclaim_scratch.py` is no longer standalone.** Its sweep mode loads `src/conductor/scratch_sweep.py` by file path (`C:\Programmierung\Orchestrator_System\scripts\harness\reclaim_scratch.py:30-31`, `:101`, `:703-707`). Its pinned parents are `p, pt, chunks, validation, c` (`:97`). PyApp's copy (`7ad02b1`) predates the sweep. Meaning: a verbatim copy breaks `--sweep-older-than` in every suite. An adopt needs the library vendored beside it, or the sweep cut.

**F-A2-06 — `closeout.py` is Conductor-bound in six places.**
1. `DECLARED_PREFIXES = ("src/", "tests/", "scripts/")` at `C:\Programmierung\Orchestrator_System\scripts\harness\closeout.py:71`.
2. Validation scalars come from `config.yaml` / `config.example.yaml` at the root (`:247-302`), and `INSTANCE_CONFIG_DEFAULT` names instance 1 (`:67`).
3. It probes the instance REST API (`GET /api/v1/queue`, `/api/v1/projects`) on loopback (`:909-940`).
4. Unless `--plan-contract-sha256` is passed, it imports `conductor.batch_package` in a subprocess with cwd at the harness root (`:943-960`).
5. Its preflight runs the parity checker of its own repository (`:55`, `:824-828`).
6. It holds the machine lease (`:2890-2909`).

Proposal A's A3 (`CD2-B547`: `.conductor/project.yaml`, bind over any root, instance-sourced ceilings) is the upstream fix. Meaning: not portable today. Recorded, not adopted.

**F-A2-07 — `regression_scope.py` upstream still hard-codes `src/`.** See `C:\Programmierung\Orchestrator_System\scripts\harness\regression_scope.py:462-466`. The census carries this as `GC-0050` (alias `PL-F-6`, open-unrouted) and `GC-1132` (PyApp's promotion, open-decision), cluster `GC-C33`: `C:\Programmierung\Orchestrator_System\implementation\Conductor_V2\planning\REGISTER_gap-census_2026-09-29.md:746`, `:6996`, `:119682`. Proposal A's `layout.source_roots` (`…\proposal\PROPOSAL_project-contract-and-validation-profiles_2026-09-22.md:234`, comment "PlantLibrary PyApp/Server: ["app/"]") is the same idea as PyApp's `IMPORTABLE_SOURCE_TREES`. Meaning: PyApp's promotion is the right shape. GC-1132's review (`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:929`) is still unrecorded: no "reviewed" line exists in `ONBOARDING_harness-port.md`. That review gates Server's port (step 7).

**F-A2-08 — Upstream tables PyApp lacks.** `DIRECT_VALIDATION_PREFIXES = ("design/", ".impeccable/", "validation/", "docs/", ".github/")` lets a declared design/docs path close without a pytest target (`C:\Programmierung\Orchestrator_System\scripts\harness\regression_scope.py:282-311`). PyApp has none. Its `SRC_TREE_STANDING_CHECKS` still names the Conductor-only `tests/acceptance/test_dynamic_vendor.py` (`PlantLibrary_PyApp/scripts/harness/regression_scope.py:333`). That entry is unreachable because it is gated on `src/conductor/` (`:970`). Meaning: once PyApp's GUI rework (B6) touches `design/` or `.impeccable/` paths, the 7ad02b1 port refuses them as unmapped. The re-port must carry this table with PlantLibrary's prefixes.

**F-A2-09 — `run_validation.py` assumes a `pyproject.toml` on every command.** It calls `reclaim_scratch.preflight_basetemp(command)` unconditionally (`PlantLibrary_PyApp/scripts/harness/run_validation.py:208`; upstream `C:\Programmierung\Orchestrator_System\scripts\harness\run_validation.py:371`). With no `--basetemp` in the argv, `resolve_basetemp` falls through to `configured_default_basetemp`, which reads `pyproject.toml` without a guard (`PlantLibrary_PyApp/scripts/harness/reclaim_scratch.py:532-552`; upstream `:638-647`). The superproject, Workspace, AndroidApp, Dashboard and SharedContracts have no `pyproject.toml` (measured). By reading, an unchanged copy would raise before running a gradle/npm command there. Not executed. Meaning: in non-Python suites `run_validation.py` is "carry adapted", not "carry".

**F-A2-10 — `run-batch` names a script five suites lack.** `SW_Development/.claude/skills/run-batch/SKILL.md:171-173` (byte-mirrored into all six suites, measured) says that a command expected to take over 60 s runs once through `scripts/harness/run_validation.py`. Only PyApp has that script. Meaning: every Server, Dashboard, AndroidApp, SharedContracts or Workspace batch with a long build already has an instruction it cannot follow. Fix options: carry an adapted `run_validation.py` + `reclaim_scratch.py` into each (F-A2-09), or a suite `CLAUDE.md` line. The second contradicts "a skill limitation is raised as a proposal" (`PlantLibrary_Server/CLAUDE.md:93-94`).

**F-A2-11 — Nothing checks suite mirror parity, though every suite says something does.**
- `SW_Development/scripts/harness/check_harness_parity.py:36-39` roots at the superproject.
- `compare_trees` (`:58-83`) reads only `<root>/.claude` and `<root>/.codex`.
- Six suite `CLAUDE.md` files say the mirrors are "checked by its `scripts/harness/check_harness_parity.py`" (`PlantLibrary_Server/CLAUDE.md:89-92`; same text at Dashboard `:55`, AndroidApp `:63`, SharedContracts `:54`, Workspace `:57`).
- Onboarding step 3 did a one-off per-suite byte compare (`…onboarding-runbook…md:909`).
- Measured today: the 5 skills and 3 agents are byte-identical in all six suites.

Meaning: B7 extends the checker (RC-A2-08). Until then the claim is false and nothing catches drift.

**F-A2-12 — The Conductor's parity checker has six checks; four do not travel.**
- `check_codex_frozen` and `check_agents_frozen` are pinned to `FROZEN_AT = "10177e3"` (`C:\Programmierung\Orchestrator_System\scripts\harness\check_harness_parity.py:54`, `:213-270`).
- `check_proposal_facts` and `check_section_map_contents` cover the v5 proposal (`:377-563`).
- `compare_chunk_argv_parity` checks the `-p no:randomly` determinism flag between the chunk template and the canonical invocation (`:85`, `:575-598`).
- `check_no_mirrored_ceiling` covers harness modules (`:601-626`).
- `check_all` is at `:629-642`.

Meaning: only the freeze pattern (if Q-G-09 (a)), argv parity and the ceiling check are reusable, the last two only where a harness copy exists. The v5 checks are Conductor-specific.

**F-A2-13 — The hygiene kit already owns most of the Conductor's hygiene tests.**
- `KIT_SPEC.md` §4 copies the proof-surface detectors verbatim from `test_prompt_proof_surface_hygiene.py` at `fc5a14c` (`C:\Programmierung\Repo_Hygiene_Template_Kit\KIT_SPEC.md:122-152`).
- §7 carries the naming, index, root, rule-block and record rules (`:222-269`).
- §10 carries the root allowlist (retired names, forbidden paths) and the scratch root (`:317-332`).
- §13 names what stays out: the harness, the `.tmp` interior, skill mirrors, the package schema, the v5 checks (`:383-397`).
- All seven TARGET checker copies are byte-identical to the kit (md5 `4286f9e0…`).

Gaps the kit does not cover:
- the package contract-file mixed-newline guard (`C:\Programmierung\Orchestrator_System\tests\test_repo_hygiene.py:216-275`);
- docs link/anchor/locator integrity (`…\tests\test_docs_links_and_sources.py:1-20`);
- skill mirror parity;
- parser-backed package premises.

Meaning: §7.2 lists exactly what B7 ports.

**F-A2-14 — Two root allowlists in PyApp, neither the kit's.** PyApp's pin says `Modules none` (`PlantLibrary_PyApp/hygiene/CONSUMED_HYGIENE.md`). Its own sentinel `tests/test_repo_hygiene.py:28-75` is the root allowlist, and the harness's `ROOT_DOC_STANDING_CHECKS` needs that pytest node. The sentinel still sanctions `graphify-out` (`:47`), although the superproject dropped graphify hooks (commits `53051b0`, `7946483`). Meaning: keep the PyApp sentinel; it is a harness dependency, not a duplicate to delete. Its allowlist needs the graphify line revisited (B3).

**F-A2-15 — The superproject package census uses the real Conductor parser, from instance 2's source.** `SW_Development/scripts/harness/check_batch_packages.py:15-20` imports `conductor.batch_package`, falling back to `C:\Programs\AI_Orchestrator_2\src`. Since 2026-09-15 the parser changed twice: `f904c8d` (model-tuple grammar loosened) and `6526c93` (AM-51 own-record count). Meaning: the census judges packages by whatever parser instance 2 has deployed. The output does not say which, so record the parser source in its output (RC-A2-09). PyApp's local restatement (`PlantLibrary_PyApp/tests/test_batch_package_contract.py:1-18`) can drift silently from either; lane A7 owns depth.

**F-A2-16 — Onboarding step 8 is overtaken; the Conductor's route is proposal A, not yet built.** Step 8 (`…onboarding-runbook…md:646-679`) asked for `PROPOSAL_per-project-closeout-adapter_<date>.md`; no such file exists in SOURCE-C (find over `implementation/`, measured). The Conductor absorbed PL-F-6 into proposal A instead:
- A3 cites `PL-F-6` (`…\proposal\PROPOSAL_project-contract-and-validation-profiles_2026-09-22.md:680`).
- Profiles `gradle`, `npm` and `contracts` all extend `command` (`:38`, `:296-298`, `:317-319`).
- Gradle and npm ship over `command` first (`:341-342`).
- The harness half is `CD2-B543`…`B547`, rows `CD-V2-HRN-195`…`-208`, all `todo` (`C:\Programmierung\Orchestrator_System\implementation\Conductor_V2\BATCH_PLAN.md:12688`, `:12701`, `:12714`, `:12725`, `:12736`; `TASK_CHECKLIST.md:1211-1224`; `PLAN_conductor-native_2026-10-10.md:79-81`).
- Per-project toolchain steps for SharedContracts, Dashboard and Android are `ob-25`, "not written yet, deliberately" (`PROMPTS_project-onboarding-to-e3_2026-09-30.md:86`, `:352`).
- `GC-2009` holds the non-pytest route as an operator-act item (`PLAN_gap-census-handoff_2026-09-29.md:2350`).

Meaning: TARGET's §L step 8 should be flipped to "superseded by Conductor proposal A" (B8). It should not be executed as written.

**F-A2-17 — Dead driver helpers.** `PlantLibrary_Dashboard/scripts/run_next_batch.py:11-13` and `PlantLibrary_Server/scripts/run_next_batch.py` read `BATCH_PLAN.md` at the suite root. No such file exists there; packages live under `implementation/System_V1_Implementation/`. Both are cited only by terminal MVP package files and the suite `README.md` (`PlantLibrary_Dashboard/README.md:15`, `PlantLibrary_Server/README.md:10`). Meaning: retire with a legacy note (B3). Do not delete silently: terminal evidence cites them.

**F-A2-18 — Scratch policy: the suites copied the Conductor's layout without its gate.** Six suite `CLAUDE.md` scratch paragraphs name `.tmp/chunks/<run-id>` and `.tmp/p/<slug>`, e.g. `PlantLibrary_PyApp/CLAUDE.md:385-401`. The same boilerplate sits in Dashboard (`:75-77`) and AndroidApp (`:83-85`), which have no closeout harness. The superproject's `CLAUDE.md` has no scratch paragraph, and its `.gitignore` has no `.tmp/`. No repository pins the kit's `scratch` module. The Conductor adds:
- `.tmp/pt/d` and `.tmp/c` (base worktrees);
- `.tmp/validation/<batch>/genNN/.live` sentinels;
- `.tmp/.reclaim.lock`;
- an operator-only `scratch-gate` skill (`C:\Programmierung\Orchestrator_System\CLAUDE.md:145-157`; `…\.claude\skills\scratch-gate\SKILL.md:24-49`; `…\scripts\harness\reclaim_scratch.py:24-45`, `:97`).

Delta in §7.4.

**F-A2-19 — The Conductor's harness docs rule set is reusable; its gate test does not exist yet.** `C:\Programmierung\Orchestrator_System\docs\harness\README.md:19-51` sets the folder rules:
- one page per harness;
- fixed headings: Contract, Invocation, Evidence written, Exit codes, Owning tests, Open debts, Owner;
- "Verified at `<sha>`";
- the truth rule;
- no proof surface.

Its "docstrings that disagree" table (`:199-243`) lists, among others, `reclaim_scratch.py:14,37`, `run_chunks.py:34` and `regression_scope.py:863-868`; PyApp's copies inherit the older forms of these. Meaning: B7 can adopt the folder rules for a small PlantLibrary harness index. There is no Conductor guard to port; `test_harness_docs_hygiene.py` is planned only.

**F-A2-20 — The machine lease is live, and current `run_chunks.py` speaks it.** Upstream `run_chunks.py` takes the machine-wide `closeout.v1` lease by default at `C:\ProgramData\Conductor\leases\closeout.lease` (`C:\Programmierung\Orchestrator_System\scripts\harness\run_chunks.py:733-760`, `:1725`). The directory exists and a lease file is present (listed, not read). PyApp's `7ad02b1` copy predates the lease. Meaning: for Phase C, a re-ported `run_chunks.py` makes a PlantLibrary closeout wait for the Conductor's slot instead of contending with it. That is the strongest argument for re-porting at all (kickoff §1: "the machine's one test slot belongs to the Conductor").

**F-A2-21 — Design scripts are Kit 1.7.0 verbatim, plus one local script.** Six `scripts/design/*.mjs` equal `C:\Programmierung\Design_Template_Kit\anchoring-kit\checks\*.mjs` EOL-normalized (diff, 0 lines each). `check-parity.mjs` is Conductor-local, and its header says it is modelled on `SW_Development/scripts/harness/check_harness_parity.py` (`C:\Programmierung\Orchestrator_System\scripts\design\check-parity.mjs:1-6`). `scripts/design_row_audit.mjs` is the pilot's "writes nothing tracked" wrapper (`…\tests\test_design_row_audit.py:1-6`). Meaning: these come into TARGET through the Kit installer (A4/B5), not through B7.

## §3 Candidates

| ID | Source path @ pin | What | Verdict | Target repo and path | Lane | Q id or — |
|---|---|---|---|---|---|---|
| RC-A2-01 | Orchestrator_System:`scripts/harness/run_validation.py` @ 2e7adb3 | runs one argv once, no shell, Job Object, 540 s ceiling, full-output artifact | adapt: in Phase C re-port as one set with RC-A2-02/-03/-04/-06 at one Conductor pin, replacing PyApp's `7ad02b1` copy; for suites without `pyproject.toml`, guard the basetemp preflight (F-A2-09). If copied wrong, every long command in Dashboard/AndroidApp/SharedContracts/Workspace dies in the preflight, and PyApp's `UNCHANGED_COPIES` pin fails | PlantLibrary_PyApp, PlantLibrary_Server `scripts/harness/run_validation.py` (carry); Dashboard, AndroidApp, SharedContracts, Workspace (carry adapted) | B7 (record), C1 (port) | Q-A2-01 |
| RC-A2-02 | Orchestrator_System:`scripts/harness/run_chunks.py` @ 2e7adb3 | resumable exactly-once chunk runner; envelope triple; machine closeout lease | adopt verbatim at re-port time (replaces PyApp's `7ad02b1` copy). If wrong: chunk argv/envelope flags must match the `run-batch` the suite mirrors (B1); a lease-path mismatch makes PlantLibrary and Conductor closeouts contend for the one slot | PlantLibrary_PyApp, PlantLibrary_Server `scripts/harness/run_chunks.py` | C1 | Q-A2-01 |
| RC-A2-03 | Orchestrator_System:`scripts/harness/reclaim_scratch.py` @ 2e7adb3 | scratch classifier/reclaimer; sweep through `src/conductor/scratch_sweep.py` | adapt: vendor `scratch_sweep.py` beside it, or keep the `7ad02b1` copy (F-A2-05). If wrong: `--sweep-older-than` crashes; `run_validation.py` loses its preflight sibling | PlantLibrary_PyApp, PlantLibrary_Server `scripts/harness/reclaim_scratch.py`; adapted where RC-A2-01 goes | C1 | Q-A2-01 |
| RC-A2-04 | Orchestrator_System:`scripts/harness/regression_scope.py` @ 2e7adb3 | touched-path scope, chunk packing, ledger classification | adapt: tables only, as at step 4. Re-apply `IMPORTABLE_SOURCE_TREES` (upstream still hard-codes `src/`); add PlantLibrary `DIRECT_VALIDATION_PREFIXES`; sentinels = suite tests. If wrong: every product path refuses `unmapped touched path`, or a widened map silently skips proof | PlantLibrary_PyApp (replace), PlantLibrary_Server (new) `scripts/harness/regression_scope.py` | C1 | Q-A2-01, Q-A2-02 |
| RC-A2-05 | Orchestrator_System:`scripts/harness/closeout.py` @ 2e7adb3 | one-command closeout (preflight, scope, plan, run, classify, evidence, handoff) | record only now (F-A2-06); adopt after proposal A's A3 (`CD2-B547`) makes it root-agnostic | — (later PyApp, Server) | B7 records; C1 | Q-A2-01 |
| RC-A2-06 | Orchestrator_System:`scripts/harness/durations_flush.py` @ 2e7adb3 | pytest plugin keeping the per-file durations of a killed run | adopt verbatim with the RC-A2-01 set (current `run_validation.py` injects it for history runs). If missing: history runs lose the plugin | PlantLibrary_PyApp, PlantLibrary_Server `scripts/harness/durations_flush.py` | C1 | Q-A2-01 |
| RC-A2-07 | Orchestrator_System:`scripts/harness/session_profile.py` @ 2e7adb3 | aggregate session profiler, no caller (H08 "unowned") | record only | — | — | — |
| RC-A2-08 | Orchestrator_System:`scripts/harness/check_harness_parity.py` @ 2e7adb3 | six-check parity preflight (codex/AGENTS freeze, v5 facts, Section Map, chunk-argv parity, mirrored ceiling) | adapt: keep PlantLibrary's `compare_trees` and add (1) the 5 skills + 3 agents byte-compared in all six suites; (2) the freeze checks if Q-G-09 (a); (3) chunk-argv parity and no-mirrored-ceiling over each suite's harness copy. Drop the v5 checks. If wrong: a false pass is what every suite's `CLAUDE.md` already relies on (F-A2-11) | SW_Development `scripts/harness/check_harness_parity.py` | B7 | Q-A2-04, Q-G-09 |
| RC-A2-09 | SW_Development:`scripts/harness/check_batch_packages.py` @ 8702e0a | census of all packages through the real Conductor parser | keep PlantLibrary's; adapt: print the parser module path and the instance's sync stamp, so a verdict names its parser (F-A2-15) | SW_Development `scripts/harness/check_batch_packages.py` | B7 | — |
| RC-A2-10 | SW_Development:`scripts/harness/migrate_checklist_schema.py` @ 8702e0a | one-off 14→15-column migration; refuses a migrated file | record only (spent operator act; keep for history) | — | — | — |
| RC-A2-11 | Orchestrator_System:`tests/test_prompt_proof_surface_hygiene.py` @ 2e7adb3 | prompt proof-surface detectors | record only: the kit's `proof-argv`/`proof-prose`/`proof-floor` already enforce it in all seven repositories (KIT_SPEC §4) | — | — | — |
| RC-A2-12 | Orchestrator_System:`tests/test_docs_naming_hygiene.py` @ 2e7adb3 | `<TYPE>_<topic>_<date>.md` naming guard | record only: kit rule `name` | — | — | — |
| RC-A2-13 | Orchestrator_System:`tests/test_repo_hygiene.py` @ 2e7adb3 (`:216-275`) | package contract files must not mix CRLF/LF | adapt: port as a static stdlib script over every `implementation/*/` package of all seven repositories (and SDA); the root-allowlist part is the kit's. If wrong: a CRLF/LF-mixing package write (kickoff §2 rule 8) goes unseen | SW_Development `scripts/harness/check_package_newlines.py` (new) | B7 | — |
| RC-A2-14 | PlantLibrary_PyApp:`tests/test_repo_hygiene.py` @ 35ddc63 | PyApp root allowlist, the harness's root sentinel | keep PlantLibrary's; adapt the allowlist after the graphify drop (B3 decides) | PlantLibrary_PyApp `tests/test_repo_hygiene.py` | B3/B7 | — |
| RC-A2-15 | Orchestrator_System:`tests/test_docs_links_and_sources.py` @ 2e7adb3 | docs gate: links, anchors (case-sensitive), `src:` locators, head/foot, catalog, figures | record only; the link+anchor half is covered by RC-A2-16 | — | — | Q-A2-05 |
| RC-A2-16 | PlantLibrary_Workspace:`scripts/check_markdown_links.py` @ 6b4b88b | relative-link and heading-anchor checker with a baseline file; default roots = every `PlantLibrary_*` | keep PlantLibrary's; adapt: add the superproject's deliverable roots and case-sensitive target matching (the Conductor gate's Windows rule) | PlantLibrary_Workspace `scripts/check_markdown_links.py` | B7 | Q-A2-05 |
| RC-A2-17 | Orchestrator_System:`docs/authoring/standard.md` @ 2e7adb3 | living-documentation contract (head/foot, behaviour/confidence, locators, catalog, lifecycle) | adapt (subset), only if Q-A2-05 (b)/(c); otherwise record only | — (or Workspace `system_description/`) | B7 | Q-A2-05 |
| RC-A2-18 | Orchestrator_System:`docs/harness/README.md` @ 2e7adb3 (`:19-51`) | harness folder rules: one page per harness, fixed headings, verified-at sha, truth rule | adapt: one `scripts/harness/README.md` per repository that carries a harness, using the same headings, with PlantLibrary owners | SW_Development, PlantLibrary_PyApp `scripts/harness/README.md` | B7 | — |
| RC-A2-19 | Orchestrator_System:`tests/test_batch_package_row_premises.py`, `tests/test_batch_package_scope_allowlist.py`, `tests/test_batch_package_out_of_band_marker.py` @ 2e7adb3 | parser-backed premise, scope-allowlist and out-of-band-marker guards | record only here; A7 decides; a port would be a static extension of RC-A2-09 | — | A7→B4 | — |
| RC-A2-20 | Orchestrator_System:`tests/suite_guard.py`, `tests/conftest.py` guards @ 2e7adb3 | Layer 3b refusal of an unwrapped/elevated pytest session; git and live-scratch guards | record only; a deferred-register row for Phase C (they need a test run to prove) | — | C1 | — |
| RC-A2-21 | Orchestrator_System:`scripts/design/*.mjs` (six) @ 2e7adb3 = Design_Template_Kit `anchoring-kit/checks/*` @ f08e588 | the Kit's mechanical design checks | record only for B7; installed by the Kit installer | — | A4→B5 | Q-G-01 |
| RC-A2-22 | Orchestrator_System:`scripts/design/check-parity.mjs` @ 2e7adb3 | byte parity of Kit-installed skills across `.claude`/`.codex`/`.agents`/`.github` | adapt for PyApp and AndroidApp (`impeccable` mirrors) when B5 installs the Kit | PlantLibrary_PyApp, PlantLibrary_AndroidApp `scripts/design/check-parity.mjs` | B5 | — |
| RC-A2-23 | Orchestrator_System:`scripts/design_row_audit.mjs` @ 2e7adb3 | runs `run-all.mjs` against a `.tmp/` scratch root so a row's design audit writes nothing tracked | adapt for the three client suites | PyApp, Dashboard, AndroidApp `scripts/design_row_audit.mjs` | B5/B6 | Q-G-01 |
| RC-A2-24 | Orchestrator_System:`.claude/skills/scratch-gate/SKILL.md` @ 2e7adb3 | operator scratch gate over `reclaim_scratch.py` | adapt for PyApp and Server only, where the script exists; not applicable elsewhere | PlantLibrary_PyApp, PlantLibrary_Server `.claude/skills/scratch-gate/` | B1 | — |
| RC-A2-25 | Orchestrator_System:`.claude/skills/harness-upkeep/SKILL.md` @ 2e7adb3 | which check follows which edit | adapt: PlantLibrary table (hygiene checker, parity checker, package census, newline guard, link checker) | SW_Development `.claude/skills/harness-upkeep/` | B1 | — |
| RC-A2-26 | PlantLibrary_PyApp:`scripts/harness/scope_cap.py` + `pyproject.toml [tool.plantlibrary.closeout]` @ 35ddc63 | derives the 600 cap for `--max-targets` | keep PlantLibrary's while PlantLibrary's `run-batch` names the cap; retire with the re-port (upstream retired the cap, `35429ea`), together with the five suites' "Closeout cap" paragraphs | PlantLibrary_PyApp; suites' `CLAUDE.md` | B2 (text), C1 (retire) | Q-A2-01 |
| RC-A2-27 | PlantLibrary_Dashboard:`scripts/run_next_batch.py` @ 7795fc8; PlantLibrary_Server:`scripts/run_next_batch.py` @ f1a31b9 | MVP-era next-batch printers reading a root `BATCH_PLAN.md` that does not exist | retire: legacy banner or archive under the terminal MVP package, which cites them; never a silent delete | the two suites | B3 | — |
| RC-A2-28 | Orchestrator_System:`implementation/Conductor_V2/proposal/PROPOSAL_project-contract-and-validation-profiles_2026-09-22.md` §3.3 @ 2e7adb3 | `.conductor/project.yaml` project contract; profiles `pytest`/`command`/`gradle`/`npm`/`contracts`/`docs`/`planning`/`audit`/`ops`/`design` | record only; each suite's future contract (replaces `IMPORTABLE_SOURCE_TREES`, `scope_cap.py`, the suite sentinels' wiring) once `CD2-B543`…`B547` and `ob-25` land | — | B8 (record), C1 | Q-A2-03 |
| RC-A2-29 | PlantLibrary_PyApp:`tests/test_batch_package_contract.py` @ 35ddc63 | local restatement of the parser's structural contract, 8 negative cases | keep PlantLibrary's (the harness sentinel); re-check against the parser at re-port (F-A2-15) | PlantLibrary_PyApp | A7/C1 | — |
| RC-A2-30 | Repo_Hygiene_Template_Kit:`checker/repo_hygiene_check.py` @ 0.2.1 | the hygiene contract | keep (all seven copies byte-identical); optionally turn on the `scratch` module in the six suites | the seven repositories' `hygiene/CONSUMED_HYGIENE.md` | B3/B7 | Q-A2-06 |

## §4 Questions for the operator

| ID | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A2-01 | When to re-port the PyApp closeout harness to the Conductor's current code | (a) hold PyApp's `7ad02b1` port unchanged through Phase B, record the drift, and re-port once, as one set with `closeout.py`, after the Conductor ships proposal A's harness half (`CD2-B543`…`B547`); (b) re-port `run_validation`/`run_chunks`/`regression_scope`/`reclaim_scratch` now at `2e7adb3`, tables adapted; (c) re-port now including a locally adapted `closeout.py` | Phase B cannot prove any port (no tests, kickoff §2 rule 1). The current `reclaim_scratch.py` and `closeout.py` are coupled to `src/conductor` and the instance (F-A2-05, F-A2-06), and A3 removes that coupling upstream; porting now means porting twice | B7 harness sub-step; C1; Server step 7 |
| Q-A2-02 | GC-1132: accept PyApp's `IMPORTABLE_SOURCE_TREES` promotion (`app/`, `backend/`) | (a) accept; record the dated "reviewed" line in `ONBOARDING_harness-port.md` and flip §L step 4; Server's port uses `(("app/", ""),)`; (b) reject and write a FINDING that the harness cannot map a non-`src/` suite | The fail-closed rule is unchanged and was proven by the `.qss` refusal. Proposal A's `layout.source_roots` is the same design upstream (F-A2-07) | Server step 7; RC-A2-04 |
| Q-A2-03 | What a harness port means for Dashboard, AndroidApp, SharedContracts and Workspace, and what happens to onboarding step 8 | (a) no closeout harness there now; carry only the static guards of §7.2 and an adapted `run_validation.py` (F-A2-10); flip step 8 to "superseded by Conductor proposal A (PL-F-6 → A3; gradle/npm/contracts profiles; `ob-25`)"; (b) write a PlantLibrary-local command adapter now; (c) execute step 8 as written (a new Conductor proposal) | The Conductor already absorbed F-6 (proposal A :680), and its rows are planned (F-A2-16). A local adapter or a second proposal would fork a design the Conductor will ship | B7; B8 (step 8 flip) |
| Q-A2-04 | Scope of the superproject parity checker | (a) extend it to byte-compare the 5 mirrored skills and 3 agents of all six suites against the superproject, and apply Q-G-09's answer to `.codex`; (b) keep per-suite parity as a manual compare and correct the six `CLAUDE.md` sentences | Six `CLAUDE.md` files already promise (a); today nothing enforces it (F-A2-11) | B7; B2 (sentence wording) |
| Q-A2-05 | The Conductor's living-documentation standard | (a) do not adopt it wholesale; adopt its mechanical subset (relative links and anchors resolve, case-sensitive) for all seven repositories through the Workspace `check_markdown_links.py`, and its head/foot shape only for reader-facing pages written from now on; (b) adopt it for the Workspace `system_description/` (138 files) with catalog and Document IDs; (c) adopt it for every suite's `docs/` | TARGET has no page in that shape. `system_description/` is a frozen exempt tree (`PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md:137`). The suites' `docs/` are per-row design notes, not living explanations. The standard's locator, catalog and figure apparatus is built around `src/conductor` and an archify pin (§7.3) | B7 (living-docs part); B2 (`CLAUDE.md` pointer) |
| Q-A2-06 | The kit's `scratch` module | (a) turn it on in the six suites (each already ignores `.tmp/`, onboarding §L step 3) by one decision entry per repository, and leave it off in the superproject until a step there needs scratch; (b) keep it off everywhere | Makes the suites' scratch paragraph checkable at no runtime cost; the superproject has no `.tmp/` ignore and no scratch user today | B3/B7 |

## §5 Reusable things this brief did not name

- `C:\Programmierung\Orchestrator_System\scripts\check_plan_contract_stable.py` and `…\scripts\plan_readiness.py` (H17, H18): plan tools over the real parser. They are parameterised by package path and could serve TARGET's packages through instance 2's interpreter, the way `check_batch_packages.py` does. Record for A7/B4.
- `C:\Programmierung\Orchestrator_System\tests\suite_guard.py:1-29`: Layer 3b. A pytest session collecting more than 30 files outside `run_validation.py` is refused at launch. This is the runtime twin of the kit's lexical proof-surface rule. Phase C (RC-A2-20).
- The machine lease protocol (`run_chunks.py:733-760`; `python -m conductor closeout-lease`, `docs/harness/README.md:115`): PlantLibrary's route to share the one test slot (F-A2-20).
- `…\docs\harness\README.md:199-243`, the "docstrings that disagree with their page" table: a ready list of known stale docstrings in the files PyApp copied.
- `PlantLibrary_Workspace/scripts/check_contract_version_drift.py` (report-only version visibility) and `PlantLibrary_SharedContracts/scripts/validate_contracts.py`: TARGET-native static checks that become the `contracts` profile's checks in proposal A (`:319`). Keep them.
- `C:\Programmierung\Orchestrator_System\tests\test_redacted_fixtures.py`: a guard for fixtures cut from real logs. Not needed in TARGET today; record only.

## §6 Claims to verify

1. *PyApp's three "unchanged" harness files equal the Conductor at `7ad02b1`.* Check (no output means equal):
   `diff <(git --no-optional-locks -C /c/Programmierung/Orchestrator_System show 7ad02b1:scripts/harness/run_chunks.py | tr -d '\r') <(tr -d '\r' < /c/Programmierung/SW_Development/PlantLibrary_PyApp/scripts/harness/run_chunks.py)`. Repeat for `run_validation.py` and `reclaim_scratch.py`.
2. *The superproject parity checker never reads a submodule.* Check: `grep -n "root /" /c/Programmierung/SW_Development/scripts/harness/check_harness_parity.py`. Every hit is `root / ".claude"` or `root / ".codex"` (lines 60-61, 77-78), and `repository_root()` is the superproject (`:36-39`).
3. *The current Conductor `reclaim_scratch.py` depends on `src/conductor/scratch_sweep.py`.* Check: `grep -n "SWEEP_LIBRARY_RELATIVE\|scratch_sweep" /c/Programmierung/Orchestrator_System/scripts/harness/reclaim_scratch.py`. Expect the definition at `:101`, use sites after it, and the docstring at `:30`.

## §7 Deliverables

### §7.1 Matrix

Columns per suite: Sup = superproject, WS = Workspace, Py = PyApp, An = AndroidApp, Da = Dashboard, Sv = Server, SC = SharedContracts. C = carry, CA = carry adapted, NA = not applicable.

| Conductor script or guard | What it does | Assumptions | Class | PyApp status | Sup | WS | Py | An | Da | Sv | SC | Lane |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `scripts/harness/closeout.py` | one-command closeout, exits 0/1/2/3 | pytest; `DECLARED_PREFIXES` `src/` (`:71`); `config.yaml` validation scalars (`:247-302`); Conductor parser subprocess (`:943-960`); instance REST (`:909-940`); own-repo parity (`:824-828`); machine lease | Conductor-specific until proposal A A3 | absent (born after the port) | NA | NA | CA after `CD2-B547` (Q-A2-01) | NA | NA | CA after `CD2-B547` | NA | B7 record, C1 |
| `scripts/harness/regression_scope.py` | scope, packing, deltas, classification, history | pytest-only targets (`_require_collectible_pytest_target` `:564`); `src/` hard-coded (`:462-466`); sentinel test names; `implementation/` packages; `KNOWN_FAILURES.md` | parameterised (tables) | adapted at step 4 (`7ad02b1`; tables + `_module_for_path`) | NA | NA | CA (re-port later) | NA | NA | CA (step 7) | NA | C1 |
| `scripts/harness/run_chunks.py` | exactly-once resumable chunk runner, `--stop`, lease | manifest from `regression_scope`; envelope triple from caller; lease path default `C:\ProgramData\…` (`:744`) | generic (argv runner) | ported unchanged (`7ad02b1`, pre-lease) | NA | NA | C | NA | NA | C | NA | C1 |
| `scripts/harness/run_validation.py` | one argv once, no shell, ceiling 540 s | sibling `reclaim_scratch.py`; `pyproject.toml` read on every command via the basetemp preflight (F-A2-09) | generic for Python repositories, parameterised elsewhere | ported unchanged | NA | CA | C | CA | CA | C | CA | B7 (F-A2-10), C1 |
| `scripts/harness/reclaim_scratch.py` | classify/reclaim `.tmp/`; age sweep | `.tmp` root; pinned parents `p pt chunks validation c`; sweep loads `src/conductor/scratch_sweep.py` (`:101`); `pyproject.toml` basetemp | parameterised (current); generic (`7ad02b1`) | ported unchanged (`7ad02b1`) | NA | CA | C | CA | CA | C | CA | C1 |
| `scripts/harness/durations_flush.py` | pytest plugin: durations survive a kill | pytest; `run_validation.py` injects it | generic (pytest) | absent | NA | NA | C (with re-port) | NA | NA | C | NA | C1 |
| `scripts/harness/check_harness_parity.py` | six parity checks, closeout preflight | `.claude`/`.codex`; codex freeze `10177e3`; v5 proposal facts; chunk argv; ceiling names | parameterised (two checks) / Conductor-specific (four) | absent in PyApp; superproject has a trimmed Aug-05 variant | CA (RC-A2-08) | NA | NA | NA | NA | NA | NA | B7 |
| `scripts/harness/session_profile.py` | session aggregates | Claude/Codex JSONL | generic, unowned | absent | NA | NA | NA | NA | NA | NA | NA | — |
| `scripts/harness/duration_history*.json` | packer history and provenance | Conductor test ids | Conductor-specific data | not shipped by decision | NA | NA | NA (born on first run) | NA | NA | NA | NA | — |
| `scripts/design/*.mjs` (six Kit checks) | mechanical design conformance | node; Kit pin; Configuration | generic (Kit) | absent | NA | NA | C via Kit | C via Kit | C via Kit | NA | NA | A4→B5 |
| `scripts/design/check-parity.mjs` | Kit-skill mirror parity | four mirror roots | parameterised | absent | NA | NA | CA | CA | NA | NA | NA | B5 |
| `scripts/design_row_audit.mjs` | design audit into `.tmp/` only | node; `run-all.mjs` | parameterised | absent | NA | NA | CA | CA | CA | NA | NA | B5/B6 |
| `tests/test_prompt_proof_surface_hygiene.py` | prompt proof-surface lexical guard | `implementation/*/planning` | generic, owned by the kit | kit wrapper (`tests/test_repo_hygiene_kit.py`) | covered by kit | covered by kit | covered by kit | covered by kit | covered by kit | covered by kit | covered by kit | — |
| `tests/test_docs_naming_hygiene.py` | deliverable naming | Conductor_V2 folders | generic, owned by the kit | kit | covered by kit | covered by kit | covered by kit | covered by kit | covered by kit | covered by kit | covered by kit | — |
| `tests/test_repo_hygiene.py` root allowlist / retired / `C:\pt` | root stays sanctioned | dev-repo marker; machine paths | generic, owned by the kit (module) | own pytest sentinel (harness need) | kit module on | NA | keep own (RC-A2-14) | NA | NA | NA | NA | B3 |
| `tests/test_repo_hygiene.py:216-275` mixed newlines | contract files keep one EOL style | `implementation/*/BATCH_PLAN.md` | generic | absent | C as static script over all seven (RC-A2-13) | via Sup | via Sup | via Sup | via Sup | via Sup | via Sup | B7 |
| `tests/test_docs_links_and_sources.py` | docs links, anchors, locators, shape, catalog, figures | `docs/` living tree; `ast` on `src/`; archify pin | Conductor-specific (shape/catalog/figures); generic (links) | absent | CA links via RC-A2-16 | CA (owner of the checker) | CA via RC-A2-16 | CA via RC-A2-16 | CA via RC-A2-16 | CA via RC-A2-16 | CA via RC-A2-16 | B7 |
| `tests/test_skill_mirror_parity.py` | bridge-table mirror parity | `.agents/README.md`; codex freeze | parameterised | absent | CA inside RC-A2-08 | NA | NA | NA | NA | NA | NA | B7 |
| `tests/test_batch_package_row_premises.py`, `…scope_allowlist.py`, `…out_of_band_marker.py` | package premise guards | real parser; `SCOPE.md` grammar | parameterised | partly (local contract test, structural only) | record (A7) | record | record | record | record | record | record | A7→B4 |
| `tests/suite_guard.py` + `conftest.py` guards | refuse unwrapped/elevated sessions; live-scratch/git guards | pytest; `run_validation.py` env | parameterised | absent | NA | NA | CA (Phase C) | NA | NA | CA (Phase C) | NA | C1 |
| `.claude/skills/scratch-gate` | operator gate procedure | `reclaim_scratch.py` exists | parameterised | absent | NA | NA | CA | NA | NA | CA | NA | B1 |
| `.claude/skills/harness-upkeep` | which check after which edit | Conductor checks | parameterised | absent | CA | NA | NA | NA | NA | NA | NA | B1 |
| `docs/harness/README.md` folder rules | harness inventory + page template | none beyond markdown | generic | absent | CA (RC-A2-18) | NA | CA | NA | NA | CA (with port) | NA | B7 |

### §7.2 What the kit covers, and what the Conductor's tests add

Already the checker's (port nothing). Rules are from `C:\Programmierung\Repo_Hygiene_Template_Kit\KIT_SPEC.md:240-250`; TARGET copies are byte-identical in all seven repositories:
- deliverable naming (`name`);
- `INDEX.md` lines (`index`, `index-missing`);
- declared roots (`root-missing`);
- the prompt proof surface (`proof-argv`, `proof-prose`, `proof-floor`), with detectors copied verbatim from the Conductor test at `fc5a14c`;
- the rule block (`block-missing`, `block-parity`);
- the decision record (`record`);
- the root allowlist (`allowlist`, `retired`, `forbidden-path`; on in the superproject only);
- the scratch root (`scratch`; off everywhere, Q-A2-06).

Pin differences worth knowing:
- The `Sanctioned launcher` is empty in all seven. A PyApp `PROMPT` line that wraps a test through `run_validation.py` would therefore be flagged. That is stricter than the Conductor's and fine.
- The prompt floor is 0 in the six suites and 1 in the superproject.

What B7 must add, each as a static, stdlib-only script under the superproject's `scripts/harness/`, with one success line and exit 0/1/2 like the kit's:
1. **Package newline guard**, from `tests/test_repo_hygiene.py:216-275`: one EOL style per contract file (`README.md`, `SCOPE.md`, `CONTEXT_INDEX.md`, `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`) in every package that has a `BATCH_PLAN.md`, across the superproject and the six submodules. This directly guards kickoff §2 rule 8.
2. **Suite mirror parity**: extend `check_harness_parity.py` (RC-A2-08, Q-A2-04).
3. **Package census with parser provenance**: extend `check_batch_packages.py` (RC-A2-09).
4. **Docs links/anchors**: extend the Workspace `check_markdown_links.py` rather than port the Conductor's 1,060-line gate (RC-A2-16, Q-A2-05).

Not ported: the Conductor's v5 proposal-facts and Section Map checks, the Conductor_V2-specific naming exemptions, the `C:\pt` machine-path checks (the kit's `forbidden-path` replaces them if ever wanted), and the parser-backed premise guards (A7).

### §7.3 The living-documentation standard

What it requires (`C:\Programmierung\Orchestrator_System\docs\authoring\standard.md`):
- **Scope** (`:25-40`): living explanations under `docs/`; a `docs/harness/` page is governed for shape and catalog only.
- **Head** (`:60-79`): a breadcrumb plus one status line, `Status: <lifecycle> · L<n> · reviewed <date> at <rev7> · owner: <role>`.
- **Foot** (`:80-95`): a `## Sources and review` table (Document ID `DCD-…`, type/level/purpose, owner/reviewer, lifecycle, reviewed revision, parent/related, behaviour and confidence, sources).
- **Claim records** (`:96-102`): per-claim records `C-nn` on L2/L3 pages.
- **Two axes** (`:104-120`): behaviour (intended / implemented / planned / limited / unverified) and confidence (source-observed / evidence-supported / unverified) are independent.
- **Locators** (`:122-142`): symbol-anchored `<!-- src: path::Symbol -->`, resolved via `ast`.
- **Catalog** (`:396-423`): a catalog row per page, the reverse index for change impact.
- **Lifecycle** (`:425-470`): exceptions at most 30 days in `exceptions.md`, a quarterly review, deprecate to `docs/archive/` with compatibility pointers.
- **Living-docs rule** (`C:\Programmierung\Orchestrator_System\CLAUDE.md:250-257`): a batch that changes user-visible behaviour updates the affected pages in the same batch. The gate is `tests/test_docs_links_and_sources.py`.

Where it would fit in TARGET:
- `PlantLibrary_Workspace/system_description/PlantLibrary_System_Description/` (138 `.md`, numbered chapters 00-12, "single source of truth for the final system shape") is the only living-explanation corpus. It is a frozen exempt tree (`PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md:137`).
- The suites' `docs/` folders hold per-row design notes and plans: AndroidApp 12, Dashboard 6, Server 12. `PlantLibrary_PyApp/Documentation/` holds 38 proposals/plans with V1/V2 duplicates.
- `PlantLibrary_Workspace/docs/` holds dated deliverables (EVIDENCE/PROMPT/PROPOSAL).
- No TARGET page carries the head line (grep: 0 hits).

What adopting it would change:
- Every in-scope page gains a head, a foot and a catalog row.
- `CLAUDE.md` in each adopting repository gains the "Living documentation" pointer, and every batch row that changes behaviour names its doc pages.
- A gate script is needed. The `ast` locator resolution works only for Python repositories (PyApp, Server). TypeScript and Kotlin suites could check path locators only.
- For `system_description/` it means a hygiene decision releasing the frozen exempt tree; the K-7 interaction (Q-G-06) applies.

Recommendation Q-A2-05 (a). The mechanical link/anchor discipline is cheap and universal. The provenance apparatus pays off only for a reader-facing corpus that is actively maintained, and TARGET has none outside a frozen tree.

### §7.4 Scratch policy delta

| Aspect | Conductor | PlantLibrary suites (onboarding step 3) | Delta |
|---|---|---|---|
| Root | `.tmp/` only, gitignored (`C:\Programmierung\Orchestrator_System\CLAUDE.md:145`) | `.tmp/` only, gitignored in all six (`…onboarding-runbook…md:909`); superproject: no `.tmp/` ignore, no paragraph | superproject gap (only matters if a superproject step writes scratch) |
| Interior | `.tmp/pt/d` (pinned basetemp), `.tmp/p/<slug>`, `.tmp/chunks/`, `.tmp/c/base-*` (closeout base worktrees), `.tmp/validation/<batch>/genNN/.live`, `.tmp/.reclaim.lock`, `.tmp/worker-runs` | `.tmp/chunks/<run-id>`, `.tmp/p/<slug>` / `.tmp/p/<run-id>` (`PlantLibrary_PyApp/CLAUDE.md:385-401`) | PlantLibrary matches the `7ad02b1` layout. `c`, `validation` and `.live` arrive only with `closeout.py`. Dashboard, AndroidApp and Workspace carry closeout lines for a harness they do not have (F-A2-18) |
| Gate | operator-only `scratch-gate` skill over `reclaim_scratch.py`; exit 0 recorded before releasing dispatch or before a session's first validation; workers never run it (`…\CLAUDE.md:147-157`) | no gate procedure; PyApp has the script; `run_validation.py`'s preflight runs it implicitly | add the skill to PyApp and Server only (RC-A2-24) |
| Reclaim | report → `--reclaim` → printed elevated block; `--sweep-older-than` with `--apply`; never-list includes `.tmp/pt/d`, worktrees, `.live` | `7ad02b1` reclaim (no sweep, no lock) | sweep and lock arrive only with a re-port (RC-A2-03) |
| Elevation | never run pytest elevated; never point a basetemp outside the repository | same sentence in step 4's constraints (`…onboarding-runbook…md:541`) | none |
| Machine slot | one closeout at a time; lease file under `C:\ProgramData\Conductor\leases` (`…\CLAUDE.md:191-193`) | no lease; kickoff gives the slot to the Conductor | arrives with the re-ported `run_chunks.py` (F-A2-20) |
| Checked by | `tests/test_repo_hygiene.py` retired scratch names | kit `scratch` module off in all seven | Q-A2-06 (a) |

### §7.5 Parity checker and package checker against the Conductor's contract (scripts only)

- **Parity.** PlantLibrary's `SW_Development/scripts/harness/check_harness_parity.py` is the Conductor's 2026-08-05 shape, trimmed (`:1-10`). It byte-compares `.claude/skills` with `.codex/skills`, allowing `validate-real-stack/SKILL.md` to differ (`:22`). It pairs agent stems (`:58-83`) and self-tests one drift (`:95-117`). The Conductor's current checker has moved on three axes:
  - Codex is frozen: no more `.claude`↔`.codex` compare; both are pinned to `10177e3` blobs (`…\check_harness_parity.py:213-270`).
  - It carries v5 facts and the Section Map (Conductor-only).
  - It guards the harness copies themselves (`-p no:randomly` chunk-argv parity `:575-598`; no mirrored ceiling constants `:601-626`) and is the closeout's preflight (`closeout.py:824-828`).

  Neither checker looks into submodules (F-A2-11). The B7 extension is RC-A2-08. The freeze half waits on Q-G-09.
- **Package.** `SW_Development/scripts/harness/check_batch_packages.py` does not restate the contract. It imports `conductor.batch_package.parse_package` (`:15-20`) and buckets error messages by substring (`:28-40`). Its divergence is provenance, not rules: it judges with whichever parser instance 2's `src` holds. The Conductor's parser changed at `f904c8d` (model tuple: a trailing parenthetical override is now ignored) and `6526c93` (AM-51 counts a row's own record). Its scan roots include `PlantLibrary_Workspace\strategy\*` and `system_description\*` (`:23-27`), which the onboarding §9 item 4 note puts outside the intake root by design.
  
  PyApp's `tests/test_batch_package_contract.py` is a third reading: a hand restatement of the parser's structure. It does not import the parser (`:9-17`), so it cannot see grammar changes upstream. The Conductor additionally guards row premises (`cites:` clauses), `SCOPE.md` allowlists and out-of-band markers with parser-backed tests (RC-A2-19). PlantLibrary has none of these; A7 decides whether to make them part of the census.

### §7.6 Non-pytest suites: what a harness port would mean, and the step-8 status

- **What "port" can mean today.** The Conductor's harness maps touched paths to pytest nodes only. Every product path in Dashboard (`src/**`, vitest under `tests/`, playwright `e2e/`), AndroidApp (Gradle modules `app/`, `core/`, `feature/`; 0 `*Test.kt` files, `GC-2006`) and SharedContracts (`openapi/`, `generated/`, `schemas/`; one pytest module `tests/contract_validation/test_examples_against_schemas.py` plus `scripts/validate_contracts.py`) would refuse as `unmapped touched path`. The census calls this out: "no harness port can work since every product path is unmapped by design" (`C:\Programmierung\Orchestrator_System\implementation\Conductor_V2\planning\PLAN_gap-census-handoff_2026-09-29.md:871`). The Workspace has no product code: its proof is structural (hygiene, links, package census).
- **Meaningful scope now**, per suite:
  1. the static guards of §7.2;
  2. an adapted `run_validation.py` with its sibling, so `run-batch` §6 item 1 is followable for long builds (F-A2-10, RC-A2-01);
  3. the suite's own build/test commands in its `CLAUDE.md` as row validations;
  4. no closeout matrix. A batch there closes on its rows' named validations, as it already does out of band (onboarding step 9).
- **Step-8 status in the Conductor.** No `PROPOSAL_per-project-closeout-adapter` exists. The problem it was to state (PL-F-6) is absorbed into proposal A (`…\proposal\PROPOSAL_project-contract-and-validation-profiles_2026-09-22.md:680`). That proposal defines `gradle`, `npm` and `contracts` profiles over a `command` adapter: exit-code classification first, a JUnit-XML classifier as a named follow-up (`:296-298`, `:317-319`, `:341-342`). Its project contract `.conductor/project.yaml` is sketched at `:229-256`.
  - Harness half: `CD2-B543` (grammars), `B544` (registry + pytest adapter), `B545` (`command` adapter + docs/audit/planning), `B546` (ops/design), `B547` (project contract); all `todo`.
  - Product half: A4 at `st-29`, "not yet a batch" (`PLAN_conductor-native_2026-10-10.md:79-81`).
  - The per-project steps for SharedContracts, Dashboard and Android are `ob-25`, "not written yet, deliberately", after PyApp/Server's `ob-24` (`PROMPTS_project-onboarding-to-e3_2026-09-30.md:86`).
  - TARGET's own §L still lists step 8 as `todo` (`…onboarding-runbook…md:915`).

  Recommendation Q-A2-03 (a): B8 flips step 8 to superseded, citing proposal A and `ob-25`. A harness port for these four suites is deferred to the Conductor's profile rollout. The register gains one deferred-validation row per suite for Phase C.
