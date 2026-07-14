---
name: plan-batch
description: Author or amend an implementation batch package in the PlantLibrary house format (BATCH_PLAN.md, TASK_CHECKLIST.md, TASK_CONTEXT.md, STATE.md). Turns a proposal, audit finding, or feature request into sized, verifiable batch rows; enforces the row schema, ID scheme, and dependency/evidence rules; presents the draft for item-by-item approval before writing any file. Use for "plan a batch for X", "add rows for finding Y", "turn this proposal into batches", "create a new implementation package".
user-invocable: true
argument-hint: "[suite-or-package-path] [what to plan]"
---

Produce batch plans that run-batch can execute unattended. Plan quality is
measured by one thing: can a fresh session complete each row from its
checklist line + anchor alone, and prove it with the named validation?

## 1. Gather inputs (narrowly)

1. Locate the target package the same way run-batch does (argument → path or
   suite → glob `implementation/*/BATCH_PLAN.md`). If none exists, this is a
   new package — see §6.
2. Read `STATE.md` (durable status, blockers) and only the sections of the
   proposal/authority docs the request touches. Do not re-read what the
   conversation already established.
3. List existing batch keys and row IDs (grep headings and ID column) so new
   ones extend the sequences without collision.

## 2. First-principles gate — before drafting anything

1. **Already covered?** Search existing rows across the affected packages.
   If another package owns the concern, route the finding there (one line in
   its STATE.md or a row proposal for it) — never duplicate rows.
2. **Actually needed?** Planning documents written by earlier AI sessions are
   draft input, not requirements — challenge inherited scope, "binding"
   labels, and deferral rationales unless they record an explicit user
   decision. Recommend dropping low-value work; say so in the draft.
3. **Right size?** Prefer one batch with 1–4 primary rows over many thin
   batches. If the request needs more than ~3 batches, propose the batch
   skeleton first and detail only the first batch; later batches get
   detailed when their prerequisites exist (plans written far ahead of
   reality rot).

## 3. Row authoring rules

Checklist schema (one table, one row per task):

```text
ID | status | skill | design_context | baseline_id | area | file(s) | task | context | requirements | done-when | validation | risk | effort
```

- **ID**: `<SUITE>-<PROGRAM>-<AREA>-NN`, e.g. `PY-V1-UX-03`. Continue existing
  sequences; never reuse or renumber.
- **status**: new rows are `todo` (or `blocked`/`gated` with the reason
  recorded). Allowed values: todo | needs-reverify | gated | blocked |
  deferred | done.
- **skill**: `none` unless the row genuinely executes a skill command
  (`impeccable:audit`, …). Skills are activated by rows, never ambiently.
- **design_context**: decide from the row's *action*, not its file paths.
- **baseline_id**: what the row traces to — a gap ID, decision ID, deferral,
  or `GAP(<short>)`. Every row must trace to something; a row that traces to
  nothing is scope creep — cut it or record the new decision first.
- **task**: imperative, self-contained, one session of work. Split anything
  larger; merge fragments that always ship together.
- **context**: `[details](TASK_CONTEXT.md#<id-lowercase>)`.
- **requirements**: checkable artifacts only — row IDs, file paths, versions
  ("`SC1-B00` done", "stack recipe recorded"). Never vibes ("design stable").
- **done-when**: an observable end state a reviewer could verify, not a
  restatement of the task.
- **validation**: a runnable command or a concrete artifact path
  (`pytest -m server_integration`, `validation/<BATCH>_<slug>.md`).
  **"tests" or "review" alone is not a valid entry — the row is rejected.**
- **risk/effort**: H/M/L and S/M/L. An `L` effort must still fit one session.

## 4. Anchor and batch rules

- One `### <ROW-ID>` anchor in `TASK_CONTEXT.md` per row, written together
  with the row. First line repeats `` `skill: …` · `design_context: …` ``
  (run-batch stops on mismatch). Body: the how — key files/symbols, protocol
  steps, environment, output format. End with `**Done when:** …`.
- Anchors carry everything a fresh session needs; if the how depends on an
  MVP-era or external document, summarize the needed part into the anchor
  instead of linking a file the executor must not or cannot read.
- Batch section format in `BATCH_PLAN.md`:

```markdown
## Batch <KEY> — <title> [(independent)]

**Goal:** <one or two sentences — the user-visible or system outcome>
**Primary rows:** `<ID>`, `<ID>`
**Requires:** <checkable artifacts, or "Nothing — independent">
**Blockers:** <known failure modes and what to record when they hit>
**Notes:** <coordination with other packages; route-don't-duplicate targets>
```

- Order batches by execution order; mark independence explicitly.
- Standing invariants (e.g. offline smoke) live once in the package
  scope file — never restated per row.
- A batch whose goal is only "update documents" should be a `STATE.md`
  continuation entry instead, unless the documents are contracts.

## 5. Approval gate — nothing is written before this

1. Present the draft compactly: batch heading(s), a table of proposed rows
   (ID, task one-liner, requirements, validation, risk/effort), what gets
   dropped or routed elsewhere, and any inherited constraint you recommend
   discarding.
2. Ask for approval item-by-item (AskUserQuestion when interactive; otherwise
   stop and leave the draft in the report). Apply vetoes and re-present only
   the changed items.
3. On approval, write in one pass: batch section(s), checklist rows, anchors,
   and a dated `STATE.md` continuation entry —
   `**<date> — plan amendment (<short>, no code run).** <what + why + authority>`.
4. Amendments to existing batches follow the same gate. Never edit a `done`
   row's meaning — supersede it with a new row.

## 6. Scaffolding a new package

File set under `<suite>/implementation/<Package_Name>/`:

```text
README.md          purpose, authority chain, how to run (points at run-batch)
SCOPE.md           hard scope (touchable/read-only paths) + standing invariants
CONTEXT_INDEX.md   what a session may read, and what it must not (MVP-era docs)
BATCH_PLAN.md      batches (§4)
TASK_CHECKLIST.md  schema comment + row table (§3)
TASK_CONTEXT.md    anchors (§4)
STATE.md           durable status / authority / blockers / continuation log
proposal/          the why — proposals and decision records
validation/        evidence packs written by run-batch
```

Procedure lives in the run-batch skill — do **not** generate a per-package
DRIVER_SCRIPT.md; `SCOPE.md` replaces it. No `_ACT_STATE.md` (deprecated;
checklist status is the single source of truth).

## 7. Self-review before presenting

- [ ] Every row completable by a fresh session from row + anchor alone
- [ ] Every `validation` entry runnable or a concrete artifact path
- [ ] Every `requirements` entry checkable; dependency cycle-free
- [ ] Every row traces to a baseline; no untraceable scope
- [ ] Row/anchor `skill` + `design_context` values identical
- [ ] IDs collision-free; batches ordered; independence marked
- [ ] Findings for other packages routed, not duplicated
