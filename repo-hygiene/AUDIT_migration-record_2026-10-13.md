# AUDIT — migration record: SW_Development and six submodules (2026-10-13)

*Step `M-8` of `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` (§16, item 3), run as step `B3-1` of the
master rework program. Written from the Repo Hygiene Template Kit's `templates/AUDIT_migration-record_TEMPLATE.md`
(kit `0.2.1`, `810733e`), adopted per `rework/REGISTER_conductor-reuse-candidates_2026-10-13.md` row `RC-A6S-04`. One
record for the seven repositories, under the name runbook §16 gives it (the template's per-repository
`AUDIT_migration-record-<repository>_<date>.md` in each `planning` root would write six submodules, which this step does
not touch). The closing record of migration steps `M-1`…`M-7`: every candidate the rename map named has a disposition,
the counts reconcile with `REGISTER_target-corpus-census_2026-10-13.md` §2, the sweep's residue is accounted for by
category, and the verdicts are quoted. Edited never.*

## 1. Scope and baseline

| | |
|---|---|
| Repositories | SW_Development (`master`, `fda7524`) and PlantLibrary_PyApp, _Server, _SharedContracts, _Dashboard, _AndroidApp, _Workspace (each `main`; heads in the census §1) |
| Rename map | `repo-hygiene/MATRIX_rename-map_2026-09-16.md`, confirmed at gate `GM` — "Yes, all recommendations accepted (Recommended)" (2026-09-16) |
| Census registers | baseline `repo-hygiene/REGISTER_target-corpus-census_2026-09-15.md` (HEADs `6ecc155`, `5cefe62`, `5c312d3`, `75846a9`, `472e7d2`, `b75265a`, `5147569`); post-migration `repo-hygiene/REGISTER_target-corpus-census_2026-10-13.md` |
| Decision entries cited or added by the migration | SW `D-2026-09-16-03`; PyApp `D-2026-09-16-03` (re-pin), `-04`; Server, SharedContracts, Dashboard, AndroidApp `D-2026-09-17-01` (re-pin), `-02`; Workspace `D-2026-09-17-01` (re-pin), `-02` (four general roots), `-03`. The anchoring entries `D-2026-09-16-01` in every repository carry the holds and exempt trees |
| Roots migrated | SW: `repo-hygiene`, `onboarding` (general), `handovers` (handovers, date-anywhere); `rework` (general) added later by `D-2026-10-13-01`. Each suite: `implementation/System_V1_Implementation/planning`, `proposal` (standard), `handovers` (date-anywhere). Workspace: those three for SV1 and for `implementation/System_Design_Architecture`, plus `docs`, `docs/proposals`, `prompts`, `implementation/Server_VM_Setup` (general) |

## 2. Disposition table

Counts per repository first; then one row per file that changed name or place, one row per held name, and one row per
group of identically dispositioned files (the group's members are listed in the map section named).

| repo | candidates | renamed / moved | held | exempt | set-folder (members) | already compliant | frozen | pinned | generated | legacy |
|---|---|---|---|---|---|---|---|---|---|---|
| SW_Development | 6 | 1 moved | 3 | 1 | 0 | 4 (2 also held) | 0 | 0 | 0 | 0 |
| PlantLibrary_PyApp | 31 | 2 | 4 (2 moot) | 27 (legacy tree) | 0 | 0 | 64 | 0 | 23 | 38 |
| PlantLibrary_Server | 5 | 3 (2 released) | 2 | 0 | 0 | 0 | 10 | 0 | 0 | 0 |
| PlantLibrary_SharedContracts | 1 | 0 | 1 | 0 | 0 | 0 | 9 | 0 | 134 | 0 |
| PlantLibrary_Dashboard | 5 | 2 (2 released) | 3 | 0 | 0 | 0 | 51 | 0 | 0 | 0 |
| PlantLibrary_AndroidApp | 2 | 0 | 2 | 0 | 0 | 0 | 22 | 0 | 0 | 0 |
| PlantLibrary_Workspace | 53 | 7 | 15 + 1 set folder | 1 | 3 renamed (22); 4 held in sets (19 members) | 0 | 205 | 121 | 1 | 0 |

Frozen, pinned, generated and legacy are the checker's exempt-tree file counts today (census §1); they are never renamed.

| Old path | Disposition | New path (or target on release) | TYPE | Citer / entry | Note |
|---|---|---|---|---|---|
| SW `HANDOVER_batch-package-schema-drift_2026-09-15.md` | moved | `handovers/HANDOVER_batch-package-schema-drift_2026-09-15.md` | HANDOVER | `D-2026-09-16-03`; hold re-declared at the new path | basename unchanged (`G0` Q4) |
| SW `onboarding/AUDIT_skill-assumptions_2026-09-15.md`, `onboarding/REGISTER_package-census_2026-09-15.md` | held (already compliant) | unchanged | AUDIT, REGISTER | onboarding runbook; onboarding-runbook group | released by the runbook retiring (Q-A6S-02 (a)) |
| SW `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md`, `repo-hygiene/PROMPT_kit-bootstrap-session_2026-09-15.md` | already-compliant | — | PROMPTS, PROMPT | — | |
| SW `IMPLEMENTATION_PLAN.md` | exempt | unchanged (census target `PLAN_plantlibrary-continuation_2026-08-05.md` not applied) | PLAN | `GM` proposal 1; `D-2026-09-16-03` (hold released moot, `exempt-name`) | header 2026-08-04, git-created 2026-08-05 |
| PyApp `GUI/FUTURE_GUI_DEVELOPMENT_PROPOSAL.md` | renamed+moved | `…/SV1/proposal/PROPOSAL_future-gui-development-workflow_2026-07-03.md` | PROPOSAL | `D-2026-09-16-04` | |
| PyApp `GUI/source_derived/Source_GUI_Integration_Report.md` | renamed+moved | `…/SV1/planning/EVIDENCE_source-gui-integration-run_2026-07-04.md` | EVIDENCE | `D-2026-09-16-04` | |
| PyApp `…/SV1/proposal/PYAPP_V1_PROPOSAL.md` | held | `PROPOSAL_pyapp-v1_2026-07-10.md` | PROPOSAL | `…/SV1/STATE.md:11`; live package | M-9 ready (Q-A6P-03 (a)); header 2026-07-09, git-created 2026-07-10 |
| PyApp `GUI/screen_structures/improvements.md` | held | `…/SV1/handovers/FINDING_gpt-screen-requirement-merge_2026-07-01.md` | FINDING | Design initiative (pinned tree); pinned | permanent (Q-A6P-05 (a)) |
| PyApp `Documentation/` (27 candidates, map §4) | exempt | never renamed; each row carries the name it would have had | — | `exempt-tree: Documentation` (legacy), `D-2026-09-16-01`:132 | two of them are also held, moot while the tree stands: `Design_Implementation_Claude.md` (pinned), `plant_information_system_implementation_plan_v1.md` (code) |
| Server `docs/SV-CONTRACT-01_contract_validation_report.md` | renamed+moved | `…/SV1/planning/AUDIT_sv-contract-01-contract-validation_2026-07-04.md` | AUDIT | `D-2026-09-17-02` | |
| Server `docs/SV-B07_runtime_verification_report.md` | renamed+moved | `…/SV1/planning/EVIDENCE_sv-b07-runtime-verification_2026-07-05.md` | EVIDENCE | released, `D-2026-09-17-02`:307 (proposal 6) | |
| Server `docs/SV-B08_deployment_hardening_report.md` | renamed+moved | `…/SV1/planning/EVIDENCE_sv-b08-deployment-hardening_2026-07-05.md` | EVIDENCE | released, `D-2026-09-17-02`:308 (proposal 6) | |
| Server `…/SV1/proposal/SERVER_V1_PROPOSAL.md` | held | `PROPOSAL_server-v1_2026-07-10.md` | PROPOSAL | `…/SV1/STATE.md:15`; live package | M-9 ready (Q-A6V-02 (a)) |
| Server `docs/SV-B07_dashboard_endpoint_coverage_report.md` | held | `…/SV1/planning/AUDIT_sv-b07-dashboard-endpoint-coverage_2026-07-05.md` | AUDIT | `app/api/routes/dashboard_support.py:2`, `app/workers/tasks.py:9`; code | released by a code edit in a batch |
| SharedContracts `…/SV1/proposal/SHAREDCONTRACTS_V1_PROPOSAL.md` | held | `PROPOSAL_sharedcontracts-v1_2026-07-10.md` | PROPOSAL | `…/SV1/STATE.md:11`; live package | M-9 ready (Q-A6C-04 (a)) |
| Dashboard `docs/WD-A11Y-01_validation_report.md` | renamed+moved | `…/SV1/planning/EVIDENCE_wd-a11y-01-accessibility-validation_2026-07-05.md` | EVIDENCE | released, `D-2026-09-17-02`:308 (proposal 6) | |
| Dashboard `docs/WD-PARITY-01_parity_report.md` | renamed+moved | `…/SV1/planning/AUDIT_wd-parity-01-page-contract-parity_2026-07-05.md` | AUDIT | released, `D-2026-09-17-02`:309 (proposal 6) | |
| Dashboard `…/SV1/proposal/DASHBOARD_V1_PROPOSAL.md` | held | `PROPOSAL_dashboard-v1_2026-07-10.md` | PROPOSAL | `…/SV1/STATE.md:14`; live package | M-9 ready (Q-A6D-02 (a)) |
| Dashboard `docs/WD-MOCKUP-UPGRADE_PROPOSAL.md` | held | `…/SV1/proposal/PROPOSAL_wd-mockup-driven-dashboard-upgrade_2026-07-07.md` (`MC-1`; the directive at `D-2026-09-16-01`:137 still says `planning/`) | PROPOSAL | DTI `METHODOLOGY_RECONCILIATION.md:24`; pinned | M-9 ready (Q-A6D-03 (a)) |
| Dashboard `docs/WD-UX-10_mockup_parity_report.md` | held | `…/SV1/planning/AUDIT_wd-ux-10-mockup-parity_2026-07-07.md` | AUDIT | as above; pinned | M-9 ready (Q-A6D-03 (a)) |
| AndroidApp `…/SV1/proposal/ANDROIDAPP_V1_PROPOSAL.md` | held | `PROPOSAL_androidapp-v1_2026-07-10.md` | PROPOSAL | none (policy hold, Q5c) | M-9 ready (no citer; Q-A6A-02 (a)) |
| AndroidApp `docs/security_token_storage_acceptance.md` | held | `…/SV1/proposal/PROPOSAL_an-mvp-security-01-auth-token-storage-deviation_2026-07-06.md` (`MC-1`; the directive at `D-2026-09-16-01`:144 still says `planning/`) | PROPOSAL | `AuthTokenStore.kt:27`; live anchors `TASK_CHECKLIST.md:56`, `TASK_CONTEXT.md:350`; code | released by a code edit in a batch |
| Workspace `docs/garden-app-product-research.md`, `…_2.md` | renamed | `docs/EVIDENCE_garden-apps-4-products_2026-07-11.md`, `docs/EVIDENCE_garden-apps-13-products_2026-07-11.md` | EVIDENCE | `D-2026-09-17-03` | |
| Workspace `docs/fable5_business_proposal_prompt.md`, `docs/fable5_system_strategy_proposal_prompt.md` | renamed | `docs/PROMPT_fable5-business-gtm-proposal_2026-07-11.md`, `docs/PROMPT_fable5-system-strategy-proposal_2026-07-11.md` | PROMPT | `D-2026-09-17-03` | proof scan 0 lines |
| Workspace `docs/proposals/ENRICHMENT_V2_PROPOSAL.md`, `GARDEN_DESIGNER_PROPOSAL.md` | renamed | `docs/proposals/PROPOSAL_enrichment-v2_2026-07-10.md`, `PROPOSAL_garden-designer_2026-07-10.md` | PROPOSAL | `D-2026-09-17-03` | |
| Workspace `implementation/Server_VM_Setup/DockerDesktop_Audit_Migration_Prompt.md` | renamed | `implementation/Server_VM_Setup/PROMPT_docker-desktop-audit-migration_2026-07-10.md` | PROMPT | `D-2026-09-17-03` | header 2026-07-09 |
| Workspace `docs/fable5_business_proposal/`, `fable5_strategy_proposal/`, `fable5_strategy_proposal_v2/` | set-folder | `docs/PROPOSAL_fable5-business-gtm_2026-07-11/`, `docs/PROPOSAL_fable5-product-strategy-v1_2026-07-11/`, `docs/PROPOSAL_fable5-product-strategy-v2_2026-07-11/` | PROPOSAL | `D-2026-09-17-03` | 11 + 7 + 5 files (22 candidates + the v2 `README.md`), names unchanged |
| Workspace `docs/proposals/Repo_Restructure_MVP_V1_Split/` | held (set folder) | `docs/proposals/PROPOSAL_repo-restructure-mvp-v1-split_2026-07-15/` | PROPOSAL | the record's own `D-2026-09-16-01`:161; record group | rename reverted at `M-7` (`D-2026-09-17-03` item 2); released by kit patch `K-7`, then `M-9` |
| Workspace `MVP_Reconciliation/` (00–06) | held in set (3 held members) | `docs/SNAPSHOT_mvp-reconciliation_2026-07-10/` (proposal 4) | SNAPSHOT | members 02, 04, 05: live anchors (census §3 #19–#21) | 4 free members wait with the set |
| Workspace SV1 `proposal/00`, `01`, `02` | held in set | `…/SV1/proposal/PROPOSAL_v1-system_2026-07-10/` (proposal 3) | PROPOSAL / AUDIT | live `STATE.md` and anchors in six packages (census §3 #16–#18) | Q-A6W-03 (a): anchors stay |
| Workspace SDA `proposal/00`–`04` | held in set | `…/SDA/proposal/PROPOSAL_system-design-architecture_2026-07-09/` (proposal 3) | PROPOSAL | pinned DTI tree and Design kit (00–03); code (04) (census §3 #23–#27) | owners outside this track |
| Workspace `prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | held | `…/SV1/handovers/HANDOVER_process-improvements_2026-07-10.md` (`MC-2`) | HANDOVER | live anchors PyApp, Dashboard, AndroidApp; frozen `System_Tooling/STATE.md` | terminal-`STATE.md` group, live-cited |
| Workspace `…/SDA/MODEL_RECOMMENDATION.md`, `docs/proposals/PlantLibrary_Full_Implementation_Update.md`, `prompts/reference/SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | held | `…/SDA/proposal/PROPOSAL_sda-model-allocation_2026-07-09.md`, `docs/proposals/PROPOSAL_full-implementation-package_2026-07-16.md`, `prompts/PROMPT_setup-android-test-environment_2026-07-16.md` | PROPOSAL, PROPOSAL, PROMPT | the restructure set's `manifests/MANIFEST_*.csv`; code | released by a code edit; the CSVs move with their set, unedited |
| Workspace `implementation/Server_VM_Setup/ServerSetUp_MVP.md` | exempt | never renamed | — | `exempt-name`, `D-2026-09-16-01`:150 | GUIDE-shaped (Q6) |

## 3. Counts

| Class | Register (2026-09-15) | This record | Difference explained |
|---|---|---|---|
| candidates | 103 | 103 | none created, deleted or re-classified; deliverables written since are compliant in roots (census §2a) |
| renamed in place | — | 7 (Workspace) | map §9b–§9d |
| moved (incl. move-renames) | — | 8 (SW 1 move; PyApp 2, Server 3, Dashboard 2 move-renames) | with the 7 renames, the 15 file renames and moves map §13 planned |
| held | 34 (+1 policy) | 30 + 1 set folder | 4 released by proposal 6, 1 released moot (proposal 1); the set folder added by the `M-7` deviation |
| exempt by decision | — (`G0` Q4/Q6 open) | 29 candidates (SW 1, PyApp 27, Workspace 1) | map §13 `X` |
| set folders | — | 3 renamed (22 candidate members) + 4 held sets | map planned 4 renames; 1 reverted (`M-7`) |
| already compliant | 5 | 4 (+ the moved handover, compliant in its new root) | the register counted the root handover compliant; the map counts it `MV` |
| frozen / pinned / generated (never renamed) | 361 / 107 / 140 | 361 / 121 / 158 (+ legacy 38) | pinned +14 (methodology 4.1.0, DTI close); generated +18 (PyApp `app/` tree); legacy is PyApp `Documentation/` as an exempt tree |

## 4. The reference sweep

| | |
|---|---|
| Editable list | per step, as each `M-n` ledger row records: `onboarding/INDEX.md:10` (SW); `GUI/README.md:32`, `GUI/GUI_CONTEXT_INDEX.md:25` (PyApp); `openapi/README.md:12`, one paragraph of `docs/README.md` (Server); `docs/README.md` (Dashboard); 27 lines in 12 files (Workspace); none in SharedContracts and AndroidApp (nothing renamed) |
| Never-edit list | package-schema files (`STATE.md`, anchors), frozen and pinned trees, generated files, code, the decision records, the Workspace transcript `docs/Fable5_Prompt_Improvements` — served by the "Renamed" tables |
| Residue after the sweep (re-measured today) | 231 hits of the 17 old names (14 file basenames, 3 folder names) across the seven repositories: track and program documents 107 · decision records 61 · mapping tables and indexes 27 · frozen or pinned trees 23 · transcript 7 · other 6 — the moved PyApp evidence file's own historical lines `:13`, `:20`; the restructure set member `VERIFICATION_REPORT.md:240,243`; the `MVP_Reconciliation/00_SOURCE_INVENTORY.md:60` set member; the superproject's exempt `IMPLEMENTATION_PLAN.md:370`. Every "other" hit was named as residue in its step's ledger row; no live citer of an old name remains |

## 5. The commit split

The template's three-commit split was not used: each repository migrated in one commit carrying the `git mv`s, the sweep,
the `INDEX.md` lines and "Renamed" tables and the decision entry, followed by one superproject commit bumping the gitlink
with the ledger flip (the track runbook §14–§15 shape). Re-pins to kit `0.2.1` landed first, inside the same commit.

| repo | migration commit | superproject commit | re-pin |
|---|---|---|---|
| SW_Development | `fd71295` (`M-1`) | — (same commit) | `e639e5c` (`K-6`, `D-2026-09-16-02`) |
| PlantLibrary_PyApp | `faa6072` (`M-2`) | `6c48599` | in `faa6072`, `D-2026-09-16-03` |
| PlantLibrary_Server | `f1a31b9` (`M-3`) | `06dfd0f` | in `f1a31b9`, `D-2026-09-17-01` |
| PlantLibrary_SharedContracts | `d43f7a2` (`M-4`) | `50b3d74` | in `d43f7a2`, `D-2026-09-17-01` |
| PlantLibrary_Dashboard | `7795fc8` (`M-5`) | `5bfbdc1` | in `7795fc8`, `D-2026-09-17-01` |
| PlantLibrary_AndroidApp | `38877e9` (`M-6`) | `c1d8092` | in `38877e9`, `D-2026-09-17-01` |
| PlantLibrary_Workspace | `a12703c` (`M-7`) | `40233c6` | in `a12703c`, `D-2026-09-17-01`; roots `D-2026-09-17-02` |
| this record | — | the `M-8` commit (`B3-1`) | — |

## 6. Holds outstanding

Thirty held names and one held set folder. The citers, re-verified by `git grep` at HEAD, are in
`REGISTER_target-corpus-census_2026-10-13.md` §3 (rows #1–#31); the group and the releaser are summarised here.

| Held name | Group | Citer | Released by | Target on release |
|---|---|---|---|---|
| SW `handovers/HANDOVER_batch-package-schema-drift…`, `onboarding/AUDIT_skill-assumptions…`, `onboarding/REGISTER_package-census…` | onboarding runbook | the onboarding runbook (`:5`; `:211,212,216,905`; `:251,584,911`); the audit also by PyApp `scripts/harness/regression_scope.py:33`, `scope_cap.py:5` | the onboarding runbook retiring (Q-A6S-02 (a)); the audit stays in place while code cites it | unchanged names |
| PyApp, Server, SharedContracts, Dashboard, AndroidApp `…/SV1/proposal/<SUITE>_V1_PROPOSAL.md` (5) | live package | each package's `STATE.md` (AndroidApp: none) | **`M-9` now** — operator release recorded 2026-10-13 (Q-A6P-03, Q-A6V-02, Q-A6C-04, Q-A6D-02, Q-A6A-02, each (a)) → step `B3-4` | `PROPOSAL_<suite>-v1_2026-07-10.md` |
| Dashboard `docs/WD-MOCKUP-UPGRADE_PROPOSAL.md`, `docs/WD-UX-10_mockup_parity_report.md` | pinned | the closed Design initiative (three lines) | **`M-9` now** — operator release words (Q-A6D-03 (a)) → step `B3-4` | `…/SV1/proposal/PROPOSAL_wd-mockup-driven-dashboard-upgrade_2026-07-07.md`, `…/SV1/planning/AUDIT_wd-ux-10-mockup-parity_2026-07-07.md` |
| PyApp `GUI/screen_structures/improvements.md`, `Documentation/Design_Implementation_Claude.md` | pinned | the Design initiative | permanent (Q-A6P-05 (a)); the second is moot while the legacy tree stands | as §2 |
| PyApp `Documentation/plant_information_system_implementation_plan_v1.md`; Server `docs/SV-B07_dashboard_endpoint_coverage_report.md`; AndroidApp `docs/security_token_storage_acceptance.md` | code | a test docstring; two module docstrings; `AuthTokenStore.kt:27` plus two live anchors | a code edit in a batch (policy A.0.5) | as §2 |
| Workspace SV1 `proposal/00`–`02`; `MVP_Reconciliation/02`, `04`, `05` | live package | `STATE.md` and anchors in six packages | the anchors stop citing them; Q-A6W-03 (a) keeps them | the two set folders of §2 |
| Workspace `prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | terminal `STATE.md` + live | PyApp, Dashboard, AndroidApp anchors | those anchors migrating | `…/SV1/handovers/HANDOVER_process-improvements_2026-07-10.md` |
| Workspace SDA `proposal/00`–`03` | pinned | DTI tree; Design kit `TEMPLATE_SPEC.md` | the Design kit's owner or a re-pin | SDA set folder |
| Workspace SDA `proposal/04`, `MODEL_RECOMMENDATION.md`, `PlantLibrary_Full_Implementation_Update.md`, `SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | code | `semantic-roles.json:3` and Design-kit tools; the restructure manifests | a code edit | as §2 |
| Workspace `docs/proposals/Repo_Restructure_MVP_V1_Split/` | record (set folder) | `D-2026-09-16-01`:161 | kit patch `K-7` (Q-G-06, owed item 9), then `M-9` | `docs/proposals/PROPOSAL_repo-restructure-mvp-v1-split_2026-07-15/` |

## 7. Verdict

The checker's `check` in each repository, 2026-10-13, verbatim (each preceded by its `held:` lines):

```text
SW_Development               repo-hygiene: pass with holds — 0 violations, 3 held
PlantLibrary_Workspace       repo-hygiene: pass with holds — 0 violations, 10 held
PlantLibrary_PyApp           repo-hygiene: pass with holds — 0 violations, 1 held
PlantLibrary_AndroidApp      repo-hygiene: pass with holds — 0 violations, 1 held
PlantLibrary_Dashboard       repo-hygiene: pass with holds — 0 violations, 1 held
PlantLibrary_Server          repo-hygiene: pass with holds — 0 violations, 1 held
PlantLibrary_SharedContracts repo-hygiene: pass with holds — 0 violations, 1 held
```

`census`, `## Repository totals`, verbatim:

```text
SW_Development               totals: 41 files, 34 compliant, 0 candidates, 4 exempt, 3 held, 0 set folders
PlantLibrary_Workspace       totals: 30 files, 7 compliant, 0 candidates, 12 exempt, 10 held, 3 set folders
PlantLibrary_PyApp           totals: 6 files, 2 compliant, 0 candidates, 3 exempt, 1 held, 0 set folders
PlantLibrary_AndroidApp      totals: 4 files, 0 compliant, 0 candidates, 3 exempt, 1 held, 0 set folders
PlantLibrary_Dashboard       totals: 6 files, 2 compliant, 0 candidates, 3 exempt, 1 held, 0 set folders
PlantLibrary_Server          totals: 7 files, 3 compliant, 0 candidates, 3 exempt, 1 held, 0 set folders
PlantLibrary_SharedContracts totals: 4 files, 0 compliant, 0 candidates, 3 exempt, 1 held, 0 set folders
```

The superproject's lines are as measured before this record and its two siblings were added; with them and their index
lines the `repo-hygiene` root gains two compliant files and `handovers` one; the final run before the `M-8` commit
printed `repo-hygiene: pass with holds — 0 violations, 3 held` and
`totals: 44 files, 37 compliant, 0 candidates, 4 exempt, 3 held, 0 set folders`.
