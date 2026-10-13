---
name: design-adoption
description: Retired 2026-10-13 (Q-G-07 (a), step B5-7 of the master rework program) - do not use. Use design-gate instead, installed in each anchored client (PlantLibrary_Dashboard, PlantLibrary_AndroidApp, PlantLibrary_PyApp) under .claude/skills/design-gate. This file is a pointer only.
user-invocable: false
---

# design-adoption - retired

Retired 2026-10-13, Q-G-07 (a): the three client suites are anchored to the
Design Configuration (`B5-4`, `B5-5`, `B5-6`), so this house gate is replaced
by its parameterised successor. This file keeps no canon, no values and no
rows.

- **Use `design-gate`** - `.claude/skills/design-gate/SKILL.md` in
  `PlantLibrary_Dashboard`, `PlantLibrary_AndroidApp` and `PlantLibrary_PyApp`
  (installed by the Design Template Kit; closes with `design-audit`).
- **The P-DS map** lives in `PlantLibrary_SharedContracts/design/decisions/`
  (and the conduct parameters in `design/conduct-rules.md`).
- **The adoption rows** live in
  `PlantLibrary_SharedContracts/design/DESIGN_VERSION.md`, its "Consumers"
  lines.

The six batch rows that named this skill (`WD-V1-DS-01`, `WD-V1-DS-06`,
`AN-V1-DS-01`, `AN-V1-DS-05`, `PY-V1-DS-01`, `PY-V1-DS-03`) name
`design-gate` since `B5-7`, each recorded as a plan amendment in its
package's `STATE.md`. The frozen Codex copy under `.codex/skills/` keeps the
old text and is not edited.
