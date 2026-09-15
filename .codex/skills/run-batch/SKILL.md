---
name: run-batch
description: Execute one implementation batch from a batch package (BATCH_PLAN.md + TASK_CHECKLIST.md + TASK_CONTEXT.md). Selects the next actionable batch or the one named in the argument, enforces requirements, implements only the selected rows, runs each row's named validation, records evidence, updates row statuses, proposes the exact batch commit to the orchestrator, and prints a compact report. Use for "run the next batch", "execute PY1-B02", "continue the V1 implementation" in any suite.
user-invocable: true
argument-hint: "[suite-or-package-path] [batch-key]"
---

Execute exactly one batch per invocation, then stop. Optimize for low context:
narrow reads, small edits, compact output.

## 1. Locate the package

1. If the argument names a path, use it. If it names a known PlantLibrary
   suite shorthand (`PyApp`, `Server`, `AndroidApp`, `Dashboard`,
   `SharedContracts`, `Workspace`), glob
   `PlantLibrary_<Suite>/implementation/*/BATCH_PLAN.md`. Otherwise — no
   argument, or an argument that names neither a path nor a known PlantLibrary
   suite — glob `implementation/*/BATCH_PLAN.md` under the current working
   directory; this is the general case for any project using this package
   format (matches plan-batch's own locator). Suite-name inference is
   PlantLibrary-specific and must not be assumed for other projects.
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
3. Gate-authorized deviations — if `STATE.md` or the row's anchor records an
   explicit operator gate decision (a `D-<date>-<nn>` id) authorizing a named
   deviation for this batch (exact path + action), treat that authorization as
   a satisfied requirement: carry the decision id into the report's Notes and
   never re-request the same authorization during the attempt. Absent such a
   recorded id, out-of-scope needs stay routed per §5 — this item grants
   nothing new; it only stops re-litigating what a gate already granted.
4. Skill gating — the `skill` column is the **sole** activation source:
   `none` → load no skill, even if the row touches GUI files or screenshots.
   `<skill>:<command>` → load that skill only now (after selection and
   requirements pass) and run the exact command; never approximate a skill
   result manually; never mark such a row done unless the command ran.
   A `+`-joined list (`<skillA>:<cmdA>+<skillB>:<cmdB>`) loads each named
   skill in the listed order, all gated on the same row selection and
   requirements pass — e.g. `verify-stack:walkthrough+gui-validation` runs
   the walkthrough procedure under the gui-validation input-safety protocol
   for its live-driving steps.
   `validate-real-stack` is execution plumbing owned by
   `real-stack-testing`, not an additional row skill. Invoke it only after
   implementing a selected `real-stack-testing` row.
5. `design_context: required` → read the suite `DESIGN.md` once per session,
   then reuse it. `not-required` → do not read it merely because GUI paths
   appear. Load `PRODUCT.md` independently, only for product
   behavior/IA/terminology work.
6. Context-manifest check (advisory): before reading any file outside the
   package root that the selected rows do not explicitly cite, check the
   package `CONTEXT_INDEX.md` — the read must match its source map /
   external-context entries and must not fall under its "Do not read as V1
   context" section. Needed-but-denied file → do not read it as context;
   summarize the needed content into the row's `TASK_CONTEXT.md` anchor
   first (metadata fix before task work, as in step 1), then work from the
   anchor and note the event in the report's Notes. Hard-stop only if the
   needed content cannot be summarized.
7. Model recommendation — read the row's `model` column (falling back to the
   batch's `**Model:**` line when the row leaves it blank): `opus/sol` |
   `sonnet/terra` | `haiku/luna` (Claude tier / matching Codex tier, see
   plan-batch §3). If this invocation can select a model (e.g. an Agent-tool
   `model` param, or a session model switch), use the Claude tier when the
   executing worker is Claude Code and the Codex tier when it is Codex CLI.
   If the invocation has no model selection available, do not attempt one —
   just carry the recommendation into the report's Notes.
   AM-27: when this invocation can spawn agents, individual rows may be
   delegated to in-session subagents at the row's recommended tier (Agent-tool
   `model` param); the parent session remains the single accountable executor
   for the whole batch; a row's named validation is never delegated to a
   background agent; the report's `Model:` line lists the applied model per
   row. The no-model-selection fallback above is unchanged — Codex runs this
   text unchanged too.
8. Track the selected rows with TodoWrite (one todo per row).

## 5. Implement

- Only the selected rows, in risk order H → M → L. No opportunistic fixes or
  refactors beyond what a row needs; route out-of-scope findings to the
  owning package or a new row proposal in the report — never duplicate.
- Read source narrowly: locate symbols with Grep, read windows around them,
  expand only as needed. Whole-file reads only for small files or when
  narrow reads fail.
- Large authority documents (e.g. a package's normative proposal) follow the
  same rule: if this invocation can spawn agents, delegate section lookups to
  the workspace's read-only section-reader agent where one exists (e.g.
  Conductor's `v5-section-reader`) and consume only its quoted windows; if it
  cannot, use the document's section map and bounded windows per the package
  `CONTEXT_INDEX.md`.
- Smallest safe edit first. Run formatters only on touched files.
- For a row changing a constructor, protocol, shared seam, or mandatory
  preflight, before its first test run locate constructors/implementers and
  consuming fixtures with narrow searches; write the complete relative-path and
  symbol blast-radius inventory to evidence; migrate it as one mechanical pass;
  compare migrated and expected counts; then run one scoped matrix. Do not use
  repeated pytest failures as discovery. If this invocation can spawn agents,
  the inventory search may be delegated to a read-only exploration agent
  returning relative paths, symbols, and per-path counts; the executor still
  writes the evidence inventory and performs the migration itself. If it
  cannot, run the narrow searches inline.
- Before reading implementation or diagnostic output, locate named symbols or
  headings with narrow `rg` queries, then read bounded windows and expand only
  when needed. Prefer a known failing node ID to broad test searches; after the
  first diagnostic pytest failure, run only that node with `--tb=line`.
- Inspect unknown return objects with their type, bounded key names, and length;
  never serialize a whole unknown object merely to discover its shape. Record an
  explicit reason in the batch Notes or evidence for every model-visible tool
  result above approximately 8,000 tokens.
- Cross-suite resources marked read-only in the hard scope (e.g. generated
  clients, other packages' control files) are never edited from here.

## 6. Validate — a gate, not a formality

0. **Foreground rule — no detached work, ever.** Every validation, regression,
   lint, and closeout command runs in the foreground of the turn that launched
   it: never with a background/detached flag, never behind `start`, `&`,
   `Start-Process`, or a nohup equivalent, and never through a driver script
   that returns before its children do. A batch worker may be a headless agent
   CLI whose process tree is terminated with the session, so a backgrounded
   command is not slow — it is *lost*, and the turn that ends while "waiting for
   it" reports work that will never finish. Ending a turn to wait for anything
   is always wrong here. Work too large for one turn is made **resumable**
   (item 6), never detached. Validation commands are run in the foreground and
   are awaited; long validations are the orchestrator's job (item 1). An
   attempt that ends its turn with background work still running is
   classified a protocol failure (AM-17).
1. **Long validation rule.** When a command is expected to take more than 60
   seconds, launch it exactly once through
   `python scripts/harness/run_validation.py --artifact <full-output-artifact> --max-seconds <declared-budget> -- <command>`.
   Set the shell timeout to the declared budget plus teardown headroom, and set
   the outer tool yield at least as long as that deadline. Never issue a wait,
   polling, retry, or status-loop call for that command: retain complete output
   only in the artifact and admit only the runner's compact summary to model
   context. If the declared budget cannot fit the applicable runtime ceiling
   (the runner ceiling is 540 seconds), split the validation by scope before
   launch.
2. For each selected `real-stack-testing` row, invoke `validate-real-stack`
   after implementation. Pass only the row ID, exact named command, acceptance
   criteria, touched paths, and a full-output artifact path under the package
   evidence or scratch directory. Wait for the cheaper validation worker's
   compact result. The parent agent owns fixes, evidence prose, row status,
   and completion. If the worker is unavailable, run inline and report the
   fallback.
3. Run each row's `validation` column entry literally. Delegating the command
   still counts as running it; a row whose named
   validation did not actually run is **not done** — leave it
   `needs-reverify` with a note, even if the code looks right.
4. Lint/type-check touched files (`ruff check`, `ruff format`, targeted
   `mypy` for Python; suite equivalents otherwise). A repository-wide suite is
   authorized only when the selected checklist row's `validation` cell
   literally names it; no closeout convenience run may widen scope.
5. Before materializing the pytest-only selector, account for every touched
   path. A path may be classified `direct-validation-only` and omitted only
   when it is outside the suite's shipped-product paths and pytest collection;
   the selected row's `file(s)` cell names that exact path; a literal
   non-pytest validation for that row directly covers the path and has already
   exited 0 in the current attempt; and row evidence records the exact path,
   command, exit, and reason no pytest consumer exists. Never omit `src/**`,
   `tests/**`, a `test_*.py`, or a `conftest.py`; never infer coverage from a
   broad command without the exact row declaration. Any uncertainty remains in
   the selector and fails closed.
5a. **Standing legs before the first immutable generation.** Before the first
   `--plan-chunks` of this batch, in this order and all in the foreground:
   (i) the lagged duration-history merge — `python
   scripts/harness/regression_scope.py --merge-history-from-ledger .tmp/chunks`
   (best-effort: absent or reclaimed ledgers merge nothing; a changed
   `scripts/harness/duration_history.json` is a touched path of this batch and
   is committed with it); (ii) `ruff check` and `ruff format --check` on the
   touched files (item 4); (iii) the acceptance registries — `python
   scripts/harness/run_validation.py --artifact <scratch>/acceptance.txt
   --max-seconds 300 --prepare-dir <scratch> -- python -m pytest -q
   -p no:randomly --basetemp=<scratch>/bt tests/acceptance`; (iv) the
   pre-closeout probe — `python scripts/harness/regression_scope.py
   --probe-targets <touched paths> --max-targets <cap> --duration-history
   scripts/harness/duration_history.json --artifact <scratch>/probe.json`
   (omit `--duration-history` when the file is absent) and its one emitted
   `run_validation.py` argv, run once. The probe is a cheap **mutable** pass:
   fix what it shows, re-run the legs, and only then materialize the matrix. It
   is never cited as evidence and never replaces item 6. **After the matrix
   launches, only evidence, row status and prose edits are permitted; any edit
   to a touched path — a rename included — is a stated new generation** (AM-19
   §7.15 item 4: the matrix attests the tree whose digest it opened with), named
   as such in the report with its generation number.
6. For normal batch close, collect the batch's touched repository-relative
   paths and materialize the deterministic scoped matrix once with `python
   scripts/harness/regression_scope.py <paths> --format json --max-targets
   <cap> --artifact <scope-json>`. `<cap>` is derived, never a model-typed
   number and never omitted: it is `validation.max_scope_targets` read from the
   active `config.yaml`, falling back to the shipped `config.example.yaml` when
   that file has no `validation:` section. Omitting the flag is the defect that
   parked `CD2-B140`–`CD2-B142` and again `CD2-B230`: the harness falls back to
   its own `DEFAULT_MAX_TARGETS`, so a deployment that raised the configured cap
   still parks on `scope cap exceeded: N targets exceeds 30` — a bound nothing
   else in the system uses. `ValidationPlanner.scope()` already passes the
   configured value on the coordinator-planned route; this is the same property
   on the worker-planned one. Read the cap, state it in the row evidence beside
   the target count, and never substitute a literal. Before any pytest launch,
   plan it with `--plan-chunks
   <scope-json> --chunk-artifact-dir <dir> --chunk-basetemp-root <dir>
   --max-seconds 300 --artifact <chunk-manifest>` and verify its exact-coverage
   invariant. Add `--duration-history scripts/harness/duration_history.json`
   when that file exists in the repository: it packs chunks to a time budget
   instead of flat groups of ten, which is what keeps one slow file from
   setting the floor. Omit the flag when the file is absent — the harness fails
   closed on an unreadable history rather than silently packing flat.
   Point `--chunk-artifact-dir` at a gitignored scratch path (e.g.
   `.tmp/chunks/<run-id>`), never at the persisted `validation/` evidence tree:
   the per-chunk raw pytest text is regenerable scratch, not evidence — only
   the chunk manifest, `scope.json`, and `classification.json` are kept. The
   complete, disjoint manifest is immutable after that point:
   each planned argv runs sequentially in manifest order exactly once through
   `run_validation.py`; never retry, exclude, split, merge, reorder, or consult
   pytest cache. A nonzero test result does not skip a remaining precomputed
   chunk, because aggregate classification requires every observation; timeout,
   infrastructure failure, missing artifact, or incomplete launch is blocking.
   Execute the manifest only with `python scripts/harness/run_chunks.py
   --manifest <chunk-manifest> --ledger <scratch>/chunk-ledger.jsonl
   --envelope-seconds <budget>`; never hand-roll a driver and never background
   one. AM-44 Clause 7 (§7.14 item 10, AC131/AC132): `<budget>` is derived,
   never a model-typed number — `envelope-seconds := foreground_ceiling_s −
   envelope_grace_s` (`validation.foreground_ceiling_s`/`envelope_grace_s`,
   §12.1; `run_chunks.py` mirrors the same defaults and refuses an
   over-ceiling `--envelope-seconds` at exit 2, naming the correct value,
   before any chunk runs). Emit the tool timeout and the envelope as one unit
   — timeout ≥ envelope and ≤ the tool's own maximum — never two
   independently-typed numbers: for this skill's 600 s Bash tool, that is
   `--envelope-seconds 480` with the Bash tool's own `timeout: 600000`.
   That runner is the resumable form item 0 requires: it runs one chunk at
   a time in the foreground, records each outcome durably before the next
   starts, and when the remaining envelope cannot cover the next chunk's ceiling
   it stops **at a chunk boundary** and exits 3. Exit 3 is neither a failure
   nor a human action — it is the ordinary loop iteration: re-run the printed
   `resume:` command verbatim, and keep re-running it until it exits 0 or 1;
   never re-plan, never repartition mid-ledger, never background the runner.
   Each invocation continues at the first unrun chunk and never repeats a
   recorded one. The only way to stop a live run is `run_chunks.py --stop`
   (same `--manifest`/`--ledger`), which resolves the live run from its lock
   file and terminates exactly that process tree, leaving the ledger
   resumable — never a background kill, never one that selects by image or
   filter. Only if the turn genuinely cannot hold the remaining
   chunks: leave the affected rows `needs-reverify`, put the exact resume
   command and the recorded chunk count in the report, and let the next attempt
   continue the same ledger. Never end a turn describing a run as still in
   progress.
   **Serial where it is paid.** `validation.parallel_ordinary` and `parallel_gui_real`
   (§12.1) are honoured only by the in-process `ValidationRunner` on the coordinator
   route. `run_chunks.py` runs one chunk at a time by AM-44 Clause 7 (AC131/AC132), so a
   worker-route or out-of-band closeout is sized for **serial** wall-clock — the sum of
   the manifest's chunk estimates — never for the dials; no flag turns the runner
   concurrent, and a hand-rolled parallel driver is never a substitute.
   After every launch, resolve the ledger with `--active-package <package>`:
   prefer that package's ledger when present, otherwise select exactly one
   valid central ledger capable of the active route. Never fabricate a
   package-local ledger. Classify all chunk artifacts together once using
   `--classify-pytest-output <artifacts...> --active-package <package>` so only
   active-route records match or become stale. Report clean `pass` or exact
   `pass-with-ledger` with every owner; new, changed-signature, malformed,
   ownerless, ambiguous, or applicable resolved-stale cases are blocking. This
   scoped closeout is additional to, never a replacement for, named row
   validations.
   Both `regression_scope.py` invocations of this item — the scope and
   `--plan-chunks` — use `--summary-only` with `--artifact`; the full JSON lives
   only in the artifact. Record the two SHA-256 digests the summaries print
   (scope and manifest) in the row evidence, so the immutability claim is
   checkable without paging either file.
7. Do not run speculative plain-suite, `-x`, `--ignore`, exclude-known,
   polling, or retry variants. Do not repartition a manifest after its first
   launch; a plan that cannot fit its 300-second chunk ceiling is blocking.
8. Run the suite's standing invariant checks before closing the batch
   (e.g. offline startup smoke for PyApp). On a suite whose whole-suite run
   cannot fit the runner ceiling (`run_validation.py`'s 540 s), the
   standing-invariant leg **is** item 5a plus the scoped matrix of item 6 —
   never a whole-suite `pytest` under the ceiling; the bounded whole-suite form
   is `CD-V2-HRN-13`'s and is not improvised here.
9. Long output → write to the scratchpad, quote ≤20 relevant lines.
10. Evidence-producing rows write to `validation/<BATCH-KEY>_<slug>.md`
    with: steps, commands, honest pass/fail per criterion, and artifact
    paths. Failures become new row proposals, never silent inline fixes.
    Any row that instead writes a new file into the package's `planning/`,
    `proposal/`, or `handovers/` folder (e.g. an incident write-up) names it
    `<TYPE>_<topic>_<YYYY-MM-DD>.md` and adds it to that folder's `INDEX.md`
    in the same commit (see CLAUDE.md's "Deliverable naming" section).

## 7. Close the batch

Before completion, inspect `git diff --stat` first and then only focused hunks
for the touched paths. If this invocation can spawn agents, also pass the
batch key, each selected row's done-when, the touched paths, and the package
scope file to a read-only closeout-review agent (e.g.
`batch-closeout-reviewer`) and resolve every confirmed finding it returns —
fix in-batch or record it as a blocker/new-row proposal — before proposing the commit.
If it cannot, this inline diff inspection against the same criteria is the
full review.

1. Update only the affected checklist row lines with Edit (match the exact
   `| <ID> | <status> |` prefix). Partial work → `blocked` or
   `needs-reverify` with a short reason; never `done`.
2. When all primary rows are resolved, append ` (done)` to the batch heading.
3. Append a dated continuation entry to `STATE.md` **only** for durable
   changes: new blockers, recorded decisions, deviations, deferred work.
   Routine completion is visible in the checklist and needs no entry.
4. **Propose the commit — never mutate Git.** Read-only Git inspection is
   allowed. Do not run `git add`, `git commit`, `git push`, `git reset`, or any
   other Git-mutating command. Preserve foreign paths and propose only the
   batch's validated touched paths. When paths changed, report exactly
   `Commit: proposed for orchestrator` and form one canonical JSON object with
   exactly these sorted keys: `batch_key`, `message`, `paths`, `reason`,
   `row_attribution`, `status`, `version`. Use version integer `1`, the selected
   batch key, status `proposed`, null reason, subject
   `<batch-key>: <batch title>`, a sorted unique non-empty normalized
   repository-relative path array, and sorted selected-row keys whose sorted
   unique arrays union exactly to `paths`. Attribute each path to at least one
   selected row; package `TASK_CHECKLIST.md`, `STATE.md`, and package
   `validation/**` closeout paths may be attributed to any selected row. Emit
   UTF-8 canonical JSON equivalent to `json.dumps(value, ensure_ascii=False,
   sort_keys=True, separators=(",", ":"))`. Bounds: payload 65,536 UTF-8 bytes;
   512 paths; 512 UTF-8 bytes per path; 64 rows; 200 UTF-8 bytes for the
   non-empty single-line subject. Paths contain no absolute, drive, UNC,
   device, rooted, empty, `.`, `..`, or `.git` component. If the batch is
   already complete and changed nothing, report `Commit: skipped (no changes)`
   and emit no proposal.

## 8. Report and stop

```text
Batch: <key + title>
Rows: <ID status, ...>
Model: <parent recommended tier pair + applied/noted; validation worker tier/fallback>
Changed: <paths, max 12; else "N files, see git diff --stat">
Validation: <command: pass/fail/skipped+reason, one line each>
Invariants: <e.g. offline smoke: pass>
Commit: <proposed for orchestrator / skipped (no changes)>
Human action needed: <IDs + concrete action, or none>
Notes: <max 5 bullets>
```

When paths changed, append exactly one line immediately after the human report
and immediately before any caller-required three-line Conductor footer:

```text
CONDUCTOR_BATCH_COMMIT_PROPOSAL: <canonical-json>
```

On failure add `Failure: <one sentence>` and `Next: <one concrete action>`.

<!-- Telegram notify block: prose is intentionally near-duplicated in
     plan-batch/SKILL.md §8 (notice vs. report artifact, "planning result" vs.
     "batch failure" wording differ on purpose). Keep the enqueue-only
     contract and mode restrictions in sync across both when either changes. -->

**Notify.** Best-effort, never blocks: pipe the report text to
`python scripts/notify_telegram.py --enqueue` (repo root). This command performs
only an atomic local outbox write; it does not access Credential Manager, the
network, Telegram, or any other external system, so it needs no external-action
authorization or host/sandbox escalation. A user-installed Windows background
task independently drains the outbox, reads the token from Credential Manager,
sends the message, and retains transient failures for retry.

The run-batch agent must use `--enqueue`; never invoke this script's direct-send,
`--drain-once`, or `--watch` modes. On exit 0 report `Notification: queued for
local Telegram notifier` — do not claim synchronous delivery. On non-zero note
the local enqueue failure and continue; notification is never a batch failure.

Then stop — never roll into the next batch in the same invocation.
