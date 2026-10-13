# Bind proof - step B4-5 evidence (2026-10-13)

*Step `B4-5` of the master rework program (`rework/PROMPTS_master-rework-runbook_2026-10-13.md` §3.6),
Sonnet 5.5 · high, check route, headless session in `C:\Programmierung\SW_Development` on `master`. Base
`20aba6e` (clean). The proof list is `AUDIT_batch-packages_2026-10-13.md` §7.2 "What B4's static proof must show"
and §7.5 "What a B4 static check must prove". Rescoped at `R-4.1`: the instance-2 bindings are obsolete
(Q-G-02 / Q-A8-02, 2026-10-13), so instance 2's parser leg is informational and the PyApp plan-contract hash is
quoted as a fact, not a gate. Everything below is static: no instance REST call, no database read, no test, no
build, no app launch; sources and the instance read-only; bytecode writing disabled (`python -B`,
`PYTHONDONTWRITEBYTECODE=1`).*

## §0 Verdict

| # | Proof (§7.5 item) | Result |
|---|---|---|
| 1 | Parse-clean under both parsers | PASS under main's parser (0 errors, 7 counted packages, 60 batches, 185 rows); instance 2's parser (informational) gives the identical result |
| 2 | Required files committed, suite trees clean | PASS - 28 of 28 required files tracked; six suites `git status --porcelain` empty; superproject clean at `20aba6e` |
| 3 | Each git toplevel is the suite folder | PASS - 7 of 7 packages resolve to their suite folder (Workspace twice) |
| 4 | Package path is `<root>\<relative>` under the `config.yaml` root | PASS - six roots read once and exist; seven relative paths exist |
| 5 | PyApp plan contract (a fact, not a gate) | `c6e3b3109fdc2d9b84cda30a37a47878c9cb70ce2aca0b21cc89a2dd71658122` before B4 and after: identical |
| 6 | No `not_yet_detailed`; classification changes explained | PASS - 0 `not_yet_detailed`; two packages changed classification against the audit baseline, both explained by a STATE decision |

One correction to the step block's wording, which affects no verdict: the commit named as "the last commit
before B4-2" (`791da51`) is a descendant of B4-2 (`e8b738d` is its ancestor); see §5. The tree before B4 is
`35ddc63`, and the audit's baseline tree `0be0e5a` is hashed too.

## §1 Pins at the run

| Repository | HEAD | Branch | `git status --porcelain` |
|---|---|---|---|
| SW_Development (super) | `20aba6e` rework: B4-4 - bump five gitlinks; ledger B4-4 | master | empty |
| PlantLibrary_AndroidApp | `a0f614a` | main | empty |
| PlantLibrary_Dashboard | `57ecc25` | main | empty |
| PlantLibrary_PyApp | `2bd98b2` | main | empty |
| PlantLibrary_Server | `6dd192b` | main | empty |
| PlantLibrary_SharedContracts | `c3ab790` | main | empty |
| PlantLibrary_Workspace | `88a6226` | main | empty |
| Conductor checkout (main parser, read-only) | `C:/Programmierung/Orchestrator_System` @ `7610926` | main | parser file clean at HEAD |
| Instance 2 parser (read-only) | `C:\Programs\AI_Orchestrator_2\src` | not a git checkout | `_sync_stamp.json`: v2.1587 synced from `a900174` at 2026-10-02T22:43:54Z |

Interpreter: Python 3.12.10.

## §2 Proof 1 - the census under both parsers

Command, run once per parser from `C:\Programmierung\SW_Development` (both exit 0):

```text
PYTHONDONTWRITEBYTECODE=1 python -B scripts/harness/check_batch_packages.py
PYTHONDONTWRITEBYTECODE=1 python -B scripts/harness/check_batch_packages.py --parser-src C:/Programs/AI_Orchestrator_2/src
```

### §2.1 Main's parser (default; the gate)

```text
parser: C:\Programmierung\Orchestrator_System\src\conductor\batch_package.py
parser checkout: C:/Programmierung/Orchestrator_System @ 7610926 (main; parser file clean at HEAD)
PlantLibrary_AndroidApp/implementation/System_V1_Implementation [live]: OK 15 batches 39 rows :: AN1-B00=already_done, AN1-B01=will_run, AN1-B02=will_run, AN1-B03=will_run, AN1-B04=will_run, AN1-B05=will_run, AN1-B06=will_run, AN1-B07=will_run, AN1-B08=will_run, AN1-B11=will_run, AN1-B09=blocked, AN1-B12=already_done, AN1-B13=will_run, AN1-B14=already_done, AN1-B10=blocked
PlantLibrary_Dashboard/implementation/System_V1_Implementation [live]: OK 8 batches 22 rows :: WD1-B01=already_done, WD1-B02=already_done, WD1-B04=already_done, WD1-B06=will_run, WD1-B05=will_run, WD1-B07=already_done, WD1-B08=will_run, WD1-B00=will_run
PlantLibrary_PyApp/implementation/System_V1_Implementation [live]: OK 9 batches 20 rows :: PY1-B08=will_run, PY1-B01=blocked, PY1-B02=blocked, PY1-B03=already_done, PY1-B05=blocked, PY1-B04=will_run, PY1-B07=already_done, PY1-B06=will_run, PY1-B00=will_run
PlantLibrary_Server/implementation/System_V1_Implementation [live]: OK 7 batches 36 rows :: SV1-B00=will_run, SV1-B01=blocked, SV1-B02=blocked, SV1-B03=blocked, SV1-B04=blocked, SV1-B06=blocked, SV1-B07=will_run
PlantLibrary_SharedContracts/implementation/System_V1_Implementation [live]: OK 4 batches 10 rows :: SC1-B01=already_done, SC1-B00=will_run, SC1-B02=will_run, SC1-B03=will_run
PlantLibrary_Workspace/implementation/System_Design_Architecture [live]: OK 9 batches 42 rows :: SDA-B00=already_done, SDA-B01=already_done, SDA-B02=already_done, SDA-B03=already_done, SDA-B04=already_done, SDA-B05=already_done, SDA-B06=already_done, SDA-B07=already_done, SDA-B08=already_done
PlantLibrary_Workspace/implementation/System_Integration_MVP [frozen, not counted]: 25 errors -> {'no 15-column': 1, 'declares missing primary row': 24}
PlantLibrary_Workspace/implementation/System_Tooling [frozen, not counted]: 6 errors -> {'no 15-column': 1, 'declares missing primary row': 5}
PlantLibrary_Workspace/implementation/System_V1_Implementation [live]: OK 8 batches 16 rows :: SY1-B00=already_done, SY1-B01=will_run, SY1-B02=will_run, SY1-B03=will_run, SY1-B04=will_run, SY1-B07=will_run, SY1-B05=blocked, SY1-B06=already_done
PlantLibrary_Workspace/strategy/Cross_Platform_Strategy [frozen, not counted]: 30 errors -> {'no 15-column': 1, 'declares missing primary row': 29}
PlantLibrary_Workspace/system_description/PlantLibrary_System_Description [frozen, not counted]: 62 errors -> {'no 15-column': 1, 'duplicate': 46, 'declares missing primary row': 15}
    duplicate context anchor Intent
    duplicate context anchor Output
    duplicate context anchor Validation
    duplicate context anchor Intent
    duplicate context anchor Output
    duplicate context anchor Validation
    duplicate context anchor Intent
    duplicate context anchor Output
    … 38 more
batch-packages: pass — 0 errors in 7 counted packages (60 batches, 185 rows parsed clean); 4 frozen packages listed, 123 errors there not counted; parser C:\Programmierung\Orchestrator_System\src\conductor\batch_package.py
```

### §2.2 Instance 2's parser (`--parser-src`; informational under the 2026-10-13 rescope)

```text
parser: C:\Programs\AI_Orchestrator_2\src\conductor\batch_package.py
parser checkout: not a git checkout
parser stamp: v2.1587 synced from a900174 at 2026-10-02T22:43:54.1740833Z
PlantLibrary_AndroidApp/implementation/System_V1_Implementation [live]: OK 15 batches 39 rows :: AN1-B00=already_done, AN1-B01=will_run, AN1-B02=will_run, AN1-B03=will_run, AN1-B04=will_run, AN1-B05=will_run, AN1-B06=will_run, AN1-B07=will_run, AN1-B08=will_run, AN1-B11=will_run, AN1-B09=blocked, AN1-B12=already_done, AN1-B13=will_run, AN1-B14=already_done, AN1-B10=blocked
PlantLibrary_Dashboard/implementation/System_V1_Implementation [live]: OK 8 batches 22 rows :: WD1-B01=already_done, WD1-B02=already_done, WD1-B04=already_done, WD1-B06=will_run, WD1-B05=will_run, WD1-B07=already_done, WD1-B08=will_run, WD1-B00=will_run
PlantLibrary_PyApp/implementation/System_V1_Implementation [live]: OK 9 batches 20 rows :: PY1-B08=will_run, PY1-B01=blocked, PY1-B02=blocked, PY1-B03=already_done, PY1-B05=blocked, PY1-B04=will_run, PY1-B07=already_done, PY1-B06=will_run, PY1-B00=will_run
PlantLibrary_Server/implementation/System_V1_Implementation [live]: OK 7 batches 36 rows :: SV1-B00=will_run, SV1-B01=blocked, SV1-B02=blocked, SV1-B03=blocked, SV1-B04=blocked, SV1-B06=blocked, SV1-B07=will_run
PlantLibrary_SharedContracts/implementation/System_V1_Implementation [live]: OK 4 batches 10 rows :: SC1-B01=already_done, SC1-B00=will_run, SC1-B02=will_run, SC1-B03=will_run
PlantLibrary_Workspace/implementation/System_Design_Architecture [live]: OK 9 batches 42 rows :: SDA-B00=already_done, SDA-B01=already_done, SDA-B02=already_done, SDA-B03=already_done, SDA-B04=already_done, SDA-B05=already_done, SDA-B06=already_done, SDA-B07=already_done, SDA-B08=already_done
PlantLibrary_Workspace/implementation/System_Integration_MVP [frozen, not counted]: 25 errors -> {'no 15-column': 1, 'declares missing primary row': 24}
PlantLibrary_Workspace/implementation/System_Tooling [frozen, not counted]: 6 errors -> {'no 15-column': 1, 'declares missing primary row': 5}
PlantLibrary_Workspace/implementation/System_V1_Implementation [live]: OK 8 batches 16 rows :: SY1-B00=already_done, SY1-B01=will_run, SY1-B02=will_run, SY1-B03=will_run, SY1-B04=will_run, SY1-B07=will_run, SY1-B05=blocked, SY1-B06=already_done
PlantLibrary_Workspace/strategy/Cross_Platform_Strategy [frozen, not counted]: 30 errors -> {'no 15-column': 1, 'declares missing primary row': 29}
PlantLibrary_Workspace/system_description/PlantLibrary_System_Description [frozen, not counted]: 62 errors -> {'no 15-column': 1, 'duplicate': 46, 'declares missing primary row': 15}
    duplicate context anchor Intent
    duplicate context anchor Output
    duplicate context anchor Validation
    duplicate context anchor Intent
    duplicate context anchor Output
    duplicate context anchor Validation
    duplicate context anchor Intent
    duplicate context anchor Output
    … 38 more
batch-packages: pass — 0 errors in 7 counted packages (60 batches, 185 rows parsed clean); 4 frozen packages listed, 123 errors there not counted; parser C:\Programs\AI_Orchestrator_2\src\conductor\batch_package.py
```

Comparison: the package lines (seven live, four frozen) are identical between the two runs; the runs differ only
in the provenance lines at the top and the parser path on the last line. Both verdict lines read `batch-packages:
pass — 0 errors in 7 counted packages (60 batches, 185 rows parsed clean)`. The four frozen Workspace packages (123
errors) are listed and not counted, as at `B7-1`.

## §3 Proofs 2 and 3 - required files tracked, trees clean, git toplevels

Required files per `batch_package.py:53-58`: `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`.
`git -C <suite> ls-files --error-unmatch implementation/<package>/<file>` returned the path for all 28 (7 packages
x 4 files). Every suite's `git status --porcelain` is empty (§1), so what intake would hash from disk equals the
committed content.

`git -C <package> rev-parse --show-toplevel`:

| Package | Toplevel | = suite folder |
|---|---|---|
| `PlantLibrary_AndroidApp/implementation/System_V1_Implementation` | `C:/Programmierung/SW_Development/PlantLibrary_AndroidApp` | yes |
| `PlantLibrary_Dashboard/implementation/System_V1_Implementation` | `C:/Programmierung/SW_Development/PlantLibrary_Dashboard` | yes |
| `PlantLibrary_PyApp/implementation/System_V1_Implementation` | `C:/Programmierung/SW_Development/PlantLibrary_PyApp` | yes |
| `PlantLibrary_Server/implementation/System_V1_Implementation` | `C:/Programmierung/SW_Development/PlantLibrary_Server` | yes |
| `PlantLibrary_SharedContracts/implementation/System_V1_Implementation` | `C:/Programmierung/SW_Development/PlantLibrary_SharedContracts` | yes |
| `PlantLibrary_Workspace/implementation/System_V1_Implementation` | `C:/Programmierung/SW_Development/PlantLibrary_Workspace` | yes |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture` | `C:/Programmierung/SW_Development/PlantLibrary_Workspace` | yes |

Workspace V1 and SDA share one git root (the shared-tree acknowledgement of `intake.py:715-720`); that is
unchanged since step 5 and, with the bindings obsolete, only informational.

## §4 Proof 4 - package path under the configured root

`C:\Programs\AI_Orchestrator_2\config.yaml` lines 500-520 read once; `intake.batch_package_roots` is lines 505-517:

```text
  batch_package_roots:
  - id: pyapp
    path: C:\Programmierung\SW_Development\PlantLibrary_PyApp\implementation
  - id: server
    path: C:\Programmierung\SW_Development\PlantLibrary_Server\implementation
  - id: androidapp
    path: C:\Programmierung\SW_Development\PlantLibrary_AndroidApp\implementation
  - id: dashboard
    path: C:\Programmierung\SW_Development\PlantLibrary_Dashboard\implementation
  - id: sharedcontracts
    path: C:\Programmierung\SW_Development\PlantLibrary_SharedContracts\implementation
  - id: workspace
    path: C:\Programmierung\SW_Development\PlantLibrary_Workspace\implementation
```

All six root directories exist. Each package path is `<root>\<relative>`: relative `System_V1_Implementation` for
the six V1 packages, `System_Design_Architecture` for SDA under the `workspace` root; all seven directories exist
(§3). With the bindings obsolete this is a statement about shape, not a claim that instance 2 holds a live binding.

## §5 Proof 5 - PyApp plan-contract hash, a fact

`conductor.batch_package.parse_package(<path>).plan_contract_sha256`, main's parser
(`C:\Programmierung\Orchestrator_System\src\conductor\batch_package.py`), on `git archive <commit>
implementation/System_V1_Implementation` extracts in scratch (never in the repository) and on the live tree. The
script lives in scratch outside the extracts and ran with `python -B -I`; the hash is computed by the parser and
nothing else.

| Tree | Commit | `plan_contract_sha256` |
|---|---|---|
| audit baseline (package migrated to 15 columns) | `0be0e5a` | `c6e3b3109fdc2d9b84cda30a37a47878c9cb70ce2aca0b21cc89a2dd71658122` |
| before B4 (parent of B4-2 `e8b738d`) | `35ddc63` | `c6e3b3109fdc2d9b84cda30a37a47878c9cb70ce2aca0b21cc89a2dd71658122` |
| named in the launch note | `791da51` | `c6e3b3109fdc2d9b84cda30a37a47878c9cb70ce2aca0b21cc89a2dd71658122` |
| after B4 (HEAD, extract) | `2bd98b2` | `c6e3b3109fdc2d9b84cda30a37a47878c9cb70ce2aca0b21cc89a2dd71658122` |
| after B4 (live working tree, clean) | `2bd98b2` | `c6e3b3109fdc2d9b84cda30a37a47878c9cb70ce2aca0b21cc89a2dd71658122` |

The hash is unchanged across B4 and equals the value the launch note expected. `791da51` ("M-9 - PYAPP_V1_PROPOSAL
released and renamed") lies after `e8b738d` (B4-2) in PyApp's history (`git merge-base --is-ancestor e8b738d
791da51` true), so it is not the tree before B4; the true pre-B4 tree is `35ddc63`, the parent of `e8b738d`. The
result is the same at all four commits. Q-A7-04 (the PyApp plan contract stays) therefore holds as a fact; no
re-intake is owed, and the hash is no longer a gate.

## §6 Proof 6 - classification and `not_yet_detailed`

Neither census run prints a `not_yet_detailed` batch (0 hits over both outputs). Against the baseline of
`AUDIT_batch-packages_2026-10-13.md` §7.1, counted as will_run / already_done / blocked:

| Package | Audit baseline | Now | Explained by |
|---|---|---|---|
| PyApp V1 | 4 / 2 / 3 | 4 / 2 / 3 | unchanged |
| Server V1 | 3 / 0 / 4 | 2 / 0 / 5 | STATE.md "rework B4: SV1-B06 Requires expanded" (range token `SV1-B00..B04` replaced by five tokens; `SV1-B06` now classifies blocked) |
| SharedContracts V1 | 3 / 1 / 0 | 3 / 1 / 0 | unchanged (the `SC1-B02` token expansion changes no classification) |
| Dashboard V1 | 4 / 4 / 0 | 4 / 4 / 0 | unchanged |
| AndroidApp V1 | 10 / 3 / 2 | 10 / 3 / 2 | unchanged |
| Workspace V1 | 5 / 2 / 1 | 5 / 2 / 1 | unchanged; batch order differs (`SY1-B07` before `SY1-B05`) by STATE.md "rework B4: SY1-B07 moved before SY1-B05" |
| Workspace SDA | 4 / 0 / 5 | 0 / 9 / 0 | STATE.md "rework B4: package superseded by the rework design lanes" (`B4-3`): nine batches already_done |

Totals are unchanged (60 batches, 185 rows). Every classification difference has a dated STATE.md decision line in
the owning package.

## §7 What was not done

No instance REST call, no database read, no write to any suite, no test. No `Q-B4-` row proposed. Scratch (the
extracts, the census captures, the hashing script) stays in the session scratchpad and is not committed.
