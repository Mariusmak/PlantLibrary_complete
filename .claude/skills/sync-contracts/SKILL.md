---
name: sync-contracts
description: The PlantLibrary contract-wave ritual. Reviews a Server OpenAPI export diff against SharedContracts (breaking-change detection, semver recommendation, consumer impact), regenerates the Python/TypeScript/Kotlin clients, validates sync contracts and examples, updates the client manifest and contract version, reports consumer unblocks, and drives client-side adoption. Use for "run the contract wave", "review the OpenAPI diff", "regenerate the clients", "check contract drift", "adopt the regenerated client in PyApp", or any row whose skill column says sync-contracts:<command>.
user-invocable: true
argument-hint: "[review|wave|check|adopt] [suite]"
---

One contract wave = Server export → diff review → client regeneration →
validation → manifest + one coherent version bump → consumer unblock report.
Every step leaves recorded evidence; generated output is **never hand-edited**
(fixes go in the OpenAPI source or the suite-side wrapper layer).

## Canonical locations

All SharedContracts commands run from `PlantLibrary_SharedContracts/`.

| Artifact | Where |
|---|---|
| OpenAPI snapshot | `openapi/plantlibrary.openapi.yaml` (SHA-256 recorded in manifest) |
| Server export | `PlantLibrary_Server/scripts/export_openapi.py` (owned by `SV-OPENAPI-*` rows) |
| Generated clients | `generated/{python,typescript,kotlin}/` |
| Client manifest | `generated/CLIENT_MANIFEST.md` — source hash, per-target command, tool versions, consumer readiness |
| Version + changelog | `CONTRACT_VERSION.md` — semver rule lives there; one bundle version for everything |
| Sync contracts | `sync-contracts/entities.yaml` · `operations.yaml`, plus `schemas/` + `api-examples/` |
| Tooling | `scripts/generate_clients.py` (Windows `.cmd`-shim caveat: `GENERATION_BLOCKERS.md`, row `SC-TOOL-01` — fall back to the manifest's direct per-target commands while open) · `scripts/validate_contracts.py` |

## Commands

### `review` — pre-regen / pre-handoff diff review

Input: a fresh Server export (or the export a `SV-OPENAPI-*` row just
produced). Never edits contracts.

1. Diff against the committed snapshot: added/removed/renamed paths,
   operations, schema fields; parameter and response changes.
2. Classify each change per `CONTRACT_VERSION.md`'s rule → **semver
   recommendation** (patch/minor/major) with the breaking items named.
3. Sync-contract consistency: do `entities.yaml`/`operations.yaml` still
   match the routes (push-supported entity types, operation shapes)?
   List every mismatch.
4. Consumer impact table: per client (PyApp / Dashboard / Android) — what
   changes for it, which of its rows this wave unblocks or breaks.
5. Write the review to the invoking package's `validation/`
   (`<ROW-ID>_contract_review_<date>.md`). The later version-bump row
   (`SC-VER-01` / `SC-V1-VER-01`) consumes this recommendation.

### `wave` — full regeneration ritual (SharedContracts regen rows)

1. Requirements: the feeding `SV-OPENAPI-*` row is done. Import the export
   into `openapi/`; run `review` on it if no current review exists.
2. Regenerate all three targets: `python scripts/generate_clients.py`
   (wrapper), or the manifest's direct commands while `SC-TOOL-01` is open.
   Regenerate **all** targets in one wave — never leave clients on mixed
   snapshots.
3. Validate: `python scripts/validate_contracts.py` must report
   0 failed / 0 skipped; fix contract/example drift (that is contract
   content, not generated output) before proceeding.
4. Update `generated/CLIENT_MANIFEST.md`: new source SHA-256, tool versions,
   per-target status, consumer readiness lines.
5. Version: apply the review's semver recommendation to
   `CONTRACT_VERSION.md` with an itemized changelog entry — one coherent
   bump per release window (coordinate an in-flight SDA design bump via the
   Workspace checkpoint before bumping twice).
6. Consumer unblock report (goes in the compact report and the evidence
   file): which suite rows are now actionable (e.g. PyApp `PY-V1-CLIENT-01`,
   Dashboard/Android rows requiring `SC1-B02`), for the Workspace
   checkpoint rows (`SY1-SEQ-01`/`SY1-SEQ-02`) to record.

### `check` — drift detection (CI and on demand)

Recompute the snapshot's SHA-256 vs the manifest; regenerate to a temp
location and diff against the committed clients; run
`validate_contracts.py`. Any difference = drift: report the offending
target and stop (no silent regeneration). This is the check `SC-CI-01`
wires into CI.

### `adopt <suite>` — consumer-side wave pickup

- **PyApp**: `pip install -e ../PlantLibrary_SharedContracts/generated/python`
  into the venv; run the sync-scoped pytest set; offline startup smoke
  (standing invariant). Wrapper adjustments go in PyApp's sync wrapper —
  never in `generated/`.
- **Dashboard / Android**: rebuild against the regenerated TS/Kotlin client;
  run the affected test scope. Their per-feature rows own the deeper
  integration.
- Record the adopted contract version + any wrapper adjustments in the
  suite's `STATE.md` continuation log.

## Integration with batch rows

Rows activate this skill via their `skill` column (`sync-contracts:review`
on Server `SV-OPENAPI-*` export rows as the pre-handoff self-check;
`sync-contracts:wave` on SharedContracts regen rows; `sync-contracts:adopt`
on client adoption rows). Version-bump rows stay `skill: none` — they apply
the recorded review recommendation. run-batch loads this skill only for
such rows, after selection and requirements pass.
