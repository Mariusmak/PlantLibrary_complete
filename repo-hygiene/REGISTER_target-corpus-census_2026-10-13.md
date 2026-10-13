# REGISTER — target corpus census, post-migration (2026-10-13)

*Produced by step `M-8` of `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` (§16, item 2), run as step
`B3-1` of the master rework program (`rework/PROMPTS_master-rework-runbook_2026-10-13.md` §3.5), measured 2026-10-13
over `C:\Programmierung\SW_Development` at `fda7524` and its six submodules, each clean on its own `main`. Measured
twice: first at the commits the gitlinks pin (`35ddc63`, `243b13e`, `86398fe`, `7795fc8`, `5d6410f`, `9669d19`), then —
because step `B4-2` committed one package edit in every suite during this session — at the heads in §1 (`B4-2`'s
commits). The `check` lines, the census tables, the walk and the citer grep are identical at both; §1 names the later
heads, which the gitlinks do not yet pin. Read-only: nothing renamed, moved, released or recorded in any repository. This is the
post-migration census; §2 is the diff against the pre-migration baseline `REGISTER_target-corpus-census_2026-09-15.md`
§1, every difference explained by a map row, a decision entry or a file the re-measurement found.*

**Method.** Three measurements, all re-run today, none copied from an audit:

1. The kit's checker, `python scripts/hygiene/repo_hygiene_check.py check` and `census`, run inside each of the seven
   repositories (kit `0.2.1`; `git status --porcelain` empty before and after in all seven). Its census sees the
   declared roots and the declared exempt trees only.
2. The baseline register's own walk (its §7, its exclusion list: `node_modules`, `.git`, `.venv`, `build`, `.tmp`, the four
   runtime mirrors `.claude` `.codex` `.agents` `.github`, `__pycache__`, `.gradle`, `.idea`, `dist`, `coverage`,
   `playwright-report`, `test-results`, the three tool caches, `graphify-out`, `.vite`), reproduced over tracked `.md`
   files with `git ls-files`, plus `git diff --name-status -M50%` from each baseline HEAD to today's HEAD for the delta.
   The walk reproduces the baseline exactly for the six submodules at their baseline HEADs (192, 47, 187, 75, 56, 399).
3. Every held name's citers, `git grep -n -I -F <basename> HEAD` in all seven repositories and in
   `C:\Programmierung\Design_Template_Kit` at `f08e588` (read-only, `--no-optional-locks`), basename bounded on the
   left; hits classified by the baseline's hold rule (§3 below).

---

## 1. Totals per repository — today

| repo | HEAD | files (walk) | checker census: files · compliant · candidates · exempt · held · set folders | exempt-tree files (frozen / pinned / legacy / generated) | `check` verdict |
|---|---|---|---|---|---|
| SW_Development (superproject) | `fda7524` | 48 | 41 · 34 · 0 · 4 · 3 · 0 | — | pass with holds — 0 violations, 3 held |
| PlantLibrary_PyApp | `e8b738d` | 200 | 6 · 2 · 0 · 3 · 1 · 0 | 125 (64 / 0 / 38 / 23) | pass with holds — 0 violations, 1 held |
| PlantLibrary_Server | `dd62b80` | 53 | 7 · 3 · 0 · 3 · 1 · 0 | 10 (10 / 0 / 0 / 0) | pass with holds — 0 violations, 1 held |
| PlantLibrary_SharedContracts | `93933ff` | 195 | 4 · 0 · 0 · 3 · 1 · 0 | 143 (9 / 0 / 0 / 134) | pass with holds — 0 violations, 1 held |
| PlantLibrary_Dashboard | `98c9b0a` | 83 | 6 · 2 · 0 · 3 · 1 · 0 | 51 (51 / 0 / 0 / 0) | pass with holds — 0 violations, 1 held |
| PlantLibrary_AndroidApp | `b780d20` | 64 | 4 · 0 · 0 · 3 · 1 · 0 | 22 (22 / 0 / 0 / 0) | pass with holds — 0 violations, 1 held |
| PlantLibrary_Workspace | `61dd9a2` | 429 | 30 · 7 · 0 · 12 · 10 · 3 | 327 (205 / 121 / 0 / 1) | pass with holds — 0 violations, 10 held |
| **total** | | **1072** | **98 · 48 · 0 · 31 · 18 · 3** | **678 (361 / 121 / 38 / 158)** | seven green, 18 held |

*Files (walk)* for the superproject is 47 tracked files plus the git-ignored `Todo.md` (the baseline's one `scratch` file,
still on disk); the walk counts it because the baseline's file-system walk did. The superproject row is measured
before the three `M-8` deliverables existed; in the `M-8` commit they make it 51 files by the walk and
`totals: 44 files, 37 compliant, 0 candidates, 4 exempt, 3 held, 0 set folders`, verdict unchanged. *Checker census* counts only declared
roots: "candidates 0" in every repository means no non-compliant, unheld name sits in a declared root.

Per-root census totals (verbatim `totals:` lines, abridged to the numbers):

| repo | root | files · compliant · candidates · exempt · held · set folders |
|---|---|---|
| SW_Development | `repo-hygiene` · `onboarding` · `handovers` · `rework` | 6·5·0·1·0·0 · 4·1·0·1·2·0 · 5·3·0·1·1·0 · 26·25·0·1·0·0 |
| each suite | `…/System_V1_Implementation/planning` · `proposal` · `handovers` | PyApp 2·1·0·1·0·0 · 3·1·0·1·1·0 · 1·0·0·1·0·0; Server 4·3·0·1·0·0 · 2·0·0·1·1·0 · 1·0·0·1·0·0; SharedContracts 1·0·0·1·0·0 · 2·0·0·1·1·0 · 1·0·0·1·0·0; Dashboard 3·2·0·1·0·0 · 2·0·0·1·1·0 · 1·0·0·1·0·0; AndroidApp 1·0·0·1·0·0 · 2·0·0·1·1·0 · 1·0·0·1·0·0 |
| PlantLibrary_Workspace | SV1 `planning` · `proposal` · `handovers`; SDA `planning` · `proposal` · `handovers` | 1·0·0·1·0·0 · 4·0·0·1·3·0 · 1·0·0·1·0·0; 1·0·0·1·0·0 · 6·0·0·1·5·0 · 1·0·0·1·0·0 |
| PlantLibrary_Workspace | `docs` · `docs/proposals` · `prompts` · `implementation/Server_VM_Setup` | 7·4·0·2·0·3 · 4·2·0·1·1·0 · 2·0·0·1·1·0 · 3·1·0·2·0·0 |

Workspace exempt trees by path: `system_description` 138, `implementation/System_Integration_MVP` 36,
`strategy/Cross_Platform_Strategy` 17, `implementation/System_Tooling` 14 (frozen, 205);
`methodology/GUI_Improvement_Methodology` 74, `methodology/Design_Template_Initiative` 47 (pinned, 121);
`docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/REVIEW_LIST.md` (generated, 1).

---

## 2. Diff against the 2026-09-15 register §1

### 2a. Files

| repo | register §1 | M-0 (2026-09-16) | today | delta | what the delta is |
|---|---|---|---|---|---|
| SW_Development | 11 | 18 | 48 | +37 | Baseline 11 = the 8 tracked at `6ecc155` + `Todo.md` + the 2 then-untracked `repo-hygiene/` files committed in `89d86ac` (`PROMPT_kit-bootstrap-session_2026-09-15.md`, `INDEX.md`; the register's 5 compliant and 4 schema rows). +7 to M-0 (the `M-0` row of map §1b: 2 registers and the runbook, `FINDING_kit-proof-floor…`, `handovers/INDEX.md`, `hygiene/` ×2). +30 since: `MATRIX_rename-map_2026-09-16.md` (`M-0`); `FINDING_kit-release-after-move-fails-record_2026-09-16.md` (`07e2f48`), `FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md` (`M-7`); the 26 files of the `rework/` root (`D-2026-10-13-01`, `R-0` onward); `scripts/harness/README.md` (`B7-1`, `a25b62e`). One move (`M-1`, map §3 `MV`): count unchanged |
| PlantLibrary_PyApp | 192 | 200 | 200 | +8 | the 8 of map §1b (`hygiene/` ×2, `SCOPE.md`, three root `INDEX.md`, `validation/KNOWN_FAILURES.md`, `validation/ONBOARDING_harness-port.md`); nothing since. Two moves (`M-2`): count unchanged |
| PlantLibrary_Server | 47 | 53 | 53 | +6 | the 6 of map §1b; nothing since. Three moves (`M-3`) |
| PlantLibrary_SharedContracts | 187 | 195 | 195 | +8 | the 8 of map §1b; nothing since |
| PlantLibrary_Dashboard | 75 | 83 | 83 | +8 | the 8 of map §1b; nothing since. Two moves (`M-5`) |
| PlantLibrary_AndroidApp | 56 | 64 | 64 | +8 | the 8 of map §1b; nothing since |
| PlantLibrary_Workspace | 399 | 411 | 429 | +30 | +12 to M-0 (map §1b). +18 since: the four general-root `INDEX.md` seeded at `M-7` (`D-2026-09-17-02`); 12 files of `methodology/GUI_Improvement_Methodology` 4.1.0 (six `*_TEMPLATE.md`, `PROMPTS/01a`, `06a`–`06d`); 2 of `methodology/Design_Template_Initiative` (`INITIATIVE_CLOSEOUT.md`, `evidence/16_pilot_acceptance_summary.md`). Seven file renames and three folder renames (`M-7`, 23 member files): count unchanged |
| **total** | **967** | **1024** | **1072** | **+105** | no file deleted in any repository (`git diff --diff-filter=D` empty for `.md`) |

### 2b. Candidates and their dispositions

The baseline's 103 candidates, each dispositioned once by map §13 and executed by `M-1`…`M-7`. "Moved" includes the
move-renames; the git diff counts are measured (`R` entries, similarity 82–100 %).

| repo | candidates | already compliant | renamed or moved (files) | set folders renamed (candidate members) | held today (file names) | exempt by decision | released at migration |
|---|---|---|---|---|---|---|---|
| SW_Development | 6 | 4 | 1 (`MV`) | 0 | 3 | 1 | 1 (moot) |
| PlantLibrary_PyApp | 31 | 0 | 2 | 0 | 4 (2 of them inside the legacy tree, moot) | 27 | 0 |
| PlantLibrary_Server | 5 | 0 | 3 | 0 | 2 | 0 | 2 (proposal 6, moved) |
| PlantLibrary_SharedContracts | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| PlantLibrary_Dashboard | 5 | 0 | 2 | 0 | 3 | 0 | 2 (proposal 6, moved) |
| PlantLibrary_AndroidApp | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| PlantLibrary_Workspace | 53 | 0 | 7 | 3 (22) | 15 + 1 set folder | 1 | 0 |
| **total** | **103** | **4** | **15** | **3 (22)** | **30 + 1 set folder** | **29** | **5** |

Reconciliation per repository (register → today):

- **SW_Development.** 6 = 4 compliant (`onboarding/` audit, register and runbook; `repo-hygiene/PROMPT_kit-bootstrap…`) +
  1 moved (`HANDOVER_batch-package-schema-drift_2026-09-15.md` → `handovers/`, `M-1`, `D-2026-09-16-03`) + 1 exempt
  (`IMPLEMENTATION_PLAN.md`, `GM` proposal 1, `D-2026-09-16-03`). Holds 4 → 3: `IMPLEMENTATION_PLAN.md` released moot
  (`D-2026-09-16-03`); the handover's hold released at its old path and re-declared at its new one (count unchanged).
  The checker's held count rose 2 → 3 at `M-1` because the moved handover entered a root.
- **PlantLibrary_PyApp.** 31 = 2 move-renames (`M-2`, `D-2026-09-16-04`) + 2 held in place (`PYAPP_V1_PROPOSAL.md`,
  `GUI/screen_structures/improvements.md`) + 27 exempt by the `Documentation` legacy tree (`D-2026-09-16-01`:132), two
  of which are also held (moot). Holds 4 → 4. The checker reports 1: the other three sit outside every root.
- **PlantLibrary_Server.** 5 = 1 move-rename (`SV-CONTRACT-01…`) + 2 move-renames released by proposal 6 (`release` lines
  `D-2026-09-17-02`:307–308) + 2 held. Holds 4 → 2.
- **PlantLibrary_SharedContracts.** 1 = 1 held. Holds 1 → 1.
- **PlantLibrary_Dashboard.** 5 = 2 move-renames released by proposal 6 (`D-2026-09-17-02`:308–309) + 3 held. Holds 5 → 3.
- **PlantLibrary_AndroidApp.** 2 = 2 held (one the `A-6` policy hold, Q5c). Holds 1 (+1 policy) → 2.
- **PlantLibrary_Workspace.** 53 = 7 renames (`M-7`) + 4 held free files + 1 exempt (`ServerSetUp_MVP.md`) + 41 set
  members: 22 in the three `fable5_*` sets renamed to dated set folders (23 files with the v2 set's `README.md`);
  4 in `docs/proposals/Repo_Restructure_MVP_V1_Split/`, **not renamed** (the `M-7` deviation, §2d); 7 in
  `MVP_Reconciliation/` (3 held, so the set stays, map §9a); 5 in the SDA `proposal/` set (all held); 3 in the SV1
  `proposal/` set (all held). Holds 15 → 15, plus the set folder held against the record's own line.

### 2c. Holds by group — register against today

| group (baseline §1b) | register | today | difference explained |
|---|---|---|---|
| onboarding runbook | 4 | 3 | `IMPLEMENTATION_PLAN.md` released moot (`GM` proposal 1, `D-2026-09-16-03`) |
| live package `STATE.md`/anchor | 10 + 1 policy | 11 | none released: onboarding `2a`/`2b` migrated every package but no citing `STATE.md`/anchor line changed (§3) |
| terminal `STATE.md` only | 5 | 1 | 4 released by `GM` proposal 6 at `M-3` (Server ×2) and `M-5` (Dashboard ×2); the Workspace handoff stays (live anchors also cite it) |
| pinned tree or Design kit | 8 | 8 | none; the Design Template Initiative closed 2026-10-12 without recording release words |
| code or config | 7 | 7 | none; no code citer changed |
| record (set folder) | — | 1 | new at `M-7`: `docs/proposals/Repo_Restructure_MVP_V1_Split/`, held against `D-2026-09-16-01`:161 (`handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md`) |
| **total** | **34 (35)** | **30 + 1** | 5 released, 1 set-folder hold added |

Checker-visible holds today: 18 (3 + 1 + 1 + 1 + 1 + 1 + 10). The other 12 held names sit outside every declared root
and appear only in their records: PyApp 3, Server 1, Dashboard 2, AndroidApp 1, Workspace 5 (`MVP_Reconciliation` ×3,
`MODEL_RECOMMENDATION.md`, `prompts/reference/SETUP_ANDROID…`), plus the Workspace set folder.

### 2d. Set folders, exempt trees, deviations

- **Set folders.** Map §13 planned 4 folder renames (26 candidate members); 3 were executed (22 members) and the fourth was
  reverted at `M-7` because kit `0.2.1` cannot retire an `exempt-tree` line whose path moves (`D-2026-09-17-03` item 2;
  `FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md`). The checker's Workspace `docs` root counts 3 set
  folders; map §9h anticipated 4. (Map §13's "26 members" counts the 22 plus the restructure set's 4.)
- **Frozen 361 → 361.** The six frozen trees and every MVP package are unchanged in count.
- **Pinned 107 → 121.** +14 in the two pinned methodology trees (§2a, Workspace).
- **Generated 140 → 158.** +18: PyApp's `exempt-tree: app` (generated, `D-2026-09-16-01`:143) counts the 18 module docs under
  `app/` that the register's §1 totals carried under product (its §7 rule table already named `app` generated); `.docpipeline` 5, SharedContracts `generated` 134 and the Workspace
  `REVIEW_LIST.md` 1 are as before.
- **Legacy 38 (new class).** PyApp `exempt-tree: Documentation` (legacy, `D-2026-09-16-01`:132, `G0` Q4 / map proposal 2):
  the 27 candidates, 4 product specs and the `adr/` notes the register had split across candidate and product.
- **Header-date divergences 28 → 28.** No divergent file was renamed onto its header date; the renamed ones took the
  git-created date (Q5a); the held ones carry the divergence in their target-on-release note.

---

## 3. Hold register — every held name, citer re-verified at HEAD

Hold-class citers only (live `STATE.md`, live package anchors, the onboarding runbook, a pinned tree, the Design kit, a code
or config file); the decision records, `INDEX.md` mapping tables, this track's and the rework program's own documents,
frozen packages' non-`STATE.md` files and product prose are not holds and are left out. The Workspace transcript
`docs/Fable5_Prompt_Improvements` (no extension) names many of these files; it is a never-edited transcript, not a hold.
*M-9 ready* means the release precondition of runbook §17 is met today: no hold-class citer remains, or the operator has
recorded the release (register `rework/REGISTER_operator-questions_2026-10-13.md`, answers of 2026-10-13 18:05 UTC).

| # | repo · held name | group | hold-class citers at HEAD (file:line) | M-9 ready |
|---|---|---|---|---|
| 1 | SW · `handovers/HANDOVER_batch-package-schema-drift_2026-09-15.md` | onboarding runbook | `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:5` | no — Q-A6S-02 (a): held until the onboarding runbook retires |
| 2 | SW · `onboarding/AUDIT_skill-assumptions_2026-09-15.md` | onboarding runbook (+ code) | runbook `:211,212,216,905`; PyApp `scripts/harness/regression_scope.py:33`, `scripts/harness/scope_cap.py:5` (code, not in the record) | no — as #1; the code citers keep it in place regardless |
| 3 | SW · `onboarding/REGISTER_package-census_2026-09-15.md` | onboarding runbook | runbook `:251,584,911` | no — as #1 |
| 4 | PyApp · `…/SV1/proposal/PYAPP_V1_PROPOSAL.md` | live package | PyApp `…/SV1/STATE.md:11` | **yes** — operator release, Q-A6P-03 (a) |
| 5 | PyApp · `Documentation/Design_Implementation_Claude.md` | pinned (moot, legacy tree) | Workspace `methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md:130` | no — pinned citer stands; moot while the legacy tree stands |
| 6 | PyApp · `GUI/screen_structures/improvements.md` | pinned | Workspace DTI `INITIATIVE_PROPOSAL.md:122`, `evidence/00_inventory_reverification.md:64,94`, `STATE.md:1994` | no — Q-A6P-05 (a): permanent |
| 7 | PyApp · `Documentation/plant_information_system_implementation_plan_v1.md` | code (moot, legacy tree) | PyApp `tests/services/test_ai_extraction_service.py:1` | no — code citer stands |
| 8 | Server · `…/SV1/proposal/SERVER_V1_PROPOSAL.md` | live package | Server `…/SV1/STATE.md:15` | **yes** — operator release, Q-A6V-02 (a) |
| 9 | Server · `docs/SV-B07_dashboard_endpoint_coverage_report.md` | code | Server `app/api/routes/dashboard_support.py:2`, `app/workers/tasks.py:9`; frozen MVP `STATE.md:49,182` (mapping-served) | no — code citers stand |
| 10 | SharedContracts · `…/SV1/proposal/SHAREDCONTRACTS_V1_PROPOSAL.md` | live package | SharedContracts `…/SV1/STATE.md:11` | **yes** — operator release, Q-A6C-04 (a) |
| 11 | Dashboard · `…/SV1/proposal/DASHBOARD_V1_PROPOSAL.md` | live package | Dashboard `…/SV1/STATE.md:14` | **yes** — operator release words, Q-A6D-02 (a) |
| 12 | Dashboard · `docs/WD-MOCKUP-UPGRADE_PROPOSAL.md` | pinned | Workspace DTI `METHODOLOGY_RECONCILIATION.md:24`, `INITIATIVE_PROPOSAL.md:131`, `evidence/00_inventory_reverification.md:73`; frozen MVP `STATE.md:403` | **yes** — operator release words, Q-A6D-03 (a) |
| 13 | Dashboard · `docs/WD-UX-10_mockup_parity_report.md` | pinned | as #12; frozen MVP `STATE.md:75` | **yes** — Q-A6D-03 (a) |
| 14 | AndroidApp · `…/SV1/proposal/ANDROIDAPP_V1_PROPOSAL.md` | live package (policy) | none | **yes** — no citer, and Q-A6A-02 (a) |
| 15 | AndroidApp · `docs/security_token_storage_acceptance.md` | code | AndroidApp `core/auth/src/main/java/com/plantlibrary/android/core/auth/AuthTokenStore.kt:27`; live `…/SV1/TASK_CHECKLIST.md:56`, `TASK_CONTEXT.md:350`; frozen MVP `STATE.md:371` | no — code and live anchors stand |
| 16 | Workspace · `…/SV1/proposal/00_V1_SYSTEM_PROPOSAL.md` | live package | Workspace SV1 `STATE.md:12`, `BATCH_PLAN.md:22`, `TASK_CONTEXT.md:34`; PyApp `STATE.md:12`; Server `BATCH_PLAN.md:110`, `STATE.md:16`; SharedContracts `STATE.md:12`; Dashboard `STATE.md:15` | no — Q-A6W-03 (a): the anchors stay |
| 17 | Workspace · `…/SV1/proposal/01_PRODUCT_VALUE_AUDIT.md` | live package | Workspace SV1 `STATE.md:14,83`, `TASK_CHECKLIST.md:25` | no — as #16 |
| 18 | Workspace · `…/SV1/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` | live package | Workspace SV1 `BATCH_PLAN.md:176`, `STATE.md:118`, `TASK_CHECKLIST.md:37`, `TASK_CONTEXT.md:184`; `BATCH_PLAN`/`STATE` of PyApp `:35/:136`, AndroidApp `:248/:153`, Dashboard `:157/:83`, Server `:165/:130`, SharedContracts `:86/:80` | no — as #16 |
| 19 | Workspace · `MVP_Reconciliation/02_GAPS_AND_DEFERRED_REGISTER.md` | live package | Workspace SV1 `BATCH_PLAN.md:23`; AndroidApp SV1 `BATCH_PLAN.md:35` | no — as #16 |
| 20 | Workspace · `MVP_Reconciliation/04_MVP_TO_V1_PROPOSAL.md` | live package | PyApp SV1 `TASK_CONTEXT.md:22` | no — as #16 |
| 21 | Workspace · `MVP_Reconciliation/05_NEXT_STEPS_AND_USAGE.md` | live package | Dashboard SV1 `BATCH_PLAN.md:12` | no — as #16 |
| 22 | Workspace · `prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | terminal `STATE.md` + live | PyApp SV1 `BATCH_PLAN.md:137`, `STATE.md:130`; Dashboard `:122`/`:77`; AndroidApp `:213`/`:147`; frozen `System_Tooling/STATE.md:6,13` (mapping-served) | no — live anchors stand |
| 23 | Workspace · `…/SDA/proposal/00_DESIGN_GOVERNANCE_PROPOSAL.md` | pinned | DTI `INITIATIVE_PROPOSAL.md:80`, `KICKOFF_PROMPT.md:43`, `PROMPTS/02_AUTHOR_TEMPLATE_SPEC_AND_CORE.md:18`, `evidence/00_inventory_reverification.md:22`; Design kit `template/TEMPLATE_SPEC.md:39,518` | no — pinned and Design-kit citers stand |
| 24 | Workspace · `…/SDA/proposal/01_DESIGN_ARTIFACT_TEMPLATES.md` | pinned | DTI `INITIATIVE_PROPOSAL.md:81`, `KICKOFF_PROMPT.md:43`, `PROMPTS/02:18`, `evidence/00:23` | no — as #23 |
| 25 | Workspace · `…/SDA/proposal/02_CONFORMANCE_AND_ENFORCEMENT.md` | pinned | DTI `INITIATIVE_PROPOSAL.md:82`, `KICKOFF_PROMPT.md:43`, `PROMPTS/02:18`, `PROMPTS/10_ANCHORING_KIT_ENFORCEMENT_AND_INSTALLER.md:16`, `evidence/00:24`; Design kit `template/TEMPLATE_SPEC.md:519` | no — as #23 |
| 26 | Workspace · `…/SDA/proposal/03_CLAUDE_MD_AND_DOC_LAYERING.md` | pinned | DTI `INITIATIVE_PROPOSAL.md:83`, `KICKOFF_PROMPT.md:43`, `PROMPTS/02:18`, `PROMPTS/10:16`, `evidence/00:25` | no — as #23 |
| 27 | Workspace · `…/SDA/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | code | SharedContracts `design-tokens/semantic-roles.json:3`; Design kit `tools/import-flat-tokens.mjs:456,466,468`, `tools/lib/color-extra.mjs:6`, `examples/plantlibrary-field-ledger/design/banned-colors.json:16,25,32`, `CONFIGURATION.md:33`, `decisions/DECISION_RECORD_2026-07-10.md:16,25`; live `STATE.md` SDA `:45,65`, PyApp `:102`, AndroidApp `:121`, Dashboard `:51`; live anchors PyApp `BATCH_PLAN.md:169`, `TASK_CONTEXT.md:162`, AndroidApp `:187`/`:262`, Dashboard `:97`/`:130`; DTI five lines | no — code citers stand |
| 28 | Workspace · `…/SDA/MODEL_RECOMMENDATION.md` | code | `docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_Workspace.csv:3`; DTI `DRIVER.md:7`, `INITIATIVE_PROPOSAL.md:97`, `KICKOFF_PROMPT.md:49`, `evidence/00:39` | no — code citer stands |
| 29 | Workspace · `docs/proposals/PlantLibrary_Full_Implementation_Update.md` | code | `…/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_complete.csv:2` | no — code citer stands |
| 30 | Workspace · `prompts/reference/SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | code | `…/manifests/MANIFEST_complete.csv:3`; AndroidApp frozen MVP `STATE.md:457` | no — code citer stands |
| 31 | Workspace · `docs/proposals/Repo_Restructure_MVP_V1_Split/` (set folder) | record | the record's own `hygiene/HYGIENE_DECISIONS.md:161` (`exempt-tree` for `manifests/REVIEW_LIST.md`); one-line path citers in the five suites' `implementation/README.md` (PyApp `:4,25`, AndroidApp `:16`, Dashboard `:19`, Server `:27`, SharedContracts `:19`) | no — kit patch `K-7` first (Q-G-06 open) |

**M-9 set (step `B3-4`): seven names** — #4, #8, #10, #11, #12, #13, #14. Of these only #14 has no hold-class citer; the
other six release on the operator's recorded words while their citer still names them, so `B3-4` writes the citing
`STATE.md` line change as a package decision (kickoff rule 4) and the release entry quotes the 2026-10-13 answer.
Line drift since the records were written (no effect on the hold): Workspace SV1 `BATCH_PLAN.md` cites #18 at `:176`
(record `:133`); SharedContracts `BATCH_PLAN.md` at `:86` (record `:85`).

---

## 4. Enforcement and kit pin per repository

| repo | pin (`hygiene/CONSUMED_HYGIENE.md`) | roots | modules | wrapper | CI | rule block | floor | hook | checker vs kit |
|---|---|---|---|---|---|---|---|---|---|
| SW_Development | kit `0.2.1`, SOURCE `fc5a14c`, pinned 2026-09-16 | 4 (`repo-hygiene`, `onboarding`, `handovers`, `rework`) | root-allowlist | no | `.github/workflows/repo-hygiene.yml` | on (`CLAUDE.md`, `AGENTS.md`, `@ 0.2.1`) | 1 | none | identical |
| PlantLibrary_Workspace | kit `0.2.1`, pinned 2026-09-17 | 10 | none | no | yes | on | 0 | none | identical |
| PlantLibrary_PyApp | kit `0.2.1`, pinned 2026-09-16 | 3 | none | yes (`tests/test_repo_hygiene_kit.py`) | yes | on | 0 | none | identical |
| PlantLibrary_Server | kit `0.2.1`, pinned 2026-09-17 | 3 | none | yes (`tests/test_repo_hygiene_kit.py`) | yes | on | 0 | none | identical |
| PlantLibrary_SharedContracts | kit `0.2.1`, pinned 2026-09-17 | 3 | none | no | yes | on | 0 | none | identical |
| PlantLibrary_Dashboard | kit `0.2.1`, pinned 2026-09-17 | 3 | none | no | yes | on | 0 | none | identical |
| PlantLibrary_AndroidApp | kit `0.2.1`, pinned 2026-09-17 | 3 | none | no | yes | on | 0 | none | identical |

"Identical": `scripts/hygiene/repo_hygiene_check.py` in each repository has the SHA-256 of the kit's
`checker/repo_hygiene_check.py` at `810733e` (tag `v0.2.1`, the kit's HEAD; prefix `b8485bab05c2`). The kit has not moved
since `K-6`, so no re-pin is owed today. Kit path in every pin: `C:/Programmierung/Repo_Hygiene_Template_Kit`.

---

## 5. Classification rules used

The baseline's §7 table, unchanged, for the walk; the checker's own classes (`compliant`, `held`, `index`, `exempt`, the
exempt-tree classes `frozen`, `pinned`, `legacy`, `generated`) for the census. Two method differences from the baseline,
both stated where they matter: the walk runs over tracked files (`git ls-files`) plus the one git-ignored scratch file
the baseline counted, where the baseline walked the file system; and citations are searched with `git grep` at `HEAD`
per repository (the superproject's `--recurse-submodules` returns superproject hits only), with the Design Template Kit
added as the eighth tree because the record names it as a citer class.
