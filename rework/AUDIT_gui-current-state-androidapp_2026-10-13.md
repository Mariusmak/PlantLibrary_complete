# GUI current state — PlantLibrary_AndroidApp — lane A9 (read-only analysis, 2026-10-13)

*Lane A9-android, Phase A, read-only static scan. AndroidApp @ `5d6410f` (main), SharedContracts @ `d43f7a2`,
Workspace @ `6b4b88b`, Design_Template_Kit @ `f08e588` (emitter, literal and banned-colour checks, the field-ledger
example only), superproject @ `8702e0a` (`design-adoption`, `android-validation` skills). Tools: Read/grep/find/wc/diff
over files, one throw-away Python value diff in the session scratchpad (static comparison of two text files), one
read of the approved mockup artifact. Nothing was built, compiled, installed or launched; no emulator, no Gradle.
`build/` and `.gradle/` folders and `PlantLibrary_SharedContracts/generated/kotlin` (generated network client) are
excluded from every count as generated.*

## §0 Summary

1. The UI is 3,556 Kotlin lines in 14 Gradle modules: `:app` (entry, gate, nav graph), `:core:design` (hand-written theme, 339 lines) and seven `:feature:*` modules with 15 screens and 12 ViewModels. Compose BOM 2024.06.00 (Material3 1.2.1, UI 1.6.8), Kotlin 1.9.24, AGP 8.13.2, Navigation 2.7.7. There are no test source files.
2. Tokens reach Compose through a **hand-transcribed mirror** of `tokens.json`. There is no generator, no copied JSON and no colour resource. The mirror is the **pre-1.2.0** palette: 59 values equal the canon, 26 differ and 49 are missing. It holds the banned greens `#16A34A` (light M3 `primary`), `#22C55E` (focus) and `#4ADE80` (dark `primary`). `semantic-roles.json` is not consumed.
3. Feature code has **0 colour literals** and **0 references to the custom token objects**. All colour reaches the screens through `MaterialTheme`. Spacing is the opposite: **82 raw `N.dp` literals** in 15 files, all on the 4-px grid, 50 % of them in 3 files. Only `EmptyState` uses the spacing tokens.
4. `Theme.kt` sets 17 Material3 colour roles. The rest (`secondaryContainer`, `surfaceContainer*`, `tertiary*`, `outlineVariant`, …) fall back to Material baseline values. The light scheme binds `background` to `NEUTRAL.50`, but the canon app background is `NEUTRAL.100`. The launch theme is light-only. Dark mode has never been captured.
5. Screens: 15 views (3 gate, 5 bottom-nav, 7 pushed). Five Android page contracts cover 9 of them. Route names in the contracts differ from the code (`plantDetail/{profileId}` vs `plant_detail/{plantSyncId}`, `addPlant` vs `add`, `settings` vs `settings_account`). The approved mockup holds 4 Android phones (light and dark) and uses a different bottom-nav order.
6. The design rows are untouched. `AN-V1-DS-05` (value adoption), `-DS-02/03/04` are `todo` and `-DS-01` is `gated`. Only `-DS-06`, a report-only drift script, is done. That script cannot exit 0 after DS-05, because canon `CHART.series_1` is `#16A34A`. It also skips HIGHLIGHT, CHART, EXTRA and both `*_DARK` groups.
7. The Kit's Compose emitter exists (`emit-stack.mjs`, stack `compose`), but nothing proves it. The Kit holds no `.kt` file. The emitter writes `package design.generated` and `Tokens.Color.*` / `LightRoles` / `DarkRoles`. It emits no font weights, `TextStyle`, `Shapes` or `ColorScheme`. The Kit's literal check misses Kotlin's `Color(0xFF…)` and `16.dp`. Its banned scan has no ARGB spelling.
8. No compile-free Kotlin check exists: no ktlint, no detekt, no spotless, no `.editorconfig`. What can run without Gradle: `scripts/check_token_drift.py`, the hygiene checker and the Kit's node checks (blind to Kotlin, see 7).
9. Assumptions: SDA-DEC-05 (system font) holds. SDA-DEC-04 (Material Symbols) does not: the app uses `material-icons-extended`. SDA-DEC-03 (native capture) holds only in mechanism, not in its naming or dark capture. All five SDA-DEC rows are still `open` in their package `STATE.md`.
10. Static census draft: 61 repository-layer operations. The UI reaches 47 of them. 8 are internal, 1 is dead, and 4 are tier-1 `capability-missing` candidates: favourite, personal notes, note edit and confidence. A second table covers the 40 generated REST operations.
11. Seven operator questions (Q-A9A-01..07), fourteen reuse candidates, and twelve items for the deferred-validation register.

## §1 Coverage

| Item | Status (read / partly read / not read) | Reason |
|---|---|---|
| Kickoff prompt §1, §2 (Q-G-01, -04, -07, -08) | read | brief rule 6 |
| `settings.gradle.kts`, root `build.gradle.kts`, `gradle/libs.versions.toml`, `gradle/wrapper/gradle-wrapper.properties`, `gradle.properties` | read | versions, module set |
| `app/build.gradle.kts`, `core/design/build.gradle.kts`, `feature/home/build.gradle.kts` | read | compose setup; other module gradle files grep-only |
| `app/src/main/**` (6 `.kt`, manifest, all 7 res files) | read | entry, gate, nav graph, resources |
| `core/design/**` (6 `.kt`) | read | the theme |
| `feature/**/*Screen.kt` (15) | partly read | grep in full (theme refs, literals, components, strings, icons); read line by line around findings only |
| `feature/**/*ViewModel.kt`, `core/data`, `core/sync`, `core/auth`, `core/network` | partly read | public-operation extraction and call-site matching by grep; no logic read |
| `scripts/check_token_drift.py` | read | the only token check |
| `CLAUDE.md` (AndroidApp), `docs/compose_theme_plan.md`, `docs/navigation_plan.md` | read | design context, mapping rationale |
| `docs/*` other 9 files, `README.md`, `AGENTS.md` | not read | not GUI-current-state material; `docs/module_architecture.md` staleness is lane A6's F-A6A-11 |
| `implementation/System_V1_Implementation/TASK_CHECKLIST.md` | read | all rows |
| `…/TASK_CONTEXT.md` | partly read | anchors SHELL-01, DS-01..05, QA-01 |
| `…/BATCH_PLAN.md` | partly read | headings; AN1-B08, AN1-B11 |
| `…/validation/AN1-B12_token_drift.md` | partly read | grep for banned hits and exit code |
| `implementation/MVP/evidence/**` | partly read | file listing of every screenshot folder; one screenshot viewed (`validation_screenshots_2026-07-10_an_b12/03_current.png`); evidence markdown not read |
| `…/System_V1_Implementation/validation/evidence/AN-V1-LOCAL-OIDC-01-20260715-01/` | partly read | listing only |
| `.claude/skills/impeccable/**` | partly read | `SKILL.md` head, detector file-type sets, visual engine head; compared byte-wise with PyApp and Conductor copies |
| SharedContracts `design-tokens/*` (7 files) | read | canon; `semantic-roles.json` head and meta only |
| SharedContracts `page-contracts/android/*` (7 files) | partly read | `README`, `EXCLUSIONS`, `home` in full; others route, primary and secondary actions |
| SharedContracts `generated/kotlin/.../apis/*.kt` | partly read | public method names only, for census pass A |
| Workspace `System_Design_Architecture/STATE.md` | partly read | decisions table (lines 1-40), 135-150 |
| Workspace `…/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` | read | P-DS-01..10 |
| Approved mockup artifact `claude.ai/code/artifact/370bf3f9-…` | partly read | the Android section (phones 1-4) and headings only |
| Methodology 4.1.0 `FUNCTION_UI_CENSUS_TEMPLATE.md`, `PROMPTS/01a_FUNCTION_UI_CENSUS.md` | read | census shape |
| Methodology `PROMPTS/01_SOURCE_INVENTORY.md` | partly read | inputs and the "Mechanical design census" section |
| Methodology `FORWARD_SURFACE_TEMPLATE.md`, `INFORMATION_MODEL_TEMPLATE.md`, `INFORMATION_ARCHITECTURE_TEMPLATE.md`, `PROMPTS/06a…`, `PROMPTS/06b…` | partly read | headings and required inputs |
| Superproject `.claude/skills/design-adoption/SKILL.md` | read | gate assumptions |
| Superproject `.claude/skills/android-validation/SKILL.md` | partly read | capture and naming lines |
| Kit `anchoring-kit/emitters/emit-stack.mjs` | partly read | lines 1-31, 228-305, 366-404 |
| Kit `anchoring-kit/checks/check-literals.mjs` | partly read | lines 1-60 |
| Kit `anchoring-kit/checks/check-banned-colors.mjs` | partly read | lines 20-60 |
| Kit `examples/plantlibrary-field-ledger/design/banned-colors.json` | partly read | BAN-01..03 |
| Kit `examples/plantlibrary-field-ledger/design/tokens.json`, `semantic-roles.json` | partly read | top-level group names |
| Gradle user cache `compose-bom-2024.06.00.pom` | partly read | resolved material3 / ui versions (static file) |

## §2 Findings

- **F-A9A-01 Module and UI shape.** `PlantLibrary_AndroidApp/settings.gradle.kts:31-46` includes 14 modules. The UI lives in `:app` (415 lines), `:core:design` (339) and `:feature:{home,plants,tasks,addplant,sync,auth,more}` (2,802). Together that is 3,556 lines, 15 `*Screen.kt` files and 12 ViewModels. The network client is a composite build of the generated Kotlin client (`settings.gradle.kts:25`). `PlantLibrary_AndroidApp/app/build.gradle.kts:43` passes `-Xskip-metadata-version-check` because the generated client brings kotlin-stdlib 2.2.20 against the app's 1.9.24 (comment at `:41-42`).
- **F-A9A-02 Versions.** All in `PlantLibrary_AndroidApp/gradle/libs.versions.toml`:
  - AGP 8.13.2 (`:2`), Kotlin 1.9.24 (`:3`), KSP 1.9.24-1.0.20 (`:4`)
  - Compose BOM 2024.06.00 (`:8`). The cached BOM POM resolves it to material3 1.2.1, compose-ui 1.6.8 and material-icons-extended 1.6.8.
  - navigation-compose 2.7.7 (`:9`), Hilt 2.51.1 (`:11`), Coil 2.6.0 (`:17`), CameraX 1.3.4 (`:18`), AppAuth 0.11.1 (`:19`)
  - Gradle 8.13 (`gradle/wrapper/gradle-wrapper.properties:3`)
  - Compose compiler extension 1.5.14 (`app/build.gradle.kts:51`); compileSdk/targetSdk 34, minSdk 29 (`:10-15`).
- **F-A9A-03 Zero test sources (GC-2006 confirmed by glob).** `find` for `*Test.kt`, `*Tests.kt`, `src/test` and `src/androidTest` under the 14 modules returns nothing. Every module has only `src/main` (listing). `PlantLibrary_AndroidApp/CLAUDE.md:25-28` says the same. The test dependencies are declared but have no sources (`app/build.gradle.kts:100-105`).
- **F-A9A-04 Entry and gate.** `PlantLibrary_AndroidApp/app/src/main/AndroidManifest.xml:34-42` declares the launcher `MainActivity`. `MainActivity.kt:15-17` wraps `PlantLibraryTheme { Surface { AppRoot() } }`. `AppRoot.kt:28-41` switches on a gate state: Loading spinner, `LoginScreen`, `GardenSelectionScreen`, `InitialSyncScreen`, then `PlantLibraryNavGraph()`. Three of the 15 views therefore sit outside the navigation graph.
- **F-A9A-05 Token transport is a hand mirror of the pre-1.2.0 palette.** `PlantLibrary_AndroidApp/core/design/src/main/java/com/plantlibrary/android/core/design/Color.kt:5-14` calls itself a "1:1 mirror" of `tokens.json`. A static value diff against `PlantLibrary_SharedContracts/design-tokens/tokens.json` gives 59 equal, 26 different and 49 missing:
  - **Different:** all 10 `PRIMARY` (`Color.kt:18-27`); `NEUTRAL` 50/100/300/500/600/800 (`:32-40`); `DARK.primary` and `DARK.primary_hover` (`:67-68`); 8 of 9 `HIGHLIGHT` (`:80-88`).
  - **Missing:** `NEUTRAL.150/350`; 7 new `DARK` keys; `CHART.series_1..4`; all 28 `SEMANTIC_DARK` and 8 `CHART_DARK` values.
  - **Equal:** `SEMANTIC` (light, 28 values), `EXTRA`, the 10 legacy `CHART` keys, 9 of 11 `DARK` keys and 6 of 12 `NEUTRAL`.
  - Nothing pins a version: no `CONSUMED_*` file exists apart from `hygiene/CONSUMED_HYGIENE.md`, and `tokens.json` has no version field. The only `1.2.0` stamp is `semantic-roles.json:5`.
- **F-A9A-06 Banned greens are live in the rendered theme.**
  - `Theme.kt:14` binds light `primary` to `Primary.c600` = `#16A34A` (`Color.kt:24`). Every filled `Button` label sits on it, at 3.30:1 per `04_APPROVED…:47`. The static screenshot `implementation/MVP/evidence/validation_screenshots_2026-07-10_an_b12/03_current.png` shows the green filled buttons.
  - `Theme.kt:38` binds dark `primary` to `#4ADE80` (`Color.kt:67`). `Highlight.focusRing` is `#22C55E` (`Color.kt:83`) but nothing uses it.
- **F-A9A-07 MaterialTheme setup is partial.**
  - `PlantLibrary_AndroidApp/core/design/src/main/java/com/plantlibrary/android/core/design/Theme.kt:13-31` (light) and `:37-55` (dark) set 17 roles each. Unset roles take the Material baseline. The static screenshot above shows a lavender NavigationBar selected indicator, which is consistent with the baseline `secondaryContainer`.
  - `secondary` is bound to chart blue `Chart.secondary` (`Theme.kt:18,42`).
  - Light `background` = `Neutral.c50` (`:20`), but canon `semantic-roles.json` LIGHT `app_bg` = `#F5F7F2` (NEUTRAL.100).
  - Dark `onPrimary` = `Neutral.c950` (`:39`), not `DARK.on_accent`. Dark `errorContainer` = light-group `Semantic.error.text` (`:53`), not `SEMANTIC_DARK.error.light`.
  - Typography maps 12 M3 roles from `TYPE_SCALE` 1:1 (`Type.kt:48-61`). `TYPE_SCALE` values equal the canon. Shapes map `RADIUS` (`Shape.kt:24-30`); `nav` is missing and `pillInput` is defined (`:15`) but has no call site.
- **F-A9A-08 Feature screens never touch the custom token objects.**
  - `grep PlantLibraryToken` over `feature/` and `app/` returns 0. Only `core/design/EmptyState.kt:27-28` uses `PlantLibraryTokenSpace`.
  - `MaterialTheme.typography.*` appears 87 times in feature screens (`bodyMedium` 30, `bodySmall` 25, `titleMedium` 11, `bodyLarge` 10, `titleSmall` 5, `headlineSmall` 5, `labelMedium` 1).
  - `MaterialTheme.colorScheme.*` appears 4 times, all `.error`: `GardenSelectionScreen.kt:53,70`, `LoginScreen.kt:80`, `SettingsScreen.kt:70`.
  - `Highlight`, `Extra`, `Chart` (apart from M3 `secondary`), `PlantLibraryTokenType` and `PlantLibraryTokenButtonSizes` are unused. No `PlantButton` exists, though `Spacing.kt:25` expects one.
- **F-A9A-09 Literals outside the theme.** 0 `Color(0x…)`, 0 hex strings, 0 `RoundedCornerShape`, 0 elevation, 0 `FontFamily`, 0 `.sp` in `app/` and `feature/`. There are 82 `N.dp` literals:
  - values: 16dp ×29, 12dp ×20, 8dp ×16, 4dp ×10, 24dp ×5, 20dp ×1, 2dp ×1. Every value is a `SPACE` step.
  - top files: `feature/addplant/.../AddPlantScreen.kt` 16, `feature/plants/.../PlantDetailScreen.kt` 16, `feature/home/.../HomeScreen.kt` 9.
  - resources: two hex literals in launcher drawables, `app/src/main/res/drawable/ic_launcher_background.xml:8` (`#1B5E20`) and `ic_launcher_foreground.xml:8` (`#A5D6A7`), neither of them canon. There is no `colors.xml`.
- **F-A9A-10 Launch theme and dark mode.** `PlantLibrary_AndroidApp/app/src/main/res/values/themes.xml:8` parents `android:Theme.Material.Light.NoActionBar`. There is no night variant, so the window background before the first Compose frame is light in dark mode (a runtime check, §7.6.3). `PlantLibraryTheme` follows `isSystemInDarkTheme()` only (`Theme.kt:59`). There is no in-app theme preference, although `PlantLibrary_SharedContracts/page-contracts/android/MobilePageContract_more.md:22` asks for "Adjust appearance/theme". None of the 198 PNG screenshots under `implementation/` is named as a dark capture (listing).
- **F-A9A-11 Icons.**
  - `PlantLibrary_AndroidApp/app/build.gradle.kts:86` pulls `material-icons-extended`. `PlantLibraryNavGraph.kt:4-10,48-52,89` uses `Icons.Filled.*` and `Icons.AutoMirrored.Filled.*`: 7 icons in all, all in the shell.
  - That is the legacy Material Icons set, not Material Symbols, which was the SDA-DEC-04 recommendation (`PlantLibrary_Workspace/implementation/System_Design_Architecture/STATE.md:150`).
  - The approved mockup draws its own stroke icons. Feature screens use no icons at all.
- **F-A9A-12 Fonts.** `PlantLibrary_AndroidApp/core/design/src/main/java/com/plantlibrary/android/core/design/Type.kt:16` uses `FontFamily.Default` (Roboto/system), with the rationale at `:9-15`. This matches `TOKEN_USAGE_NOTES.md:79-80` and the SDA-DEC-05 recommendation. No font resource exists.
- **F-A9A-13 Conduct rules visible statically.**
  - Scientific names are never italic. `PlantDisplayNames.kt:9-17` falls back to `scientific_name` inside a single plain label, rendered at `PlantsScreen.kt:111`, `HomeScreen.kt:141` and `AddPlantScreen.kt:142`. There are 0 `FontStyle`/`italic` occurrences in `feature/`.
  - Status is text-plus-colour on Home (`HomeScreen.kt` alert card, verified in the screenshot).
  - 88 user-facing `Text("…")` literals sit in Kotlin; `strings.xml` holds only `app_name` (`app/src/main/res/values/strings.xml:3`).
  - Content descriptions: 2 literal ones plus the 5 nav labels.
- **F-A9A-14 Navigation graph vs contracts vs mockup.**
  - `PlantLibraryNavGraph.kt:117-176` registers 12 destinations plus the nested `add_plant_flow` (`:136`). `docs/navigation_plan.md:22` is stale: it says 10 destinations and "Conflict Detail / Settings remain placeholders".
  - Contract routes differ: `MobilePageContract_plants.md:5` (`plantDetail/{profileId}`), `:25` (`camera/{plantId}`), `MobilePageContract_add.md:5` (`addPlant`) and `MobilePageContract_more.md:5` (`settings`) against `Routes.kt:13,17,20,27`.
  - Bottom-nav order in code is Home, Plants, Tasks, Add, More (`PlantLibraryNavGraph.kt:47-53`). The approved mockup's Android phones show Home, Plants, Add, Tasks, More.
  - Pushed routes highlight no tab (`PlantLibraryNavGraph.kt:102`). This is already named by `AN-V1-SHELL-01` (`TASK_CHECKLIST.md:27`).
- **F-A9A-15 Design rows are open and partly contradictory.** `PlantLibrary_AndroidApp/implementation/System_V1_Implementation/TASK_CHECKLIST.md`:
  - `AN-V1-DS-05` `todo` (`:52`); `-DS-02/03/04` `todo` (`:49-51`); `-DS-01` `gated` on SDA-B02 (`:48`); `-DS-06` `done` (`:57`).
  - DS-03's skill files are already present since `f29f578` (2026-07-10). What remains of the row is the CLAUDE.md gating section, `.impeccable/design.json` and PRODUCT/DESIGN. `PlantLibrary_AndroidApp/CLAUDE.md:38` confirms `DESIGN.md`/`PRODUCT.md` do not exist.
  - DS-05's done-when (`:52`, `TASK_CONTEXT.md:283-284`) requires "no pre-1.2.0 greens remain" and also wants `Chart.series1..4` mirrored (`TASK_CONTEXT.md:277-279`). `CHART.series_1` and `CHART.primary` are `#16A34A` in the canon (`tokens.json:157,161`). The done-when cannot be met as written. This is the same canon contradiction as Dashboard Q-A9D-02.
- **F-A9A-16 The drift script under-reports.**
  - `PlantLibrary_AndroidApp/scripts/check_token_drift.py:175-186` compares only Primary, Neutral, Dark and Semantic. HIGHLIGHT, CHART, EXTRA, `SEMANTIC_DARK`, `CHART_DARK` and `semantic-roles.json` are never read. Row DS-06 (`TASK_CHECKLIST.md:57`) names `semantic-roles.json`.
  - The banned grep covers `core/design` only (`:45`). It will keep flagging `Color.kt:92` (`Chart.primary` `#16A34A`, canon-correct), so its "exit 0 once DS-05 lands" promise (`:201`; `validation/AN1-B12_token_drift.md:48`) is unattainable.
  - Recorded output: 18 mismatches and 6 banned hits (`AN1-B12_token_drift.md:22`), against 26 value differences in the full diff.
- **F-A9A-17 Kit Compose emission: present, never proven, shape differs from this app.**
  - `C:/Programmierung/Design_Template_Kit/anchoring-kit/emitters/emit-stack.mjs:31` lists `compose`. `:247-305` writes one `Tokens.kt` in `package design.generated` (`:298`), containing `object Tokens { object Color; object Dimension; object Duration; object ZIndex }` plus `LightRoles`/`DarkRoles` objects.
  - Typography is emitted as size and line-height `sp` only. There is no weight, no `TextStyle`, no `Typography`, no `Shapes`, no `ColorScheme` and no button-size struct.
  - `find` over the Kit (excluding `node_modules`) finds no `.kt` file, so no compile evidence exists anywhere.
  - Inside `object Color`, the emitted `Color(0x…)` calls rely on Kotlin resolving to `androidx.compose.ui.graphics.Color` past the enclosing object's own name. That is a compile-only question (§7.6.3).
- **F-A9A-18 Kit static checks are blind to Kotlin.**
  - `C:/Programmierung/Design_Template_Kit/anchoring-kit/checks/check-literals.mjs:36` only matches hex with a leading `#`, so `Color(0xFF16A34A)` is invisible. `:40` requires the unit right after the digits, so `16.dp` is invisible. The tool reads `.kt` (`:43`) and finds nothing.
  - `check-banned-colors.mjs:21-23` matches `value` plus `aliases`. The field-ledger `banned-colors.json` BAN-01..03 have no `0xFF…` alias.
  - BAN-02 is already scoped to `color.primary/secondary/highlight` (`banned-colors.json:37-41`), which resolves the chart conflict inside the Kit.
- **F-A9A-19 impeccable here: right version, wrong scanner.**
  - `PlantLibrary_AndroidApp/.claude/skills/impeccable/SKILL.md:4` is 3.8.0, byte-identical to PyApp's `.claude` copy and to the Conductor's (`diff -rq` empty). `.agents/` and `.github/` carry 3.8.0 harness variants.
  - The detector scans only web extensions (`scripts/detector/node/file-system.mjs:14-18`). The visual contrast engine needs a browser page (`scripts/detector/engines/visual/screenshot-contrast.mjs`).
  - `SKILL.md:18` stops at `NO_PRODUCT_MD` until `PRODUCT.md` exists.
  - On this client, impeccable is a guided LLM critique over code and screenshots, never a mechanical gate.
- **F-A9A-20 SDA decisions are recorded as open.**
  - `PlantLibrary_Workspace/implementation/System_Design_Architecture/STATE.md:21-25` lists SDA-DEC-01..05 as `open`. `:139-141` says a runbook (G1/D5) accepted the five recommendations but did not record them in the package. `:150` lists the recommendations.
  - SDA-DEC-01's recommendation is "sibling SharedContracts folders", against a `design/` restructure. Q-G-01 (a) proposes `SharedContracts/design/`. The two need reconciling when B5 records the decision.
- **F-A9A-21 Capture tooling vs SDA-DEC-03.**
  - The superproject `android-validation` captures with `adb screencap` (`.claude/skills/android-validation/SKILL.md:120`), which is native per platform: it holds.
  - Its naming is `NN_<snake_case>.png` (`:209`), not `<page_id>__<platform>__<light|dark>.png`.
  - Grep for night, uimode or dark in the skill returns 0.
  - AndroidApp does not mirror the skill (`PlantLibrary_AndroidApp/CLAUDE.md:30-33`).
- **F-A9A-22 Settings surface for 06a.** DataStore-backed settings:
  - server URL (`core/network/.../ServerUrlStore.kt:32-36`)
  - OIDC issuer and client (`core/auth/.../OidcSetupStore.kt:33-39`)
  - active garden (`core/auth/.../ActiveGardenStore.kt:29-35`)
  - tokens (`AuthTokenStore.kt`)

  There is no appearance, reminder or notification preference. `AN-V1-CARE-04` (`TASK_CHECKLIST.md:40`) plans the reminder group.
- **F-A9A-23 Hygiene roots for B6.** `PlantLibrary_AndroidApp/hygiene/CONSUMED_HYGIENE.md:23-27` declares three roots, all under `implementation/System_V1_Implementation/`. A `design/` pin folder or a design-migration workspace needs a `D-…` entry first.

## §3 Candidates

| ID | Source path @ pin | What | Verdict | Target repo and path | Lane (B5, B6) | Q id or — |
|---|---|---|---|---|---|---|
| RC-A9A-01 | `PlantLibrary_AndroidApp/core/design/src/main/java/com/plantlibrary/android/core/design/{Theme,Type,Shape}.kt` @ 5d6410f | The M3 role-mapping layer (ColorScheme, Typography, Shapes). These are the bindings the Kit emitter does not produce | keep as the stack adapter; rebind its inputs to generated `Tokens`/`LightRoles`/`DarkRoles`; fix the role gaps of F-A9A-07 | AndroidApp, same paths | B5 (anchoring) · B6 (role fixes) | Q-A9A-01 |
| RC-A9A-02 | `PlantLibrary_AndroidApp/core/design/.../Color.kt`, `Spacing.kt` (token objects) @ 5d6410f | The hand mirror | retire once the generated `Tokens.kt` compiles; until then it is the value source DS-05 would edit | AndroidApp `core/design` | B5 | Q-A9A-02 |
| RC-A9A-03 | `PlantLibrary_AndroidApp/docs/compose_theme_plan.md` @ 5d6410f | Role-mapping rationale tables (Material3 role → token) | adapt into the Kit's `template/docs/STACK_MAPPING_TEMPLATE.md` shape as `design/stacks/compose/mapping.md` | AndroidApp `design/stacks/compose/mapping.md` (path after Q-A9A-01) | B5 | Q-A9A-01 |
| RC-A9A-04 | `PlantLibrary_AndroidApp/scripts/check_token_drift.py` @ 5d6410f | Compile-free drift and banned-literal check (Python, no Gradle) | keep until the Kit's `check-drift`/`check-literals` can read Kotlin; extend to all groups plus `semantic-roles.json`; scope the banned grep as BAN-02 does | AndroidApp `scripts/` | B5 | Q-A9D-02 (canon ban scope) |
| RC-A9A-05 | `PlantLibrary_AndroidApp/core/design/.../EmptyState.kt` @ 5d6410f | The only shared, token-consuming component (empty/error/offline) | keep; seed of the Compose component set | AndroidApp `core/design` | B6 | — |
| RC-A9A-06 | `Design_Template_Kit/anchoring-kit/emitters/emit-stack.mjs` (compose) @ f08e588 | Emits `Tokens.kt` | use as is for B5's first emission into the client's generated folder; record Kit findings (package name fixed to `design.generated`, no weights/`TextStyle`, no compile proof), do not patch (G-08) | Kit finding → `REGISTER_conductor-reuse-candidates` | B5 (A4 owns the emitter verdict) | Q-A9A-01 |
| RC-A9A-07 | `Design_Template_Kit/anchoring-kit/checks/check-literals.mjs`, `check-banned-colors.mjs` @ f08e588 | Literal census and ban scan | Kit finding: Kotlin `Color(0xAARRGGBB)` and `N.dp` patterns missing. Until fixed, the Android literal census uses the grep adapter of §7.3; ban aliases (`0xFF16A34A` …) can be added in the instance Configuration's `banned-colors.json` (Configuration data, not Kit code) | Kit finding; Configuration `banned-colors.json` aliases | B5 | Q-A9A-03 |
| RC-A9A-08 | Approved mockup artifact `claude.ai/code/artifact/370bf3f9-cb04-4d30-9917-9306db16d1b7` (version 1783680555-4a24), section "Mockups · 3 of 3 Android app (Compose)" | 4 phones (Today/Home, Add plant via server search, plant detail with quick log, Sync under More), light+dark | import as a static snapshot into the design-migration workspace's target reference (04 normalization); it is the SDA-B07 parity reference (`04_APPROVED…:86-87`) | AndroidApp design-migration workspace `target_reference/` | B6 | Q-A9A-06 |
| RC-A9A-09 | `PlantLibrary_SharedContracts/page-contracts/android/*.md` @ d43f7a2 | 5 mobile contracts + exclusions | seed for stage 02 screen contracts; routes stale (F-A9A-14) | AndroidApp workspace `screen_requirements/` (contracts amended in SharedContracts after IA) | B6 | Q-A9A-05 |
| RC-A9A-10 | `PlantLibrary_AndroidApp/implementation/MVP/evidence/validation_screenshots_2026-07-10_an_b12/`, `…_an_b13/`, `…_2026-07-13_an_b13_conflict_fix/`, `implementation/System_V1_Implementation/validation/evidence/AN-V1-LOCAL-OIDC-01-20260715-01/` | Light-only screenshots and uiautomator XML dumps of every MVP screen. UI code has been unchanged since `a93f4c8` (2026-07-15; only `SettingsScreen.kt` +6 lines) | reference "before" set for the census, not a baseline (pre-1.2.0, light only, house naming). Phase C re-captures per SDA-DEC-03 | stays; cited from workspace `current_state/Screenshot_Fixture_Inventory.md` | B6 | — |
| RC-A9A-11 | Superproject `.claude/skills/android-validation/SKILL.md` @ 8702e0a | Native capture harness (adb screencap, uiautomator) | adapt in Phase C: add light/dark switching and `<page_id>__android__<theme>.png` naming per SDA-DEC-03 | superproject skill | C1 (deferred) | Q-A9A-04 |
| RC-A9A-12 | `PlantLibrary_AndroidApp/.claude/skills/impeccable/` (3.8.0) @ 5d6410f | Design skill, identical to PyApp and Conductor | keep; finish DS-02/03 (PRODUCT.md, DESIGN.md, `.impeccable/design.json`, CLAUDE.md gating); treat as critique only (F-A9A-19) | AndroidApp root | B5 | — |
| RC-A9A-13 | `PlantLibrary_AndroidApp/app/src/main/java/com/plantlibrary/android/navigation/PlantLibraryNavGraph.kt` @ 5d6410f | Single shared `Scaffold`/`TopAppBar`/`NavigationBar` with the destination-title map | keep as the shell seed for `AN-V1-SHELL-01`; selection fix and nav order are B6 IA items | AndroidApp, same path | B6 | Q-A9A-05 |
| RC-A9A-14 | `Design_Template_Kit/examples/plantlibrary-field-ledger/design/banned-colors.json` @ f08e588 | Scoped BAN-02 (chart allowed) | adopt in the imported Configuration; amend DS-05 done-when wording (do not widen validation) | SharedContracts Configuration (per Q-G-01) | B5 | Q-A9D-02 |

## §4 Questions for the operator

| ID | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A9A-01 | Where the generated Compose token file lives and how `:core:design` consumes it | (a) Kit emits into `PlantLibrary_AndroidApp/design/stacks/compose/generated/Tokens.kt`, pinned by `PlantLibrary_AndroidApp/design/conformance/CONSUMED_DESIGN.md`; `core/design/build.gradle.kts` adds that folder as a Kotlin source dir; `Theme.kt`/`Type.kt`/`Shape.kt` stay as the hand-written stack adapter (M3 bindings, font weights); (b) copy the emitted file into `core/design/src/main/java/...`; (c) emit into `PlantLibrary_SharedContracts/generated/kotlin` and consume it like the network client (composite build) | (a) matches the Kit's generated-path exemption (`stacks/*/generated/`, `check-literals.mjs:29`) and Q-G-01 (a)'s per-client pin. It keeps one emitted source. The adapter is the only place the M3 bindings and weights can live, because the emitter does not produce them. (c) ties token emission to the client-generation wave and its stdlib skew (F-A9A-01) | B5 Android anchoring; B6 Android implementation |
| Q-A9A-02 | Fate of `AN-V1-DS-05` (hand-edit the mirror to 1.2.0) now that B5 brings a generated artifact | (a) do not hand-edit; record in the package `STATE.md` that DS-05 and DS-01 are superseded by the design-migration gap rows; point their validation cells at the deferred register; if the Compose emitter cannot be compile-proven before B6 starts, fall back to (b); (b) run DS-05 as a value-only hand edit first (fast WCAG fix of `primary`), then switch to the generated file; (c) keep both rows as written | Transcribing 75 values by hand and then replacing them is double work. The hand mirror is exactly what drifted (F-A9A-05). The fallback keeps the WCAG fix from waiting indefinitely on Q-G-04/Q-G-08 | B5; B6 Android; package `STATE.md` decision |
| Q-A9A-03 | How the Android raw-literal census and ban scan run until the Kit reads Kotlin | (a) record Kit findings (Kotlin patterns, ARGB aliases) for a separate Kit session; meanwhile add `0xFF…` aliases to the instance Configuration's `banned-colors.json` and run the §7.3 grep adapter as the census; (b) extend `scripts/check_token_drift.py` into a full Kotlin literal check in AndroidApp; (c) accept no literal gate for Android | (a) respects G-08 (no Kit patching from TARGET). Aliases are Configuration data. The grep adapter is reproducible today. (b) builds a second checker the Kit would later replace | B5 Android checks; B6 mechanical gate |
| Q-A9A-04 | Record the five SDA decisions, and how Android meets SDA-DEC-03/-04 | (a) B5 records SDA-DEC-01..05 in `System_Design_Architecture/STATE.md` as accepted at G1/D5, with Android notes: DEC-03 capture via `android-validation` extended for dark and the `<page_id>__android__<theme>.png` naming in Phase C; DEC-04 Material Symbols imported as vector drawables for the 7 shell icons in B6, `material-icons-extended` removed after; DEC-05 `FontFamily.Default` confirmed; (b) record DEC-04 as an accepted Android deviation (keep Material Icons) | The table says `open` while a runbook accepted them (F-A9A-20). The icon set is 7 icons in one file, so (a)'s DEC-04 cost is small, and it removes a 1.6.8 artifact bound to the BOM. DEC-01's "siblings" recommendation must be reconciled with Q-G-01 (a) in the same entry | B5 (SDA record); B6 icon change; C1 capture |
| Q-A9A-05 | Route names, nav order and bottom-nav selection against contracts and mockup | (a) leave code and contracts as they are; the 06b IA decides tab order (code: Tasks before Add; mockup: Add before Tasks) and route names; amend the contracts after IA approval; (b) adopt the mockup order and contract route names now | P-DS-10 keeps the contracts until the IA (the same reasoning as Q-A9D-06). Changing either side twice is waste | B6 IA (06b) for Android |
| Q-A9A-06 | Where the Android design-migration workspace and the `design/` pin live | (a) a new package root `PlantLibrary_AndroidApp/implementation/Design_Migration_V1/` (the pilot's shape) plus `PlantLibrary_AndroidApp/design/` for the conformance pin, each declared by a `D-…` entry in `hygiene/HYGIENE_DECISIONS.md`; (b) a planning file inside `System_V1_Implementation/planning/` and no separate package | Methodology 4.1.0 needs a workspace with `current_state/`, `screen_requirements/` and `validation/`. Only `System_V1_Implementation/{planning,proposal,handovers}` are declared roots (F-A9A-23) | B6 bootstrap for Android |
| Q-A9A-07 | Brief class for Android: restructure or re-skin | (a) restructure: 01a, 06a, 06b run. V1 rows add screens and sections (offline inbox `AN-V1-ADD-04`, rejected-outbox `-SYNC-01`, reminders and settings `-CARE-04`, add wizard `-ADD-01`), and the census finds 4 tier-1 gaps (§7.6.2); (b) re-skin only (token and role adoption, structure untouched) | A re-skin would freeze today's 15-view structure, which the V1 plan already changes | B6 Android stage order |

## §5 Reusable things this brief did not name

- `PlantLibrary_AndroidApp/core/design/src/main/java/com/plantlibrary/android/core/design/Spacing.kt:25-39` holds a ready `BUTTON_SIZES` data class (`PlantLibraryButtonSize`). It is the natural input for the missing `PlantButton`, and maps onto Kit `size.button.*`.
- The uiautomator XML dumps next to the MVP screenshots (`implementation/MVP/evidence/window_*.xml`, `validation_screenshots_2026-07-10_an_b12/*.xml`, `…_an_b13/*.xml`) can serve as a view-inventory cross-check for census pass B without a running device: resource ids and text per screen.
- The Gradle user cache holds the resolved BOM POM (`~/.gradle/caches/modules-2/files-2.1/androidx.compose/compose-bom/2024.06.00/*.pom`). Reading it statically gives exact library versions without Gradle. `core/design/build/intermediates/**/debug-artifact-dependencies.xml` confirms material3 1.2.1 from an earlier build.
- `PlantLibrary_AndroidApp/feature/sync/build.gradle.kts:39` depends on `:core:design` but no file in `feature/sync` imports it. Coil is declared in `feature/plants/build.gradle.kts:50` but unused there: there are no list thumbnails. These are inputs for `AN-V1-PLANTS-01`.
- `PlantLibrary_SharedContracts/design-tokens/platform-mapping-android.md:5` already specifies the expected generated module (`generated/kotlin/...Tokens.kt`, `Tokens.Space.s4`, `Tokens.Radius.md`). Its naming differs from both the app (`PlantLibraryTokenSpace.s4`) and the Kit (`Tokens.Dimension.Space4`). It needs a one-line amendment once Q-A9A-01 is answered.

## §6 Claims to verify

1. **The banned greens are present at exactly six lines of the hand mirror.**
   - Check: `grep -n "0xFF16A34A\|0xFF22C55E\|0xFF4ADE80" C:/Programmierung/SW_Development/PlantLibrary_AndroidApp/core/design/src/main/java/com/plantlibrary/android/core/design/Color.kt`
   - Expect: lines 22, 23, 24, 67, 83, 92.
2. **No feature or app file references the custom token objects.**
   - Check: `grep -rln "PlantLibraryToken" C:/Programmierung/SW_Development/PlantLibrary_AndroidApp/feature C:/Programmierung/SW_Development/PlantLibrary_AndroidApp/app --include=*.kt`
   - Expect: no output.
3. **The Kit's literal regexes cannot see Compose literals.**
   - Check: `sed -n 36,40p C:/Programmierung/Design_Template_Kit/anchoring-kit/checks/check-literals.mjs`
   - Expect: `HEX_COLOR` requires a literal `#`, and `DIMENSION_RE` requires the unit immediately after the digits. `0xFF2A7A30` and `16.dp` therefore match neither.

## §7 Brief sections

### §7.1 UI source inventory

**Module and package tree.** Kotlin under `src/main/java`; root package `com.plantlibrary.android`. Counts are `.kt` files / lines.

| Module (`settings.gradle.kts` line) | Package | Files / lines | Screens | ViewModels | Role |
|---|---|---|---|---|---|
| `:app` (31) | `com.plantlibrary.android`, `.navigation` | 6 / 415 | 0 | 1 (`AppRootViewModel`) | `MainActivity`, `PlantLibraryApplication`, `AppRoot` gate, `Routes`, `PlantLibraryNavGraph` |
| `:core:design` (34) | `…core.design` | 6 / 339 | — | — | `Color.kt` 103, `Theme.kt` 70, `Type.kt` 61, `Spacing.kt` 39, `EmptyState.kt` 36, `Shape.kt` 30 |
| `:feature:home` (40) | `…feature.home` | 2 / 274 | 1 | 1 | Home |
| `:feature:plants` (41) | `…feature.plants` | 4 / 560 | 2 | 2 | Plants list, Plant detail (4 tabs) |
| `:feature:tasks` (42) | `…feature.tasks` | 2 / 163 | 1 | 1 | Tasks |
| `:feature:addplant` (43) | `…feature.addplant` | 4 / 515 | 3 | 1 (shared, graph-scoped) | Add, Camera, Photo review |
| `:feature:sync` (44) | `…feature.sync` | 6 / 405 | 3 | 3 | Conflict list, Conflict detail, Sync diagnostics |
| `:feature:auth` (45) | `…feature.auth` | 5 / 475 | 3 | 2 | Login, Garden selection, Initial sync |
| `:feature:more` (46) | `…feature.more` | 4 / 410 | 2 | 2 | More, Settings |
| non-UI: `:core:common` 2/65, `:core:data` 26/1,463, `:core:network` 4/233, `:core:auth` 8/457, `:core:sync` 11/969 | | | | | data, sync, auth, network |

The project has no `ui/`, `screens/` or `components/` packages: screens sit flat in each feature package. The only shared component is `core/design/EmptyState.kt`, and the theme lives in `core/design`.

**Resources.** All under `app/src/main/res/`:

| File | Content |
|---|---|
| `values/themes.xml` | 9 lines; parent `android:Theme.Material.Light.NoActionBar` |
| `values/strings.xml` | `app_name` only |
| `drawable/ic_launcher_{background,foreground}.xml` | 2 hex literals |
| `mipmap-anydpi-v26/ic_launcher{,_round}.xml` | adaptive icon |
| `xml/network_security_config.xml` | network security config |

No other module has a `res/` folder.

**Versions.** See F-A9A-02. Compose is enabled per module (`buildFeatures.compose`, `composeOptions.kotlinCompilerExtensionVersion = "1.5.14"`), Java/JVM target 17.

**Entry Activity.** `app/src/main/AndroidManifest.xml:34-42` → `MainActivity` (`@AndroidEntryPoint`, `MainActivity.kt:10`) → `PlantLibraryTheme { Surface { AppRoot() } }` (`:15-17`).

**Navigation graph.** `AppRoot.kt:28-41` gates first. The `NavHost` is at `PlantLibraryNavGraph.kt:117-176`, start `home`.

| Route (`Routes.kt` line) | Kind | Composable (file) |
|---|---|---|
| gate `Loading` (`AppRoot.kt:28`) | gate | inline `CircularProgressIndicator` |
| gate `LoggedOut` (`AppRoot.kt:31`) | gate | `LoginScreen` (`feature/auth/.../LoginScreen.kt`) |
| gate `GardenRequired` (`AppRoot.kt:32`) | gate | `GardenSelectionScreen` (`feature/auth/.../GardenSelectionScreen.kt`) |
| gate `InitialSync` (`AppRoot.kt:36`) | gate | `InitialSyncScreen` (`feature/auth/.../InitialSyncScreen.kt`) |
| `home` (10) | bottom nav, start | `HomeScreen` (`feature/home/.../HomeScreen.kt`) |
| `plants` (11) | bottom nav | `PlantsScreen` (`feature/plants/.../PlantsScreen.kt`) |
| `tasks` (12) | bottom nav | `TasksScreen` (`feature/tasks/.../TasksScreen.kt`) |
| `add_plant_flow` (26) → `add` (13) | bottom nav, nested graph | `AddPlantScreen` (`feature/addplant/.../AddPlantScreen.kt`) |
| `add_plant_flow` → `camera` (27) | pushed | `CameraCaptureScreen` (`feature/addplant/.../CameraCaptureScreen.kt`) |
| `add_plant_flow` → `photo_review` (28) | pushed | `PhotoReviewScreen` (`feature/addplant/.../PhotoReviewScreen.kt`) |
| `more` (14) | bottom nav | `MoreScreen` (`feature/more/.../MoreScreen.kt`) |
| `plant_detail/{plantSyncId}` (17) | pushed | `PlantDetailScreen` (`feature/plants/.../PlantDetailScreen.kt`); tabs Overview, Care, Garden / Tasks, Notes (`:43`) |
| `conflicts` (18) | pushed | `ConflictListScreen` (`feature/sync/.../ConflictListScreen.kt`) |
| `conflict_detail/{conflictSyncId}` (19) | pushed | `ConflictDetailScreen` (`feature/sync/.../ConflictDetailScreen.kt`) |
| `settings_account` (20) | pushed | `SettingsScreen` (`feature/more/.../SettingsScreen.kt`) |
| `sync_diagnostics` (21) | pushed | `SyncDiagnosticsScreen` (`feature/sync/.../SyncDiagnosticsScreen.kt`) |

**Test folders (listing only).** None. No `src/test`, no `src/androidTest` and no `*Test.kt` in any of the 14 modules (F-A9A-03). Rows `AN-V1-TEST-01..03` (`TASK_CHECKLIST.md:59-60,62`) plan them.

### §7.2 Token consumption

**Transport.** A hand-written Kotlin mirror, with no generated file, copied JSON or colour XML:

| File | Content | Lines |
|---|---|---|
| `core/design/.../Color.kt` | `PlantLibraryTokenColors` (Primary, Neutral, Semantic, Dark, Extra, Highlight, Chart), 85 `Color(0xFF…)` literals | `:15-103` |
| `Spacing.kt` | `PlantLibraryTokenSpace`, `PlantLibraryTokenButtonSizes` | — |
| `Shape.kt` | `PlantLibraryTokenRadius`, `PlantLibraryShapes` | — |
| `Type.kt` | `PlantLibraryTokenType`, `PlantLibraryTypography` | — |

The mirror carries no version and no pin. It is the pre-1.2.0 palette, so 1.1.0 by content. Rationale: `docs/compose_theme_plan.md:5-15`.

**Static diff against the canon** (`SharedContracts/design-tokens/tokens.json` @ d43f7a2):

| Group | Equal | Different | Missing in Android |
|---|---|---|---|
| PRIMARY (10) | 0 | 10 | 0 |
| NEUTRAL (14) | 6 | 6 | 2 (150, 350) |
| SEMANTIC (28) | 28 | 0 | 0 |
| SEMANTIC_DARK (28) | 0 | 0 | 28 |
| DARK (18) | 9 | 2 | 7 (`surface4`, `text_body`, `primary_active`, `on_accent`, `accent_soft`, `accent_border`, `focus_ring`) |
| EXTRA (5) | 5 | 0 | 0 |
| HIGHLIGHT (9) | 1 (`search`) | 8 | 0 |
| CHART (14) | 10 | 0 | 4 (`series_1..4`) |
| CHART_DARK (8) | 0 | 0 | 8 |
| RADIUS (8) | 7 | 0 | 1 (`nav`) |
| SPACE (15), TYPE_SCALE (14), BUTTON_SIZES (4) | all | 0 | 0 |
| SHELL_SIZES, FONT_FAMILY, MONO_FONT_FAMILY | — | — | intentionally unmapped (`docs/compose_theme_plan.md:15`) |
| `semantic-roles.json` LIGHT/DARK | — | — | not consumed at all |

Colour totals: 59 equal, 26 different, 49 missing.

**MaterialTheme setup.** `Theme.kt:57-70`:

- `PlantLibraryTheme(darkTheme = isSystemInDarkTheme())`.
- The light scheme (`:13-31`) and the dark scheme (`:37-55`) set 17 roles each from the primitives; role gaps per F-A9A-07.
- `typography = PlantLibraryTypography` (12 M3 roles, `Type.kt:48-61`).
- `shapes = PlantLibraryShapes` (5 roles, `Shape.kt:24-30`).
- There is no `CompositionLocal` for extended tokens (state containers, chart, highlight). Features can reach those only through the raw `PlantLibraryTokenColors` object, and none does.

**Composable files that reference theme tokens.** Counts per file: `MaterialTheme.colorScheme.*` / `MaterialTheme.typography.*` / `MaterialTheme.shapes.*` / `PlantLibraryToken*`.

| File | colorScheme | typography | shapes | custom token objects |
|---|---|---|---|---|
| `feature/addplant/.../AddPlantScreen.kt` | 0 | 8 | 0 | 0 |
| `feature/addplant/.../CameraCaptureScreen.kt` | 0 | 1 | 0 | 0 |
| `feature/addplant/.../PhotoReviewScreen.kt` | 0 | 1 | 0 | 0 |
| `feature/auth/.../GardenSelectionScreen.kt` | 2 | 6 | 0 | 0 |
| `feature/auth/.../InitialSyncScreen.kt` | 0 | 4 | 0 | 0 |
| `feature/auth/.../LoginScreen.kt` | 1 | 3 | 0 | 0 |
| `feature/home/.../HomeScreen.kt` | 0 | 7 | 0 | 0 |
| `feature/more/.../MoreScreen.kt` | 0 | 2 | 0 | 0 |
| `feature/more/.../SettingsScreen.kt` | 1 | 9 | 0 | 0 |
| `feature/plants/.../PlantDetailScreen.kt` | 0 | 16 | 0 | 0 |
| `feature/plants/.../PlantsScreen.kt` | 0 | 3 | 0 | 0 |
| `feature/sync/.../ConflictDetailScreen.kt` | 0 | 7 | 0 | 0 |
| `feature/sync/.../ConflictListScreen.kt` | 0 | 3 | 0 | 0 |
| `feature/sync/.../SyncDiagnosticsScreen.kt` | 0 | 12 | 0 | 0 |
| `feature/tasks/.../TasksScreen.kt` | 0 | 5 | 0 | 0 |
| `core/design/.../EmptyState.kt` | 0 | 2 | 0 | 2 (`PlantLibraryTokenSpace`) |
| `app/.../MainActivity.kt` | 0 | 0 | 0 | `PlantLibraryTheme` ×1 call |
| `app/.../navigation/PlantLibraryNavGraph.kt`, `AppRoot.kt` | 0 | 0 | 0 | 0 (M3 defaults only) |

Material3 components imported by feature, app and design files: `Text` 17, `Button` 12, `OutlinedButton` 9, `Card` 8, `OutlinedTextField` 6, `CircularProgressIndicator` 4, `TextButton` 3, `Divider` 2, and one each of `Scaffold`, `TopAppBar`, `NavigationBar`, `NavigationBarItem`, `TabRow`, `Tab`, `FilterChip`, `RadioButton`, `IconButton`, `Icon`, `Surface`. All of these take colour and shape from M3 component defaults, so the role gaps of F-A9A-07 decide what they render.

### §7.3 Literals that remain

**Excluded as generated or vendor:** every `build/`, `.gradle/`, `.idea/`, and `PlantLibrary_SharedContracts/generated/kotlin` (composite build). `core/design` token definitions are counted separately: they are the token layer.

| Measurement | `app/` + `feature/` | `core/design/` (token layer) | Resources |
|---|---|---|---|
| `Color(0x…)` | 0 | 85 (`Color.kt`) | — |
| hex strings | 0 | 0 | 2 (`drawable/ic_launcher_background.xml:8` `#1B5E20`, `ic_launcher_foreground.xml:8` `#A5D6A7`) |
| `N.dp` | 82 in 15 files | 38 (`Spacing.kt` 31, `Shape.kt` 7) | launcher vector sizes only |
| `N.sp` | 0 | 4 in `Spacing.kt` (button font sizes) + `Type.kt` via `size.sp` (14 styles) | — |
| `FontFamily` | 0 | 1 (`Type.kt:16` `FontFamily.Default`) | no `res/font` |
| `RoundedCornerShape(` | 0 | 5 (`Shape.kt:25-29`) | — |
| elevation / shadow | 0 | 0 | — |
| `colors.xml` | — | — | absent |
| `themes.xml` | — | — | 1 style, no colour items (`themes.xml:8`) |
| drawable tints | — | — | none (`android:tint` 0) |

Top offenders for `N.dp`: 41 of 82 sit in three files.

| File | `N.dp` | Example lines |
|---|---|---|
| `PlantLibrary_AndroidApp/feature/addplant/src/main/java/com/plantlibrary/android/feature/addplant/AddPlantScreen.kt` | 16 | `:45` `padding(16.dp)`, `:113` `Divider(… vertical = 16.dp)`, `:140` `padding(12.dp)` … `spacedBy(8.dp)` |
| `PlantLibrary_AndroidApp/feature/plants/src/main/java/com/plantlibrary/android/feature/plants/PlantDetailScreen.kt` | 16 | `:46,52,86,116,170` `padding(16.dp)`, `:61` `horizontal = 16.dp, vertical = 8.dp` |
| `PlantLibrary_AndroidApp/feature/home/src/main/java/com/plantlibrary/android/feature/home/HomeScreen.kt` | 9 | `:42` `PaddingValues(16.dp)`, `:43` `spacedBy(12.dp)` |
| `…/feature/plants/.../PlantsScreen.kt` | 6 | |
| `…/feature/tasks/.../TasksScreen.kt` | 6 | |
| `…/feature/auth/.../GardenSelectionScreen.kt` | 5 | |
| `…/feature/sync/.../SyncDiagnosticsScreen.kt` | 5 | |
| `…/feature/sync/.../ConflictListScreen.kt` | 4 | |
| `…/feature/addplant/.../PhotoReviewScreen.kt` | 3 | |
| `…/feature/more/.../MoreScreen.kt` | 3 | |
| 5 other files | 1–2 each | |

Distinct values: 2, 4, 8, 12, 16, 20 and 24 dp. All are `SPACE` steps (`0_5`, `1`, `2`, `3`, `4`, `5`, `6`), so each literal has a 1:1 token replacement. `20.dp` is a size (`GardenSelectionScreen.kt:94`), not a spacing value.

**Grep adapter used** (re-runnable, compile-free; this replaces the Kit census for Kotlin until RC-A9A-07):

- colour: `Color\(0x|"#[0-9A-Fa-f]{6}|Color\.(Red|Green|…)`
- dimension: `[0-9]+(\.[0-9]+)?\.(dp|sp)`
- also `RoundedCornerShape|CircleShape|elevation|shadow\(|FontFamily`

Each runs over `find app feature -path '*/build' -prune -o -name '*.kt' -print`.

### §7.4 Screens

"Theme" in the last column means: does the screen consume theme tokens? Every screen takes colour, type and shape from `MaterialTheme`, so none is legacy for colour. Every screen is legacy for spacing (raw dp). The theme's own values are pre-1.2.0 (F-A9A-05), which makes every screen visually legacy until the theme is fixed.

| Screen (composable file) | Page contract | Mockup (approved artifact, Android section) | MVP / V1 screenshots (static) | Package rows that touch it | Theme |
|---|---|---|---|---|---|
| Login (`feature/auth/.../LoginScreen.kt`) | none (account handling is under More, `MobilePageContract_more.md:5`) | none | `MVP/evidence/validation_screenshots_2026-07-06/01-04`; `…_2026-07-07/*` (sign-in series); `…_2026-07-10_an_b13/01-09`; `System_V1_Implementation/validation/evidence/AN-V1-LOCAL-OIDC-01-20260715-01/01,05` | `AN-V1-LOCAL-OIDC-01` (done), `AN-V1-SEC-01`, `AN-V1-QA-01` | M3 type + `colorScheme.error`; dp literals |
| Garden selection (`…/GardenSelectionScreen.kt`) | none | none | `…_an_b13/10,11`; `…_2026-07-07/32-34,47-59`; OIDC `06` | `AN-V1-SETTINGS-01` (switcher), `-QA-01` | M3 type + `colorScheme.error` |
| Initial sync (`…/InitialSyncScreen.kt`) | none | none | not identifiable by name (possibly `…_an_b13/02_after_wait`) | `AN-V1-CARE-03` (offline invariants), `-QA-01` | M3 type |
| Home (`feature/home/.../HomeScreen.kt`) | `MobilePageContract_home.md` | phone 1 "Today" (reminders, inbox) | `…_an_b12/03_current`; `…_2026-07-09/23,24,45`; `…_2026-07-09_gap1_gap2/01,02`; `…_an_b11/05_home_sync_status`; `…_2026-07-13_an_b13_conflict_fix/04` | `AN-V1-SHELL-01`, `-HOME-01`, `-HOME-02`, `-ADD-04`, `-CARE-04`, `-DS-04`, `-QA-01` | M3 type; `EmptyState` (tokens) |
| Plants (`feature/plants/.../PlantsScreen.kt`) | `MobilePageContract_plants.md` | none (list) | `…_an_b12/04_plants`; `…_an_b13/12`; `…_2026-07-09/25`; `…_gap1_gap2/03` | `AN-V1-PLANTS-01`, `-SHELL-01`, `-QA-01` | M3 type; `EmptyState` |
| Plant detail (`…/PlantDetailScreen.kt`) | `MobilePageContract_plants.md` (`plantDetail/{profileId}`) | phone 3 (detail with quick log) | `…_an_b13/13,14,15`; `…_2026-07-09/29,30,31`; `…_gap1_gap2/04`; `…_2026-07-07/64,65` | `AN-V1-DETAIL-01`, `-DETAIL-02`, `-MEDIA-01`, `-CARE-02`, `-QA-01` | M3 type (16 refs) |
| Tasks (`feature/tasks/.../TasksScreen.kt`) | `MobilePageContract_tasks.md` | none | `…_an_b12/05_tasks`; `…_2026-07-09/26,27,28,34,44`; `…_2026-07-07/62` | `AN-V1-CARE-01`, `-CARE-04`, `-QA-01` | M3 type; `EmptyState` |
| Add (`feature/addplant/.../AddPlantScreen.kt`) | `MobilePageContract_add.md` (`addPlant`) | phone 2 (server search, 3 candidates) | `…_an_b12/06_add`; `…_an_b13/16,17,18,19`; `MVP/evidence/window_add_tab.xml`; `…_2026-07-07/70` | `AN-V1-ADD-01..04`, `-QA-01` | M3 type; `EmptyState` |
| Camera (`…/CameraCaptureScreen.kt`) | partial (`camera/{plantId}` in `MobilePageContract_plants.md:25`) | none | `…_an_b13/20`; `MVP/evidence/an-b10a_upload_camera.png` | `AN-V1-MEDIA-01` | M3 type |
| Photo review (`…/PhotoReviewScreen.kt`) | none | none | `…_an_b13/21,22`; `MVP/evidence/an-b10a_upload_review.png` | `AN-V1-MEDIA-01` | M3 type |
| More (`feature/more/.../MoreScreen.kt`) | `MobilePageContract_more.md` | phone 4 frames under the More tab | `…_an_b12/07_more`; `…_an_b11/01,08`; `…_2026-07-07/66` | `AN-V1-MORE-01`, `-MEDIA-02`, `-QA-01` | M3 type |
| Settings (`…/SettingsScreen.kt`) | `MobilePageContract_more.md` (`settings`) | none | `…_an_b12/08_settings`; `…_an_b11/09`; `…_2026-07-07/69`; OIDC `01,08` | `AN-V1-SETTINGS-01`, `-CARE-04`, `-SEC-01` | M3 type + `colorScheme.error` |
| Conflict list (`feature/sync/.../ConflictListScreen.kt`) | `MobilePageContract_more.md` (`conflicts`) | none | `…_an_b13/23`; `…_conflict_fix/03` | `AN-V1-SYNC-02` | M3 type |
| Conflict detail (`…/ConflictDetailScreen.kt`) | none of its own (under More's "resolve a conflict") | none | `…_an_b13/24,25`; `…_conflict_fix/01,02` | `AN-V1-SYNC-02` | M3 type |
| Sync diagnostics (`…/SyncDiagnosticsScreen.kt`) | none | phone 4 "Sync" | `…_an_b11/02,03,04`; `…_an_b12/09` | `AN-V1-SYNC-01`, `-SYNC-03`, `-MEDIA-02` | M3 type (12 refs) |

Coverage: 9 of 15 screens fall under one of the five contracts. 4 phones in the approved mockup map to Home, Add, Plant detail and Sync diagnostics/More, each in light and dark (`04_APPROVED…:86-87` counts 12 screens, 4 per client). No dark screenshot exists.

Rows touching all screens: `AN-V1-DS-01/05` (theme), `-DS-04` (audit over screenshots), `-QA-01` (accessibility and dark parity), `-SHELL-01` (scaffold). The walkthrough row is `AN-V1-ACC-01` (`verify-stack:walkthrough+android-validation:walkthrough`, `TASK_CHECKLIST.md:58`). No other `AN-V1-ACC-*` row exists.

### §7.5 The design-adoption gate's and impeccable's assumptions against this client

**`design-adoption`** (superproject `.claude/skills/design-adoption/SKILL.md`; it is not mirrored into AndroidApp, and row skill cells `design-adoption:android` name it).

| Assumption (line) | Holds? | Evidence |
|---|---|---|
| Fires on token-mirror files `Color.kt`, `Shape.kt` (`:23`) | holds | they exist at `core/design/...` |
| Canon paths `tokens.json`, `semantic-roles.json`, `TOKEN_USAGE_NOTES.md`, `platform-mapping-android.md`, `04_APPROVED…` (`:29-35`) | holds | all present at the cited paths |
| Android adoption row is `AN-V1-DS-05` in `AN1-B11` (`:60`) | holds | `TASK_CHECKLIST.md:52`, `BATCH_PLAN.md:169-178`; still `todo` |
| "Banned greens never anywhere" (`:71-74`) | contradicts canon | `tokens.json:157,161` keep `#16A34A` as chart green; Kit BAN-02 is scoped. Q-A9D-02 decides |
| "Regenerate where the suite generates" (`:82-83`) | n/a for Android | there is no generator (F-A9A-05) |
| Light accent `#2A7A30`, dark accent `#74BC85` with dark on-accent (`:72-74`) | does not hold in code | `Theme.kt:14,38-39` |
| "Dark surfaces need dark tokens" (`:75-76`) | does not hold | no `SEMANTIC_DARK` in the mirror; dark `errorContainer` uses a light-group value (`Theme.kt:53`) |
| Scientific names italic, status = text+colour (`:78-81`) | partly | italic: no (F-A9A-13); status text: yes on Home |
| Reintroduce no `pillInput` (`:90`) | holds by accident | defined (`Shape.kt:15`) but 0 call sites |
| P-DS-06 platform-native fonts | holds | `Type.kt:16` |
| P-DS-08 "32 px targets" | superseded on Android | Android floors at its own 48 dp minimum (`platform-mapping-android.md:14`, `MobilePageContract_home.md:39`). M3 `Button` defaults are 40 dp high plus a 48 dp touch target. Needs a runtime check (§7.6.3) |
| P-DS-10 bottom-nav phone-first, contracts unchanged | holds for anatomy | tab order differs from the mockup (F-A9A-14) |

Under Q-G-07 (a), these assumptions transfer to the Kit's `design-gate` reading the pinned Configuration. What this client needs from that gate: an Android pin, Kotlin-aware literal and ban checks (Q-A9A-03), and the SDA records (Q-A9A-04).

**SDA decisions.** All are recorded `open` (`STATE.md:21-25`); the recommendations are at `:150`.

| Decision | Recommendation | Holds on Android? |
|---|---|---|
| DEC-03 | native per-platform capture | holds in mechanism (`adb screencap`), not in naming or dark capture (F-A9A-21) |
| DEC-04 | Material Symbols | does not hold (F-A9A-11) |
| DEC-05 | Android system font | holds (F-A9A-12) |

**impeccable** (`PlantLibrary_AndroidApp/.claude/skills/impeccable/`, 3.8.0; gate rule in `TASK_CHECKLIST.md:10-15`: loads only for `impeccable:<command>` rows, i.e. only `AN-V1-DS-04`).

| What it assumes or checks | Holds? |
|---|---|
| `PRODUCT.md` (and `DESIGN.md`) at the project root, read by `scripts/context.mjs` (`SKILL.md:18`) | no: absent, so it stops at `NO_PRODUCT_MD` (DS-02 open) |
| "Read a project file (CSS / tokens / theme)" (`SKILL.md:20`) | holds: `core/design` |
| Mechanical anti-pattern detector over source | no: only web extensions (`file-system.mjs:14-18`) |
| Contrast check from screenshots | no: needs a browser page (`screenshot-contrast.mjs`) |
| `palette.mjs` brand seed for brand-new projects (`SKILL.md:22`) | must not fire: committed brand colours exist. The step-3 skip rule applies, but the committed values are the wrong (pre-1.2.0) ones, so a session must read the canon, not `Color.kt` |
| Activation gating section in `CLAUDE.md`, `.impeccable/design.json` | absent (DS-03 open) |
| Version parity with Conductor/PyApp | holds: byte-identical 3.8.0 |

### §7.6 Design-migration census shape (as far as a static scan can fill it)

#### 7.6.1 Mechanical design census (prompt 01, "Mechanical design census")

| Measurement | Value at 5d6410f | Note |
|---|---|---|
| Colour literals | 0 in UI code; 85 in the token layer; 2 in resources | 100 % of UI colour flows through `MaterialTheme` |
| Dimension literals | 82 `dp` in 15 UI files (50 % in 3 files); 0 `sp` | all on the SPACE grid, so 1:1 token replacement |
| Radii | 0 literal in UI; 5 shape roles (4, 6, 10, 12, 12 dp) in the token layer; M3 component defaults elsewhere (e.g. pill `Button`) | `RADIUS.nav` missing |
| Font families and sizes | 1 family (`FontFamily.Default`); 14 token styles; UI uses 7 typography roles | no ad-hoc sizes |
| Detector summary | not runnable: impeccable detector has no Kotlin support; Kit `check-literals` blind to Kotlin | §7.5, F-A9A-18 |
| Drift dry-run | `scripts/check_token_drift.py` (report-only, last recorded output 18 mismatches and 6 banned hits); full static diff 26 different and 49 missing; Kit `emit-stack --stacks compose` dry-run not performed (Phase A reads only) | F-A9A-16, -17 |

#### 7.6.2 Function / UI census (`FUNCTION_UI_CENSUS_TEMPLATE.md`), static draft

| Field | Value |
|---|---|
| Census date | 2026-10-13 |
| Repository | `PlantLibrary_AndroidApp` @ `5d6410f` |
| Configuration | none (no `design/CONSUMED_DESIGN.md`) |
| Stack adapter | Compose: repository/coordinator methods ↔ ViewModel/Screen calls; NavHost destinations plus the AppRoot gate |
| Status | DRAFT (lane A9 input; the B6 workspace owns the real census) |

**§0.2 Adapter.**

| Question | This stack's answer |
|---|---|
| Operations: where declared, how extracted | Non-private `fun` and `Flow` vals of `core/data/.../repository/*.kt`, `core/sync/.../{SyncCoordinator,ConflictResolutionCoordinator,SyncScheduler,MediaUploadCoordinator,GardenBootstrapRunner}.kt`, `core/auth/.../AuthRepository.kt`, `OidcSetupStore.kt`, `core/network/.../ServerUrlStore.kt`; regex `^\s*(suspend )?fun ` without `private` |
| UI calls: where, how extracted | `feature/**/*.kt` + `app/**/*.kt`; regex `\.<name>\(` or `::<name>` |
| Matcher | method name plus owning type (Kotlin calls are not path strings, so a segment-wise rule degenerates to name+receiver); overloaded names (`save` ×2) are counted per receiver |
| One view | a top-level `@Composable fun *Screen` registered in `PlantLibraryNavGraph`, or a gate branch in `AppRoot` |
| Navigation entry | a `bottomNavEntries` item (`PlantLibraryNavGraph.kt:47-53`); pushed routes are link-reached; gate views are state-reached |
| One subsystem | a Gradle module (`:core:*`), plus the WorkManager sync job |

A second adapter (the generated REST client) is recorded for completeness. Android is offline-first and most entity writes travel through `SyncApi.push`, so REST-level reach is not the primary measure.

**§1 Route inventory (repository layer).**

| Family | Operations | Reached by UI |
|---|---|---|
| Conflicts (`ConflictRepository`, `ConflictResolutionCoordinator`) | 4 | 3 |
| Enrichment | 3 | 3 |
| Field actions (tasks, events, notes) | 9 | 8 |
| Garden / user | 4 | 3 |
| Media (`MediaRepository`, `MediaUploadCoordinator`) | 10 | 6 |
| Catalog | 3 | 2 |
| Plant instances | 7 | 3 |
| Sync status / scheduling (`SyncStatusRepository`, `SyncScheduler`, `SyncCoordinator`) | 12 | 11 |
| Auth / setup (`AuthRepository`, `GardenBootstrapRunner`, `OidcSetupStore`, `ServerUrlStore`) | 9 | 8 |

**Totals: 61 operations, 47 reached, 14 unreached.** Of the 14:

- 8 are infrastructural (called only by coordinators or workers): `recordResolutionChoice`, `getPendingUploads`, `recordCapturedPhoto`, `replaceUploadIdentity`, `markUploadState`, `PlantInstanceRepository.getBySyncId`, `syncActiveGarden`, `observeMembershipsForUser`.
- 1 is dead: `AuthRepository.isLoggedIn`, which has no caller anywhere.
- 1 is reached by another path: `PlantInstanceRepository.search` is unused, but `PlantsViewModel.kt:89` filters in memory.
- 4 are §2 rows below.

The matched counts come from one grep pass. Each unreached name was hand-checked against `core/**` callers.

**REST client (secondary).** 40 generated operations in `PlantLibrary_SharedContracts/generated/kotlin/.../apis/*.kt`. 8 are called directly: `listMyGardens`, `getMe`, media `createUploadIntent` and `completeUpload`, sync `pull`, `push`, `listConflicts` and `resolveConflict`. The other 32 fall into four groups:

- plants, tasks, notes and events CRUD, reached semantically via sync push and pull;
- locations write, garden create, statistics and admin review, excluded by `page-contracts/android/EXCLUSIONS.md` or D-V1-07 (to be confirmed by the 06a filter);
- `getDownloadUrl`, `syncStatus` and client-device register/list, unreached;
- health and metrics, infrastructural.

**§2 Operations with no UI element (tier 1).** Candidates, high confidence: name match plus a hand check.

| ID | Operation | Handler | What is unreachable | Forward |
|---|---|---|---|---|
| CM-01 | `PlantInstanceRepository.setFavorite` | `core/data/.../repository/PlantInstanceRepository.kt:25` | marking a plant favourite (the contract's filter facet "favorite", `AN-V1-PLANTS-01`) | (06a) |
| CM-02 | `PlantInstanceRepository.updatePersonalNotes` | `…/PlantInstanceRepository.kt:26` | editing a plant's personal notes field | (06a) |
| CM-03 | `FieldActionsRepository.editNote` | `core/data/.../repository/FieldActionsRepository.kt:32` | editing an existing note (add only today; `AN-V1-CARE-02` names "notes add/edit") | (06a) |
| CM-04 | `PlantCatalogRepository.observeConfidence` | `core/data/.../repository/PlantCatalogRepository.kt:17` | seeing profile confidence (`AN-V1-DETAIL-01` "confidence display") | (06a) |

**§3 Subsystems with no dedicated surface (tier 2).** Medium confidence, to be hand-checked in B6.

| ID | Subsystem | Operation surface today | What has no UI | Reach | Forward |
|---|---|---|---|---|---|
| CM-05 | Enrichment jobs | trigger in Add (`AddPlantScreen.kt`), active count in More | job list, failure detail, retry | partial | (06a) |
| CM-06 | Media | capture, review, retry, failed list in diagnostics | gallery, thumbnails (Coil present, unused in lists), download URL | partial | (06a) |
| CM-07 | Background sync policy (WorkManager, `SyncScheduler`) | sync now, pending/rejected counts | schedule, constraints, cursor display (`AN-V1-SYNC-03`) | partial | (06a) |
| CM-08 | Notifications | none (no module) | reminders and digest (`AN-V1-CARE-04`) | none (planned capability, not an existing subsystem; may belong in 06a's "mandated surfaces that do not exist" instead) | (06a) |

**§4 View inventory.** 15 views (§7.1 table): 5 reached from the bottom nav, 7 link-reached pushed views, 3 gate views. None is unreachable.

- Link-reached detail or flow views (normal): plant detail, conflict detail, camera, photo review.
- Link-reached non-detail views: conflict list (from Home and More), settings (from More), sync diagnostics (from More and Settings).

**§5 Other operator surfaces.**

| Surface | Entry points | GUI representation |
|---|---|---|
| WorkManager periodic sync | `PlantLibrarySyncWorker`, scheduled in `PlantLibraryApplication` | partial (sync now, counts) |
| OIDC/server setup | Login screen fields, `SettingsScreen` server URL | yes |
| `adb reverse` local-stack wiring | `AN-V1-LOCAL-OIDC-01` | none (developer) |

**§6 Families.**

- tier 1: 4 (CM-01..04)
- tier 2: 4 (CM-05..08, CM-08 provisional)
- structure: 3 candidates:
  1. pushed routes select no tab (`PlantLibraryNavGraph.kt:102`);
  2. tab order differs from the approved mockup;
  3. contract routes differ (F-A9A-14).

**§7 Findings for the IA.**

1. Everything present serves field work on one garden. Everything absent concerns curation: favourites, notes edit, confidence, enrichment and media depth.
2. The two recovery exits, rejected-outbox and conflict resolution, are reachable only via More or a Home alert card.
3. There is no theme or appearance control, although the More contract asks for one.

#### 7.6.3 Not determinable statically → deferred-validation register (proposed rows)

| # | Item | Needs | Skill / owner | After |
|---|---|---|---|---|
| DV-A9A-a | The Kit-emitted `Tokens.kt` compiles inside `:core:design` (name resolution of `Color(…)` inside `object Color`, package `design.generated`) | Gradle compile (Q-G-04 (b) or Phase C) | `run-batch` standing leg (`assembleDebug`) | B5 Android emission |
| DV-A9A-b | Light and dark "current state" capture of all 15 views, named `<page_id>__android__<light\|dark>.png` | emulator | `android-validation:capture` (extended per RC-A9A-11) | B6 workspace bootstrap |
| DV-A9A-c | Visual comparison of Home, Add, Plant detail and Sync against the 4 approved phones, light and dark | emulator plus mockup snapshot | methodology 05 / `android-validation:capture` | B6 IA |
| DV-A9A-d | Dark-theme parity (SEMANTIC_DARK surfaces, no light creams on dark) | emulator, dark mode | `AN-V1-QA-01` | B6 implementation |
| DV-A9A-e | Rendered contrast of filled-button labels and focus indicators (today `#16A34A`; after: `#2A7A30`) | screenshots plus a contrast measurement (impeccable's engine needs a browser, F-A9A-19) | `AN-V1-QA-01` | B6 implementation |
| DV-A9A-f | Touch targets ≥ 48 dp, TalkBack traversal, font scaling | emulator | `AN-V1-QA-01` | B6 implementation |
| DV-A9A-g | Bottom-nav selected state on pushed routes | emulator walk | `AN-V1-SHELL-01` | B6 implementation |
| DV-A9A-h | Launch-window flash in dark mode (`themes.xml:8` light parent) | emulator, dark mode | `android-validation:capture` | B6 implementation |
| DV-A9A-i | Which M3 baseline roles actually render (lavender indicator, `surfaceTint` on elevated bars, Card container role in material3 1.2.1) | screenshots, light and dark | `android-validation:capture` | B6 census |
| DV-A9A-j | The Gradle lint task over all modules (lint is a Gradle task, excluded by Q-G-04 (a)) | Gradle | `run-batch` standing leg | B6 implementation |
| DV-A9A-k | `impeccable audit` and `critique` over fresh screenshots (`AN-V1-DS-04`) | screenshots from DV-A9A-b | `impeccable:audit` | DS-02/03 done |
| DV-A9A-l | Census pass B confirmation that every view renders with seeded data (gate views included) | emulator plus local stack | `android-validation:walkthrough`, `verify-stack` | B6 census |

### §7.7 Stack facts for the anchoring (lane B5)

**What the theme expects today.**

- Package `com.plantlibrary.android.core.design` (namespace `core/design/build.gradle.kts:7`).
- Objects:
  - `PlantLibraryTokenColors.{Primary.cNNN, Neutral.cNNN, Semantic.<state>.{main,light,border,text}, Dark.<camelKey>, Extra, Highlight, Chart}`
  - `PlantLibraryTokenSpace.sN`, `PlantLibraryTokenRadius.<key>`, `PlantLibraryTokenType.<key>` (`TextStyle`), `PlantLibraryTokenButtonSizes`
  - `PlantLibraryTypography`, `PlantLibraryShapes`, and the composable `PlantLibraryTheme`.
- Callers outside `core/design`: only `PlantLibraryTheme` (`MainActivity.kt:15`), `EmptyState` (4 feature files), and indirectly `MaterialTheme`. Renaming the token objects therefore touches one module only.

**What the Kit emits for `compose`** (`emit-stack.mjs:247-305`).

- One file `Tokens.kt`, `package design.generated`.
- `Tokens.Color.<PascalPath>`, e.g. `Primary600`, `NeutralN150`-style names from DTCG paths such as `color.primary.600`. Each is `Color(0xFFRRGGBB)`.
- `Tokens.Dimension.<PascalPath>` for `space`, `radius`, `size` as `.dp`, plus typography size and line-height as `.sp`.
- `Tokens.Duration`, `Tokens.ZIndex`.
- `LightRoles.<Role>` / `DarkRoles.<Role>` as `Color` (theme names `LIGHT`/`DARK` from the Configuration's `semantic-roles.json`).
- Imports `androidx.compose.ui.graphics.Color`, `.unit.dp`, `.unit.sp`.

**What a generated artifact must look like to fit this app.** Minimum, given Q-A9A-01 (a):

1. `Tokens.kt` as emitted, placed under `PlantLibrary_AndroidApp/design/stacks/compose/generated/` and added to `:core:design` as a source dir. A package of `design.generated` is acceptable in Kotlin. A Kit option for `com.plantlibrary.android.core.design.generated` would be cleaner (Kit finding).
2. The hand adapter `Theme.kt` builds `lightColorScheme`/`darkColorScheme` from `LightRoles`/`DarkRoles`, covering all M3 roles: `secondaryContainer`, `surfaceContainer*`, `outlineVariant`, `surfaceTint`, `inverse*`.
3. `Type.kt` keeps the weights (the emitter drops them) and reads sizes from `Tokens.Dimension.Typography*`.
4. `Shape.kt` reads `Tokens.Dimension.Radius*`, including `RadiusNav`.
5. A `CompositionLocal` for state containers and chart roles, so features stop needing the raw object.
6. `Spacing.kt` becomes aliases of `Tokens.Dimension.Space*` until the 82 dp literals are replaced.

**What the Kit must emit, or the Configuration must carry, for this client to be pinned.**

- **(i)** `Tokens.kt` (exists).
- **(ii)** Weights per typography role, so `TextStyle` can be generated. Kit finding, otherwise adapter-side.
- **(iii)** Banned-colour aliases in ARGB spelling (`0xFF22C55E`, `0xFF16A34A`, `0xFF4ADE80`). Configuration data.
- **(iv)** Kotlin-aware literal patterns in `check-literals.mjs` (`Color\(0x[0-9A-Fa-f]{8}\)`, `\b\d+(\.\d+)?\.(dp|sp)\b`). Kit finding.
- **(v)** `PlantLibrary_AndroidApp/design/conformance/CONSUMED_DESIGN.md` naming the Configuration and its version (per Q-G-01 (a)), plus a `design/stacks/compose/mapping.md` from RC-A9A-03.
- **(vi)** A hygiene `D-…` entry declaring `design/` (and the migration workspace, Q-A9A-06).

**Compile-free checks available (names only).**

| Check | Available? |
|---|---|
| `scripts/check_token_drift.py` (Python, report-only) | yes |
| `scripts/hygiene/repo_hygiene_check.py` (hygiene) | yes |
| Kit node checks (`check-literals`, `check-banned-colors`, `check-drift`, `check-pin`, `run-all`) | yes, but blind to Kotlin literals until (iii) and (iv) |
| ktlint, detekt, spotless, ktfmt | none: no plugin in `libs.versions.toml`, no config file, no `.editorconfig` |
| Android Lint, Kotlin compile | Gradle tasks only, so not usable under Q-G-04 (a) |
