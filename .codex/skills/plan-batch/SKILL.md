---
name: plan-batch
description: Author or amend an implementation batch package in the PlantLibrary house format (BATCH_PLAN.md, TASK_CHECKLIST.md, TASK_CONTEXT.md, STATE.md). Turns a proposal, audit finding, or feature request into sized, verifiable batch rows; enforces the row schema, ID scheme, and dependency/evidence rules; presents the draft for item-by-item approval before writing any file. Use for "plan a batch for X", "add rows for finding Y", "turn this proposal into batches", "create a new implementation package".
user-invocable: true
argument-hint: "[suite-or-package-path] [what to plan]"
---

<!-- plan-batch skill version: 1.2.0 (2026-07-26) — adds mandatory local
     Telegram notification enqueueing at every terminal user handoff. -->

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
ID | status | skill | design_context | baseline_id | area | file(s) | task | context | requirements | done-when | validation | risk | effort | model
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
  The named validation must **execute the code the row changes**. A row whose
  validation can pass while its production code is broken is rejected — most
  often because the test substitutes the layer under test with a fixture
  stand-in. Substitution is allowed only at process boundaries (subprocesses,
  third-party HTTP, clock, randomness); the composition root, domain services,
  persistence, and routes/rendering always run for real. See the
  `real-stack-testing` skill. For any row touching a rendered surface or
  cross-module behavior, cite that skill in the row's `skill` column and make
  the validation observe real behavior end to end.
- **risk/effort**: H/M/L and S/M/L. An `L` effort must still fit one session.
- **model**: recommended worker tier pair, one of `opus/sol`, `sonnet/terra`, or
  `haiku/luna` — left is the Claude tier, right the matching Codex tier, always
  named together (never one alone). These are the same tier names as
  `vendors.claude.ladder` / `vendors.codex.ladder` in `config.example.yaml`,
  which already pair them 1:1 (Opus 4.8 ≡ GPT 5.6 Sol, Sonnet 5 ≡ GPT 5.6 Terra,
  Haiku 4.5 ≡ GPT 5.6 Luna). Default `sonnet/terra`; use `opus/sol` for
  architectural/high-risk rows (`risk: H` or design-defining work) and
  `haiku/luna` for mechanical/low-risk rows (`risk: L`, boilerplate, rote
  edits). run-batch surfaces this so the operator (or an Agent-spawning caller)
  can select the matching model when the row executes.

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
**Model:** <default tier pair for this batch's rows, e.g. `sonnet/terra`; a row's own `model` column overrides this>
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
2. Before every approval request, enqueue an `approval required` notification
   per §8. Then ask for approval item-by-item (AskUserQuestion when
   interactive; otherwise stop and leave the draft in the report). Apply
   vetoes and re-present only the changed items, enqueueing again before any
   new approval request.
3. On approval, write in one pass: batch section(s), checklist rows, anchors,
   and a dated `STATE.md` continuation entry —
   `**<date> — plan amendment (<short>, no code run).** <what + why + authority>`.
4. Amendments to existing batches follow the same gate. Never edit a `done`
   row's meaning — supersede it with a new row.
5. After the approved write and self-review succeed, report the planning task
   as finished and enqueue a `completed` notification per §8 before returning.

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
- [ ] Every `validation` entry executes the row's real production code — no
      row can pass while the code it changes is broken (`real-stack-testing`)
- [ ] Every `requirements` entry checkable; dependency cycle-free
- [ ] Every row traces to a baseline; no untraceable scope
- [ ] Row/anchor `skill` + `design_context` values identical
- [ ] Every row and batch names a `model` pair (`opus/sol` · `sonnet/terra` · `haiku/luna`); never a Claude tier without its Codex match
- [ ] IDs collision-free; batches ordered; independence marked
- [ ] Findings for other packages routed, not duplicated

## 8. Notify at every terminal user handoff

Notify whenever the invocation must yield control and the user must be
informed:

- before requesting approval, including a revised approval request;
- after the planning task finishes successfully, including a conclusion that
  no package changes are needed;
- before stopping for any blocker, ambiguity, missing input/artifact,
  required decision, failed write/validation, or other human action; and
- before any other terminal report whose outcome the user must see.

Do not notify for routine progress updates that do not yield control. For each
required notification, prepare this compact plain-text notice:

```text
Plan batch: <package path, or unresolved target>
Status: <approval required | completed | blocked | stopped>
Summary: <what was drafted, written, concluded, or prevented>
Human action needed: <specific approval/action, or none>
```

**Notify.** Best-effort, never blocks: pipe the notice text to
`python scripts/notify_telegram.py --enqueue` (repo root). This command performs
only an atomic local outbox write; it does not access Credential Manager, the
network, Telegram, or any other external system, so it needs no external-action
authorization or host/sandbox escalation. A user-installed Windows background
task independently drains the outbox, reads the token from Credential Manager,
sends the message, and retains transient failures for retry.

The plan-batch agent must use `--enqueue`; never invoke this script's
direct-send, `--drain-once`, or `--watch` modes. Enqueue before presenting the
approval prompt or terminal report. On exit 0 report `Notification: queued for
local Telegram notifier` — do not claim synchronous delivery. On non-zero note
the local enqueue failure and continue; notification failure never changes the
planning result or replaces the user-facing prompt/report.
