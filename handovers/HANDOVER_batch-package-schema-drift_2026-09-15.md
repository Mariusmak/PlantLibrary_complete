# HANDOVER — batch-package schema drift across PlantLibrary suites (2026-09-15)

Written for: the operator of this repo, to analyze and decide how to update
the batch plans, the shared skill mirrors, and each suite's `CLAUDE.md`.

Context: a second Conductor instance (`C:\Programs\AI_Orchestrator_2`) was set
up to drive this repository, following
`C:\Programmierung\Orchestrator_System\docs\handbook\09-second-instance.md`.
That setup is done and out of scope here — this handover covers only what it
surfaced about the batch packages themselves.

## Finding 1 (blocking): every checked batch package fails Conductor's package validator

None of the 9 batch packages checked across the 6 `PlantLibrary_*` suites can
currently be bound to a Conductor project. Attempting to bind any of the 5
`System_V1_Implementation` packages via `POST /api/v1/projects` fails with:

```
no 15-column checklist table found; batch PY1-B00 declares missing primary
row PY-V1-WALK-01; ... (dozens more "declares missing primary row" lines) ...
batch PY1-B04 has requires token PY1-B05 outside the first sentence; fold the
prerequisite into the first sentence or move the commentary to **Notes:**
```

**Root cause:** Conductor's parser (`src/conductor/batch_package.py`,
`CHECKLIST_COLUMNS`) requires an exact 15-column `TASK_CHECKLIST.md` header:

```
ID | status | skill | design_context | baseline_id | area | file(s) | task | context | requirements | done-when | validation | risk | effort | model
```

Every `System_V1_Implementation` package's checklist uses a **14-column**
header — missing the trailing `model` column — and even says so in its own
comment: *"Columns (V3 schema): ID | status | skill | ... | risk | effort"*.
The column-count match is exact-equality, so a 14-vs-15 mismatch means **zero
rows are ever parsed** — not shifted, not partially read, none. That is why
the error list also claims dozens of specific rows are "missing": they are
textually present in the file (spot-checked `PY-V1-WALK-01`, `PY-V1-INT-01`,
`PY-V1-TEST-01` — all exist), but the whole table was never recognized in the
first place. Most of the noisy error output is this one root cause fanning
out, not independent defects.

**Timing:** the `model` column was added by commit `1e59f65`
("CD2-B184: AM-26 — the batch plan's model tuple becomes policy"), dated
**2026-08-15**. `PlantLibrary_PyApp`'s own `TASK_CHECKLIST.md`/`BATCH_PLAN.md`
were last touched **2026-07-17** / **2026-07-15** — a month before AM-26
shipped. These packages are genuinely pre-schema-migration, not miswritten.
The freshly-refreshed `.claude/skills/plan-batch/SKILL.md` in this repo
documents the current 15-column schema and mandates a `model` pair
(`opus/sol` · `sonnet/terra` · `haiku/luna`) on every row and batch — so the
skill mirror is current; the packages are what's stale.

**"`_V3` schema"** (referenced in these files' own headers) is PlantLibrary's
internal label for this pre-AM-26 convention — it was never a distinct
Conductor schema, just the generation before the `model` column.

**PlantLibrary_Workspace is worse, not better:** its 4 packages are each at a
*different* generation, and none match 15 columns either:

| Package | Columns | Schema |
|---|---|---|
| `System_Tooling` | 14 | same pre-AM-26 `_V3` header as the other 5 suites |
| `System_Design_Architecture` | 13 | missing both `baseline_id` and `model` |
| `System_Integration_MVP` | 11 | older schema entirely: `ID\|Batch\|Status\|Skill\|Design context\|Area\|Task\|Output\|Anchor\|Requirements\|Validation` |
| `Cross_Platform_Strategy`* | 11 | same older 11-column schema |

\* lives under `strategy/Cross_Platform_Strategy`, not `implementation/`; found incidentally during this check.

## Finding 2 (separate, independent defect): malformed `Requires:` tokens

Independent of the column-count issue, several batches also fail a second,
unrelated lint (the CD2-B175 self-reference/prerequisite-placement guard):
a `Requires:`-style token referencing another batch ID appears outside the
first sentence of that batch's description, e.g.:

```
batch PY1-B04 has requires token PY1-B05 outside the first sentence; fold
the prerequisite into the first sentence or move the commentary to **Notes:**
```

This check runs over `BATCH_PLAN.md` prose regardless of whether the
checklist table parses, so it will still need fixing even after the column
issue above is resolved. Seen in `PlantLibrary_PyApp` (PY1-B04) and
`PlantLibrary_AndroidApp` (AN1-B08, AN1-B11).

## Current state on instance 2

All 6 suites are registered as Conductor projects (name = repo folder name),
but **none is bound to a batch package** — the 5 that could theoretically
bind (one package each) all fail validation as above, and
`PlantLibrary_Workspace` was left unbound by choice pending a decision on
which of its 4 packages to use. `PlantLibrary_PyApp` is the active project;
the rest are inactive (Conductor only dispatches the active project's tasks).

## Also worth checking, not yet done

The handbook's step 7 asks for a skill-assumption check: read
`.claude/skills/run-batch/SKILL.md` and `plan-batch/SKILL.md` (just refreshed
to the current version in this repo) end-to-end, list every assumption they
make about the repo they run in, and check each suite's `CLAUDE.md`/`AGENTS.md`
against it. That check wasn't run yet, and given the schema drift above it
would likely surface the same `model`-column and schema-generation gaps from
the skill's own point of view, plus possibly other stale assumptions.

## Suggested next steps (for you to decide, not applied)

1. Decide, per suite, whether to migrate `TASK_CHECKLIST.md` to the current
   15-column schema (add `model` per row/batch) or treat these as legacy
   packages Conductor won't drive until migrated.
2. For `PlantLibrary_Workspace`, decide which of the 4 packages (or all,
   migrated individually) should become biddable, given they're each at a
   different schema generation.
3. Fix the `Requires:`-placement lint failures alongside any schema
   migration (same files, same pass).
4. Once a package validates, bind its project via GUI intake or
   `PATCH /api/v1/projects/{id}` (note: `batch_package_path` is immutable
   once bound — no do-overs without archiving and recreating the project).
5. Run the step-7 skill-assumption check and update each suite's `CLAUDE.md`
   accordingly.
