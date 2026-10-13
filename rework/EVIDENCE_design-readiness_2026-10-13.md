# Design readiness — step B5-8 evidence (2026-10-13)

*Step `B5-8` of the master rework program (`rework/PROMPTS_master-rework-runbook_2026-10-13.md` §3.7, lane B5), Sonnet 5.5 · high, headless session in `C:\Programmierung\SW_Development` on `master`. Base `09cb6ed`. The Kit's Conductor readiness check (`anchoring-kit\conductor\check-conductor-readiness.mjs`, rows 1-7) was run once per anchored client, statically, with the instance-2 directory passed read-only. No test, build, browser or app ran; no client, Kit or instance file was written. The tool reads files and, for row 2, runs the client's own installed `scripts/design/check-parity.mjs`, which writes nothing.*

## §1 Pins at the run

| Item | Value |
|---|---|
| Kit | `C:\Programmierung\Design_Template_Kit` @ `612e634` = `v1.11.0`, clean (read-only) |
| Interpreter | Node v24.18.0 |
| Dashboard | `PlantLibrary_Dashboard` @ `f03a0eb`, clean |
| PyApp | `PlantLibrary_PyApp` @ `52aaed5`, clean |
| AndroidApp | `PlantLibrary_AndroidApp` @ `ffa3214`, clean |
| Each client's pin | `design/conformance/CONSUMED_DESIGN.md`: Kit `1.11.0`, Design `1.0.0` |
| Packages | `<client>\implementation\System_V1_Implementation` (`--package`, explicit) |
| Instance directory passed | `C:\Programs\AI_Orchestrator_2` (`--conductor`), read-only |

The invocation, per client (`<c>` = `Dashboard`, `PyApp`, `AndroidApp`; `--json` repeated for the machine copy):

```
node C:\Programmierung\Design_Template_Kit\anchoring-kit\conductor\check-conductor-readiness.mjs ^
  --target C:\Programmierung\SW_Development\PlantLibrary_<c> ^
  --conductor C:\Programs\AI_Orchestrator_2 ^
  --package C:\Programmierung\SW_Development\PlantLibrary_<c>\implementation\System_V1_Implementation
```

Exit code 1 for all three (at least one failing row). Raw text and JSON are in the session scratch, `...\scratchpad\b5-8\{Dashboard,PyApp,AndroidApp}.{txt,json}`; the text is quoted in §3.

## §2 Result at a glance

| Row | Dashboard `f03a0eb` | PyApp `52aaed5` | AndroidApp `ffa3214` |
|---|---|---|---|
| 1 Kit installed | pass | pass | pass |
| 2 Skill parity | pass | FAIL (impeccable only) | FAIL (impeccable only) |
| 3 Rule block in both instruction files | pass | pass | pass |
| 4 Impeccable hook active | pass | pass | FAIL (hook file absent) |
| 5 CI conformance job | pass | pass | pass |
| 6 UI rows carry `design_context` + a design check | pass, **vacuous** (§4.1) | pass, **vacuous** | pass, **vacuous** |
| 7 Worker injection deployed (path b) | FAIL (not deployed) | FAIL (not deployed) | FAIL (not deployed) |
| 8 Smoke dispatch | pending | pending | pending |
| Tool tally / verdict | 6 pass · 1 fail · 1 pending / NOT ready | 5 · 2 · 1 / NOT ready | 4 · 3 · 1 / NOT ready |

Rows 1, 3 and 5 are green in all three clients. The tool's verdict is "NOT ready" for each, and the reds are explained in §4 against the step that owns them. Two further facts the tool does not state: row 6's green is vacuous (§4.1), and the instance directory passed is not the data directory the instance's config names (§4.3).

## §3 The three runs, quoted

### Dashboard

```
Conductor readiness — C:\Programmierung\SW_Development\PlantLibrary_Dashboard

  [PASS] 1. Kit installed
         7 checks + lib + 3 skills present
  [PASS] 2. Skill parity
         design-kit parity: pass
  [PASS] 3. Rule block in both instruction files
         CLAUDE.md + AGENTS.md
  [PASS] 4. Impeccable hook active
         .github/hooks/impeccable.json
  [PASS] 5. CI conformance job
         .github\workflows\design-conformance.yml runs run-all.mjs
  [PASS] 6. UI rows carry design_context + a design check
         0 dispatchable required row(s), all closing on a design check
  [FAIL] 7. Worker injection deployed (path b)
         integrator.md not deployed; implementer.md not deployed
  [PEND] 8. Smoke dispatch proves the gate fired
         no evidence pack given; dispatch one batch with a UI row into this repo and pass --evidence

Rows: 6 pass · 1 fail · 1 pending
Verdict: NOT ready — 1 failing row(s)
```

### PyApp

```
Conductor readiness — C:\Programmierung\SW_Development\PlantLibrary_PyApp

  [PASS] 1. Kit installed
         7 checks + lib + 3 skills present
  [FAIL] 2. Skill parity
         design-kit parity: FAIL: impeccable byte-different (.claude vs .github): SKILL.md
  [PASS] 3. Rule block in both instruction files
         CLAUDE.md + AGENTS.md
  [PASS] 4. Impeccable hook active
         .github/hooks/impeccable.json
  [PASS] 5. CI conformance job
         .github\workflows\design-conformance.yml runs run-all.mjs
  [PASS] 6. UI rows carry design_context + a design check
         0 dispatchable required row(s), all closing on a design check
  [FAIL] 7. Worker injection deployed (path b)
         integrator.md not deployed; implementer.md not deployed
  [PEND] 8. Smoke dispatch proves the gate fired
         no evidence pack given; dispatch one batch with a UI row into this repo and pass --evidence

Rows: 5 pass · 2 fail · 1 pending
Verdict: NOT ready — 2 failing row(s)
```

### AndroidApp

```
Conductor readiness — C:\Programmierung\SW_Development\PlantLibrary_AndroidApp

  [PASS] 1. Kit installed
         7 checks + lib + 3 skills present
  [FAIL] 2. Skill parity
         design-kit parity: FAIL: impeccable byte-different (.claude vs .github): SKILL.md
  [PASS] 3. Rule block in both instruction files
         CLAUDE.md + AGENTS.md
  [FAIL] 4. Impeccable hook active
         impeccable is installed but .github/hooks/impeccable.json is missing
  [PASS] 5. CI conformance job
         .github\workflows\design-conformance.yml runs run-all.mjs
  [PASS] 6. UI rows carry design_context + a design check
         0 dispatchable required row(s), all closing on a design check
  [FAIL] 7. Worker injection deployed (path b)
         integrator.md not deployed; implementer.md not deployed
  [PEND] 8. Smoke dispatch proves the gate fired
         no evidence pack given; dispatch one batch with a UI row into this repo and pass --evidence

Rows: 4 pass · 3 fail · 1 pending
Verdict: NOT ready — 3 failing row(s)
```

## §4 Each red row against the step that owns it

### 4.1 Row 6 is green, but the check never looked at a row

All three runs print "0 dispatchable required row(s), all closing on a design check", and the JSON `breakdown` shows `required: 0` for both `dispatchable` and `done` in every client. The packages do contain `design_context: required` rows. A scratch re-count over each `TASK_CHECKLIST.md` (the tool's own regex, header taken from the real table header; script `scratchpad\b5-8\row6_recheck.py`) gives:

| Client | `required` rows | by status | naming a design check in `validation` |
|---|---|---|---|
| Dashboard | 12 | blocked 8, gated 2, todo 1, deferred 1 | 0 of 12 |
| PyApp | 8 | todo 4, done 2, blocked 1, gated 1 | 0 of 8 (6 dispatchable, 2 done) |
| AndroidApp | 24 | todo 19, gated 5 | 0 of 24 |

Cause: the tool picks the first line that contains a `|` and `design_context` as the header. Line 4 of each checklist is the prose line `Columns (Conductor schema, 15): ID | status | skill | design_context | baseline_id | area | …`, so the real table header (line 23 or 24) is never used. That line has no `validation` cell, `valIndex` is -1, and the loop skips. The row therefore passes after scanning one "checklist" with no rows. Under the row's own rule the true result would be a fail for all three clients (12, 6 and 24 dispatchable required rows with no design check named).

Owner of the fix, two parts:
- **The tool** (Kit finding, not editable here): select the header line by requiring both `design_context` and `validation` as exact cells. Proposed as `Q-B5-21`.
- **The validation cells**: the per-client plan-batch steps `B6a-7b`, `B6c-7b`, `B6b-7b` classify the rows and rewrite the cells to name `run-all.mjs` (never widened or deleted by this program, rule 4). `B5-7` repoints the six `skill` cells and does not touch `validation`. Until those run, row 6 is red in fact and green only by vacuity.

### 4.2 Row 2, PyApp and AndroidApp: "impeccable byte-different (.claude vs .github): SKILL.md"

Owner: `Q-B5-15`, answered (a) 2026-10-13, and ledger rows `B5-5`/`B5-6` ("Kit parity fails on impeccable per-runtime builds only (Kit finding)"). The three Kit skills (`design-gate`, `design-audit`, `gallery-governance`) pass in all four mirrors; the failure is impeccable 3.8.0's per-runtime builds. Dashboard passes because its four impeccable copies are one build. Accepted exit 1 for impeccable only; the fix is on the Kit side (the Kit finding, owner: the Kit session). Not owed by this program.

### 4.3 Row 7, all three clients: "integrator.md not deployed; implementer.md not deployed"

The tool looks for `<data_dir>\prompts\roles\integrator.md` and `implementer.md`. Facts, measured read-only:

- `C:\Programs\AI_Orchestrator_2` is the instance's install directory (`config.yaml`, `src`, `*.bat`); it has no `prompts` folder at all.
- That instance's `config.yaml` line 2 names `data_dir: C:\Conductor2\data`, and line 217 reads `roles: {}` (no role override configured). `C:\Conductor2\data` (listed only, its database never opened) has no `prompts\roles` either. So the result would be the same pointed at either directory.
- Instance-2 bindings are obsolete per the operator's 2026-10-13 answer ("We can keep repo structure but dont need to keep instance 2 bindings. They are obsolete."; runbook §3b item 10 lapsed). The absence of the two role overrides there is therefore **informational, not owed against any client**.
- The Kit's two templates exist and carry the check's sentinels: `anchoring-kit\conductor\roles\integrator.md` and `implementer.md` (first line "You are the integration role. …", guard text "If this repository contains `design/CONFIGURATION.md` …").

Owed (never written here): the two role overrides belong in the data directory of whichever Conductor instance is bound to these clients next (not instance 2). Proposed as owed item 19 in runbook §3b, owner `B8`/operator at the re-bind, folded with item 15 ("the instance's role overrides"). The deploy is a copy of the two Kit files into `<data_dir>\prompts\roles\`; a re-run of this tool with that `--conductor` is the proof.

### 4.4 Row 4, AndroidApp: "impeccable is installed but .github/hooks/impeccable.json is missing"

`PlantLibrary_AndroidApp/.claude/skills/impeccable` exists, `.github/` holds only `skills` and `workflows`, and no `.github/hooks` file is tracked. Dashboard and PyApp each track `.github/hooks/impeccable.json`. No lane-B5 step or ledger row owns the hook for AndroidApp: `B5-6` anchored the Kit and wrote the workflow, not the hook (`A4` §7.1 recorded "AndroidApp none"). Candidate owner: `B6b-1` (AndroidApp workspace bootstrap), as a one-file add taken from the Kit's packaged hook. Proposed as `Q-B5-22`.

### 4.5 Row 8: deferred in all three

Pending by construction (no evidence pack given). See §6 for the proposed deferred-validation row.

## §5 What the green rows did check

- Row 1: the seven `scripts/design/*` checks (`check-literals`, `check-banned-colors`, `check-drift`, `check-pin`, `check-gallery-coverage`, `run-all`, `check-parity`), `lib/resolve-roots.mjs`, `design/CONFIGURATION.md`, and the three skills in at least one mirror, in each client.
- Row 3: `<!-- design-kit:begin -->` and `:end` in `CLAUDE.md` and `AGENTS.md`, each client.
- Row 5: `.github/workflows/design-conformance.yml` exists and contains `run-all.mjs`, each client. The workflow needs two repository variables the operator sets (owed item 18, `Q-B5-13`); that is a runtime condition the static row cannot see.

## §6 Proposed rows (not written; the orchestrator files them)

| Id | Kind | Row |
|---|---|---|
| `Q-B5-21` | question | The Kit's row-6 header detection selects the prose `Columns (…)` line, so every PlantLibrary package passes row 6 vacuously (0 rows scanned). (a) record as a Kit finding for the next Kit session (exact-cell header match on `design_context` and `validation`), and re-run row 6 after `B6x-7b`; (b) work around in a client by moving the prose line; (c) accept. Recommended (a) |
| `Q-B5-22` | question | AndroidApp tracks impeccable without `.github/hooks/impeccable.json` (row 4 red). (a) `B6b-1` adds the Kit's packaged hook file; (b) accept the red row and record it; (c) remove impeccable. Recommended (a) |
| owed item 19 | owed | The two Conductor role overrides (`integrator.md`, `implementer.md`, from `anchoring-kit\conductor\roles\`) in the data directory of whichever Conductor instance is bound to the clients next; absent in instance 2 (obsolete, informational). Folds with item 15's role-overrides half; proof is this tool re-run with that `--conductor` |
| `DV-B5-04` | deferred validation | Readiness row 8 per anchored client: dispatch one batch containing a UI row (`design_context: required`) into the client through the bound Conductor, keep its evidence pack, and re-run `check-conductor-readiness.mjs --evidence <pack>`; skill: none (a Conductor dispatch, not a run-batch row); after the bind and after the client's `B6x-7b` has rewritten its validation cells (row 6 must be genuinely green first) |

(Ids are the next free at the time of writing; the orchestrator renumbers if parallel sessions took them.)

## §7 Verdict

Statically, none of the three clients is "ready" by the tool's own verdict, and the verdict is also too generous on row 6. The anchoring itself (rows 1, 3, 5) holds in all three. What stands between each client and a ready verdict:

| Client | Reds | Owner |
|---|---|---|
| Dashboard | row 7; row 6 vacuous | owed item 19 at the next bind; `B6a-7b` |
| PyApp | rows 2, 7; row 6 vacuous | Kit finding (accepted, `Q-B5-15`); owed item 19; `B6c-7b` |
| AndroidApp | rows 2, 4, 7; row 6 vacuous | Kit finding (accepted); `Q-B5-22`; owed item 19; `B6b-7b` |
