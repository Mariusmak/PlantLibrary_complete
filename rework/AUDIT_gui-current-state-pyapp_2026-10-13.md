# GUI current state — PlantLibrary_PyApp — lane A9 (read-only analysis, 2026-10-13)

Lane A9-pyapp, Phase A, read-only. Subject: `PlantLibrary_PyApp` @ `35ddc63` (main). Canon: `PlantLibrary_SharedContracts` @ `d43f7a2` (`design-tokens/` 1.2.0 "field-ledger"). Methodology: `PlantLibrary_Workspace` @ `6b4b88b` (GUI_Improvement_Methodology 4.1.0). Kit read for the Qt emitter only: `Design_Template_Kit` @ `f08e588`. Static scan only — nothing launched, imported or run beyond three throwaway AST/text scanners in the session scratchpad (they parse files as text; no app module was imported). This file has no INDEX.md line yet: the orchestrator adds it in the commit that files this audit.

## §0 Summary

1. Tokens already reach QSS through a working seam: `resources/styles/light.qss`/`dark.qss` are `string.Template` files (0 hex literals, 637/632 `$var` uses), rendered by `app/gui/theme_utils.py:45-103` from the hand-written Python module `app/gui/design_tokens.py` (623 lines) and applied with `QApplication.setStyleSheet` (`app/main.py:144`, `app/gui/main_window.py:1556`). Nothing is generated; nothing pins a canon version.
2. `design_tokens.py` is a half-migrated hybrid: the light role layer (`LIGHT_THEME`) is 30/37 equal to canon `semantic-roles.json` LIGHT, but the primitives are still "Verdant" — PRIMARY 0/10 equal, NEUTRAL 6/14, HIGHLIGHT 1/9, DARK 9/18, `SEMANTIC_DARK`/`CHART_DARK` absent — and `DARK_THEME` is only 11/37 equal; 14 dark roles resolve to the banned `#4ADE80`/`#22C55E`.
3. Hex literals live only in `design_tokens.py` (164) inside `app/gui` (108 .py files, 32,808 lines); but 18 Python files read raw primitives (`PRIMARY[`/`NEUTRAL[`, 96 uses) that bypass the role layer and therefore render Verdant greens, and 154 `setStyleSheet(` calls, 126 literal `px`, 20 literal radii (two off-scale: 5 px, 16 px) and sub-scale font sizes (9/10/11 px) remain, concentrated in the add-plant wizard steps and `calendar_view.py`.
4. The Kit's `qt-qss` emitter exists (`anchoring-kit/emitters/emit-stack.mjs:31,321-352`; writes one `tokens.py` with `TOKENS`/`ROLES`/`VARS`) and its literal checker reads `.py` and `.qss` — so Qt is emittable in principle, but its `VARS` names (`color_primary_600`, `light_accent_main`) do not match the 174 `$var` names the QSS uses (`primary_600`, `accent_main`): an adapter or a QSS rename is required (Q-A9P-01).
5. Screens: 9 sidebar views + plant detail + shell (all 11 covered by SharedContracts `page-contracts/desktop-web/`), 1 add-plant wizard (6 steps), 14 named dialogs; the suite's own 31-file `GUI/screen_structures/` contract set covers the dialogs; the V3 HTML mockups it cites were deleted in `6921bc8` (2026-07-04) and exist only in git history.
6. Defects found statically: missing `resources/icons/check-white.svg` referenced by both QSS (checked checkbox), "Follow system setting" theme maps to light, `app/constants.py:70-74` keeps banned `#22c55e` in an (unused-by-GUI) confidence palette, `npx impeccable detect app/gui/` scans no file type this app has, and the onboarding harness refuses `resources/styles/*.qss` as an unmapped touched path.
7. Gate assumptions: design-adoption's paths and adoption row hold; its "never anywhere" ban on `#16A34A` contradicts canon `CHART.series_1` (the Kit already scoped it, BAN-02); `platform-mapping-python.md` is stale; impeccable 3.8.0 is web-oriented and its context file `.impeccable/design.json` still carries the Verdant ramp; gui-validation holds (window title "Plant Library").
8. Nine operator questions (Q-A9P-01..09), eleven candidates, ten deferred-validation items.

## §1 Coverage

| Item | Status | Reason |
|---|---|---|
| Kickoff prompt §1, §2, §4 | read | brief rule 6 |
| PyApp `pyproject.toml`, `main.py`, `app/main.py`, `app/config.py` (paths) | read | entry point, versions |
| `app/gui/design_tokens.py`, `styles.py`, `theme_utils.py`, `icons.py`, `domain_colors.py` (head), `motion.py` | read | token path |
| `app/gui/main_window.py` | partly read | view registry 410-516, theme 275-290 and 1547-1561, title 262; rest by grep |
| `app/gui/navigation.py` | partly read | nav items 139-165 |
| `app/gui/**` other 100 files | partly read | per-file static counts (all files) + targeted line reads; no file read whole |
| `resources/styles/light.qss`, `dark.qss` | partly read | head, diff light vs dark, var census, url() and px/radius greps over the whole files |
| `resources/icons/` | read | listing (32 SVG) |
| `app/gui/devtools/scenario_provider.py` | partly read | scenario ids and `SCREEN_VARIANTS` keys |
| `app/services/**` | partly read | AST public-method census only (pass A input) |
| `tests/` | read (listing) | listing only, nothing run; `tests/test_design_tokens.py` test names, `tests/acceptance/test_harness_port.py` pin list |
| `scripts/check_token_drift.py`, `scripts/harness/regression_scope.py` | partly read | structure, shipped-data rule, tables |
| `implementation/System_V1_Implementation/` TASK_CHECKLIST, BATCH_PLAN (B04/B06/B07), STATE (head, 196-228), `validation/PY1-B07_token_drift.md`, `validation/ONBOARDING_harness-port.md` §(e) | partly read | rows PY-V1-DS-*, -UX-*, -WALK-01, -REL-01 |
| TASK_CONTEXT.md anchors | not read | row cells were sufficient for this brief |
| `DESIGN.md`, `PRODUCT.md` | partly read / not read | DESIGN.md: frontmatter + grep for banned greens; PRODUCT.md not needed |
| `GUI/` (screen_structures index, README) | partly read | index table; individual contracts not read |
| `.impeccable/design.json`, `.claude/skills/impeccable/` | partly read | SKILL.md head, version, detector extension set |
| `CLAUDE.md` (PyApp) | partly read | Design System section by grep |
| Superproject `.claude/skills/design-adoption/SKILL.md` | read | whole file |
| Superproject `.claude/skills/gui-validation/SKILL.md` + PyApp pointer copy | partly read | headings, §16 lessons, pointer diff |
| SharedContracts `design-tokens/*` | read | tokens.json, semantic-roles.json keys, TOKEN_USAGE_NOTES.md, platform-mapping-python.md |
| SharedContracts `page-contracts/desktop-web/*` | partly read | one-line view mapping per contract |
| Workspace `System_Design_Architecture/proposal/04_*` | partly read | §1, §2 decisions, §3-§5 |
| Workspace SDA `STATE.md` | partly read | decision table SDA-DEC-01..05 |
| Methodology `FUNCTION_UI_CENSUS_TEMPLATE.md`, `PROMPTS/01a_*` | read | census shape |
| Methodology `PROMPTS/01_SOURCE_INVENTORY.md` | partly read | mechanical design census table |
| Methodology 06a/06b templates and prompts | partly read | headings only |
| Methodology `VERSION.md`, `MIGRATION_NOTES_FROM_V2_V3.md` | partly read | 4.1.0 entry; V3 origin |
| MVP evidence `System_Integration_MVP/validation/evidence/MVP-VALIDATION-20260708-01/pyapp_gui/` | read (listing) | 82 PNG names; images not opened |
| PyApp `validation/evidence/PY-V1-GAP-CLOSURE-*` | read (listing) | 22 PNG names |
| Kit `emit-stack.mjs` (qt-qss), `check-literals.mjs` (extensions), `examples/plantlibrary-field-ledger/design/` | partly read | Qt emitter, banned-colors BAN-02, var-name shape |
| Archive_PreMVP/GUI_Improvements_V3 | not read | historical; mockups located through git only |

## §2 Findings

**F-A9P-01 — The token path is "hand-written Python module → QSS template", already the shape a Qt emitter needs.** `app/gui/styles.py:17-25` reads `resources/styles/{light,dark}.qss` (`app/config.py:20-22`) and calls `render_qss_template` (`app/gui/theme_utils.py:95-97`, `string.Template(...).substitute`) over the flat map built in `theme_template_values` (`app/gui/theme_utils.py:45-92`) from `design_tokens.py`. Applied app-wide with `app.setStyleSheet(load_stylesheet(...))` at `app/main.py:144` and on theme change at `app/gui/main_window.py:1547-1556`. No `QPalette` theming at app level (palette calls only in 4 widget files). Both QSS files hold 0 hex and 0 `rgba(`; the 174 distinct light / 166 dark `$vars` resolve to role, primitive, type, space, radius and button keys.

**F-A9P-02 — `design_tokens.py` disagrees with canon 1.2.0 (static AST diff, scratch resolver, no import).** Group by group against `PlantLibrary_SharedContracts/design-tokens/tokens.json`: PRIMARY 0 equal / 10 differ (`PlantLibrary_PyApp/app/gui/design_tokens.py:10-21`, e.g. 600 `#16A34A` vs canon `#2A7A30`); NEUTRAL 6/8 (50, 100, 300, 500, 600, 800 differ; 150, 350 absent); SEMANTIC 28/0; SEMANTIC_DARK absent; DARK 9/9 (`:83-95`, primary `#4ADE80` vs `#74BC85`; seven 1.2.0 roles absent); EXTRA 5/0; HIGHLIGHT 1/8 (`:105-115`, focus_ring `#22C55E`); CHART 10 equal, `series_1..4` absent (`:117-128`); CHART_DARK absent; RADIUS 7/1 (`nav` absent; `pill_input` still present `:143`); SPACE, TYPE_SCALE, BUTTON_SIZES, SHELL_SIZES, FONT_FAMILY, MONO_FONT_FAMILY all equal. Role layer against `semantic-roles.json`: `LIGHT_THEME` (`:403`) 30 equal / 7 differ (disabled/readonly fills, `on_accent`, `icon_well_bg`, `states`, `chart` absent); `DARK_THEME` (`:484`) 11 equal / 26 differ. `DARK_THEME` keys resolving to banned greens: selection_border, selection_marker (`:323`), card_hover_border, calendar_today_ring, accent_main (`:501`), accent_active, accent_border, focus_ring (`:507`), scrollbar_handle_hover, button_primary_bg (`:533`), button_primary_active, button_outline_border, button_success_bg, button_success_active. The existing drift checker covers only four literal dicts and says so (`implementation/System_V1_Implementation/validation/PY1-B07_token_drift.md` "Reading" paragraph); the role-layer drift above is not in its report.

**F-A9P-03 — QSS consumes a few primitives that are still Verdant.** `$text_selection` (HIGHLIGHT, `#BBF7D0`) at `resources/styles/light.qss:11` and `dark.qss:11`; `$neutral_100` (`#F4F5F4` vs canon `#F5F7F2`) at `light.qss:507`; `$radius_pill_input` (deprecated, P-DS-06) at `light.qss:861`, `dark.qss:868`. Because `theme_template_values` writes HIGHLIGHT before the theme dict (`theme_utils.py:61-66`), keys present in both (e.g. `focus_ring`) take the theme value; keys only in HIGHLIGHT (`text_selection`, `search`, `drag_target`…) keep Verdant values.

**F-A9P-04 — Python-side literal and primitive debt (static counts over `app/gui`, 108 files).** Hex: 164, all in `design_tokens.py`. `QColor(`: 50 uses in 18 files, only 1 with a literal argument (`theme_utils.py:120`, transparent). `setStyleSheet(`: 154 in 27 files, 57 with an inline string literal. Literal `px` in strings: 126; `set{Fixed,Minimum,Maximum}{Size,Width,Height}(<number>)`: 71. Literal `border-radius: Npx`: 20 occurrences in 11 files, values 4/5/6/8/10/12/16 — 5 px (`app/gui/views/calendar_view.py:551`) and 16 px (`app/gui/dialogs/tag_dialog.py:135`) are not on the RADIUS scale. Literal `font-size: N px`: 34 in 9 files, of which 9 px ×3, 10 px ×10, 11 px ×12 are below the smallest TYPE_SCALE entry (caption 12) — e.g. `calendar_view.py:105`, `:241`, `app/gui/dialogs/provider_result_detail_dialog.py:58`, `app/gui/views/locations_view.py:160`. Raw primitive reads that bypass theme roles: `PRIMARY[` 37 and `NEUTRAL[` 59 uses; worst `app/gui/wizard/steps/step2_choose_match.py` (4 + 27), `step4_choose_images.py` (11 + 7), `step3_review_profile.py` (4 + 8), e.g. `step2_choose_match.py:637` (`PRIMARY[50]`/`PRIMARY[200]` banner with literal `border-radius: 10px`). Font families: only in `design_tokens.py:222-223`. Outside `app/gui`: `app/constants.py:70-74` (5 Tailwind hexes incl. banned `#22c55e`), `app/services/confidence_service.py:174`, `app/db/seed.py:18`; `confidence_display` is not called from `app/gui` (grep).

**F-A9P-05 — Light-only semantic primitives used on themed surfaces.** `app/gui/domain_colors.py:5-27` composes plant-category and stat-card colours from light `SEMANTIC`/`CHART` with no theme branch, and 18 files index `SEMANTIC[` directly (101 uses; `step2_choose_match.py` 20, `calendar_view.py` 8). P-DS-04 and conduct rule 7 (`TOKEN_USAGE_NOTES.md`, "Dark surfaces need dark tokens") require `SEMANTIC_DARK` on dark; whether these sites paint dark surfaces needs a render (DV-A9P-06).

**F-A9P-06 — Missing icon asset.** `resources/styles/light.qss:1094` and `dark.qss:1097` set `QCheckBox::indicator:checked { image: url(resources/icons/check-white.svg) }`; the file does not exist, is not tracked and has no git history (`git log --all -- resources/icons/check-white.svg` empty); `tests/test_design_tokens.py` (`test_ds23_…`, line 250-257) asserts only the string. All `url()` paths are relative, so they resolve against the process working directory (DV-A9P-03).

**F-A9P-07 — "Follow system setting" is light.** `app/gui/views/settings_view.py:1165` offers `system`; `resolve_theme_name` (`app/gui/design_tokens.py:574-578`) maps everything but `dark` to light; no `styleHints().colorScheme()` anywhere in `app/`.

**F-A9P-08 — Theme property is set after views are built.** `app/main.py:144` applies the stylesheet but never sets the `theme_name` property; `MainWindow` builds views in `_build_ui()` (`main_window.py:274`) and sets the property only in `_apply_theme` (`:286` → `:1555`). `current_theme_name()` (`theme_utils.py:37-42`) is called 34 times in 21 files; any of them that caches colours at construction gets light roles under a persisted dark theme. Needs a running app (DV-A9P-04).

**F-A9P-09 — Harness refuses the stylesheet paths.** `implementation/System_V1_Implementation/validation/ONBOARDING_harness-port.md:243-250`: `regression_scope.py resources/styles/light.qss` → `unmapped touched path`, exit 2, and one such path parks the whole scope. Cause: `_module_for_path` returns None for non-Python files under `app/`/`backend/` only (`scripts/harness/regression_scope.py:273`), the shipped-data route is repo-root only (`:566-587`, `"/" in changed` → None), and the acceptance test pins that behaviour (`tests/acceptance/test_harness_port.py:133`). `regression_scope.py` itself is adapted, not digest-pinned (`test_harness_port.py:35-39` pins three other files). Every B6 change to `light.qss`/`dark.qss` meets this at Phase C closeout.

**F-A9P-10 — Canon contradiction on `#16A34A`.** `TOKEN_USAGE_NOTES.md:27` and design-adoption `SKILL.md:71` ban `#16A34A` "anywhere"; canon `tokens.json:157` sets `CHART.series_1 = #16A34A`. The PyApp drift checker counts `design_tokens.py:118` (CHART) as a banned hit, so `PY-V1-DS-03`'s done-when "no pre-1.2.0 greens remain" cannot be met while matching canon. The Kit's round-trip already scopes the ban to accent/fill (`Design_Template_Kit/examples/plantlibrary-field-ledger/design/banned-colors.json:23-25`, BAN-02).

**F-A9P-11 — impeccable's detector cannot see this app.** `CLAUDE.md:93` documents `npx impeccable detect app/gui/`; the detector's scannable set is `.html .htm .css .scss .sass .less .jsx .tsx .js .ts .vue .svelte .astro` (`.claude/skills/impeccable/scripts/detector/node/file-system.mjs:13-17`) — no `.py`, no `.qss`. The four `/* impeccable-disable-line side-tab … */` comments in `light.qss` (e.g. `:248`, `:1487`) are therefore inert. impeccable's context file `.impeccable/design.json` lists the primary `tonalRamp` with `#16A34A`, `#4ADE80`, `#DCFCE7` (Verdant).

**F-A9P-12 — `platform-mapping-python.md` is stale.** `PlantLibrary_SharedContracts/design-tokens/platform-mapping-python.md:5` still says `tokens.json` is exported from `design_tokens.py`, and `:11` says the role layer is Python-only — superseded by `semantic-roles.json` 1.2.0 (P-DS-05). `:12` (QSS consumes the Python role dicts) is still true.

**F-A9P-13 — Type checking is effectively off for the GUI.** `pyproject.toml:72-75` sets `ignore_errors = true` for `app.*` ("344 pre-existing type errors across 53 files"); ruff ignores F401/F821/E402/F841/E401/F541 under `app/**` (`:65-67`). CI runs `ruff check .` and `mypy app/` (`.github/workflows/ci.yml:12-13`).

**F-A9P-14 — Dependency declared, unused.** `matplotlib>=3.9` (`pyproject.toml:21`) has no import under `app/`; charts are hand-drawn widgets (`app/gui/widgets/chart_list.py`, `bloom_strip.py`, `month_bar.py`). There is no `qasync` dependency (the brief's example); async work runs in `app/gui/workers/` (14 files, QThread workers).

**F-A9P-15 — Mockups referenced by the suite's contracts are gone from the tree.** `GUI/screen_structures/Screen_Structure_Index.md:7-30` cites `mockup_*.html` per screen; commit `6921bc8` (2026-07-04) deleted `Improvements/GUI_Improvements_V3/mockups/` (13 `mockup_*.html` + `rendered/current_*.png`, 45 paths). The approved 1.2.0 visual reference is an external artifact (`04_APPROVED_DESIGN_REVISION_2026-07-10.md:5`, claude.ai artifact `370bf3f9…`), not a repository file.

**F-A9P-16 — Conduct rules that already hold statically.** Flat by default: shadows only on hover/state (`app/gui/widgets/card.py:33-48`); exactly the two left-stripe exceptions (3 px selected row `light.qss:248,265,1374`; 4 px toast `:1487`); font family equals canon (`design_tokens.py:222-223`); spacing, type scale and button sizes equal canon.

## §3 Candidates

| ID | Source path @ pin | What | Verdict | Target repo and path | Lane | Q id |
|---|---|---|---|---|---|---|
| RC-A9P-01 | `Design_Template_Kit/anchoring-kit/emitters/emit-stack.mjs` @ f08e588 (`qt-qss`, :321-352) | Generated `tokens.py` (`TOKENS`, `ROLES`, `VARS`) from the Configuration | adopt as the PyApp stack artifact, behind an adapter | PlantLibrary_PyApp `app/gui/generated/tokens.py` (or the path the installer fixes) | B5 | Q-A9P-01 |
| RC-A9P-02 | `PlantLibrary_PyApp/app/gui/theme_utils.py` @ 35ddc63 (:45-92) | `theme_template_values()` — the seam that maps tokens to today's 174 `$vars` | keep; re-source from generated `TOKENS`/`ROLES` so QSS templates need no rename | same file | B5/B6 | Q-A9P-01 |
| RC-A9P-03 | `PlantLibrary_PyApp/resources/styles/{light,dark}.qss` @ 35ddc63 | Already pure templates (0 hex) | keep as templates; fix F-A9P-03 keys and F-A9P-06 asset | same files | B6 | Q-A9P-05 |
| RC-A9P-04 | `PlantLibrary_PyApp/scripts/check_token_drift.py` @ 35ddc63 | AST drift checker, 4 dicts | extend to the role layer (name-resolving evaluator, as this lane's scratch did) or retire for the Kit's drift check | same file, or Kit check in `scripts/design/` | B5 | Q-A9P-06 |
| RC-A9P-05 | `Design_Template_Kit/anchoring-kit/checks/check-literals.mjs` @ f08e588 (:42-44) | Literal checker that already parses `.py` (hash comments) and `.qss` (block comments) | adopt as PyApp's static literal gate (Q-G-04 (a) compatible) | PlantLibrary_PyApp `scripts/design/` per installer | B5 | — |
| RC-A9P-06 | `Design_Template_Kit/examples/plantlibrary-field-ledger/design/banned-colors.json` @ f08e588 (BAN-02) | Scoped `#16A34A` ban | adopt the scoping into the Configuration; amend `TOKEN_USAGE_NOTES.md:27` and design-adoption `SKILL.md:71` | SharedContracts `design-tokens/` (or `design/` per Q-G-01) | B5 | Q-A9P-06 |
| RC-A9P-07 | `PlantLibrary_PyApp/app/gui/devtools/scenario_provider.py` @ 35ddc63 | 33 deterministic scenarios × 24 screens (`SCREEN_VARIANTS`), incl. `theme.light`/`theme.dark` | reuse as the screenshot-capture matrix for methodology 03 in Phase C | same file; referenced from the design-migration workspace | B6 | — |
| RC-A9P-08 | `PlantLibrary_PyApp/GUI/screen_structures/` @ 35ddc63 (31 files) | Per-screen structure contracts incl. dialogs and wizard | reuse as methodology-02 screen contracts; map into the Configuration's `contracts/` | Configuration `contracts/` (Q-G-01) | B6 | Q-A9P-07 |
| RC-A9P-09 | `PlantLibrary_PyApp/tests/test_design_tokens.py` @ 35ddc63 | ~35 rule assertions over the rendered light QSS (DS-01..35) | keep as the QSS conformance oracle; repoint its literal hex assertions to roles when values move | same file | B6 | — |
| RC-A9P-10 | `PlantLibrary_PyApp/scripts/harness/regression_scope.py` @ 35ddc63 (:273, :566-587) | No route for `resources/styles/*.qss` | add a declared route mapping `resources/styles/*.qss` to the tests that render the stylesheet; update `test_harness_port.py:133` in the same change | same files | B6 | Q-A9P-04 |
| RC-A9P-11 | `PlantLibrary_PyApp` git `6921bc8^:Improvements/GUI_Improvements_V3/mockups/` | 13 V3 page mockups + rendered current PNGs | historical evidence only; do not restore as targets | none (cite by commit) | B6 | Q-A9P-07 |

## §4 Questions for the operator

| ID | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A9P-01 | How does PyApp consume the Kit's Qt artifact? | (a) generated `tokens.py` + `theme_utils.theme_template_values()` rewritten as an adapter that emits today's `$var` names; QSS templates untouched; `design_tokens.py` reduced to re-exports, then retired; (b) rename all QSS `$vars` to the Kit's `VARS` names (`light_accent_main`…) and split per theme; (c) keep hand-mirroring with an extended drift check | smallest diff to 3,802 QSS lines; the template seam already exists; one place to change | B5 PyApp anchoring; B6 token rows |
| Q-A9P-02 | Does `PY-V1-DS-03` (hand alignment to 1.2.0) still run, or is it absorbed by generation? | (a) absorbed: B6 delivers DS-03's done-when through the generated artifact and records DS-03 as superseded in STATE.md, validation cell pointed at the deferred register; (b) run DS-03 by hand first, generate later | doing it twice touches the same 161 role keys twice | B6 |
| Q-A9P-03 | "Follow system setting" theme | (a) implement OS colour-scheme follow (`QStyleHints.colorScheme`, PySide6 ≥ 6.5; installed 6.11.1) as a bugfix-bucket change; (b) remove the option; (c) record an accepted deviation | the control exists and lies; Qt supports it | B6 |
| Q-A9P-04 | How to unpark `.qss` at the harness closeout | (a) add a `resources/styles/` route in `regression_scope.py` + update `test_harness_port.py:133`; (b) every B6 row lists the `.qss` path with a literal non-pytest validation; (c) leave it and ledger each parked close | (a) fixes it once, in the adapted (unpinned) file; (b) repeats per row | B6, Phase C closeouts |
| Q-A9P-05 | Missing `check-white.svg` | (a) add a check glyph (`currentColor`, tinted from `on_accent` per theme) and resolve QSS `url()` against `ICONS_PATH` at render time instead of the cwd; (b) drop the `image:` rule and the matching test string | fixes the glyph and the cwd-relative path in one step | B6 |
| Q-A9P-06 | Scope of the `#16A34A` ban | (a) adopt the Kit's BAN-02 scope (accent/fill banned, chart series allowed) in the Configuration, `TOKEN_USAGE_NOTES.md` and design-adoption; (b) keep "anywhere" and change canon `CHART.series_1` | canon measured series_1 passing; the Kit already reconciled it | B5 (Configuration), B6 (DS-03 done-when) |
| Q-A9P-07 | Which targets does PyApp's migration design against? | (a) the Configuration's gallery pages generated from SharedContracts page contracts + `GUI/screen_structures` contracts; V3 HTML mockups historical only; (b) restore the V3 mockups as targets | P-DS-10 keeps page anatomy; V3 mockups predate 1.2.0 | B6 mockup/visual steps |
| Q-A9P-08 | Open SDA decisions SDA-DEC-02 (PyApp inversion mode) and SDA-DEC-05 (Android font policy) | (a) close SDA-DEC-02 as "fully generated via the Kit" once Q-G-01 is answered, recorded in SDA STATE.md; leave SDA-DEC-05 to the Android lane (PyApp font is canon Segoe UI stack, unaffected); (b) keep both open | SDA-DEC-02 is the same choice as Q-A9P-01 | B5 |
| Q-A9P-09 | Is PyApp's GUI work a re-skin or a restructure (methodology 4.1.0 trigger)? | (a) re-skin: screens and navigation stay (P-DS-10), 01a census optional and kept as an input only; (b) restructure: run 01a and 06a-06d | no new screens or navigation are asked for PyApp | B6 planning |

## §5 Reusable things this brief did not name

- `app/gui/devtools/scenario_provider.py` — deterministic fixture scenarios and per-screen variants (shell, dashboard, first_run, plant_list, plant_detail, wizard, search, settings, admin_sources, dataviz, states, component_gallery, approval_gallery, backup_restore, conflict_resolution, edit_instance, edit_profile, image_attribution, image_lightbox, location_editor, provider_setup, provenance_details, reenrichment_provider_selection, tag_management). The ready-made capture matrix.
- `GUI/screen_structures/Screen_Coverage_From_Source.md` and `Component_Library_Coverage_From_Screen_Structures.md` — an existing source-to-screen coverage map.
- `GUI/COMMON_GUI_CHANGE_PROTOCOL.md` — "contract before source" rule the checklist cites for GUI rows.
- `tests/test_design_tokens.py` — rule assertions over the rendered QSS (a conformance oracle once runs resume).
- `DESIGN.md` — already rewritten to field-ledger 1.2.0 (line 214-217, 301), so prose is ahead of code; usable as the PyApp `conduct-rules` source.
- `app/gui/icons.py` — SVG `currentColor` tinting by theme role; the generated artifact only needs role names, not icon changes.
- The PyApp V1 package's `PY1-B07` evidence shape (drift report with expected non-zero exit) — a template for a static drift leg.

## §6 Claims to verify

1. PRIMARY.600 is still Verdant. `sed -n 17p C:/Programmierung/SW_Development/PlantLibrary_PyApp/app/gui/design_tokens.py` prints `600: "#16A34A",`; `grep -n '"600"' C:/Programmierung/SW_Development/PlantLibrary_SharedContracts/design-tokens/tokens.json | head -1` prints the line with `#2A7A30`.
2. The QSS files hold no hex literal. `grep -ciE '#[0-9a-f]{6}' C:/Programmierung/SW_Development/PlantLibrary_PyApp/resources/styles/light.qss C:/Programmierung/SW_Development/PlantLibrary_PyApp/resources/styles/dark.qss` prints `:0` for both.
3. The checked-checkbox icon is missing. `grep -n check-white C:/Programmierung/SW_Development/PlantLibrary_PyApp/resources/styles/light.qss` prints line 1094, and `ls C:/Programmierung/SW_Development/PlantLibrary_PyApp/resources/icons/ | grep -c check-white` prints `0`.

## §7.1 UI source inventory

**Versions** (`pyproject.toml`): Python `>=3.11` (`:10`; machine runs 3.12); `PySide6>=6.7` (`:12`; installed in `.venv`: PySide6/Essentials/Addons/shiboken6 6.11.1); SQLAlchemy ≥2.0, alembic, Pillow, httpx, keyring, platformdirs, rapidfuzz, anthropic, matplotlib (unused, F-A9P-14). No `qasync`. Dev: pytest, pytest-qt, pytest-cov, ruff (0.15.21 installed), mypy (2.2.0 installed), types-requests. Package: pyinstaller.

**Entry point**: `main.py` → `app.run` → `app/main.py:main` (`:105-155`); console script `plant-library = app.main:main` (`pyproject.toml:54`). Window title `Plant Library` (`app/gui/main_window.py:262`), minimum size from `SHELL_SIZES` (`:263`).

**Package tree (`app/gui`, Python files and lines)**

| Package | .py files | Lines | Notes |
|---|---|---|---|
| `app/gui/` (top) | 11 | 3,483 | `main_window.py` 1,972; `design_tokens.py` 623; `navigation.py` 244; `app_state.py` 150; `theme_utils.py` 139; `actions.py` 138; `domain_colors.py` 112; `icons.py` 50; `motion.py` 29; `styles.py` 25 |
| `app/gui/views/` | 12 | 10,742 | see §7.4 |
| `app/gui/widgets/` | 42 | 7,108 | 41 widget modules (card, table, stat_card, toggle_switch, skeleton, toast, dialog_scaffold …) |
| `app/gui/wizard/` + `steps/` | 3 + 7 | 1,664 + 4,300 | add-plant wizard, first-sync assistant, 6 steps |
| `app/gui/dialogs/` | 15 | 3,145 | 13 dialogs + 1 shim + `__init__` |
| `app/gui/workers/` | 14 | 1,275 | QThread workers (no styling) |
| `app/gui/devtools/` | 2 | 708 | scenario provider |
| `app/gui/models/` | 2 | 383 | plant list table model |
| **Total** | **108** | **32,808** | |

**Resources**: `resources/styles/light.qss` 1,903 lines, `dark.qss` 1,899 lines (112 differing lines; ordering and a few spacing/disabled rules); `resources/icons/` 32 SVG (+ `.gitkeep`), loaded by `app/gui/icons.py:23-33` with `currentColor` replacement; `resources/translations/` empty. No `.qrc`, no compiled resources.

**Navigation**: sidebar `NavigationSidebar` (`app/gui/navigation.py:139-151`) with 8 primary items + Settings pinned below; views live in a stack registered in `MainWindow._view_widgets` (`main_window.py:410-516`); plant detail is pushed (`:380`); wizard and dialogs are modal.

| Nav id | Label | Class | File |
|---|---|---|---|
| dashboard | Dashboard | `DashboardView` | `app/gui/views/dashboard_view.py:89` |
| plants | Plants | `PlantListView` | `app/gui/views/plant_list_view.py:671` |
| plant_search | Search | `PlantSearchView` | `app/gui/views/plant_search_view.py:47` |
| calendar | Calendar | `CalendarView` | `app/gui/views/calendar_view.py:404` |
| statistics | Statistics | `StatisticsView` | `app/gui/views/statistics_view.py:116` |
| locations | Locations | `LocationsView` | `app/gui/views/locations_view.py:304` |
| admin_review | Admin Review | `AdminReviewView` | `app/gui/views/admin_review_view.py:1226` |
| sources | Sources & Imports | `SourcesImportsView` | `app/gui/views/sources_imports_view.py:583` |
| settings | Settings | `SettingsView` (8 tabs) | `app/gui/views/settings_view.py:1692` |
| (pushed) | — | `PlantDetailView` | `app/gui/views/plant_detail_view.py:239` |
| (unused) | — | `PlaceholderView` | `app/gui/views/placeholder_view.py:9` |

**Tests (listing only, nothing run)**: `tests/` holds 110 `.py` files — top level 38 `test_*.py` (incl. `test_design_tokens.py`, `test_phase7_gui_shell.py`, `test_phase8_shared_widgets.py`, `test_gui_fixture_scenarios.py`, `test_gui_improvements_*`, eight `test_*_primitives.py`, `test_repo_hygiene*.py`, `test_batch_package_contract.py`); `tests/gui/` 8 (dashboard, other views, provider setup dialog, main window sync, workers, dataviz batch 25); `tests/acceptance/` 1 (`test_harness_port.py`); `tests/integration/` 9; `tests/services/` 22; `tests/providers/` 17; `tests/db/` 9; `tests/plant_search/` 4; `tests/fixtures/legacy/`. Onboarding note for B6: the closeout harness refuses `resources/styles/light.qss` as `unmapped touched path` (F-A9P-09).

## §7.2 Token consumption

- **Source**: hand-written `app/gui/design_tokens.py` (docstring `:1-4` still points at `Documentation/Verdant_Modern_GUI_Design_System.docx`). No generated file, no import of `tokens.json`, no version pin anywhere in `app/` or `resources/`. The only canon reader is the out-of-band `scripts/check_token_drift.py:28`.
- **Equality with canon**: no (F-A9P-02). Equal groups: SEMANTIC, EXTRA, SPACE, TYPE_SCALE, BUTTON_SIZES, SHELL_SIZES, FONT_FAMILY, MONO_FONT_FAMILY. Divergent: PRIMARY, NEUTRAL, DARK, HIGHLIGHT, CHART (missing series_*), RADIUS (missing nav). Missing: SEMANTIC_DARK, CHART_DARK. Python-only: `LIGHT_SEMANTIC_ROLES`/`DARK_SEMANTIC_ROLES` (`:229`, `:316`), `ELEVATION` (`:565`), `SHADOW_COLOR`. Role layer 161 keys per theme vs canon 37 per theme.
- **Application**: one app-wide `QApplication.setStyleSheet` (`app/main.py:144`; re-applied `main_window.py:1556`); `theme_name` app property (`main_window.py:1555`) read by `current_theme_name()`; per-widget `setStyleSheet` f-strings (154 calls) for local styling; dynamic properties (`variant`, `textRole`, `tone`… 306 `setProperty` uses) select QSS rules; `polish()` helper (`theme_utils.py:100-105`); shadows by `QGraphicsDropShadowEffect` from `ELEVATION` (`theme_utils.py:108-139`).
- **Consumers**: 67 files import `design_tokens`, 31 import `theme_utils`, 5 import `domain_colors`; 31 GUI files import none (QSS-only or logic: e.g. `widgets/status_badges.py`, `notice_panel.py`, `confidence_widget.py`, all workers).

Per-file reference counts (files with any; `roles` = `theme_colors(`/`current_theme_name(`/`colors[`/`_colors[`/`domain_colors`; `dims` = `SPACE[`/`RADIUS[`/`TYPE_SCALE[`/`BUTTON_SIZES[`/`SHELL_SIZES[`; `prim` = `PRIMARY[`+`NEUTRAL[`; `sem` = `SEMANTIC[`):

| File | prim | sem | CHART[ | roles | dims |
|---|---|---|---|---|---|
| wizard/steps/step2_choose_match.py | 31 | 20 | 0 | 6 | 17 |
| wizard/steps/step4_choose_images.py | 18 | 3 | 0 | 5 | 14 |
| wizard/steps/step3_review_profile.py | 12 | 3 | 0 | 0 | 2 |
| widgets/disambiguation_widget.py | 6 | 2 | 0 | 10 | 15 |
| dialogs/tag_dialog.py | 5 | 0 | 0 | 1 | 7 |
| wizard/steps/step1_enter_name.py | 4 | 4 | 0 | 0 | 1 |
| views/calendar_view.py | 3 | 8 | 0 | 15 | 13 |
| views/plant_search_view.py | 3 | 1 | 0 | 0 | 7 |
| widgets/tag_badge.py | 3 | 0 | 0 | 0 | 7 |
| domain_colors.py | 2 | 43 | 6 | 0 | 0 |
| wizard/steps/step5_garden_details.py | 2 | 4 | 0 | 0 | 1 |
| views/plant_detail_view.py | 1 | 1 | 0 | 0 | 26 |
| widgets/image_gallery.py, image_lightbox.py, filter_chip_bar.py, toggle_switch.py, workers/thumbnail_worker.py, theme_utils.py | 1 each | 0 | 0 | 0–15 | 0–19 |
| views/sources_imports_view.py | 0 | 2 | 0 | 15 | 0 |
| widgets/event_timeline.py | 0 | 5 | 1 | 0 | 0 |
| views/plant_list_view.py | 0 | 0 | 0 | 19 | 29 |
| views/dashboard_view.py | 0 | 0 | 0 | 0 | 30 |
| views/settings_view.py | 0 | 0 | 0 | 0 | 23 |
| views/statistics_view.py | 0 | 0 | 0 | 0 | 17 |
| wizard/steps/step6_confirmation.py | 0 | 1 | 0 | 17 | 9 |
| views/locations_view.py | 0 | 0 | 0 | 15 | 5 |
| widgets/skeleton_widget.py | 0 | 0 | 0 | 7 | 22 |
| widgets/stat_card.py | 0 | 0 | 0 | 5 | 16 |
| dialogs/sync_conflict_dialog.py | 0 | 0 | 0 | 3 | 15 |
| views/admin_review_view.py | 0 | 1 | 0 | 5 | 12 |
| remaining 40 files | 0 | 0–1 | 0–1 | 0–9 | 0–9 |

Totals: `PRIMARY[` 37, `NEUTRAL[` 59, `SEMANTIC[` 101, `CHART[` 8, roles 185, dims 461.

## §7.3 Literals that remain

Excluded as generated/vendor/non-GUI: `.venv/`, `__pycache__/`, `.mypy_cache/`, `.ruff_cache/`, `.pytest_cache/`, `graphify-out/` (gitignored tool output), `plant_library.egg-info/`, `.claude/skills/impeccable/scripts/**` (vendored skill), `tests/`, `app/gui/design_tokens.py` (the token source itself, counted separately).

| Measure | QSS (light / dark) | Python `app/gui` | Top offenders (line example) |
|---|---|---|---|
| Hex colour | 0 / 0 | 164, all in `design_tokens.py` (6 banned-green hits: `:15-17`, `:93`, `:109`, `:118`) | outside GUI: `app/constants.py:70-74`, `app/services/confidence_service.py:174`, `app/db/seed.py:18` |
| `rgba(` | 0 / 0 | built by the `rgba()` helper only (`design_tokens.py:592`) | used at `theme_utils.py:82-91` |
| `QColor(` | — | 50 in 18 files; 1 literal | `toggle_switch.py` 14, `skeleton_widget.py` 5, `plant_list_view.py` 5, `step4_choose_images.py` 5; literal `theme_utils.py:120` |
| Literal px | 129 / 126 (1 px ×55, 2 px ×25 borders; sizes 12/18/24/28/32/36/40 px e.g. `light.qss:334`, `:416`, `:876-893`) | 126 in strings; 71 numeric size calls | strings: `calendar_view.py` 25, `step2_choose_match.py` 17, `step3_review_profile.py` 14, `sources_imports_view.py` 14; size calls: `step2_choose_match.py:132,238,321` (9), `settings_view.py:80,371,380` (7), `plant_list_view.py:304-313` (6), `calendar_view.py:110,145,314` (6) |
| Inline `setStyleSheet("…")` | — | 154 calls, 57 literal-string | `step2_choose_match.py` 29 (10 literal, e.g. `:326` `"font-weight: 600;"`), `sources_imports_view.py` 15, `calendar_view.py` 14, `step6_confirmation.py` 13, `step3_review_profile.py` 12, `locations_view.py` 9, `disambiguation_widget.py` 9, `source_detail_dialog.py` 7 (`:58`), `field_provenance_detail_dialog.py` 7 (`:56`) |
| Font family | 0 literal (all `$font_family`/`$mono_font_family`) | only `design_tokens.py:222-223` | — |
| Font size literal | — | 34 (9 px ×3, 10 px ×10, 11 px ×12 below scale) | `calendar_view.py` 9 (`:105`, `:191`, `:241`, `:246`, `:459`), `sources_imports_view.py` 7, `step2_choose_match.py` 4, `locations_view.py` 4 (`:160`, `:165`) |
| Border-radius | 69 / 69 rules; 1 literal each (`light.qss:1243`, `0`); `pill_input` 1 each | 42 occurrences, 20 literal px: 10 px ×9, 6 px ×6, 12 px ×4, 4 px ×4, 8 px ×1, 5 px ×1, 16 px ×1 | `calendar_view.py` 6 (`:103`, `:164`, `:217`, `:551`), `step3_review_profile.py` 4 (`:137`, `:401`), `tag_dialog.py` 3 (`:110`, `:135`, `:306`), `sources_imports_view.py` 3 (`:105`, `:120`, `:419`), `admin_review_view.py:332` |
| Icon paths | 4 `url(resources/icons/…)` each, cwd-relative; 1 missing file (`check-white.svg`) | 26 `load_icon(`/`.svg` uses, all through `icons.py` by name | `main_window.py` 5, `plant_list_view.py` 5 |

Concentration: of 126 Python px literals, 70 (56 %) sit in four files (`calendar_view.py`, `step2_choose_match.py`, `step3_review_profile.py`, `sources_imports_view.py`); of 96 raw primitive reads, 61 (64 %) in the three wizard steps 2-4.

## §7.4 Screens

| Screen | Class @ file | SharedContracts page contract | Suite contract (`GUI/screen_structures/`) | Mockup | MVP / V1 screenshots (static) | Package rows | Token state |
|---|---|---|---|---|---|---|---|
| Shell | `MainWindow` @ `app/gui/main_window.py:192`; `NavigationSidebar` @ `navigation.py` | `PageContract_shell.md` | `shell` | V3 `mockup_shell.html` (deleted, `6921bc8`); approved 1.2.0 artifact (external) | `pyapp_gui/01_startup.png`, `70_maximized.png`; `PY-V1-GAP-CLOSURE-20260715-01/01_pyapp_initial_window.png` | PY-V1-UX-01 (toolbar sync indicator), PY-V1-DS-03 | roles + dims; clean of primitives |
| Dashboard | `DashboardView` @ `views/dashboard_view.py:89` | `PageContract_dashboard.md` | `dashboard`, `first_run` | V3 `mockup_dashboard.html` (deleted) | `PY-V1-GAP-CLOSURE-20260715-02/01_…`, `03_…` | PY-V1-DS-03 | dims only (30); QSS-styled — token-clean |
| Plants | `PlantListView` @ `views/plant_list_view.py:671` (+ `plant_list_table_model.py`) | `PageContract_plants.md` | `plant_list` | V3 `mockup_plant_list.html` (deleted) | `pyapp_gui/13_sanity_plants.png`, `53_…`, `58_…`; `GAP-CLOSURE-03/01_…`, `11_…` | PY-V1-SYNC-REFRESH-01 (done), PY-V1-DS-03 | roles + dims; token-clean |
| Search | `PlantSearchView` @ `views/plant_search_view.py:47` | `PageContract_search.md` | `search` | V3 `mockup_search.html` (deleted); `Documentation/Search_Improvement_Mockup.png` | none found | PY-V1-DS-03 | 3 primitive reads — partly legacy |
| Calendar | `CalendarView` @ `views/calendar_view.py:404` | `PageContract_calendar.md` | `dataviz` | V3 `mockup_dataviz.html` (deleted) | `pyapp_gui/56_calendar_view.png` | PY-V1-DS-03, PY-V1-UX-03 (harvest preset) | **legacy**: 25 px literals, 9-11 px fonts, off-scale radius |
| Statistics | `StatisticsView` @ `views/statistics_view.py:116` | `PageContract_statistics.md` | `dataviz` | V3 `mockup_dataviz.html` (deleted) | none found | PY-V1-DS-03 (chart order + CHART_DARK) | dims + `domain_colors` (light-only, F-A9P-05) |
| Locations | `LocationsView` @ `views/locations_view.py:304` | `PageContract_locations.md` | `dataviz`, `location_editor` | — | none found | PY-V1-DS-03 | roles; 11 px fonts — partly legacy |
| Admin review | `AdminReviewView` @ `views/admin_review_view.py:1226` (5 tabs, `_PlantFieldReviewDialog` `:303`) | `PageContract_admin_review.md` | `admin_sources` | V3 `mockup_admin_sources.html` (deleted) | `pyapp_gui/85_after_review_click.png` | PY-V1-DS-02 (impeccable audit, conflict surfaces) | roles + dims; mostly clean |
| Sources & Imports | `SourcesImportsView` @ `views/sources_imports_view.py:583` | `PageContract_sources.md` | `admin_sources` | V3 `mockup_admin_sources.html` (deleted) | none found | PY-V1-DS-03 | **legacy**: 14 px literals, 15 setStyleSheet |
| Settings (8 tabs) | `SettingsView` @ `views/settings_view.py:1692` | `PageContract_settings.md` | `settings` | V3 `mockup_settings.html` (deleted) | `pyapp_gui/02_settings.png`, `03_account_sync.png`, `12_…`, `51_…`, `52_…`; `GAP-CLOSURE-02/04_…`, `GAP-CLOSURE-03/02_…`, `03_…`, `09_…`, `10_…` | PY-V1-UX-02 (garden picker), PY-V1-SYNC-ERROR-01 (done), PY-V1-DS-02, PY-V1-WALK-01 | dims; clean |
| Plant detail | `PlantDetailView` @ `views/plant_detail_view.py:239` (+ `_ProviderSelectDialog` `:105`) | `PageContract_plant_detail.md` | `plant_detail`, `reenrichment_provider_selection` | V3 `mockup_plant_detail.html` (deleted) | `pyapp_gui/57_tomato_detail.png`, `60_care_tab.png`, `61_…`, `62_…`, `63_task_list.png` | PY-V1-DS-03 | dims; 1 primitive read |
| Add-plant wizard (6 steps) | `AddPlantWizard` @ `wizard/add_plant_wizard.py:90`; steps @ `wizard/steps/step1…step6` | none | `wizard` | V3 `mockup_wizard.html` (deleted) | none found | PY-V1-DS-03 | **legacy**: steps 2-4 hold 64 % of raw primitive reads; steps 1-6 hold 46 % of `setStyleSheet(` calls |
| First-sync assistant | `FirstSyncAssistantDialog` @ `wizard/first_sync_assistant_dialog.py:20` | none | — (sync era) | — | `pyapp_gui/06_fsa_opened.png`, `15_…`, `21_…`, `39_…`, `40_…` | PY-V1-DS-02, PY-V1-WALK-01 | dims; clean |
| Sync conflict list / dialog | `SyncConflictListDialog` @ `dialogs/sync_conflict_list_dialog.py:28`; `SyncConflictDialog` @ `dialogs/sync_conflict_dialog.py:45` | none | `sync_conflict_review` | — | `pyapp_gui/82_conflict_dialog.png`, `83_…` | PY-V1-DS-02, PY-V1-WALK-01 | roles + dims; clean |
| Conflict (field) | `ConflictDialog` @ `dialogs/conflict_dialog.py:27` (alias `conflict_detail_dialog.py`) | none | `conflict_resolution` | V3 related (deleted) | — | PY-V1-DS-02 | roles; 1 literal style |
| Edit instance | `EditInstanceDialog` @ `dialogs/edit_instance_dialog.py:32` | none | `edit_instance` | V3 related (deleted) | `pyapp_gui/77_…`, `79_edit_garden_instance_dialog.png`, `80_notes_typed.png` | PY-V1-WALK-01 (offline edit) | dims; clean |
| Edit profile | `EditProfileDialog` @ `dialogs/edit_profile_dialog.py:74` | none | `edit_profile` | V3 related (deleted) | `pyapp_gui/74_edit_dialog_raw.png` | — | dims; clean |
| Provider setup | `ProviderSetupDialog` @ `dialogs/provider_setup_dialog.py:129` | none | `provider_setup` | V3 related (deleted) | `GAP-CLOSURE-01/01b_…`, `GAP-CLOSURE-02/02_provider_setup_dialog.png` | — | dims; clean |
| Source / field provenance / provider result detail | `SourceDetailDialog` :28, `FieldProvenanceDetailDialog` :27, `ProviderResultDetailDialog` :26 (all `dialogs/`) | none | `provenance_details` | V3 related (deleted) | — | — | roles via inline f-strings; 11 px fonts |
| Image attribution / lightbox | `ImageAttributionDialog` @ `dialogs/image_attribution_dialog.py:25`; `ImageLightbox` @ `widgets/image_lightbox.py:28` | none | `image_attribution`, `image_lightbox` | V3 related (deleted) | — | — | clean (1 primitive read in lightbox) |
| Location editor | `LocationDialog` @ `dialogs/location_dialog.py:24` | none | `location_editor` | V3 related (deleted) | — | — | roles; clean |
| Tag management | `TagDialog` @ `dialogs/tag_dialog.py:42` | none | `tag_management` | none | — | — | **legacy**: 5 primitive reads, off-scale 16 px radius |
| Backup / restore | `BackupRestoreDialog` @ `dialogs/backup_restore_dialog.py:28` | none | `backup_restore` | V3 related (deleted) | — | — | dims; clean |
| Quick switch | `_QuickSwitchDialog` @ `main_window.py:95` | `PageContract_shell.md` (global search) | `shell` | — | — | — | QSS-styled |
| Destructive confirm | `DestructiveConfirmationDialog` @ `widgets/dialog_recovery.py:22` | none | `states` | — | — | — | dims; clean |

Sign-in: the OIDC flow runs in the system browser (`pyapp_gui/26_browser_login.png`, `43_keycloak_login_page.png`) — no Qt screen. Gui-validation rows in the package: PY-V1-WALK-01, PY-V1-UX-01, PY-V1-UX-02, PY-V1-DS-03, PY-V1-REL-01. Design rows: PY-V1-DS-01 (blocked on SDA-B02), PY-V1-DS-02 (gated), PY-V1-DS-03 (todo), PY-V1-DS-04 (done).

## §7.5 Gate assumptions against this client

| Gate | What it checks | Holds | Does not hold |
|---|---|---|---|
| design-adoption (superproject `SKILL.md`) | Pre-work read of canon (`tokens.json`, `semantic-roles.json`, `TOKEN_USAGE_NOTES.md`, platform mapping, `04_*` P-DS-01..10); adoption row; hard rules | Paths exist; `design_tokens.py` is the token-mirror file (`:23`); adoption row `PY-V1-DS-03`/`PY1-B06` exists and is todo (`:61`); P-DS-06 fonts unchanged (Segoe stack equals canon); P-DS-08 flat-by-default and two-stripe rule hold (F-A9P-16) | "`#16A34A` never anywhere" (`:71`) contradicts canon `CHART.series_1` (F-A9P-10); "regenerate where the suite generates" (`:82`) has no PyApp generator; it points to `platform-mapping-python.md`, which is stale (F-A9P-12); no skill text knows the Kit Configuration or `CONSUMED_DESIGN.md` (Q-G-07) |
| impeccable 3.8.0 (PyApp `.claude/skills/impeccable/`) | Design craft guidance; `context.mjs` loads PRODUCT.md/DESIGN.md; `audit`/`critique` commands; `npx impeccable detect` anti-pattern scan | Activation gating per `CLAUDE.md:28-30` (only rows with `impeccable:<cmd>`; only PY-V1-DS-02); DESIGN.md is current field-ledger prose | Detector scans no `.py`/`.qss` (F-A9P-11); `.impeccable/design.json` ramp is Verdant; guidance assumes CSS (`clamp()`, `ch`, OKLCH, browser screenshots) — Qt has no such units; `palette.mjs` "brand-new project" branch must not fire (committed brand exists) |
| gui-validation (superproject canonical + PyApp pointer copy) | OS-level mouse/keyboard driving: foreground verification, PID-specific kills, evidence | Window title "Plant Library" (`main_window.py:262`) matches the lesson log (`SKILL.md:289`); the app is a single-window PySide6 desktop app with modal dialogs and a browser OIDC hop, as assumed; pointer copy in PyApp names exactly this | Assumes the operator's live desktop; the program's one test slot belongs to the Conductor, so nothing here is drivable in Phase B (rule 1); the skill has no knowledge of the scenario provider (deterministic states) that could replace much of manual driving |
| SDA-DEC-05 | Android font policy (system/Roboto) | Not applicable to PyApp: PyApp uses the canon desktop stack `"Segoe UI", "SF Pro Text", system-ui` | The brief's reading "SDA-DEC-05 system font" for PyApp does not match SDA `STATE.md:25` (Android only); PyApp's open decision is SDA-DEC-02 (inversion mode) |

## §7.6 Design-migration census shape (methodology 4.1.0)

Two census artifacts apply: prompt 01's **mechanical design census** (always) and prompt 01a's **function/UI census** (only for a restructure; Q-A9P-09 recommends re-skin, so 01a is input only).

**Prompt 01 mechanical design census (filled)**: colour literals §7.3 (Python 164 in one file; QSS 0); dimension literals §7.3 (126 + 71 Python, 129/126 QSS); radii distinct values in Python 4/5/6/8/10/12/16 px + tokens; font families 1 stack + 1 mono; font sizes 9-16 px literals (25 below scale); detector summary — not available (F-A9P-11), Kit `check-literals.mjs` would be the detector; drift dry-run — static diff F-A9P-02 (no emitter run).

**Function / UI census header**

| Field | Value |
|---|---|
| Census date | 2026-10-13 |
| Repository | PlantLibrary_PyApp @ 35ddc63 |
| Configuration | none (no `design/CONSUMED_DESIGN.md`; Q-G-01) |
| Stack adapter | §0.2 below |
| Status | DRAFT (static input for B6, not a workspace artifact) |

**§0.2 Stack adapter (PySide6)**

| Question | This stack's answer |
|---|---|
| Operations | public methods (no leading `_`) of classes and module functions in `app/services/*.py`, extracted by AST |
| UI calls | `\b<method>\(` text occurrences anywhere under `app/gui/**` (views, dialogs, wizard, widgets, workers) |
| Matcher | method-name match (desktop has no path segments); weaker than segment-wise: same-named methods on different services collide — every tier-1 row needs a hand check |
| One view | a `QWidget` subclass added to `MainWindow._view_widgets` (`main_window.py:410-516`), the pushed `PlantDetailView`, or a `QDialog`/`DialogScaffold` subclass |
| Navigation entry | a `NavigationSidebar` item (`navigation.py:141-150`), a menu action (`main_window.py` `_build_menus`), or a toolbar action |
| One subsystem | one module of `app/services/` (30), plus `app/providers/` (20 modules) |

**§1 Pass A totals (static, low-medium confidence)**: 200 public operations in 30 service modules; 104 name-referenced from `app/gui`; 96 not. Modules with zero name references: `ai_extraction_service` (5 ops; `AdminReviewView` has an `_AIExtractionTab` at `admin_review_view.py:993` — check by hand), `normalization_service` (15, likely internal), `profile_completeness` (2), `request_identity` (2, infrastructure), `wfo_snapshot_service` (6). Low reach: `confidence_service` 1/13, `plant_creation_service` 7/18, `plant_cache_service` 2/8. Tier-1 `CM-*` rows are **not assigned** here — every unreached name needs the hand check the prompt requires.

**§4 Pass B**: 11 views (9 nav-reached, plant detail link-reached, `PlaceholderView` unreached — `structure` candidate or dead code), 1 wizard (toolbar/menu `add_plant` action), 14 named dialogs + 1 quick-switch dialog, all link/action-reached.

**§5 Other operator surfaces**: CLI flag `--offline` (`app/main.py:112`), env `PLANT_LIBRARY_AUTOCLOSE_MS` (`:146`), `backend/` (FastAPI-era package in the same repo, not represented in the GUI), `scripts/` (drift check, harness, hygiene).

**06a / 06b inputs available statically**: forward rows = the open PyApp V1 rows in §7.4; settings inventory = `settings_view.py` 8 tabs (`_GeneralTab` `:158` … `_AccountSyncTab` `:1364`); page tree = §7.1 navigation table; provenance markers = `widgets/source_badge.py`, `field_provenance_widget.py`.

**Needs a running app or a screenshot → deferred-validation register** (proposed rows; what, which skill, after which lane):

| ID | What would be run | Skill | After |
|---|---|---|---|
| DV-A9P-01 | Light + dark capture of every `SCREEN_VARIANTS` screen (24) through the scenario provider, as the current-state baseline (methodology 03) | gui-validation / scenario provider | B6 start (before) and B6 end (after) |
| DV-A9P-02 | Checked checkbox shows a glyph in both themes (F-A9P-06) | gui-validation | B6 |
| DV-A9P-03 | QSS `url()` icons render when launched from a cwd other than the repo root and from the packaged build | gui-validation (+ PY-V1-REL-01) | B6 |
| DV-A9P-04 | Startup with persisted `theme=dark`: no widget shows light-role colours before the first theme change (F-A9P-08) | gui-validation | B6 |
| DV-A9P-05 | "Follow system setting" follows the OS scheme (Q-A9P-03) | gui-validation | B6 |
| DV-A9P-06 | Dark-theme contrast and `SEMANTIC_DARK` use on rendered surfaces (P-DS-04; F-A9P-05) | gui-validation + contrast measurement | B6 |
| DV-A9P-07 | Retiring `pill_input` (19) for `full` does not drop rounding on fixed-height inputs (`design_tokens.py:138-143` documents Qt's half-height cutoff) | gui-validation | B6 |
| DV-A9P-08 | Rendered QSS of both themes byte-compared before/after the generated artifact lands (PY-V1-DS-01 done-when) | the suite's design-token tests via run-batch validation | B5/B6 |
| DV-A9P-09 | impeccable audit + critique of sync-era surfaces (PY-V1-DS-02) on fresh screenshots | impeccable:audit | after DV-A9P-01 |
| DV-A9P-10 | Chart series order and `CHART_DARK` on statistics/calendar (P-DS-07) | gui-validation | B6 |

## §7.7 Stack facts for the anchoring (lane B5)

- **Shape that fits**: a QSS with variables is impossible in Qt, and this app already solved it: QSS files are `string.Template` sources with `$identifier`/`${identifier}` placeholders, rendered per theme in Python. A generated artifact therefore has to be **a Python module**, not a generated `.qss`. Two fits:
  1. *Adapter (recommended, Q-A9P-01 (a))*: Kit `qt-qss` → `tokens.py` (`TOKENS`, `ROLES`, `VARS`) checked into PyApp; `theme_utils.theme_template_values(theme)` builds today's flat names from `TOKENS`/`ROLES[theme]`; `design_tokens.py` re-exports the dict names its 67 importers use (`PRIMARY`, `SPACE`, `TYPE_SCALE`, `theme_colors`…) from the generated data until they are migrated, then is deleted. QSS untouched except F-A9P-03.
  2. *Rename*: rewrite 174 distinct `$vars` in each QSS to the Kit's `VARS` names. `VARS` prefixes roles by theme (`light_accent_main`), so one template would need either two template files with different names (today's model) or a per-theme un-prefixing step anyway.
- **What the Kit must emit for Qt so the client can be pinned**: (i) `tokens.py` with deterministic key order and a header carrying the Configuration name + version (today the header carries only the regenerate command — `emit-stack.mjs:339-345`); (ii) role values resolved per theme including `states` and `chart` sub-groups (canon `semantic-roles.json` has them; PyApp role names are flat, e.g. `status_success_bg` → needs a documented flattening rule); (iii) numeric dimensions as numbers, not strings with units (QSS templates append `px` themselves, e.g. `${space_4}px`); (iv) the elevation/shadow tokens kept in `TOKENS` (emitter skips shadows from `VARS`, `:329`; PyApp parses `ELEVATION` strings in `theme_utils.py:31-34`); (v) a stable output path the PyApp installer records in `design/conformance/CONSUMED_DESIGN.md` (Q-G-01 (a)); (vi) `check-literals.mjs` configured for `app/gui/**/*.py` and `resources/styles/*.qss` with `design_tokens.py`/`tokens.py` allow-listed. Whether the emitter output was ever imported by a Qt client is not shown in the Kit (A4's item); nothing in PyApp proves it.
- **Python-only role keys**: PyApp has 161 role keys per theme against canon's 37 (+ `states`, `chart`). The 124 extra keys are compositions (`notice_*`, `confidence_*`, `readiness_*`, `button_*`, `table_*`…) that the adapter must derive from canon roles, or the Configuration must add them (a P-DS-05 extension) — a B5 decision, not a mechanical one.
- **Lint / format / type-check (names only; Q-G-04 (a))**: `ruff check` and `ruff format` (config `pyproject.toml:63-67`, `:85-96`, format excludes four harness files), `mypy` (`:69-75`, `app.*` errors ignored), all also in CI (`.github/workflows/ci.yml:12-13`). No `black`, no `pyright`, no QSS linter. Static design checks available: `scripts/check_token_drift.py` (suite), Kit `check-literals.mjs` (once installed). The hygiene checker under `scripts/hygiene/repo_hygiene_check.py`.
- **Closeout coupling**: any B6 change to `resources/styles/*.qss` parks at the harness until RC-A9P-10 / Q-A9P-04 is decided.
