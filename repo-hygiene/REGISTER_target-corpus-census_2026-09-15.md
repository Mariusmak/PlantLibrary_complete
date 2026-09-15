# REGISTER — target corpus census (2026-09-15)

*Produced by the Repo Hygiene Template Kit bootstrap session (`PROMPT_kit-bootstrap-session_2026-09-15.md` §3, item (b)),*
*measured 2026-09-15 evening over `C:\Programmierung\SW_Development` at `6ecc155` (tree clean apart from the untracked*
*`repo-hygiene\` folder) and its six submodules, each clean on its own `main`. Read-only. Nothing renamed. This is the*
*pre-migration baseline that step M-8 of the track runbook diffs against; its totals are in §1, its rules in §7.*

**Method.** A scripted walk (Python 3.12, stdlib) over every `.md` file per repository, excluding `node_modules`, `.git`,
`.venv`, `build`, `.tmp`, the four runtime mirrors (`.claude`, `.codex`, `.agents`, `.github`), `__pycache__`, `.gradle`,
`.idea`, `dist`, `coverage`, `playwright-report`, `test-results`, `.pytest_cache`, `.ruff_cache`, `.mypy_cache`, `graphify-out`,
`.vite`. Folder classes come from an explicit rule table (§7) refined by six read-only Explore agents, one per submodule,
which opened representative files in every non-frozen folder and proposed a TYPE and topic for every candidate. For every
candidate: git-created date (`git log --follow --diff-filter=A`, oldest line), last-change date, the date in the document
header where the agent found one, and every citation of its basename across all seven repositories plus
`C:\Programmierung\Design_Template_Kit` (`git grep -F` per repo, basename bounded on the left so `PROPOSAL.md` does not match
inside `X_PROPOSAL.md`; for a basename that exists at more than one location the citation counts only when it sits in the
candidate's own repo or names that repo or the candidate's parent folder). **Hold rule** (the prompt's, plus
`DECISION_FILE_AND_DOCS_POLICY.md` A.0.5): a citation from a live batch package's anchor file (`BATCH_PLAN.md`,
`TASK_CHECKLIST.md`, `TASK_CONTEXT.md` of the seven live packages), from any `STATE.md`, from the onboarding runbook, from
a pinned tree, from the Design kit, or from a code/config file is a **hold**. Citations from frozen trees, terminal packages'
anchors, READMEs/indexes, other candidates and product docs are **sweep-editable or mapping-covered**, not holds.
One false negative of the collision rule was found by the fresh-context review of the runbook and corrected by hand:
`PlantLibrary_PyApp\GUI\screen_structures\improvements.md` is named four times by the pinned Design initiative in lines that call
its folder `screen_requirements/` (an earlier name), so neither the repo nor the parent folder appeared on the line; its hold is
restored in §2.2 and §3, and PyApp's holds are 4, the total 34.

**Counts against the pre-session measurement** (`PROMPT_kit-bootstrap-session_2026-09-15.md` §1b: AndroidApp 143 · Dashboard 75 ·
PyApp 284 · Server 48 · SharedContracts 187 · Workspace 405): AndroidApp 143 = 56 + 87 under the three skill mirrors
(`.claude`, `.agents`, `.github`, 29 each, byte-identical); PyApp 192 here (the 192 scratch files under `.tmp\audit-harness-probe`
are gone — the folder exists and is empty; the earlier figure did not exclude the mirrors and `.venv`); Server 47 (`.pytest_cache\README.md`
excluded here); SharedContracts 187 = 187; Dashboard 75 = 75; Workspace 399 (six under `.claude\`). Total censused: **967**.

---

## 1. Totals per repository — the M-8 baseline

| repo | HEAD | files | candidates | already compliant | to rename | **holds** | header-date divergences | frozen | package-schema (exempt) | product | generated | pinned | evidence | scratch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SW_Development (superproject) | `6ecc155` | 11 | 6 | 5 | 1 | **4** | 1 | 0 | 4 | 0 | 0 | 0 | 0 | 1 |
| PlantLibrary_PyApp | `5cefe62` | 192 | 31 | 0 | 31 | **4** | 10 | 64 | 8 | 80 | 5 | 0 | 4 | 0 |
| PlantLibrary_Server | `5c312d3` | 47 | 5 | 0 | 5 | **4** | 2 | 10 | 8 | 18 | 0 | 0 | 6 | 0 |
| PlantLibrary_SharedContracts | `75846a9` | 187 | 1 | 0 | 1 | **1** | 1 | 9 | 8 | 33 | 134 | 0 | 2 | 0 |
| PlantLibrary_Dashboard | `472e7d2` | 75 | 5 | 0 | 5 | **5** | 1 | 51 | 8 | 8 | 0 | 0 | 3 | 0 |
| PlantLibrary_AndroidApp | `b75265a` | 56 | 2 | 0 | 2 | **1** | 1 | 22 | 8 | 19 | 0 | 0 | 5 | 0 |
| PlantLibrary_Workspace | `5147569` | 399 | 53 | 0 | 53 | **15** | 12 | 205 | 16 | 13 | 1 | 107 | 4 | 0 |
| **total** | | **967** | **103** | **5** | **98** | **34** | **28** | **361** | **60** | **171** | **140** | **107** | **24** | **1** |

Reading the table: *candidates* are files the agents judged to be dated deliverables (a proposal, plan, audit, register,
evidence write-up, prompt, handover, finding or snapshot written on a date), wherever they sit; *to rename* is the subset
whose name does not already match `<TYPE>_<topic>_<YYYY-MM-DD>.md`; *holds* is the subset with at least one hold-class
citation (§3); *header-date divergences* counts candidates whose git-created date differs from the date in their own
header (all 28 are one day later, except one: the Android setup prompt, ten days later). Five candidates are already
compliant, all in the superproject (`onboarding\`, `repo-hygiene\`, the root `HANDOVER`). Eleven candidates are cited by
nothing at all.

---

## 2. Per repository — folders, classes, candidates

### 2.1 SW_Development (superproject) — `6ecc155`

| folder | .md | class | what is there |
|---|---|---|---|
| `.` | 5 | package-schema 2, dated deliverable 2, scratch 1 | `CLAUDE.md`/`AGENTS.md` instruction files (exempt by name); `HANDOVER_…_2026-09-15.md` compliant name, no `handovers\` home; `IMPLEMENTATION_PLAN.md` the 2026-08-04 program plan; `Todo.md` git-ignored personal notes |
| `onboarding` | 4 | dated deliverable 3, package-schema 1 | the onboarding track: `INDEX.md` + three compliant deliverables (step `0` and `1` done) |
| `repo-hygiene` | 2 | package-schema 1, dated deliverable 1 | this track; `PROMPT_kit-bootstrap-session_2026-09-15.md` untracked at census time |

**Candidates (6).** TYPE and topic are the census proposal (agent-read where marked, heuristic otherwise);
`?` marks a TYPE outside the enum (§6 of the runbook's gate, Q6). Dates: git = `git log --follow --diff-filter=A`;
header = the date the document states about itself; a differing pair is bolded.

| file | git-created | last change | header date | TYPE | topic | name today | citations | hold |
|---|---|---|---|---|---|---|---|---|
| `HANDOVER_batch-package-schema-drift_2026-09-15.md` | 2026-09-15 | 2026-09-15 | 2026-09-15 | HANDOVER | `batch-package-schema-drift` | compliant | onb-runbook 1, schema/index 1 | onboarding-runbook |
| `IMPLEMENTATION_PLAN.md` | 2026-08-05 | 2026-08-05 | **2026-08-04** | PLAN | `plantlibrary-continuation` | non-compliant | onb-runbook 8 | onboarding-runbook |
| `onboarding/AUDIT_skill-assumptions_2026-09-15.md` | 2026-09-15 | 2026-09-15 | — | AUDIT (h) | `skill-assumptions` | compliant | onb-runbook 1, schema/index 1 | onboarding-runbook |
| `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | 2026-09-15 | 2026-09-15 | — | PROMPTS (h) | `conductor-onboarding` | compliant | schema/index 1, candidate 1 | — |
| `onboarding/REGISTER_package-census_2026-09-15.md` | 2026-09-15 | 2026-09-15 | — | REGISTER (h) | `package-census` | compliant | onb-runbook 2, schema/index 1 | onboarding-runbook |
| `repo-hygiene/PROMPT_kit-bootstrap-session_2026-09-15.md` | untracked | untracked | — | PROMPT (h) | `kit-bootstrap-session` | compliant | none | — |

### 2.2 PlantLibrary_PyApp — `5cefe62`

| folder | .md | class | what is there |
|---|---|---|---|
| `.` | 4 | product documentation | `CLAUDE.md`, `AGENTS.md`, `PRODUCT.md` (PRD), `DESIGN.md` (token sheet) — durable, undated |
| `.docpipeline` | 5 | generated | documentation-pipeline step artifacts ("Generated by Step n") |
| `Documentation` | 31 | dated deliverable 27, product documentation 4 | 27 pre-MVP session documents (June 2026: proposals, plans, audits, gap lists, dated in the header only) + 4 product specs (`DatabaseStructure_GPT_V3`, `PlantLibraryGUI_GPT_V3`, `plant_information_api_keys`, `plant_information_sources`) |
| `Documentation/adr` | 7 | product documentation | `NNNN-kebab-title.md` ADRs (0001–0006) + README index — own convention |
| `GUI` | 8 | product documentation 7, dated deliverable 1 | GUI context routing and shared rules (SCREAMING_SNAKE topics); one candidate inside (`FUTURE_GUI_DEVELOPMENT_PROPOSAL.md`) |
| `GUI/common_requirements` | 1 | product documentation | README placeholder |
| `GUI/screen_structures` | 31 | product documentation 30, dated deliverable 1 | `Screen_Structure_<id>.md` implementation contracts (25) + index/policy; one candidate inside (`improvements.md`) |
| `GUI/source_derived` | 9 | product documentation 8, dated deliverable 1 | `<Topic>_From_Source.md` derived requirements; one candidate inside (`Source_GUI_Integration_Report.md`) |
| `GUI/templates` | 1 | product documentation | `Contract_Packet_Template.md` |
| `app/db/models` | 2 | product documentation | ↳ module reference docs beside the `.py` (`metadata.type: reference`), written by the doc pipeline |
| `app/db/repositories` | 2 | product documentation | ↳ module reference docs beside the `.py` (`metadata.type: reference`), written by the doc pipeline |
| `app/gui` | 1 | product documentation | ↳ module reference docs beside the `.py` (`metadata.type: reference`), written by the doc pipeline |
| `app/gui/views` | 3 | product documentation | ↳ module reference docs beside the `.py` (`metadata.type: reference`), written by the doc pipeline |
| `app/gui/wizard` | 1 | product documentation | ↳ module reference docs beside the `.py` (`metadata.type: reference`), written by the doc pipeline |
| `app/gui/wizard/steps` | 1 | product documentation | ↳ module reference docs beside the `.py` (`metadata.type: reference`), written by the doc pipeline |
| `app/plant_search` | 1 | product documentation | ↳ module reference docs beside the `.py` (`metadata.type: reference`), written by the doc pipeline |
| `app/providers` | 2 | product documentation | ↳ module reference docs beside the `.py` (`metadata.type: reference`), written by the doc pipeline |
| `app/services` | 5 | product documentation | ↳ module reference docs beside the `.py` (`metadata.type: reference`), written by the doc pipeline |
| `implementation` | 1 | package-schema (exempt) | `README.md` — package layout map |
| `implementation/Archive_PreMVP/Archive/GUI_Improvements_V3/screen_requirements_GPT` | 14 | frozen / terminal | ↳ frozen (onboarding runbook §1b, `IMPLEMENTATION_PLAN.md` §7) |
| `implementation/Archive_PreMVP/Improvements/Python_Client_Sync` | 8 | frozen / terminal | ↳ frozen (onboarding runbook §1b, `IMPLEMENTATION_PLAN.md` §7) |
| `implementation/Archive_PreMVP/Improvements/Python_Client_Sync/docs` | 15 | frozen / terminal | ↳ frozen (onboarding runbook §1b, `IMPLEMENTATION_PLAN.md` §7) |
| `implementation/Archive_PreMVP/Improvements/Python_Client_Sync/implementation` | 1 | frozen / terminal | ↳ frozen (onboarding runbook §1b, `IMPLEMENTATION_PLAN.md` §7) |
| `implementation/Archive_PreMVP/Improvements/Python_Client_Sync/validation` | 3 | frozen / terminal | ↳ frozen (onboarding runbook §1b, `IMPLEMENTATION_PLAN.md` §7) |
| `implementation/Archive_PreMVP/Prompts` | 22 | frozen / terminal | ↳ frozen (onboarding runbook §1b, `IMPLEMENTATION_PLAN.md` §7) |
| `implementation/MVP/package` | 1 | frozen / terminal | ↳ frozen terminal evidence chain |
| `implementation/System_V1_Implementation` | 7 | package-schema (exempt) | live package; all seven files are schema names |
| `implementation/System_V1_Implementation/proposal` | 1 | dated deliverable (candidate) | `PYAPP_V1_PROPOSAL.md` |
| `implementation/System_V1_Implementation/validation` | 3 | validation evidence (`<BATCH>_<slug>`, catalogued) | `PY1-B02_…`, `PY1-B07_…` + README manifest (which lists four files that do not exist) |
| `implementation/System_V1_Implementation/validation/evidence/PY-V1-GAP-CLOSURE-20260715-03` | 1 | validation evidence (`<BATCH>_<slug>`, catalogued) | ↳ `PY1-B02_…`, `PY1-B07_…` + README manifest (which lists four files that do not exist) |

**Candidates (31).** TYPE and topic are the census proposal (agent-read where marked, heuristic otherwise);
`?` marks a TYPE outside the enum (§6 of the runbook's gate, Q6). Dates: git = `git log --follow --diff-filter=A`;
header = the date the document states about itself; a differing pair is bolded.

| file | git-created | last change | header date | TYPE | topic | name today | citations | hold |
|---|---|---|---|---|---|---|---|---|
| `Documentation/Care_Profile_Enrichment_Implementation_Gaps_V1.md` | 2026-06-19 | 2026-06-19 | 2026-06-19 | AUDIT | `care-profile-enrichment-gaps` | non-compliant | candidate 1, other 1 | — |
| `Documentation/Care_Profile_Enrichment_Implementation_V1.md` | 2026-06-19 | 2026-06-19 | 2026-06-19 | PLAN | `care-profile-enrichment-parser-only` | non-compliant | candidate 1, other 1 | — |
| `Documentation/Care_Profile_Enrichment_Proposal_V1.md` | 2026-06-19 | 2026-06-19 | 2026-06-19 | PROPOSAL | `care-profile-enrichment-v1` | non-compliant | candidate 2, other 1 | — |
| `Documentation/Cross_Platform_Architecture_Proposal.md` | 2026-06-21 | 2026-06-21 | **2026-06-20** | PROPOSAL | `cross-platform-architecture` | non-compliant | candidate 2 | — |
| `Documentation/Cross_Platform_Baseline_Audit.md` | 2026-06-21 | 2026-06-21 | **2026-06-20** | AUDIT | `cross-platform-baseline` | non-compliant | candidate 2 | — |
| `Documentation/Cross_Platform_Checklist.md` | 2026-06-21 | 2026-07-16 | — | PLAN | `cross-platform-task-tracking` | non-compliant | frozen 6, candidate 2 | — |
| `Documentation/Cross_Platform_Implementation_Plan.md` | 2026-06-21 | 2026-06-21 | **2026-06-20** | PLAN | `cross-platform-delivery` | non-compliant | frozen 2 | — |
| `Documentation/Cross_Platform_Implementation_Plan_V1.md` | 2026-06-21 | 2026-06-21 | 2026-06-21 | PLAN | `cross-platform-delivery-v1` | non-compliant | frozen 2 | — |
| `Documentation/Cross_Platform_Implementation_Plan_V2.md` | 2026-06-21 | 2026-06-21 | 2026-06-21 | PLAN | `cross-platform-delivery-v2` | non-compliant | frozen 19, schema/index 1, candidate 1 | — |
| `Documentation/Cross_Platform_Proposal_V1.md` | 2026-06-21 | 2026-06-21 | 2026-06-21 | PROPOSAL | `cross-platform-v1` | non-compliant | candidate 1 | — |
| `Documentation/Cross_Platform_Proposal_V2.md` | 2026-06-21 | 2026-06-21 | 2026-06-21 | PROPOSAL | `cross-platform-v2` | non-compliant | frozen 3, schema/index 2, candidate 5 | — |
| `Documentation/Current_State_Assessment.md` | 2026-06-21 | 2026-06-21 | **2026-06-20** | AUDIT | `current-state` | non-compliant | candidate 3 | — |
| `Documentation/DECISIONS_NEEDED.md` | 2026-06-21 | 2026-06-21 | **2026-06-20** | REGISTER | `open-decisions-final-workflow` | non-compliant | candidate 2 | — |
| `Documentation/DataEnrichment_Proposal_Claude.md` | 2026-06-16 | 2026-06-16 | 2026-06-16 | PROPOSAL | `data-enrichment-pipeline` | non-compliant | candidate 3, other 1 | — |
| `Documentation/Design_Implementation_Claude.md` | 2026-06-16 | 2026-06-16 | — | PLAN | `verdant-design-system-adoption` | non-compliant | pinned 1, candidate 7, other-md 1 | pinned |
| `Documentation/Final_Workflow_Proposal_V1.md` | 2026-06-19 | 2026-06-19 | 2026-06-19 | PROPOSAL | `enrichment-workflow-v1` | non-compliant | candidate 3 | — |
| `Documentation/IMPLEMENTATION_CHECKLIST.md` | 2026-06-21 | 2026-06-21 | **2026-06-20** | PLAN | `enrichment-workflow-tasks` | non-compliant | frozen 2, candidate 1 | — |
| `Documentation/ImplementationPlan_Claude_V2.md` | 2026-06-15 | 2026-06-15 | 2026-06-15 | PLAN | `full-app-build-v2` | non-compliant | candidate 7 | — |
| `Documentation/Phase_0_2_fixing.md` | 2026-06-17 | 2026-06-17 | 2026-06-17 | FINDING | `phases-0-2-gaps` | non-compliant | none | — |
| `Documentation/Phase_0_6_fixing.md` | 2026-06-19 | 2026-06-19 | 2026-06-19 | FINDING | `phases-0-6-gaps` | non-compliant | none | — |
| `Documentation/Target_Architecture_Recommendation.md` | 2026-06-21 | 2026-06-21 | **2026-06-20** | PROPOSAL | `target-architecture` | non-compliant | candidate 2 | — |
| `Documentation/ToolbarButtons_Redesign_Claude.md` | 2026-06-16 | 2026-06-16 | — | PROPOSAL | `toolbar-buttons-redesign` | non-compliant | none | — |
| `Documentation/legacy-data-inventory.md` | 2026-06-22 | 2026-06-22 | **2026-06-21** | REGISTER | `legacy-sqlite-fixture` | non-compliant | frozen 2, candidate 7 | — |
| `Documentation/plant_information_system_implementation_plan_gaps.md` | 2026-06-17 | 2026-06-17 | 2026-06-17 | AUDIT | `plant-information-system-phases-0-6` | non-compliant | none | — |
| `Documentation/plant_information_system_implementation_plan_v1.md` | 2026-06-17 | 2026-06-19 | 2026-06-17 | PLAN | `plant-information-system-v1` | non-compliant | code 1, candidate 4 | code |
| `Documentation/plant_information_system_proposal_v2.md` | 2026-06-17 | 2026-06-17 | 2026-06-17 | PROPOSAL | `plant-information-system-v2` | non-compliant | candidate 2 | — |
| `Documentation/spike-results.md` | 2026-06-22 | 2026-06-22 | **2026-06-21** | EVIDENCE | `backend-spikes` | non-compliant | frozen 4, candidate 10 | — |
| `GUI/FUTURE_GUI_DEVELOPMENT_PROPOSAL.md` | 2026-07-03 | 2026-07-03 | 2026-07-03 | PROPOSAL | `future-gui-development-workflow` | non-compliant | schema/index 1, candidate 1 | — |
| `GUI/screen_structures/improvements.md` | 2026-07-01 | 2026-07-03 | — | FINDING | `gpt-screen-requirement-merge` | non-compliant | pinned 4 | pinned |
| `GUI/source_derived/Source_GUI_Integration_Report.md` | 2026-07-04 | 2026-07-04 | — | EVIDENCE | `source-gui-integration-run` | non-compliant | candidate 1, other-md 1 | — |
| `implementation/System_V1_Implementation/proposal/PYAPP_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-16 | **2026-07-09** | PROPOSAL | `pyapp-v1` | non-compliant | state 1, schema/index 2, candidate 1, other 5 | state |

Notes: `improvements.md` — hold restored by hand after the fresh-context review: the pinned Design initiative names it four times in lines that say `screen_requirements/` (the folder's earlier name), which the collision rule filtered out.

### 2.3 PlantLibrary_Server — `5c312d3`

| folder | .md | class | what is there |
|---|---|---|---|
| `.` | 3 | product documentation | `CLAUDE.md`, `AGENTS.md`, `README.md` |
| `app` | 1 | product documentation |  |
| `deploy` | 1 | product documentation |  |
| `docs` | 15 | product documentation 11, dated deliverable 4 | id-prefixed `<ROW-ID>_<snake_topic>.md` (`SV-SYNC-01_sync_protocol_notes.md`); 10 living design notes + 4 dated batch write-ups (`*_report.md`, candidates) + `local_android_test_environment.md` (dated H1, live runbook — product) |
| `implementation` | 1 | package-schema (exempt) |  |
| `implementation/MVP/evidence` | 1 | frozen / terminal | ↳ frozen |
| `implementation/MVP/handoffs` | 1 | frozen / terminal | ↳ frozen |
| `implementation/MVP/package` | 8 | frozen / terminal | ↳ frozen |
| `implementation/System_V1_Implementation` | 7 | package-schema (exempt) | live package; all seven files are schema names |
| `implementation/System_V1_Implementation/proposal` | 1 | dated deliverable (candidate) | ↳ live package |
| `implementation/System_V1_Implementation/validation` | 6 | validation evidence (`<BATCH>_<slug>`, catalogued) | `SV1-B00_…` (4), `SV1-B06_oidc_local.md` + README manifest naming five files that do not exist yet |
| `openapi` | 1 | product documentation |  |
| `tests` | 1 | product documentation |  |

**Candidates (5).** TYPE and topic are the census proposal (agent-read where marked, heuristic otherwise);
`?` marks a TYPE outside the enum (§6 of the runbook's gate, Q6). Dates: git = `git log --follow --diff-filter=A`;
header = the date the document states about itself; a differing pair is bolded.

| file | git-created | last change | header date | TYPE | topic | name today | citations | hold |
|---|---|---|---|---|---|---|---|---|
| `docs/SV-B07_dashboard_endpoint_coverage_report.md` | 2026-07-05 | 2026-07-05 | — | AUDIT | `sv-b07-dashboard-endpoint-coverage` | non-compliant | state 2, code 2, terminal-anchor 2, candidate 2 | code, state |
| `docs/SV-B07_runtime_verification_report.md` | 2026-07-05 | 2026-07-05 | **2026-07-04** | EVIDENCE | `sv-b07-runtime-verification` | non-compliant | state 1, terminal-anchor 2 | state |
| `docs/SV-B08_deployment_hardening_report.md` | 2026-07-05 | 2026-07-05 | — | EVIDENCE | `sv-b08-deployment-hardening` | non-compliant | state 1, terminal-anchor 2, frozen 4, candidate 1 | state |
| `docs/SV-CONTRACT-01_contract_validation_report.md` | 2026-07-04 | 2026-07-04 | — | AUDIT | `sv-contract-01-contract-validation` | non-compliant | terminal-anchor 5, schema/index 1 | — |
| `implementation/System_V1_Implementation/proposal/SERVER_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-16 | **2026-07-09** | PROPOSAL | `server-v1` | non-compliant | state 1, schema/index 3, candidate 2, other 6 | state |

### 2.4 PlantLibrary_SharedContracts — `75846a9`

| folder | .md | class | what is there |
|---|---|---|---|
| `.` | 2 | product documentation | `README.md`, `CONTRACT_VERSION.md` (bundle semver, pinned by name from five repos and two skills — never renamed) |
| `api-examples` | 1 | product documentation |  |
| `design-tokens` | 5 | product documentation | `platform-mapping-<platform>.md`, `TOKEN_USAGE_NOTES.md` |
| `generated` | 3 | generated | `CLIENT_MANIFEST.md` (pinned by name cross-repo), `GENERATION_BLOCKERS.md`, generator READMEs |
| `generated/kotlin` | 1 | generated | ↳ `CLIENT_MANIFEST.md` (pinned by name cross-repo), `GENERATION_BLOCKERS.md`, generator READMEs |
| `generated/kotlin/docs` | 64 | generated | openapi-generator 7.23.0 per-model docs |
| `generated/python` | 1 | generated | ↳ `CLIENT_MANIFEST.md` (pinned by name cross-repo), `GENERATION_BLOCKERS.md`, generator READMEs |
| `generated/typescript` | 1 | generated | ↳ `CLIENT_MANIFEST.md` (pinned by name cross-repo), `GENERATION_BLOCKERS.md`, generator READMEs |
| `generated/typescript/docs` | 64 | generated | openapi-generator 7.23.0 per-model docs |
| `implementation` | 1 | package-schema (exempt) |  |
| `implementation/MVP/handoffs` | 1 | frozen / terminal |  |
| `implementation/MVP/package` | 8 | frozen / terminal |  |
| `implementation/System_V1_Implementation` | 7 | package-schema (exempt) |  |
| `implementation/System_V1_Implementation/proposal` | 1 | dated deliverable (candidate) |  |
| `implementation/System_V1_Implementation/validation` | 2 | validation evidence (`<BATCH>_<slug>`, catalogued) | `SC1-B01_tooling_ci_doc_hygiene.md` + README naming three other files that do not exist |
| `openapi` | 2 | product documentation |  |
| `page-contracts/android` | 7 | product documentation | `MobilePageContract_<page>.md` + `EXCLUSIONS.md` |
| `page-contracts/desktop-web` | 12 | product documentation | `PageContract_<page>.md` (11) |
| `schemas` | 1 | product documentation |  |
| `scripts` | 1 | product documentation |  |
| `sync-contracts` | 1 | product documentation |  |
| `tests/contract_validation` | 1 | product documentation |  |

**Candidates (1).** TYPE and topic are the census proposal (agent-read where marked, heuristic otherwise);
`?` marks a TYPE outside the enum (§6 of the runbook's gate, Q6). Dates: git = `git log --follow --diff-filter=A`;
header = the date the document states about itself; a differing pair is bolded.

| file | git-created | last change | header date | TYPE | topic | name today | citations | hold |
|---|---|---|---|---|---|---|---|---|
| `implementation/System_V1_Implementation/proposal/SHAREDCONTRACTS_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | PROPOSAL | `sharedcontracts-v1` | non-compliant | state 1, schema/index 2, candidate 1, other 5 | state |

### 2.5 PlantLibrary_Dashboard — `472e7d2`

| folder | .md | class | what is there |
|---|---|---|---|
| `.` | 1 | product documentation |  |
| `docs` | 8 | product documentation 4, dated deliverable 4 | id-prefixed `WD-<AREA>-<NN>_<topic>.md`; 3 living notes (`WD-AUTH-01`, `WD-BOOT-02`, `WD-DESIGN-01`) + 4 dated deliverables (candidates) |
| `implementation` | 1 | package-schema (exempt) |  |
| `implementation/MVP/handoffs` | 1 | frozen / terminal |  |
| `implementation/MVP/package` | 8 | frozen / terminal |  |
| `implementation/System_V1_Implementation` | 7 | package-schema (exempt) |  |
| `implementation/System_V1_Implementation/proposal` | 1 | dated deliverable (candidate) |  |
| `implementation/System_V1_Implementation/validation` | 3 | validation evidence (`<BATCH>_<slug>`, catalogued) | `WD1-B07_token_drift.md`, `WD1-B08_local_oidc.md` + README |
| `references/PlantLibrary_pythonApp_old/mockup_briefs` | 13 | frozen / terminal | ↳ frozen reference copy of the old Python-app mockup briefs and screen requirements (42) |
| `references/PlantLibrary_pythonApp_old/screen_requirements` | 29 | frozen / terminal | ↳ frozen reference copy of the old Python-app mockup briefs and screen requirements (42) |
| `src` | 1 | product documentation |  |
| `src/api` | 1 | product documentation |  |
| `tests` | 1 | product documentation |  |

**Candidates (5).** TYPE and topic are the census proposal (agent-read where marked, heuristic otherwise);
`?` marks a TYPE outside the enum (§6 of the runbook's gate, Q6). Dates: git = `git log --follow --diff-filter=A`;
header = the date the document states about itself; a differing pair is bolded.

| file | git-created | last change | header date | TYPE | topic | name today | citations | hold |
|---|---|---|---|---|---|---|---|---|
| `docs/WD-A11Y-01_validation_report.md` | 2026-07-05 | 2026-07-05 | — | EVIDENCE | `wd-a11y-01-accessibility-validation` | non-compliant | state 1, terminal-anchor 3 | state |
| `docs/WD-MOCKUP-UPGRADE_PROPOSAL.md` | 2026-07-07 | 2026-07-07 | 2026-07-07 | PROPOSAL | `wd-mockup-driven-dashboard-upgrade` | non-compliant | state 1, pinned 1, terminal-anchor 3 | pinned, state |
| `docs/WD-PARITY-01_parity_report.md` | 2026-07-05 | 2026-07-05 | — | AUDIT | `wd-parity-01-page-contract-parity` | non-compliant | state 1, terminal-anchor 3 | state |
| `docs/WD-UX-10_mockup_parity_report.md` | 2026-07-07 | 2026-07-07 | 2026-07-07 | AUDIT | `wd-ux-10-mockup-parity` | non-compliant | state 1, pinned 1, terminal-anchor 4, candidate 1 | pinned, state |
| `implementation/System_V1_Implementation/proposal/DASHBOARD_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | PROPOSAL | `dashboard-v1` | non-compliant | state 1, schema/index 2, candidate 1, other 5 | state |

### 2.6 PlantLibrary_AndroidApp — `b75265a`

| folder | .md | class | what is there |
|---|---|---|---|
| `.` | 1 | product documentation |  |
| `app` | 1 | product documentation |  |
| `core` | 1 | product documentation |  |
| `docs` | 12 | product documentation 11, dated deliverable 1 | `<topic>_plan.md` living design docs keyed to a row id in the H1 (10) + `security_token_storage_acceptance.md` (an accepted-deviation record, candidate) + `android_studio_emulator_configs.md` |
| `feature` | 1 | product documentation |  |
| `feature/addplant` | 1 | product documentation |  |
| `feature/home` | 1 | product documentation |  |
| `feature/plants` | 1 | product documentation |  |
| `feature/tasks` | 1 | product documentation |  |
| `implementation` | 1 | package-schema (exempt) |  |
| `implementation/MVP/evidence` | 11 | frozen / terminal | ↳ frozen |
| `implementation/MVP/handoffs` | 2 | frozen / terminal | ↳ frozen |
| `implementation/MVP/package` | 9 | frozen / terminal | ↳ frozen |
| `implementation/System_V1_Implementation` | 7 | package-schema (exempt) |  |
| `implementation/System_V1_Implementation/proposal` | 1 | dated deliverable (candidate) |  |
| `implementation/System_V1_Implementation/validation` | 5 | validation evidence (`<BATCH>_<slug>`, catalogued) | `AN1-B00_…` (2), `AN1-B12_…`, `AN1-B14_…` + README naming two files that do not exist |

**Candidates (2).** TYPE and topic are the census proposal (agent-read where marked, heuristic otherwise);
`?` marks a TYPE outside the enum (§6 of the runbook's gate, Q6). Dates: git = `git log --follow --diff-filter=A`;
header = the date the document states about itself; a differing pair is bolded.

| file | git-created | last change | header date | TYPE | topic | name today | citations | hold |
|---|---|---|---|---|---|---|---|---|
| `docs/security_token_storage_acceptance.md` | 2026-07-06 | 2026-07-06 | — | DECISION? | `auth-token-storage-deviation` | non-compliant | live-anchor 2, state 1, code 1, terminal-anchor 1, frozen 1, candidate 1, other 2 | code, live-package-anchor, state |
| `implementation/System_V1_Implementation/proposal/ANDROIDAPP_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-16 | **2026-07-09** | PROPOSAL | `androidapp-v1` | non-compliant | schema/index 2, candidate 3, other 4 | — |

### 2.7 PlantLibrary_Workspace — `5147569`

| folder | .md | class | what is there |
|---|---|---|---|
| `.` | 3 | product documentation | `README.md`; `REPOSITORY_MAP.md` (living suite map); `WORKSPACE_STATE.md` (living state doc, stale since 2026-07-06 per onboarding Appendix D) |
| `MVP_Reconciliation` | 8 | dated deliverable 7, package-schema 1 | numbered chapter set 00–06, every header "MVP-reconciliation snapshot (frozen 2026-07-09)" + README |
| `docs` | 5 | dated deliverable 4, product documentation 1 | two Fable-5 prompt files, two desk-research reports (2026-07-11), `local_development.md` (standing how-to) |
| `docs/fable5_business_proposal` | 11 | dated deliverable (candidate) | one proposal as numbered chapters 00–10 (2026-07-11, "Proposal only") |
| `docs/fable5_strategy_proposal` | 7 | dated deliverable (candidate) | one proposal as numbered chapters 00–06 (2026-07-11) |
| `docs/fable5_strategy_proposal_v2` | 5 | dated deliverable 4, product documentation 1 | v2 reconciliation layer, chapters 00/07/08/09 + README (2026-07-11) |
| `docs/proposals` | 3 | dated deliverable (candidate) | three free-standing proposals |
| `docs/proposals/Repo_Restructure_MVP_V1_Split` | 4 | dated deliverable (candidate) | the executed 2026-07-15/16 restructure track (proposal, prompts, verification report) |
| `docs/proposals/Repo_Restructure_MVP_V1_Split/manifests` | 1 | generated | `REVIEW_LIST.md` — roll-up of the `MANIFEST_*.csv` REVIEW rows |
| `implementation` | 1 | package-schema (exempt) | `README.md` — package index |
| `implementation/Server_VM_Setup` | 2 | dated deliverable (candidate) | a run-this prompt and a Proxmox setup runbook (2026-07-09); no package |
| `implementation/System_Design_Architecture` | 8 | package-schema 7, dated deliverable 1 | live package (gated on `SDA-DEC-01..05`); `MODEL_RECOMMENDATION.md` is a non-schema dated proposal inside the package root |
| `implementation/System_Design_Architecture/proposal` | 5 | dated deliverable (candidate) | numbered set 00–04; `04_APPROVED_DESIGN_REVISION_2026-07-10.md` is the owner-approved values record the Design kit cites |
| `implementation/System_Integration_MVP` | 14 | frozen / terminal | frozen terminal (MVP closed 2026-07-15) |
| `implementation/System_Integration_MVP/validation` | 14 | frozen / terminal | ↳ frozen terminal (MVP closed 2026-07-15) |
| `implementation/System_Integration_MVP/validation/evidence/MVP-VALIDATION-20260708-01` | 8 | frozen / terminal | ↳ frozen terminal (MVP closed 2026-07-15) |
| `implementation/System_Tooling` | 7 | frozen / terminal | frozen terminal (`WST-B01`, `WST-B02` done) |
| `implementation/System_Tooling/proposal` | 1 | frozen / terminal | ↳ frozen terminal (`WST-B01`, `WST-B02` done) |
| `implementation/System_Tooling/validation` | 6 | frozen / terminal | ↳ frozen terminal (`WST-B01`, `WST-B02` done) |
| `implementation/System_V1_Implementation` | 10 | package-schema 7, product documentation 3 | live coordinating package; `SKILLS.md`, `SUITE_HANDOFFS.md`, `V1_IMPLEMENTATION_SEQUENCE.md` are living package organs with non-schema names (product, not renamed) |
| `implementation/System_V1_Implementation/proposal` | 3 | dated deliverable (candidate) | numbered set 00–02 (`02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` already carries its date) |
| `implementation/System_V1_Implementation/validation` | 4 | validation evidence (`<BATCH>_<slug>`, catalogued) | `SY1-B06_…`, `SY1_checkpoints.md` + README |
| `methodology` | 1 | product documentation | `VALIDATION_METHODOLOGY.md` — standing normative methodology cited across suites (product); the two pinned trees sit below |
| `methodology/Design_Template_Initiative` | 11 | pinned by the Design kit (held) | pinned — the Design kit's live initiative (Phase 6; `STATE.md`, `HANDOVER.md`, `PROMPTS\`, `evidence\`) |
| `methodology/Design_Template_Initiative/PROMPTS` | 24 | pinned by the Design kit (held) | ↳ pinned — the Design kit's live initiative (Phase 6 |
| `methodology/Design_Template_Initiative/evidence` | 10 | pinned by the Design kit (held) | ↳ pinned — the Design kit's live initiative (Phase 6 |
| `methodology/GUI_Improvement_Methodology` | 36 | pinned by the Design kit (held) | pinned — `VERSION.md` 4.0.0, 28 `*_TEMPLATE.md`, `PROMPTS\`, `SKILL_SPECS\`; pinned by absolute path, version and per-file name from `Design_Template_Kit\METHODOLOGY_SOURCE.md` |
| `methodology/GUI_Improvement_Methodology/PROMPTS` | 14 | pinned by the Design kit (held) | ↳ pinned — `VERSION.md` 4.0.0, 28 `*_TEMPLATE.md`, `PROMPTS\`, `SKILL_SPECS\` |
| `methodology/GUI_Improvement_Methodology/SKILL_SPECS` | 12 | pinned by the Design kit (held) | ↳ pinned — `VERSION.md` 4.0.0, 28 `*_TEMPLATE.md`, `PROMPTS\`, `SKILL_SPECS\` |
| `prompts` | 1 | dated deliverable (candidate) | `PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` (date already in the name) |
| `prompts/reference` | 5 | product documentation 4, dated deliverable 1 | four `*_V3.md` template reference copies (product) + one misfiled session prompt (candidate) |
| `strategy/Cross_Platform_Strategy` | 11 | frozen / terminal | frozen terminal (closed 2026-07-06); UPPER_SNAKE topics, numbered `PROMPTS\` |
| `strategy/Cross_Platform_Strategy/PROMPTS` | 3 | frozen / terminal | ↳ frozen terminal (closed 2026-07-06) |
| `strategy/Cross_Platform_Strategy/validation` | 3 | frozen / terminal | ↳ frozen terminal (closed 2026-07-06) |
| `system_description` | 1 | frozen / terminal |  |
| `system_description/PlantLibrary_System_Description` | 13 | frozen / terminal | frozen; numbered chapter directories `NN_topic\NN_UPPER_SNAKE.md`, position is load-bearing |
| `system_description/PlantLibrary_System_Description/00_overview` | 7 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/01_architecture` | 6 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/02_domain_model` | 10 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/03_platforms` | 7 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/04_sync_and_data_consistency` | 10 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/05_api_and_contracts` | 8 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/06_ui_ux` | 8 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/07_security_identity_privacy` | 9 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/08_enrichment_media_ai` | 6 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/09_operations` | 7 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/10_quality_acceptance` | 8 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/11_derivation_inputs` | 7 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/12_future_derivation` | 5 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/completion/Missing_Context_Completion` | 8 | frozen / terminal | ↳ frozen |
| `system_description/PlantLibrary_System_Description/validation` | 18 | frozen / terminal | ↳ frozen |

**Candidates (53).** TYPE and topic are the census proposal (agent-read where marked, heuristic otherwise);
`?` marks a TYPE outside the enum (§6 of the runbook's gate, Q6). Dates: git = `git log --follow --diff-filter=A`;
header = the date the document states about itself; a differing pair is bolded.

| file | git-created | last change | header date | TYPE | topic | name today | citations | hold |
|---|---|---|---|---|---|---|---|---|
| `MVP_Reconciliation/00_SOURCE_INVENTORY.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | REGISTER | `mvp-source-inventory` | non-compliant | schema/index 1, candidate 1, other 1 | — |
| `MVP_Reconciliation/01_CURRENT_SYSTEM_BASELINE.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | SNAPSHOT | `mvp-current-system-baseline` | non-compliant | schema/index 2, candidate 2, other 2 | — |
| `MVP_Reconciliation/02_GAPS_AND_DEFERRED_REGISTER.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | REGISTER | `mvp-gaps-and-deferrals` | non-compliant | live-anchor 2, schema/index 1, candidate 9, other-md 1, other 11 | live-package-anchor |
| `MVP_Reconciliation/03_SUBSYSTEM_RECONCILIATION.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | FINDING | `mvp-subsystem-reconciliation` | non-compliant | schema/index 1, candidate 2, other 2 | — |
| `MVP_Reconciliation/04_MVP_TO_V1_PROPOSAL.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | PROPOSAL | `mvp-to-v1` | non-compliant | live-anchor 1, schema/index 2, candidate 6, other 7 | live-package-anchor |
| `MVP_Reconciliation/05_NEXT_STEPS_AND_USAGE.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | PLAN | `mvp-reconciliation-next-steps` | non-compliant | live-anchor 1, schema/index 3, candidate 7, other-md 1, other 12 | live-package-anchor |
| `MVP_Reconciliation/06_V1_KICKOFF_PROMPT.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | PROMPT | `v1-kickoff` | non-compliant | none | — |
| `docs/fable5_business_proposal_prompt.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROMPT | `fable5-business-gtm-proposal` | non-compliant | none | — |
| `docs/fable5_system_strategy_proposal_prompt.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROMPT | `fable5-system-strategy-proposal` | non-compliant | none | — |
| `docs/garden-app-product-research.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | REPORT? | `garden-apps-4-products` | non-compliant | candidate 1 | — |
| `docs/garden-app-product-research_2.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | REPORT? | `garden-apps-13-products` | non-compliant | candidate 3 | — |
| `docs/fable5_business_proposal/00_EXECUTIVE_SUMMARY.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-executive-summary` | non-compliant | terminal-anchor 1, frozen 2, schema/index 2, candidate 5, other 1 | — |
| `docs/fable5_business_proposal/01_BUSINESS_MODEL_OPTIONS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-business-model-options` | non-compliant | candidate 2 | — |
| `docs/fable5_business_proposal/02_PACKAGING_AND_PRICING.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-packaging-and-pricing` | non-compliant | candidate 4, other 1 | — |
| `docs/fable5_business_proposal/03_GO_TO_MARKET.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-go-to-market` | non-compliant | candidate 2 | — |
| `docs/fable5_business_proposal/04_POSITIONING_AND_MESSAGING.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-positioning-and-messaging` | non-compliant | candidate 2 | — |
| `docs/fable5_business_proposal/05_SALES_MOTION_AND_CHANNELS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-sales-motion-and-channels` | non-compliant | candidate 2 | — |
| `docs/fable5_business_proposal/06_UNIT_ECONOMICS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-unit-economics` | non-compliant | candidate 2 | — |
| `docs/fable5_business_proposal/07_RISKS_AND_MITIGATIONS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-risks-and-mitigations` | non-compliant | candidate 2 | — |
| `docs/fable5_business_proposal/08_LICENSING_RECOMMENDATION.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-licensing-recommendation` | non-compliant | candidate 2 | — |
| `docs/fable5_business_proposal/09_ROADMAP_TIE_IN.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-roadmap-tie-in` | non-compliant | candidate 3 | — |
| `docs/fable5_business_proposal/10_ASSUMPTIONS_AND_OPEN_QUESTIONS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `business-gtm-assumptions-and-open-questions` | non-compliant | candidate 4, other 1 | — |
| `docs/fable5_strategy_proposal/00_EXECUTIVE_SUMMARY.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v1-executive-summary` | non-compliant | terminal-anchor 1, frozen 2, schema/index 2, candidate 5, other 1 | — |
| `docs/fable5_strategy_proposal/01_USER_SEGMENTS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v1-user-segments` | non-compliant | schema/index 1, candidate 4, other 1 | — |
| `docs/fable5_strategy_proposal/02_FUNCTION_CATALOG.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v1-function-catalog` | non-compliant | schema/index 1, candidate 6, other 1 | — |
| `docs/fable5_strategy_proposal/03_PRIORITIZATION_AND_FOCUS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v1-prioritization-and-focus` | non-compliant | schema/index 1, candidate 3, other 1 | — |
| `docs/fable5_strategy_proposal/04_FUTURE_INTEGRATIONS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v1-future-integrations` | non-compliant | schema/index 1, candidate 6, other 1 | — |
| `docs/fable5_strategy_proposal/05_NON_GOALS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v1-non-goals` | non-compliant | schema/index 1, candidate 5, other 1 | — |
| `docs/fable5_strategy_proposal/06_ASSUMPTIONS_AND_OPEN_QUESTIONS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v1-assumptions-and-open-questions` | non-compliant | schema/index 1, candidate 4, other 1 | — |
| `docs/fable5_strategy_proposal_v2/00_EXECUTIVE_SUMMARY.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v2-executive-summary` | non-compliant | terminal-anchor 1, frozen 2, schema/index 2, candidate 4, other 1 | — |
| `docs/fable5_strategy_proposal_v2/07_SOURCE_MAP_AND_RECONCILIATION.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v2-source-map-and-reconciliation` | non-compliant | schema/index 1, candidate 2, other 1 | — |
| `docs/fable5_strategy_proposal_v2/08_WORKING_DECISIONS.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v2-working-decisions` | non-compliant | schema/index 3, candidate 3, other 1 | — |
| `docs/fable5_strategy_proposal_v2/09_BATCH_DERIVATION_GUIDE.md` | 2026-07-11 | 2026-07-11 | 2026-07-11 | PROPOSAL | `product-strategy-v2-batch-derivation-guide` | non-compliant | schema/index 2, candidate 5, other 1 | — |
| `docs/proposals/ENRICHMENT_V2_PROPOSAL.md` | 2026-07-10 | 2026-07-10 | 2026-07-10 | PROPOSAL | `enrichment-v2` | non-compliant | other 2 | — |
| `docs/proposals/GARDEN_DESIGNER_PROPOSAL.md` | 2026-07-10 | 2026-07-10 | 2026-07-10 | PROPOSAL | `garden-designer` | non-compliant | other 2 | — |
| `docs/proposals/PlantLibrary_Full_Implementation_Update.md` | 2026-07-16 | 2026-07-16 | — | PROPOSAL | `full-implementation-package` | non-compliant | code 1, candidate 4 | code |
| `docs/proposals/Repo_Restructure_MVP_V1_Split/EXECUTION_PROMPTS.md` | 2026-07-15 | 2026-07-16 | 2026-07-15 | PROMPTS | `repo-restructure-execution` | non-compliant | candidate 1 | — |
| `docs/proposals/Repo_Restructure_MVP_V1_Split/FOLLOWUP_CLOSURE_PROMPT.md` | 2026-07-16 | 2026-07-16 | 2026-07-16 | PROMPT | `repo-restructure-followup-closure` | non-compliant | none | — |
| `docs/proposals/Repo_Restructure_MVP_V1_Split/PROPOSAL.md` | 2026-07-15 | 2026-07-15 | 2026-07-15 | PROPOSAL | `repo-restructure-mvp-v1-split` | non-compliant | candidate 4, other-md 1 | — |
| `docs/proposals/Repo_Restructure_MVP_V1_Split/VERIFICATION_REPORT.md` | 2026-07-16 | 2026-07-16 | 2026-07-16 | EVIDENCE | `repo-restructure-phase5-verification` | non-compliant | candidate 6 | — |
| `implementation/Server_VM_Setup/DockerDesktop_Audit_Migration_Prompt.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | PROMPT | `docker-desktop-audit-migration` | non-compliant | candidate 2 | — |
| `implementation/Server_VM_Setup/ServerSetUp_MVP.md` | 2026-07-10 | 2026-07-10 | **2026-07-09** | GUIDE? | `proxmox-server-setup-mvp` | non-compliant | none | — |
| `implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md` | 2026-07-09 | 2026-07-09 | **2026-07-08** | PROPOSAL | `sda-model-allocation` | non-compliant | pinned 4, code 1, schema/index 3, candidate 1, other-md 2 | code, pinned |
| `implementation/System_Design_Architecture/proposal/00_DESIGN_GOVERNANCE_PROPOSAL.md` | 2026-07-09 | 2026-07-09 | — | PROPOSAL | `design-governance` | non-compliant | pinned 4, design-kit 2, schema/index 3, candidate 4, other 2 | external-kit, pinned |
| `implementation/System_Design_Architecture/proposal/01_DESIGN_ARTIFACT_TEMPLATES.md` | 2026-07-09 | 2026-07-09 | — | PROPOSAL | `design-artifact-templates` | non-compliant | pinned 4, schema/index 2, candidate 4, other 4 | pinned |
| `implementation/System_Design_Architecture/proposal/02_CONFORMANCE_AND_ENFORCEMENT.md` | 2026-07-09 | 2026-07-09 | — | PROPOSAL | `design-conformance-enforcement` | non-compliant | pinned 5, design-kit 1, schema/index 2, candidate 9, other-md 1, other 7 | external-kit, pinned |
| `implementation/System_Design_Architecture/proposal/03_CLAUDE_MD_AND_DOC_LAYERING.md` | 2026-07-09 | 2026-07-09 | — | PROPOSAL | `claude-md-doc-layering` | non-compliant | pinned 5, schema/index 2 | pinned |
| `implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | 2026-07-10 | 2026-07-10 | 2026-07-10 | DECISION? | `approved-design-revision` | non-compliant | live-anchor 6, state 5, pinned 5, design-kit 10, code 1, candidate 1, other-md 6, other 2 | code, external-kit, live-package-anchor, pinned, state |
| `implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` | 2026-07-10 | 2026-07-16 | **2026-07-09** | PROPOSAL | `v1-system` | non-compliant | live-anchor 3, state 5, frozen 9, schema/index 13, candidate 10, other-md 2, other 37 | live-package-anchor, state |
| `implementation/System_V1_Implementation/proposal/01_PRODUCT_VALUE_AUDIT.md` | 2026-07-10 | 2026-07-10 | 2026-07-10 | AUDIT | `product-value` | non-compliant | live-anchor 1, state 2, frozen 3, schema/index 1, candidate 2, other-md 2 | live-package-anchor, state |
| `implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | 2026-07-10 | 2026-07-10 | 2026-07-10 | DECISION? | `validation-methodology` | non-compliant | live-anchor 8, state 6, schema/index 1, candidate 2, other-md 1 | live-package-anchor, state |
| `prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | 2026-07-10 | 2026-07-10 | 2026-07-10 | HANDOVER | `process-improvements` | non-compliant | live-anchor 3, state 5, frozen 3, other 3 | live-package-anchor, state |
| `prompts/reference/SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | 2026-07-16 | 2026-07-16 | **2026-07-06** | PROMPT | `setup-android-test-environment` | non-compliant | state 1, code 1, terminal-anchor 1, frozen 1, candidate 3 | code, state |

Notes: `00_SOURCE_INVENTORY.md` — numbered chapter set (00-06); `01_CURRENT_SYSTEM_BASELINE.md` — numbered chapter set (00-06); `02_GAPS_AND_DEFERRED_REGISTER.md` — numbered chapter set (00-06); `03_SUBSYSTEM_RECONCILIATION.md` — numbered chapter set (00-06); `04_MVP_TO_V1_PROPOSAL.md` — numbered chapter set (00-06); `05_NEXT_STEPS_AND_USAGE.md` — numbered chapter set (00-06); `06_V1_KICKOFF_PROMPT.md` — numbered chapter set (00-06); `garden-app-product-research.md` — desk research; enum has no fit (REPORT proposed); `garden-app-product-research_2.md` — desk research; `_2` is a version suffix; `00_EXECUTIVE_SUMMARY.md` — numbered chapter set (00-10) of one proposal; `01_BUSINESS_MODEL_OPTIONS.md` — numbered chapter set (00-10) of one proposal; `02_PACKAGING_AND_PRICING.md` — numbered chapter set (00-10) of one proposal; `03_GO_TO_MARKET.md` — numbered chapter set (00-10) of one proposal; `04_POSITIONING_AND_MESSAGING.md` — numbered chapter set (00-10) of one proposal; `05_SALES_MOTION_AND_CHANNELS.md` — numbered chapter set (00-10) of one proposal; `06_UNIT_ECONOMICS.md` — numbered chapter set (00-10) of one proposal; `07_RISKS_AND_MITIGATIONS.md` — numbered chapter set (00-10) of one proposal; `08_LICENSING_RECOMMENDATION.md` — numbered chapter set (00-10) of one proposal; `09_ROADMAP_TIE_IN.md` — numbered chapter set (00-10) of one proposal; `10_ASSUMPTIONS_AND_OPEN_QUESTIONS.md` — numbered chapter set (00-10) of one proposal; `00_EXECUTIVE_SUMMARY.md` — numbered chapter set (00-06) of one proposal; `01_USER_SEGMENTS.md` — numbered chapter set (00-06) of one proposal; `02_FUNCTION_CATALOG.md` — numbered chapter set (00-06) of one proposal; `03_PRIORITIZATION_AND_FOCUS.md` — numbered chapter set (00-06) of one proposal; `04_FUTURE_INTEGRATIONS.md` — numbered chapter set (00-06) of one proposal; `05_NON_GOALS.md` — numbered chapter set (00-06) of one proposal; `06_ASSUMPTIONS_AND_OPEN_QUESTIONS.md` — numbered chapter set (00-06) of one proposal; `00_EXECUTIVE_SUMMARY.md` — numbered chapter set of one proposal (v2 layer); `07_SOURCE_MAP_AND_RECONCILIATION.md` — numbered chapter set of one proposal (v2 layer); `08_WORKING_DECISIONS.md` — numbered chapter set of one proposal (v2 layer); `09_BATCH_DERIVATION_GUIDE.md` — numbered chapter set of one proposal (v2 layer); `ServerSetUp_MVP.md` — standing install runbook; arguably product-doc (GUIDE proposed); `MODEL_RECOMMENDATION.md` — non-schema file inside a live package root; `00_DESIGN_GOVERNANCE_PROPOSAL.md` — numbered set (00-04); `01_DESIGN_ARTIFACT_TEMPLATES.md` — numbered set (00-04); `02_CONFORMANCE_AND_ENFORCEMENT.md` — numbered set (00-04); `03_CLAUDE_MD_AND_DOC_LAYERING.md` — numbered set (00-04); `04_APPROVED_DESIGN_REVISION_2026-07-10.md` — numbered set (00-04); `00_V1_SYSTEM_PROPOSAL.md` — numbered set (00-02); `01_PRODUCT_VALUE_AUDIT.md` — numbered set (00-02); `02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` — numbered set (00-02); `PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` — date already in name; HANDOFF is a synonym; `SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` — misfiled in a template folder.

---

## 3. Hold register — every hold with the citation that causes it

One row per hold-class citation (path:line, class). A rename of the held file needs either the citing file edited in the
same change (only where the citing file is editable by this track: the onboarding track's own documents are **not**, live
package anchors and `STATE.md` files are **never** edited by a rename, pinned trees and the Design kit are another kit's) or
the hold released by the owner of the citation. The M-0 rename map lists every held name with its target-on-release, as
the Chapter-8 precedent did.

| held file | citing file | line | class |
|---|---|---|---|
| `SW_Development/HANDOVER_batch-package-schema-drift_2026-09-15.md` | `SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | 5 | onboarding-runbook |
| `SW_Development/IMPLEMENTATION_PLAN.md` | `SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | 17 (+7) | onboarding-runbook |
| `SW_Development/onboarding/AUDIT_skill-assumptions_2026-09-15.md` | `SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | 897 | onboarding-runbook |
| `SW_Development/onboarding/REGISTER_package-census_2026-09-15.md` | `SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | 251 (+1) | onboarding-runbook |
| `PlantLibrary_PyApp/Documentation/Design_Implementation_Claude.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md` | 130 | pinned |
| `PlantLibrary_PyApp/Documentation/plant_information_system_implementation_plan_v1.md` | `PlantLibrary_PyApp/tests/services/test_ai_extraction_service.py` | 1 | code |
| `PlantLibrary_PyApp/GUI/screen_structures/improvements.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md` | 122 | pinned |
| `PlantLibrary_PyApp/GUI/screen_structures/improvements.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/STATE.md` | 1695 | pinned |
| `PlantLibrary_PyApp/GUI/screen_structures/improvements.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/evidence/00_inventory_reverification.md` | 64 (+1) | pinned |
| `PlantLibrary_PyApp/implementation/System_V1_Implementation/proposal/PYAPP_V1_PROPOSAL.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/STATE.md` | 10 | state |
| `PlantLibrary_Server/docs/SV-B07_dashboard_endpoint_coverage_report.md` | `PlantLibrary_Server/app/api/routes/dashboard_support.py` | 2 | code |
| `PlantLibrary_Server/docs/SV-B07_dashboard_endpoint_coverage_report.md` | `PlantLibrary_Server/app/workers/tasks.py` | 9 | code |
| `PlantLibrary_Server/docs/SV-B07_dashboard_endpoint_coverage_report.md` | `PlantLibrary_Server/implementation/MVP/package/STATE.md` | 49 (+1) | state |
| `PlantLibrary_Server/docs/SV-B07_runtime_verification_report.md` | `PlantLibrary_Server/implementation/MVP/package/STATE.md` | 181 | state |
| `PlantLibrary_Server/docs/SV-B08_deployment_hardening_report.md` | `PlantLibrary_Server/implementation/MVP/package/STATE.md` | 183 | state |
| `PlantLibrary_Server/implementation/System_V1_Implementation/proposal/SERVER_V1_PROPOSAL.md` | `PlantLibrary_Server/implementation/System_V1_Implementation/STATE.md` | 15 | state |
| `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/proposal/SHAREDCONTRACTS_V1_PROPOSAL.md` | `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/STATE.md` | 11 | state |
| `PlantLibrary_Dashboard/docs/WD-A11Y-01_validation_report.md` | `PlantLibrary_Dashboard/implementation/MVP/package/STATE.md` | 172 | state |
| `PlantLibrary_Dashboard/docs/WD-MOCKUP-UPGRADE_PROPOSAL.md` | `PlantLibrary_Dashboard/implementation/MVP/package/STATE.md` | 403 | state |
| `PlantLibrary_Dashboard/docs/WD-MOCKUP-UPGRADE_PROPOSAL.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/METHODOLOGY_RECONCILIATION.md` | 24 | pinned |
| `PlantLibrary_Dashboard/docs/WD-PARITY-01_parity_report.md` | `PlantLibrary_Dashboard/implementation/MVP/package/STATE.md` | 172 | state |
| `PlantLibrary_Dashboard/docs/WD-UX-10_mockup_parity_report.md` | `PlantLibrary_Dashboard/implementation/MVP/package/STATE.md` | 75 | state |
| `PlantLibrary_Dashboard/docs/WD-UX-10_mockup_parity_report.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/METHODOLOGY_RECONCILIATION.md` | 24 | pinned |
| `PlantLibrary_Dashboard/implementation/System_V1_Implementation/proposal/DASHBOARD_V1_PROPOSAL.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/STATE.md` | 10 | state |
| `PlantLibrary_AndroidApp/docs/security_token_storage_acceptance.md` | `PlantLibrary_AndroidApp/core/auth/src/main/java/com/plantlibrary/android/core/auth/AuthTokenStore.kt` | 27 | code |
| `PlantLibrary_AndroidApp/docs/security_token_storage_acceptance.md` | `PlantLibrary_AndroidApp/implementation/MVP/package/STATE.md` | 371 | state |
| `PlantLibrary_AndroidApp/docs/security_token_storage_acceptance.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/TASK_CHECKLIST.md` | 54 | live-package-anchor |
| `PlantLibrary_AndroidApp/docs/security_token_storage_acceptance.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/TASK_CONTEXT.md` | 350 | live-package-anchor |
| `PlantLibrary_Workspace/MVP_Reconciliation/02_GAPS_AND_DEFERRED_REGISTER.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/BATCH_PLAN.md` | 26 | live-package-anchor |
| `PlantLibrary_Workspace/MVP_Reconciliation/02_GAPS_AND_DEFERRED_REGISTER.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/BATCH_PLAN.md` | 20 | live-package-anchor |
| `PlantLibrary_Workspace/MVP_Reconciliation/04_MVP_TO_V1_PROPOSAL.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/TASK_CONTEXT.md` | 22 | live-package-anchor |
| `PlantLibrary_Workspace/MVP_Reconciliation/05_NEXT_STEPS_AND_USAGE.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/BATCH_PLAN.md` | 11 | live-package-anchor |
| `PlantLibrary_Workspace/docs/proposals/PlantLibrary_Full_Implementation_Update.md` | `PlantLibrary_Workspace/docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_complete.csv` | 2 | code |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md` | `PlantLibrary_Workspace/docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_Workspace.csv` | 3 | code |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/DRIVER.md` | 7 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md` | 97 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/KICKOFF_PROMPT.md` | 49 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/evidence/00_inventory_reverification.md` | 39 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/00_DESIGN_GOVERNANCE_PROPOSAL.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md` | 80 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/00_DESIGN_GOVERNANCE_PROPOSAL.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/KICKOFF_PROMPT.md` | 43 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/00_DESIGN_GOVERNANCE_PROPOSAL.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/PROMPTS/02_AUTHOR_TEMPLATE_SPEC_AND_CORE.md` | 18 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/00_DESIGN_GOVERNANCE_PROPOSAL.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/evidence/00_inventory_reverification.md` | 22 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/00_DESIGN_GOVERNANCE_PROPOSAL.md` | `Design_Template_Kit/template/TEMPLATE_SPEC.md` | 39 (+1) | external-kit |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/01_DESIGN_ARTIFACT_TEMPLATES.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md` | 81 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/01_DESIGN_ARTIFACT_TEMPLATES.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/KICKOFF_PROMPT.md` | 43 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/01_DESIGN_ARTIFACT_TEMPLATES.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/PROMPTS/02_AUTHOR_TEMPLATE_SPEC_AND_CORE.md` | 18 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/01_DESIGN_ARTIFACT_TEMPLATES.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/evidence/00_inventory_reverification.md` | 23 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/02_CONFORMANCE_AND_ENFORCEMENT.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md` | 82 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/02_CONFORMANCE_AND_ENFORCEMENT.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/KICKOFF_PROMPT.md` | 43 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/02_CONFORMANCE_AND_ENFORCEMENT.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/PROMPTS/02_AUTHOR_TEMPLATE_SPEC_AND_CORE.md` | 18 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/02_CONFORMANCE_AND_ENFORCEMENT.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/PROMPTS/10_ANCHORING_KIT_ENFORCEMENT_AND_INSTALLER.md` | 16 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/02_CONFORMANCE_AND_ENFORCEMENT.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/evidence/00_inventory_reverification.md` | 24 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/02_CONFORMANCE_AND_ENFORCEMENT.md` | `Design_Template_Kit/template/TEMPLATE_SPEC.md` | 519 | external-kit |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/03_CLAUDE_MD_AND_DOC_LAYERING.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md` | 83 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/03_CLAUDE_MD_AND_DOC_LAYERING.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/KICKOFF_PROMPT.md` | 43 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/03_CLAUDE_MD_AND_DOC_LAYERING.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/PROMPTS/02_AUTHOR_TEMPLATE_SPEC_AND_CORE.md` | 18 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/03_CLAUDE_MD_AND_DOC_LAYERING.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/PROMPTS/10_ANCHORING_KIT_ENFORCEMENT_AND_INSTALLER.md` | 16 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/03_CLAUDE_MD_AND_DOC_LAYERING.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/evidence/00_inventory_reverification.md` | 25 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/BATCH_PLAN.md` | 107 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/STATE.md` | 101 | state |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/TASK_CONTEXT.md` | 162 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_SharedContracts/design-tokens/semantic-roles.json` | 3 | code |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/BATCH_PLAN.md` | 103 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/STATE.md` | 47 | state |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/TASK_CONTEXT.md` | 129 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/BATCH_PLAN.md` | 155 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/STATE.md` | 121 | state |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/TASK_CONTEXT.md` | 262 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_Workspace/implementation/System_Design_Architecture/STATE.md` | 45 (+1) | state |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md` | 84 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/KICKOFF_PROMPT.md` | 43 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/PROMPTS/02_AUTHOR_TEMPLATE_SPEC_AND_CORE.md` | 18 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/PROMPTS/03_TEMPLATE_VALIDATOR_AND_CANON_ROUNDTRIP.md` | 19 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `PlantLibrary_Workspace/methodology/Design_Template_Initiative/evidence/00_inventory_reverification.md` | 26 | pinned |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `Design_Template_Kit/examples/plantlibrary-field-ledger/design/CONFIGURATION.md` | 33 | external-kit |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `Design_Template_Kit/examples/plantlibrary-field-ledger/design/banned-colors.json` | 16 (+2) | external-kit |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `Design_Template_Kit/examples/plantlibrary-field-ledger/design/decisions/DECISION_RECORD_2026-07-10.md` | 16 (+1) | external-kit |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `Design_Template_Kit/tools/import-flat-tokens.mjs` | 456 (+2) | external-kit |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | `Design_Template_Kit/tools/lib/color-extra.mjs` | 6 | external-kit |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/STATE.md` | 11 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` | `PlantLibrary_Server/implementation/System_V1_Implementation/BATCH_PLAN.md` | 99 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` | `PlantLibrary_Server/implementation/System_V1_Implementation/STATE.md` | 16 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` | `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/STATE.md` | 12 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/STATE.md` | 11 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/BATCH_PLAN.md` | 19 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/STATE.md` | 12 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/TASK_CONTEXT.md` | 32 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/01_PRODUCT_VALUE_AUDIT.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/STATE.md` | 14 (+1) | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/01_PRODUCT_VALUE_AUDIT.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/TASK_CHECKLIST.md` | 23 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/BATCH_PLAN.md` | 153 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/STATE.md` | 135 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_Server/implementation/System_V1_Implementation/BATCH_PLAN.md` | 151 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_Server/implementation/System_V1_Implementation/STATE.md` | 130 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/BATCH_PLAN.md` | 76 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/STATE.md` | 80 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/BATCH_PLAN.md` | 154 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/STATE.md` | 79 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/BATCH_PLAN.md` | 217 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/STATE.md` | 153 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/BATCH_PLAN.md` | 117 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/STATE.md` | 118 | state |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/TASK_CHECKLIST.md` | 35 | live-package-anchor |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | `PlantLibrary_Workspace/implementation/System_V1_Implementation/TASK_CONTEXT.md` | 173 | live-package-anchor |
| `PlantLibrary_Workspace/prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/BATCH_PLAN.md` | 113 | live-package-anchor |
| `PlantLibrary_Workspace/prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | `PlantLibrary_PyApp/implementation/System_V1_Implementation/STATE.md` | 129 | state |
| `PlantLibrary_Workspace/prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/BATCH_PLAN.md` | 123 | live-package-anchor |
| `PlantLibrary_Workspace/prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/STATE.md` | 73 | state |
| `PlantLibrary_Workspace/prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/BATCH_PLAN.md` | 175 | live-package-anchor |
| `PlantLibrary_Workspace/prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/STATE.md` | 147 | state |
| `PlantLibrary_Workspace/prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | `PlantLibrary_Workspace/implementation/System_Tooling/STATE.md` | 6 (+1) | state |
| `PlantLibrary_Workspace/prompts/reference/SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | `PlantLibrary_AndroidApp/implementation/MVP/package/STATE.md` | 457 | state |
| `PlantLibrary_Workspace/prompts/reference/SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | `PlantLibrary_Workspace/docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_complete.csv` | 3 | code |

---

## 4. Enforcement surfaces per repository (item (c))

Measured 2026-09-15: `python` on `PATH` resolves to Python 3.12.10 (`%LOCALAPPDATA%\Programs\Python\Python312`), the `py`
launcher offers 3.14.6 and 3.12, and `python -m pytest` reports pytest 9.1.1 — for every session opened in any of the seven
folders, since `PATH` is per user, not per repo. No repository carries a `.gitattributes`.

| repo | pytest suite | own CI | `CLAUDE.md` / `AGENTS.md` | line endings of `.md` (CRLF / LF / mixed) | `.tmp\` ignored | deliverable roots the census would declare |
|---|---|---|---|---|---|---|
| SW_Development | none (only `scripts\harness\check_harness_parity.py`, `check_batch_packages.py`) | none | both, CRLF+LF mixed inside each | 3 / 6 / 2 | not ignored (`.gitignore` has `tmp_*/`, not `.tmp/`) | `repo-hygiene\`, `onboarding\`, a new `handovers\` |
| PlantLibrary_PyApp | yes — `tests\` (98 `test_*.py`), `pyproject.toml`, `.venv` | `.github\workflows\ci.yml` (ruff, mypy, pytest) | both, CRLF | 154 / 36 / 2 | yes (`.gitignore:16`) | `implementation\System_V1_Implementation\proposal\`; the package root's `planning\`/`handovers\` once created; `Documentation\` only if the gate opts it in (Q4) |
| PlantLibrary_Server | yes — `tests\` (10), `pyproject.toml`; runs in a `[test]`-extra env or the disposable Docker container (`CLAUDE.md`) | `ci.yml` (ruff, pytest, alembic) | both, LF | 23 / 24 / 0 | not ignored | `…\System_V1_Implementation\proposal\`; `docs\` only if opted in |
| PlantLibrary_SharedContracts | partial — `tests\contract_validation\test_examples_against_schemas.py` + `scripts\validate_contracts.py` (no `pyproject.toml`; `requirements.txt` in the test folder) | `ci.yml` (setup-python 3.12, `validate_contracts.py`, `generate_clients.py`) | none | 29 / 158 / 0 | not ignored | `…\System_V1_Implementation\proposal\` |
| PlantLibrary_Dashboard | no — Vitest + Playwright (`package.json`: `vitest run`, `playwright test`) | none in-repo | none | 58 / 17 / 0 | not ignored | `…\System_V1_Implementation\proposal\`; `docs\` only if opted in |
| PlantLibrary_AndroidApp | no — Gradle (`build.gradle.kts`) | none in-repo | none (three byte-identical skill mirrors: `.claude`, `.agents`, `.github`, 29 `.md` each, all git-tracked) | 18 / 38 / 0 | not ignored | `…\System_V1_Implementation\proposal\`; `docs\` only if opted in |
| PlantLibrary_Workspace | none | none | none | 205 / 193 / 1 (`README.md` mixed) | not ignored | `MVP_Reconciliation\`, `docs\` (+ the three `fable5_*` sets), `docs\proposals\` (+ `Repo_Restructure_MVP_V1_Split\`), `implementation\Server_VM_Setup\`, `…\System_Design_Architecture\proposal\`, `…\System_V1_Implementation\proposal\`, `prompts\` |

Consequence for the kit: a stdlib-only checker runs everywhere today with nothing installed; a pytest wrapper has a home in
PyApp and Server only (SharedContracts has one test module but no pytest configuration; the other three have no Python
suite). Per-repo CI exists in three submodules; the superproject and the other three have none.

---

## 5. Conventions catalogued, not folded into the dated rule

| convention | where | shape | disposition |
|---|---|---|---|
| batch-keyed validation evidence | every `implementation\<Package>\validation\` | `<BATCH>_<slug>.md`, date in the body; README manifests that name files before they exist (PyApp 4, Server 5, SharedContracts 3, AndroidApp 2 such names today) | catalogued; the kit exempts `validation\` from the dated rule and must not collide with pre-contracted names |
| evidence packs | `validation\evidence\<ROW>-<YYYYMMDD>-NN\NN_<name>.md` | compact date in the directory, numbered members | catalogued |
| id-prefixed product notes | Server `docs\`, Dashboard `docs\` | `<ROW-ID>_<snake_topic>.md`, type word as suffix (`_notes`, `_plan`, `_report`, `_design`) | catalogued; the four/five `_report`/`_PROPOSAL` files inside are candidates (§2) |
| row-anchored plans | AndroidApp `docs\` | `<topic>_plan.md`, row id in the H1, updated in place | catalogued (living docs) |
| ADRs | PyApp `Documentation\adr\` | `NNNN-kebab-title.md` + README index | catalogued |
| screen contracts | PyApp `GUI\screen_structures\` | `Screen_Structure_<id>.md` | catalogued |
| page contracts | SharedContracts `page-contracts\` | `PageContract_<page>.md`, `MobilePageContract_<page>.md` | catalogued |
| pipeline module docs | PyApp `app\**\<module>.md`, `.docpipeline\` | written by the documentation pipeline | generated |
| generated client docs | SharedContracts `generated\*\docs\<Model>.md` | openapi-generator output | generated |
| numbered chapter sets | Workspace `MVP_Reconciliation\`, `docs\fable5_*\`, both `proposal\` folders; frozen `system_description\` | `NN_UPPER_SNAKE.md`, reading order is load-bearing | candidates in the live folders — the gate decides per-file vs folder-level dating (Q5) |
| version pins by file name | SharedContracts `CONTRACT_VERSION.md`, `generated\CLIENT_MANIFEST.md`; Workspace `methodology\GUI_Improvement_Methodology\VERSION.md` and 28 `*_TEMPLATE.md` | cited by literal name from other repos and from the Design kit | never renamed |
| living package organs with non-schema names | Workspace `System_V1_Implementation\{SKILLS,SUITE_HANDOFFS,V1_IMPLEMENTATION_SEQUENCE}.md`, root `WORKSPACE_STATE.md`, `REPOSITORY_MAP.md`; frozen MVP packages' `IMPLEMENTATION.md`, `IMPLEMENTATION_PLAN.md`, `RESUME_VALIDATION_PROMPT.md` | | product / frozen; the per-repo decision record lists them as exempt by name |

---

## 6. What the census cannot decide — for gate G0

1. **Mixed folders.** PyApp `Documentation\` (27 candidates + 4 product specs, all June 2026, pre-MVP), Server `docs\` (4 of 15),
   Dashboard `docs\` (4 of 8), AndroidApp `docs\` (1 of 12) hold dated deliverables inside product-documentation folders. Renaming
   in place makes the folder a deliverable root; moving them into the package's `planning\` changes their home; leaving them
   catalogued keeps 36 non-compliant names. (Q4)
2. **Numbered chapter sets.** 35 Workspace candidates are chapters of five multi-file documents; a per-file rename destroys the
   reading order unless the number survives inside the topic. (Q5)
3. **Header dates.** 28 candidates were committed the day after the date they state; the Chapter-8 rule takes git. (Q5)
4. **Holds inside live packages.** Every `proposal\` file of the seven live packages is cited by its package's `STATE.md` and, in
   Workspace, by anchors; these are exactly the files the rule is for. Releasing them means editing the citing package files,
   which the onboarding track (steps `2a`/`2b`) is about to rewrite anyway. (Q5, and the sequencing against onboarding)
5. **TYPEs outside the enum.** `DECISION` (3 files: an accepted-deviation record, an approved design revision, the validation-
   methodology decisions), `REPORT` (2 desk-research reports), `GUIDE` (1 Proxmox setup runbook). (Q6)

---

## 7. Classification rules used (so M-8 can reproduce this census)

Longest matching prefix wins; a file named `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`,
`CONTEXT_INDEX.md`, `DRIVER_SCRIPT.md`, `SCOPE.md`, `README.md`, `INDEX.md`, `CLAUDE.md` or `AGENTS.md` in a candidate folder is
package-schema; the per-file exceptions are the ones §2 names in its notes and candidate tables.

| repo | prefix → class |
|---|---|
| SW_Development | root → candidate (`Todo.md` scratch, `CLAUDE.md`/`AGENTS.md` schema); `onboarding` → candidate; `repo-hygiene` → candidate |
| every submodule | root → product; `implementation` → schema; `implementation/MVP` → frozen; `implementation/System_V1_Implementation` → candidate; `…/proposal` → candidate; `…/validation` → evidence; `docs`, `app`, `tests`, `src`, `deploy`, `openapi`, `core`, `feature` → product |
| PyApp | `.docpipeline`, `app` → generated; `Documentation` → candidate (4 named files product); `Documentation/adr`, `GUI` → product (3 named files candidate); `implementation/Archive_PreMVP` → frozen |
| Server | `docs` → product (4 named `_report` files candidate) |
| SharedContracts | `generated` → generated; `api-examples`, `design-tokens`, `page-contracts`, `schemas`, `scripts`, `sync-contracts` → product |
| Dashboard | `references` → frozen; `docs` → product (4 named files candidate) |
| AndroidApp | `docs` → product (`security_token_storage_acceptance.md` candidate) |
| Workspace | `MVP_Reconciliation`, `docs`, `implementation/Server_VM_Setup`, `implementation/System_Design_Architecture`, `…/proposal`, `prompts` → candidate (named living files product; `manifests/REVIEW_LIST.md` generated); `implementation/System_Integration_MVP`, `implementation/System_Tooling`, `strategy`, `system_description` → frozen; `methodology` → pinned (`VALIDATION_METHODOLOGY.md` product) |

The scripted census itself was session scratch under `SW_Development\.tmp\` and is deleted with the session; step K-2 of the
runbook builds the census as a mode of the kit's checker from this table, and M-8 diffs that tool's output against §1.

