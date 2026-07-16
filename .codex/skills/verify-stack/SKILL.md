---
name: verify-stack
description: Repeatable verification harness for the PlantLibrary local stack. Brings up the Docker stack (API/Postgres/Redis/MinIO/Keycloak), migrates, seeds, health-checks, captures before/after entity snapshots, and drives evidence-pack walkthroughs for validation rows (live sync walkthroughs, cross-platform smoke, acceptance runs). Use for "bring up the stack", "run the walkthrough for PY-V1-WALK-01", "capture a convergence snapshot", "is the stack healthy", or any row whose skill column says verify-stack:<command>.
user-invocable: true
argument-hint: "[up|seed|status|snapshot|walkthrough|down] [row-id|label]"
---

Evidence-driven verification: a step passes only with captured proof
(command output, API response, screenshot, timestamped observation) — never
because the code looks correct. This skill owns the **procedure, environment
recipe, and evidence format**; the **scenario list** for a walkthrough always
comes from the invoking row's `TASK_CONTEXT.md` anchor or named runbook —
never duplicated here.

## Operating rules

- Never edit product code during a verification run. Failures become gap/row
  proposals routed to the owning suite (run-batch §5 route-don't-duplicate).
- Never paste secrets, tokens, or real personal data into evidence files;
  redact and note the redaction. The disposable local credential source is
  `PlantLibrary_Server/docs/local_android_test_environment.md`.
- Clients under test use a disposable validation database, never a real
  personal working DB.
- Step statuses: `pass | fail | blocked | gated | skipped | pass-with-gap |
  pending`. Record honestly; a partial run is a partial run.

## Canonical environment

All stack commands run from `PlantLibrary_Server/`. If any command here has
drifted, the authority is `docs/local_android_test_environment.md` — fix the
drift there and here together.

```bash
COMPOSE="docker compose -f deploy/docker-compose.dev.yml -f deploy/docker-compose.oidc.yml"
```

| Item | Value |
|---|---|
| API (host) | `http://localhost:8000` — health: `/api/v1/health`, ready: `/api/v1/health/ready` |
| API (Android emulator) | `http://10.0.2.2:8000` |
| Keycloak | `http://localhost:8080/realms/plantlibrary` (emulator: `10.0.2.2:8080`) |
| Test identity | user `testgrower`, garden `Test Backyard Garden` |
| Services | api, worker, postgres, redis, minio, keycloak |

Scripted API access: obtain a token from Keycloak's token endpoint via
password grant for `testgrower` (credentials per the doc above), then
`curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/api/v1/...`.

## Client environments

Walkthrough scriptable steps may drive clients through these recipes.
GUI-emulator or visible-browser runs happen only on explicit user request;
headless execution is the default.

### Android (headless)

Use AVD `plantlibrary_test_noGUI`. Start it and run the test recipe through
`PlantLibrary_AndroidApp/scripts/run_headless_tests.ps1`, created by
`AN-V1-TEST-02`; the emulator uses `-no-window -no-audio -no-boot-anim` and
waits for `sys.boot_completed`. For a direct instrumented run, execute
`gradlew connectedDebugAndroidTest` from `PlantLibrary_AndroidApp/`.

The GUI fallback — AVD `plantlibrary_test_GUI` through
`scripts/start_gui_emulator.ps1` — is used only on explicit request.

### Dashboard (headless browser)

From `PlantLibrary_Dashboard/`, run `npm run test:e2e` for Playwright
Chromium headless against the MSW-mocked development server; no stack is
needed. Run `npm run test:e2e:live` for the environment-gated live project
against this skill's canonical stack. These recipes are created by
`WD-V1-TEST-01` and `WD-V1-TEST-02`.

### PyApp (offscreen)

From `PlantLibrary_PyApp/`, run:

- `python scripts/offline_smoke.py` — the real `main.py` subprocess with
  `QT_QPA_PLATFORM=offscreen` and a disposable application-data directory.
- `pytest -m app_e2e` — the in-process assembled `MainWindow` tier.
- `pytest -m server_integration` — the service-level tier against the live
  stack.

These recipes are created by `PY-V1-TEST-02`, `PY-V1-TEST-03`, and
`PY-V1-INT-01`.

## Commands

### `up`

1. `$COMPOSE up -d`, then wait for `curl -fsS http://localhost:8000/api/v1/health/ready`
   (retry ~60s; on timeout print `$COMPOSE ps` + the failing service's last
   log lines and stop).
2. `$COMPOSE exec -T api alembic upgrade head`.
3. Seed check: authenticated `GET /api/v1/gardens` must list
   `Test Backyard Garden`; if missing, run `seed`.
4. Print the endpoint table above plus per-service status. Known quirk: new
   photo uploads from the Android emulator hit the MinIO container-network
   URL gap recorded in the environment doc — reference it, don't re-diagnose.

### `seed`

Reseed procedure from the environment doc (the script is **not idempotent**
— follow the doc's reset steps exactly):

```bash
docker cp scripts/seed_android_test_environment.py <api-container>:/srv/...
$COMPOSE exec -T api python seed_android_test_environment.py
```

Verify the seed script's exit code and the seeded counts the doc lists
(plants, 6 care tasks incl. 2 overdue, photo). Record the reseed timestamp —
walkthroughs must state which seed state they ran against.

### `status`

`$COMPOSE ps` + both health endpoints + authenticated garden list. One
compact table; no log dumps unless something is down.

### `snapshot <label>`

The convergence-check primitive. Authenticated API reads of the entities the
current run cares about (default: gardens, plants, care tasks of the test
garden), saved as `validation/evidence/<RUN-ID>/<label>_<timestamp>.json`
with a printed summary table: entity, id, `server_version`, key field values.
Take one `before` and one `after` snapshot around every mutating scenario;
the diff is the convergence evidence.

### `walkthrough <row-id>`

1. **Resolve the scenario source**: read the row's checklist line + anchor in
   the invoking package. The anchor (or the runbook it names) defines the
   scenario list, required clients, and the evidence pack path (the row's
   `file(s)` column). Requirements unmet → report and stop (do not bring up
   half a run).
2. **Prepare**: `up` (+ `seed` if the run needs a fresh dataset); create
   `validation/evidence/<RUN-ID>/` in the invoking package,
   `RUN-ID = <ROW-ID>-<yyyymmdd>-NN`; take the `before` snapshot.
3. **Execute scenarios in order.** Scriptable steps (API calls, service
   checks, snapshots, and client-automation commands from the Client
   environments section) run directly. GUI steps are human steps: print
   **one** exact numbered instruction (what to click/enter, expected result,
   what to capture), then wait for confirmation and the evidence path before
   the next. Never batch-print all steps and never mark a human step `pass`
   without its evidence.
4. **Capture**: evidence files named `<ROW-ID>_<flow>_<timestamp>.<ext>`
   into the run folder; `after` snapshots following each mutating scenario.
5. **On failure**: record the exact command/screen + error, log a gap
   (`MVP_VALIDATION_GAP_LOG.md` conventions: next `VGAP-NNN`, or the V1
   package's register), mark the scenario `fail` or `pass-with-gap`, and
   continue with the remaining scenarios where independent — never inline-fix.
6. **Write the evidence pack** (path from the row) and finish with the
   pack-completeness check below. Update the package's evidence index if it
   has one.

### `down`

`$COMPOSE down` (volumes preserved — the seeded state survives).
`down --clean` additionally removes volumes; confirm with the user first and
note that the next `up` requires `seed`.

## Evidence pack format

```markdown
# <ROW-ID> — <title>
Run: <RUN-ID> · Date · Seed state: <reseed timestamp> · Stack: <compose files + git rev>

## Scenario results
| # | Scenario | Steps ref | Status | Evidence |
## Convergence
| Entity | id | server_version before | after | Verdict |
## Gaps raised
| Gap ID | Scenario | One-line description | Routed to |
## Verdict
<overall + what remains pending, honestly>
```

Completeness check before closing: every scenario has a status and at least
one evidence file; every mutating scenario has before/after versions; every
`fail`/`pass-with-gap` has a gap row with an owner; secrets redacted.

## Integration with batch rows

Rows opt in via their `skill` column (`verify-stack:walkthrough`,
`verify-stack:snapshot`); run-batch loads this skill only for such rows,
after selection and requirements pass. A walkthrough row is `done` only when
its evidence pack passes the completeness check — matching run-batch's rule
that unexecuted validation means not done.
