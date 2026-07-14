# SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT — run this in a fresh session from `SW_Development/`

Paste everything below the `---` into a new session, run from the `SW_Development` workspace root
(not from inside `PlantLibrary_AndroidApp`, since this task needs read/write access to
`PlantLibrary_Server` too). It implements the one remaining human action blocking Android MVP
validation: a reachable OIDC test server, one test user, one owned garden, and seeded
plant/task/media/conflict data.

---

## Why this exists

`PlantLibrary_AndroidApp/implementation/Android_MVP_Validation_Report.md` (2026-07-06) recorded that
the Android app now builds cleanly, lints clean, and installs/launches on a real emulator without
crashing — it correctly reaches the fresh-install OIDC login screen and handles a real network error
gracefully. What could **not** be validated is everything past login (garden selection, initial sync,
Home/Plants/Tasks, Add/photo, sync diagnostics, conflict resolution, shell polish across ~12
destinations), because no reachable OIDC provider or seeded test-server data exists. Read that
report's "What is still blocked, and exactly why" and "What a human needs to do" sections, and
`PlantLibrary_AndroidApp/STATE.md`'s latest continuation update, before doing anything else — they
are the authoritative statement of what this session needs to produce.

**Your job is to stand up that test environment, not to modify Android app source code.** A
follow-up session (re-running `PlantLibrary_AndroidApp/DRIVER_SCRIPT.md`'s validation methodology)
will consume what you build here to actually complete a login and walk the remaining acceptance
flows. If, after standing up the environment, you have time and the emulator from the prior session
still exists (`plantlibrary_test`, API 30), you may optionally continue into that validation pass
yourself — but do not skip or shortcut the environment setup to get there faster.

## Hard scope

Work primarily in:

```text
SW_Development/PlantLibrary_Server
```

You may read (but should not need to modify):

```text
SW_Development/PlantLibrary_SharedContracts   (entity/sync contract shapes, for seed data fields)
SW_Development/PlantLibrary_AndroidApp        (read auth_plan.md, build.gradle.kts, validation report — do not edit app source)
```

Do not modify `PlantLibrary_Dashboard`, `PlantLibrary_PyApp`, or `PlantLibrary_Workspace`. You may
append one short, honest status note to `PlantLibrary_AndroidApp/STATE.md` at the end recording that
a test environment now exists and where its connection details live — do not otherwise touch that
suite's control files (`TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `BATCH_PLAN.md`) — that bookkeeping is
this suite's own driver's job, not yours.

## What already exists (verified 2026-07-06, re-verify before trusting)

- `PlantLibrary_Server` is FastAPI + PostgreSQL 16 + Redis + Dramatiq worker + MinIO (S3-compatible
  media storage), run locally via `docker compose -f deploy/docker-compose.dev.yml up` — starts
  `postgres` (5432), `redis` (6379), `minio` (9000/9001), `api` (uvicorn, **port 8000**, hot-reload),
  `worker`. No `.env.example`; config is `app/core/config.py`'s `Settings` (pydantic-settings).
- **There is no OIDC provider anywhere in this codebase or its siblings.** `app/core/security.py`
  validates bearer tokens by fetching `{oidc_issuer}/.well-known/jwks.json` and checking `aud`/`iss`.
  `Settings.oidc_issuer` / `oidc_audience` default to `None` — auth does not work until a real
  issuer is configured. `docs/SV-AUTH-01_auth_design.md` explicitly defers IdP choice to deploy time.
- **No seed scripts or fixtures exist.** Server tests (`tests/conftest.py`, `tests/test_auth_garden.py`)
  create users directly via SQLAlchemy models and mint session tokens directly, bypassing real OIDC —
  useful as a reference for DB shape, not reusable as-is for testing the Android app's actual login.
- The Android app does a **real** OIDC discovery + Authorization Code + PKCE flow via AppAuth (Chrome
  Custom Tabs) — not a bare JWKS check. Its registered redirect URI is exactly:
  ```
  com.plantlibrary.android:/oauth2redirect
  ```
  (from `PlantLibrary_AndroidApp/core/auth/src/main/java/.../OidcConfig.kt`'s `DEFAULT_REDIRECT_URI`,
  matching `app/build.gradle.kts`'s `appAuthRedirectScheme = "com.plantlibrary.android"`). A bare
  JWKS/token stub is **not sufficient** — the provider must serve a real
  `/.well-known/openid-configuration` discovery document plus working authorization/token endpoints.
- Verify all of the above yourself first (`grep`/read the actual files) — this list is a starting
  point from a prior session, not a substitute for checking current state.

## Step 1 — add a real local OIDC provider

Add Keycloak (or another real OIDC provider if you have a strong reason to prefer one — Keycloak is
recommended because one component satisfies discovery + PKCE + JWKS with a realm-export file) to a
new docker-compose override (e.g. `deploy/docker-compose.oidc.yml`, composed alongside
`docker-compose.dev.yml`, so the base dev file stays untouched). Configure:

- A realm with one client: public client (PKCE, no client secret — the Android app is a native
  app), redirect URI `com.plantlibrary.android:/oauth2redirect`, plus a browser-reachable redirect
  for any manual/browser testing you do yourself.
- One test user with a known username/password.
- **Critical, non-obvious constraint — verify this before considering the step done:** the issuer
  URL the Android emulator uses to fetch the discovery document must be a URL the emulator can
  actually reach, and it must exactly match what Keycloak reports as its own `issuer` claim in that
  discovery document (AppAuth checks this). The emulator reaches the host machine via `10.0.2.2`, not
  `localhost`. Depending on Keycloak's hostname mode (`KC_HOSTNAME`, strict vs. request-based in
  recent versions), you may need to explicitly set the hostname to `10.0.2.2:<port>` or run Keycloak
  in a mode that infers the issuer from the incoming request's `Host` header. **Prove this works**
  by fetching `http://10.0.2.2:<port>/realms/<realm>/.well-known/openid-configuration` from inside a
  running emulator (`adb shell curl ...` or equivalent) before moving on — don't assume it's correct
  from the docker-compose config alone.
- Set `OIDC_ISSUER` and `OIDC_AUDIENCE` env vars on the `api` service (in your override file) to
  match the realm issuer and client id, so the server's own JWKS validation agrees with what the
  Android app receives.

## Step 2 — bring the stack up and migrate

```bash
docker compose -f deploy/docker-compose.dev.yml -f deploy/docker-compose.oidc.yml up -d
alembic upgrade head
```

Confirm `GET http://localhost:8000/` (or whatever this app's health endpoint is — check
`app/main.py`) returns healthy before proceeding.

## Step 3 — seed one test user, one owned garden, and real plant/task/media/conflict data

No seed script exists yet — write one (Python, using the server's own SQLAlchemy models directly is
fine for the user/garden-ownership linkage, since that mirrors the existing test pattern in
`tests/conftest.py`; use the real HTTP CRUD API for garden-scoped content so the data is created the
same way the Android app itself would create it). Reference
`PlantLibrary_SharedContracts/sync-contracts/entities.yaml` for required fields per entity. At
minimum:

1. A `UserProfile` row whose identity matches the OIDC subject (`sub` claim) of the test user you
   created in Keycloak — a real login must resolve to this same profile, not a disconnected one.
2. One garden owned by that user (`POST /api/v1/gardens`).
3. A handful of plant instances, at least one care task (some overdue, some upcoming, so
   `AN-MVP-TASKS-01`'s grouping is actually visible), a note, and at least one uploaded photo
   (`POST /api/v1/gardens/{garden_id}/media` + the presigned-URL completion step — check
   `feature:addplant`'s `MediaUploadCoordinator` in the Android app or the server's own media tests
   for the exact two-step contract).
4. **At least one genuine sync conflict** — conflicts are not static rows. Per
   `docs/SV-CONFLICT-01_conflict_protocol_notes.md` and `tests/test_sync.py::test_push_update_conflict_when_base_version_stale`,
   produce one by pushing an update directly (e.g. via the CRUD API or DB), then pushing a second
   conflicting update through `POST /api/v1/gardens/{garden_id}/sync/push` using a stale
   `base_server_version` — this is what actually populates `sync_conflict`.

Verify every piece of seeded data with a direct read (DB query or GET endpoint) before calling this
step done — don't assume your seed script's exit code of 0 means the data is actually queryable in
the shape the Android app expects.

## Step 4 — record the handoff

Write connection details to a new file, e.g.
`PlantLibrary_Server/docs/local_android_test_environment.md` (this is local dev-only throwaway
credentials, not a production secret, but still don't commit anything that isn't clearly a
disposable local dev value):

- Issuer URL (as the Android emulator must use it, i.e. the `10.0.2.2`-based one), client ID,
  test username/password.
- API base URL for the Android app to use (also `10.0.2.2`-based, port 8000).
- Test user's owned garden name/id, and a one-line summary of what was seeded (counts of
  plants/tasks/notes/photos, and confirmation a conflict exists and how to see it).
- The exact `docker compose` command to bring this stack up again later, and how to re-run the seed
  script idempotently (or note that it isn't idempotent and a fresh DB is needed each time).

Then append one short paragraph to `PlantLibrary_AndroidApp/STATE.md` (append, do not rewrite prior
continuation notes) stating that a local OIDC test environment + seeded data now exists, pointing at
`PlantLibrary_Server/docs/local_android_test_environment.md`, and that the next step is re-running
`PlantLibrary_AndroidApp/DRIVER_SCRIPT.md`'s validation methodology against it.

## Output

Finish with a compact report: what was stood up (services, ports, issuer), what was seeded (counts +
confirmation a real conflict exists), the exact discovery-document fetch you used to prove the
emulator-reachable issuer works, where the handoff doc lives, and any open blocker if something in
this step couldn't be completed (e.g. Docker not available in this environment, port conflicts with
services already running — check for those before assuming a clean slate). Do not print full
docker-compose YAML, full seed script source, or full logs inline — summarize and point at the
files.
