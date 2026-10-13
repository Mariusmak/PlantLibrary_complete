# Corpus census — PlantLibrary_SharedContracts — lane A6 (read-only analysis, 2026-10-13)

Pin read: PlantLibrary_SharedContracts `main` @ `d43f7a2` (clean working tree, 23 commits, 604 tracked files, 214 tracked `.md`). Paths in the tables of §7 are relative to `PlantLibrary_SharedContracts/`; every citation in prose is written in full as `PlantLibrary_SharedContracts/<path>:line`. Citer counts are `git grep -l -F <name>` hits per repository, today, `generated/` excluded (the superproject count includes `.claude/` and `.codex/` skills, `onboarding/`, `repo-hygiene/`, `handovers/`).

## 0. Summary

- 214 tracked `.md`: 134 generated (exempt-tree `generated`, whole folder), 9 frozen MVP (exempt-tree `implementation/MVP`), 19 byte-identical skill/agent mirrors, 52 other documents (product docs, package schema files, instruction files, hygiene records, 3 `INDEX.md`). No candidate, no violation: `repo-hygiene: pass with holds — 0 violations, 1 held`.
- The one hold is `implementation/System_V1_Implementation/proposal/SHAREDCONTRACTS_V1_PROPOSAL.md` (cited by `STATE.md:11`); its release condition (onboarding 2a/2b migration) is met, so it waits only for the rolling step M-9. It does not need K-7.
- K-7 is still open (kit 0.2.1). It would bite this repository only if `implementation/MVP` or `generated` were moved, and nothing here needs that, so Q-G-06 (a) costs SharedContracts nothing. Recommendation: no `archive/` folder here; keep both exempt trees in place.
- No `design/` folder exists (`git ls-tree` HEAD shows `design-tokens/` only). Declaring it needs no new root, no allowlist entry (pin `Modules | none`) and no checker change; a prose decision entry suffices, plus an `exempt-tree: design/stacks — generated` line only if generated markdown is emitted there.
- Real obstacle to Q-G-01 (a) is ownership text: `CLAUDE.md:31-34` and `SCOPE.md:14-19` say design-system artifacts are owned by Workspace SDA and read-only here; both need amending first.
- `design-tokens/` is a flat layout (14 groups in `tokens.json`, no version key; `semantic-roles.json:5` carries `contract_version 1.2.0`) read by code in Dashboard, PyApp, AndroidApp and the Kit's importer/exporter by path: it must not move without a five-repository sweep.
- The three `platform-mapping-*.md` are stale against the 1.2.0 canon (banned `#16A34A` as worked example, generated token modules that do not exist, role layer "not shared").
- Drift GC-2431 confirmed, recorded not fixed: `CONTRACT_VERSION.md:7` is `1.2.0`, `generated/CLIENT_MANIFEST.md:3` cites `1.1.0`; owner `SC-SYNC-REGEN-01`.
- Legacy GC-7053 confirmed: `DRIVER_SCRIPT.md:17,38,50` still use `_ACT_STATE.md`; no `_ACT_STATE.md`, root `IMPLEMENTATION_PLAN.md` or `Todo.md` exists in this repository.
- Five questions, Q-A6C-01..05; none blocks anything outside B3 and B5.

## 1. Coverage

| Item | Status (read / partly read / not read) | Reason |
|---|---|---|
| `git ls-files -- '*.md'` full list (214) | read | listed with line counts; every file placed in one §7.1 row (row counts sum to 214) |
| CLAUDE.md, README.md, CONTRACT_VERSION.md, AGENTS.md | read | CLAUDE.md and README.md in full; AGENTS.md lines 1-20; CONTRACT_VERSION.md lines 1-30 plus changelog heads |
| hygiene/CONSUMED_HYGIENE.md, hygiene/HYGIENE_DECISIONS.md | read | in full; every directive line in §7.2 |
| implementation/System_V1_Implementation (README, SCOPE, STATE 1-30, DRIVER_SCRIPT 1-52, BATCH_PLAN 1-25, CONTEXT_INDEX 1-30, TASK_CHECKLIST rows, 3 INDEX, proposal 1-25, validation) | partly read | TASK_CONTEXT.md and the bodies of STATE.md, BATCH_PLAN.md, the proposal not read; only class and citers were needed |
| implementation/MVP (9 `.md`) | partly read | STATE.md head, handoff head, IMPLEMENTATION.md head and `implementation/README.md` read; bodies not read (frozen, class fixed by decision) |
| generated/ (134 `.md`) | partly read | CLIENT_MANIFEST.md 1-14, GENERATION_BLOCKERS.md, README.md, three generator READMEs heads; 128 per-model docs not read (generator output) |
| design-tokens/** (5 `.md`, 2 `.json`) | read | README, TOKEN_USAGE_NOTES lines 1-61, three mappings in full, tokens.json group keys and CHART group, semantic-roles.json head |
| page-contracts/** (19 `.md`) | partly read | both READMEs, EXCLUSIONS head, headings of one desktop and one mobile contract; the other contracts line-counted and citer-counted only |
| openapi/README.md, openapi/changelog.md | partly read | README in full, changelog first entry |
| .claude/ and .codex/ mirrors (19 `.md` + 3 agent `.toml` + 2 `.ps1`) | partly read | compared with the superproject working tree by `cmp` (all identical); bodies not read |
| Citers across superproject, onboarding/, repo-hygiene/, handovers/, Workspace, Server, Dashboard, PyApp, AndroidApp | read | `git grep -l -F` per basename; counts exact, file lists shown only for the code citers |
| MATRIX_rename-map §6, FINDING K-7, KIT_SPEC §1.4-1.8, §6, §7, kickoff §1, §2, §4 | read | per the brief |
| Checker `check` and `census` | read | both executed read-only (§7.4) |
| Design_Template_Kit references to SharedContracts | partly read | grep of `tools/` and the example folder listing only |

## 2. Findings

- **F-A6C-01 (check green, one hold).** `check` prints `repo-hygiene: pass with holds — 0 violations, 1 held`; the single `held:` line is `SHAREDCONTRACTS_V1_PROPOSAL.md`. `census`: 4 files in roots, 0 compliant, 0 candidates, 3 exempt (the `INDEX.md`s), 1 held. Evidence: `PlantLibrary_SharedContracts/hygiene/HYGIENE_DECISIONS.md:134`.
- **F-A6C-02 (hold is releasable now, by M-9).** The hold group is live-package (Q5c); the release condition "onboarding 2a/2b migrated the package" is met: `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/SCOPE.md:1-4` exists and the checklist is the 15-column schema (`TASK_CHECKLIST.md:4`). Citers to sweep or serve by table: `STATE.md:11`, package `README.md:6,55`, `proposal/INDEX.md`, the decision record. Citers that must not be edited stay served by the Renamed table: Workspace `docs/Fable5_Prompt_Improvements` (transcript), Workspace's held `00_V1_SYSTEM_PROPOSAL.md:223`, the superproject track files. Target on release: `PROPOSAL_sharedcontracts-v1_2026-07-10.md` (git-created 2026-07-10, header 2026-07-09; `HYGIENE_DECISIONS.md:134`). A `held-name` release works in kit 0.2.1 (K-6), so K-7 is not needed.
- **F-A6C-03 (exempt trees and K-7).** Two `exempt-tree` lines: `PlantLibrary_SharedContracts/hygiene/HYGIENE_DECISIONS.md:114` (`implementation/MVP`, frozen) and `:115` (`generated`, generated). Under kit 0.2.1 each path must exist for ever; a move fails `record` permanently (`handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md`, "Why" and "Who else it blocks", which names `generated/` and every frozen `implementation/MVP/` explicitly). `PlantLibrary_SharedContracts/implementation/README.md` also states the MVP package is terminal ("never bound, never migrated, never edited").
- **F-A6C-04 (exempt-name lines are inert).** `PlantLibrary_SharedContracts/hygiene/HYGIENE_DECISIONS.md:121-123` exempt `CONTRACT_VERSION.md`, `generated/CLIENT_MANIFEST.md`, `openapi/changelog.md`; none sits in a declared root, so the checker never evaluates them. They are map records, harmless. The real protection is the citer base: `CONTRACT_VERSION.md` has 15 SC, 42 Workspace, 4 Server, 1 PyApp and 7 superproject citers.
- **F-A6C-05 (version drift GC-2431, recorded).** `PlantLibrary_SharedContracts/CONTRACT_VERSION.md:7` = `1.2.0` (entry at `:19`, 2026-07-10); `PlantLibrary_SharedContracts/generated/CLIENT_MANIFEST.md:3` cites `1.1.0`, 27 paths, SHA-256 `eff91162…` (`:4`). Known and documented at `PlantLibrary_SharedContracts/CLAUDE.md:25-27`; owner `SC-SYNC-REGEN-01` (`implementation/System_V1_Implementation/TASK_CHECKLIST.md`, status `todo`, waits Server `SV-OPENAPI-01`). Not fixed here. A fix needs a regeneration, which this program does not do: it is a row for the deferred-validation register.
- **F-A6C-06 (legacy sequencer GC-7053; no stale root sequencer here).** `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/DRIVER_SCRIPT.md:7` declares `_ACT_STATE.md` deprecated while `:17` (state cache), `:38` (read it) and `:50` (append to it) still instruct it. `implementation/System_V1_Implementation/README.md:39-42` and `PlantLibrary_SharedContracts/README.md:25` still tell a fresh session to execute or use `DRIVER_SCRIPT.md`. Mitigation exists: process note `DRIVER_SCRIPT.md:3-10`, legacy marker `SCOPE.md:3-4`, `CLAUDE.md:42-46`. No `_ACT_STATE.md` is tracked or on disk; no root `IMPLEMENTATION_PLAN.md`, `Todo.md` or `WORKSPACE_STATE.md` exists (the only `IMPLEMENTATION_PLAN.md` is the frozen `implementation/MVP/package/IMPLEMENTATION_PLAN.md`).
- **F-A6C-07 (checklist behind reality).** `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/TASK_CHECKLIST.md:24` still has `SC-V1-DOC-01` at `todo` ("CLAUDE.md + AGENTS.md (suite root, new)") although both files exist (created by `c51c5ff`, `HYGIENE_DECISIONS.md:75-78`). A status flip is a plan-batch/STATE decision, not a hygiene act; recorded for the runbook.
- **F-A6C-08 (no design/ folder).** `git ls-tree -d --name-only HEAD` lists `.claude .codex .github api-examples design-tokens generated hygiene implementation openapi page-contracts schemas scripts sync-contracts tests`.
- **F-A6C-09 (ownership text blocks Q-G-01 (a)).** `PlantLibrary_SharedContracts/CLAUDE.md:31-34`: design-system artifacts (`design-tokens/` schema, roles, generator; `DESIGN_SYSTEM.md`; component/pattern contracts; terminology) are owned by `../PlantLibrary_Workspace/implementation/System_Design_Architecture/` and read-only here. `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/SCOPE.md:14-19` says the same and `CONTEXT_INDEX.md` (source map) repeats it. A Configuration under `design/` here needs these three statements amended as a plan-batch decision recorded in `STATE.md` (program rule 4).
- **F-A6C-10 (token consumers are code).** `PlantLibrary_Dashboard/scripts/generate-theme.mjs:4,7,31` reads `../PlantLibrary_SharedContracts/design-tokens/tokens.json` and cites `platform-mapping-web.md`; `PlantLibrary_Dashboard/tests/theme/tokens.test.ts` cites the mapping; `PlantLibrary_PyApp/scripts/check_token_drift.py` and `DESIGN.md` cite `design-tokens/`; `PlantLibrary_AndroidApp/core/design/src/main/java/com/plantlibrary/android/core/design/Color.kt`, `Theme.kt`, `Type.kt` and `app/src/main/res/values/themes.xml` cite `platform-mapping-android.md` / `design-tokens/`; Design_Template_Kit `tools/import-flat-tokens.mjs:25` and `tools/export-flat-tokens.mjs:20` hard-code `SW_Development/PlantLibrary_SharedContracts/design-tokens`; `.claude/skills/design-adoption/SKILL.md:31-34` lists the four paths. In kit terms these are "cited by code" holds: `design-tokens/` must not move or rename without a sweep across five repositories and the Kit.
- **F-A6C-11 (no generated token artifacts exist).** `git ls-files generated | grep -i token` returns nothing. Yet `PlantLibrary_SharedContracts/design-tokens/platform-mapping-web.md:5-8` promises CSS variables and `generated/typescript/tokens.ts`, and `platform-mapping-android.md:5` promises `generated/kotlin/...Tokens.kt`, both from `scripts/generate_clients.py`, which generates API clients only (`CLAUDE.md:7-12`). Every client hand-mirrors the values (`CONTRACT_VERSION.md` 1.2.0 entry: clients that hand-mirror token values are out of sync until their reconciliation tasks). This is the gap Kit stack emission is meant to close (input for A4/B5).
- **F-A6C-12 (stale content in the platform mappings and README).** `PlantLibrary_SharedContracts/design-tokens/platform-mapping-web.md:7` uses `--primary-600: #16A34A;` as its worked example; `design-tokens/TOKEN_USAGE_NOTES.md:27-28` bans `#16A34A` for the accent (1.2.0 `PRIMARY.600` is `#2A7A30`). `platform-mapping-web.md:5,16` cites `03_SHARED_DESIGN_SYSTEM_STRATEGY.md`, which is not a tracked file in Workspace. `platform-mapping-android.md:5` and `platform-mapping-python.md:9` say the composed role layer is not yet shared, which `design-tokens/semantic-roles.json` (1.2.0, P-DS-05) contradicts. `design-tokens/README.md:3` still says the JSON is exported from PyApp's `app/gui/design_tokens.py`, while `platform-mapping-python.md:5` says the direction should invert. Note: `#16A34A` correctly remains as chart `series_1`/`primary` at `design-tokens/tokens.json:157,161` (the categorical order is explained at `TOKEN_USAGE_NOTES.md:54-56`), so a naive banned-colour sweep would false-positive there.
- **F-A6C-13 (hand-authored files inside the generated class).** Of the 134 `.md` under `generated/`, 128 are per-model docs (64 `kotlin/docs`, 64 `typescript/docs`), 2 are generator READMEs (`python/`, `kotlin/`), and four are hand-written: `generated/README.md` (11 lines; `:11` still says batch `SC-B06` "is the active gate"), `generated/GENERATION_BLOCKERS.md`, `generated/typescript/README.md` (3 lines) and `generated/CLIENT_MANIFEST.md`. The `generated` exempt-tree covers all of them (`HYGIENE_DECISIONS.md:115`), so the stale `SC-B06` sentence is invisible to the checker; CI's drift gate (`PlantLibrary_SharedContracts/.github/workflows/ci.yml:39`, `git diff --exit-code -- generated/`) polices regeneration only.
- **F-A6C-14 (page contracts: per-page, versionless, cited by code).** `page-contracts/desktop-web/` holds 11 `PageContract_<page>.md`; `page-contracts/android/` holds 5 `MobilePageContract_<page>.md` plus `EXCLUSIONS.md`. A loop over all 19 found no version line. They are cited by Dashboard (30 files, e.g. `src/app/Shell.tsx`, `src/app/routes.ts`), AndroidApp (9 files, e.g. `feature/plants/src/main/java/com/plantlibrary/android/feature/plants/PlantDetailScreen.kt`) and Workspace (9). Not renamed, not moved.
- **F-A6C-15 (validation README names files that do not exist).** `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/validation/README.md` lists `SC1-B00_regen_report.md`, `SC1-B01_ci_evidence.md`, `SC1-B02_regen_report.md`, none tracked; D-2026-09-16-01 already forbids later deliverables from taking those names. The only evidence file is `validation/SC1-B01_tooling_ci_doc_hygiene.md`.
- **F-A6C-16 (mirrors identical).** All 22 non-script files under `.claude/` and `.codex/` (md and toml) match the superproject working tree byte for byte (`cmp`); the `plan-batch` copy is 247 lines, behind the Conductor's 1.5.1 per kickoff §1. `PlantLibrary_SharedContracts/AGENTS.md:6-10` states the Codex mirrors are tolerated copies (Q-G-09 freeze applies).
- **F-A6C-17 (nothing archive-like here).** There is no `Archive_PreMVP`, no `docs/` tree, no `Todo.md`, no content in `handovers/` (its `INDEX.md` table is empty), no loose reports. The only archived-in-place material is `implementation/MVP/` and the generated tree, both already exempt where they are.

## 3. Candidates

| ID | Source path @ pin | What | Verdict | Target repo and path | Lane (B3, B5) | Q id or — |
|---|---|---|---|---|---|---|
| RC-A6C-01 | `PlantLibrary_SharedContracts/design-tokens/tokens.json` + `semantic-roles.json` @ d43f7a2 | the 1.2.0 field-ledger canon in flat layout (14 groups + role layer) | reuse as the import source for the Configuration (Kit `tools/import-flat-tokens.mjs` already round-trips it); do not move | PlantLibrary_SharedContracts `design/` (new Configuration), generated from `design-tokens/` | B5 | Q-G-01, Q-A6C-02 |
| RC-A6C-02 | `PlantLibrary_SharedContracts/design-tokens/TOKEN_USAGE_NOTES.md` @ d43f7a2 | per-group rules, rationale, conduct rules, WCAG measurements | reuse; the Kit example's `design/conduct-rules.md` is the matching home; original stays as flat-layout companion | `design/conduct-rules.md` (derived); original unchanged | B5 | Q-G-01 |
| RC-A6C-03 | `PlantLibrary_SharedContracts/design-tokens/platform-mapping-{web,android,python}.md` @ d43f7a2 | per-platform consumption notes (stale, F-A6C-11/12) | rewrite or supersede once B5 knows which stacks are emittable; until then hold | `design/` stack documentation; originals kept while the Dashboard generator cites `platform-mapping-web.md` | B5 | Q-A6C-05 |
| RC-A6C-04 | `PlantLibrary_SharedContracts/page-contracts/**` @ d43f7a2 | 11 desktop + 5 mobile per-page contracts and `EXCLUSIONS.md` | keep in place; B5 links them from the design gate as the page inventory | stays; referenced from `design/` conformance | B5 | — |
| RC-A6C-05 | `PlantLibrary_SharedContracts/.github/workflows/ci.yml:39` + `scripts/generate_clients.py` readiness mode @ d43f7a2 | regenerate-then-diff drift gate over `generated/` | reuse the pattern for emitted design stack artifacts | PlantLibrary_SharedContracts `.github/workflows/` (new job) | B5 | Q-A6C-02 |
| RC-A6C-06 | `PlantLibrary_SharedContracts/hygiene/HYGIENE_DECISIONS.md:115` + `generated/CLIENT_MANIFEST.md` @ d43f7a2 | generated-class exempt tree plus a manifest pinning tool versions and hashes | reuse the shape for `design/stacks` (class `generated`) and a `DESIGN_VERSION.md` pin by name | PlantLibrary_SharedContracts `hygiene/HYGIENE_DECISIONS.md` (new entry) | B3 | Q-A6C-01 |
| RC-A6C-07 | `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/proposal/SHAREDCONTRACTS_V1_PROPOSAL.md` @ d43f7a2 | the held proposal | rename on release (hold condition met) | same root, `PROPOSAL_sharedcontracts-v1_2026-07-10.md`, with a `release` line | B3 | Q-A6C-04 |
| RC-A6C-08 | `PlantLibrary_SharedContracts/.claude/**`, `.codex/**`, `CLAUDE.md`, `AGENTS.md` @ d43f7a2 | instruction files and byte-identical skill mirrors | refresh from the superproject when the mirror lane moves the skills (plan-batch 1.4.0 to the Conductor level); rule block never hand-edited | same paths (mirror lane) | B3 | Q-G-09 |
| RC-A6C-09 | `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/DRIVER_SCRIPT.md` @ d43f7a2 | legacy driver with `_ACT_STATE.md` steps (F-A6C-06) | keep as legacy; the smallest closure of GC-7053 is a one-line banner, not a rewrite | same file | B3 | Q-A6C-03 |

## 4. Questions for the operator

| ID | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A6C-01 | Does SharedContracts get an `archive/` folder? | (a) No `archive/`; `implementation/MVP` and `generated` stay under their existing `exempt-tree` lines; any future retirement is a new in-place `exempt-tree` line. (b) Create `archive/` declared `exempt-tree: legacy` and move `implementation/MVP` into it. (c) Same as (b) but only after K-7 is released. | Nothing here is a dated deliverable to retire; (b) would fail `record` for ever under kit 0.2.1 (F-A6C-03); (c) buys a folder rename for history nobody edits. | B3's SharedContracts archive row only |
| Q-A6C-02 | If the Design Configuration lands in `design/` here (Q-G-01 (a)), what is the source of truth for the flat `design-tokens/`? | (a) `design/` becomes the source; `design-tokens/` stays at its path as the emitted flat view (Kit `tools/export-flat-tokens.mjs`) until Dashboard, PyApp and AndroidApp move to stack artifacts, then a separate step retires it. (b) `design-tokens/` stays the source and `design/` is re-imported from it each time. (c) Move `design-tokens/` into `design/` now. | Five repositories and the Kit read `design-tokens/` by path (F-A6C-10); (a) keeps those paths working while authority moves; (c) breaks them all at once. | B5's design-landing step and the hygiene wording of any `design/` entry |
| Q-A6C-03 | Close GC-7053 (`_ACT_STATE.md` lines in the legacy driver) in this rework? | (a) Leave `DRIVER_SCRIPT.md` as is (process note at `:3-10` and `SCOPE.md:3-4` already govern it) and fix only the two README sentences that still send a fresh session to it (`README.md:25`, package `README.md:39-42`). (b) Also add a one-line banner beside lines 17, 38, 50. (c) Leave everything. | Decision D7 chose the legacy marker over amending the file; the README sentences are the only live instruction pointing at the wrong file. | B3 package-legacy row |
| Q-A6C-04 | Release the `SHAREDCONTRACTS_V1_PROPOSAL.md` hold now? | (a) Yes, in the next rolling M-9 batch for this repository (`git mv`, `release` line, sweep `STATE.md:11` and the package README, Renamed row). (b) Keep the hold until the SC1 package closes. | The release condition is met (F-A6C-02); the hold costs a permanent `held:` line. Independent of K-7. | M-9 for SharedContracts |
| Q-A6C-05 | What happens to `platform-mapping-*.md` and `design-tokens/README.md` (stale, F-A6C-11/12)? | (a) Leave until B5 decides the emittable stacks, then replace or supersede them in one step; the defects are recorded here. (b) Correct the four files now (banned colour, role-layer sentence, missing generator, README ownership line). | Their content depends on which stack artifacts will exist; an edit now would be redone, and the Dashboard generator cites `platform-mapping-web.md`. | B5 documentation row only |

## 5. Reusable things this brief did not name

- `scripts/validate_contracts.py` with `tests/contract_validation/` is a compact "examples against schemas" check; its shape is a model for a Configuration validity check inside this repository (static, no stack).
- The banned greens (`#22C55E`, `#16A34A`, `#4ADE80`) and the chart exemption are written at `PlantLibrary_SharedContracts/design-tokens/TOKEN_USAGE_NOTES.md:27-28,54-56`; the Kit's `banned-colors.json` already mirrors them, and any sweep must carry the chart exemption over (F-A6C-12).
- `.github/workflows/repo-hygiene.yml` already runs the checker on every push in this repository; a design emission-drift job can sit beside `ci.yml` without touching it.
- `generated/CLIENT_MANIFEST.md` is a proven pin shape (source, hash, tool versions, readiness per consumer) for a future `design/` emission manifest.
- `.gitignore` already ignores `generated/**/build`, `.gradle`, `.kotlin` and `.tmp/`; a `design/` stack compiled by consumers needs equivalent build-output lines.
- The superproject `sync-contracts` skill cites `CONTRACT_VERSION.md`, `generated/CLIENT_MANIFEST.md` and `generated/GENERATION_BLOCKERS.md` by name (`.claude/skills/sync-contracts/SKILL.md`); renaming any of them breaks the skill.

## 6. Claims to verify

1. The drift is exactly lines 7 and 3: `sed -n 7p PlantLibrary_SharedContracts/CONTRACT_VERSION.md` prints `` `1.2.0` `` and `sed -n 3p PlantLibrary_SharedContracts/generated/CLIENT_MANIFEST.md` contains `1.1.0` and `27 paths`.
2. There is no design folder and no generated token module: `git -C PlantLibrary_SharedContracts ls-tree -d --name-only HEAD` has no `design` entry, and `git -C PlantLibrary_SharedContracts ls-files generated | grep -i token` prints nothing.
3. The allowlist is off and only two exempt trees exist: `sed -n 15p PlantLibrary_SharedContracts/hygiene/CONSUMED_HYGIENE.md` prints `| Modules | none |`, and `grep -n '^- exempt-tree' PlantLibrary_SharedContracts/hygiene/HYGIENE_DECISIONS.md` prints exactly lines 114 and 115.

## 7. Disposition and hygiene detail

### 7.1 Disposition table

Class legend: live; superseded (by what); archive; frozen / pinned / generated (the exempt-tree class); mirror (byte-identical copy); index. Citer keys: SC = this repository, SP = superproject, WS = Workspace, SV = Server, DB = Dashboard, PY = PyApp, AN = AndroidApp.

| File or folder (n) | Class | Citers | Hold / exemption (D-id) and release | Disposition (keep / archive to <path> / retire / hold) | Reason |
|---|---|---|---|---|---|
| `README.md` (1, 38 lines) | live, partly stale (`:25` points sessions at DRIVER_SCRIPT.md) | basename generic | none | keep | root description; fix `:25` under Q-A6C-03 |
| `CLAUDE.md` (1, 108 lines), `AGENTS.md` (1, 47) (2) | live instruction files (rule block inside markers) | read by every session and by Conductor intake | rule block installed by kit (D-2026-09-16-01, -02, D-2026-09-17-01); never hand-edited | keep | ownership text at `CLAUDE.md:31-34` to amend under Q-G-01 (a) |
| `CONTRACT_VERSION.md` (1, 95) | pinned (bundle semver `1.2.0`) | SC 15, SP 7 (sync-contracts skill, onboarding, repo-hygiene), WS 42, SV 4, PY 1 | exempt-name `HYGIENE_DECISIONS.md:121`; never renamed; no release | keep | version pin by file name from five repos and two skills |
| `design-tokens/README.md` (1, 3) | live, stale (F-A6C-12) | basename generic | catalogued, not declared (D-2026-09-16-01) | hold | rewrite waits for B5 (Q-A6C-05) |
| `design-tokens/TOKEN_USAGE_NOTES.md` (1, 95) | live (1.2.0 rules, P-DS-01..10) | SC 2, SP 3 (design-adoption skill + census), WS 12, DB 1, PY 2, AN 1 | catalogued, not declared | keep | binding rationale for the canon; source for RC-A6C-02 |
| `design-tokens/platform-mapping-web.md` (1, 20) | live but stale (banned-colour example, non-existent `tokens.ts`) | SC 1, WS 4, DB 6 (incl. `scripts/generate-theme.mjs`, `tests/theme/tokens.test.ts`) | catalogued, not declared | hold | cited by Dashboard code; supersede under B5 (Q-A6C-05) |
| `design-tokens/platform-mapping-android.md` (1, 18) | live but stale (non-existent `Tokens.kt`, role layer "not shared") | SC 2, WS 7, AN 9 (incl. `Color.kt`, `Theme.kt`, `Type.kt`) | catalogued, not declared | hold | as above |
| `design-tokens/platform-mapping-python.md` (1, 16) | live but stale (role layer "Python-only", direction of truth) | SC 2, WS 2 | catalogued, not declared | hold | as above |
| `hygiene/CONSUMED_HYGIENE.md` (1, 27), `hygiene/HYGIENE_DECISIONS.md` (1, 260) (2) | pinned record (append-only) | the checker; kickoff rule 3 | not a root | keep | never edited retroactively |
| `implementation/README.md` (1, 35) | live package index, cites MVP as terminal | SC 1 | none | keep | states V1 path "never moves" and MVP is read-only |
| `implementation/System_V1_Implementation/` schema files: `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`, `SCOPE.md`, `CONTEXT_INDEX.md`, `README.md` (7) | live package schema | Conductor intake; basenames cited in every suite; `SCOPE.md` SC 8 | none (the package folder is not a root) | keep | progress truth = checklist row status (`CLAUDE.md:42-46`); `TASK_CHECKLIST.md:24` stale status (F-A6C-07) |
| `implementation/System_V1_Implementation/DRIVER_SCRIPT.md` (1, 69) | superseded by the run-batch skill (legacy, `SCOPE.md:3-4`) | SC 15, WS 81, SV 21, DB 16, PY 16, AN 19, SP 11 (basename) | none; legacy in every package (kickoff §1) | keep | cited by package READMEs and every census; `_ACT_STATE.md` lines 17/38/50 (GC-7053) left by D7; Q-A6C-03 |
| `implementation/System_V1_Implementation/planning/INDEX.md`, `handovers/INDEX.md` (2) | index | the checker | declared roots (planning standard, handovers date-anywhere) | keep | tables empty by design; B3 adds lines for new deliverables |
| `implementation/System_V1_Implementation/proposal/INDEX.md` (1) | index | the checker | declared root (proposal standard) | keep | carries the held row |
| `implementation/System_V1_Implementation/proposal/SHAREDCONTRACTS_V1_PROPOSAL.md` (1, 87) | live proposal, held | SC 4 (`STATE.md:11`, package `README.md:6,55`, record, INDEX), SP 3 (track files), WS 2 (held `00_V1_SYSTEM_PROPOSAL.md:223`, transcript) | held-name `HYGIENE_DECISIONS.md:134` (D-2026-09-16-01, kept by D-2026-09-17-02); release: onboarding 2a/2b (met), then M-9, with `release` in the commit of the `git mv` | hold, then rename to `implementation/System_V1_Implementation/proposal/PROPOSAL_sharedcontracts-v1_2026-07-10.md` at M-9 | F-A6C-02, Q-A6C-04 |
| `implementation/System_V1_Implementation/validation/` (2: `README.md`, `SC1-B01_tooling_ci_doc_hygiene.md`) | live batch-keyed evidence (catalogued, not a root) | SC 2, SP 1 | none | keep | README names 3 files that do not exist (F-A6C-15) |
| `implementation/MVP/package/` (8) + `implementation/MVP/handoffs/Generated_Client_Handoff.md` (1) = 9 | frozen | SC (root `README.md`, `implementation/README.md`), WS 1 (handoff) and the Workspace restructure manifest; the 8 basenames are cited suite-wide | exempt-tree `HYGIENE_DECISIONS.md:114` (D-2026-09-16-01); no release defined; a move is blocked by K-7 | keep (in place) | terminal evidence, never bound or edited; Q-A6C-01 |
| `openapi/README.md` (1, 3) | live product doc | folder-local | catalogued | keep | one-paragraph folder note |
| `openapi/changelog.md` (1, 33) | pinned by name (export changelog) | SC 8, SV 1, WS 2, SP 2 | exempt-name `HYGIENE_DECISIONS.md:123`; never renamed | keep | version history of the export snapshot |
| `page-contracts/desktop-web/` (11 `PageContract_*.md` + README) (12) | live product contracts (no version line) | DB 30 files incl. `src/app/Shell.tsx`, `src/app/routes.ts`; WS 9; SC 15; AN 4 (plants) | catalogued, not declared | keep | cited by code; B5 reads as page inventory |
| `page-contracts/android/` (5 `MobilePageContract_*.md` + `EXCLUSIONS.md` + README) (7) | live product contracts | AN 9 (incl. `feature/plants/.../PlantDetailScreen.kt`); WS 7 (`EXCLUSIONS.md`); SC 5 | catalogued, not declared | keep | as above |
| `api-examples/README.md`, `schemas/README.md`, `scripts/README.md`, `sync-contracts/README.md`, `tests/contract_validation/README.md` (5) | live product docs | folder-local | catalogued | keep | 3-6 lines each; `scripts/README.md` points to the archived `run_next_batch.py` |
| `generated/CLIENT_MANIFEST.md` (1, 14) | generated-class pin (hand/ritual-maintained, cites `1.1.0`) | SC 13, SP 7, WS 14, PY 1, AN 1; sync-contracts skill | exempt-tree `generated` (`:115`) and exempt-name (`:122`); no release | keep | GC-2431 owned by `SC-SYNC-REGEN-01`; do not hand-edit |
| `generated/README.md`, `generated/GENERATION_BLOCKERS.md`, `generated/typescript/README.md` (3, hand-written) | generated (class), hand-authored | GENERATION_BLOCKERS: SC 9, SP 3, WS 5 | exempt-tree `generated` | keep | `README.md:11` carries a stale `SC-B06` sentence (F-A6C-13); changes ride a regeneration wave |
| `generated/python/README.md`, `generated/kotlin/README.md` (2) | generated | generator-owned | exempt-tree `generated` | keep | output of `openapi-python-client` / openapi-generator |
| `generated/kotlin/docs/` (64) and `generated/typescript/docs/` (64) (128) | generated | none by name outside the folders | exempt-tree `generated` | keep | per-model docs, policed by the `ci.yml:39` drift job |
| `.claude/agents/` (3) + `.claude/skills/` (8 `.md`) (11) | mirror of the superproject (byte-identical, `cmp`) | parity checker `scripts/harness/check_harness_parity.py` | none | keep | "never edit a mirrored skill here" (`CLAUDE.md`); refresh through the mirror lane |
| `.codex/skills/` (8 `.md`) | mirror, Codex (frozen per Q-G-09) | parity checker | none | keep | `AGENTS.md:6-10` |
| `design/` (does not exist) | n/a | n/a | none | n/a (new, subject to Q-G-01 and Q-A6C-02) | see §7.3 |
| `archive/` (does not exist) | n/a | n/a | none | n/a (not proposed) | Q-A6C-01 (a) |

Row counts sum to 214: 1+2+1+1+1+3+2+1+7+1+2+1+1+2+9+1+1+12+7+5+1+3+2+128+11+8.

### 7.2 Holds and exemptions

| Directive line (file:line) | Decision | State | Release condition |
|---|---|---|---|
| `exempt-tree: implementation/MVP — frozen` (`hygiene/HYGIENE_DECISIONS.md:114`) | D-2026-09-16-01 | active; path exists; 9 `.md` under census class `frozen` | none defined (terminal tree); a move or rename needs kit K-7 first, since no directive ends an `exempt-tree` in 0.2.1 |
| `exempt-tree: generated — generated` (`:115`) | D-2026-09-16-01 | active; 134 `.md` under census class `generated` | none; same K-7 limit if the folder were ever moved |
| `exempt-name: CONTRACT_VERSION.md` (`:121`) | D-2026-09-16-01 | active in the record; no effect on the checker (file outside every root) | none; never renamed |
| `exempt-name: generated/CLIENT_MANIFEST.md` (`:122`) | D-2026-09-16-01 | as above | none; never renamed |
| `exempt-name: openapi/changelog.md` (`:123`) | D-2026-09-16-01 | as above | none; never renamed |
| `held-name: implementation/System_V1_Implementation/proposal/SHAREDCONTRACTS_V1_PROPOSAL.md` (`:134`) | D-2026-09-16-01, kept at D-2026-09-17-02 item 2 | active; the checker's one `held:` line; census class `held` | onboarding 2a/2b migration (done), then M-9, in the commit of the `git mv`, with a `release` line for this path |
| `held-line`, `release`, `enum-add`, `allowlist`, `allowlist-remove`, `retired-name`, `forbidden-path`, `scratch-root` | none present | the `.tmp/` ignore is a `.gitignore` line, not a `scratch-root` directive; modules none; no enum extension | not applicable |
| Catalogued, not declared (Q4): `README.md`, `api-examples/`, `design-tokens/`, `openapi/`, `page-contracts/`, `schemas/`, `scripts/`, `sync-contracts/`, `tests/contract_validation/`, `implementation/System_V1_Implementation/validation/` | D-2026-09-16-01 prose | no directive; never renamed | a later decision entry only if one is turned into a root |
| Prompt file floor 0 | D-2026-09-16-01 | pin row `Prompt file floor | 0` (`hygiene/CONSUMED_HYGIENE.md:19`) | raise by `--force` re-pin with a decision entry when the first `PROMPT_` file lands in `planning/` |

### 7.3 Archive layout proposal

**Recommended: no `archive/` folder; in-place exempt-tree lines only (Q-A6C-01 (a)).**

| | `archive/` declared `exempt-tree: legacy` | in-place `exempt-tree` lines |
|---|---|---|
| What moves | retired sets `git mv` into `archive/<set>/`; one directive covers all | nothing moves; each retired set gets its own line at its current path |
| New allowlist entry | none (pin `Modules | none`, `hygiene/CONSUMED_HYGIENE.md:15`) | none |
| K-7 exposure | a set already under an `exempt-tree` line (`implementation/MVP`, `generated`) cannot move in without failing `record` for ever; sets with no line move freely | none |
| Citer cost | sweep of every path citer; the MVP paths are cited by Workspace's restructure manifest and `implementation/README.md` ("this path never moves" is said of V1; MVP is "terminal") | none |
| Fit here | nothing in this repository is an unexempted retiree | already how SharedContracts is set up |

What K-7 limits (two sentences): under kit 0.2.1 an `exempt-tree` or `exempt-subfolder` path must exist for as long as the record holds its line, and no directive ends the line, so any `git mv` of such a path fails `record` permanently; this repository's two trees (`implementation/MVP`, `generated`) are exactly such paths, but K-7 does not limit moving undeclared files into a new tree or declaring a new `exempt-tree` for a folder that exists at that commit.

The D-entry B3 would write is the "no archive needed" entry (and, if the operator picks Q-A6C-01 (b), the declaration). Id: `D-2026-10-13-01` (a grep for `D-2026-10` in `hygiene/HYGIENE_DECISIONS.md` returns 0 today, so `-01` is the next free id for 2026-10-13; B3 re-verifies by grep when writing). Draft, under heading `## 2026-10-13 — rework: archive layout`:

```text
### D-2026-10-13-01 — PlantLibrary_SharedContracts: archive layout (no archive/; trees stay in place)

Authority: master rework step B3, answer to Q-A6C-01 (operator's words recorded verbatim). Preconditions measured: check
`pass with holds — 0 violations, 1 held` at d43f7a2; K-7 open (kit 0.2.1). Dispositions: implementation/MVP and generated
stay under D-2026-09-16-01; no path moved; no directive line.
```

If (b) were chosen instead, the entry adds `- exempt-tree: archive — legacy; <what moved and from where>` in the same commit that creates `archive/` (with a short `archive/README.md`), and K-7 blocks moving `implementation/MVP` into it.

INDEX lines B3 would write (draft shapes, newest first, `- YYYY-MM-DD · <file> · <TYPE> · <status> · <summary>`):

- `implementation/System_V1_Implementation/proposal/INDEX.md`, at M-9: replace the held line by `- 2026-07-10 · PROPOSAL_sharedcontracts-v1_2026-07-10.md · PROPOSAL · active · the SharedContracts MVP→V1 suite proposal (binding scope under D-V1-01..07, amended 2026-07-10); released <date>, D-<date>-<nn>`, and a row in `## Renamed <date>`: `| SHAREDCONTRACTS_V1_PROPOSAL.md | PROPOSAL_sharedcontracts-v1_2026-07-10.md |`.
- `implementation/System_V1_Implementation/planning/INDEX.md`: one line per rework deliverable this repository receives, e.g. `- 2026-10-xx · AUDIT_<topic>_2026-10-xx.md · AUDIT · active · <summary>` (a report is `EVIDENCE` or `AUDIT`; the Deliverable naming section of `CLAUDE.md` points to the rule block).

**Q-G-06 evidence for this repository.**

1. The Kit is still 0.2.1 (`C:/Programmierung/Repo_Hygiene_Template_Kit/KIT_VERSION.md`, "Current version"), and the finding's index line, `handovers/INDEX.md:11`, still reads "open".
2. The only exempt paths in SharedContracts are the two at `hygiene/HYGIENE_DECISIONS.md:114-115`; no `exempt-subfolder` exists.
3. Nothing in the dispositions above moves either path, so recording the need, holding the affected set (empty here) and queueing a Kit session (option (a)) leaves SharedContracts unblocked; a workaround inside TARGET (b) would only matter for a move this repository does not need.
4. The M-9 release of the one `held-name` is unaffected by K-7.

**What declaring a new `design/` root (Q-G-01 (a)) would need here.**

- Not a general root. The checker reads files only inside declared roots and `exempt-tree` paths; a folder outside both is "catalogued, not declared", like `design-tokens/` and `page-contracts/`. The Kit's Configuration folder holds `CONFIGURATION.md`, `DESIGN_VERSION.md`, `conduct-rules.md`, `decisions/DECISION_RECORD_<date>.md`, `banned-colors.json`, `tokens.json`, `semantic-roles.json` and `gallery/` (Kit `examples/plantlibrary-field-ledger/design/`). `DESIGN_VERSION.md` and the decision record are product records, not `<TYPE>_<topic>_<date>` deliverables; forcing them into a root would need an `enum-add` (for example `DECISION`) or renames, which the Kit's own example does not do.
- Hygiene files touched: one prose entry (`D-2026-10-xx-nn — design/ catalogued as product documentation (Q4), version pinned by name DESIGN_VERSION.md`) with no directive. `hygiene/CONSUMED_HYGIENE.md` is untouched (no new root).
- Generated stack artifacts: if the emitter writes markdown under `design/stacks/` and the operator wants them classed, the same entry adds `- exempt-tree: design/stacks — generated; emitted stack artifacts, policed by a drift job in ci.yml`; the path must exist at that commit.
- Allowlist: not needed. Confirmed from the pin: `hygiene/CONSUMED_HYGIENE.md:15` reads `Modules | none`, and D-2026-09-16-01 states "Root-allowlist module: off (on only in the superproject)". A new top-level `design/` raises no `allowlist` violation here.
- Non-hygiene prerequisites: amend `CLAUDE.md:31-34` and `SCOPE.md:14-19` (F-A6C-09); a drift job for emission (RC-A6C-05); `.gitignore` build-output lines only if consumers compile inside `design/`.

### 7.4 Checker

Run inside the submodule, read-only, today (2026-10-13):

- `check` printed `held: implementation/System_V1_Implementation/proposal/SHAREDCONTRACTS_V1_PROPOSAL.md — live-package (Q5c); cited by implementation/System_V1_Implementation/STATE.md:11 (state); target on release: PROPOSAL_sharedcontracts-v1_2026-07-10.md (date divergence: git-created 2026-07-10, header 2026-07-09)` and the verdict line **`repo-hygiene: pass with holds — 0 violations, 1 held`**.
- `census` per-root totals:

| Root | Files | Compliant | Candidates | Exempt | Held | Set folders |
|---|---|---|---|---|---|---|
| `implementation/System_V1_Implementation/planning` | 1 | 0 | 0 | 1 | 0 | 0 |
| `implementation/System_V1_Implementation/proposal` | 2 | 0 | 0 | 1 | 1 | 0 |
| `implementation/System_V1_Implementation/handovers` | 1 | 0 | 0 | 1 | 0 | 0 |
| Repository | 4 | 0 | 0 | 3 | 1 | 0 |

Exempt-tree table (census): 9 files class `frozen` (`implementation/MVP/handoffs/Generated_Client_Handoff.md` and 8 under `implementation/MVP/package/`) and 134 class `generated`. 143 exempt-tree files agree with the map's "143 (9 frozen, 134 generated)" (`repo-hygiene/MATRIX_rename-map_2026-09-16.md:40`).

### 7.5 design-tokens / page-contracts inventory (for A4 and B5; listed, not analysed)

**design-tokens/** (7 files, 596 lines)

| Path | Lines | Version line / marker | Note |
|---|---|---|---|
| `design-tokens/README.md` | 3 | none | says the JSON is "exported from `app/gui/design_tokens.py` per OD-13" and that mapping notes describe how Python, web and Android consume the tokens; does not describe the flat layout or name consumers |
| `design-tokens/TOKEN_USAGE_NOTES.md` | 95 | "Approved 2026-07-10 as decisions P-DS-01..P-DS-10" (line 7) | headings: Identity (11), Group rules (18), Cross-cutting conduct rules (82); says `tokens.json` stays comment-free because the Dashboard theme generator flattens every key (lines 3-4) |
| `design-tokens/platform-mapping-web.md` | 20 | none | sections: Consumption pattern, Naming normalization, Component mapping reference, Divergence rule |
| `design-tokens/platform-mapping-android.md` | 18 | none | sections: Consumption pattern, Mobile adaptation rule, Divergence rule |
| `design-tokens/platform-mapping-python.md` | 16 | none | sections: Source of truth relationship, Consumption pattern, Divergence rule |
| `design-tokens/tokens.json` | 325 | none (no version key; the version is the bundle's 1.2.0) | the flat layout: 14 top-level groups `PRIMARY NEUTRAL SEMANTIC SEMANTIC_DARK DARK EXTRA HIGHLIGHT CHART CHART_DARK RADIUS SPACE TYPE_SCALE BUTTON_SIZES SHELL_SIZES` plus two scalars `FONT_FAMILY`, `MONO_FONT_FAMILY` (lines 2-324) |
| `design-tokens/semantic-roles.json` | 119 | `meta.contract_version "1.2.0"` (line 5); meta text: closes governance gap G4, approved 2026-07-10 (P-DS-05) | role layer (`LIGHT` and dark counterpart) built only from `tokens.json` primitives |

Flat layout and consumers, as the files describe them: the group names are the Python module's, mapped 1:1 onto the top-level keys (`platform-mapping-python.md:7`); consumers are the Dashboard theme generator (`PlantLibrary_Dashboard/scripts/generate-theme.mjs:4,31`), PyApp's drift check (`PlantLibrary_PyApp/scripts/check_token_drift.py`) and `DESIGN.md`, AndroidApp's `core/design` module, the `design-adoption` skill (`.claude/skills/design-adoption/SKILL.md:31-34`) and the Kit's importer/exporter (`tools/import-flat-tokens.mjs:25`, `tools/export-flat-tokens.mjs:20`). No generated token module exists in `generated/` (F-A6C-11).

**page-contracts/** (19 `.md`, no other file types)

- What a page contract is (`page-contracts/desktop-web/README.md:3`): one contract file per shared page covering desktop/web layout parity, data inputs/endpoints, offline behavior, actions, states, accessibility and accepted deviations. The Android side (`page-contracts/android/README.md:3`) holds a reduced phone-friendly contract per page or an explicit exclusion note.
- desktop-web, 11 contracts + README (lines): admin_review 43, calendar 45, dashboard 48, locations 44, plant_detail 49, plants 47, search 45, settings 46, shell 50, sources 44, statistics 42; README 3.
- android, 5 contracts + `EXCLUSIONS.md` 21 + README 3 (lines): add 45, home 44, more 43, plants 48, tasks 43.
- One example's headings, `page-contracts/desktop-web/PageContract_plants.md`: "Page Contract — Plants (library list)"; Route mapping; User problem solved; Data inputs / endpoints; Primary actions; Secondary actions; Empty / loading / error states; Offline / local cache behavior; Accessibility; Accepted platform deviations. Mobile example `MobilePageContract_home.md`: Route mapping; User problem solved; Data inputs / endpoints; Primary actions; Secondary actions; Empty / loading / error states; Offline / local cache behavior; Accessibility; MVP scope / deferred items.
- No version line in any page contract.

**Version documents.** `CONTRACT_VERSION.md` (95 lines): current version `1.2.0` (line 7); changelog entries 1.2.0 (line 19, design-token revision, P-DS-01..10), 1.1.0 (54), 1.0.0 (62), 0.1.0 (85). `generated/CLIENT_MANIFEST.md` (14 lines): cites `1.1.0` (line 3), SHA-256 `eff91162ed9c431b86335ae095163334ba8e4790f134527ee1776d7870434a91` (line 4), tools `openapi-python-client` 0.29.0 and `openapi-generator-cli` 2.39.1. The drift (GC-2431) is recorded, owned by `SC-SYNC-REGEN-01`, not fixed.

**design/ today.** Does not exist (F-A6C-08).
