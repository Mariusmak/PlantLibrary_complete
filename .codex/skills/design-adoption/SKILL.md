---
name: design-adoption
description: Pre-work gate for any session touching UI code in PlantLibrary_Dashboard, PlantLibrary_AndroidApp, or PlantLibrary_PyApp. Forces the work to be checked against the binding design system (tokens 1.2.0 "field-ledger" canon + decisions P-DS-01..10) instead of relying on memory. Fires before editing styles, colors, spacing, radii, themes, components, or any rendered surface in the three client suites.
user-invocable: true
argument-hint: "[dashboard|android|pyapp]"
---

# Design Adoption Gate

## 1. Purpose

The design system is **binding and lives in files**, not in your memory. Token
values drift the moment they are copied, so this skill never restates them — it
**points** to the canon and makes you read it before you touch UI. Trust the
files below over anything you recall about greens, ramps, or roles.

## 2. When this fires

Any session that edits, adds, or reviews a **rendered surface** in
`PlantLibrary_Dashboard`, `PlantLibrary_AndroidApp`, or `PlantLibrary_PyApp` —
colors, spacing, radii, typography, themes (light/dark), components, charts,
focus/hover/selection states, or the token-mirror files themselves
(`design_tokens.py`, `Color.kt`, `Shape.kt`, generated theme CSS/vars).

If the change is pure logic with no rendered effect, this gate does not apply.

## 3. Canon — read before writing (never copy values out)

| What | Path |
|---|---|
| Token values (1.2.0 field-ledger) | `PlantLibrary_SharedContracts/design-tokens/tokens.json` |
| Semantic role compositions (light+dark) | `PlantLibrary_SharedContracts/design-tokens/semantic-roles.json` |
| Rules & rationale (per token group) | `PlantLibrary_SharedContracts/design-tokens/TOKEN_USAGE_NOTES.md` |
| How each platform consumes tokens | `PlantLibrary_SharedContracts/design-tokens/platform-mapping-{web,android,python}.md` |
| Binding decisions P-DS-01..10 | `PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` |

`tokens.json` is the **only** source of token values. `TOKEN_USAGE_NOTES.md` is
the only source of the group rules. If they disagree with a decision in `04_*`,
the decision record wins — record the conflict, do not improvise.

## 4. Pre-work checklist

1. **Read the ledger.** Open `tokens.json` + `TOKEN_USAGE_NOTES.md` and, for any
   themed/stateful surface, `semantic-roles.json`. Read the platform-mapping note
   for the suite you're in.
2. **Check which P-DS decisions apply** to what you're touching (in `04_*` §2):
   PRIMARY/accent → P-DS-02/09; neutrals → P-DS-03; dark surfaces → P-DS-04/05;
   type/spacing/radii → P-DS-06; charts → P-DS-07; component/conduct rules →
   P-DS-08; page anatomy/nav → P-DS-10.
3. **Check the adoption row for this suite** (below): is the code you're touching
   inside what that row already covers? If the row is still open and your change
   overlaps its scope, align to tokens 1.2.0 now and note it against the row —
   don't create parallel, conflicting adoption.

### Adoption rows (each in its suite's `implementation/System_V1_Implementation/{BATCH_PLAN,TASK_CHECKLIST}.md`)

| Suite | Row (batch) | Covers |
|---|---|---|
| Dashboard | `WD-V1-DS-06` (`WD1-B06`) | `npm run generate:theme` regen; role bindings (app bg→neutral-100, links/focus→accent); `SEMANTIC_DARK` dark surfaces; `--radius-pill-input` → `full`. |
| Android | `AN-V1-DS-05` (`AN1-B11`) | Hand-mirrored `core/design` (`Color.kt`, `Shape.kt`) → tokens 1.2.0; M3 state containers + dark scheme bound to `semantic-roles.json`; retire `pillInput`. |
| PyApp | `PY-V1-DS-03` (`PY1-B06`) | `design_tokens.py` ramps/roles → tokens 1.2.0 (desktop values are the canon); adopt `SEMANTIC_DARK` names; retire `pill_input`. |

Until a row runs, that suite's hand-mirrored values are **knowingly** out of sync
(recorded drift, per `04_*` §4) — do not silently "fix" them outside the row
unless your change requires it, and if it does, align to the ledger.

## 5. Hard rules

- **Tokens 1.2.0 is the only source of truth.** Never hardcode a hex, spacing,
  or radius that duplicates a token — reference the token/role/generated var.
- **Banned pre-1.2.0 Tailwind greens — never anywhere:** `#22C55E`, `#16A34A`,
  `#4ADE80`. They fail WCAG (see `04_*` §3 / `TOKEN_USAGE_NOTES.md` PRIMARY). The
  light accent is Living Green `PRIMARY.600 #2A7A30`; the dark accent is
  `PRIMARY.400 #74BC85` with dark on-accent text, never white.
- **Dark surfaces need dark tokens.** Any light-theme fill needs an explicit
  `DARK` role from `semantic-roles.json`; white wells/banners on dark are a defect.
- **Neutrals are green-tinted field neutrals** — never flat greys.
- **Conduct rules stand** (P-DS-08): accent ≤10% of a screen, flat by default,
  status = text/icon + color (never color alone), sentence case, scientific names
  italic, chart categorical order green→blue→amber→purple with purple reserved
  for bloom.
- **After changing token-mirror files, regenerate** where the suite generates
  (Dashboard `generate:theme`) rather than hand-editing generated output.

## 6. Do not

- Restate token values from memory or from an old mockup instead of reading the ledger.
- Introduce a green/neutral/radius not present in `tokens.json`.
- Compose a new surface without checking `semantic-roles.json` for an existing role.
- Reintroduce the deprecated `pill_input`/`pillInput`/`--radius-pill-input` (use `full`).
