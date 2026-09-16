# MATRIX — rename map for seven repositories (2026-09-16)

*Produced by step `M-0` of `PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` (§13), Fable 5.1 · high, over*
*`C:\Programmierung\SW_Development` at `bb9ba9a` (`master`, clean) and its six submodules, each clean on its own `main`.*
*Nothing was renamed or moved by this step; no `git mv`. The map is derived from `REGISTER_target-corpus-census_2026-09-15.md`*
*(the candidates, §2; the hold register, §3), the seven decision records `hygiene\HYGIENE_DECISIONS.md` entry `-01`*
*(the exempt, frozen, pinned, generated and held sets confirmed at `GA`), gate `G0` (runbook §1d: Q4/Q4b, Q5/Q5a/Q5b/Q5c,*
*Q6) and `KIT_SPEC.md` §1–3. It is presented at gate `GM`; the first `git mv` waits for the operator's words in §0.*

## 0. Gates

**`GA` — recorded.** The seven decision records were confirmed 2026-09-16 at the opening of the `A-8` session, before
the `REPORT` question was put (runbook §2 item 12: "`GA` was confirmed first (the sets are unaffected)"; every suite's
`D-2026-09-16-02` entry cites that line). The operator's verbatim words for `GA` were not captured in the runbook or in
any record at the time; the runbook's §4 carries the same sentence as this preamble. `GM` was asked to restate them; the
restatement, verbatim, 2026-09-16: "GA confirmed (Recommended)" — recorded here and in the runbook's §4.

**`GM` — open.** The question: is this map confirmed — old → new per file (§3–§9), the holds with their group and
target on release (§10), the date divergences (§11), the set folders, the moves, the two map calls and the six
proposals (§12)? The operator's answer, 2026-09-16, verbatim: "Yes, all recommendations accepted (Recommended)" — given to the question that listed the six proposals and
the two map calls with their recommendations; every recommendation of §12 stands. Recorded in the runbook's §4 and §L in the
`M-0` commit.

## 1. Re-measurement, 2026-09-16

**Method.** The kit's checker in census mode (`python scripts\hygiene\repo_hygiene_check.py census`, read-only,
`git status` unchanged before and after) in all seven repositories; the census register's own walk reproduced over
tracked `.md` files with the register's exclusions (the four runtime mirrors, `node_modules`, `.venv`, `build`, `.tmp`,
caches, `graphify-out`); `git diff --name-status <census HEAD> HEAD -- '*.md'` per repository for the delta;
`git log --follow --diff-filter=A` for the git-created date of every new file. Hold-class citers re-verified by
`git grep -F` at today's HEADs in all seven repositories and in `C:\Programmierung\Design_Template_Kit` at `8e708f8`.

### 1a. HEADs and the checker's census totals (declared roots only)

| repo | census HEAD | HEAD today | checker census: files · compliant · candidates · exempt · held · set folders | exempt-tree files |
|---|---|---|---|---|
| SW_Development | `6ecc155` | `bb9ba9a` | 11 · 6 · 0 · 3 · 2 · 0 (roots `repo-hygiene`, `onboarding`, `handovers`) | — |
| PlantLibrary_PyApp | `5cefe62` | `edcd1e6` | 4 · 0 · 0 · 3 · 1 · 0 | 125 (64 frozen, 38 legacy, 23 generated) |
| PlantLibrary_Server | `5c312d3` | `7ac804d` | 4 · 0 · 0 · 3 · 1 · 0 | 10 (frozen) |
| PlantLibrary_SharedContracts | `75846a9` | `998806a` | 4 · 0 · 0 · 3 · 1 · 0 | 143 (9 frozen, 134 generated) |
| PlantLibrary_Dashboard | `472e7d2` | `f9028f0` | 4 · 0 · 0 · 3 · 1 · 0 | 51 (frozen) |
| PlantLibrary_AndroidApp | `b75265a` | `352ba26` | 4 · 0 · 0 · 3 · 1 · 0 | 22 (frozen) |
| PlantLibrary_Workspace | `5147569` | `ddeb9b3` | 14 · 0 · 0 · 6 · 8 · 0 | 313 (205 frozen, 107 pinned, 1 generated) |

The checker sees only the declared roots, so its "candidates 0" says that no non-compliant, unheld name sits in a root
today; the 98 names to rename all sit outside the roots (the census's §2), which is what the register says. The
superproject's two root-level holds (`HANDOVER_…`, `IMPLEMENTATION_PLAN.md`) are outside every root and therefore not in
its `held` count (the `A-1` finding); the record carries them.

### 1b. The corpus, register §1 against today

| repo | register §1 files | today | delta | what the delta is (git-created date; disposition) |
|---|---|---|---|---|
| SW_Development | 11 | 18 | +7 | `repo-hygiene\REGISTER_hygiene-harness-inventory_2026-09-15.md`, `REGISTER_target-corpus-census_2026-09-15.md`, `PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` (2026-09-15; compliant, this track's); `handovers\FINDING_kit-proof-floor-blocks-suite-anchoring_2026-09-16.md` (2026-09-16; compliant); `handovers\INDEX.md` (2026-09-16; exempt by construction); `hygiene\CONSUMED_HYGIENE.md`, `hygiene\HYGIENE_DECISIONS.md` (2026-09-16; the kit's anchoring folder, outside every root) |
| PlantLibrary_PyApp | 192 | 200 | +8 | `hygiene\*.md` (2, 2026-09-16); `implementation\System_V1_Implementation\SCOPE.md` (2026-09-15, onboarding `0be0e5a`; package schema); three root `INDEX.md` (2026-09-16); `validation\KNOWN_FAILURES.md`, `validation\ONBOARDING_harness-port.md` (2026-09-16, onboarding `9dd6e97`; validation evidence, catalogued per `KIT_SPEC.md` §1.7 — names outside the `<BATCH>_<slug>` shape, noted for the onboarding track, no action here) |
| PlantLibrary_Server | 47 | 53 | +6 | `hygiene\*.md` (2); `SCOPE.md` (2026-09-15, `020347e`); three `INDEX.md` |
| PlantLibrary_SharedContracts | 187 | 195 | +8 | `CLAUDE.md`, `AGENTS.md` (2026-09-16, `c51c5ff`; instruction files, exempt by name); `hygiene\*.md` (2); `SCOPE.md` (2026-09-15, `04fe99b`); three `INDEX.md` |
| PlantLibrary_Dashboard | 75 | 83 | +8 | the same eight (`CLAUDE.md`/`AGENTS.md` from `4eefc61`, `SCOPE.md` from `7cb48e9`) |
| PlantLibrary_AndroidApp | 56 | 64 | +8 | the same eight (`CLAUDE.md`/`AGENTS.md` from `869572f`, `SCOPE.md` from `3f67465`) |
| PlantLibrary_Workspace | 399 | 411 | +12 | `CLAUDE.md`, `AGENTS.md` (2026-09-16, `be56647`); `hygiene\*.md` (2); two `SCOPE.md` (2026-09-15, `36445cc`); six `INDEX.md` (2026-09-16) |
| **total** | **967** | **1024** | **+57** | no candidate was created, deleted, renamed or moved since the census; every new file is package schema, an instruction file, an index, the anchoring folder, validation evidence or a compliant deliverable of this track |

Modified but not moved since the census: the superproject's `onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md`
and `onboarding\REGISTER_package-census_2026-09-15.md`; every suite's `CLAUDE.md`/`AGENTS.md`, `implementation\README.md`
and live package anchors (`BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`) — the onboarding track's
schema migration moved several citing line numbers; the decision records carry today's lines, and no hold class changed.

### 1c. Hold citers, re-verified today

All 34 census holds stand, plus the `A-6` policy hold (`ANDROIDAPP_V1_PROPOSAL.md`, Q5c, no citer) — 35 held names. Spot
checks at today's HEADs: `onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md` cites `IMPLEMENTATION_PLAN.md` on
10 lines (17, 52, 210, 213, 217, 221, 685, 820, 845, 898), the root `HANDOVER` on line 5, the `AUDIT` on 4 lines and the
`REGISTER` on 3; PyApp `tests\services\test_ai_extraction_service.py:1`, Server `app\api\routes\dashboard_support.py:2`
and `app\workers\tasks.py:9`, AndroidApp `core\auth\…\AuthTokenStore.kt:27`, SharedContracts `design-tokens\semantic-roles.json:3`
and the two Workspace `MANIFEST_*.csv` rows still cite their held names; the pinned Design initiative still names
`improvements.md` (4 lines) and `Design_Implementation_Claude.md`; the Design kit at `8e708f8` still cites
`04_APPROVED_DESIGN_REVISION_2026-07-10.md` from five files. No citer has changed, so no hold is released by this map.

### 1d. Proof surfaces of the files that become `PROMPT_`/`PROMPTS_` in a declared root

With `docs\` and `implementation\Server_VM_Setup\` declared general roots at `M-7` (proposal 5), three renamed files fall
under the checker's proof-surface scan (`KIT_SPEC.md` §4). Scanned today with the kit's own detectors: `fable5_business_proposal_prompt.md`,
`fable5_system_strategy_proposal_prompt.md`, `DockerDesktop_Audit_Migration_Prompt.md` — zero `proof-argv`/`proof-prose`
lines. `SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` (held; target in `prompts\`) — zero. The two prompt-shaped members of the
`Repo_Restructure_MVP_V1_Split` set keep their names inside the set folder and are outside the scan; note that
`FOLLOWUP_CLOSURE_PROMPT.md:69` carries `python -m pytest tests -q --collect-only`, which a per-file rename to `PROMPT_…`
would report as `proof-argv` — the set-folder disposition (Q5b) is the one that keeps `M-7` green.

## 2. How to read the sections

One row per census candidate (plus every new file of §1b that is not already dispositioned there). **Disposition:**
`C` compliant, unchanged · `MV` moved by `git mv`, basename unchanged · `R` renamed by `git mv` · `MV+R` moved and renamed ·
`H` held — stays under its current name; the target column is the target on release · `X` exempt by decision — a
"never renamed" row citing the entry · `S` set folder — the folder is renamed as a folder (Q5b), the member keeps its name
(members held keep the folder waiting) · `K` catalogued, outside the rule. **TYPE** is the census proposal as adjusted by
Q6 (DECISION → `PROPOSAL` with status in the index line; REPORT → `EVIDENCE`; GUIDE → exempt product doc). **Date** is
git-created (Q5a); a header-date divergence is marked `†` and listed in §11. **Group** is the hold group of runbook §1b;
the citing file and its class follow. Paths are repository-relative; `…\SV1\` abbreviates `implementation\System_V1_Implementation\`
and `…\SDA\` abbreviates `implementation\System_Design_Architecture\`. Two map calls (`MC-1`, `MC-2`, §12) decide where a
moved file lands; rows show the recommended target and name the alternative.

## 3. SW_Development (superproject) — 6 candidates, 4 holds

Roots: `repo-hygiene\` (general), `onboarding\` (general), `handovers\` (handovers); root allowlist on. Record `D-2026-09-16-01`.

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `HANDOVER_batch-package-schema-drift_2026-09-15.md` | `MV` (+`H` against rename) | `handovers\HANDOVER_batch-package-schema-drift_2026-09-15.md` | HANDOVER · 2026-09-15 | onboarding-runbook · `onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md:5` (live runbook) | name already compliant; the move is Q4's; `onboarding\INDEX.md:10` links it as `../HANDOVER_…` — the one-line path fix `M-1` is allowed to make (runbook §1e); the runbook citation is served by the mapping table; `M-1`'s entry removes the name from the allowlist |
| `IMPLEMENTATION_PLAN.md` | **proposal 1** → `X` (recommended) | stays; exempt by decision, allowlisted (already `allowlist: IMPLEMENTATION_PLAN.md`) | PLAN · 2026-08-05 † (header 2026-08-04) | onboarding-runbook · the runbook, 10 lines (17, 52, 210, 213, 217, 221, 685, 820, 845, 898) | if proposal 1 is declined: `H`, target `PLAN_plantlibrary-continuation_2026-08-05.md`, released when the onboarding runbook retires; note the basename is shared with every frozen MVP package's `IMPLEMENTATION_PLAN.md` |
| `onboarding\AUDIT_skill-assumptions_2026-09-15.md` | `C` (`H` against rename) | unchanged | AUDIT · 2026-09-15 | onboarding-runbook · lines 211, 212, 216, 905 | nothing to do; listed as held in `onboarding\INDEX.md` by the mapping row |
| `onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | `C` | unchanged | PROMPTS · 2026-09-15 | — | another track's live runbook; never edited by this track |
| `onboarding\REGISTER_package-census_2026-09-15.md` | `C` (`H` against rename) | unchanged | REGISTER · 2026-09-15 | onboarding-runbook · lines 251, 584, 911 | nothing to do |
| `repo-hygiene\PROMPT_kit-bootstrap-session_2026-09-15.md` | `C` | unchanged | PROMPT · 2026-09-15 | — | untracked at census time, tracked since |

New since the census (§1b): the three track registers/runbook and the `FINDING` are `C`; the four `INDEX.md`/`hygiene\` files
are exempt by construction or outside every root. Outside the roots and governed by the allowlist only: `CLAUDE.md`,
`AGENTS.md`, `Todo.md` (git-ignored). Never-renamed rows from the record: none beyond the allowlist (no `exempt-tree`).

**`M-1` does:** one `git mv` (the handover), the `onboarding\INDEX.md` link fix, proposal 1's exemption entry, the three
roots' "Renamed 2026-09-16" tables (the handover's move row; the two `onboarding\` held rows; the exempt row).

## 4. PlantLibrary_PyApp — 31 candidates, 4 holds

Roots: `…\SV1\planning`, `…\SV1\proposal`, `…\SV1\handovers`. Record `D-2026-09-16-01`. Exempt legacy corpus `Documentation\`
(Q4b, `exempt-tree: Documentation — legacy`): the 27 candidates below are **never renamed**; the name the rule would have
given is kept in the row so the exemption can be lifted later without re-deriving it.

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `Documentation\Care_Profile_Enrichment_Implementation_Gaps_V1.md` | `X` | never renamed (`D-2026-09-16-01`, legacy corpus); rule name would be `AUDIT_care-profile-enrichment-gaps_2026-06-19.md` | AUDIT · 2026-06-19 | — | |
| `Documentation\Care_Profile_Enrichment_Implementation_V1.md` | `X` | never renamed; `PLAN_care-profile-enrichment-parser-only_2026-06-19.md` | PLAN · 2026-06-19 | — | |
| `Documentation\Care_Profile_Enrichment_Proposal_V1.md` | `X` | never renamed; `PROPOSAL_care-profile-enrichment-v1_2026-06-19.md` | PROPOSAL · 2026-06-19 | — | |
| `Documentation\Cross_Platform_Architecture_Proposal.md` | `X` | never renamed; `PROPOSAL_cross-platform-architecture_2026-06-21.md` | PROPOSAL · 2026-06-21 † | — | |
| `Documentation\Cross_Platform_Baseline_Audit.md` | `X` | never renamed; `AUDIT_cross-platform-baseline_2026-06-21.md` | AUDIT · 2026-06-21 † | — | |
| `Documentation\Cross_Platform_Checklist.md` | `X` | never renamed; `PLAN_cross-platform-task-tracking_2026-06-21.md` | PLAN · 2026-06-21 | — | |
| `Documentation\Cross_Platform_Implementation_Plan.md` | `X` | never renamed; `PLAN_cross-platform-delivery_2026-06-21.md` | PLAN · 2026-06-21 † | — | |
| `Documentation\Cross_Platform_Implementation_Plan_V1.md` | `X` | never renamed; `PLAN_cross-platform-delivery-v1_2026-06-21.md` | PLAN · 2026-06-21 | — | |
| `Documentation\Cross_Platform_Implementation_Plan_V2.md` | `X` | never renamed; `PLAN_cross-platform-delivery-v2_2026-06-21.md` | PLAN · 2026-06-21 | — | |
| `Documentation\Cross_Platform_Proposal_V1.md` | `X` | never renamed; `PROPOSAL_cross-platform-v1_2026-06-21.md` | PROPOSAL · 2026-06-21 | — | |
| `Documentation\Cross_Platform_Proposal_V2.md` | `X` | never renamed; `PROPOSAL_cross-platform-v2_2026-06-21.md` | PROPOSAL · 2026-06-21 | — | |
| `Documentation\Current_State_Assessment.md` | `X` | never renamed; `AUDIT_current-state_2026-06-21.md` | AUDIT · 2026-06-21 † | — | |
| `Documentation\DECISIONS_NEEDED.md` | `X` | never renamed; `REGISTER_open-decisions-final-workflow_2026-06-21.md` | REGISTER · 2026-06-21 † | — | |
| `Documentation\DataEnrichment_Proposal_Claude.md` | `X` | never renamed; `PROPOSAL_data-enrichment-pipeline_2026-06-16.md` | PROPOSAL · 2026-06-16 | — | |
| `Documentation\Design_Implementation_Claude.md` | `X` (+`H`) | never renamed; would be `PLAN_verdant-design-system-adoption_2026-06-16.md` | PLAN · 2026-06-16 | pinned · `PlantLibrary_Workspace\methodology\Design_Template_Initiative\INITIATIVE_PROPOSAL.md:130` (pinned tree) | the hold is moot while the legacy exemption stands; it survives a lifted exemption |
| `Documentation\Final_Workflow_Proposal_V1.md` | `X` | never renamed; `PROPOSAL_enrichment-workflow-v1_2026-06-19.md` | PROPOSAL · 2026-06-19 | — | |
| `Documentation\IMPLEMENTATION_CHECKLIST.md` | `X` | never renamed; `PLAN_enrichment-workflow-tasks_2026-06-21.md` | PLAN · 2026-06-21 † | — | |
| `Documentation\ImplementationPlan_Claude_V2.md` | `X` | never renamed; `PLAN_full-app-build-v2_2026-06-15.md` | PLAN · 2026-06-15 | — | |
| `Documentation\Phase_0_2_fixing.md` | `X` | never renamed; `FINDING_phases-0-2-gaps_2026-06-17.md` | FINDING · 2026-06-17 | — | |
| `Documentation\Phase_0_6_fixing.md` | `X` | never renamed; `FINDING_phases-0-6-gaps_2026-06-19.md` | FINDING · 2026-06-19 | — | |
| `Documentation\Target_Architecture_Recommendation.md` | `X` | never renamed; `PROPOSAL_target-architecture_2026-06-21.md` | PROPOSAL · 2026-06-21 † | — | |
| `Documentation\ToolbarButtons_Redesign_Claude.md` | `X` | never renamed; `PROPOSAL_toolbar-buttons-redesign_2026-06-16.md` | PROPOSAL · 2026-06-16 | — | |
| `Documentation\legacy-data-inventory.md` | `X` | never renamed; `REGISTER_legacy-sqlite-fixture_2026-06-22.md` | REGISTER · 2026-06-22 † | — | |
| `Documentation\plant_information_system_implementation_plan_gaps.md` | `X` | never renamed; `AUDIT_plant-information-system-phases-0-6_2026-06-17.md` | AUDIT · 2026-06-17 | — | |
| `Documentation\plant_information_system_implementation_plan_v1.md` | `X` (+`H`) | never renamed; would be `PLAN_plant-information-system-v1_2026-06-17.md` | PLAN · 2026-06-17 | code · `tests\services\test_ai_extraction_service.py:1` (module docstring) | moot while the exemption stands; a code-cited file never moves (A.0.5) |
| `Documentation\plant_information_system_proposal_v2.md` | `X` | never renamed; `PROPOSAL_plant-information-system-v2_2026-06-17.md` | PROPOSAL · 2026-06-17 | — | |
| `Documentation\spike-results.md` | `X` | never renamed; `EVIDENCE_backend-spikes_2026-06-22.md` | EVIDENCE · 2026-06-22 † | — | |
| `GUI\FUTURE_GUI_DEVELOPMENT_PROPOSAL.md` | **proposal 2** → `MV+R` | `…\SV1\proposal\PROPOSAL_future-gui-development-workflow_2026-07-03.md` (`MC-1`; `planning\` if Q4b is read literally) | PROPOSAL · 2026-07-03 | — (citers: `GUI\README.md:32`, sweep-editable) | |
| `GUI\source_derived\Source_GUI_Integration_Report.md` | **proposal 2** → `MV+R` | `…\SV1\planning\EVIDENCE_source-gui-integration-run_2026-07-04.md` | EVIDENCE · 2026-07-04 | — (citers: `GUI\GUI_CONTEXT_INDEX.md:25`, itself:13,20 — sweep-editable) | |
| `GUI\screen_structures\improvements.md` | **proposal 2** → `H` | `…\SV1\handovers\FINDING_gpt-screen-requirement-merge_2026-07-01.md` (`MC-1`; `planning\` if literal) | FINDING · 2026-07-01 | pinned · `…\Design_Template_Initiative\INITIATIVE_PROPOSAL.md:122`, `STATE.md:1695`, `evidence\00_inventory_reverification.md:64,94` (pinned tree) | released by the Design initiative's owner or a Design-kit re-pin, not this track; the frozen Dashboard `references\…\screen_requirements\improvements.md` shares the basename and is never renamed |
| `…\SV1\proposal\PYAPP_V1_PROPOSAL.md` | `H` | `PROPOSAL_pyapp-v1_2026-07-10.md` (same root) | PROPOSAL · 2026-07-10 † (header 2026-07-09) | live-package (Q5c) · `…\SV1\STATE.md:11` (state) | released by onboarding `2a`/`2b` for PyApp, then `M-9`; other citers (`…\SV1\README.md:5,63`, Workspace `00_V1_SYSTEM_PROPOSAL.md:226`, the transcript) are sweep-editable or mapping-covered |

Never-renamed rows from the record (`D-2026-09-16-01`): `exempt-tree` `implementation\MVP` (frozen, 1 file), `implementation\Archive_PreMVP`
(frozen, 63), `Documentation` (legacy, 31 + `adr\` 7), `.docpipeline` (generated, 5), `app` (generated, 18 `*.md`); `exempt-name`
`PRODUCT.md`, `DESIGN.md`. Catalogued (§1.7): `GUI\` product documentation (30 screen contracts, derived requirements, templates,
routing), `…\SV1\validation\` (now 5 `.md`), the package schema files and `hygiene\`. New since the census: §1b.

**`M-2` does:** two `git mv` (the two free `GUI\` candidates into the package roots), the three roots' mapping tables (two
move rows, the `PYAPP_V1_PROPOSAL.md` held row, the `improvements.md` held row with its target), a decision entry; nothing
in `Documentation\`.

## 5. PlantLibrary_Server — 5 candidates, 4 holds

Roots: `…\SV1\planning`, `…\SV1\proposal`, `…\SV1\handovers`. Record `D-2026-09-16-01`.

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `docs\SV-B07_dashboard_endpoint_coverage_report.md` | `H` | `…\SV1\planning\AUDIT_sv-b07-dashboard-endpoint-coverage_2026-07-05.md` | AUDIT · 2026-07-05 | code · `app\api\routes\dashboard_support.py:2`, `app\workers\tasks.py:9` (module docstrings); also `implementation\MVP\package\STATE.md:49,182` (state, frozen) | released only by a code edit in a batch (A.0.5); proposal 6 does not cover the code citers |
| `docs\SV-B07_runtime_verification_report.md` | `H` → **proposal 6** releases → `MV+R` at `M-3` | `…\SV1\planning\EVIDENCE_sv-b07-runtime-verification_2026-07-05.md` | EVIDENCE · 2026-07-05 † (header 2026-07-04) | terminal-`STATE.md` · `implementation\MVP\package\STATE.md:181` (state, frozen package) | |
| `docs\SV-B08_deployment_hardening_report.md` | `H` → **proposal 6** releases → `MV+R` at `M-3` | `…\SV1\planning\EVIDENCE_sv-b08-deployment-hardening_2026-07-05.md` | EVIDENCE · 2026-07-05 | terminal-`STATE.md` · `implementation\MVP\package\STATE.md:183` (state, frozen package) | cites `SV-B07_runtime_verification_report.md` itself (line 107) — swept in the same step |
| `docs\SV-CONTRACT-01_contract_validation_report.md` | `MV+R` | `…\SV1\planning\AUDIT_sv-contract-01-contract-validation_2026-07-04.md` | AUDIT · 2026-07-04 | — (citers: frozen MVP `TASK_CONTEXT.md:190`, SharedContracts' frozen MVP anchors, `openapi\README.md:12` — terminal anchors or sweep-editable) | row id kept in the topic (Q4b) |
| `…\SV1\proposal\SERVER_V1_PROPOSAL.md` | `H` | `PROPOSAL_server-v1_2026-07-10.md` (same root) | PROPOSAL · 2026-07-10 † (header 2026-07-09) | live-package (Q5c) · `…\SV1\STATE.md:15` (state) | released by onboarding `2a`/`2b` for Server, then `M-9` |

Never-renamed rows: `exempt-tree` `implementation\MVP` (frozen, 10); `exempt-name` `docs\local_android_test_environment.md`
(GUIDE-shaped live runbook, Q6; cited by code in Server and AndroidApp). Catalogued: `docs\` (10 living notes + README),
`…\SV1\validation\`, `openapi\`, `app\`, `deploy\`, `tests\` READMEs.

**`M-3` does:** one `git mv` (SV-CONTRACT-01) — three if proposal 6 is accepted (the two `EVIDENCE` write-ups too); the
mapping tables (the moves; the `SERVER_V1_PROPOSAL.md` and `SV-B07_dashboard…` held rows; if proposal 6 is declined, two more
held rows); the sweep over `docs\README.md`, `openapi\README.md` and `SV-B08`'s own line 107; a decision entry.

## 6. PlantLibrary_SharedContracts — 1 candidate, 1 hold

Roots: `…\SV1\planning`, `…\SV1\proposal`, `…\SV1\handovers`. Record `D-2026-09-16-01`.

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `…\SV1\proposal\SHAREDCONTRACTS_V1_PROPOSAL.md` | `H` | `PROPOSAL_sharedcontracts-v1_2026-07-10.md` (same root) | PROPOSAL · 2026-07-10 † (header 2026-07-09) | live-package (Q5c) · `…\SV1\STATE.md:11` (state) | released by onboarding `2a`/`2b` for SharedContracts, then `M-9` |

Never-renamed rows: `exempt-tree` `implementation\MVP` (frozen, 9), `generated` (generated, 134); `exempt-name`
`CONTRACT_VERSION.md`, `generated\CLIENT_MANIFEST.md` (version pins by file name, cited from five repositories and the skills),
`openapi\changelog.md`. Catalogued: `api-examples\`, `design-tokens\`, `openapi\`, `page-contracts\`, `schemas\`, `scripts\`,
`sync-contracts\`, `tests\contract_validation\`, `…\SV1\validation\`.

**`M-4` does:** no `git mv`; the three mapping tables (one held row); a decision entry recording that.

## 7. PlantLibrary_Dashboard — 5 candidates, 5 holds

Roots: `…\SV1\planning`, `…\SV1\proposal`, `…\SV1\handovers`. Record `D-2026-09-16-01`.

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `docs\WD-A11Y-01_validation_report.md` | `H` → **proposal 6** releases → `MV+R` at `M-5` | `…\SV1\planning\EVIDENCE_wd-a11y-01-accessibility-validation_2026-07-05.md` | EVIDENCE · 2026-07-05 | terminal-`STATE.md` · `implementation\MVP\package\STATE.md:172` (state, frozen package) | |
| `docs\WD-MOCKUP-UPGRADE_PROPOSAL.md` | `H` | `…\SV1\proposal\PROPOSAL_wd-mockup-driven-dashboard-upgrade_2026-07-07.md` (`MC-1`; `planning\` if literal) | PROPOSAL · 2026-07-07 | pinned · `PlantLibrary_Workspace\methodology\Design_Template_Initiative\METHODOLOGY_RECONCILIATION.md:24` (pinned tree); also MVP `STATE.md:403` (state, frozen) | released by the Design initiative's owner or a re-pin, not this track; proposal 6 does not cover the pinned citer |
| `docs\WD-PARITY-01_parity_report.md` | `H` → **proposal 6** releases → `MV+R` at `M-5` | `…\SV1\planning\AUDIT_wd-parity-01-page-contract-parity_2026-07-05.md` | AUDIT · 2026-07-05 | terminal-`STATE.md` · `implementation\MVP\package\STATE.md:172` (state, frozen package) | |
| `docs\WD-UX-10_mockup_parity_report.md` | `H` | `…\SV1\planning\AUDIT_wd-ux-10-mockup-parity_2026-07-07.md` | AUDIT · 2026-07-07 | pinned · `…\METHODOLOGY_RECONCILIATION.md:24` (pinned tree); also MVP `STATE.md:75` (state, frozen) | as above |
| `…\SV1\proposal\DASHBOARD_V1_PROPOSAL.md` | `H` | `PROPOSAL_dashboard-v1_2026-07-10.md` (same root) | PROPOSAL · 2026-07-10 † (header 2026-07-09) | live-package (Q5c) · `…\SV1\STATE.md:14` (state) | released by onboarding `2a`/`2b` for Dashboard, then `M-9` |

Never-renamed rows: `exempt-tree` `implementation\MVP` (frozen, 9), `references\PlantLibrary_pythonApp_old` (frozen, 42 —
its `screen_requirements\improvements.md` shares PyApp's held basename and is never renamed). Catalogued: `docs\` (three
living notes + README), `…\SV1\validation\`, `src\`, `src\api\`, `tests\` READMEs.

**`M-5` does:** no `git mv` unless proposal 6 is accepted (then two); the mapping tables (five held rows, or three held and
two moved); a decision entry.

## 8. PlantLibrary_AndroidApp — 2 candidates, 1 census hold + 1 policy hold

Roots: `…\SV1\planning`, `…\SV1\proposal`, `…\SV1\handovers`. Record `D-2026-09-16-01`.

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `docs\security_token_storage_acceptance.md` | `H` | `…\SV1\proposal\PROPOSAL_an-mvp-security-01-auth-token-storage-deviation_2026-07-06.md` (`MC-1`; `planning\` if literal); index status "accepted as-is (MVP)" | PROPOSAL (Q6 for DECISION) · 2026-07-06 | code · `core\auth\src\main\java\com\plantlibrary\android\core\auth\AuthTokenStore.kt:27` (code); also `…\SV1\TASK_CHECKLIST.md:56`, `TASK_CONTEXT.md:350` (live anchors), MVP `STATE.md:371` (state, frozen) | released by a code edit in a batch together with the live anchors, not this track; row id `AN-MVP-SECURITY-01` kept in the topic (Q4b) |
| `…\SV1\proposal\ANDROIDAPP_V1_PROPOSAL.md` | `H` (policy) | `PROPOSAL_androidapp-v1_2026-07-10.md` (same root) | PROPOSAL · 2026-07-10 † (header 2026-07-09) | live-package (Q5c) · no citer (policy hold, runbook §1e finding 5) | released with the other ten live-package holds by onboarding `2a`/`2b`, then `M-9` |

Never-renamed rows: `exempt-tree` `implementation\MVP` (frozen, 22). Catalogued: `docs\` (README, nine row-anchored plans,
the emulator-config note), `…\SV1\validation\`, the module READMEs; the four skill/agent mirrors are the onboarding track's.

**`M-6` does:** no `git mv`; the three mapping tables (two held rows); a decision entry.

## 9. PlantLibrary_Workspace — 53 candidates, 15 holds

Roots today: the six of `…\SV1\` and `…\SDA\`. **Proposal 5** has `M-7` declare `docs\`, `docs\proposals\`, `prompts\` and
`implementation\Server_VM_Setup\` as `general` roots by a decision entry (pin re-written with `--force`) before its first
`git mv`; `MVP_Reconciliation\` is not declared — it becomes a set folder under `docs\` on release (proposal 4). Record
`D-2026-09-16-01`.

### 9a. `MVP_Reconciliation\` — one snapshot, numbered 00–06 (+ README) → **proposal 4**

Set folder on release: `docs\SNAPSHOT_mvp-reconciliation_2026-07-10\` (git-created 2026-07-10; every header says "frozen
2026-07-09" — one divergence for the folder, seven in §11). Members keep their names. Three members are live-package holds
whose citers name the folder path, so the folder move waits for those three to release (`M-9`); until then the folder is
catalogued outside every root.

| old name | disp. | member name (unchanged) | TYPE · date | group · citer (class) |
|---|---|---|---|---|
| `MVP_Reconciliation\00_SOURCE_INVENTORY.md` | `S` member | unchanged | REGISTER · 2026-07-10 † | — |
| `MVP_Reconciliation\01_CURRENT_SYSTEM_BASELINE.md` | `S` member | unchanged | SNAPSHOT · 2026-07-10 † | — |
| `MVP_Reconciliation\02_GAPS_AND_DEFERRED_REGISTER.md` | `S` member, `H` | unchanged | REGISTER · 2026-07-10 † | live-package (Q5c) · `PlantLibrary_AndroidApp\…\SV1\BATCH_PLAN.md:35`, `…\SV1\BATCH_PLAN.md:23` here (live anchors) |
| `MVP_Reconciliation\03_SUBSYSTEM_RECONCILIATION.md` | `S` member | unchanged | FINDING · 2026-07-10 † | — |
| `MVP_Reconciliation\04_MVP_TO_V1_PROPOSAL.md` | `S` member, `H` | unchanged | PROPOSAL · 2026-07-10 † | live-package (Q5c) · `PlantLibrary_PyApp\…\SV1\TASK_CONTEXT.md:22` (live anchor) |
| `MVP_Reconciliation\05_NEXT_STEPS_AND_USAGE.md` | `S` member, `H` | unchanged | PLAN · 2026-07-10 † | live-package (Q5c) · `PlantLibrary_Dashboard\…\SV1\BATCH_PLAN.md:12` (live anchor) |
| `MVP_Reconciliation\06_V1_KICKOFF_PROMPT.md` | `S` member | unchanged | PROMPT · 2026-07-10 † | — (cited by nothing) |
| `MVP_Reconciliation\README.md` | `S` member | unchanged | (exempt by construction) | — |

If proposal 4 is declined, the per-file targets are the census's (`REGISTER_mvp-source-inventory_2026-07-10.md`, …,
`PROMPT_v1-kickoff_2026-07-10.md`) inside `docs\`, with the three held ones waiting.

### 9b. `docs\` — four free files, three chapter sets, one exempt how-to, two non-`.md` items

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `docs\fable5_business_proposal_prompt.md` | `R` | `docs\PROMPT_fable5-business-gtm-proposal_2026-07-11.md` | PROMPT · 2026-07-11 | — (cited by nothing) | proof scan: 0 lines (§1d) |
| `docs\fable5_system_strategy_proposal_prompt.md` | `R` | `docs\PROMPT_fable5-system-strategy-proposal_2026-07-11.md` | PROMPT · 2026-07-11 | — (cited by nothing) | proof scan: 0 lines |
| `docs\garden-app-product-research.md` | `R` | `docs\EVIDENCE_garden-apps-4-products_2026-07-11.md` | EVIDENCE (Q6 for REPORT) · 2026-07-11 | — | |
| `docs\garden-app-product-research_2.md` | `R` | `docs\EVIDENCE_garden-apps-13-products_2026-07-11.md` | EVIDENCE (Q6 for REPORT) · 2026-07-11 | — | `_2` was a version suffix; the topic carries the product count instead |
| `docs\fable5_business_proposal\` (00–10, 11 files) | `S` | `docs\PROPOSAL_fable5-business-gtm_2026-07-11\` — members `00_EXECUTIVE_SUMMARY.md` … `10_ASSUMPTIONS_AND_OPEN_QUESTIONS.md` unchanged | PROPOSAL · 2026-07-11 | — (chapter `00` is cited by a terminal anchor and frozen files — mapping-covered) | one index line for the set |
| `docs\fable5_strategy_proposal\` (00–06, 7 files) | `S` | `docs\PROPOSAL_fable5-product-strategy-v1_2026-07-11\` — members unchanged | PROPOSAL · 2026-07-11 | — | |
| `docs\fable5_strategy_proposal_v2\` (00, 07, 08, 09 + README, 5 files) | `S` | `docs\PROPOSAL_fable5-product-strategy-v2_2026-07-11\` — members unchanged | PROPOSAL · 2026-07-11 | — | the v2 reconciliation layer over v1; its README stays a member |
| `docs\local_development.md` | `X` | never renamed (`exempt-name`, product how-to) | — | — | |
| `docs\Fable5_Prompt_Improvements` (no extension), `docs\PlantLibrary_System_Artefact\` (HTML export) | `K` | left in place | — | — | outside the `.md` rule; the census counts them as `other` / `subfolder` once `docs\` is a root |

### 9c. `docs\proposals\` — two free proposals, one held, one track set

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `docs\proposals\ENRICHMENT_V2_PROPOSAL.md` | `R` | `docs\proposals\PROPOSAL_enrichment-v2_2026-07-10.md` | PROPOSAL · 2026-07-10 | — | |
| `docs\proposals\GARDEN_DESIGNER_PROPOSAL.md` | `R` | `docs\proposals\PROPOSAL_garden-designer_2026-07-10.md` | PROPOSAL · 2026-07-10 | — | |
| `docs\proposals\PlantLibrary_Full_Implementation_Update.md` | `H` | `docs\proposals\PROPOSAL_full-implementation-package_2026-07-16.md` | PROPOSAL · 2026-07-16 | code · `docs\proposals\Repo_Restructure_MVP_V1_Split\manifests\MANIFEST_complete.csv:2` (config) | released by a code edit, not this track; the manifest moves with its set folder, unedited |
| `docs\proposals\Repo_Restructure_MVP_V1_Split\` (`EXECUTION_PROMPTS.md`, `FOLLOWUP_CLOSURE_PROMPT.md`, `PROPOSAL.md`, `VERIFICATION_REPORT.md`, `manifests\`) | `S` | `docs\proposals\PROPOSAL_repo-restructure-mvp-v1-split_2026-07-15\` — members unchanged, `manifests\*.csv` and the generated `REVIEW_LIST.md` unchanged | PROPOSAL · 2026-07-15 (earliest member; 07-16 for two members) | — | the executed restructure track as one set; the set-folder form keeps `FOLLOWUP_CLOSURE_PROMPT.md:69` outside the proof scan (§1d) |

### 9d. `implementation\Server_VM_Setup\` — one prompt, one exempt runbook

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `implementation\Server_VM_Setup\DockerDesktop_Audit_Migration_Prompt.md` | `R` | `implementation\Server_VM_Setup\PROMPT_docker-desktop-audit-migration_2026-07-10.md` | PROMPT · 2026-07-10 † (header 2026-07-09) | — | proof scan: 0 lines |
| `implementation\Server_VM_Setup\ServerSetUp_MVP.md` | `X` | never renamed (`exempt-name`, GUIDE-shaped, Q6) | — · 2026-07-10 † | — | |

### 9e. `implementation\System_Design_Architecture\` — the package-root proposal and the numbered set 00–04 → **proposal 3**

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `…\SDA\MODEL_RECOMMENDATION.md` | `H` | `…\SDA\proposal\PROPOSAL_sda-model-allocation_2026-07-09.md` | PROPOSAL · 2026-07-09 † (header 2026-07-08) | code · `docs\proposals\Repo_Restructure_MVP_V1_Split\manifests\MANIFEST_Workspace.csv:3` (config); also `…\Design_Template_Initiative\DRIVER.md:7`, `INITIATIVE_PROPOSAL.md:97`, `KICKOFF_PROMPT.md:49`, `evidence\00_inventory_reverification.md:39` (pinned tree) | outside every root today; released by a code edit, and the pinned citers stand |
| `…\SDA\proposal\00_DESIGN_GOVERNANCE_PROPOSAL.md` | `S` member (on release), `H` | set folder `…\SDA\proposal\PROPOSAL_system-design-architecture_2026-07-09\`, member unchanged; per-file alternative `PROPOSAL_design-governance_2026-07-09.md` | PROPOSAL · 2026-07-09 | pinned · `INITIATIVE_PROPOSAL.md:80`, `KICKOFF_PROMPT.md:43`, `PROMPTS\02_AUTHOR_TEMPLATE_SPEC_AND_CORE.md:18`, `evidence\00_inventory_reverification.md:22` (pinned tree); `Design_Template_Kit\template\TEMPLATE_SPEC.md:39,518` (external kit) | |
| `…\SDA\proposal\01_DESIGN_ARTIFACT_TEMPLATES.md` | `S` member (on release), `H` | as above; per-file alternative `PROPOSAL_design-artifact-templates_2026-07-09.md` | PROPOSAL · 2026-07-09 | pinned · `INITIATIVE_PROPOSAL.md:81`, `KICKOFF_PROMPT.md:43`, `PROMPTS\02:18`, `evidence\00:23` | |
| `…\SDA\proposal\02_CONFORMANCE_AND_ENFORCEMENT.md` | `S` member (on release), `H` | as above; per-file alternative `PROPOSAL_design-conformance-enforcement_2026-07-09.md` | PROPOSAL · 2026-07-09 | pinned · `INITIATIVE_PROPOSAL.md:82`, `KICKOFF_PROMPT.md:43`, `PROMPTS\02:18`, `PROMPTS\10_ANCHORING_KIT_ENFORCEMENT_AND_INSTALLER.md:16`, `evidence\00:24`; `Design_Template_Kit\template\TEMPLATE_SPEC.md:519` (external kit) | |
| `…\SDA\proposal\03_CLAUDE_MD_AND_DOC_LAYERING.md` | `S` member (on release), `H` | as above; per-file alternative `PROPOSAL_claude-md-doc-layering_2026-07-09.md` | PROPOSAL · 2026-07-09 | pinned · `INITIATIVE_PROPOSAL.md:83`, `KICKOFF_PROMPT.md:43`, `PROMPTS\02:18`, `PROMPTS\10:16`, `evidence\00:25` | |
| `…\SDA\proposal\04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `S` member (on release), `H` | as above; per-file alternative `PROPOSAL_approved-design-revision_2026-07-10.md`, status "approved" in the index line | PROPOSAL (Q6 for DECISION) · 2026-07-10 | code · `PlantLibrary_SharedContracts\design-tokens\semantic-roles.json:3` (code); `Design_Template_Kit` `tools\import-flat-tokens.mjs:456,466,468`, `tools\lib\color-extra.mjs:6`, `examples\…\banned-colors.json:16,25,32` (external kit, code); also `…\SDA\STATE.md:45,65`, the `…\SV1` anchors and `STATE.md` of PyApp (:169/:102/:162), Dashboard (:97/:51/:130), AndroidApp (:187/:121/:262), the pinned initiative (5 lines), the Design kit's example `CONFIGURATION.md:33`, `DECISION_RECORD_2026-07-10.md:16,25` | the most-cited name in the corpus; a name cited from two groups belongs to the later one — code |

The whole set is held (four pinned, one code); under proposal 3 the subfolder is created only when every member's hold has
released — for this set, by owners outside this track, so in practice the set stays as it is, listed held in
`…\SDA\proposal\INDEX.md` with the subfolder as its target.

### 9f. `implementation\System_V1_Implementation\proposal\` — the numbered set 00–02 → **proposal 3**

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `…\SV1\proposal\00_V1_SYSTEM_PROPOSAL.md` | `S` member (on release), `H` | set folder `…\SV1\proposal\PROPOSAL_v1-system_2026-07-10\`, member unchanged; per-file alternative `PROPOSAL_v1-system_2026-07-10.md` | PROPOSAL · 2026-07-10 † (header 2026-07-09) | live-package (Q5c) · `…\SV1\STATE.md:12`, `BATCH_PLAN.md:22`, `TASK_CONTEXT.md:34` here; PyApp `STATE.md:12`, Server `BATCH_PLAN.md:110`/`STATE.md:16`, SharedContracts `STATE.md:12`, Dashboard `STATE.md:15` (each `…\SV1\`) | released when onboarding `2a`/`2b` has migrated **every** citing package (five suites and Workspace), then `M-9` |
| `…\SV1\proposal\01_PRODUCT_VALUE_AUDIT.md` | `S` member (on release), `H` | as above; per-file alternative `AUDIT_product-value_2026-07-10.md` (would route to `planning\`) | AUDIT · 2026-07-10 | live-package (Q5c) · `…\SV1\STATE.md:14,83`, `TASK_CHECKLIST.md:25` | |
| `…\SV1\proposal\02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `S` member (on release), `H` | as above; per-file alternative `PROPOSAL_validation-methodology_2026-07-10.md`, status "approved" | PROPOSAL (Q6 for DECISION) · 2026-07-10 | live-package (Q5c) · `…\SV1\BATCH_PLAN.md:133`, `STATE.md:118`, `TASK_CHECKLIST.md:37`, `TASK_CONTEXT.md:184` here, and the `…\SV1` `BATCH_PLAN.md`/`STATE.md` of PyApp (:35/:136), Server (:165/:130), SharedContracts (:85/:80), Dashboard (:157/:83), AndroidApp (:248/:153) | as above — every citing package |

### 9g. `prompts\` — one held handoff, one misfiled prompt, four exempt templates

| old name | disp. | new name / target on release | TYPE · date | group · citer (class) | note |
|---|---|---|---|---|---|
| `prompts\PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | `H` | `…\SV1\handovers\HANDOVER_process-improvements_2026-07-10.md` (`MC-2`; `prompts\HANDOVER_…` if it stays in its general root) | HANDOVER · 2026-07-10 | terminal-`STATE.md` · `implementation\System_Tooling\STATE.md:6,13` (state, frozen package); **and** live anchors: PyApp `…\SV1\BATCH_PLAN.md:137`/`STATE.md:130`, Dashboard `BATCH_PLAN.md:122`/`STATE.md:77`, AndroidApp `BATCH_PLAN.md:213`/`STATE.md:147` | proposal 6 covers the frozen citer; the three live citers release with onboarding `2a`/`2b` — so `M-9`, not `M-7`; HANDOFF is a HANDOVER synonym |
| `prompts\reference\SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | `H` | `prompts\PROMPT_setup-android-test-environment_2026-07-16.md` (out of the template folder) | PROMPT · 2026-07-16 † (header 2026-07-06 — the ten-day divergence) | code · `docs\proposals\Repo_Restructure_MVP_V1_Split\manifests\MANIFEST_complete.csv:3` (config); also `PlantLibrary_AndroidApp\implementation\MVP\package\STATE.md:457` (state, frozen) | released by a code edit, not this track; proof scan: 0 lines |
| `prompts\reference\BATCH_PLAN_V3.md`, `DRIVER_SCRIPT_V3.md`, `TASK_CHECKLIST_V3.md`, `TASK_CONTEXT_V3.md` | `X` | never renamed (`exempt-name`, V3 template reference copies) | — | — | `prompts\reference\` is an undeclared subfolder of the `prompts\` root — ignored by the file rule |

### 9h. Never-renamed rows from the record (`D-2026-09-16-01`)

`exempt-tree` frozen: `implementation\System_Integration_MVP` (36), `implementation\System_Tooling` (14), `strategy\Cross_Platform_Strategy`
(17), `system_description` (138); pinned: `methodology\GUI_Improvement_Methodology` (62 — `VERSION.md` 4.0.0, the 28 `*_TEMPLATE.md`,
`PROMPTS\`, `SKILL_SPECS\`, pinned by absolute path, version and per-file name from `Design_Template_Kit\METHODOLOGY_SOURCE.md`),
`methodology\Design_Template_Initiative` (45 — the Design kit's live initiative); generated: `docs\proposals\Repo_Restructure_MVP_V1_Split\manifests\REVIEW_LIST.md`.
`exempt-name`: `WORKSPACE_STATE.md`, `REPOSITORY_MAP.md`, `methodology\VALIDATION_METHODOLOGY.md`, `docs\local_development.md`,
`implementation\Server_VM_Setup\ServerSetUp_MVP.md`, `…\SV1\SKILLS.md`, `…\SV1\SUITE_HANDOFFS.md`, `…\SV1\V1_IMPLEMENTATION_SEQUENCE.md`,
the four `prompts\reference\*_V3.md`. Catalogued: every `README.md`, `…\SV1\validation\`, the package schema files, `hygiene\`, the
`.claude`/`.codex` mirrors.

**`M-7` does, in order:** (0) the decision entry declaring the four general roots and the pin re-written with `--force`, four
`INDEX.md` seeded; (1) four folder renames (`S`: the three `fable5_*` sets, `Repo_Restructure_MVP_V1_Split`); (2) seven file
renames (`R`: four in `docs\`, two in `docs\proposals\`, one in `Server_VM_Setup\`); (3) the sweep over the roots' files,
READMEs and product docs; (4) the mapping tables — four new roots and the two `proposal\` roots — carrying every held row
with group and target (15 names) and the exempt rows; (5) a decision entry. Nothing in `MVP_Reconciliation\`, the two
`proposal\` sets, `prompts\reference\`, or any frozen or pinned tree moves.

## 10. Holds summary — 35 held names by repository and group

| repo | onboarding runbook (4) | live package `STATE.md`/anchor (10 + 1 policy) | terminal `STATE.md` only (5) | pinned tree / Design kit (8) | code or config (7) |
|---|---|---|---|---|---|
| SW_Development | `HANDOVER_batch-package-schema-drift_2026-09-15.md` (move only), `IMPLEMENTATION_PLAN.md` (proposal 1), `onboarding\AUDIT_skill-assumptions_2026-09-15.md`, `onboarding\REGISTER_package-census_2026-09-15.md` | — | — | — | — |
| PlantLibrary_PyApp | — | `…\SV1\proposal\PYAPP_V1_PROPOSAL.md` | — | `Documentation\Design_Implementation_Claude.md` (moot: legacy corpus), `GUI\screen_structures\improvements.md` | `Documentation\plant_information_system_implementation_plan_v1.md` (moot: legacy corpus) |
| PlantLibrary_Server | — | `…\SV1\proposal\SERVER_V1_PROPOSAL.md` | `docs\SV-B07_runtime_verification_report.md`, `docs\SV-B08_deployment_hardening_report.md` | — | `docs\SV-B07_dashboard_endpoint_coverage_report.md` |
| PlantLibrary_SharedContracts | — | `…\SV1\proposal\SHAREDCONTRACTS_V1_PROPOSAL.md` | — | — | — |
| PlantLibrary_Dashboard | — | `…\SV1\proposal\DASHBOARD_V1_PROPOSAL.md` | `docs\WD-A11Y-01_validation_report.md`, `docs\WD-PARITY-01_parity_report.md` | `docs\WD-MOCKUP-UPGRADE_PROPOSAL.md`, `docs\WD-UX-10_mockup_parity_report.md` | — |
| PlantLibrary_AndroidApp | — | `…\SV1\proposal\ANDROIDAPP_V1_PROPOSAL.md` (policy, no citer) | — | — | `docs\security_token_storage_acceptance.md` |
| PlantLibrary_Workspace | — | `…\SV1\proposal\00_V1_SYSTEM_PROPOSAL.md`, `01_PRODUCT_VALUE_AUDIT.md`, `02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md`; `MVP_Reconciliation\02_GAPS_AND_DEFERRED_REGISTER.md`, `04_MVP_TO_V1_PROPOSAL.md`, `05_NEXT_STEPS_AND_USAGE.md` | `prompts\PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` (also live-cited; releases at `M-9`) | `…\SDA\proposal\00_DESIGN_GOVERNANCE_PROPOSAL.md`, `01_DESIGN_ARTIFACT_TEMPLATES.md`, `02_CONFORMANCE_AND_ENFORCEMENT.md`, `03_CLAUDE_MD_AND_DOC_LAYERING.md` | `…\SDA\proposal\04_APPROVED_DESIGN_REVISION_2026-07-10.md`, `…\SDA\MODEL_RECOMMENDATION.md`, `docs\proposals\PlantLibrary_Full_Implementation_Update.md`, `prompts\reference\SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` |
| **what releases it** | the onboarding track retiring or editing its runbook (three of the four are compliant already) | onboarding `2a`/`2b` migrating the citing package(s), then `M-9` | **proposal 6** (the mapping table serves a frozen `STATE.md`) — at `M-3`, `M-5`; `M-9` for the Workspace one | the Design initiative's owner or a Design-kit re-pin — not this track | a code edit in a batch (A.0.5) — not this track |

Both pinned methodology trees (`GUI_Improvement_Methodology`, `Design_Template_Initiative`) are never-renamed rows (§9h), not holds:
nothing in them is a candidate. Every live citation in the corpus is a hold above; none is mapped as a plain rename.

## 11. Date divergences — 28 candidates (git-created wins, Q5a)

| repo | file | git-created | header | days |
|---|---|---|---|---|
| SW_Development | `IMPLEMENTATION_PLAN.md` | 2026-08-05 | 2026-08-04 | 1 |
| PlantLibrary_PyApp | `Documentation\Cross_Platform_Architecture_Proposal.md` | 2026-06-21 | 2026-06-20 | 1 |
| PlantLibrary_PyApp | `Documentation\Cross_Platform_Baseline_Audit.md` | 2026-06-21 | 2026-06-20 | 1 |
| PlantLibrary_PyApp | `Documentation\Cross_Platform_Implementation_Plan.md` | 2026-06-21 | 2026-06-20 | 1 |
| PlantLibrary_PyApp | `Documentation\Current_State_Assessment.md` | 2026-06-21 | 2026-06-20 | 1 |
| PlantLibrary_PyApp | `Documentation\DECISIONS_NEEDED.md` | 2026-06-21 | 2026-06-20 | 1 |
| PlantLibrary_PyApp | `Documentation\IMPLEMENTATION_CHECKLIST.md` | 2026-06-21 | 2026-06-20 | 1 |
| PlantLibrary_PyApp | `Documentation\Target_Architecture_Recommendation.md` | 2026-06-21 | 2026-06-20 | 1 |
| PlantLibrary_PyApp | `Documentation\legacy-data-inventory.md` | 2026-06-22 | 2026-06-21 | 1 |
| PlantLibrary_PyApp | `Documentation\spike-results.md` | 2026-06-22 | 2026-06-21 | 1 |
| PlantLibrary_PyApp | `…\SV1\proposal\PYAPP_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-09 | 1 |
| PlantLibrary_Server | `docs\SV-B07_runtime_verification_report.md` | 2026-07-05 | 2026-07-04 | 1 |
| PlantLibrary_Server | `…\SV1\proposal\SERVER_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-09 | 1 |
| PlantLibrary_SharedContracts | `…\SV1\proposal\SHAREDCONTRACTS_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-09 | 1 |
| PlantLibrary_Dashboard | `…\SV1\proposal\DASHBOARD_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-09 | 1 |
| PlantLibrary_AndroidApp | `…\SV1\proposal\ANDROIDAPP_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-09 | 1 |
| PlantLibrary_Workspace | `MVP_Reconciliation\00` … `06` (seven members; the set folder's own date) | 2026-07-10 | 2026-07-09 | 1 |
| PlantLibrary_Workspace | `implementation\Server_VM_Setup\DockerDesktop_Audit_Migration_Prompt.md` | 2026-07-10 | 2026-07-09 | 1 |
| PlantLibrary_Workspace | `implementation\Server_VM_Setup\ServerSetUp_MVP.md` (exempt) | 2026-07-10 | 2026-07-09 | 1 |
| PlantLibrary_Workspace | `…\SDA\MODEL_RECOMMENDATION.md` | 2026-07-09 | 2026-07-08 | 1 |
| PlantLibrary_Workspace | `…\SV1\proposal\00_V1_SYSTEM_PROPOSAL.md` | 2026-07-10 | 2026-07-09 | 1 |
| PlantLibrary_Workspace | `prompts\reference\SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | 2026-07-16 | 2026-07-06 | 10 |

The ten PyApp rows and the exempt Workspace runbook are "never renamed" today; the divergence is recorded so a lifted
exemption does not re-derive it. Every mapping-table row of a renamed or held file with a divergence carries it in the
`(date divergence: …)` form of `KIT_SPEC.md` §3.

## 12. What `GM` decides — six proposals and two map calls, each with a recommendation

**Proposal 1 — `IMPLEMENTATION_PLAN.md` at the superproject root.** Options: (a) exempt by decision as the living program
plan ("How to continue implementation", written 2026-08-04, updated in place), entered in the root allowlist (it already is)
and listed as a never-renamed row; (b) hold with target `PLAN_plantlibrary-continuation_2026-08-05.md` until the onboarding
runbook, which cites it on ten lines, retires. **Recommend (a).** It is a "how to continue" document, not a dated
deliverable; the onboarding runbook cites it as the program's plan, and every frozen MVP package carries a file of the same
basename, so a rename would leave the corpus with the same name meaning two things. `M-1` writes the `exempt-name` line.

**Proposal 2 — the three PyApp `GUI\` candidates.** Options: (a) the `docs\` treatment — `git mv` into the package's roots,
`FUTURE_GUI_DEVELOPMENT_PROPOSAL.md` and `Source_GUI_Integration_Report.md` now, `screen_structures\improvements.md` held
(pinned group) with its target; (b) catalogue `GUI\` whole as product documentation and leave the three names. **Recommend
(a).** Two of the three are cited only by `GUI\` index files this track may sweep; the third is held either way.

**Proposal 3 — the two numbered sets inside live `proposal\` roots** (Workspace `…\SV1\proposal\` 00–02, `…\SDA\proposal\`
00–04). Options: (a) on release, a dated set subfolder inside `proposal\` (`PROPOSAL_v1-system_2026-07-10\`,
`PROPOSAL_system-design-architecture_2026-07-09\`), members unchanged, so the root keeps its name and the reading order
survives; (b) per-file renames on release (the census names, §9e/§9f), which scatter chapter `01_PRODUCT_VALUE_AUDIT.md` into
`planning\` by type. **Recommend (a).** Until release both sets stay as they are, listed held with the subfolder as their
target; the SDA set's citers are outside this track, so (a) changes nothing there in practice.

**Proposal 4 — `MVP_Reconciliation\`.** Options: (a) on release of its three live-package members, the whole folder becomes
the set folder `docs\SNAPSHOT_mvp-reconciliation_2026-07-10\` (every header calls it one frozen snapshot), members unchanged;
(b) declare `MVP_Reconciliation\` a root at `M-7` and rename its members per file. **Recommend (a).** (b) would leave three
held names in a root whose every other member is renamed, and the folder is one document.

**Proposal 5 — Workspace's loose roots.** `M-7` declares `docs\`, `docs\proposals\`, `prompts\` and `implementation\Server_VM_Setup\`
as `general` roots by a decision entry, pin re-written with `--force`, before its first `git mv`; `docs\fable5_*` (three) and
`docs\proposals\Repo_Restructure_MVP_V1_Split\` become dated set folders (§9b, §9c); `prompts\reference\` stays an undeclared
subfolder. **Recommend yes.** With floor 0 the three `PROMPT_` files that land in general roots are scanned and pass today
(§1d).

**Proposal 6 — the terminal-`STATE.md` hold group (five names).** A citation from a frozen package's `STATE.md`
(`implementation\MVP\package\STATE.md` in Server and Dashboard; `implementation\System_Tooling\STATE.md` in Workspace) is
served by the receiving root's mapping table, as Chapter 8's own rule served `STATE.md` citations in SOURCE — the frozen file
is never edited, and the old name resolves through the "Renamed" table. Accepting releases `SV-B07_runtime_verification_report.md`
and `SV-B08_deployment_hardening_report.md` at `M-3`, `WD-A11Y-01_validation_report.md` and `WD-PARITY-01_parity_report.md`
at `M-5`, and `PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` at `M-9` once its three live citers have migrated. It does **not**
release a name with a code or pinned citer (`SV-B07_dashboard_endpoint_coverage_report.md`, `WD-MOCKUP-UPGRADE_PROPOSAL.md`,
`WD-UX-10_mockup_parity_report.md`, `SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md`), and the live-package group stays held per
Q5c. **Recommend accept.** Declining keeps four names in `docs\` folders that are otherwise migrated and adds nothing the
mapping table does not already give a reader of the frozen file.

**Map call `MC-1` — where a moved `docs\`/`GUI\` candidate lands.** Q4b says "into their package's `planning\` root"; Q6
then typed three of them `PROPOSAL` and one `FINDING`, which the rule block routes to `proposal\` and `handovers\`. The map
routes by TYPE: `PROPOSAL` → `proposal\` (PyApp `FUTURE_GUI_DEVELOPMENT_PROPOSAL.md`; Dashboard `WD-MOCKUP-UPGRADE_PROPOSAL.md`
and AndroidApp `security_token_storage_acceptance.md` when released), `FINDING` → `handovers\` (PyApp `improvements.md` when
released), everything else → `planning\`. The checker enforces the pattern, never the routing, so either reading is green;
the map's reading is the one the rule block tells authors. Confirm, or say "planning\ literal" and every target in the
rows moves to `planning\`.

**Map call `MC-2` — the home of `PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` on release.** A HANDOVER routes to a
`handovers` root; the map targets `…\SV1\handovers\` (it is the handoff into the V1 packages that cite it). The alternative
is to stay in `prompts\`, a general root, as `prompts\HANDOVER_process-improvements_2026-07-10.md`. Confirm, or name the alternative.

## 13. Reconciliation — every candidate dispositioned once

| repo | census candidates | `C` | `MV` | `R` / `MV+R` | `H` (kept) | `H` → released by proposal 6 | `X` | `S` members | holds (register / +policy) |
|---|---|---|---|---|---|---|---|---|---|
| SW_Development | 6 | 4 | 1 | 0 | (2 name-holds on `C` rows, 1 on the `MV` row) | 0 | 1 (proposal 1) | 0 | 4 / 4 |
| PlantLibrary_PyApp | 31 | 0 | 0 | 2 | 2 (`improvements.md`, `PYAPP_V1_PROPOSAL.md`) | 0 | 27 (2 of them also held, moot) | 0 | 4 / 4 |
| PlantLibrary_Server | 5 | 0 | 0 | 1 | 2 (`SV-B07_dashboard…`, `SERVER_V1_PROPOSAL.md`) | 2 | 0 | 0 | 4 / 4 |
| PlantLibrary_SharedContracts | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 / 1 |
| PlantLibrary_Dashboard | 5 | 0 | 0 | 0 | 3 | 2 | 0 | 0 | 5 / 5 |
| PlantLibrary_AndroidApp | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 / 2 |
| PlantLibrary_Workspace | 53 | 0 | 0 | 7 | 4 (`MODEL_RECOMMENDATION.md`, `PlantLibrary_Full_Implementation_Update.md`, `SETUP_ANDROID…`, `PROCESS_IMPROVEMENTS_HANDOFF…`*) | (*1, at `M-9`) | 1 (`ServerSetUp_MVP.md`) | 41 (3 sets free = 26 members + `Repo_Restructure` 4; `MVP_Reconciliation` 7 with 3 held; SDA 5 held; V1 3 held) | 15 / 15 |
| **total** | **103** | 4 | 1 | 10 | 14 (+ the 11 held set members) | 4 (+1 at `M-9`) | 29 | 41 | **34 / 35** |

Check: 4 + 1 + 10 + 14 + 4 + 29 + 41 = 103. Holds: 4 + 4 + 4 + 1 + 5 + 1 + 15 = 34 census holds, 35 with the AndroidApp policy
hold — all 35 appear in §10 with group and target; none is a plain rename. Files: 967 in the register, 1024 today, the 57
new ones dispositioned in §1b (none a candidate). With every recommendation accepted, `M-1`…`M-7` perform 15 file moves or
renames (1 + 2 + 3 + 0 + 2 + 0 + 7) and 4 folder renames (26 member files), and leave 30 names held for `M-9` or for
owners outside this track (35 − 4 released by proposal 6 at `M-3`/`M-5` − 1 made moot by proposal 1).

## 14. Order of execution

`M-1` (superproject) → `M-2` PyApp → `M-3` Server → `M-4` SharedContracts → `M-5` Dashboard → `M-6` AndroidApp → `M-7`
Workspace, one session each, `M-2`…`M-7` in any order once `GM` is answered; each writes its roots' "Renamed 2026-09-16"
tables from this map's rows (old → new; held rows in the `**held** — cited by <citer>. Target on release: <name> (date
divergence: …)` form; exempt rows citing their entry), a decision entry quoting the `GM` words, and verifies per
`INSTALL.md`. `M-9` releases a held name only when a `git grep` at HEAD across the whole target shows no hold-class citer
of its old name or the operator records a release; the target-on-release column here is the only target.
