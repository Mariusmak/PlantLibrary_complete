# PlantLibrary — How to continue implementation

**Written:** 2026-08-04. **Verified against:** every `BATCH_PLAN.md`,
`TASK_CHECKLIST.md` and `STATE.md` in the repo, read directly (not from
[Todo.md](Todo.md), which is stale — see §2).

This document answers one question: *what do I run next, in what order, and
what is blocking me?* It does not re-plan the program — the batch packages
already contain the work. It sequences them.

---

## 1. Where the program actually stands

Two things changed since [Todo.md](Todo.md) was written, and both matter:

1. **The MVP is closed.** `SYS-B00..SYS-B16` in
   [System_Integration_MVP](PlantLibrary_Workspace/implementation/System_Integration_MVP/BATCH_PLAN.md)
   are all `done`. `SYS-B16` completed 2026-07-15;
   `validation/FINAL_ACCEPTANCE_PACKAGE.md` exists and the acceptance verdict
   is **"ready with accepted deviations"** (`VGAP-020`/`SD-GAP-008` deferred
   to V1 by product-owner decision). There is nothing left to run in that
   package. The Android MVP package is likewise terminal (`AN-B00..AN-B13`
   all done, gate `AN-MVP-GATE-01` = `done` since 2026-07-13).
2. **The repo was restructured.** Every batch package now lives under
   `<Suite>/implementation/…`. All paths in [Todo.md](Todo.md) point at files
   that no longer exist at those locations.

So the program is entirely in **MVP → V1** territory now.

### Package status (verified row-by-row)

| Package | Done | Next actionable batch | Not runnable yet |
|---|---|---|---|
| [Workspace / System_Integration_MVP](PlantLibrary_Workspace/implementation/System_Integration_MVP/BATCH_PLAN.md) | `SYS-B00..B16` — **all** | — closed | — |
| [Workspace / System_V1](PlantLibrary_Workspace/implementation/System_V1_Implementation/BATCH_PLAN.md) | `SY1-B00`, `SY1-B06` | `SY1-B01` remainder (`SY1-SEQ-01`) | `SY1-B02/B03/B04/B07/B05` — checkpoints + gates |
| [Server / System_V1](PlantLibrary_Server/implementation/System_V1_Implementation/BATCH_PLAN.md) | `SV1-B00` partial (**6 of 9 primary rows done** after §3.3; no `needs-reverify` left) | **`SV1-B00` remainder** ← critical path: `SV-SYNC-PUSH-02`, `SV-SYNC-REFDATA-01`, `SV-OPENAPI-01`; `SV1-B07` (independent) | `SV1-B01..B04` after `B00`; `SV1-B06` last |
| [SharedContracts / System_V1](PlantLibrary_SharedContracts/implementation/System_V1_Implementation/BATCH_PLAN.md) | `SC1-B01` | `SC1-B03` (independent, now unblocked) | `SC1-B00` ← `SV-OPENAPI-01`; `SC1-B02` ← `SV1-B01..B04` |
| [Dashboard / System_V1](PlantLibrary_Dashboard/implementation/System_V1_Implementation/BATCH_PLAN.md) | `WD1-B07` | `WD1-B00`, `WD1-B06`, `WD1-B08` (all independent) | `WD1-B01/B02` ← `SC1-B02`; `WD1-B05` release |
| [PyApp / System_V1](PlantLibrary_PyApp/implementation/System_V1_Implementation/BATCH_PLAN.md) | `PY1-B07`; `PY1-B02` partial (3 rows) | `PY1-B00`, `PY1-B06`, `PY1-B08` (all independent) | `PY1-B03` ← `SC1-B00/B02`; `PY1-B05` release |
| [Android / System_V1](PlantLibrary_AndroidApp/implementation/System_V1_Implementation/BATCH_PLAN.md) | `AN1-B00`, `AN1-B12`, `AN1-B14` | **`AN1-B01`, `AN1-B02`, `AN1-B04`..`AN1-B07` now actionable** (gate flipped, §3.1); `AN1-B11`, `AN1-B13` independent | `AN1-B03` (bar `AN-V1-ADD-04`) ← `SC1-B02`; `AN1-B09`/`AN1-B10`; 9 rows still `gated` |
| [Workspace / System_Design_Architecture](PlantLibrary_Workspace/implementation/System_Design_Architecture/BATCH_PLAN.md) | `SDA-BOOT-01` only | `SDA-B00` — **human decision gate**, §5.1 | `SDA-B01..B08` |

**One sentence:** the whole V1 program is waiting on **Server `SV1-B00` →
`SV-OPENAPI-01`**, which unblocks the contract wave, which unblocks every
client feature batch. Everything else currently runnable is independent
foundation work that can proceed in parallel.

---

## 2. Corrections to Todo.md

Do not follow [Todo.md](Todo.md) as an execution guide. It is a useful idea
backlog, but as a status document it is wrong on these points:

| Todo.md says | Reality |
|---|---|
| `PlantLibrary_AndroidApp/BATCH_PLAN.md` | Moved → [implementation/MVP/package/](PlantLibrary_AndroidApp/implementation/MVP/package/BATCH_PLAN.md) (terminal) and [implementation/System_V1_Implementation/](PlantLibrary_AndroidApp/implementation/System_V1_Implementation/BATCH_PLAN.md) |
| "Finish all Android batches" via `DRIVER_SCRIPT.md` | Android MVP batches are **all done**. Driver scripts are superseded — execution is via the `run-batch` skill (§6) |
| "Validate MVP" / `MVP_VALIDATION_SESSION_DRIVER.md` | MVP validation ran to completion (`SYS-B07..B16`); gaps are reconciled into `VGAP-*` → `SD-GAP-*` and routed to V1 backlogs |
| "Run `SY1-B06` first" | Already done (`SY1-VAL-01..03` all `done`) |
| "Complete/record `SYS-B16` first" | Done 2026-07-15 |
| "`SY1-B00` → `SY1-B01`" as pending | `SY1-B00` done 2026-07-16; `SY1-B01` is 2/3 done |
| "`AN1-B00` Luna" as pending | Done 2026-07-10 |
| "`AN1-B14` Sol" as pending | Done 2026-07-15 |

The **wave ordering** in Todo.md (§"Task chain for future implementations")
is still substantially correct and is the basis of §4 below — it has just
already advanced past waves 0 and most of 1.

---

## 3. Inconsistencies — ✅ ALL FIXED 2026-08-04

> **Status: done.** All three were fixed on 2026-08-04, plus a fourth found
> while fixing them (§3.4). The subsections below are kept as the record of
> what was wrong and what was changed. Nothing here is outstanding.

### 3.1 Android's V1 rows were stale-`gated` — ✅ fixed

28 Android V1 rows still carry status `gated` on the MVP evidence gate. That
gate **closed** on 2026-07-13 (root `AN-MVP-GATE-01` = `done`), and Workspace
`SY1-GATE-02` recorded it as closed on 2026-07-17. But
[Android's gate ledger](PlantLibrary_AndroidApp/implementation/System_V1_Implementation/validation/)
was written on 2026-07-10, while the gate was still open, and nothing has
flipped the rows since.

`run-batch` **never executes a `gated` row** — so as written, no Android
feature batch is selectable, and a session will report "nothing actionable"
even though `AN1-B01` is genuinely ready.

**Fixed.** Re-read all 15 root `AN-MVP-*` rows (all `done` except
`AN-MVP-MEDIA-01`, `deferred` with acceptance carried by
`AN-MVP-MEDIA-FIX-01`), rewrote
[the gate ledger](PlantLibrary_AndroidApp/implementation/System_V1_Implementation/validation/AN1-B00_gate_ledger.md)
with a 2026-07-10 vs 2026-08-04 comparison so the drift stays auditable, and
flipped **19 rows** `gated` → `todo`: `AN1-B01` (3), `AN1-B02` (3), `AN1-B04`
(4), `AN1-B05` (2), `AN1-B06` (3), `AN1-B07` (2), plus `AN-V1-ADD-04` and
`AN-V1-DS-04`.

**9 rows correctly stay `gated`**, each on a real non-MVP-gate dependency:
`AN-V1-ADD-01/-02/-03` (`SC1-B02`), `AN-V1-DS-01` (`SDA-B02`), `AN-V1-QA-01`
+ `AN-V1-REL-01/-02` (`AN1-B09`'s `AN1-B01..B07` batch gate), `AN-V1-SEC-01`
(human sign-off, §5.2), `AN-V1-ACC-01` (`AN1-B09` + `SY1-B04`).

`AN-V1-ADD-04` was flipped despite living in the `SC1-B02`-gated `AN1-B03`
because that batch's `Requires:` and `Blockers:` lines already record the
exception verbatim — no plan amendment was needed or made.

Status rule applied and written into the ledger: **`gated` means waiting on
something outside the row's own batch.** Intra-batch sequencing is expressed
by row order, because `run-batch` executes a batch's rows in order and never
selects a `gated` row — leaving successors `gated` would make every such batch
permanently half-executable.

### 3.2 `SUITE_HANDOFFS.md` was a 2026-07-09 snapshot — ✅ fixed

[SUITE_HANDOFFS.md](PlantLibrary_Workspace/implementation/System_V1_Implementation/SUITE_HANDOFFS.md)
is the documented "what to run next" index, but its status column still showed
Android MVP `AN-B10..B13` open, `SC1-B01` ready, `SY1-B00` ready, and
`SYS-B10..B16` open.

**Fixed.** Table rewritten from each package's `TASK_CHECKLIST.md` row
statuses (not from `STATE.md` prose); progress markers added to the run-order
section. Also dropped the "Driver to run" column for a single line naming the
`run-batch` skill — the column was still pointing sessions at the
`DRIVER_SCRIPT.md` procedural sections that were superseded on 2026-07-10.

### 3.3 Two Server rows were `needs-reverify` — ✅ fixed, both now `done`

The reason turned out to be different from what this plan first recorded.
Their validations had **already passed** on 2026-07-15, in the same
disposable-container run (15 passed / 47 passed) that closed
`SV-OPENAPI-VERSION-01`, `SV-SYNC-CONFLICT-01` and `SV-SYNC-IMAGE-01` — that
session just never revisited these two. The Python 3.12 blocker was real on
2026-07-14 but had been resolved a day later. So this was a bookkeeping
oversight, not an unmet criterion.

Re-ran on host Python 3.14.6 to confirm before closing: `pytest
tests/test_sync.py` → **15 passed**; `-k profile` → **2 passed, 13
deselected**; full `pytest` → **47 passed**. Docker was down and is not needed
— `tests/conftest.py` uses in-memory SQLite with `get_db` overridden, so the
default suite is stack-free.

Criteria were checked against the actual assertions rather than the pass
count: `test_pull_sees_task_note_and_media_changes` really does `POST` to the
direct `/events` route, assert `201`, and then assert `plant_event` comes back
from `/sync/pull` with `event_type == "watered"` — which is exactly
`SV-SYNC-EVENT-01`'s done-when.

**No `needs-reverify` row remains anywhere in the Server package.**

### 3.4 `pip install -e ".[test]"` never worked — ✅ fixed (found while fixing §3.3)

The test recipe documented in
[PlantLibrary_Server/CLAUDE.md](PlantLibrary_Server/CLAUDE.md) could not
complete: `pyproject.toml` declared no `[tool.setuptools]` package config, so
flat-layout auto-discovery aborted with *"Multiple top-level packages
discovered in a flat-layout: ['app', 'deploy', 'openapi', 'implementation']"*.
The 2026-07-15 session hit this, recorded it, and worked around it with
`PYTHONPATH=/srv` instead of fixing it.

**Fixed** by adding to `pyproject.toml`:

```toml
[tool.setuptools.packages.find]
include = ["app*"]
```

This is the one **product-repo** change in this pass (build metadata only, no
application code). Verified by running the documented recipe end-to-end:
install exit 0, pytest 9.1.1 available, 47 tests pass. No `PYTHONPATH`
workaround needed from here on.

---

## 4. Execution plan

Model roles as you defined them: **Sol** = cross-system / security / sync /
contracts / release; **Terra** = normal scoped feature + test work; **Luna** =
reconciliation, docs, checkpoints.

### Wave A — unblock everything (do first, strictly in order)

| # | Run | Model | Why |
|---|---|---|---|
| A1 | `/run-batch Server SV1-B00` | **Sol** | The system's critical path. Contains `SV-OPENAPI-01`, the export that gates the entire contract wave. Also carries `SV-SYNC-PUSH-02`, `SV-SYNC-REFDATA-01` (the deferred `SD-GAP-008` work), and clears the two `needs-reverify` rows from §3.3. |
| A2 | `/run-batch SharedContracts SC1-B00` | **Sol** | Regen wave 1. Nothing on any client may consume the new server behavior before this lands. |
| A3 | `/run-batch Workspace SY1-B01` | **Luna** | Closes `SY1-SEQ-01` — records that the contract loop completed. Cheap, and it keeps the handoff index honest. |

`SV1-B00` is large. If it does not close in one session, it is legitimate to
stop after `SV-OPENAPI-01` is `done` and start A2 — that single row is the
only hard prerequisite for `SC1-B00`.

### Wave B — independent foundations (run in parallel with Wave A)

None of these touch the contract path. They are safe to interleave, and
several were unblocked by `SY1-B06` completing (all the `*-DOC-01` rows were
waiting on `SY1-VAL-01`, which is now `done`).

| Run | Model | Contents |
|---|---|---|
| `/run-batch Server SV1-B07` | Terra | `pytest -m stack` live-stack tier + suite CLAUDE.md/AGENTS.md |
| `/run-batch SharedContracts SC1-B03` | Luna | Suite CLAUDE.md + AGENTS.md validation section |
| `/run-batch Dashboard WD1-B00` | Terra | **Live browser walkthrough evidence** — needs the Docker stack up |
| `/run-batch Dashboard WD1-B06` | Terra | Design tokens 1.2.0 adoption (`WD-V1-DS-06`) |
| `/run-batch Dashboard WD1-B08` | Terra | Playwright e2e layer (extend the existing `e2e/`, do not scaffold a new one) |
| `/run-batch PyApp PY1-B00` | Terra | **Live OIDC/sync walkthrough evidence** — needs the stack + editable client install |
| `/run-batch PyApp PY1-B06` | Terra | Design tokens 1.2.0 adoption (`PY-V1-DS-03`) |
| `/run-batch PyApp PY1-B08` | Terra | Headless app-e2e tier + docs |
| `/run-batch AndroidApp AN1-B11` | Terra | Design tokens 1.2.0 adoption (`AN-V1-DS-05`) |
| `/run-batch AndroidApp AN1-B13` | Terra | **Android has zero test sources today** — this creates them, plus the headless-AVD script |

The three tokens-1.2.0 rows (`WD-V1-DS-06`, `AN-V1-DS-05`, `PY-V1-DS-03`) are
the adoption work your memory flags as pending. Until they run, all three
clients are knowingly on 1.1.0 token values — recorded drift, not a defect.

### Wave C — API expansion → contract wave 2

Strictly sequential. Do not parallelize `SV1-B02`/`SV1-B04` unless you have
two independent sessions and are willing to reconcile a shared OpenAPI export.

```
SV1-B01 (Terra) → SV1-B02 (Sol) → SV1-B04 (Terra) → SV1-B03 (Sol)
      → SC1-B02 (Sol, regen wave 2)   → SY1-B02 (Terra, checkpoint)
```

`SC1-B02` is the gate that unblocks the *blocked* client rows: Dashboard's
eight `WD-V1-QUERY-*`/`WD-V1-AUTH-01`, PyApp's `PY-V1-CLIENT-01`/
`PY-V1-TAGS-01`/`PY-V1-REFDATA-01`, and Android's `AN1-B03` family.

### Wave D — client V1 capability

After `SC1-B02`, all three clients open up. These are independent of each
other and can run in parallel sessions:

- **Dashboard:** `WD1-B01` (Terra) → `WD1-B02` (Terra)
- **PyApp:** `PY1-B02` remainder (Terra) → `PY1-B03` (Sol)
- **Android:** `AN1-B01` → `B02` → `B03` (Sol) → `B04` → `B05` → `B06` (Sol) → `B07`

Android is the longest chain by far (7 batches, ~28 rows). If you want V1
sooner, start Android's `AN1-B01`/`AN1-B02` as soon as §3.1's gate flip lands
— neither needs `SC1-B02`, only the MVP gate.

### Wave E — design track (optional, must not block V1)

`SDA-B00` is a human decision gate (§5.1). It was explicitly de-gated from V1
by decision D-V1-11 — **nothing waits on it**. If you resolve the five
decisions, run `SDA-B01..B08`; then, and only if `SDA-B02` lands in time, the
opportunistic token-switch rows `WD1-B04` / `PY1-B04` / `AN1-B08`. Record the
taken-or-deferred outcome with `SY1-B03` (Luna).

### Wave F — harden and release

```
SV1-B06 (Sol; SV-V1-SEC-01 /security-review runs LAST in this batch)
WD1-B05 (Sol) · PY1-B05 (Sol) · AN1-B09 (Sol)
        → AN1-B10 (Sol) scheduled jointly with SY1-B04 (Sol, system V1 smoke)
        → SY1-B07 (Sol, security gate — verdict must be `pass`)
        → SY1-B05 (Sol, release ledger + acceptance package)
```

Note the ordering trap: despite the numbering, **`SY1-B07` runs before
`SY1-B05`** (same precedent as `SY1-B06`, numbered last and run first).
`/security-review` must run from the **Server repo**, never from the
workspace repo — it reviews a branch diff, and the workspace holds only
planning docs and submodule gitlinks.

---

## 5. Decisions only you can make

These are the genuine blockers that no agent session can resolve. Two of them
sit on the release path.

### 5.1 The five `SDA-DEC-*` design decisions (not release-blocking)

`SDA-B00` cannot close and `SDA-B01/B02/B06/B07` cannot start until you record
choices for these. The proposal's own recommendations are in the
[SDA STATE.md](PlantLibrary_Workspace/implementation/System_Design_Architecture/STATE.md):

| ID | Decision | Proposal recommends |
|---|---|---|
| `SDA-DEC-01` | SharedContracts folder layout | sibling folders (no `design/` restructure) |
| `SDA-DEC-02` | PyApp token inversion mode | fully generated tokens |
| `SDA-DEC-03` | Parity screenshot tooling | per-platform native capture, `<page_id>__<platform>__<light\|dark>.png` |
| `SDA-DEC-04` | Shared icon set | Material Symbols |
| `SDA-DEC-05` | Android font policy | system font / Roboto as accepted deviation |

Accepting all five as recommended is a five-minute decision and unblocks the
whole design track. Declining to decide is also fine — the track is
non-gating.

### 5.2 Two named security sign-offs (release-blocking)

Rule `SYS-QUAL-GAP-004`: no security-class finding may be accepted or deferred
without a **named human sign-off**. Two rows depend on you personally:

- `AN-V1-SEC-01` (Android): keep the DataStore token-storage deviation, or
  implement Keystore. Without your sign-off the row stays `blocked` and
  `AN1-B09` cannot close — which blocks `AN1-B10` → `SY1-B04` → release.
- `SV-V1-SEC-01` → `SY1-B07`: every `/security-review` finding must land as
  fixed / accepted-with-rationale / deferred-with-register-entry, and the
  accepted and deferred ones need your name on them.

### 5.3 Release-scope confirmation

`VGAP-020` / `SD-GAP-008` (PyApp `data_source`/tags first-sync) was deferred
out of MVP by you on 2026-07-15 **into V1 scope**. It is now real V1 work
carried by `SV-SYNC-REFDATA-01` (Server), `SC1-B00` (contracts) and
`PY-V1-REFDATA-01` (PyApp). Confirm that's still what you want before `SV1-B00`
runs, since it materially sizes that batch.

---

## 6. How to run a batch

One batch per session. The `DRIVER_SCRIPT.md` files still exist in every
package but their **procedural sections are superseded** — use the skill.

```
/run-batch <Suite> <BATCH-KEY>        e.g.  /run-batch Server SV1-B00
/run-batch <Suite>                    picks the next actionable batch
```

Binding rules the skill enforces, worth knowing before you start:

- **Never execute `gated` or `deferred` rows.** The session reports the human
  action needed instead. (This is exactly what §3.1 trips over.)
- Row status in `TASK_CHECKLIST.md` is the single source of truth. A `(done)`
  heading is a convenience marker only. `_ACT_STATE.md` is deprecated.
- Every row's **named validation must actually run**. Per
  [CLAUDE.md](CLAUDE.md), anything spanning more than one module follows
  `real-stack-testing`, and `validate-real-stack` delegates the run to the
  cheaper worker agent — the implementing session still owns the fixes.
- Skills fire per-row from the checklist `skill` column: `verify-stack` for
  the Docker stack, `android-validation` for emulator work, `webapp-testing`
  for the Dashboard, `gui-validation` for PySide6, `sync-contracts` for the
  contract wave, `design-adoption` before touching any rendered surface,
  `test-driven-development` on the 13 failing-test-first Server rows.
- When a row's validation fails unexpectedly, `systematic-debugging` is the
  failure-time technique — root-cause before proposing a fix.

**Environment gotchas** already paid for, don't rediscover them:

- Docker is Docker Desktop's `desktop-linux` context. Use it explicitly.
- The running `api` container has Python 3.14.6 but **no pytest**. For tests
  use a disposable `python:3.14-slim` container (recipe in
  [PlantLibrary_Server/CLAUDE.md](PlantLibrary_Server/CLAUDE.md)).
- All six suites are git submodules, all currently on `main`, all clean. Batch
  commits belong in the suite repo; the workspace repo carries the gitlink
  bump.
- The desktop GUI sessions must never assume window focus — a locked session
  silently swallowed input twice during MVP validation.

---

## 7. Work in Todo.md that has no batch row yet

These are real items from your backlog that the packages do **not** currently
cover. Each needs a `plan-batch` pass before it can be executed. Listed in the
order I'd add them:

| Item | Where it belongs | Note |
|---|---|---|
| **No cleartext HTTP on Android; plan HTTPS** | Android `AN1-B09` (or a new row alongside `AN-V1-SEC-01`) | Verified: **zero** rows anywhere mention cleartext/HTTPS/TLS. This is a genuine hole on a release-path security batch. |
| **Server setup guide ("Ausführliche Anleitung")** | Server `SV1-B06`, next to `SV-OPS-INSTALL-01` | `SV-OPS-INSTALL-01` verifies a one-command install; it does not author an operator guide. |
| **Gradle 9 deprecation warnings** | Android `AN1-B09` | Not tracked anywhere. Build works today; this is forward-compat debt. |
| **Server-side data enrichment proposal** | Server — partially covered by `SV-V1-SEARCH-01`, `SV-V1-PROVIDER-01`, `SV-V1-JOBS-01`, `SV-V1-REVIEW-01` | The *enrichment-in-the-creation-flow* design you describe is broader than those rows. Write the proposal first, then plan rows. |
| **Fable 5 business/GTM proposal follow-through** | `fable5_business_proposal/` (BDEV-01..06, authored 2026-07-11) | Nothing approved yet. Independent of V1 execution. |
| **Cleaning up old MVP folders** | Workspace | The MVP/V1 split already happened (restructure D1–D10). Deleting MVP packages would destroy the evidence chain the V1 registers cite — I'd keep them read-only, not remove them. |

`fewer-permission-prompts` is worth running once before Wave C — with this
many batch sessions ahead, the prompt reduction compounds.

---

## 8. The short version

0. ~~Fix the inconsistencies (§3)~~ ✅ **done 2026-08-04** — Android's gate
   flipped (19 rows actionable), the handoff index refreshed, both Server
   `needs-reverify` rows closed, and the broken Server test recipe fixed.
1. Run **`/run-batch Server SV1-B00`** (Sol). This is the critical path, and
   `SV-OPENAPI-01` is its highest-leverage row.
2. In parallel, work the Wave B independent list — especially the three
   tokens-1.2.0 adoption batches and Android's missing test foundation.
   **Android `AN1-B01`/`AN1-B02` are now runnable too** and don't wait on the
   contract wave.
3. The moment `SV-OPENAPI-01` is `done`, run **`/run-batch SharedContracts
   SC1-B00`** (Sol).
4. Decide the five `SDA-DEC-*` items (§5.1) whenever convenient — nothing
   waits on them.
5. Then Wave C (API expansion → `SC1-B02`), which opens all three clients at
   once.
