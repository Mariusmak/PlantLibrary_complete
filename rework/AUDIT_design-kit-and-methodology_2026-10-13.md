# Design kit and methodology — lane A4 (read-only analysis, 2026-10-13)

Lane A4 of the PlantLibrary master rework program, Phase A (Opus 5.5, read-only). Sources: Design Template Kit
`master` @ `f08e588` (Kit 1.7.0, tag `v1.0.0`) and its branches; Conductor `main` @ `2e7adb3`; the round-6 folder
`C:\Programmierung\Conductor_GUI_Reconciliation_2026-10-12` (no git; pinned by its `handover/MANIFEST.sha256`). TARGET
read at superproject `8702e0a`, Workspace `6b4b88b`, SharedContracts `d43f7a2`. Kit tools were run only with every
output in the lane's scratch folder (`…\scratchpad\a4\`); nothing in any repository was written except this file.
TARGET paths are written repository-prefixed (`SW_Development/` = the superproject).

## §0 Summary

1. The Kit really emits five stacks in code (`web-css`, `web-ts`, `tailwind`, `compose`, `qt-qss`, plus `flat.json`). Its own tests cover only `web-css`; `compose` has never been compiled (F-A4-01, F-A4-02).
2. The canon imports cleanly and round-trips byte-equal. The scratch import matches `examples/plantlibrary-field-ledger` except for the validator's write-back fields (F-A4-06).
3. The canon fails 7 of 110 contrast pairs: six LIGHT `text_muted` pairs and chart `series_3` on `app_bg`. P-DS-03 and P-DS-07 were measured on white only. `run-all` blocks on failing pairs, so the canon cannot be BINDING-anchored as it is. That is a design decision (Q-A4-02, F-A4-07).
4. The Kit's mechanical gate does not see Compose or Qt literals (`16.dp`, `Color(0xFF…)`, `QColor(r,g,b)`). Android today has 64 plus 103 such literals that the gate would miss, so it would report a false green (F-A4-03).
5. The Kit spec puts one Configuration per system at the shared-contracts root. The installed tooling assumes `<repo>/design/` in every anchored repo: the pin path, the rule block, the worker-injection guard, readiness row 1 and CI. Q-G-01 (a) as worded does not work. The recommended form: SharedContracts holds the canonical Configuration and each client holds a synced copy with its own `conformance/` (Q-A4-01, F-A4-10).
6. The import tool takes no input path. The canon root is hard-coded to the main SharedContracts checkout, so a worktree can never be imported from (F-A4-04).
7. Kit `master` (1.7.0) still pins methodology 4.0.0 and carries `design-migration` 1.0.0. The 4.1.0 pin is on unmerged `kit/meth-4.1.0` (1.9.0) and `kit/r6-c23` (1.10.0). `design-wizard` and `design-migration` cannot be loaded in any runtime (F-A4-11, F-A4-12).
8. The installer installs three skills (`design-gate`, `design-audit`, `gallery-governance`). The "fourth" is `impeccable`: optional, vendored from a checkout, not shipped by the Kit. The AndroidApp and PyApp copies are already clean.
9. `design-adoption` is invisible to Conductor workers (it is in no client suite), yet six batch rows name it. `design-gate` is its parameterised successor. This favours Q-G-07 (a) (F-A4-18).
10. Per-client GUI rework should follow methodology 4.1.0's restructure order (00 → 01 → 01a → 02 … 06 → 06a–06d → 07/08), with one workspace per client at `implementation/Design_Migration_V1/`. Capture, visual gates, baselines and the round-6 Playwright tools go to the deferred register (Q-A4-06, Q-A4-08).
11. On Q-G-08 (a) the evidence says Dashboard first (proven stack), then PyApp (statically checkable), then Android last (needs a Kit session and a compile).

## §1 Coverage

| Item | Status | Reason |
|---|---|---|
| Kickoff prompt §1–§4 | read | brief rule 7 |
| Kit `README.md` | read | full |
| Kit `HOW_TO_INSTANTIATE_A_NEW_PROJECT.md` | read | full |
| Kit `PACKAGE_REVIEW.md` §1–§8 | read | full (incl. §3 findings, §5 limits) |
| Kit `KIT_VERSION.md` | partly read | header, 1.7.0, 0.5.0 (emitters) entries; other entries by grep |
| Kit `METHODOLOGY_SOURCE.md` | read | full |
| Kit `anchoring-kit/INSTALL.md`, `install.mjs`, `rule-block/`, `skills/README.md`, `CODEX_ADAPTATION.md` | read | full |
| Kit skills `design-gate` | read | §0–§6 |
| Kit skills `design-audit`, `gallery-governance`, `design-migration`, `design-wizard` | partly read | headings, frontmatter, version comments |
| Kit `anchoring-kit/emitters/emit-stack.mjs` | read | full (it lives under `anchoring-kit/emitters/`, not `tools/`) |
| Kit `emit-impeccable.mjs` | not read | role taken from KIT_VERSION 0.5.0 and INSTALL.md |
| Kit `checks/` (`resolve-roots`, `check-pin`, `check-literals` header, `run-all` header and verdict, `check-drift` stacks parser) | partly read | the parts that decide placement, stacks and blocking |
| Kit `conductor/` (injection block, readiness rows, roles guard) | partly read | guard lines and row list |
| Kit `ci/design-conformance.yml` | partly read | lines 1–70 |
| Kit `template/TEMPLATE_SPEC.md` §3.1, §3.9; `docs/` CONSUMED_DESIGN, DESIGN_VERSION templates | partly read | the Configuration shape, governance, pin |
| Kit `tools/*.mjs` (import, export, validate, mapping lib) | read | import, export, mapping in full; validate header and CLI |
| Kit `tools/check-prerequisites.mjs`, `lib/color-extra`, `dtcg`, `token-builders` | not read | not needed for the import path |
| Kit `examples/plantlibrary-field-ledger/` | read | CONFIGURATION.md, decision record P-DS and D-01..04 rows, JSON diffed by script |
| Kit `examples/anchored-target/` | partly read | layout, Stacks table, one contract header |
| Kit `wizard/` | partly read | emit-configuration CLI and exports, QUESTION_SCRIPT Q-W0-07, DISPOSITION file; the generators themselves not read |
| Kit `gallery/` | partly read | snippets path, coverage dimensions, compare-baselines header; GALLERY_SPEC not read |
| Kit `proposals/METH-4.1.0_design-migration-1.1.0.md` | partly read | status block, headings; no Compose/Qt content (grep) |
| Kit `tests/`, `anchoring-kit/tests/`, `wizard/tests/` | partly read | grep for which stacks are exercised; not run |
| Kit branches `kit/meth-4.1.0`, `kit/cn7-c23-c20`, `kit/r6-c23` | partly read | `git log`/`diff --stat` against `master` |
| `C:\Programmierung\design-directions-2026-09-06-backup` | not read | listing only; wizard-direction exploration, not on the import path |
| Methodology 4.1.0 `README.md`, `VERSION.md` 4.1.0 entry, `PROMPTS/README.md` | read | full or relevant entry |
| Methodology `GUI_IMPROVEMENT_STRATEGY.md` | partly read | §4, §5, §7, §8 |
| Methodology prompts 01, 01a, 06b, 06c; prompt 11 lint | partly read | grep for capture, render, Configuration writes; lint a–e |
| Methodology seven new templates | partly read | presence in the file list only (FILE_INDEX not opened) |
| `Design_Template_Initiative/` STATE.md, INITIATIVE_CLOSEOUT.md, RUNBOOK_GUI_REWORK.md | partly read | G-close closure, DTI-05, deferred items, runbook headings |
| SDA `04_APPROVED_DESIGN_REVISION_2026-07-10.md` | partly read | §2 decisions, §3 evidence |
| SDA `STATE.md`, `00_DESIGN_GOVERNANCE_PROPOSAL.md` §4, §5, §9 | partly read | decisions table, token pipeline, D1 |
| SharedContracts `design-tokens/**` | read | README, platform mappings, usage notes head, JSON structure, eol |
| Superproject `.claude/skills/design-adoption/SKILL.md` | read | full |
| Client TASK_CHECKLIST rows naming `design-adoption`, client `.claude/skills` listings, hygiene roots | read | grep and listing |
| Dashboard `scripts/generate-theme.mjs`, Android `core/design`, PyApp `design_tokens.py`, `light.qss` | partly read | only what the import, emitter and census need (A9 owns consumption) |
| Conductor `implementation/Design_Migration_V1/` README, SCOPE §1, planning/ (INDEX, round-5 PLAN §0–§3a, round-4 pack headings), folder listings | partly read | as the brief asks |
| Conductor `design/` (layout, stacks, `CONSUMED_DESIGN.md`, `stacks/web-css/mapping.md` head), `.gitattributes` | partly read | layout and pin shape |
| Conductor `design-gate`, `design-audit`, `gallery-governance` | read | byte-compared with the Kit (equal after CR stripping) |
| Round-6 `README.md`, proposal §1, §6, §11, §12 and headings, R1–R7 headings, `tools/shot.py`, `sweep.py`, `after_shots.sh`, `mockups/AUTHORING.md` head, `handover/` | partly read | as the brief asks |
| Round-6 `mockups/*.html`, `notes/`, `BRIEFS.md`, `patch_*.py` | not read | format known from README, AUTHORING and LANDING; contents not needed |
| `C:\Programmierung\Working_Folder` | partly read | listing only; `design-round-3-2026-10-01/capture_r3*.py` and `gui-improvement/` not opened |

Counts: 15 read · 23 partly read · 4 not read.

## §2 Findings

**F-A4-01: all five stacks are implemented; only `web-css` is tested.** `KNOWN_STACKS` is defined at `C:\Programmierung\Design_Template_Kit\anchoring-kit\emitters\emit-stack.mjs:31`, and the emitter table at `:366` maps all five stacks plus `flat.json`. Every emitter call in the Kit's test files passes `--stacks web-css` (`…\anchoring-kit\tests\install.test.mjs:122`, `…\fk3-outputs.test.mjs:69`, `…\fk4-walker.test.mjs:32`, `…\check-drift.test.mjs:39`). No test references `compose`, `qt-qss`, `web-ts` or `tailwind`. The pilot consumed `web-css` only (`C:\Programmierung\Orchestrator_System\design\stacks\` listing: `web-css/` and `flat.json`). Meaning for TARGET: the Dashboard stack is proven; the AndroidApp and PyApp stacks are emittable but unproven.

**F-A4-02: Compose output has open structural risks** (record only, Kit). `…\emit-stack.mjs:247-306` writes `package design.generated` (`:298`), an `object Tokens { object Color { val X = Color(0x…) } … }` and theme objects `LightRoles`/`DarkRoles`. The nested `object Color` carries the same name as the imported `androidx.compose.ui.graphics.Color`. That is a compile risk nobody has checked, because the output has never been compiled. The emitter writes no `TextStyle`, `FontWeight`, font family or Material3 `ColorScheme`, all of which `PlantLibrary_SharedContracts/design-tokens/platform-mapping-android.md:7-10` expects. The scratch run produced a 394-line `Tokens.kt` with 367 `val`s. Meaning: Android needs a hand-written theme wrapper that consumes `Tokens.*`, plus a compile before anything relies on it.

**F-A4-03: the literal census cannot see Compose or Qt literal forms** (record only, Kit). The regexes at `C:\Programmierung\Design_Template_Kit\anchoring-kit\checks\check-literals.mjs:35-40` were probed in scratch. `16.dp`, `14.sp`, `Color(0xFF2A7A30)` and `QColor(42, 122, 48)` give no match; `16px` and `"#2A7A30"` match. `.xml` is not in the final-acceptance walk (`…\checks\run-all.mjs:56`). Today's invisible literals:
- AndroidApp: 64 `Color(0x…)` in `PlantLibrary_AndroidApp/core/design/src/main/java/com/plantlibrary/android/core/design/Color.kt:18` onwards, and 103 `N.dp` across 17 files, for example `PlantLibrary_AndroidApp/feature/home/src/main/java/com/plantlibrary/android/feature/home/HomeScreen.kt:42`.
- PyApp: one `QColor(int…)` at `PlantLibrary_PyApp/app/gui/theme_utils.py:120`.

Meaning: on Android, `design-audit` would report green while literals remain.

**F-A4-04: the import tool takes no input path** (record only, Kit). Usage at `C:\Programmierung\Design_Template_Kit\tools\import-flat-tokens.mjs:7` is `[--out <dir>]`. The canon root is hard-coded as `<kit>/../SW_Development/PlantLibrary_SharedContracts/design-tokens` (`:25`), and a positional argument is silently ignored (`:27-31`). The exporter does the same (`…\tools\export-flat-tokens.mjs:20`). Meaning: it works only with the Kit beside the superproject's main checkout. A rule-5 worktree of SharedContracts (`C:\Programmierung\SW_Development_wt\…`) cannot be imported from or round-tripped.

**F-A4-05: part of the import is frozen in a table.** The 19 DARK/EXTRA literals and all 70 role aliases are hard-coded in `C:\Programmierung\Design_Template_Kit\tools\lib\plantlibrary-mapping.mjs:39-60` and `:69-144`; they are not read from the canon. The importer parses the canon's `semantic-roles.json` only "for provenance" (`…\import-flat-tokens.mjs:389-391`). Only the export round trip would notice a canon change. Today it reports `groups with a diff: 0`, `LIGHT equal: true, DARK equal: true` (scratch `import/roundtrip-report.json`). Meaning: after B5, `design-tokens/` must stop being edited by hand, or every edit must be followed by the round trip.

**F-A4-06: the scratch import equals the Kit example except for validator write-back.** After stripping the validator's write-back fields (`$extensions.kit.validated_against` on chart groups; `measured`/`verdict` on the 110 pairs), `tokens.json` and `semantic-roles.json` are equal to `C:\Programmierung\Design_Template_Kit\examples\plantlibrary-field-ledger\design\`. `banned-colors.json` and `roundtrip-report.json` are byte-identical. Meaning: the canon has not moved since the example was cut (2026-09-01; last SharedContracts `design-tokens` commit `1650271`). The example is a faithful preview of the B5 Configuration core.

**F-A4-07: seven pairs fail, and `run-all` blocks on them.** The validator run in scratch reported `pairs_checked: 110`, `pairs_failed: 7`, exit 1. The failures:
- six LIGHT `text_muted` pairs: on `app_bg` 4.46, `surface_2` 4.33, `surface_3` 4.28, `surface_4` 3.87, `hover_bg` 4.33, `selected_bg` 4.28;
- `chart.series_3` on `app_bg`: 2.95 against 3.

The same seven are recorded in `…\examples\plantlibrary-field-ledger\design\decisions\DECISION_RECORD_2026-07-10.md:83-89`. The approval evidence measured white only: `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md:52` and `:56`, and `PlantLibrary_SharedContracts/design-tokens/TOKEN_USAGE_NOTES.md:34`. `run-all` makes "Contrast pairs" a blocking section (`C:\Programmierung\Design_Template_Kit\anchoring-kit\checks\run-all.mjs:278`). Meaning: with the canon anchored as it is, every UI row audit and every final acceptance is red. A disposition at PlantLibrary's design gate must come before BINDING (Q-A4-02).

**F-A4-08: the import writes only part of a Configuration.** It writes three files (`…\import-flat-tokens.mjs:485-489`). The example's `CONFIGURATION.md`, `DESIGN_VERSION.md`, `conduct-rules.md` and decision record are hand-authored (`…\examples\plantlibrary-field-ledger\design\CONFIGURATION.md:27`). That `CONFIGURATION.md` says "PlantLibrary itself remains grandfathered … no PlantLibrary suite reads this folder" (`:8-11`) and declares no stacks (`:41-45`). Yet `check-drift` and the installer read the `## Stacks` table (`…\anchoring-kit\checks\check-drift.mjs:66-79`, `…\anchoring-kit\install.mjs:251-253`). Component contracts come only from the wizard's `renderComponentContract` (`C:\Programmierung\Design_Template_Kit\wizard\emit-configuration.mjs:611`, exported at `:1007-1017`), which has no CLI for an imported Configuration. Meaning: B5 hand-writes four documents and scripts the contract emission.

**F-A4-09: metadata inside hashed files must be final before the first pin.** The pin hashes `tokens.json`, `semantic-roles.json`, `conduct-rules.md` and `banned-colors.json` (`…\anchoring-kit\install.mjs:248-249`, `…\checks\check-pin.mjs:15`). The importer writes into them:
- `kit_version '0.1.0'`, `design_version '1.0.0'`, `consumption 'Reference example only — no suite consumes this file.'` (`…\import-flat-tokens.mjs:426-429`);
- "this is not adopted by any suite" (`:398-400`);
- a `$schema` path that is valid only inside the Kit (`:396`).

The pilot had to spend a dedicated re-pin task on exactly this class of string (`C:\Programmierung\Orchestrator_System\design\conformance\CONSUMED_DESIGN.md:51-58`). Meaning: B5 rewrites these strings and only then runs `install.mjs`.

**F-A4-10: one Configuration per system is specified, but not implemented** (record only, Kit). `C:\Programmierung\Design_Template_Kit\template\TEMPLATE_SPEC.md:41-42` places the Configuration "at the shared-contracts root of a multi-suite system (one Configuration per system, never per suite)", and `:85` repeats it. The tooling contradicts this:
- the pin, allowlist and matrix are written under `<config>/conformance/` (`…\install.mjs:200`, `:230`, `:327`), and `check-pin` reads the pin only there (`…\checks\check-pin.mjs:49`);
- the root probe looks only at `<repo>/design/conformance/CONSUMED_DESIGN.md` or `$DESIGN_ROOT` (`…\checks\lib\resolve-roots.mjs:32-38`, `:45-56`);
- the rule block hard-codes `design/…` paths (`…\anchoring-kit\rule-block\DESIGN_RULES_BLOCK.md:4-12`);
- the worker-injection guard and readiness row 1 key on `<repo>/design/CONFIGURATION.md` (`…\anchoring-kit\conductor\WORKER_INJECTION_BLOCK.md:13`, `…\conductor\check-conductor-readiness.mjs:39`, `:74`);
- the CI template checks out only the repository and the Kit (`…\anchoring-kit\ci\design-conformance.yml:24-34`).

The template asks for one `CONSUMED_DESIGN.md` per consuming surface (`…\template\docs\CONSUMED_DESIGN_TEMPLATE.md:5`) at a single path. Meaning: Q-G-01 (a) in its seed wording (a client's own `CONSUMED_DESIGN.md` pinning SharedContracts) is never checked. `check-pin` would read SharedContracts' file instead (Q-A4-01).

**F-A4-11: `design-wizard` and `design-migration` cannot be loaded anywhere** (record only, Kit). `…\anchoring-kit\skills\README.md:33-34` says they live in the Kit's `.claude/skills/` and `.codex/skills/`, but the Kit root has neither folder. The guide invokes them as `/design-wizard` and `/design-migration` (`…\HOW_TO_INSTANTIATE_A_NEW_PROJECT.md:37`, `:111`), and the installer never installs them (`…\install.mjs:11-13`). Meaning: PlantLibrary runs the methodology prompts directly, as the pilot did. They live in PlantLibrary's own Workspace.

**F-A4-12: Kit `master` is behind the methodology, and its docs are stale** (record only, Kit). `C:\Programmierung\Design_Template_Kit\METHODOLOGY_SOURCE.md:15` pins `4.0.0`, and `design-migration` is `1.0.0` (`…\anchoring-kit\skills\design-migration\SKILL.md:8`). The 4.1.0 pin and `design-migration` 1.1.0 are on `kit/meth-4.1.0` `c34b56c` (Kit 1.9.0), which `kit/r6-c23` `4722ac9` (1.10.0) extends. Neither is merged. Their merge is scheduled at the Conductor's `DM1-B67` boundary (`PlantLibrary_Workspace/methodology/Design_Template_Initiative/STATE.md:414-416`). The annotated tag `v1.0.0` on `f08e588` was created 2026-10-12, yet `…\KIT_VERSION.md:37` and `…\PACKAGE_REVIEW.md:146` still say "not tagged".

**F-A4-13: stack names disagree across the Kit** (record only, Kit). `…\template\TEMPLATE_SPEC.md:28` and `…\template\docs\STACK_MAPPING_TEMPLATE.md:13` say `web-tailwind`; the emitter knows `tailwind` (`…\emit-stack.mjs:31`). The wizard suggests `react`, `pyside6` and `jetpack-compose` (`…\wizard\QUESTION_SCRIPT.md:53`), which the emitter rejects with exit 2 (`…\emit-stack.mjs:392-396`). Meaning: B5's hand-written `## Stacks` table must use `web-css`, `web-ts`, `compose` and `qt-qss` exactly.

**F-A4-14: Gallery snippets are wiped by the emitter** (record only, Kit, minor). The Gallery reads per-stack snippets from `stacks/<stack>/generated/snippets/` (`…\gallery\generate-gallery.mjs:267-276`). `emit-stack` deletes `generated/` before writing (`…\emit-stack.mjs:406`), and no emitter writes snippets.

**F-A4-15: the Dashboard's naming does not match the Kit's `web-css` output.** The emitted selectors are `[data-theme="LIGHT"]` and `[data-theme="DARK"]`, taken from `meta.themes` (`…\emit-stack.mjs:110-113`; the importer sets uppercase at `…\import-flat-tokens.mjs:428`). Variables are `--token-…` and `--role-…`. The Dashboard uses `[data-theme="dark"]` (`PlantLibrary_Dashboard/src/theme/base.css:26`) and `--primary-600`-style variables from its own generator (`PlantLibrary_Dashboard/scripts/generate-theme.mjs:1-32`, `PlantLibrary_Dashboard/package.json:15`). Its generated `src/theme/tokens.generated.*` lie outside `stacks/*/generated/`, which is the only generated path the census exempts (`…\checks\check-literals.mjs:29`). Meaning: the Dashboard needs a migration decision (A9 owns the detail).

**F-A4-16: PyApp's token direction must invert, and its names differ.** PyApp's `app/gui/design_tokens.py` is the canon's origin (`PlantLibrary_SharedContracts/design-tokens/platform-mapping-python.md:5`, `PlantLibrary_SharedContracts/design-tokens/README.md:3`). The `qt-qss` output is a Python module with `TOKENS`, `ROLES` and `VARS` (386 keys such as `light_app_bg`, `typography_body_md_size`), not a `.qss` file. PyApp's QSS uses `$app_bg` and `${type_body_md_size}` (`PlantLibrary_PyApp/resources/styles/light.qss:2-10`). The scratch `tokens.py` parses (Python `ast.parse` only). Meaning: a thin adapter is needed that maps generated names to PyApp's names and transcribes no values. That matches the accepted SDA-DEC-02 "fully generated" (`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:214`).

**F-A4-17: SDA decisions were accepted but never recorded in the package.** Onboarding D5 accepted SDA-DEC-01..05 as recommended (`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:214`). The package's table still shows all five `open` (`PlantLibrary_Workspace/implementation/System_Design_Architecture/STATE.md:21-25`), and Workspace binding waits for them to be recorded (`PlantLibrary_Workspace/CLAUDE.md:31`). SDA-DEC-01 "siblings now" (`…/proposal/00_DESIGN_GOVERNANCE_PROPOSAL.md:80`, `:210`) is compatible with a new sibling `design/` folder in SharedContracts, but not with restructuring the existing folders. The planned single generator SDA-B02 (`…/BATCH_PLAN.md:58`) is what `emit-stack.mjs` already is. Meaning: B4/B5 record the decisions and supersede SDA-B01/B02 (A7 owns the package edits).

**F-A4-18: `design-adoption` never reaches a Conductor worker** (Q-G-07 evidence). No client suite carries it. Their `.claude/skills` listings hold only `plan-batch`, `real-stack-testing`, `run-batch`, `test-driven-development`, `validate-real-stack`, plus `impeccable` in AndroidApp and PyApp and `gui-validation` in PyApp. Discovery does not cross from a submodule working directory to the parent (`SW_Development/onboarding/AUDIT_skill-assumptions_2026-09-15.md:169`). Yet six rows name it:
- `PlantLibrary_Dashboard/implementation/System_V1_Implementation/TASK_CHECKLIST.md:36-37`;
- `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/TASK_CHECKLIST.md:48`, `:52`;
- `PlantLibrary_PyApp/implementation/System_V1_Implementation/TASK_CHECKLIST.md:37`, `:39`.

The skill also restates hex values (`SW_Development/.claude/skills/design-adoption/SKILL.md:71-74`) against its own rule (`:12-15`).

**F-A4-19: a second package in a client confuses headless workers.** A design-migration workspace at `<client>/implementation/Design_Migration_V1/` is matched by run-batch's one-level glob alongside `System_V1_Implementation`. The tiebreak then ends in "ask the user", which a headless worker cannot do (`SW_Development/onboarding/AUDIT_skill-assumptions_2026-09-15.md:34`). The Workspace precedent is to name the package path and bind one project per package (`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:213`).

**F-A4-20: no PlantLibrary repository pins line endings.** None has a `.gitattributes`, and `core.autocrlf=true` (git config, SharedContracts). The Kit's open F-K10 (`C:\Programmierung\Design_Template_Kit\PACKAGE_REVIEW.md:109`) means a CRLF checkout of the core changes every pin digest. The Conductor pins `eol=lf` on its design core and generated stacks (`C:\Programmierung\Orchestrator_System\.gitattributes:4-9`). Today `design-tokens/*.json` are `i/lf w/lf` (`git ls-files --eol`).

**F-A4-21: the round-6 tools are browser automation.** `tools/shot.py` and `tools/sweep.py` drive Playwright Chromium against `file://` mockups (`C:\Programmierung\Conductor_GUI_Reconciliation_2026-10-12\tools\shot.py:14`, `:44-46`; `…\tools\sweep.py:10`, `:29-30`), and `after_shots.sh` wraps `shot.py` (`…\tools\after_shots.sh:10`). No running app is needed, but this is browser automation, which kickoff §2 rule 1 excludes. The mockups' "before" images are product screenshots, which need a running app (`…\README.md:10`). Meaning: these tools go to the deferred register.

**F-A4-22: the Workspace exempt-tree record is stale** (A6 owns). It reads "VERSION.md 4.0.0 … 62 .md files" (`PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md:141`); the folder is now 4.1.0 with 74 tracked `.md` files. Line `:142` says 45, against 47 tracked for the Initiative. The Initiative itself flagged this as owed (`PlantLibrary_Workspace/methodology/Design_Template_Initiative/STATE.md:416`).

**F-A4-23: required screenshot work cannot be done in Phase B.** The methodology requires a "current screenshot baseline or explicit unavailable rationale" (`PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/GUI_IMPROVEMENT_STRATEGY.md:164`). Phase 3 capture, phase 10 visual gates, Gallery baselines (`C:\Programmierung\Design_Template_Kit\gallery\capture-baselines.mjs:30`, which imports Chromium) and the Kit's own browser tests are not runnable in Phase B. Meaning: Phase B records "unavailable: rule 1" plus deferred rows. Phase 5 compares against contracts and source only.

**F-A4-24: instance 2 carries no design role override** (`PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_CLOSEOUT.md:168`). Until the operator deploys `C:\Programmierung\Design_Template_Kit\anchoring-kit\conductor\roles\{implementer,integrator}.md` into instance 2's data directory, readiness row 7 fails for every anchored client (`…\HOW_TO_INSTANTIATE_A_NEW_PROJECT.md:148-152`).

**F-A4-25: PlantLibrary's adoption ends a recorded grandfathering.** DTI-05 kept the canon grandfathered and read-only for the initiative (`PlantLibrary_Workspace/methodology/Design_Template_Initiative/STATE.md:44`). "PlantLibrary adoption of the generated `design-gate`" is listed as "a PlantLibrary decision" (`…/INITIATIVE_CLOSEOUT.md:162`). Meaning: B5 needs a recorded decision that ends the grandfathering (Q-A4-04).

## §3 Candidates

| RC | Source path @ pin | What | Verdict | Target repo and path | Lane | Q |
|---|---|---|---|---|---|---|
| RC-A4-01 | `C:\Programmierung\Design_Template_Kit\tools\import-flat-tokens.mjs` @ `f08e588` | Converts the flat canon into the DTCG core (`tokens.json`, `semantic-roles.json`, `banned-colors.json`) | adapt: run with `--out` to SharedContracts `design/` from the main checkout (F-A4-04). Before any pin, rewrite `$schema`, `$description`, `meta.kit_version/design_version/consumption` (F-A4-09). It replaces nothing yet; `design-tokens/` stays the legacy export. If wrong, a later string fix forces a re-pin in every client | PlantLibrary_SharedContracts `design/` | B5 | Q-A4-01, Q-A4-04 |
| RC-A4-02 | `…\Design_Template_Kit\examples\plantlibrary-field-ledger\design\{CONFIGURATION.md,DESIGN_VERSION.md,conduct-rules.md,decisions\DECISION_RECORD_2026-07-10.md}` @ `f08e588` | The hand-written documents for this exact canon (P-DS-01..10 restated; D-01..D-04) | adapt: Status DRAFT `0.1.0`; drop the "grandfathered / no suite reads" text; add a `## Stacks` table (`web-css`, `web-ts`, `compose`, `qt-qss`) and the L2 layer; methodology 4.1.0. Replaces nothing (new). If wrong, `check-drift` cannot run ("declares no stacks") | PlantLibrary_SharedContracts `design/` | B5 | — |
| RC-A4-03 | `…\Design_Template_Kit\tools\export-flat-tokens.mjs` @ `f08e588` | Round-trip proof that the Configuration equals the flat `design-tokens/` | adopt verbatim as a B5 static check, run against a scratch copy only: it writes `roundtrip-report.json` beside the design directory. It replaces the planned SDA-B02 "CI-diff transition". If skipped, `design-tokens/` drifts silently | PlantLibrary_SharedContracts (procedure) | B5 | Q-G-04 |
| RC-A4-04 | `…\Design_Template_Kit\anchoring-kit\emitters\emit-stack.mjs` @ `f08e588` | One generator for `web-css`, `web-ts`, `compose`, `qt-qss`, `flat.json` | adopt verbatim (run from the Kit). It replaces the planned SDA-B02 `generate_tokens.py` and becomes the source the Dashboard generator, Android `Color.kt`/`Shape.kt` and PyApp values move to. If wrong, an untested `compose`/`qt-qss` output is consumed blind (deferred compile row) | PlantLibrary_SharedContracts `design/stacks/*/generated/` (+ client copies) | B5 | Q-A4-01, Q-A4-05 |
| RC-A4-05 | `…\Design_Template_Kit\anchoring-kit\install.mjs` @ `f08e588` | Anchors one repository: skills, `scripts/design/`, CI, rule block, pin | adopt verbatim, once per client with `--stacks` per client (Dashboard `web-css,web-ts`; AndroidApp `compose`; PyApp `qt-qss`). `--runtimes` follows Q-G-09: if Codex is frozen, drop `codex`. `--rule-block-before` is set per CLAUDE.md layout. Replaces nothing. If wrong, rule-block placement breaks shared-block parity | PlantLibrary_Dashboard, PlantLibrary_AndroidApp, PlantLibrary_PyApp roots | B5 | Q-A4-01, Q-G-09 |
| RC-A4-06 | `…\anchoring-kit\skills\{design-gate,design-audit,gallery-governance}\SKILL.md` @ `f08e588` | The three installed skills | adopt verbatim through the installer. Replaces `design-adoption` (RC-A4-17). If wrong, the parity guard fails on hand edits | the three clients' runtime mirrors | B5 (B1 for the superproject's set) | Q-G-07 |
| RC-A4-07 | `C:\Programmierung\Orchestrator_System\.gitattributes:4-9` @ `2e7adb3` | `eol=lf` on the design core and the generated stacks | adapt the paths to `design/…` in SharedContracts and in each client copy. Closes the F-K10 exposure. If skipped, a CRLF checkout breaks every pin | SharedContracts and the three clients, `.gitattributes` | B5 | — |
| RC-A4-08 | `C:\Programmierung\Orchestrator_System\design\conformance\{audit_exclude.txt,row_audit_commands.txt}` @ `2e7adb3` | Declares non-product roots and sanctioned row-audit commands | adapt the roots per client (Dashboard `e2e`, `tests`, `dist`, `test-results`; AndroidApp build output; PyApp tests and venvs). Without them, the final-acceptance walk counts evidence and test literals (F-K4) | each client `design/conformance/` | B5 | — |
| RC-A4-09 | `…\Design_Template_Kit\anchoring-kit\conductor\roles\{implementer,integrator}.md` @ `f08e588` | Worker-injection role override | adopt verbatim; the operator deploys it to instance 2's data directory at a drained boundary (F-A4-24). Without it, readiness row 7 fails and workers are not design-bound | instance 2 data directory (operator act) | B8 | — |
| RC-A4-10 | `PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/` @ `6b4b88b` (4.1.0) | Prompts 00–10, 01a, 06a–06d, templates | keep PlantLibrary's: it is the source the Kit pins | used in place by each client workspace | B6 | — |
| RC-A4-11 | `C:\Programmierung\Orchestrator_System\implementation\Design_Migration_V1\README.md:16-61` @ `2e7adb3` | Workspace layout and the methodology-name deviation note | adapt: one per client at `implementation/Design_Migration_V1/`. Methodology names are allowed because `implementation/` is not a declared root (`PlantLibrary_Dashboard/hygiene/CONSUMED_HYGIENE.md:21-26`); `planning/`, `proposal/`, `handovers/` are declared by D-entry; the README records path-named invocation (F-A4-19) | PlantLibrary_Dashboard, _AndroidApp, _PyApp `implementation/Design_Migration_V1/` | B6 (roots: B3) | Q-A4-06 |
| RC-A4-12 | `…\Design_Migration_V1\planning\PLAN_design-round-5_2026-10-09.md:10-108` @ `2e7adb3` | Round runbook shape: gate → cut → Kit half → batches → captures → re-gate → sign; ledger; lanes table | adapt into the program runbook's per-client step blocks (A5 owns the contract). Captures and re-gate become deferred rows | `SW_Development/rework/PROMPTS_master-rework-runbook_2026-10-13.md` §3 | R-3 / B6 | Q-A4-08 |
| RC-A4-13 | `C:\Programmierung\Conductor_GUI_Reconciliation_2026-10-12\research\R1…R7` and proposal shape (`PROPOSAL_gui-round-6_2026-10-12.md:25-449`), pinned by `handover\MANIFEST.sha256` | Research lanes (code inventory, data vs display, design-system brief, planned work, normative requirements, critique, special topic) and the proposal skeleton | adapt per client: R6 critique is source-only until screenshots exist; R5 reads `system_description`, page contracts and V1 rows | each client workspace `current_state/`, `proposal/` | B6 | — |
| RC-A4-14 | `…\Conductor_GUI_Reconciliation_2026-10-12\mockups\{assets,AUTHORING.md,BRIEFS.md,notes}` | Static-HTML mockup kit: generated `tokens.css` and Gallery `pages.css` verbatim, plus shell, fixture and per-page notes | adapt: PlantLibrary's generated `web-css` and Gallery CSS; Android at phone width; authored statically, never rendered by a tool in Phase B | SharedContracts `design/gallery/pages/`, `fixtures/` (06b) | B6 | Q-A4-08 |
| RC-A4-15 | `…\Conductor_GUI_Reconciliation_2026-10-12\tools\{shot.py,sweep.py,after_shots.sh}` | Playwright render and sweep of static mockups | record only → deferred register (browser automation, rule 1) | `SW_Development/rework/REGISTER_deferred-validations_2026-10-13.md` | C1 | Q-A4-08 |
| RC-A4-16 | `…\Conductor_GUI_Reconciliation_2026-10-12\handover\{LANDING.md,MANIFEST.sha256}` | Byte-pinned landing of out-of-checkout evidence | adopt the pattern for landing mockups or evidence built in scratch | client workspaces `validation/` | B6 | — |
| RC-A4-17 | `SW_Development/.claude/skills/design-adoption/SKILL.md` (+ `.codex` copy) @ `8702e0a` | Old pre-work design gate | retire after B5 anchors the three clients, leaving a one-line pointer to `design-gate`. The six rows' skill cells are re-pointed through plan-batch and recorded in STATE. If retired before B5, no gate has a Configuration to read | superproject `.claude/skills/`, client TASK_CHECKLISTs | B1 + B4 | Q-G-07 |
| RC-A4-18 | Kit findings F-A4-02, -03, -04, -10, -11, -12, -13, -14 @ `f08e588` | Kit defects and gaps | record only; queue one Kit session (operator) with a proposal: Compose/Qt literal forms, emitter tests for `compose`/`qt-qss`/`web-ts`, Compose TextStyle and ColorScheme, multi-suite pin root, import `--canon`, skill loading, naming, snippets | the Kit (not TARGET) | — | Q-A4-05 |
| RC-A4-19 | `PlantLibrary_Workspace/implementation/System_Design_Architecture/` SDA-B01..B08 @ `6b4b88b` | Pre-Kit design-governance plan | record the D5 answers in its STATE.md; mark SDA-B01/B02/B04/B05/B08 superseded by B5 (Kit Configuration, emitter, CI, rule block, anchoring); keep SDA-B03 (contracts), B06 (icons, font), B07 (parity) as inputs to B6 | PlantLibrary_Workspace SDA package | B4 (A7) | Q-A4-04 |
| RC-A4-20 | `…\Design_Template_Kit\tools\validate-configuration.mjs` @ `f08e588` | E4 validator | adopt verbatim as a static check, always with `--reports-dir <scratch> --no-write-back` until BINDING. Replaces nothing. If run without flags, it rewrites `tokens.json` and `semantic-roles.json` (`:9-15`) | procedure | B5 | Q-G-04 |
| RC-A4-21 | `…\Design_Template_Kit\wizard\emit-configuration.mjs:611` (`renderComponentContract`) @ `f08e588` | Contract emitter with no CLI | adapt: a scratch-held script imports it and writes the 23 component contracts into the Configuration; requirement IDs and Role stay PlantLibrary-owned. If skipped, `design-gate` §4 step 2 has no contracts | PlantLibrary_SharedContracts `design/contracts/components/` | B5 | — |
| RC-A4-22 | `…\Design_Template_Kit\gallery\generate-gallery.mjs` @ `f08e588` | Static Gallery page from the Configuration | adopt verbatim (no browser). Baselines are deferred | PlantLibrary_SharedContracts `design/gallery/index.html` | B5 | — |
| RC-A4-23 | `C:\Programmierung\Orchestrator_System\design\conformance\CONSUMED_DESIGN.md:30-58` @ `2e7adb3` | "What this pin gates" note | adapt as guidance in B5's prompt: final metadata before the first pin; the Design version row is display-only | B5 step block | B5 | — |
| RC-A4-24 | `…\Design_Template_Kit\HOW_TO_INSTANTIATE_A_NEW_PROJECT.md:135-144` @ `f08e588` | Pilot batch lessons (foundation before bugfix, contracts name roles, capture after settle) | adopt verbatim as B6 plan rules | B6 step blocks | B6 | Q-G-08 |
| RC-A4-25 | `PlantLibrary_SharedContracts/page-contracts/**` @ `d43f7a2` | 11 desktop-web and 5 Android page contracts (P-DS-10) | keep in place at B5, where `CONFIGURATION.md` links them as the L1 page layer. Move them into `design/contracts/pages/` (git mv, mapping row, reference sweep) at each client's 06b, when they are revised | PlantLibrary_SharedContracts | B6 | — |
| RC-A4-26 | `…\Design_Template_Kit\wizard\lib\zone-models.mjs` @ `f08e588` | Ten page-structure models (static post-processor) | adapt for 06b IA alternatives on Dashboard and PyApp | B6 mockup steps | B6 | — |

## §4 Questions for the operator

| Q | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A4-01 | How is Q-G-01 (a) built, given the Kit's tooling assumes `<repo>/design/` (F-A4-10)? | (a) **Hybrid**: one canonical Configuration in `PlantLibrary_SharedContracts/design/` (the only place edits land). Each client holds a synced copy in its own `design/` (core, stacks, contracts, Gallery; byte-equal, parity-checked against SharedContracts) plus its own `design/conformance/` (pin, matrix, allowlist, audit_exclude). Re-sync is each client's upgrade task. (b) Pure shared: every client installs with `--design-root ../PlantLibrary_SharedContracts/design` and one shared pin. (c) One Configuration per client (Q-G-01 (b)). (d) Hold anchoring until a Kit session makes multi-suite first-class | (a) works with the Kit as built: rule block, injection guard, readiness row 1, CI, worktrees and standalone clones all see `design/`. It keeps the Template's "one per system" rule (R2) and gives each client its own pin. (b) breaks the guard, the rule block, CI and rule-5 worktrees. (c) violates `TEMPLATE_SPEC.md:42` and triples the design gate | B5 anchoring, B6 S0/00 |
| Q-A4-02 | The canon fails 7 of 110 contrast pairs, and `run-all` blocks on them (F-A4-07). What happens before BINDING? | (a) A design-decision step (Opus 5.5 · xhigh, operator gate) recomposes the failing roles or values with measured evidence: a decision record plus a P-DS amendment, then re-validate. (b) Narrow the pair set by a recorded decision (`text_muted` only on `surface_1`/`odd_row_bg`, `series_3` only on `surface_1`). (c) Keep the canon; the Configuration stays DRAFT and no client is anchored | `design-gate` rule 5 sanctions only recomposition. (b) was rejected as "tuning the test to the answer" in the canon's own import record (`…\DECISION_RECORD_2026-07-10.md:103`). (c) stalls B5 and B6 | B5 BINDING, every B5 install, all of B6 |
| Q-A4-03 | Which Kit commit does PlantLibrary pin? | (a) `master` `f08e588` (Kit 1.7.0, tag `v1.0.0`) now; re-pin as its own task when `master` takes 1.9.0/1.10.0. (b) Wait for the operator's merge of `kit/meth-4.1.0` and `kit/r6-c23`, then pin. (c) Pin a branch commit (`4722ac9`) | Only the tag is CI-fetchable (`…\ci\design-conformance.yml:6-8`). Anchoring is identical across 1.7.0–1.10.0, and the methodology prompts (4.1.0) are PlantLibrary's own (F-A4-11, -12) | B5 install |
| Q-A4-04 | Does PlantLibrary formally end DTI-05 and adopt the Kit, superseding the SDA package where they overlap? | (a) Yes: a recorded decision (Workspace SDA STATE plus each repo's decision log as the hygiene kit requires). SharedContracts `design/` becomes the canon. `design-tokens/` stays as the flat export, round-trip checked, until the three clients move off it. SDA-DEC-01..05 recorded; SDA-B01/B02/B04/B05/B08 superseded. (b) Keep grandfathering and use only Kit tooling | DTI-05 deferred exactly this to "a PlantLibrary decision" (`…/INITIATIVE_CLOSEOUT.md:162`). The kickoff's B5 presupposes it | B5 (all), B4 SDA edits |
| Q-A4-05 | Android (and part of PyApp) cannot be audited or compile-proven with the Kit as is (F-A4-02, -03). How? | (a) Queue one Kit session (operator) for: Compose/Qt literal forms in `check-literals`, tests for `compose`/`qt-qss`/`web-ts`, Compose TextStyle and ColorScheme, and the nested `Color` name. Android implementation waits for that session plus a compile (Phase C or Q-G-04 (b)). (b) A PlantLibrary-local Kotlin literal check outside `scripts/design/`, as an interim. (c) Accept the gap | Rule 2 forbids patching the Kit from here. (b) creates a second census the Kit's report never cites. (c) ships a false green | B6 Android implementation; B5 Android consumption wiring |
| Q-A4-06 | Where does each client's design-migration workspace live, and how is it dispatched? | (a) `<client>/implementation/Design_Migration_V1/`; every `/run-batch` and `/plan-batch` names the package path; a second instance-2 project per client (`PlantLibrary_<Suite>-DM`). (b) Absorb the rework rows into each `System_V1_Implementation` package. (c) A central workspace in PlantLibrary_Workspace | Code-touching batches must sit in the repository whose code they edit (the worker's working directory is the suite root). (a) is the pilot's shape and the Workspace D4 precedent (F-A4-19). (b) mixes methodology artifacts into V1's package | B6 00 bootstrap; B4 bind contract |
| Q-A4-07 | Is each client's brief a re-skin or a restructure (the 4.1.0 trigger)? | (a) Restructure for all three, recorded at each workspace's prompt 00. (b) Re-skin first (token and literal foundation), restructure later per client. (c) Decide per client after its 01a census | Kickoff B6 names IA and mockups (stages 06b/06c), which exist only behind the restructure trigger (`…/PROMPTS/README.md:46-58`). P-DS-10 left page anatomy untouched, so the operator must say so explicitly | B6 per client from prompt 00 |
| Q-A4-08 | Round-6 rendering tools and all captures are browser automation (F-A4-21, -23). | (a) Deferred-register rows; mockups are authored statically; the operator reviews them by opening the HTML (06c user leg); rendering, sweeps, baselines and captures run in Phase C. (b) A narrow operator exception for `file://` mockup rendering (no app, no slot) | Rule 1 names browser automation explicitly. (a) keeps 06b/06c's mechanical leg static (`run-all` on mockup files) | B6 06b/06c evidence legs |

## §5 Reusable things this brief did not name

- `C:\Programmierung\Design_Template_Kit\examples\anchored-target\` is a complete anchored repository: mirrors, `scripts/design/`, `design/` with 23 contracts, conformance and a validation report. It is the reference shape for B5's done state.
- `…\anchoring-kit\check-parity.mjs` checks skill-mirror parity, including a vendored impeccable. It overlaps with PlantLibrary's harness parity checker (A1/A2).
- `…\anchoring-kit\conductor\check-conductor-readiness.mjs` gives a static readiness verdict for rows 1–7 per client package. Row 8 needs one dispatched UI batch.
- `…\gallery\GALLERY_GOVERNANCE.md` §5 is the baseline-diff classification table, for Phase C.
- The pilot's `RUNBOOK_GUI_REWORK.md` steps R2b (out-of-band P0 bugfixes) and R6b (premise verification and hardening) (`PlantLibrary_Workspace/methodology/Design_Template_Initiative/RUNBOOK_GUI_REWORK.md:322`, `:720`). These are steps the 4.1.0 prompts do not have.
- The pilot's `SCOPE.md` §1 rule "one batch is permitted to move the pin" (`C:\Programmierung\Orchestrator_System\implementation\Design_Migration_V1\SCOPE.md:32-40`).
- Round-6 `research/R3_design-system-brief.md` §0, "eleven traps for the mockup builder", is a pattern for a per-client brief before 06b.
- `…\Design_Migration_V1\exploration\` (`check.mjs`, `directions.json`, `run.mjs`) is direction-exploration scripting. Not read; possibly useful if Q-A4-02 (a) needs candidate values.
- Kit `tools/check-prerequisites.mjs` (`npm run doctor`) is a static prerequisite report.

## §6 Claims to verify

1. **Only `web-css` is exercised by the Kit's tests, though five stacks are implemented.** Check, read-only:
   `grep -n "KNOWN_STACKS =" C:/Programmierung/Design_Template_Kit/anchoring-kit/emitters/emit-stack.mjs; grep -rhoE "'--stacks', '[a-z,-]+'" C:/Programmierung/Design_Template_Kit/anchoring-kit/tests C:/Programmierung/Design_Template_Kit/tests C:/Programmierung/Design_Template_Kit/wizard/tests | sort | uniq -c`
   Expected: five names on line 31; only `'--stacks', 'web-css'` in the counts.
2. **The canon fails 7 pairs, and contrast pairs block `run-all`.** Check, read-only:
   `grep -c '"verdict": "fail"' C:/Programmierung/Design_Template_Kit/examples/plantlibrary-field-ledger/design/semantic-roles.json; grep -n "'Contrast pairs'" C:/Programmierung/Design_Template_Kit/anchoring-kit/checks/run-all.mjs`
   Expected: `7`; line 278 ending in `, true],`. The example equals today's canon import plus write-back (F-A4-06).
3. **Anchoring keys on `<repo>/design/`: the pin is read under the Configuration root, and the worker guard keys on `design/CONFIGURATION.md`.** Check, read-only:
   `grep -n "'conformance', 'CONSUMED_DESIGN.md'" C:/Programmierung/Design_Template_Kit/anchoring-kit/checks/check-pin.mjs C:/Programmierung/Design_Template_Kit/anchoring-kit/install.mjs; grep -n "If this repository contains" C:/Programmierung/Design_Template_Kit/anchoring-kit/conductor/WORKER_INJECTION_BLOCK.md`
   Expected: `check-pin.mjs:49` (`path.join(configRoot, …)`), `install.mjs:230`, and `WORKER_INJECTION_BLOCK.md:13`.

## §7 Delivery

### §7.1 The Kit at 1.7.0 in one page

**What it is.** The Kit holds the schema and the process; a project holds the values (`C:\Programmierung\Design_Template_Kit\README.md:3-6`).

**What a Configuration is.** A folder, not a document (`…\template\TEMPLATE_SPEC.md:41-72`):
- `CONFIGURATION.md`: identity, version, the `## Stacks` table and links; never a design fact.
- `DESIGN_VERSION.md`: semver and changelog, with a "Consumers" line naming each stack's upgrade task.
- The core of four files:
  - `tokens.json`: DTCG primitives;
  - `semantic-roles.json`: the 35 roles plus states and chart per theme, aliases only, and `a11y.pairs`;
  - `conduct-rules.md`: CR-01…CR-12 with this project's parameters;
  - `banned-colors.json`.
- `decisions/`.
- `stacks/<stack>/mapping.md` and `stacks/<stack>/generated/` (never hand-edited).
- `gallery/index.html` and `gallery/baselines/` (23 components × 2 themes at 1.7.0).
- `contracts/{components,patterns,pages}/`.
- `conformance/`: `literal_allowlist.txt`, `CONSUMED_DESIGN.md` (the pin: Kit version and path, Configuration path, sha256 of the four core files), `CONFORMANCE_MATRIX.md`, and optionally `audit_exclude.txt` and `row_audit_commands.txt`.
- Outside the folder: `DESIGN.md` and `.impeccable/design.json` at the repository root.

**DRAFT → BINDING.** The wizard emits `0.1.0` DRAFT (`…\HOW_TO_INSTANTIATE_A_NEW_PROJECT.md:46`). "Your design gate" is the project's own approval: it makes the Configuration `1.0.0` BINDING. After that, every token, role or conduct-rule change is its own task with its own version step (`:48-49`; workflow at `…\TEMPLATE_SPEC.md:539-547`). The status is a field in `CONFIGURATION.md` (`…\template\docs\CONFIGURATION_TEMPLATE.md:23`), and DRAFT/approved strings inside hashed files cost the pilot a re-pin (F-A4-09). For PlantLibrary the path is import, not wizard: the four core-adjacent documents are hand-written, and the gate must also settle the seven failing pairs (Q-A4-02).

**The installer** (`…\anchoring-kit\install.mjs:9-27`, `C:\Programmierung\Design_Template_Kit\anchoring-kit\INSTALL.md:32-45`). In order, it:
- checks that the core is complete;
- copies three skills byte-for-byte into `.claude`, `.codex`, `.agents` and `.github`;
- optionally vendors impeccable and writes `.github/hooks/impeccable.json`;
- writes `scripts/design/` (`check-literals`, `check-banned-colors`, `check-drift`, `check-pin`, `check-gallery-coverage`, `run-all`, `check-parity`, `lib/resolve-roots.mjs`);
- writes `.github/workflows/design-conformance.yml`;
- writes the rule block into `CLAUDE.md` and `AGENTS.md`, before the runtime section, creating `AGENTS.md` if absent;
- seeds `conformance/literal_allowlist.txt` and `CONFORMANCE_MATRIX.md` (never overwritten);
- writes the pin. It refuses to re-pin without `--force` but still exits 0 (`:236-246`).

It never touches product code or the core. Stack emission (`emit-stack.mjs`) is a separate, Configuration-content step (`INSTALL.md:56-65`).

**What the rule block writes into a consumer** (`…\anchoring-kit\rule-block\DESIGN_RULES_BLOCK.md:1-14`):
- the source of truth is `design/CONFIGURATION.md`, pinned in `design/conformance/CONSUMED_DESIGN.md`;
- run `design-gate` before touching any rendered surface;
- no colour, spacing, radius or type literal: consume `design/stacks/<stack>/generated/`; banned colours are hard;
- a new component goes to the Gallery first, through `gallery-governance`;
- after a UI change: regenerate, run `design-audit` on the touched paths, update the matrix; a row closes only when the report is green;
- `Kit: <relative path> @ <version>`; "A prompt never overrides this block".

**The skills.** Three are installed (`…\install.mjs:42`):
- `design-gate`: the pre-work check (E8);
- `design-audit`: the mechanical report, E1–E5 plus the detector;
- `gallery-governance`: a component type added, changed or retired.

The "fourth" is **impeccable**, vendored only with `--with-impeccable` and owned by no Kit. The Kit's two other skills, `design-wizard` and `design-migration`, are Kit-side and cannot be loaded anywhere (F-A4-11).

**Enforcement** is E1–E8 (`…\TEMPLATE_SPEC.md:560-571`). `run-all` blocks on literals, drift, pin, contrast pairs, banned values, and Gallery coverage when a Gallery exists (`…\checks\run-all.mjs:274-281`).

**impeccable's role.**
- The Kit ships none (`…\anchoring-kit\INSTALL.md:89-93`).
- `emit-impeccable.mjs` writes `DESIGN.md` and `.impeccable/design.json` from the Configuration (`C:\Programmierung\Design_Template_Kit\KIT_VERSION.md:930-934`).
- `run-all` runs `impeccable detect` only if it is on PATH, and only as advice (`…\checks\run-all.mjs:493-502`).
- The operator's order (permission mode `auto`, two user-level off-switches) is documented at `…\INSTALL.md:101-129`. Six reductions are still owed (`…\PACKAGE_REVIEW.md:110`).
- In TARGET: AndroidApp and PyApp carry impeccable 3.8.0. Their `live-copy-edit-agent.mjs` has no bypass flags and is byte-identical to the Conductor's (sha256 `1a86b412…`). PyApp still has `.github/hooks/impeccable.json` (reduction 1 is owed). The Dashboard has none, by DTI-06 (`…/INITIATIVE_CLOSEOUT.md:163`).

**Conductor seam.** Two role overrides go into the instance's data directory. The readiness check has eight rows; row 8 needs one dispatched UI batch (`C:\Programmierung\Design_Template_Kit\anchoring-kit\conductor\CONDUCTOR_READINESS_CHECKLIST.md:32-39`).

### §7.2 Emitters

| Stack | Implemented in `emit-stack.mjs` | Tested | What it emits | Consumer in PlantLibrary | Gap |
|---|---|---|---|---|---|
| `web-css` | `C:\Programmierung\Design_Template_Kit\anchoring-kit\emitters\emit-stack.mjs:99-118` | yes (`…\anchoring-kit\tests\install.test.mjs:121-132`, `fk3-outputs.test.mjs:69`, `fk4-walker.test.mjs:32`, `check-drift.test.mjs:39`); proven on the pilot | `tokens.css`: `:root { --token-* }` and one `[data-theme="<THEME>"] { --role-* }` block per theme (scratch: 398 lines, 386 declarations) | Dashboard (React 18 / Vite 5), today fed by its own `scripts/generate-theme.mjs` from flat `tokens.json` | uppercase theme value against the Dashboard's lowercase `dark`; different variable names; Dashboard output sits outside `stacks/*/generated/` (F-A4-15) |
| `web-ts` | `:134-147` | none | `tokens.ts`: `export const tokens` / `roles` (`as const`, resolved hex) | Dashboard TypeScript (today `src/theme/tokens.generated.ts`) | untested; snake_case DTCG keys against the camelCase convention (`PlantLibrary_SharedContracts/design-tokens/platform-mapping-web.md:8`) |
| `tailwind` | `:170-226` | none | `theme.extend.js` (CommonJS) | none (no Tailwind in the Dashboard) | not needed; name mismatch with the spec (F-A4-13) |
| `compose` | `:247-306` | none; never compiled | `Tokens.kt`: `package design.generated`; `object Tokens { Color, Dimension (.dp/.sp), Duration, ZIndex }`; `LightRoles`, `DarkRoles` | AndroidApp `core/design` (`Color.kt`, `Shape.kt`, `Spacing.kt`, `Type.kt`, `Theme.kt`; `Color.kt:18` still the old ramp) | no TextStyle, FontWeight, font family or ColorScheme; nested `Color` name; file outside any Gradle source set; census blind to Kotlin literals (F-A4-02, -03) |
| `qt-qss` | `:321-353` | none | `tokens.py`: `TOKENS`, `ROLES`, `VARS` (386 keys); not a `.qss` file; shadows skipped | PyApp (`app/gui/design_tokens.py`, 623 lines, `LIGHT_THEME` at `:403`; QSS `$app_bg`) | key names differ from PyApp's placeholders; direction inversion; parse-only proof so far (F-A4-16) |
| `flat.json` | `:357-362` | yes (`install.test.mjs:125`) | resolved tokens and roles | any tool | — |

**Plainly: what the Kit cannot do today.**
- It cannot prove its `compose`, `qt-qss` or `web-ts` output: none is tested, and `compose` has never been compiled.
- It cannot see Kotlin or Qt literal forms, so `design-audit` on Android reports green over 167 literals.
- It emits no Compose typography or ColorScheme, and no real QSS stylesheet.
- It renders no native preview: the Gallery is HTML (`dp` is rendered as `px`).

**What that means for Android and PyApp.** In neither case should the answer be hand-written token artifacts pinned to the Configuration. That would be a hand-mirror, which R4 allows only with a drift check and an end date (`C:\Programmierung\Design_Template_Kit\template\TEMPLATE_SPEC.md:537`).
- **PyApp** consumes the generated `tokens.py` directly. A thin hand-written adapter maps generated names to PyApp's names (`PRIMARY`, `LIGHT_THEME`, the QSS placeholders) and transcribes no value. Its static proof in Phase B is a parse of the generated module and a mechanical check that every QSS placeholder resolves.
- **Android** gets the generated `Tokens.kt` plus a hand-written Material3 `ColorScheme` and `Typography` wrapper that references `Tokens.*` only. Its proof needs a Kit session (literal forms, an emitter test, TextStyle) and a Gradle compile. Both go through Q-A4-05; the compile is Q-G-04 (b) or Phase C. Until then, Android's implementation is a deferred lane.

### §7.3 Import

**The exact command.** The tool takes no input path; the canon root is fixed to the main checkout (F-A4-04). This is what was run:

```text
node C:\Programmierung\Design_Template_Kit\tools\import-flat-tokens.mjs --out C:\Users\WindowsAI\AppData\Local\Temp\claude\c--Programmierung-SW-Development\67f41652-8e5e-4d5e-9ab7-afb71be345d9\scratchpad\a4\import\design
```

**What it produced.** Exit 0. It wrote `tokens.json`, `semantic-roles.json` and `banned-colors.json`; `color.secondary.canon_reserved` has 19 steps; `a11y.pairs` has 110 pairs across 5 families.

**Follow-ups, all writing into scratch only:**
- Export round trip (`export-flat-tokens.mjs --config …\a4\import`): 16 groups compared, 0 diffs; LIGHT and DARK roles equal; resolved values equal `true`; exit 0.
- Validator (`--reports-dir …\a4\validate --no-write-back`): schema errors 0/0/0, structural 0, 110 pairs checked with 7 failed, chart checks pass, banned 0; exit 1.
- `emit-stack.mjs --stacks web-css,web-ts,tailwind,compose,qt-qss --out …\a4\stacks`: exit 0, all six artifacts.

**Diff against `examples/plantlibrary-field-ledger`.** The two differ only in the validator's write-back: chart `validated_against` lists, and `measured`/`verdict` on the 110 pairs (7 `fail`). `banned-colors.json` and `roundtrip-report.json` are byte-identical (F-A4-06).

**What the round trip changes relative to `PlantLibrary_SharedContracts/design-tokens/`:**

| Canon (flat) | Configuration (DTCG) | Kind of change |
|---|---|---|
| `PRIMARY`, `NEUTRAL` | `color.primary` (600 marked as anchor), `color.neutral` | rename and wrap |
| `DARK.*` and `EXTRA.*` (19 unique literals, plus one role-only `#1B3A22`) | `color.secondary.canon_reserved.0…900`, ordered by luminance (`…\tools\lib\plantlibrary-mapping.mjs:39-60`) | restructure; `DARK.primary`, `primary_active` and `focus_ring` deduplicated into `color.primary`; `EXTRA.chart_accent` = chart `series_4` |
| `SEMANTIC`, `SEMANTIC_DARK` `{main, light, border, text}` | `color.semantic.<state>.{light,dark}.{main, bg, border, text}` | `light` renamed to `bg` |
| `CHART`, `CHART_DARK` | `color.chart.{light,dark}` plus an added `baseline` | addition |
| `TYPE_SCALE`, `FONT_FAMILY`, `MONO_FONT_FAMILY` | `typography.font.family.{sans,mono}`, `typography.<role>.{size, line_height, weight}` | wrap, with `px` units |
| `SPACE`, `RADIUS`, `BUTTON_SIZES`, `SHELL_SIZES` | `space` (+ `base` 4), `radius` (`pill_input` marked deprecated), `size.button`, `size.shell`, + `size.min_target` 32/44 | additions |
| — | `elevation.policy` flat-by-default, `motion` (120/200/320 ms, standard easing, reduced motion required), `z` 1000–1500 | new Template defaults, not from the canon (`…\import-flat-tokens.mjs:215-249`): new design facts the PlantLibrary gate must accept |
| `semantic-roles.json` with literal hex values | aliases only, plus `a11y` (contrast level, 110 pairs, chart four-check parameters); `meta` replaced | restructure; `meta.contract_version 1.2.0` dropped |
| bans, as prose in `TOKEN_USAGE_NOTES.md` | `banned-colors.json` BAN-01..03 (BAN-02 scoped) | new machine form |

**Do P-DS-01..10 survive as Configuration decisions?** Yes. All ten are restated in the decision record's section A (`…\examples\plantlibrary-field-ledger\design\decisions\DECISION_RECORD_2026-07-10.md:29-40`). Where each lands:
- P-DS-01: `CONFIGURATION.md` Identity and the conduct rules.
- P-DS-02: `color.primary`.
- P-DS-03: `color.neutral`, but six failing `text_muted` pairs.
- P-DS-04: dark roles, `canon_reserved`, `semantic.dark`.
- P-DS-05: `semantic-roles.json`.
- P-DS-06: typography, space and radius, with `pill_input` deprecated.
- P-DS-07: `color.chart`, but `series_3` fails on `app_bg`.
- P-DS-08: `conduct-rules.md` (hand-written).
- P-DS-09: `color.highlight` and the roles.
- P-DS-10: lives outside the core, in the page contracts (RC-A4-25).

P-DS-03 and P-DS-07 survive as decisions, but their evidence (white only) does not survive the Kit's pair set. Their disposition is Q-A4-02.

### §7.4 Where the Configuration lives (Q-G-01)

**What the Kit's anchoring assumes:**
- **Paths are relative.** The pin's Kit path is relative to the consumer root (`…\install.mjs:432`). From `C:\Programmierung\SW_Development\PlantLibrary_<Suite>` it is `../../Design_Template_Kit`. The Configuration path is relative too (`:433`).
- **The Kit is pinned by path and version, not by commit.** Both the pin (`…\template\docs\CONSUMED_DESIGN_TEMPLATE.md:17-18`) and the rule block's `Kit: <path> @ <version>` work this way. Only CI pins a ref, through `vars.DESIGN_KIT_REF` (`…\ci\design-conformance.yml:6-8`).
- **Root resolution** runs `--design-root` → `$DESIGN_ROOT` → the "Configuration path" field in `<repo>/design/conformance/CONSUMED_DESIGN.md` → `design/` (`…\checks\lib\resolve-roots.mjs:45-56`).
- **The pin is always read under the resolved Configuration root** (`…\checks\check-pin.mjs:49`). So under seed option (a), a client-local pin is only a pointer; the hashes checked would be SharedContracts' (F-A4-10).

**What instance 2's worker working directory implies.** The worker runs at the suite's git root (`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:16`), and skills are not discovered from the parent folder (`SW_Development/onboarding/AUDIT_skill-assumptions_2026-09-15.md:169`). Every anchored client therefore needs its own installed skills (the installer does this) and, for the injection guard and readiness row 1, its own `design/CONFIGURATION.md` (`…\conductor\WORKER_INJECTION_BLOCK.md:13`).

**What the submodule topology implies.**
- Every client is a separate GitHub repository. A standalone clone or the CI job has no sibling `PlantLibrary_SharedContracts`.
- Rule-5 worktrees at `C:\Programmierung\SW_Development_wt\<repo>-<lane>` keep `../../Design_Template_Kit` resolvable (same depth) but lose `../PlantLibrary_SharedContracts`. The Dashboard's generator already has this flaw (`PlantLibrary_Dashboard/scripts/generate-theme.mjs:29-32`).

**Evidence for each option:**

| Option | `TEMPLATE_SPEC` §3.1 | Pin checked per client | Rule block, guard, row 1 | CI and worktrees | Writes |
|---|---|---|---|---|---|
| Seed (a) as worded | one per system ✓ | no (the shared pin is read) | broken (no `design/` in the client) | broken (sibling absent) | install writes into SharedContracts |
| (b) per client | violates "never per suite" | ✓ | ✓ | ✓ | three gates, three versions, R2 broken |
| **Hybrid (Q-A4-01 (a))** | one canonical ✓ | ✓ (each client's own `conformance/`) | ✓ | ✓ | edits only in SharedContracts; clients re-sync as their upgrade task |

**Recommendation.** Q-G-01 (a) in substance: SharedContracts is the one Configuration, built as Q-A4-01 (a). The hybrid also matches SDA-DEC-01 "siblings now": `design/` is a new sibling folder, and `design-tokens/` stays as the flat export until the clients move off it.

### §7.5 Per-client GUI rework shape (methodology 4.1.0)

**Stage list for one client** (restructure order: `PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/PROMPTS/README.md:46-58`; phases at `…/GUI_IMPROVEMENT_STRATEGY.md:135-155`). Each stage with what Phase B can do:
1. **00 Bootstrap.** Workspace from templates, pin (`SCOPE.md` §1 the pilot's way), re-skin or restructure recorded in `STATE.md`.
2. **01 Source inventory plus mechanical census.** The census is `run-all.mjs`, static.
3. **01a Function/UI census.** Routes, views and subsystem reach (with a stack adapter: React routes, Compose nav graph, Qt windows); `CM-*` gaps.
4. **02 Screen contracts.** Roles and Gallery IDs per region.
5. **03 Capture.** Phase B records "unavailable: rule 1"; deferred.
6. **04 Target normalisation.**
7. **05 Comparison.** Against contracts and source only; the visual leg is deferred.
8. **06 Gap map.**
9. **06a Forward surface and information model.** Open V1 rows classed `reserve` / `absorbed` / `no-UI`; settings classified; user gate.
10. **06b IA, then mockup.** The IA goes to the user first. Then page and pattern contracts and fixture-driven page mockups are written into the Configuration's `contracts/`, `gallery/pages/` and `gallery/fixtures/`, which means into SharedContracts (`…/PROMPTS/README.md:20`). Version step; gate.
11. **06c Mockup audit.** The mechanical leg is static; the rubric and placement legs are reading work; the user-review leg is the operator opening the HTML; gate.
12. **06d Change classification.** `bugfix` / `additive-silent` / `amendment` / `already-owned`; the amendment is drafted in PlantLibrary's own format; waves; gate.
13. **07 `plan-batch`.**
14. **08 `SCOPE.md`.**
15. **Implementation** with mechanical design checks only.
16. **09/10 Visual gates and final acceptance.** Deferred to Phase C.

**Where each workspace lives.**
- **The pilot:** `C:\Programmierung\Orchestrator_System\implementation\Design_Migration_V1\`, inside the repository whose GUI it migrated (`…\README.md:1-14`). Its naming deviation, keeping methodology file names against the `<TYPE>_<topic>_<date>` rule, is recorded at `:52-61`. Its `planning/`, `proposal/` and `handovers/` follow the rule and carry an `INDEX.md`.
- **For PlantLibrary:** one workspace per client suite, at `PlantLibrary_<Client>/implementation/Design_Migration_V1/`, not in Workspace. Code-touching batches must run from the suite root; Workspace keeps the methodology (pinned exempt-tree) and SDA.
- **Hygiene.** `implementation/` is not a declared root in the clients (`PlantLibrary_Dashboard/hygiene/CONSUMED_HYGIENE.md:21-26`; the same in AndroidApp and PyApp), so methodology names need no exemption. The workspace's `planning/`, `proposal/` and `handovers/` get root declarations by D-entry (B3).
- **Dispatch.** Path-named invocation and a second instance-2 project per client (Q-A4-06, F-A4-19).
- **Single-writer pressure.** The 06b/06c writes into SharedContracts serialize the three clients there (kickoff rule 5).

**What the pilot's round runbooks looked like.**
- **The legacy design-track runbook** ran R1 to R10. Its steps: R1 audit → `G-P6a`; R2 forward surface → `G-P6a1`; R2b out-of-band P0 bugfixes; R3 IA and full mockup → `G-P6a2`; R4 mockup audit → `G-P6a3`; R5 change classification and amendment → `G-P6a4`; R6 batch derivation → `G-P6b`; R6b premise hardening; R7 batch execution (preamble, per-batch blocks); R8 visual gates → `G-P6d`; R9 merge and R9+ follow-ups; R10 readiness and closeout → `G-close` (`PlantLibrary_Workspace/methodology/Design_Template_Initiative/RUNBOOK_GUI_REWORK.md:158-1391`).
- **Design rounds 4–6** each followed the same arc: decision pack (round 4: `Q-R4-1`…`22`, `…\planning\PROMPT_gui-round-4-decisions_2026-10-05.md:1-54`) → gate → cut batches → Kit half (`gallery-governance` on a Kit branch) → batches → merge → captures → re-gate → operator signs.
- **Round 5 in detail:** 20 steps `dr5-1`…`dr5-20`, a step-map table (model, route, working directory and branch, precondition, writes), a lanes table, and §7 as ledger (`…\planning\PLAN_design-round-5_2026-10-09.md:63-108`).
- **What it delivered:** 86 batches and 274 rows by round 5 (`…\TASK_CHECKLIST.md`); literals 265 → 0; Configuration 1.0.0 → 1.15.0 (`C:\Programmierung\Orchestrator_System\design\conformance\CONSUMED_DESIGN.md:17-27`).

**Round-6 tooling: what transfers without a running app.**

| Item | Transfers in Phase B? | Why |
|---|---|---|
| Research lanes R1–R5 (code inventory, data vs display, design-system brief, planned work, normative requirements) | yes | reading and grep only |
| R6 visual critique | partly | from source and contracts; the screenshot half is deferred |
| R7-style special-topic lane | yes | reading |
| Proposal skeleton (items, governance, superseded decisions, delivery, questions, risks) | yes | document |
| Mockup kit (generated `tokens.css`, Gallery `pages.css`, shell `kit.js`, fixture `data.js`, `AUTHORING.md`, `BRIEFS.md`, per-page notes) | yes, authored statically | static HTML, no build (`C:\Programmierung\Conductor_GUI_Reconciliation_2026-10-12\mockups\AUTHORING.md:1-4`) |
| `LANDING.md` plus `MANIFEST.sha256` | yes | byte-pinned landing |
| `tools/shot.py`, `sweep.py`, `after_shots.sh` | no → deferred | Playwright Chromium (F-A4-21) |
| `compare.html` "before" images, Working_Folder `capture_r3*.py` | no → deferred | need the running product |
| Gallery baseline capture, Kit browser tests | no → deferred | Playwright |

**Deferred-register candidates from this lane** (for R-2 to merge; none is run here):
- Gallery baseline capture of SharedContracts `design/gallery/` (Kit `gallery/capture-baselines.mjs`, Playwright), after B5 BINDING.
- Current-state captures per client (methodology phase 3): Dashboard through `webapp-testing`, PyApp through `gui-validation`, AndroidApp through `android-validation`, after each client's 02.
- Mockup render and sweep (round-6 `shot.py`/`sweep.py` pattern) per client, after 06b/06c.
- Gradle compile of AndroidApp `core/design` against the generated `Tokens.kt`, after the B5/B6 Android wiring.
- Visual gates and final acceptance (prompts 09/10) per client, after implementation.
- Readiness row 8 on instance 2 (one dispatched UI batch per anchored client), after the B8 role override.
- First run of the `design-conformance` CI job after the operator's push (Q-G-03).

**Order evidence for Q-G-08:**
- B5 must precede B6 everywhere. S0/00 pins a BINDING Configuration, and a canon with failing pairs leaves every row red (F-A4-07).
- Within each client, foundation comes before bugfix (`C:\Programmierung\Design_Template_Kit\HOW_TO_INSTANTIATE_A_NEW_PROJECT.md:143-144`).
- **Dashboard first:** the only proven stack (`web-css`, tested and piloted); complete census coverage (`.ts`, `.tsx`, `.css`); HTML mockups map one to one; `tsc --noEmit` is an allowed type check.
- **PyApp second:** `qt-qss` emits; the census covers `.py` and `.qss` hex; parse and placeholder-resolution checks are static. It needs the adapter and the inversion decision.
- **Android last:** an untested, uncompiled emitter, a blind census, and native rendering absent from the Gallery. It needs the Q-A4-05 Kit session and a compile.

This supports Q-G-08 (a), with "proven emittable" defined as above: all three are planned, the Dashboard is implemented first, PyApp follows its static proof, and Android waits for the Kit session and a compile.

### §7.6 design-adoption versus design-gate (Q-G-07)

| | `design-adoption` (`SW_Development/.claude/skills/design-adoption/SKILL.md`) | `design-gate` (`C:\Programmierung\Design_Template_Kit\anchoring-kit\skills\design-gate\SKILL.md`) |
|---|---|---|
| Fires | before UI edits in the three clients (`:17-25`) | before any rendered-surface edit; triggers are a row's `skill`, `design_context: required`, or an explicit request (`:54-72`) |
| Reads | SharedContracts `design-tokens/*`, the platform mappings, the P-DS record (`:27-39`) | the resolved Configuration: core, mapping, contracts, Gallery, pin, matrix, allowlist, decisions (`:74-102`) |
| Checks | which P-DS applies (`:46-49`); the suite's adoption row (`:55-65`) | pin against version, an open adoption row through the "Consumers" line and `partial` matrix rows, the matrix row, Gallery-first, the regeneration plan (`:110-135`) |
| Rules | hard-coded hex values and bans (`:69-81`), contradicting `:12-15` | value-free; parameters read from `conduct-rules.md`; closes with `design-audit` (`:137-171`) |
| Installed where | superproject `.claude` and `.codex` only; in no client (F-A4-18) | every anchored repository, four mirrors, plus the Conductor injection block |
| Named by rows | 6 rows (`WD-V1-DS-01/06`, `AN-V1-DS-01/05`, `PY-V1-DS-01/03`) | none yet |

**Overlap.** `design-gate` is declared "the parameterised form of the house design-adoption gate" (`…\design-gate\SKILL.md:8-11`). Its §1–§6 restate `design-adoption`'s purpose and structure without values. Only two things are unique to `design-adoption`, and both have Configuration homes:
- the P-DS-to-area map, which moves to `decisions/` and `conduct-rules.md`;
- the adoption-rows table, which moves to `DESIGN_VERSION.md` "Consumers" and the matrix's `partial` task IDs.

**Evidence for Q-G-07 (a).** Retire `design-adoption` once B5 has anchored all three clients. Until then it is the only gate with a canon to read. Leave a pointer file, and re-point the six skill cells to `design-gate` through plan-batch, recorded in each package's STATE. Do not retire it earlier: `design-gate` resolves nothing before a Configuration exists (`:20-42`).

### §7.7 Static checks available in Phase B (Q-G-04)

| Check | Command (outputs to scratch unless a cited report is intended) | What it proves |
|---|---|---|
| Core validation (E4) | `node C:\Programmierung\Design_Template_Kit\tools\validate-configuration.mjs <config> --reports-dir <scratch> --no-write-back` | schema, aliases resolve, every `a11y.pairs` entry in both themes, chart four-check, banned list |
| Canon round trip | `node C:\Programmierung\Design_Template_Kit\tools\export-flat-tokens.mjs --config <scratch copy containing design/>` | the Configuration's resolved values equal the flat `design-tokens/`. It writes `roundtrip-report.json` beside `design/`, so run it on a copy |
| Stack emission | `node C:\Programmierung\Design_Template_Kit\anchoring-kit\emitters\emit-stack.mjs --config <config> --stacks <list>` | generation only (reproducible; drift-checked next) |
| Drift (E2) | `node scripts/design/check-drift.mjs` | committed `stacks/*/generated/` (and `DESIGN.md` with impeccable) equal a fresh re-emission |
| Pin (E1) | `node scripts/design/check-pin.mjs` | the four core sha256 match `conformance/CONSUMED_DESIGN.md` |
| Literal census and bans (E3) | `node scripts/design/check-literals.mjs --paths <a,b>` or `--paths-from <file>` | no un-allowlisted colour or dimension literal and no banned value in those files. Blind to Compose and Qt forms (F-A4-03) |
| Matrix completeness (E5) | `node scripts/design/check-gallery-coverage.mjs` | component set, contracts and matrix rows agree; the baselines dimension is `not_applicable` until a capture exists |
| Aggregate row audit | `node scripts/design/run-all.mjs --paths <a,b> --kit-root <kit>` (no `--base-ref`, no `--with-audit`) | the six blocking sections in one verdict; the report goes to scratch; `impeccable detect` runs only if on PATH (advice only) |
| Mirror parity | `node scripts/design/check-parity.mjs` | the installed skill mirrors are byte-equal |
| Conductor readiness rows 1–7 | `node C:\Programmierung\Design_Template_Kit\anchoring-kit\conductor\check-conductor-readiness.mjs --target <repo> --conductor <data_dir> --package <pkg>` | install, parity, rule block, hook, CI job, design checks on UI rows, worker injection (row 8 is deferred) |
| Gallery page | `node C:\Programmierung\Design_Template_Kit\gallery\generate-gallery.mjs --config <config>` | static generation; the page records digests for freshness |
| Methodology lint | prompt 11 step 1 (a)–(e) greps (`…/PROMPTS/11_PACKAGE_REVIEW_VALIDATION_PROMPT.md:50-66`) | 15-column header, six statuses, parameterised root, no driver cache, index complete |
| Generated-artifact language checks | TypeScript `tsc --noEmit` over the Dashboard with `tokens.ts`; Python AST parse of `tokens.py` | type and syntax validity without running anything. Kotlin has no static equivalent without Gradle, so proving Compose requires Q-G-04 (b) or Phase C |

Not static, and therefore deferred: `gallery/capture-baselines.mjs`, the Kit's browser tests, captures and visual gates, readiness row 8. `gallery/compare-baselines.mjs` is a static pixel diff, but it is useful only once captures exist.
