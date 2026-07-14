# PlantLibrary Full Implementation Update Recommendation

## Executive summary

The current workspace has a solid methodology and an MVP-oriented implementation package, but it is not yet the plan for the final product. The canonical system description under `PlantLibrary_Workspace/system_description/PlantLibrary_System_Description/` is the right source of truth. The existing `PlantLibrary_Workspace/implementation/System_Integration_MVP/` package should be treated as an MVP coordination package, not stretched indefinitely into the final-state roadmap.

Recommended next move:

1. Create a new system-level package under `PlantLibrary_Workspace/implementation/System_Full_Implementation/`.
2. Use it to derive and coordinate full-system work from the canonical system description and the old Python app capability inventory.
3. Put every product-code task into the owning suite package:
   - Android-only work goes into `PlantLibrary_AndroidApp/implementation/Android_V1_Companion_Completion/` or appended Android batches.
   - Dashboard-only work goes into `PlantLibrary_Dashboard/implementation/Dashboard_Live_Data_Completion/` or appended Dashboard batches.
   - Server-only work goes into `PlantLibrary_Server/implementation/Server_V1_Completion/` or appended Server batches.
   - SharedContracts-only work goes into `PlantLibrary_SharedContracts/implementation/Contract_V1_Completion/` or appended SharedContracts batches.
   - PyApp sync work continues in `PlantLibrary_PyApp/Improvements/Python_Client_Sync/`.
4. Keep `PlantLibrary_Workspace` responsible for coordination, requirement coverage, cross-suite sequencing, smoke tests, known gaps, and release readiness only.

## Current state observed from the uploaded workspace

### Strong foundations already exist

- The canonical system description is frozen and explicitly says it is now the sole authoritative description.
- The platform scope matrix correctly defines the target system as Python desktop + server + web dashboard + Android companion + SharedContracts + Workspace.
- SharedContracts, Server, Dashboard, and Android all have task/batch/control-file methodology in place.
- Android `STATE.md` says `AN-B00` through `AN-B06` are now done, including Room, generated Kotlin client integration, add/photo flow, WorkManager sync, and reduced conflict handling.
- Dashboard `STATE.md` says all original batches are done, but it also records a real follow-up gap: page query files still need to be wired to live generated-client calls.

### Important remaining gaps

- `Missing_Context_Completion` still has 8 of 9 rows open. This matters because exact v1 scope, field-level entity details, endpoint behavior, sync state machines, security matrix, operations policy, and acceptance data are not fully specified yet.
- `System_Integration_MVP` still has open system rows for PyApp sync, Android gate, cross-platform smoke, and release readiness.
- The canonical known-gaps register currently records Dashboard live-data stubs, missing sync example schemas, missing location query filters, and incomplete PyApp/Android implementation evidence.
- Some status files are stale relative to each other. For example, `System_Integration_MVP/STATE.md` and `06_KNOWN_GAPS_REGISTER.md` still describe Android as unstarted or at `AN-B00`, while `PlantLibrary_AndroidApp/STATE.md` says all Android MVP batches are done. A rebaseline batch should fix this before deriving final work.

## Final-state principle

The old Python app capability depth should be used as the functional coverage baseline for the complete system, not as a demand that every client implements every feature.

The old Python application includes these major surfaces and workflows:

- shell/navigation, dashboard, plant list, plant detail;
- botanical search and add-plant wizard;
- calendar, statistics, locations;
- admin review, sources/imports;
- settings, provider setup, tag management;
- backup/restore;
- edit profile and edit garden instance;
- image lightbox and attribution;
- provenance details and re-enrichment provider selection;
- conflict resolution and sync conflict review.

For the new system, distribute that depth like this:

| Capability family | Final owner pattern |
|---|---|
| Dense local/offline power-user workflows | Python desktop remains full-depth. |
| Server-backed browser workflows | Dashboard implements broad desktop/web parity. |
| Authoritative synced data, media, auth, workers, secrets | Server owns implementation and security boundary. |
| API/schema/page/design/sync contracts | SharedContracts owns publication and generated clients. |
| Phone-first lookup/capture/lightweight care flows | Android implements reduced companion depth, not full desktop parity. |
| Cross-suite sequencing, evidence, smoke, release readiness | Workspace owns only coordination and validation. |

## Recommended new system-level package

Create:

```text
PlantLibrary_Workspace/implementation/System_Full_Implementation/
  README.md
  STATE.md
  CONTEXT_INDEX.md
  IMPLEMENTATION_PLAN.md
  TASK_CHECKLIST.md
  TASK_CONTEXT.md
  BATCH_PLAN.md
  DRIVER_SCRIPT.md
  SUITE_HANDOFFS.md
  validation/
  scripts/run_next_batch.py
```

Do not move product-code tasks into this package. Its task rows should only coordinate, verify, derive, and route work.

## Proposed system-level batches

### FULL-B00 — Rebaseline current workspace state

Goal: reconcile stale states before creating final tasks.

Rows:

| ID | Owner | Task | Output | Validation |
|---|---|---|---|---|
| `FULL-BASELINE-01` | Workspace | Re-read all suite `STATE.md`, `TASK_CHECKLIST.md`, `BATCH_PLAN.md`, and known gaps. | `validation/CURRENT_IMPLEMENTATION_BASELINE.md` | Every suite has one current status and next action. |
| `FULL-BASELINE-02` | Workspace | Update or cross-reference stale known-gap rows, especially Android status and Dashboard live-data status. | Updated `06_KNOWN_GAPS_REGISTER.md` or addendum | No gap row contradicts suite state. |
| `FULL-BASELINE-03` | Workspace | Create full-system coverage matrix from canonical system requirements and old Python screen coverage. | `validation/FULL_SYSTEM_COVERAGE_MATRIX.md` | Every major old-Python capability is owned, excluded, deferred, or mapped to a suite task. |

### FULL-B01 — Complete missing system context

Goal: finish the system description details that are required for precise final implementation tasks.

Rows:

| ID | Owner | Task | Output | Validation |
|---|---|---|---|---|
| `FULL-MC-01` | Workspace | Run `Missing_Context_Completion` batches `MC-B01` through `MC-B08`. | `validation/MISSING_CONTEXT_COMPLETE.md` | Exact v1 scope, fields, API behavior, sync state machines, security, ops, and acceptance data are present. |

### FULL-B02 — Contract and schema completion

Goal: make SharedContracts complete enough for final suite implementation.

Rows:

| ID | Owner | Task | Output | Validation |
|---|---|---|---|---|
| `FULL-CONTRACT-01` | SharedContracts | Add missing schemas for `conflict-response`, `pull-response`, and `push-request` examples. | New `.schema.json` files | Contract validation has zero skipped sync examples. |
| `FULL-CONTRACT-02` | SharedContracts | Update page contracts after missing-context completion, especially Dashboard live-data inputs and Android exclusions. | Updated page contracts and exclusions | Contract coverage matrix passes. |
| `FULL-CONTRACT-03` | SharedContracts | Regenerate Python, TypeScript, and Kotlin clients after server/OpenAPI changes. | Updated generated clients and manifest | Consumers build against regenerated clients. |

### FULL-B03 — Server final API and operations completion

Goal: close server-side gaps that block live clients and release readiness.

Rows:

| ID | Owner | Task | Output | Validation |
|---|---|---|---|---|
| `FULL-SERVER-01` | Server | Add missing location list filters/query parameters and any endpoint behaviors from `MC-API-001`. | Server endpoints + OpenAPI export | OpenAPI diff is expected/additive and SharedContracts re-sync succeeds. |
| `FULL-SERVER-02` | Server | Complete worker/media/provider/review behavior needed by Dashboard and PyApp. | Worker and media validation report | Provider secrets remain server-side; review flow works. |
| `FULL-SERVER-03` | Server | Finalize deployment, backup/restore, monitoring, and migration dry-run evidence. | Ops readiness report | Release gate has concrete evidence. |

### FULL-B04 — Dashboard live product completion

Goal: turn the dashboard from contract-shaped UI into live server-backed functionality.

Rows:

| ID | Owner | Task | Output | Validation |
|---|---|---|---|---|
| `FULL-DASH-01` | Dashboard | Wire all page query files to generated-client calls. | Dashboard source changes | Authenticated live-data smoke passes. |
| `FULL-DASH-02` | Dashboard | Complete page mutations/actions where currently disabled or stubbed. | Mutation/action implementation | Plant/task/location/review/settings actions work or have known-gap rows. |
| `FULL-DASH-03` | Dashboard | Re-run parity, accessibility, responsive, dark-theme, and error-state validation against live data. | Validation reports | No release-blocking dashboard gaps. |

Suggested Dashboard-local package:

```text
PlantLibrary_Dashboard/implementation/Dashboard_Live_Data_Completion/
```

or append `WD-B07` through `WD-B09` to the current root-level dashboard control files.

### FULL-B05 — Python desktop sync completion

Goal: finish the PyApp online/sync layer while preserving full local offline behavior.

Rows:

| ID | Owner | Task | Output | Validation |
|---|---|---|---|---|
| `FULL-PYAPP-01` | PyApp | Resume `Python_Client_Sync` at `PY-B09` and continue through `PY-B14`. | PyApp migrations/services/workers/UI/tests | Desktop local change reaches server and remains safe offline. |

This should continue inside:

```text
PlantLibrary_PyApp/Improvements/Python_Client_Sync/
```

### FULL-B06 — Android v1 companion completion

Goal: derive and execute Android work beyond MVP, while respecting Android's reduced scope.

Rows:

| ID | Owner | Task | Output | Validation |
|---|---|---|---|---|
| `FULL-ANDROID-DERIVE-01` | Android | Derive Android v1 completion backlog from canonical system description, Android page contracts, and old-Python capability map. | Android-local implementation package | Every Android row has canonical requirement IDs and validation. |
| `FULL-ANDROID-01` | Android | Execute Android v1 completion batches. | Android app/source changes | Offline restart, sync, capture, and reduced conflicts pass. |

Suggested Android-local package:

```text
PlantLibrary_AndroidApp/implementation/Android_V1_Companion_Completion/
```

### FULL-B07 — Cross-platform full smoke

Goal: prove the system behaves as one product.

Rows:

| ID | Owner | Task | Output | Validation |
|---|---|---|---|---|
| `FULL-E2E-01` | Workspace | Run full smoke with one account, one garden, one plant, one photo, one task, one note, one provider/review item. | `validation/FULL_CROSS_PLATFORM_SMOKE_REPORT.md` | Same data is visible and consistent in PyApp, Dashboard, Android, and Server. |
| `FULL-E2E-02` | Workspace | Run offline/online convergence scenarios for PyApp and Android. | Sync scenario report | No duplication, data loss, or silent conflict loss. |

### FULL-B08 — Final release readiness

Goal: declare the final state only when evidence exists.

Rows:

| ID | Owner | Task | Output | Validation |
|---|---|---|---|---|
| `FULL-RELEASE-01` | Workspace | Assemble final acceptance package. | `validation/FINAL_ACCEPTANCE_PACKAGE.md` | All suite gates pass or link to signed known gaps. |
| `FULL-RELEASE-02` | Workspace | Freeze known gaps, accepted deviations, release notes, and next-version backlog. | Release package | No undocumented deviation remains. |

## Recommended Android-local derivation package

Create:

```text
PlantLibrary_AndroidApp/implementation/Android_V1_Companion_Completion/
  README.md
  STATE.md
  CONTEXT_INDEX.md
  IMPLEMENTATION_PLAN.md
  TASK_CHECKLIST.md
  TASK_CONTEXT.md
  BATCH_PLAN.md
  DRIVER_SCRIPT.md
  validation/
  scripts/run_next_batch.py
```

This package should not try to make Android a clone of the Python app. It should derive phone-appropriate tasks from the canonical Android requirements and page-contract exclusions.

### Proposed Android-local batches

| Batch | Goal | Example rows |
|---|---|---|
| `ANV1-B00` | Rebaseline MVP and derive scope | `ANV1-DERIVE-01` compare existing Android MVP to system description; `ANV1-DERIVE-02` create Android coverage matrix. |
| `ANV1-B01` | Settings/account/server configuration completion | persisted server URL, active garden switcher, session/token status, sign-out, sync preferences. |
| `ANV1-B02` | Offline/restart and sync-awareness hardening | offline banner, stale-cache labeling, pending outbox list, retry controls, upload progress. |
| `ANV1-B03` | Plant detail depth within reduced scope | edit garden instance fields, edit local notes/care records, media gallery/lightbox-lite, attribution display where available. |
| `ANV1-B04` | Task/event/note care workflow completion | complete/snooze/reschedule tasks, create notes, log care events, show care history with pending-sync state. |
| `ANV1-B05` | Add plant/photo/enrichment hardening | provider-result preview, enrichment-job status, upload retry/cancel, draft recovery after process death. |
| `ANV1-B06` | Conflict and initial-sync hardening | initial garden sync flow, conflict detail comparison, accept server/local choice for supported fields, deterministic retry/backoff tests. |
| `ANV1-B07` | Accessibility, navigation, theming, and device behavior | TalkBack labels, large font behavior, dark theme, rotation/process-death smoke, permissions recovery. |
| `ANV1-B08` | Android acceptance package | build/test reports, offline-restart report, sync smoke report, known-gap update. |

### Android task derivation algorithm

Use this repeatable rule for deriving more Android tasks:

1. Start from these canonical files:
   - `03_platforms/04_ANDROID_APP_SYSTEM_DESCRIPTION.md`
   - `03_platforms/00_PLATFORM_SCOPE_MATRIX.md`
   - `06_ui_ux/03_ANDROID_ADAPTATION.md`
   - `06_ui_ux/05_PAGE_BY_PAGE_REQUIREMENTS.md`
   - `04_sync_and_data_consistency/*`
   - `05_api_and_contracts/*`
   - `10_quality_acceptance/02_SUITE_ACCEPTANCE_GATES.md`
2. Read `PlantLibrary_SharedContracts/page-contracts/android/*.md` and `EXCLUSIONS.md`.
3. Use old Python screen structures only as capability depth input, not as Android parity requirements.
4. For each page family, decide one of four outcomes:
   - Android owns it in reduced form.
   - Android only shows a read-only/status subset.
   - Android routes users to server/web/desktop for the full workflow.
   - Android explicitly excludes it for v1 and records the reason.
5. For every owned Android behavior, create rows in this order:
   - contract or model prerequisite;
   - Room/data/repository change;
   - network/sync/outbox change;
   - UI/navigation change;
   - offline/error/pending-sync state handling;
   - test/validation evidence.
6. Every row must include:
   - canonical `SYS-*` requirement IDs;
   - owning module or files;
   - blocker assumptions;
   - validation command or manual evidence;
   - known-gap handling if not fully implemented.

### Example Android task rows

| ID | Batch | Area | Task | Requirements | Validation |
|---|---|---|---|---|---|
| `ANV1-SETTINGS-01` | `ANV1-B01` | settings | Persist editable server base URL and show connection test state instead of placeholder config. | `SYS-ANDROID-001`, `SYS-UI-PAGE-REQ-004`, `SYS-SEC-*` | Unit test config storage; manual login smoke. |
| `ANV1-OFFLINE-01` | `ANV1-B02` | offline | Show offline/stale-cache/pending-sync states consistently on Home, Plants, Tasks, Add, and More. | `SYS-SYNC-*`, `SYS-UI-PAGE-REQ-004` | Offline restart smoke with queued write. |
| `ANV1-PLANT-DETAIL-01` | `ANV1-B03` | plant detail | Add reduced edit garden-instance action with Room write and outbox entry. | `SYS-UI-PAGE-REQ-006`, `SYS-SYNC-OUTBOX-*` | Edit offline, reconnect, verify server state. |
| `ANV1-MEDIA-01` | `ANV1-B03` | media | Add mobile media gallery with attribution display and upload-progress states. | `SYS-MEDIA-*`, `SYS-UI-PAGE-REQ-004` | Photo upload retry smoke. |
| `ANV1-CONFLICT-01` | `ANV1-B06` | conflict | Expand conflict detail to show server/local values and supported resolution choices. | `SYS-SYNC-CONFLICT-*`, `SYS-ANDROID-002` | Conflict fixture test. |
| `ANV1-ACCEPT-01` | `ANV1-B08` | validation | Produce Android acceptance report with build, tests, offline restart, and sync smoke evidence. | `SYS-QUAL-SUITE-001` | Report exists and references current commit. |

## Dashboard-local completion recommendation

Create:

```text
PlantLibrary_Dashboard/implementation/Dashboard_Live_Data_Completion/
```

or append:

| Batch | Goal |
|---|---|
| `WD-B07` | Wire all `*-queries.ts` files to generated-client calls and DTO mapping. |
| `WD-B08` | Enable safe page mutations/actions and error/retry states. |
| `WD-B09` | Validate page contracts against live server data, not just empty stubs. |

This is a suite-local job because the gap is Dashboard-only product code. The Workspace package should only coordinate that `WD-B07..WD-B09` exist and pass.

## Known-gap policy update

Before final implementation begins, update the known-gaps register so it distinguishes:

- resolved gaps: e.g. Android MVP no longer unstarted if `AN-B00` through `AN-B06` are truly done;
- open gaps: Dashboard live-data query wiring, SharedContracts missing sync schemas, Server location filters;
- deferred gaps: anything intentionally outside v1 scope;
- high-impact gaps: PyApp sync and cross-platform smoke until proven.

A final release should never rely on `done` task rows alone. It should rely on validation reports and smoke evidence.

## Recommended run order from here

1. Run the new `System_Full_Implementation` rebaseline batch.
2. Finish `Missing_Context_Completion` before deriving new detailed product tasks.
3. Close SharedContracts schema/page-contract gaps and regenerate clients.
4. Finish Server endpoint/worker/ops gaps that live clients need.
5. Finish Dashboard live-data wiring and mutations.
6. Resume PyApp sync implementation at `PY-B09` through `PY-B14`.
7. Derive and run Android v1 companion completion tasks in the Android suite.
8. Run full cross-platform smoke and release-readiness gates from Workspace.

## Most important recommendation

Do not create Android implementation rows in `PlantLibrary_Workspace`. Create only a Workspace handoff row that says Android needs a v1 companion completion package, then create the actual Android rows under `PlantLibrary_AndroidApp`. That preserves your driver model: when you want to work on Android, you run the Android driver from the Android workspace.
