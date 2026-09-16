# onboarding/ — package census register

Running record of `scripts\harness\check_batch_packages.py` output, one section per capture.
Interpreter used is named at each heading.

## Census at step 0

Run with `C:\Programs\AI_Orchestrator_2\.venv\Scripts\python.exe scripts\harness\check_batch_packages.py`
from `C:\Programmierung\SW_Development`, 2026-09-15. Exit code `1` (errors present, expected pre-migration).

Seven live packages match runbook §1b exactly: PyApp 24, Server 35, AndroidApp 44, Dashboard 26,
SharedContracts 11, Workspace V1 18, SDA 8.

```text
PlantLibrary_AndroidApp\implementation\System_V1_Implementation: 44 errors -> {'no 15-column': 1, 'declares missing primary row': 40, 'outside the first sentence': 3}
    batch AN1-B08 has requires token AN1-B09 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
    batch AN1-B08 has requires token AN1-B10 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
    batch AN1-B11 has requires token AN1-B09 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
PlantLibrary_Dashboard\implementation\System_V1_Implementation: 26 errors -> {'no 15-column': 1, 'declares missing primary row': 22, 'has no goal': 1, 'outside the first sentence': 2}
    batch WD1-B03 has no goal
    batch WD1-B04 has requires token WD1-B05 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
    batch WD1-B06 has requires token WD1-B05 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
PlantLibrary_PyApp\implementation\System_V1_Implementation: 24 errors -> {'no 15-column': 1, 'declares missing primary row': 22, 'outside the first sentence': 1}
    batch PY1-B04 has requires token PY1-B05 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
PlantLibrary_Server\implementation\System_V1_Implementation: 35 errors -> {'no 15-column': 1, 'declares missing primary row': 33, 'has no goal': 1}
    batch SV1-B05 has no goal
PlantLibrary_SharedContracts\implementation\System_V1_Implementation: 11 errors -> {'no 15-column': 1, 'declares missing primary row': 10}
PlantLibrary_Workspace\implementation\System_Design_Architecture: 8 errors -> {'no 15-column': 1, 'declares missing primary row': 7}
PlantLibrary_Workspace\implementation\System_Integration_MVP: 25 errors -> {'no 15-column': 1, 'declares missing primary row': 24}
PlantLibrary_Workspace\implementation\System_Tooling: 6 errors -> {'no 15-column': 1, 'declares missing primary row': 5}
PlantLibrary_Workspace\implementation\System_V1_Implementation: 18 errors -> {'no 15-column': 1, 'declares missing primary row': 16, 'outside the first sentence': 1}
    batch SY1-B05 has requires token SY1-B07 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
PlantLibrary_Workspace\strategy\Cross_Platform_Strategy: 30 errors -> {'no 15-column': 1, 'declares missing primary row': 29}
PlantLibrary_Workspace\system_description\PlantLibrary_System_Description: 62 errors -> {'no 15-column': 1, 'duplicate': 46, 'declares missing primary row': 15}
    duplicate context anchor Intent
    duplicate context anchor Output
    duplicate context anchor Validation
    duplicate context anchor Intent
    duplicate context anchor Output
    duplicate context anchor Validation
    duplicate context anchor Intent
    duplicate context anchor Output
    … 38 more
```

## Instance 2 registration, step 5

All calls run 2026-09-16 by the operator against `http://127.0.0.1:8797`, pasted and checked one
at a time per runbook §5/Appendix C. Instance 1 (`8787`, pid `12440`) and `config.yaml` were never
touched.

**1. Starting state** — `GET /api/v1/projects`: exactly the seven rows §1a predicted (`default`
archived; six unbound suite projects, every `batch_package_path` null); active project
`PlantLibrary_PyApp` (`prj_01M2JZGV1E8PGC9VF3MXC0466J`). Preconditions also checked directly (not
a REST call): superproject and all six submodules clean, each submodule `HEAD` matching the
step 2a–4 ledger commits; a fresh run of `check_batch_packages.py` (instance-2 interpreter) showed
0 errors on all seven live packages with classifications matching the step-2a/2b ledger exactly,
and the four terminal packages still showing their original pre-migration error counts.

**2. Bound project created** — `POST /api/v1/projects`:

| field | value |
|---|---|
| id | `prj_01M2MJV0KDKT6HT5XAWJ17SS5P` |
| name | `PlantLibrary_PyApp-V1` |
| repo | `C:\Programmierung\SW_Development\PlantLibrary_PyApp` |
| batch_root_id / batch_relative_path | `pyapp` / `System_V1_Implementation` |
| batch_package_path (response) | `C:\Programmierung\SW_Development\PlantLibrary_PyApp\implementation\System_V1_Implementation` (non-null — F-5 satisfied) |

**3. Activate + archive** — `POST /api/v1/projects/prj_01M2MJV0KDKT6HT5XAWJ17SS5P/activate`
succeeded, then all six old unbound projects archived via
`PATCH /api/v1/projects/{id}` `{"archived": true}`, `PlantLibrary_PyApp` last (per F-5, an active
project cannot itself be archived):

| project | id | archived_at |
|---|---|---|
| PlantLibrary_Workspace (old) | `prj_01M2JZG6N5MFNKGDSDCHKYSBKM` | 2026-09-16T07:46:42.651133Z |
| PlantLibrary_Server (old) | `prj_01M2JZGV42TDGTYJZ7ZVAAWJQG` | 2026-09-16T07:46:42.913092Z |
| PlantLibrary_AndroidApp (old) | `prj_01M2JZGV48GKXYY9RFBR3RYKVR` | 2026-09-16T07:46:43.060349Z |
| PlantLibrary_Dashboard (old) | `prj_01M2JZGV4HNM0DH660RBRJM5QX` | 2026-09-16T07:46:43.210991Z |
| PlantLibrary_SharedContracts (old) | `prj_01M2JZGV4RXJT58FHENM20BYDQ` | 2026-09-16T07:46:43.363429Z |
| PlantLibrary_PyApp (old, unbound) | `prj_01M2JZGV1E8PGC9VF3MXC0466J` | 2026-09-16T07:46:43.648717Z |

Verifying `GET /api/v1/projects`: exactly one active project — `PlantLibrary_PyApp-V1`
(`active_project_id` = `prj_01M2MJV0KDKT6HT5XAWJ17SS5P`); `default` unchanged (already archived);
all six old suite projects now carry a non-null `archived_at`.

**4. Remaining five live packages bound** (no activate; SDA project not created, per D4/D5):

| project | id | batch_root_id | batch_package_path (non-null, confirms F-5) |
|---|---|---|---|
| PlantLibrary_Server-V1 | `prj_01M2MJZPPTRW26W0PKQT7B1GXZ` | `server` | `...\PlantLibrary_Server\implementation\System_V1_Implementation` |
| PlantLibrary_SharedContracts-V1 | `prj_01M2MJZQ0E95Q5J3B43TVBRJA2` | `sharedcontracts` | `...\PlantLibrary_SharedContracts\implementation\System_V1_Implementation` |
| PlantLibrary_Dashboard-V1 | `prj_01M2MJZQAHGQ4NTH3778PH39BJ` | `dashboard` | `...\PlantLibrary_Dashboard\implementation\System_V1_Implementation` |
| PlantLibrary_AndroidApp-V1 | `prj_01M2MJZQS3C441WK6CEYDZ566J` | `androidapp` | `...\PlantLibrary_AndroidApp\implementation\System_V1_Implementation` |
| PlantLibrary_Workspace-V1 | `prj_01M2MJZR83KD39BGKH2M4HVMP4` | `workspace` | `...\PlantLibrary_Workspace\implementation\System_V1_Implementation` |

All five created `200` on first attempt (the fresh census in item 1 had already shown 0 parser
errors for each); no suite skipped.

**5. Pause + intake hold at `PY1-B08`, with a sequencing correction.** The runbook's step-5 prose
("pause dispatch... then intake") does not hold: `POST /api/v1/projects/{id}/batch/pause` was
tried first and failed verbatim `{"detail":"project prj_01M2MJV0KDKT6HT5XAWJ17SS5P has no batch
execution to pause"}` — read from source (`src/conductor/core.py:2564`, `pause_project`), the verb
requires an existing `project_batch_execution` row, which does not exist until intake is
confirmed. Reading `intake.py:_confirm_batch_package` further showed a confirmed eligible batch is
created directly with `status: "queued"` and a dispatch-ready prepared task — never pre-paused —
so the scheduler's `idle_tick_s` (5 s, `config.yaml`) could in principle dispatch it before an
operator-issued pause lands. Corrected order used instead: **preview → confirm → pause**, the
confirm and pause issued back-to-back in one script with no round-trip in between, to close that
window.

- `POST /api/v1/intake/batch-package` `{project_id: prj_01M2MJV0KDKT6HT5XAWJ17SS5P,
  start_batch_key: "PY1-B08"}` → preview `pv_01M2MK2YF4R338A9H82816G5AP`, `errors: []`,
  `PY1-B08` order 0 classification `will_run` with rows `PY-V1-TEST-02`, `PY-V1-TEST-03`,
  `PY-V1-DOC-01` (matches D6 and the independent census exactly); three informational warnings
  about `PY1-B03`'s cross-suite `Requires` being `UNKNOWN`/undecidable (F-11(c), not a blocker).
- `POST /api/v1/intake/previews/pv_01M2MK2YF4R338A9H82816G5AP/confirm`
  `{"shared_tree_acknowledged": false}` (no shared tree on this project) →
  `run_id: run_01M2MK2YF4R338A9H82816G5AN`.
- `POST /api/v1/projects/prj_01M2MJV0KDKT6HT5XAWJ17SS5P/batch/pause` → succeeded; execution
  `status: "paused"`, `current_task.state: "READY"` (not `RUNNING` — no worker was ever
  dispatched), `legal_actions: ["stop", "resume"]`.
- `GET /api/v1/projects/prj_01M2MJV0KDKT6HT5XAWJ17SS5P/batch-execution` →
  `current_batch_key: "PY1-B08"`, `status: "paused"`, `attention_reason: ""`. Done-when met.

**Outcome:** six bound projects (PyApp, Server, SharedContracts, Dashboard, AndroidApp,
Workspace V1), one active (`PlantLibrary_PyApp-V1`), the six old unbound projects archived,
PyApp's execution paused at `PY1-B08` with an empty `attention_reason`. No Workspace SDA project
created (D4/D5, deferred). Instance 1 and `config.yaml` untouched throughout.
