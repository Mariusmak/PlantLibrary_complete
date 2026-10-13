# GUI current state — PlantLibrary_Dashboard — lane A9 (read-only analysis, 2026-10-13)

*Lane A9-dashboard, Phase A, read-only static scan. Dashboard @ `7795fc8` (main), SharedContracts @ `d43f7a2`,
Server @ `f1a31b9` (route count only), Workspace @ `6b4b88b`, Design_Template_Kit @ `f08e588` (two files only).
Tools used: Read/grep/find/wc/diff/awk over files; no node, npm, build, browser or screenshot. Nothing was run.*

## §0 Summary

1. The Dashboard already has a working token pipeline: `scripts/generate-theme.mjs` flattens SharedContracts `tokens.json` into `src/theme/tokens.generated.{css,ts}`, imported once at `src/main.tsx:8`. A static diff shows the committed CSS **equals canon 1.2.0** (231/231 leaves, 134/134 hex values, all numerics). The regeneration happened in `321307b` (2026-07-15), outside any row: `WD-V1-DS-06` still reads `todo`, and the `WD1-B07` drift evidence (26 mismatches) is out of date.
2. Literal hygiene is very high. Outside the generated files there are **0 hex**, 1 `rgb()`, 0 font-family literals, 0 shadows, 0 Tailwind (no Tailwind, no CSS modules, no CSS-in-JS: two global stylesheets carry 1,587 of 1,629 hand-written CSS lines). There are 86 px/rem occurrences in 2 files (45 border/outline widths, 29 layout, 3 breakpoints, 8 misc). 551 `var(--…)` references use 110 of the 231 tokens.
3. The real gap is **roles and dark theme**, not literals. CSS binds primitives directly. `semantic-roles.json` is never consumed. Only the `DARK` group switches theme. 0 of 28 `SEMANTIC_DARK` vars and 0 of 8 `CHART_DARK` vars are used. 38 light fills are covered by only 20 dark-override selectors. Body background is `neutral-50`, but the role says `neutral-100`. Charts use legacy aliases. `--radius-pill-input` (deprecated) is still used twice.
4. The canon contradicts itself. `TOKEN_USAGE_NOTES.md` and the design-adoption skill ban `#16A34A` "anywhere", yet canon P-DS-07 keeps it as `CHART.series_1`. As a result `check-token-drift.mjs` can never exit 0: it finds 4 hits in the generated files. The Kit's example `banned-colors.json` (BAN-02) already scopes this ban correctly.
5. There is no pin: no `design/`, no `CONSUMED_DESIGN.md`, no `CONSUMED_CONTRACTS.md`. The generator reads a sibling path. The Kit emits `--token-color-*` names, while the Dashboard uses `--primary-600`-style names, so a migration needs a rename or an alias layer.
6. Screens: 13 routes → 12 page components → 11 desktop-web page contracts. `/login` has no contract of its own. The settings sub-routes and the plant-instance route differ from their contracts. There are no local 1.2.0 mockups: the approved set is a claude.ai artifact URL. The 13 local legacy HTML mockups contain banned greens. The only screenshots (16 PNG, 2026-07-08) predate 1.2.0.
7. Census Pass A (static): 42 server operations; the UI reaches 13 (11 generated-client methods + `/auth/login` + the callback). 29 are unreached, 5 of them infrastructural.
8. Mechanical checks available without a build: `npm run lint` (eslint 9) and `tsc -b` (type leg; root `noEmit`, writes only cache and referenced `.d.ts` into `node_modules/`), plus the hygiene checker. There is no stylelint and no raw-literal lint.
9. Six operator questions (Q-A9D-01..06) and twelve reuse candidates. Nine visual or behavioural items need a running app and are named for the deferred register (§7.6.3).

## §1 Coverage

| Item | Status (read / partly read / not read) | Reason |
|---|---|---|
| Kickoff prompt §1, §2, §4 | read | brief rule 6 |
| Dashboard `src/` tree, file and line counts | read | full listing + `wc` |
| `src/main.tsx`, `src/app/router.tsx`, `src/app/routes.ts`, `src/app/Shell.tsx` (1–80), `src/theme/*` (hand-written), `src/api/client.ts`, `src/api/garden.ts` | read | entry, routing, theme, API adapter |
| `src/components/components.css`, `src/pages/pages.css` | partly read | grep-scanned in full for literals/vars/selectors; read line by line only around findings |
| Page components `src/pages/**/*.tsx` | partly read | grep only (API calls, inline styles, disabled/deferred surfaces) |
| `package.json`, `package-lock.json` (versions), `vite.config.ts`, `tsconfig*.json`, `eslint.config.js`, `.prettierrc.json`, `playwright.config.ts`, `.gitignore`, `.github/workflows/repo-hygiene.yml` | read | stack facts |
| `scripts/generate-theme.mjs`, `scripts/check-token-drift.mjs` | read | token pipeline |
| `tests/`, `e2e/` | partly read | listed; `e2e/validation-smoke.spec.ts` header and `goto`/`shot` lines only; nothing run |
| Dashboard `CLAUDE.md` (1–60), `docs/WD-DESIGN-01_token_integration.md` | read | |
| `docs/WD-UX-10_mockup_parity_report.md`, `docs/WD-MOCKUP-UPGRADE_PROPOSAL.md` | partly read | first ~30 lines |
| `implementation/System_V1_Implementation/TASK_CHECKLIST.md` | partly read | all row IDs + full DS rows |
| `…/TASK_CONTEXT.md` | partly read | DS-06, DS-05, QA-01, CI-01 sections |
| `…/STATE.md`, `…/validation/WD1-B07_token_drift.md` | partly read | DS mentions; B07 evidence in full |
| `…/BATCH_PLAN.md`, `SCOPE.md`, `DRIVER_SCRIPT.md` | not read | row data came from the checklist; no batch goal paragraph needed for this brief |
| `implementation/MVP/package/TASK_CHECKLIST.md` | partly read | row IDs and scope cells for WD-PAGE/WD-UX |
| `implementation/MVP/handoffs/Dashboard_Completion_Handoff.md` | not read | context budget; MVP is terminal |
| SharedContracts `design-tokens/` (tokens.json, semantic-roles.json, TOKEN_USAGE_NOTES.md, platform-mapping-web.md, README) | read (tokens.json: lines 1–30, 150–277 plus a full mechanical hex/numeric extraction; semantic-roles.json: meta + group keys) | canon |
| SharedContracts `page-contracts/desktop-web/` | partly read | file list + the "Web route" line of each of the 11 contracts |
| SharedContracts `openapi/plantlibrary.openapi.yaml` | partly read | paths, methods, operationIds extracted mechanically |
| Server `app/api/routes/*.py` | partly read | decorator count per module only (census cross-check) |
| Workspace `System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | read | P-DS-01..10 |
| Workspace `System_Design_Architecture/STATE.md` | partly read | SDA-DEC-01..05 rows and the last decision line |
| Mockups folder in Workspace | read (absent) | `find -iname '*mockup*'` under the Workspace: none. The approved artifact is a URL (`04_*:5`), not opened |
| Methodology 4.1.0: `FUNCTION_UI_CENSUS_TEMPLATE.md`, `PROMPTS/01a_…`, `PROMPTS/01_SOURCE_INVENTORY.md` (1–100) | read | census shape |
| Methodology `PROMPTS/06a_…`, `PROMPTS/06b_…`, `FORWARD_SURFACE_TEMPLATE.md`, `INFORMATION_ARCHITECTURE_TEMPLATE.md`, `INFORMATION_MODEL_TEMPLATE.md` | partly read | purpose, inputs, headings only |
| Superproject `.claude/skills/design-adoption/SKILL.md` | read | gate assumptions |
| `references/PlantLibrary_pythonApp_old/` | partly read | listing + colour grep of the 13 mockups |
| Kit `examples/plantlibrary-field-ledger/design/` | partly read | `banned-colors.json` BAN-02, the var-naming grep, the baseline count. A4 owns the Kit |
| Existing evidence PNGs (Workspace MVP evidence, Dashboard OIDC evidence) | not read | listed only; no image viewing in a static lane |
| Workspace system-level acceptance rows (SYS-*) | not read | context budget; Dashboard WALK rows used instead |
| `dist/`, `node_modules/`, `test-results/`, `*.tsbuildinfo` | not read | generated/vendor, git-ignored |

Counts: 31 items, of which 11 read, 15 partly read and 5 not read. The "read (absent)" row for the mockups folder and the partial "read" row for the design-tokens folder are both counted as read.

## §2 Findings

**F-A9D-01 — Generated tokens already equal canon 1.2.0. The adoption row and its evidence lag behind.**
`PlantLibrary_Dashboard/src/theme/tokens.generated.css` declares 231 custom properties, which matches the 231 leaves of `PlantLibrary_SharedContracts/design-tokens/tokens.json`. The sorted multiset of 134 hex values is identical (case-normalised), the numeric values are identical, and both font stacks are present (`tokens.generated.css:217-218`). Dashboard commit `321307b` (2026-07-15, "Reconciled MVP Gaps") rewrote both generated files (+135/−53), five days after `0357313` recorded the 1.1.0 drift. Meanwhile `PlantLibrary_Dashboard/implementation/System_V1_Implementation/TASK_CHECKLIST.md:37` still shows `WD-V1-DS-06` as `todo`. `…/validation/WD1-B07_token_drift.md:19-21` (26 mismatches, 50 additions, 12 banned hits, exit 1) no longer describes the tree: only the 4 `#16A34A` hits would remain (F-A9D-09).

**F-A9D-02 — Tokens are consumed by path, with no version pin.**
`PlantLibrary_Dashboard/scripts/generate-theme.mjs:29-32` reads `../PlantLibrary_SharedContracts/design-tokens/tokens.json` directly. `tokens.json` carries no version. The version exists only in `PlantLibrary_SharedContracts/design-tokens/semantic-roles.json:5` (`contract_version 1.2.0`) and in the bundle-wide `CONTRACT_VERSION.md`. The Dashboard has no `design/`, no `CONSUMED_DESIGN.md` and no `CONSUMED_CONTRACTS.md` (the last is row `WD-V1-DS-04`, deferred, `TASK_CHECKLIST.md:38`). Its only `CONSUMED_*` file is `hygiene/CONSUMED_HYGIENE.md`. `generate:theme` runs automatically before dev and build (`package.json:10,12`), so any edit to the sibling canon silently re-themes the next build.

**F-A9D-03 — Very low literal residue.**
After excluding generated and vendor files there are no hex literals in `src/`. There is one `rgb()` (`src/components/components.css:678`), no `font-family` literal (all three uses are `var(--font-family|--mono-font-family)`: `components.css:14`, `src/theme/base.css:19,33`), no `box-shadow`, and no Tailwind classes (`grep` of `(bg|text|border)-(green|gray|…)-NNN` → 0). Radius: 46 `var(--radius-*)` uses, 4 `var(--button-sizes-*-radius)` uses and one `inherit` (`components.css:338`). Inline style props: 4, all of them dynamic (`ConfidenceBadge.tsx:84`, `LocationTree.tsx:99` (which uses `var(--space-4)`), `StatisticsPage.tsx:163,246`). The header rules in `src/theme/index.ts:1-8` and `src/theme/base.css:1-5` ("no literal …") are honoured.

**F-A9D-04 — Some literals sit where the canon has no token, plus one that duplicates a token.**
`components.css:678` `rgb(17 26 20 / 0.28)` is `NEUTRAL.900 #111A14` at 28 %: a duplicated token value with alpha, and the canon has no scrim role. Breakpoint `@media (max-width: 1100px)` appears 3 times (`components.css:757`, `pages.css:355,815`), while the canon defines `SHELL_SIZES.sidebar_compact_breakpoint 900` and `toolbar_compact_breakpoint 1200` (`tokens.generated.css:213-214`), which CSS cannot use inside `@media`. Also: z-index `1000` (toast, `components.css:447`), `900` (command palette, `:673`) and `-1` (`pages.css:612`); opacity `0.62` (disabled, `components.css:66`) and `0.35` (`pages.css:614`); 45 border/outline widths (1/2/3 px); icon boxes `1.25rem` (`pages.css:470-471,484-485`). The canon has no tokens for border width, z-index, opacity, scrim or elevation. This is a Configuration gap, not a client defect.

**F-A9D-05 — The semantic-role layer is not consumed, and the app background binds the wrong step.**
The generator emits primitives only. Neither `scripts/` nor `src/` references `semantic-roles.json` (grep → 0). The body background is `var(--neutral-50)` (`src/theme/base.css:22`, again for `.shell` at `components.css:544`), while the role `LIGHT.app_bg` is `#F5F7F2` = `NEUTRAL.100` (`semantic-roles.json:8`). This is item 4 of `WD-V1-DS-06` (`TASK_CONTEXT.md` §WD-V1-DS-06) and is still open.

**F-A9D-06 — Dark-theme coverage is structurally incomplete (static evidence; visual impact deferred).**
Only the `DARK` group lands under `[data-theme="dark"]` (`generate-theme.mjs:128,132-134`). Every other primitive is theme-invariant, so each light fill needs a hand-written override. There are 20 dark-override selectors in total: 13 in `components.css` (`:112, :546, :579, :733-751`) and 7 in `pages.css` (`:340-350`) (`base.css` adds 2). Against these stand 38 light fills (`--neutral-0/50/100`, `--semantic-*-light`, `--primary-50/100`), for example the notice panels `components.css:272-287`, status/confidence/readiness badges `:304-318, :365-381, :484-496`, and calendar markers `pages.css:474,480`. There are 44 theme-invariant `color: var(--neutral-*)` declarations (20 + 24). Usage is 0 of 28 `--semantic-dark-*` and 0 of 8 `--chart-dark-*`, and `--dark-focus-ring`, `--dark-on-accent`, `--dark-accent-soft`, `--dark-accent-border` and `--dark-surface4` are all unused. The claim in `docs/WD-DESIGN-01_token_integration.md` ("components … therefore theme-switch automatically") is false for every non-`DARK` primitive. The canon calls this a defect: `TOKEN_USAGE_NOTES.md:93-95`, `design-adoption/SKILL.md:75-76`.

**F-A9D-07 — Charts use legacy aliases and have no dark palette.**
`--chart-primary`, `--chart-secondary` and `--chart-warning` appear at `src/pages/pages.css:407,414,422,426,617,620`; `--chart-series-1..4` are never used. The canon says "new code uses the `series_*` names" (`TOKEN_USAGE_NOTES.md:67-69`), and P-DS-07 requires `CHART_DARK` on dark backgrounds (`04_APPROVED_DESIGN_REVISION_2026-07-10.md:35`).

**F-A9D-08 — The deprecated `pill_input` radius is still used.**
`src/components/components.css:655` and `src/pages/pages.css:133` use `var(--radius-pill-input)`. It is deprecated by P-DS-06 (`TOKEN_USAGE_NOTES.md:72-75`) and is item 3 of DS-06.

**F-A9D-09 — The banned-green rule contradicts the canon, so the drift checker can never pass.**
`TOKEN_USAGE_NOTES.md:27-29`, `.claude/skills/design-adoption/SKILL.md:71-72` and the done-when of DS-06 (`TASK_CHECKLIST.md:37`) all ban `#16A34A` "anywhere". The canon keeps it as `CHART.series_1` and `CHART.primary` (`tokens.json:157,161`), validated by P-DS-07 (`04_*:35,54-57`). `scripts/check-token-drift.mjs:29-31,104-116` greps all of `src/`, including the generated files, and exits 1 on any hit (`:153`). Today it hits `tokens.generated.css:100,104` and `tokens.generated.ts:91,95`, so `WD-V1-DS-07`'s "exits 0 once DS-06 is done" (`TASK_CHECKLIST.md:44`) cannot come true. The Kit's round-tripped example already resolves this: BAN-02 is "Scoped (not \"everywhere\") … the ban is on accent/fill usage, not the chart palette" (`Design_Template_Kit/examples/plantlibrary-field-ledger/design/banned-colors.json:25,37`). Also, DS-07's description says the script reads `semantic-roles.json` (`TASK_CHECKLIST.md:44`), but the script reads only `tokens.json` (`check-token-drift.mjs:24-28`).

**F-A9D-10 — The TypeScript token module has no product consumer.**
`src/theme/tokens.generated.ts` (172 lines) is imported only by `tests/theme/tokens.test.ts:4`, and `src/theme/index.ts` re-exports it but nothing in `src/` imports `@/theme`'s `tokens`. Its header mandates `tokens` "for any value-level access" (`src/theme/index.ts:1-8`), yet the chart widths are computed percentages and the colours all come from CSS.

**F-A9D-11 — The web platform mapping in the canon is stale.**
`PlantLibrary_SharedContracts/design-tokens/platform-mapping-web.md:7` gives `--primary-600: #16A34A` as its example (1.2.0 value: `#2A7A30`). `:5` and `:8` name `scripts/generate_clients.py` (`SC-GEN-01`) and `generated/typescript/tokens.ts` as the producers, but `generated/typescript/tokens.ts` does not exist and `generate_clients.py` emits only API clients. The Dashboard uses its own generator. `:20` (the divergence rule: "no new … literals outside tokens.json") still holds.

**F-A9D-12 — Routes and page contracts have drifted apart.**
Settings: the contract has `/settings`, `/settings/account`, `/settings/providers`, `/settings/sync` (`page-contracts/desktop-web/PageContract_settings.md:6`); the code has `/settings/:section` with `appearance`, `data-sources`, `tasks-reminders`, `storage-data` (`src/app/routes.ts:110`, `src/app/router.tsx:47-48`). Plant detail: the contract's `/plants/:profileId/instances/:instanceId` (`PageContract_plant_detail.md:6`) is not routed. `/login` maps to `PageContract_shell.md` (`routes.ts:23-28`), which says the shell is "not a routed page", so Login has no contract of its own. `/plants/new` shares `PageContract_plants.md` (`routes.ts:41-46`), and that contract names no `/plants/new` route.

**F-A9D-13 — A package row cites a path that does not exist.**
`WD-V1-QUERY-03` names `src/pages/plants-new/` (`TASK_CHECKLIST.md:30`). The wizard is `src/pages/plants/AddPlantWizardPage.tsx`.

**F-A9D-14 — Operation reach (census Pass A, static).**
The Server declares 42 route decorators (`PlantLibrary_Server/app/api/routes/*.py`): 40 under `/api/v1`, which equals the SharedContracts snapshot (40 operationIds in `openapi/plantlibrary.openapi.yaml`), plus `/auth/login` and `/auth/callback`. The UI calls 11 distinct generated-client methods (`src/api/garden.ts:18`, `src/pages/*/*-queries.ts`), plus `/auth/login` (`src/pages/login/LoginPage.tsx:17`), plus the callback by redirect. That makes 13 reached and 29 unreached (5 of them infrastructural: health ×2, metrics, client-devices ×2). Plant detail resolves through `listPlantInstances` (6 call sites), not `getPlantInstance`. `ClientDevicesApi`, `HealthApi` and `MediaApi` are deliberately not instantiated (`src/api/client.ts:26-29`).

**F-A9D-15 — Shell tokens are partly unused, and a code comment is stale.**
Unused: `--shell-sizes-sidebar-compact-width`, `--shell-sizes-sidebar-compact-breakpoint`, `--shell-sizes-toolbar-compact-breakpoint`, `--shell-sizes-minimum-height`, `--radius-nav`, `--radius-xl`, and all four `--button-sizes-*-icon-size`. The comment at `src/app/Shell.tsx:7-12` says the styling "land[s] in `WD-B02`", which is done in the MVP package. `docs/WD-UX-10_mockup_parity_report.md` claims "1024 px compact behavior", but the only breakpoint in the CSS is 1100 px (F-A9D-04), so that claim needs a viewport check (§7.6.3).

**F-A9D-16 — The only local mockups are legacy. The approved ones are remote.**
The 1.2.0 approved mockups are "https://claude.ai/code/artifact/370bf3f9-…" (`04_APPROVED_DESIGN_REVISION_2026-07-10.md:5`): 12 screens, 4 per client, light and dark (`:86-87`). No Workspace folder holds mockups. The 13 local HTML mockups in `PlantLibrary_Dashboard/references/PlantLibrary_pythonApp_old/mockups/` contain the banned greens (12 of 13 files have 1–3 hits each), so they are pre-1.2.0 structural references only. The Kit's example carries 47 gallery baseline PNGs derived from the canon (`Design_Template_Kit/examples/plantlibrary-field-ledger/design/gallery/baselines/`).

**F-A9D-17 — No visual baseline exists after 1.2.0.**
`e2e/validation-smoke.spec.ts:17-20` writes screenshots into `PlantLibrary_Workspace/implementation/System_Integration_MVP/validation/evidence/MVP-VALIDATION-20260708-01/playwright/`. There are 16 PNGs there, dated 2026-07-08, one week before the regeneration of 2026-07-15. The OIDC evidence (`implementation/System_V1_Implementation/validation/evidence/WD-V1-LOCAL-OIDC-20260715-01/`, 5 PNGs) covers login and settings only. `playwright.config.ts` has no `webServer` and needs the live stack (Dashboard `CLAUDE.md:20-25`). SDA-DEC-03 (parity screenshot tooling) is still `open` (`System_Design_Architecture/STATE.md:23`).

**F-A9D-18 — Mechanical check surface.**
There is no `typecheck` script (`CLAUDE.md:18-19`). The type leg is `tsc -b`, the first half of `build` (`package.json:13`). The root `tsconfig.json` has `noEmit: true` and references `tsconfig.generated.json` (`tsconfig.json:12,26`), whose composite project emits declarations into `node_modules/.generated-client-build` (`tsconfig.generated.json:9`, present on disk). `eslint.config.js` lints `src/`, `tests/` and `scripts/` with typescript-eslint, react-hooks and jsx-a11y (`:11-45`). There is no stylelint and no raw-literal rule (deferred: `WD-V1-DS-04`). CI holds only `repo-hygiene.yml`, and `WD-V1-CI-01` is `todo`.

**F-A9D-19 — CSS variable names diverge from the Kit's emitted names.**
The Kit example's gallery uses `--token-color-primary-600`-style names (`Design_Template_Kit/examples/plantlibrary-field-ledger/design/gallery/index.html`, 134 occurrences of `token-color`). The Dashboard uses `--primary-600`, `--semantic-success-main` and so on in 551 references (110 distinct names) across `components.css` (285), `pages.css` (255), `base.css` (10) and `LocationTree.tsx` (1). Whatever `emit-stack` produces for web-css (A4's analysis), the call sites need a mechanical rename or a generated alias layer.

**F-A9D-20 — A likely conduct-rule deviation in toasts.**
The canon allows a "4 px toast level stripe" (`TOKEN_USAGE_NOTES.md:90-91`). The Dashboard renders toasts as full semantic fills (`components.css:455,459-464`: `neutral-900` / `semantic-success-main` / `semantic-error-main`) with no stripe. The selected-row 3 px stripe does conform (`pages.css:166,171`). The toast case needs a visual check before it is called a defect.

## §3 Candidates

| ID | Source path @ pin | What | Verdict | Target repo and path | Lane (B5, B6) | Q id or — |
|---|---|---|---|---|---|---|
| RC-A9D-01 | `PlantLibrary_Dashboard/scripts/generate-theme.mjs` @ 7795fc8 | Working flat-JSON → CSS custom props + typed TS generator (naming rule, unit heuristic, dark block) | keep as the bridge until the Kit's web-css emission is anchored; then retire, or reduce it to an alias emitter | PlantLibrary_Dashboard `scripts/` | B5 | Q-A9D-04 |
| RC-A9D-02 | `PlantLibrary_Dashboard/scripts/check-token-drift.mjs` @ 7795fc8 | Static value-diff checker plus banned-literal grep, report-only | adapt: scope the ban to BAN-02, exclude or allowlist the generated files, and read `semantic-roles.json` as DS-07 claims; or replace it with the Kit's static checks | PlantLibrary_Dashboard `scripts/` | B5 | Q-A9D-02 |
| RC-A9D-03 | `PlantLibrary_Dashboard/src/app/routes.ts` @ 7795fc8 | Route → page-contract table (the single source of the view inventory and nav entries) | reuse as the 01a adapter's view and navigation extractor | (read in place) | B6 | — |
| RC-A9D-04 | `PlantLibrary_Dashboard/e2e/validation-smoke.spec.ts` + `playwright.config.ts` @ 7795fc8 | 16-shot page walk over every route (login → settings) | adapt in Phase C as the screenshot-capture harness: retarget the evidence dir, add a light/dark pair per route; capture only (deferred) | PlantLibrary_Dashboard `e2e/` | B6 | Q-A9D-05 |
| RC-A9D-05 | `PlantLibrary_Dashboard/src/mocks/` (handlers.ts, browser-fixtures.ts, `VITE_USE_MOCKS`) @ 7795fc8 | Dev-only MSW fixture mode for 9 GET endpoints | consider only for design-only captures, labelled as fixture-backed; never as validation (the "never fake the layer under test" rule) | (in place) | B6 | Q-A9D-05 |
| RC-A9D-06 | `PlantLibrary_Dashboard/references/PlantLibrary_pythonApp_old/{mockup_briefs,screen_requirements}` @ 7795fc8 | 13 mockup briefs + 24 screen-structure specs, including surfaces with no Dashboard view (conflict_resolution, provider_setup, location_editor, edit_instance, edit_profile, image_lightbox, provenance_details, backup_restore, reenrichment_provider_selection, image_attribution) | adopt as the specification input for 01a step 7 and 06a "mandated surfaces"; the HTML mockups are legacy-colour reference only | (read in place) | B6 | Q-A9D-01 |
| RC-A9D-07 | `PlantLibrary_Dashboard/docs/WD-UX-10_mockup_parity_report.md` @ 7795fc8 | Prior per-brief parity verdicts (2026-07-07) | treat as current-state claims to re-verify, not as evidence | (in place) | B6 | — |
| RC-A9D-08 | `PlantLibrary_Dashboard/src/components/` (14 components + `components.css`, `pl-` BEM prefix, 153 class uses) @ 7795fc8 | Component inventory: Button/IconButton, Card, Chip, ConfidenceBadge, DataState, FormField, LocationTree, NoticePanel, PageHeader, ReadinessBadge, StatusBadge, TabBar, Table, Toast | the component census baseline for B6; map to the Kit's component contracts | (in place) | B6 | — |
| RC-A9D-09 | `Design_Template_Kit/examples/plantlibrary-field-ledger/design/banned-colors.json` @ f08e588 | BAN-01..03, with BAN-02 scoped away from the chart palette | adopt into the PlantLibrary Configuration; amend `TOKEN_USAGE_NOTES.md:27-29` and the design-adoption skill | PlantLibrary_SharedContracts (Configuration home per Q-G-01) | B5 | Q-A9D-02 |
| RC-A9D-10 | `Design_Template_Kit/examples/plantlibrary-field-ledger/design/gallery/baselines/` @ f08e588 | 47 canon-derived component/page baselines (light + dark) | candidate visual reference beside the approved claude.ai artifact; A4 confirms what they depict | per Q-G-01 | B6 | — |
| RC-A9D-11 | `PlantLibrary_Dashboard/src/theme/theme-mode.ts` + `ThemeRoot.tsx` @ 7795fc8 | `data-theme` attribute switch, prefers-color-scheme default, localStorage persistence | keep; B5 checks that the Kit's web-css dark selector uses the same attribute | (in place) | B5 | — |
| RC-A9D-12 | `PlantLibrary_Dashboard/implementation/System_V1_Implementation/validation/WD1-B07_token_drift.md` @ 7795fc8 | Drift baseline with a reading template | supersede: the figures are stale (F-A9D-01); keep the shape for the migration's drift dry-run | (in place) | B5 | Q-A9D-03 |

## §4 Questions for the operator

| ID | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A9D-01 | Is the Dashboard brief a **restructure** (01a/06a–06d run) or a **re-skin** (01 → 02)? | (a) restructure; (b) re-skin only (tokens/roles/dark), structure untouched | 29 of 42 operations are unreached; ten specified screen structures have no view (RC-A9D-06); settings and plant-instance routes disagree with their contracts (F-A9D-12). A re-skin would carry these forward unexamined | B6 census and IA steps for the Dashboard |
| Q-A9D-02 | Scope of the `#16A34A` ban | (a) adopt the Kit's scoped BAN-02 (chart palette allowed; accent/fill banned) and amend `TOKEN_USAGE_NOTES.md`, the design-adoption skill, DS-06 done-when and the drift checker; (b) change `CHART.series_1` to a non-banned green (re-run the P-DS-07 palette validation, major decision); (c) keep "anywhere" and accept a permanently red checker | P-DS-07 is the decision record, and the skill itself says "the decision record wins" (`design-adoption/SKILL.md:37-39`); the Kit already encodes it | B5 anchoring of Configuration checks; DS-07 checker change |
| Q-A9D-03 | Disposition of `WD-V1-DS-06` (regen already landed), `WD-V1-DS-01` and `WD-V1-DS-07` | (a) record in the package `STATE.md` that DS-06's regeneration landed in `321307b`; supersede DS-06 items 1–4 and DS-01 by the design-migration package's gap rows, with the validation cells pointed at the deferred register; (b) keep DS-06 as an independent Phase C batch run before the migration | Avoids two parallel adoptions of the same CSS (the skill's own warning, `SKILL.md:50-53`); the remaining DS-06 items (roles, SEMANTIC_DARK, chart series, pill) are exactly what the migration's gap map will list | B6 gap map ownership; B4/B7 package edits |
| Q-A9D-04 | CSS variable names when the Kit's web-css artifact replaces `tokens.generated.css` | (a) a generated alias layer (old name → Kit name) for one wave, then a mechanical rename of the 551 call sites, then remove the aliases; (b) one-shot rename with no aliases; (c) configure emission to keep today's names | (a) keeps `tsc -b`/lint-checkable steps small and reversible with no visual change per step; (c) would fork the Kit's convention | B5 anchoring; B6 migration batch shape |
| Q-A9D-05 | Screenshot source for the Phase C capture (current state + after) | (a) live local stack with the seeded validation dataset via the existing e2e harness (verify-stack first), light and dark per route; (b) MSW fixture mode for design-only shots, labelled as such; (c) both: (b) for the design gallery, (a) for acceptance | The superproject `CLAUDE.md` testing rule forbids faking first-party layers in validation; (a) re-uses the proven harness | Deferred-register rows DVC-A9D-01..09; SDA-DEC-03 |
| Q-A9D-06 | Settings and plant-detail route drift against the page contracts | (a) leave the code as is now; the 06b IA decides and the contracts are amended after IA approval (P-DS-10 keeps contracts until then); (b) change the code to the contract routes now; (c) amend the contracts to the code now | Changing either side before the IA risks doing it twice | B6 IA step; SharedContracts contract amendments |

## §5 Reusable things this brief did not name

- `src/mocks/browser-fixtures.ts` + `VITE_DEV_BYPASS_AUTH` (`src/auth/session.ts:41`): offline dev mode. Useful for design-only captures (Q-A9D-05 (b)).
- `references/PlantLibrary_pythonApp_old/screen_requirements/Screen_Structure_conflict_resolution.md` pairs with the unreached sync-conflict operations (`/sync/conflicts`, `/sync/conflicts/{id}/resolve`), making it a ready tier-2 `capability-missing` plus mandated-surface pair for 06a.
- `docs/WD-MOCKUP-UPGRADE_PROPOSAL.md`: the 2026-07-07 gap analysis (shell depth, component vocabulary, task-first hierarchy, workflow surfaces, layout resilience at 1280×800 and 1024 px). This is ready-made input for the IA findings.
- `src/app/routes.ts:105,110`: `plantDetailTabs` (six tabs, ordered by the contract) and `settingsSections`. The census can list them as sub-views.
- `.github/workflows/repo-hygiene.yml`: the only CI job, a template for the deferred `WD-V1-CI-01`.
- `tsconfig.generated.json`: typechecks the SharedContracts generated client as a composite project. Keep it in mind if the Configuration moves (Q-G-01).
- `RUN_DASHBOARD` (one-line operator note) and `.env.local` (git-ignored; not read).

## §6 Claims to verify

1. **Generated CSS equals canon 1.2.0 (hex).** From `C:\Programmierung\SW_Development` in Git Bash: `diff <(grep -o '#[0-9A-Fa-f]\{6\}' PlantLibrary_SharedContracts/design-tokens/tokens.json | tr a-f A-F | sort) <(grep -o '#[0-9A-Fa-f]\{6\}' PlantLibrary_Dashboard/src/theme/tokens.generated.css | tr a-f A-F | sort) && echo EQUAL`. Expected: `EQUAL` (134 values each). Also `grep -c '^  --' PlantLibrary_Dashboard/src/theme/tokens.generated.css` gives `231`.
2. **No dark-state or dark-chart token is used.** `grep -rc 'semantic-dark-\|chart-dark-' PlantLibrary_Dashboard/src/components/components.css PlantLibrary_Dashboard/src/pages/pages.css PlantLibrary_Dashboard/src/theme/base.css`. Expected: `0` for all three files.
3. **The drift checker cannot exit 0 under the current canon.** `grep -rniE '#16A34A' PlantLibrary_Dashboard/src` gives exactly 4 hits (`tokens.generated.css:100,104`, `tokens.generated.ts:91,95`), and `grep -n 'BANNED_LITERALS\|GREP_ROOT' PlantLibrary_Dashboard/scripts/check-token-drift.mjs` shows the ban list includes `#16A34A` and that the grep root is all of `src/`.

## §7 Brief sections

### §7.1 UI source inventory

**Stack (resolved from `package-lock.json`; ranges are in `package.json:22-50`).** React 18.3.1, react-dom 18.3.1, react-router-dom 6.30.4 (`createBrowserRouter`), @tanstack/react-query 5.101.2, react-hook-form 7.81.0, zod 3.25.76. Vite 5.4.21 with @vitejs/plugin-react 4.7.0, TypeScript 5.9.3, ESLint 9.39.4, Prettier 3.9.4, MSW 2.14.6. Test tooling: vitest 2.1.9 (jsdom 25), @testing-library/*, @playwright/test 1.61.1. Node ≥ 20 (`package.json:6-7`). **No Tailwind, no PostCSS config, no Sass, no CSS modules (0 `*.module.css`), no styled-components or emotion, no UI component library.** Plain global CSS with a `pl-` BEM prefix (153 `className="pl-…"` uses; 7 `shell-`, 1 `login-`, 1 `route-`).

**Entry points.** `index.html:10` → `src/main.tsx`, which imports, in order, `@/theme/tokens.generated.css`, `@/theme/base.css`, `@/components/components.css` and `@/pages/pages.css` (`src/main.tsx:8-11`). It wraps the app in `QueryClientProvider` → `ThemeRoot` → `ToastProvider` → `RouterProvider` (`:22-33`), and starts the dev-only MSW worker under `VITE_USE_MOCKS` (`:41-44`). The `@` alias maps to `src/` (`vite.config.ts:10`). The dev proxy sends `/auth` and `/api` to `http://localhost:8000` (`vite.config.ts:26-29`).

**Folder tree with counts** (all files; lines from `wc -l`):

| Folder | Files | Lines | Contents |
|---|---|---|---|
| `src/` (root) | 3 | 80 | `main.tsx` 46, `vite-env.d.ts` 21, `README.md` 13 |
| `src/api/` | 3 | 103 | `client.ts` (generated-client instances), `garden.ts` (current-garden + garden-scoped query hooks), README |
| `src/app/` | 3 | 342 | `router.tsx` 53, `routes.ts` 112, `Shell.tsx` 177 |
| `src/auth/` | 2 | 95 | `ProtectedRoute.tsx`, `session.ts` |
| `src/components/` | 16 | 1,566 | 14 components (TSX) + `index.ts` + `components.css` 765 |
| `src/pages/` (root) | 2 | 844 | `PageStub.tsx` 22 (unused by the router), `pages.css` 822 |
| `src/pages/<11 folders>` | 23 | 2,622 | admin-review 2/161, calendar 3/377, dashboard 2/259, locations 2/115, login 1/29, plant-detail 2/339, plants 3/456, search 2/134, settings 2/268, sources 2/172, statistics 2/312 (each `*Page.tsx` + `*-queries.ts`) |
| `src/theme/` | 6 | 511 | `tokens.generated.css` 240 + `tokens.generated.ts` 172 (**generated**), `base.css` 42, `theme-mode.ts` 38, `index.ts` 11, `ThemeRoot.tsx` 8 |
| `src/types/` | 9 | 368 | DTO view types per page |
| `src/utils/` | 1 | 20 | `format.ts` |
| `src/mocks/` | 3 | 194 | MSW `handlers.ts`, `browser.ts`, `browser-fixtures.ts` (dev only) |
| **`src/` total** | **71** | **6,745** | 1,869 lines CSS (of which 240 generated) |
| `public/` | 1 | 349 | `mockServiceWorker.js` (**vendor**, MSW 2.14.6) |
| `scripts/` | 3 + `hygiene/` | 296 (.mjs) | `generate-theme.mjs` 140, `check-token-drift.mjs` 156, `run_next_batch.py`; `hygiene/repo_hygiene_check.py` |
| `references/PlantLibrary_pythonApp_old/` | — | — | `mockups/` (13 HTML), `mockup_briefs/` (13), `screen_requirements/` (24), `resources/` (icons, styles, translations): legacy desktop reference |
| `docs/` | 6 | 326 | WD-AUTH-01, WD-BOOT-02, WD-DESIGN-01, WD-MOCKUP-UPGRADE, WD-UX-10, README |

**Assets.** No `src/assets/`; no images or icon files in `src/`. The brand mark is the text "PL" (`src/app/Shell.tsx:67`). The icon policy is open (SDA-DEC-04, `System_Design_Architecture/STATE.md:24`).

**Routing table** (`src/app/router.tsx:23-53`; route→contract map `src/app/routes.ts:23-96`):

| Route | Element | Guard | Contract (`routes.ts`) |
|---|---|---|---|
| `/` | `<Navigate to="/dashboard">` | — | — |
| `/login` | `pages/login/LoginPage.tsx` | public | `PageContract_shell.md` |
| `/dashboard` | `pages/dashboard/DashboardPage.tsx` | `ProtectedRoute` → `Shell` | `PageContract_dashboard.md` |
| `/plants` | `pages/plants/PlantsPage.tsx` | protected | `PageContract_plants.md` |
| `/plants/new` | `pages/plants/AddPlantWizardPage.tsx` | protected | `PageContract_plants.md` |
| `/plants/:profileId` | `pages/plant-detail/PlantDetailPage.tsx` | protected | `PageContract_plant_detail.md` |
| `/search` | `pages/search/SearchPage.tsx` | protected | `PageContract_search.md` |
| `/calendar` | `pages/calendar/CalendarPage.tsx` | protected | `PageContract_calendar.md` |
| `/statistics` | `pages/statistics/StatisticsPage.tsx` | protected | `PageContract_statistics.md` |
| `/locations` | `pages/locations/LocationsPage.tsx` | protected | `PageContract_locations.md` |
| `/admin-review` | `pages/admin-review/AdminReviewPage.tsx` | protected | `PageContract_admin_review.md` |
| `/sources` | `pages/sources/SourcesPage.tsx` | protected | `PageContract_sources.md` |
| `/settings`, `/settings/:section` | `pages/settings/SettingsPage.tsx` | protected | `PageContract_settings.md` |

**Test and e2e folders (listing only; nothing run).** `tests/` holds 20 files, 725 lines: `setup.ts`, `test-utils.tsx`, `README.md`; `app/` (Shell, routes); `auth/` (ProtectedRoute); `components/` (components); `mocks/server.ts`; `pages/` (11 page files, one per page); `theme/tokens.test.ts`. `e2e/validation-smoke.spec.ts` (140 lines) is a live-stack evidence harness (§F-A9D-17). Git-ignored output folders: `test-results/`, `e2e-report/`.

### §7.2 Token consumption

- **Path.** `scripts/generate-theme.mjs` reads `../PlantLibrary_SharedContracts/design-tokens/tokens.json` (`:29-32`) and writes `src/theme/tokens.generated.ts` (typed `as const` tree) and `src/theme/tokens.generated.css` (`:root` block for every group except `DARK`, plus a `[data-theme="dark"]` block for `DARK`) (`:100-135`). It then runs Prettier on both (`package.json:15`). The naming rule is kebab CSS / camel TS, with the `TYPE_SCALE` → `--type-*` exception (`:111`). The unit heuristic is `px` for every number except keys named `weight` (`:63-66`). Hooks: `predev` and `prebuild` (`package.json:10,12`).
- **What is copied.** Nothing is copied by hand. Two generated files are committed (they are not git-ignored). `semantic-roles.json`, `TOKEN_USAGE_NOTES.md` and the page contracts are not consumed by any tooling.
- **Version pinned.** None (F-A9D-02). Effective content = SharedContracts `tokens.json` @ `1650271` (2026-07-10) = 1.2.0.
- **Copy against canon (static diff).** Equal (F-A9D-01; §6 claim 1). The generated TS has 134 hex values as well.
- **Files that reference tokens:**

| File | `var(--…)` refs | Token imports |
|---|---|---|
| `src/components/components.css` | 285 | — |
| `src/pages/pages.css` | 255 | — |
| `src/theme/base.css` | 10 | — |
| `src/components/LocationTree.tsx` | 1 (inline `calc(var(--space-4) * depth)`) | — |
| `src/main.tsx` | — | `import "@/theme/tokens.generated.css"` (`:8`) |
| `tests/theme/tokens.test.ts` | — | `import { tokens } from "@/theme/tokens.generated"` (`:4`) |
| **Total** | **551 refs, 110 distinct of 231 defined; 0 undefined names; no locally defined custom properties outside the generated file** | TS module: no product consumer (F-A9D-10) |

- **Unused token families** (121 names): all 28 `semantic-dark-*`, all 8 `chart-dark-*`, `chart-series-1..4`, 8 of 18 `dark-*`, 6 of 10 `highlight-*`, `radius-nav/none/xl`, 4 shell sizes, 4 button icon sizes, and some type-scale steps.

### §7.3 Literals that remain

**Excluded as generated or vendor:** `src/theme/tokens.generated.css`, `src/theme/tokens.generated.ts`, `public/mockServiceWorker.js`, `node_modules/`, `dist/`, `test-results/`, `*.tsbuildinfo`. `references/` (the legacy reference app) is excluded from the client census and scanned separately (F-A9D-16).

| Measure | Total | Per file | Top examples |
|---|---|---|---|
| Hex `#[0-9a-fA-F]{3,8}` | **0** | — | — |
| `rgb()/rgba()/hsl()` | **1** | `components.css` 1 | `:678 background-color: rgb(17 26 20 / 0.28)` (= neutral-900 @ 28 %) |
| Tailwind colour classes | **0** | — | no Tailwind in the stack |
| px/rem/em in CSS | **86** occurrences (85 lines) | `pages.css` 52, `components.css` 34 | border/outline widths 45 lines (`components.css:16 border: 1px solid transparent`, `:73 outline: 2px solid var(--highlight-focus-ring)`); layout 29 (`pages.css:5 minmax(260px, 1fr)`, `pages.css:220 minmax(280px, 420px)`, `components.css:681 min(40rem, …)`); breakpoints 3 (`@media (max-width: 1100px)` at `components.css:757`, `pages.css:355,815`); sr-only 3 (`pages.css:284-287`); `vertical-align: -1px` (`pages.css:406`); icon box 1.25rem ×4 (`pages.css:470-485`) |
| px in inline style props | **0** | 4 inline styles, all `%` or `var()` | `StatisticsPage.tsx:163 width: ${pct}%` |
| font-family names | **0** literal | 3 `var()` uses | `base.css:19`, `:33`; `components.css:14` |
| border-radius literals | **0** numeric | 1 `inherit` | `components.css:338`; 46 `var(--radius-*)` + 4 `var(--button-sizes-*-radius)`; 2 deprecated `--radius-pill-input` (`components.css:655`, `pages.css:133`) |
| shadow literals | **0** | — | none (consistent with "flat by default") |
| z-index literals | **3** | `components.css` 2, `pages.css` 1 | `components.css:447 z-index: 1000`, `:673 z-index: 900`, `pages.css:612 z-index: -1` |
| other unitless literals | 2 opacity | | `components.css:66 opacity: 0.62`, `pages.css:614 opacity: 0.35` |
| font-weight / font-size literals | **0** | | all via `--type-*` |

The worst offender is `pages.css` (52 of 86 dimension literals). Of the 86, 74 are border widths or layout-only, which the web divergence rule permits (`platform-mapping-web.md:20`). The residue that a strict Configuration check would flag is the scrim `rgb()`, the 1100 px breakpoint, the z-index and opacity literals and the 1.25rem icon box. The canon has no token for any of them (F-A9D-04).

### §7.4 Screens

Legend: **Tokens** means the screen's CSS uses only `var()` values (all screens do). **Roles/dark** is the static state of the 1.2.0 role and dark adoption. **Mockup (1.2.0)** means the approved claude.ai artifact (`04_*:5`), whose screen-to-client mapping was not opened. **Legacy mockup** is under `references/PlantLibrary_pythonApp_old/mockups/`.

| Screen | Route | Component file | Page contract | Mockups | Package rows touching it | Old vs new design (static) |
|---|---|---|---|---|---|---|
| Shell (chrome) | all protected | `src/app/Shell.tsx` | `PageContract_shell.md` | legacy `mockup_shell.html`; 1.2.0 artifact: unknown | MVP WD-UX-01, WD-COMP-01; V1 `WD-V1-AUTH-01` (sign-out/401), DS-06, QA-01, DS-05 | tokens yes; dark overrides present for sidebar/toolbar/nav/command (`components.css:546-751`); compact tokens unused; app bg neutral-50 ≠ role |
| Login | `/login` | `src/pages/login/LoginPage.tsx` | none of its own (mapped to shell) | — | MVP WD-AUTH-01; V1 `WD-V1-WALK-01`, `WD-V1-TEST-02` | minimal page; `login-` class |
| Dashboard | `/dashboard` | `src/pages/dashboard/DashboardPage.tsx` | `PageContract_dashboard.md` | legacy `mockup_dashboard.html`, `mockup_first_run.html` | MVP WD-PAGE-01, WD-UX-03; V1 DS-06, QA-01, WALK-01 | stat/attention/recent rows have dark overrides (`pages.css:340-350`); stat icon well `primary-100` (overridden `:350`) |
| Plants | `/plants` | `src/pages/plants/PlantsPage.tsx` | `PageContract_plants.md` | legacy `mockup_plant_list.html` | MVP WD-PAGE-01, WD-UX-04; V1 `WD-V1-QUERY-01`, `WD-V1-QUERY-07`, DS-06, QA-01 | pill-input radius in the filter (`pages.css:133`); selected-row stripe conforms |
| Add plant | `/plants/new` | `src/pages/plants/AddPlantWizardPage.tsx` | `PageContract_plants.md` (route not named there) | legacy `mockup_wizard.html` | MVP WD-UX-06; V1 `WD-V1-QUERY-03` (wrong path, F-A9D-13) | wizard panel `neutral-0` with no dark override (`pages.css:726`); stepper complete uses `semantic-success-light` (`:719`), not dark |
| Plant detail | `/plants/:profileId` | `src/pages/plant-detail/PlantDetailPage.tsx` | `PageContract_plant_detail.md` (instance route missing) | legacy `mockup_plant_detail.html` | MVP WD-PAGE-02, WD-UX-04; V1 `WD-V1-QUERY-01` | hero aside and property group overridden (`pages.css:344-345`); six tabs (`routes.ts:105`) |
| Search | `/search` | `src/pages/search/SearchPage.tsx` | `PageContract_search.md` | legacy `mockup_search.html` | MVP WD-PAGE-03, WD-UX-05; V1 `WD-V1-QUERY-04` | readiness badges light-only fills (`components.css:484-496`) |
| Calendar | `/calendar` | `src/pages/calendar/CalendarPage.tsx` | `PageContract_calendar.md` | legacy `mockup_dataviz.html` (partial) | MVP WD-PAGE-03, WD-UX-09; V1 DS-06, QA-01, WALK-02 (task edit) | markers `semantic-info/warning-light` with no dark (`pages.css:474,480`) |
| Statistics | `/statistics` | `src/pages/statistics/StatisticsPage.tsx` | `PageContract_statistics.md` | legacy `mockup_dataviz.html` | MVP WD-PAGE-07, WD-UX-09; V1 `WD-V1-QUERY-06` (deferred), DS-06 | legacy chart aliases; no `CHART_DARK` (F-A9D-07) |
| Locations | `/locations` | `src/pages/locations/LocationsPage.tsx` | `PageContract_locations.md` | legacy: none dedicated | MVP WD-PAGE-04, WD-UX-09; V1 `WD-V1-QUERY-02` | `LocationTree` indentation by `var(--space-4)` |
| Admin review | `/admin-review` | `src/pages/admin-review/AdminReviewPage.tsx` | `PageContract_admin_review.md` | legacy `mockup_admin_sources.html` | MVP WD-PAGE-05, WD-UX-07; V1 DS-06, QA-01 | diff panel `neutral-100` with no dark (`pages.css:550`) |
| Sources | `/sources` | `src/pages/sources/SourcesPage.tsx` | `PageContract_sources.md` | legacy `mockup_admin_sources.html` | MVP WD-PAGE-05, WD-UX-07; V1 `WD-V1-QUERY-05` | status badges light-only fills |
| Settings | `/settings`, `/settings/:section` | `src/pages/settings/SettingsPage.tsx` | `PageContract_settings.md` (sub-routes differ) | legacy `mockup_settings.html` | MVP WD-PAGE-06, WD-UX-08; V1 `WD-V1-QUERY-05`, `WD-V1-AUTH-01` | theme toggle lives here (`SettingsPage.tsx:12`, `useThemeMode`) |

Cross-cutting rows touching every screen: `WD-V1-DS-06` (todo), `WD-V1-DS-05` (gated, needs live screenshots), `WD-V1-QA-01` (gated), `WD-V1-WALK-01/-02` (todo), `WD-V1-TEST-01/-02` (todo), `WD-V1-DS-02/-03` (todo; PRODUCT.md and DESIGN.md are absent at the suite root). **Old versus new:** every screen consumes the 1.2.0 primitive values (there is no 1.1.0 literal anywhere). No screen consumes the 1.2.0 role layer, `SEMANTIC_DARK` or `CHART_DARK`. "New design" therefore holds for light-theme colour values and does not hold for dark-theme roles or the chart palette. Nothing static separates a "legacy" screen from a "new" one; the gap is uniform.

### §7.5 The design-adoption gate against this client

The skill (`.claude/skills/design-adoption/SKILL.md`) checks, before UI work: read `tokens.json`, `TOKEN_USAGE_NOTES.md`, `semantic-roles.json` and `platform-mapping-web.md` (`:29-35`); map the change to P-DS-02..10 (`:46-49`); check overlap with the adoption row (`:57-61`); and apply the hard rules (`:69-83`).

| Assumption | Holds here? | Evidence |
|---|---|---|
| Canon paths exist (tokens.json, semantic-roles.json, TOKEN_USAGE_NOTES.md, platform-mapping-web.md, 04_*) | holds | all present |
| "tokens 1.2.0" identifies the canon | partly | `tokens.json` has no version field; 1.2.0 is in `semantic-roles.json:5` and `CONTRACT_VERSION.md`; the Dashboard pins nothing (F-A9D-02) |
| `platform-mapping-web.md` tells how the web consumes tokens | does not hold | stale example value and wrong producer path (F-A9D-11); the real path is the suite's own generator |
| Adoption row `WD-V1-DS-06` covers "regen; role bindings; SEMANTIC_DARK; pill → full" | partly | the regen already landed (`321307b`); the other three items are open (F-A9D-05/06/08); the row omits chart series, which `TASK_CONTEXT` includes |
| "After changing token mirrors, regenerate (`generate:theme`)" | holds as a fact | the hook exists, but running it is node execution: Phase B may not run it under Q-G-04 (a) unless it is classed as a static emit |
| Banned greens "never anywhere" | does not hold | the canon keeps `#16A34A` as chart series_1 under P-DS-07 (F-A9D-09); the skill's own precedence rule (`:37-39`) resolves this in favour of the decision record |
| "Dark surfaces need dark tokens" can be followed | holds (the tokens exist) | all 28 `--semantic-dark-*` are emitted; none are used yet |
| Fires for "generated theme CSS/vars" edits | holds | `src/theme/tokens.generated.*` |
| The client has `DESIGN.md` / design context | does not hold | DS-02 todo; `CLAUDE.md:32-35` gives the fallback |
| Kit design-gate prerequisites (`design/conformance/CONSUMED_DESIGN.md`, Configuration pin) | does not hold | absent; this is what B5 anchors (Q-G-01, Q-G-07) |

For Q-G-07 (a): once B5 anchors the Dashboard, the design-gate's pin and static checks replace every row above. The two "does not hold" items about the canon (F-A9D-09, F-A9D-11) should be fixed in the Configuration, not in a successor skill.

### §7.6 Design-migration census shape (as far as a static scan can fill it)

#### 7.6.1 Mechanical design census (prompt 01, "Mechanical design census")

| Measurement | Value for PlantLibrary_Dashboard @ 7795fc8 |
|---|---|
| Colour literals | 1 (1 rgb, 0 hex, 0 named) in 1 file (`components.css`), excluding the 2 generated files |
| Dimension literals | 86 px/rem in 2 files: `pages.css` 52 (60 %), `components.css` 34. Of these, 45 border/outline widths, 29 layout, 3 breakpoint, 8 misc |
| Radii | 0 numeric; 9 distinct `var(--radius-*|--button-sizes-*-radius)` names used; 1 deprecated (`pill-input`, 2 uses) |
| Font families and sizes | 2 stacks, both tokens; 0 literal sizes/weights |
| Detector summary | **not run** (the Kit's design detector is a Phase C or Q-G-04 (a) item; A4 names the command) |
| Drift dry-run | static equivalent done: generated CSS = canon 1.2.0 values (F-A9D-01); role layer not emitted |

#### 7.6.2 Function / UI census (`FUNCTION_UI_CENSUS_TEMPLATE.md`), static draft

| Field | Value |
|---|---|
| Census date | 2026-10-13 (static draft by lane A9; B6 re-issues it) |
| Repository | `PlantLibrary_Dashboard` @ `7795fc8`; operations from `PlantLibrary_Server` @ `f1a31b9` |
| Configuration | `none` (no `design/CONSUMED_DESIGN.md`); de facto SharedContracts `design-tokens` 1.2.0 by path |
| Stack adapter | see §0.2 below |
| Status | `DRAFT` |

**§0.2 Stack adapter**

| Question | This stack's answer |
|---|---|
| Operations: where declared, how extracted | `PlantLibrary_Server/app/api/routes/*.py`, `@router.(get|post|put|patch|delete)("…")` decorators plus each router's prefix. Cross-checked against `PlantLibrary_SharedContracts/openapi/plantlibrary.openapi.yaml` `operationId` (40 = 40 under `/api/v1`) |
| UI calls: where, how extracted | (1) `src/**/*.ts(x)` occurrences of `(meApi|gardensApi|plantsApi|locationsApi|tasksApi|syncApi|dashboardSupportApi)\.<method>`; (2) literal `/auth/…` strings (`LoginPage.tsx:17`). The client instances are in `src/api/client.ts` |
| Matcher | Generated method name ↔ operationId (camelCase of the snake operationId; 1:1 by generation). This is exact, so no segment matching is needed for generated calls. Literal `/auth/*` strings match segment-wise against the auth router |
| One view; enumeration | one route element in `src/app/router.tsx` (cross-checked by `routeMap` in `src/app/routes.ts`); sub-views = `plantDetailTabs`, `settingsSections` (`routes.ts:105,110`) |
| Navigation entry | a `NavLink` generated from `routeMap` in `Shell.tsx:13-15,72-78` (protected, no `:param`, not `/plants/new`; Settings pinned separately) |
| One subsystem | one Server route module (`app/api/routes/<module>.py`); below that, a service package (not read) |

**§1 Route inventory**

| Family | Operations | Reached by the UI |
|---|---|---|
| health/metrics (infra) | 3 | 0 |
| auth | 2 | 2 (login direct; callback by redirect) |
| me | 1 | 1 |
| gardens | 3 | 1 (list) |
| client-devices (infra for sync clients) | 2 | 0 |
| locations | 5 | 1 (list) |
| plants (instances 5 + events 2 + notes 3) | 10 | 1 (list) |
| tasks | 5 | 2 (list, update) |
| media | 3 | 0 |
| sync | 5 | 2 (pull, status) |
| dashboard_support (statistics 1, admin-review 2) | 3 | 3 |
| **Totals** | **42** | **13 reached · 29 unreached** (5 infrastructural) |

**§2 Tier-1 `capability-missing` candidates** (numbered for B6 to confirm by hand; they are not final IDs): create garden, get garden; create/get/update/delete location; create/get/update/delete plant instance; list/create plant events; list/create/update plant notes; create/get/delete task; media upload-intent/complete/download-url; sync push, list conflicts, resolve conflict. That is 24 non-infrastructural operations, plus 5 infrastructural ones to mark as such. Note that several are knowingly UI-disabled pending `SD-GAP-007` (`AdminReviewPage.tsx:31`, `SourcesPage.tsx:69`).

**§3 Tier-2 subsystem candidates (medium confidence):** media (no surface; `Screen_Structure_image_lightbox.md`, `_image_attribution.md` exist), sync conflicts (none; `Screen_Structure_conflict_resolution.md`), plant journal/events and notes (none), location editing (readable only, `partial`; `Screen_Structure_location_editor.md`), garden management / multi-garden (none; `src/api/garden.ts:5-11` takes the first membership), provider setup / re-enrichment (no server operation at all; the specification names `Screen_Structure_provider_setup.md`, `_reenrichment_provider_selection.md`).

**§4 View inventory:** 12 views (13 routes; `/` is a redirect). 9 are reached from navigation (`Shell.tsx:13-15`: dashboard, plants, search, calendar, statistics, locations, admin-review, sources, settings). The other 3 are link-reached: `/plants/new` (action), `/plants/:profileId` (detail, normally link-reached), and `/login` (public).

**§5 Other operator surfaces:** none in the Dashboard. The Server's CLI and jobs were not read. `PageStub.tsx` is an unused placeholder.

**§6 Families (provisional):** tier 1: 24 candidates (+5 infrastructural); tier 2: 6 candidates; structure: 2 (settings sub-route mismatch, missing plant-instance route; F-A9D-12).

**§7 Findings for the IA:** (1) Everything present is read-mostly. Of the 13 reached operations only one writes (`updateTask`), so the UI watches the garden but can barely act on it. (2) The specification (24 screen structures) names ten surfaces with no view (RC-A9D-06), and several of them pair with unreached operations: conflicts, media, location editing. (3) Single-garden assumption: there is no garden switcher, although the API is garden-scoped. (4) Settings IA (five sections in code) has diverged from the contract (three sub-routes).

**06a and 06b inputs this lane can supply.** The forward-surface filter is `PlantLibrary_Dashboard/implementation/System_V1_Implementation/TASK_CHECKLIST.md`, `status ≠ done`. Rows matched by `area`/files touching `src/`: QUERY-01..05, QUERY-07, AUTH-01, DS-06, DS-02, DS-03, QA-01, TEST-01, TEST-02 (13 rows), plus deferred QUERY-06, DS-04 and blocked DS-01. Batch goals: not read. Page-contract index for 06b: the 11 files under `page-contracts/desktop-web/`.

#### 7.6.3 Not determinable statically → deferred-validation register (proposed rows)

| Name | What would be run | Skill | After |
|---|---|---|---|
| DVC-A9D-01 dark-theme rendering per route | light + dark screenshot of all 12 views; check for light fills on dark surfaces (38 fills, 20 overrides) | webapp-testing (via the `e2e/` harness) | B6 migration batch |
| DVC-A9D-02 post-1.2.0 current-state baseline | screenshot pass of all routes at the current commit (the existing 16 PNGs predate 1.2.0) | webapp-testing + verify-stack | before B6 gap map is accepted |
| DVC-A9D-03 compact and viewport behaviour | 1280×800, 1200, 1100, 1024, 900 px sweep; shell compact claims (F-A9D-15) | webapp-testing | B6 |
| DVC-A9D-04 contrast on dark | focus ring and text-ramp contrast on dark surfaces where `--neutral-*` text is not overridden | webapp-testing (computed styles) | B6 |
| DVC-A9D-05 accent ≤ 10 % per screen (P-DS-08) | rendered-area measurement per screen | Kit design checks / impeccable audit (`WD-V1-DS-05`) | B6 |
| DVC-A9D-06 chart palette order and dark charts | Statistics and Calendar legends in light and dark | webapp-testing | B6 |
| DVC-A9D-07 toast conduct | toast appearance against the 4 px stripe rule (F-A9D-20) | webapp-testing | B6 |
| DVC-A9D-08 drift checker after canon amendment | `node scripts/check-token-drift.mjs` exits 0 once Q-A9D-02 lands | run-batch standing leg (static; allowed under Q-G-04 (a) if classed as a static check) | B5 |
| DVC-A9D-09 type/lint after the token-name migration | `tsc -b` and `npm run lint` after the alias or rename step | run-batch standing legs | B6 migration batch |

### §7.7 Stack facts for the anchoring (lane B5)

- **Build tooling:** Vite 5.4.21 + @vitejs/plugin-react; `build` = `tsc -b && vite build` (`package.json:13`); `generate:theme` runs before dev and build. Dev server on port 5173 with a proxy to `:8000`. There is no `webServer` in the Playwright config.
- **CSS pipeline:** plain global CSS imported from `src/main.tsx:8-11` in a fixed order (tokens → base → components → pages); Vite's default CSS handling. No PostCSS config, no Tailwind, no Sass, no CSS modules. Dark mode: the `[data-theme="dark"]` attribute on `<html>` (`src/theme/theme-mode.ts:16-17`).
- **Where a generated `tokens.css` or `tokens.ts` would be consumed:** replace or augment the import at `src/main.tsx:8` (today `@/theme/tokens.generated.css`), keeping it first in the import order. The TS module lands beside `src/theme/index.ts`, which re-exports `tokens` (`:9-10`). Generated files today live in `src/theme/` with the `GENERATED FILE` header, and `generate:theme` (`package.json:15`) is the hook to repoint at a Kit emit command. A role layer (semantic roles → `--role-*` vars under `:root` and `[data-theme="dark"]`) would remove most of the 20 hand-written dark overrides.
- **Lint, format and type-check commands that exist (names only):** `npm run lint` (`eslint .`, `package.json:19`); `npm run format` (`prettier --write .`, which **writes**; the non-writing form `prettier --check .` has no script); type check `tsc -b` (no `typecheck` script, `CLAUDE.md:18-19`); hygiene: `python scripts/hygiene/repo_hygiene_check.py check` (`.github/workflows/repo-hygiene.yml`); token drift: `node scripts/check-token-drift.mjs` (report-only, exits 1 today, F-A9D-09). There is no stylelint, no CSS lint and no raw-literal lint rule. The three test-runner scripts in `package.json:16-18` are not named here per program rule 1.
- **Does a type check run without a build?** Yes. `tsc -b` alone runs the TypeScript project build without `vite build`. The root project is `noEmit: true` (`tsconfig.json:12`). The referenced `tsconfig.generated.json` is composite and emits `.d.ts`/`.js` only into `node_modules/.generated-client-build/` (`tsconfig.generated.json:9`, already present). `*.tsbuildinfo` files are written at the repo root and are git-ignored (`.gitignore`). It produces nothing to run, so it fits Q-G-04 (a). It needs the installed `node_modules/` (present, 2026-07-13) and the sibling `PlantLibrary_SharedContracts/generated/typescript/`.
