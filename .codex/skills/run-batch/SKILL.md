---
name: run-batch
description: Execute one implementation batch from a batch package (BATCH_PLAN.md + TASK_CHECKLIST.md + TASK_CONTEXT.md, PlantLibrary house format). Selects the next actionable batch or the one named in the argument, enforces requirements, implements only the selected rows, runs each row's named validation, records evidence, updates row statuses, commits, and prints a compact report. Use for "run the next batch", "execute PY1-B02", "continue the V1 implementation" in any suite.
user-invocable: true
argument-hint: "[suite-or-package-path] [batch-key]"
---

Execute exactly one batch per invocation, then stop. Optimize for low context:
narrow reads, small edits, compact output.

## 1. Locate the package

1. If the argument names a path, use it. If it names a suite
   (`PyApp`, `Server`, `AndroidApp`, `Dashboard`, `SharedContracts`,
   `Workspace`), glob `PlantLibrary_<Suite>/implementation/*/BATCH_PLAN.md`.
   No argument: infer the suite from the working directory; if ambiguous, ask.
2. If several packages match, pick the one whose `STATE.md` names a next
   actionable batch; otherwise ask the user which package to run.
3. The package root is the directory containing `BATCH_PLAN.md`. Expected
   siblings: `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`,
   `validation/`, and a suite `DRIVER_SCRIPT.md` or `SCOPE.md`.

## 2. Authority and precedence

- **Binding, always:** the suite `CLAUDE.md` (layer rules, coding standards,
  protocols such as `GUI/COMMON_GUI_CHANGE_PROTOCOL.md`) and the package
  driver/scope file's **Hard scope** section and **standing invariants**
  (e.g. PyApp's offline startup smoke at every batch close).
- **Superseded by this skill:** the procedural sections of any legacy
  `DRIVER_SCRIPT.md` (discovery, reading, edit, state-update algorithms).
  Follow this skill's procedure instead.
- **Deprecated:** `_ACT_STATE.md` / `_ACT_STATE_V3.md`. Do not read or update
  them. Checklist row status is the single source of truth; batch done-ness
  is derived from it.

## 3. Select the batch

1. If the argument names a batch key, select it (still enforce its
   `Requires:`).
2. Otherwise grep `BATCH_PLAN.md` for `^## Batch`, `**Primary rows:**`,
   `**Requires:**`, `**Blockers:**` and pick the **first batch in plan order**
   whose primary rows include actionable statuses and whose `Requires:` are
   satisfied. Batches marked independent may be taken out of order when
   earlier batches are blocked.
3. Actionable row statuses: `todo`; `blocked` only when its recorded
   requirements are now verifiably satisfied; `needs-reverify` only when
   resolvable by narrow source reads. Never execute `gated` or `deferred`
   rows — report the human action they need instead.
4. A `(done)` heading suffix is a convenience marker only. Trust the
   checklist: a batch is done when every primary row is `done`,
   `deferred`-with-rationale, or `blocked`-with-recorded-blocker.
5. If nothing is actionable, report why (per batch: the unmet requirement or
   gate) and stop.

## 4. Preflight the rows

For each primary row (read only its checklist line and its `TASK_CONTEXT.md`
anchor — never the whole files):

1. Checklist row and anchor must agree on `skill` and `design_context`.
   On mismatch, stop task work and fix the metadata first.
2. Enforce the row's `requirements` and the anchor's requirements. If unmet:
   set the row to `blocked` with the exact missing artifact (row ID, file,
   version), note it in `STATE.md` Blockers, and exclude the row.
3. Skill gating — the `skill` column is the **sole** activation source:
   `none` → load no skill, even if the row touches GUI files or screenshots.
   `<skill>:<command>` → load that skill only now (after selection and
   requirements pass) and run the exact command; never approximate a skill
   result manually; never mark such a row done unless the command ran.
   A `+`-joined list (`<skillA>:<cmdA>+<skillB>:<cmdB>`) loads each named
   skill in the listed order, all gated on the same row selection and
   requirements pass — e.g. `verify-stack:walkthrough+gui-validation` runs
   the walkthrough procedure under the gui-validation input-safety protocol
   for its live-driving steps.
4. `design_context: required` → read the suite `DESIGN.md` once per session,
   then reuse it. `not-required` → do not read it merely because GUI paths
   appear. Load `PRODUCT.md` independently, only for product
   behavior/IA/terminology work.
5. Context-manifest check (advisory): before reading any file outside the
   package root that the selected rows do not explicitly cite, check the
   package `CONTEXT_INDEX.md` — the read must match its source map /
   external-context entries and must not fall under its "Do not read as V1
   context" section. Needed-but-denied file → do not read it as context;
   summarize the needed content into the row's `TASK_CONTEXT.md` anchor
   first (metadata fix before task work, as in step 1), then work from the
   anchor and note the event in the report's Notes. Hard-stop only if the
   needed content cannot be summarized.
6. Model recommendation — read the row's `model` column (falling back to the
   batch's `**Model:**` line when the row leaves it blank): `opus/sol` |
   `sonnet/terra` | `haiku/luna` (Claude tier / matching Codex tier, see
   plan-batch §3). If this invocation can select a model (e.g. an Agent-tool
   `model` param, or a session model switch), use the Claude tier when the
   executing worker is Claude Code and the Codex tier when it is Codex CLI.
   If the invocation has no model selection available, do not attempt one —
   just carry the recommendation into the report's Notes.
7. Track the selected rows with TodoWrite (one todo per row).

## 5. Implement

- Only the selected rows, in risk order H → M → L. No opportunistic fixes or
  refactors beyond what a row needs; route out-of-scope findings to the
  owning package or a new row proposal in the report — never duplicate.
- Read source narrowly: locate symbols with Grep, read windows around them,
  expand only as needed. Whole-file reads only for small files or when
  narrow reads fail.
- Smallest safe edit first. Run formatters only on touched files.
- Cross-suite resources marked read-only in the hard scope (e.g. generated
  clients, other packages' control files) are never edited from here.

## 6. Validate — a gate, not a formality

1. Run each row's `validation` column entry literally. A row whose named
   validation did not actually run is **not done** — leave it
   `needs-reverify` with a note, even if the code looks right.
2. Lint/type-check touched files (`ruff check`, `ruff format`, targeted
   `mypy` for Python; suite equivalents otherwise). Full test suites only
   when a row requires them.
3. Run the suite's standing invariant checks before closing the batch
   (e.g. offline startup smoke for PyApp).
4. Long output → write to the scratchpad, quote ≤20 relevant lines.
5. Evidence-producing rows write to `validation/<BATCH-KEY>_<slug>.md`
   with: steps, commands, honest pass/fail per criterion, and artifact
   paths. Failures become new row proposals, never silent inline fixes.

## 7. Close the batch

1. Update only the affected checklist row lines with Edit (match the exact
   `| <ID> | <status> |` prefix). Partial work → `blocked` or
   `needs-reverify` with a short reason; never `done`.
2. When all primary rows are resolved, append ` (done)` to the batch heading.
3. Append a dated continuation entry to `STATE.md` **only** for durable
   changes: new blockers, recorded decisions, deviations, deferred work.
   Routine completion is visible in the checklist and needs no entry.
4. **Commit** — one commit per batch: if the working tree was clean at start,
   stage the batch's changes and commit as
   `<batch-key>: <batch title>` with the row IDs in the body. If it was
   dirty at start, skip the commit and say so in the report.

## 8. Report and stop

```text
Batch: <key + title>
Rows: <ID status, ...>
Model: <recommended tier pair, and whether it was applied or only noted>
Changed: <paths, max 12; else "N files, see git diff --stat">
Validation: <command: pass/fail/skipped+reason, one line each>
Invariants: <e.g. offline smoke: pass>
Commit: <hash / skipped: reason>
Human action needed: <IDs + concrete action, or none>
Notes: <max 5 bullets>
```

On failure add `Failure: <one sentence>` and `Next: <one concrete action>`.
Then stop — never roll into the next batch in the same invocation.
