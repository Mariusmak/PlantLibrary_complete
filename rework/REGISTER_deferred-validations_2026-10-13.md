# Deferred validations — PlantLibrary master rework (register of record)

*Opened 2026-10-13 at `R-0` (`PROMPT_master-rework-kickoff_2026-10-13.md` §2 rule 1). Nothing in Phases A and B of
this program runs a test: no test runner, no browser automation, no emulator, no Gradle test task, no Docker
stack, no app launch for validation. A step that believes it needs one records the need here and goes on. At `C1`
these rows become the first batches of Phase C through `plan-batch`; the validation cells of the batch packages are
never widened or deleted in Phase B, only pointed at from here. Rows are written by the orchestrator from a lane's report in
the step's flip commit; a lane outside the superproject never writes this file.*

## How to read a row

| Column | Meaning |
|---|---|
| ID | `DV-<nn>`, in order of recording |
| Lane · step | The runbook step that recorded the need |
| Repository | The repository whose change is unvalidated |
| Change | What was changed without its validation (files, rows, commit) |
| What would be run | The exact validation the change needs, as the owning row's `validation` cell or the skill's standing legs name it |
| Skill | The skill that owns the validation (`verify-stack`, `android-validation`, `gui-validation`, `webapp-testing`, `validate-real-stack`, `run-batch`, a Kit check, …) |
| After | The lane or step that must be done before the validation makes sense |
| Package row | The batch-package row (`<SUITE>-V1-…`) whose validation cell this row points at, or `new` when `C1` must plan one |
| State | `proposed` (named by an analysis lane at `R-1` before any change; the `B6` step that makes the change flips it) · `deferred` · `planned (<batch key>)` · `done (<date>)` |

## Rows

| ID | Lane · step | Repository | Change | What would be run | Skill | After | Package row | State |
|---|---|---|---|---|---|---|---|---|
| DVC-A9D-01 | A9 (analysis) → B6 | PlantLibrary_Dashboard | proposed at R-1: dark-theme rendering per route | light + dark screenshot of all 12 views; check for light fills on dark surfaces (38 fills, 20 overrides) | webapp-testing (via the `e2e/` harness) | B6 migration batch | new | proposed |
| DVC-A9D-02 | A9 (analysis) → B6 | PlantLibrary_Dashboard | proposed at R-1: post-1.2.0 current-state baseline | screenshot pass of all routes at the current commit (the existing 16 PNGs predate 1.2.0) | webapp-testing + verify-stack | before B6 gap map is accepted | new | proposed |
| DVC-A9D-03 | A9 (analysis) → B6 | PlantLibrary_Dashboard | proposed at R-1: compact and viewport behaviour | 1280×800, 1200, 1100, 1024, 900 px sweep; shell compact claims (F-A9D-15) | webapp-testing | B6 | new | proposed |
| DVC-A9D-04 | A9 (analysis) → B6 | PlantLibrary_Dashboard | proposed at R-1: contrast on dark | focus ring and text-ramp contrast on dark surfaces where `--neutral-*` text is not overridden | webapp-testing (computed styles) | B6 | new | proposed |
| DVC-A9D-05 | A9 (analysis) → B6 | PlantLibrary_Dashboard | proposed at R-1: accent ≤ 10 % per screen (P-DS-08) | rendered-area measurement per screen | Kit design checks / impeccable audit (`WD-V1-DS-05`) | B6 | new | proposed |
| DVC-A9D-06 | A9 (analysis) → B6 | PlantLibrary_Dashboard | proposed at R-1: chart palette order and dark charts | Statistics and Calendar legends in light and dark | webapp-testing | B6 | new | proposed |
| DVC-A9D-07 | A9 (analysis) → B6 | PlantLibrary_Dashboard | proposed at R-1: toast conduct | toast appearance against the 4 px stripe rule (F-A9D-20) | webapp-testing | B6 | new | proposed |
| DVC-A9D-08 | A9 (analysis) → B6 | PlantLibrary_Dashboard | proposed at R-1: drift checker after canon amendment | `node scripts/check-token-drift.mjs` exits 0 once Q-A9D-02 lands | run-batch standing leg (static; allowed under Q-G-04 (a) if classed as a static check) | B5 | new | proposed |
| DVC-A9D-09 | A9 (analysis) → B6 | PlantLibrary_Dashboard | proposed at R-1: type/lint after the token-name migration | `tsc -b` and `npm run lint` after the alias or rename step | run-batch standing legs | B6 migration batch | new | proposed |
| DV-A9A-a | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: Gradle compile (Q-G-04 (b) or Phase C) | The Kit-emitted `Tokens.kt` compiles inside `:core:design` (name resolution of `Color(…)` inside `object Color`, package `design.generated`) | `run-batch` standing leg (`assembleDebug`) | B5 Android emission | new | proposed |
| DV-A9A-b | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: emulator | Light and dark "current state" capture of all 15 views, named `<page_id>__android__<light\|dark>.png` | `android-validation:capture` (extended per RC-A9A-11) | B6 workspace bootstrap | new | proposed |
| DV-A9A-c | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: emulator plus mockup snapshot | Visual comparison of Home, Add, Plant detail and Sync against the 4 approved phones, light and dark | methodology 05 / `android-validation:capture` | B6 IA | new | proposed |
| DV-A9A-d | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: emulator, dark mode | Dark-theme parity (SEMANTIC_DARK surfaces, no light creams on dark) | `AN-V1-QA-01` | B6 implementation | new | proposed |
| DV-A9A-e | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: screenshots plus a contrast measurement (impeccable's engine needs a browser, F-A9A-19) | Rendered contrast of filled-button labels and focus indicators (today `#16A34A`; after: `#2A7A30`) | `AN-V1-QA-01` | B6 implementation | new | proposed |
| DV-A9A-f | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: emulator | Touch targets ≥ 48 dp, TalkBack traversal, font scaling | `AN-V1-QA-01` | B6 implementation | new | proposed |
| DV-A9A-g | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: emulator walk | Bottom-nav selected state on pushed routes | `AN-V1-SHELL-01` | B6 implementation | new | proposed |
| DV-A9A-h | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: emulator, dark mode | Launch-window flash in dark mode (`themes.xml:8` light parent) | `android-validation:capture` | B6 implementation | new | proposed |
| DV-A9A-i | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: screenshots, light and dark | Which M3 baseline roles actually render (lavender indicator, `surfaceTint` on elevated bars, Card container role in material3 1.2.1) | `android-validation:capture` | B6 census | new | proposed |
| DV-A9A-j | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: Gradle | The Gradle lint task over all modules (lint is a Gradle task, excluded by Q-G-04 (a)) | `run-batch` standing leg | B6 implementation | new | proposed |
| DV-A9A-k | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: screenshots from DV-A9A-b | `impeccable audit` and `critique` over fresh screenshots (`AN-V1-DS-04`) | `impeccable:audit` | DS-02/03 done | new | proposed |
| DV-A9A-l | A9 (analysis) → B6 | PlantLibrary_AndroidApp | proposed at R-1; needs: emulator plus local stack | Census pass B confirmation that every view renders with seeded data (gate views included) | `android-validation:walkthrough`, `verify-stack` | B6 census | new | proposed |
| DV-A9P-01 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | Light + dark capture of every `SCREEN_VARIANTS` screen (24) through the scenario provider, as the current-state baseline (methodology 03) | gui-validation / scenario provider | B6 start (before) and B6 end (after) | new | proposed |
| DV-A9P-02 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | Checked checkbox shows a glyph in both themes (F-A9P-06) | gui-validation | B6 | new | proposed |
| DV-A9P-03 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | QSS `url()` icons render when launched from a cwd other than the repo root and from the packaged build | gui-validation (+ PY-V1-REL-01) | B6 | new | proposed |
| DV-A9P-04 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | Startup with persisted `theme=dark`: no widget shows light-role colours before the first theme change (F-A9P-08) | gui-validation | B6 | new | proposed |
| DV-A9P-05 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | "Follow system setting" follows the OS scheme (Q-A9P-03) | gui-validation | B6 | new | proposed |
| DV-A9P-06 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | Dark-theme contrast and `SEMANTIC_DARK` use on rendered surfaces (P-DS-04; F-A9P-05) | gui-validation + contrast measurement | B6 | new | proposed |
| DV-A9P-07 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | Retiring `pill_input` (19) for `full` does not drop rounding on fixed-height inputs (`design_tokens.py:138-143` documents Qt's half-height cutoff) | gui-validation | B6 | new | proposed |
| DV-A9P-08 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | Rendered QSS of both themes byte-compared before/after the generated artifact lands (PY-V1-DS-01 done-when) | the suite's design-token tests via run-batch validation | B5/B6 | new | proposed |
| DV-A9P-09 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | impeccable audit + critique of sync-era surfaces (PY-V1-DS-02) on fresh screenshots | impeccable:audit | after DV-A9P-01 | new | proposed |
| DV-A9P-10 | A9 (analysis) → B6 | PlantLibrary_PyApp | proposed at R-1 | Chart series order and `CHART_DARK` on statistics/calendar (P-DS-07) | gui-validation | B6 | new | proposed |
| DV-B5-01 | B5 · B5-1 → B5-3 | PlantLibrary_SharedContracts | the recomposed `text_muted` and `series_3` values are checked numerically only (the gate's value set) | Gallery generation and the Kit's baseline capture for the BINDING Configuration in both themes, plus a visual check that `text_muted` reads below `text_secondary` and that `series_3` stays distinct from series 2 and 4 | Kit Gallery capture (browser) | B5-3 | new | proposed |
