# Harness guards — step B7-1 evidence (2026-10-13)

*Step `B7-1` of the master rework program (`rework/PROMPTS_master-rework-runbook_2026-10-13.md` §3.3, lane
B7), Opus 5.5 · high, headless session in `C:\Programmierung\SW_Development` on `master`. Base `55a0a28`
(clean). Register rows executed: RC-A2-08, RC-A2-09, RC-A2-13, RC-A1-21. Q-A2-04 (a) assumed, as the block
says. Each script was run once, as a static check, over the working trees below. No test, build or app ran;
no submodule, package, skill, agent or instruction file was written.*

## §1 Pins at the run

| Repository | HEAD | Clean |
|---|---|---|
| SW_Development (super) | `55a0a28` + this step's four script/README files (uncommitted at the run) | yes, apart from those |
| PlantLibrary_AndroidApp | `5d6410f` | yes |
| PlantLibrary_Dashboard | `7795fc8` | yes |
| PlantLibrary_PyApp | `35ddc63` | yes |
| PlantLibrary_Server | `f1a31b9` | yes |
| PlantLibrary_SharedContracts | `d43f7a2` | yes |
| PlantLibrary_Workspace | `6b4b88b` | yes |
| Conductor checkout (parser source, read-only) | `C:/Programmierung/Orchestrator_System` @ `40598ae` (main) | parser file clean at HEAD |

Interpreter: Python 3.12.10, run as `PYTHONDONTWRITEBYTECODE=1 python -B …` from the superproject root. No
`.pyc` was written into the Conductor's `src/conductor/__pycache__` (newest `batch_package` entry still
2026-10-06).

## §2 The deliverables

| Deliverable | What changed |
|---|---|
| `scripts/harness/check_package_newlines.py` (new) | The package newline guard (RC-A2-13), the Conductor's `mixed_newline_line` rule over every git-tracked package folder of the seven repositories; live packages counted, frozen/archive listed |
| `scripts/harness/check_batch_packages.py` | Parser provenance printed (module path, git checkout and commit read with `--no-optional-locks`, or the instance's `_sync_stamp.json`); `--parser-src <src>` with a shadowing refusal; `sys.dont_write_bytecode` before the import; exit 1 only for counted packages, the four frozen Workspace packages listed; a missing live package is an error |
| `scripts/harness/check_harness_parity.py` | Multi-root (superproject + each present `.gitmodules` folder, absent ones skipped with a line); suite mirror compare of the five shared skills and the superproject's agents, CRLF→LF normalized; the run-batch commit-contract strings in every `run-batch/SKILL.md` copy (RC-A1-21); today's `.claude`↔`.codex` compare behind `--with-codex-compare` (default on); `--self-test` extended to ten plants |
| `scripts/harness/README.md` (new) | The inventory (one row per script), the folder's rules, the "which check after which edit" table, the known limits |

The block's "four static guards" are the newline guard, the parser census with provenance, the suite mirror
compare and the run-batch commit-contract check; the last two live in the one parity script, so the commit
carries three scripts.

## §3 Verdict lines

| Script | Verdict line | Exit |
|---|---|---|
| `check_package_newlines.py` | `package-newlines: pass — 0 mixed contract files in 7 counted packages (49 contract files) over 7 repositories, 0 skipped; 10 not-counted packages listed (0 mixed there)` | 0 |
| `check_batch_packages.py` | `batch-packages: pass — 0 errors in 7 counted packages (60 batches, 185 rows parsed clean); 4 frozen packages listed, 123 errors there not counted; parser C:\Programmierung\Orchestrator_System\src\conductor\batch_package.py` | 0 |
| `check_harness_parity.py --self-test` | `harness parity self-test: pass — 10 plants proven (suite PlantLibrary_AndroidApp); restored copy equals the baseline` | — |
| (same run, the real tree) | `harness parity: pass — 7 repositories (superproject + 6 suites, 0 skipped); codex compare on; 5 shared skills + agents per suite; run-batch commit contract` | 0 |

## §4 Output: the package newline guard

The run's console was cp1252; the `·` and `—` below are those bytes decoded, nothing else changed.

```text
  PlantLibrary_AndroidApp/implementation/MVP/package: frozen MVP (not counted) · 5 contract files (CRLF 0, LF 5) · mixed 0
  PlantLibrary_AndroidApp/implementation/System_V1_Implementation: live · 7 contract files (CRLF 0, LF 7) · mixed 0
  PlantLibrary_Dashboard/implementation/MVP/package: frozen MVP (not counted) · 5 contract files (CRLF 1, LF 4) · mixed 0
  PlantLibrary_Dashboard/implementation/System_V1_Implementation: live · 7 contract files (CRLF 0, LF 7) · mixed 0
  PlantLibrary_PyApp/implementation/Archive_PreMVP/Improvements/Python_Client_Sync: Archive_PreMVP (not counted) · 6 contract files (CRLF 4, LF 2) · mixed 0
  PlantLibrary_PyApp/implementation/System_V1_Implementation: live · 7 contract files (CRLF 1, LF 6) · mixed 0
  PlantLibrary_Server/implementation/MVP/package: frozen MVP (not counted) · 5 contract files (CRLF 1, LF 4) · mixed 0
  PlantLibrary_Server/implementation/System_V1_Implementation: live · 7 contract files (CRLF 0, LF 7) · mixed 0
  PlantLibrary_SharedContracts/implementation/MVP/package: frozen MVP (not counted) · 5 contract files (CRLF 1, LF 4) · mixed 0
  PlantLibrary_SharedContracts/implementation/System_V1_Implementation: live · 7 contract files (CRLF 0, LF 7) · mixed 0
  PlantLibrary_Workspace/implementation/System_Design_Architecture: live · 7 contract files (CRLF 0, LF 7) · mixed 0
  PlantLibrary_Workspace/implementation/System_Integration_MVP: frozen MVP (not counted) · 6 contract files (CRLF 0, LF 6) · mixed 0
  PlantLibrary_Workspace/implementation/System_Tooling: frozen Workspace package (not counted) · 7 contract files (CRLF 0, LF 7) · mixed 0
  PlantLibrary_Workspace/implementation/System_V1_Implementation: live · 7 contract files (CRLF 0, LF 7) · mixed 0
  PlantLibrary_Workspace/strategy/Cross_Platform_Strategy: frozen Workspace strategy tree (not counted) · 6 contract files (CRLF 6, LF 0) · mixed 0
  PlantLibrary_Workspace/system_description/PlantLibrary_System_Description: frozen Workspace system_description tree (not counted) · 6 contract files (CRLF 6, LF 0) · mixed 0
  PlantLibrary_Workspace/system_description/PlantLibrary_System_Description/completion/Missing_Context_Completion: frozen Workspace system_description tree (not counted) · 6 contract files (CRLF 6, LF 0) · mixed 0
package-newlines: pass — 0 mixed contract files in 7 counted packages (49 contract files) over 7 repositories, 0 skipped; 10 not-counted packages listed (0 mixed there)
exit=0
```

The superproject holds no tracked `BATCH_PLAN.md`, so it contributes no package. The 49 live contract files
are 48 LF and 1 CRLF (PyApp V1 `STATE.md`); a write to any of them keeps its own style.

**The do-not-fix set.** The mixed files measured by `AUDIT_git-structure_2026-10-13.md` §7.1, quoted
verbatim. None is a contract file of a live package (the frozen Workspace evidence `.txt` files are not
contract files), which is why the guard reports 0. No lane "fixes" any of them in passing:

> The `w/mixed` files (all `i/lf`) are the ones a lane must not "fix" in passing:
> - super: `.claude/skills/run-batch/SKILL.md`, `.codex/skills/run-batch/SKILL.md`, `.claude/skills/ui-ux-pro-max/data/landing.csv`, `.codex/skills/ui-ux-pro-max/data/landing.csv`.
> - Workspace: both `run-batch/SKILL.md`, `.claude/skills/ui-ux-pro-max/data/landing.csv`, `README.md`, four `docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_*.csv`, four frozen `implementation/System_Integration_MVP/validation/evidence/MVP-VALIDATION-20260708-01/EV-00[2-5]_*.txt`.
> - PyApp: both `run-batch/SKILL.md`, `.gitignore`, `pyproject.toml`, `GUI/screen_structures/Screen_Structure_plant_list.md`, `Screen_Structure_settings.md`.
> - AndroidApp: both `run-batch/SKILL.md`, three `build.gradle.kts`, eight `.kt` sources, `implementation/MVP/evidence/emulator_boot.log`.
> - Dashboard: both `run-batch/SKILL.md`.
> - Server: both `run-batch/SKILL.md`, `app/api/routes/plants.py`, `app/core/config.py`, `app/main.py`, `app/storage/object_storage.py`, `app/sync/registry.py`, `deploy/docker-compose.dev.yml`, two files under `tests/`.
> - SharedContracts: both `run-batch/SKILL.md`, three `api-examples/*.example.json`, `scripts/validate_contracts.py`.

## §5 Output: the batch-package census

```text
parser: C:\Programmierung\Orchestrator_System\src\conductor\batch_package.py
parser checkout: C:/Programmierung/Orchestrator_System @ 40598ae (main; parser file clean at HEAD)
PlantLibrary_AndroidApp/implementation/System_V1_Implementation [live]: OK 15 batches 39 rows :: AN1-B00=already_done, AN1-B01=will_run, AN1-B02=will_run, AN1-B03=will_run, AN1-B04=will_run, AN1-B05=will_run, AN1-B06=will_run, AN1-B07=will_run, AN1-B08=will_run, AN1-B11=will_run, AN1-B09=blocked, AN1-B12=already_done, AN1-B13=will_run, AN1-B14=already_done, AN1-B10=blocked
PlantLibrary_Dashboard/implementation/System_V1_Implementation [live]: OK 8 batches 22 rows :: WD1-B01=already_done, WD1-B02=already_done, WD1-B04=already_done, WD1-B06=will_run, WD1-B05=will_run, WD1-B07=already_done, WD1-B08=will_run, WD1-B00=will_run
PlantLibrary_PyApp/implementation/System_V1_Implementation [live]: OK 9 batches 20 rows :: PY1-B08=will_run, PY1-B01=blocked, PY1-B02=blocked, PY1-B03=already_done, PY1-B05=blocked, PY1-B04=will_run, PY1-B07=already_done, PY1-B06=will_run, PY1-B00=will_run
PlantLibrary_Server/implementation/System_V1_Implementation [live]: OK 7 batches 36 rows :: SV1-B00=will_run, SV1-B01=blocked, SV1-B02=blocked, SV1-B03=blocked, SV1-B04=blocked, SV1-B06=will_run, SV1-B07=will_run
PlantLibrary_SharedContracts/implementation/System_V1_Implementation [live]: OK 4 batches 10 rows :: SC1-B01=already_done, SC1-B00=will_run, SC1-B02=will_run, SC1-B03=will_run
PlantLibrary_Workspace/implementation/System_Design_Architecture [live]: OK 9 batches 42 rows :: SDA-B00=will_run, SDA-B01=blocked, SDA-B02=blocked, SDA-B03=will_run, SDA-B04=will_run, SDA-B05=blocked, SDA-B06=blocked, SDA-B07=blocked, SDA-B08=will_run
PlantLibrary_Workspace/implementation/System_Integration_MVP [frozen, not counted]: 25 errors -> {'no 15-column': 1, 'declares missing primary row': 24}
PlantLibrary_Workspace/implementation/System_Tooling [frozen, not counted]: 6 errors -> {'no 15-column': 1, 'declares missing primary row': 5}
PlantLibrary_Workspace/implementation/System_V1_Implementation [live]: OK 8 batches 16 rows :: SY1-B00=already_done, SY1-B01=will_run, SY1-B02=will_run, SY1-B03=will_run, SY1-B04=will_run, SY1-B05=blocked, SY1-B06=already_done, SY1-B07=will_run
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
exit=0
```

Totals and classifications equal `AUDIT_batch-packages_2026-10-13.md` §7.1 (60 batches, 185 rows, 0 errors on
the live set; frozen 25/6/30/62), now under the Conductor's main at `40598ae` instead of `2e7adb3`. The parser
judged is main's, not instance 2's (F-A7-02); this step ran the census once, so the instance-2 run with
`--parser-src C:\Programs\AI_Orchestrator_2\src` belongs to B4's static proof.

## §6 Output: the parity checker and its planted-drift self-check

```text
harness parity self-test: ok: codex compare: skill byte-different: run-batch/SKILL.md
harness parity self-test: ok: suite skill: PlantLibrary_AndroidApp: skill differs from the superproject's: plan-batch/SKILL.md
harness parity self-test: ok: suite skill folder: PlantLibrary_AndroidApp: missing shared skill folder test-driven-development
harness parity self-test: ok: suite agent: PlantLibrary_AndroidApp: agent differs from the superproject's: batch-closeout-reviewer.md
harness parity self-test: ok: suite agent missing: PlantLibrary_AndroidApp: agent missing: batch-closeout-reviewer.md
harness parity self-test: ok: extra-skill table: PlantLibrary_AndroidApp: missing shared skill folder systematic-debugging
harness parity self-test: ok: run-batch required string: PlantLibrary_AndroidApp/.claude/skills/run-batch/SKILL.md lacks 'Commit: proposed for orchestrator'
harness parity self-test: ok: run-batch retired string: .codex/skills/run-batch/SKILL.md carries retired 'Commit command:'
harness parity self-test: ok: multi-root skip: skipped PlantLibrary_AndroidApp, no diagnostic
harness parity self-test: ok: LF normalization: a CRLF<->LF flip of run-batch/SKILL.md is not drift
harness parity self-test: pass — 10 plants proven (suite PlantLibrary_AndroidApp); restored copy equals the baseline
harness parity: note: PlantLibrary_PyApp: same-name skill folders listed, not compared: gui-validation
harness parity: note: PlantLibrary_Workspace: same-name skill folders listed, not compared: design-adoption, gui-validation, sync-contracts, ui-ux-pro-max, verify-stack, webapp-testing
harness parity: pass — 7 repositories (superproject + 6 suites, 0 skipped); codex compare on; 5 shared skills + agents per suite; run-batch commit contract
exit=0
```

The self-check is a static mode of the checker: it copies the `.claude/` and `.codex/` skill and agent trees
of the seven repositories into the system temp folder, plants one drift per check, proves each is reported,
restores each plant and proves the copy equals its baseline, and then checks the real tree. The copy is
removed at the end.

Two notes the green verdict hides:
- **Not compared today.** PyApp's `gui-validation` (a pointer stub, LF-different from the superproject's) and
  Workspace's six PlantLibrary-only copies (`verify-stack/SKILL.md` LF-different from the superproject's) are
  listed, not compared, until B1 mirrors the RC-A1-22 set and fills `SUITE_EXTRA_SKILLS` (Q-A1-04).
- **One behaviour change in the codex compare.** It now compares LF-normalized content rather than raw bytes.
  Today both trees are byte-equal, so the verdict is the same; a pure line-ending difference between a
  `.claude` file and its `.codex` mirror no longer counts as drift.

## §7 Not done

Nothing. Deferred to their own steps, as the block says: the Codex freeze (B7-2), the docs link checker
(B7-3), the instance-2 parser census (B4's static proof), the RC-A1-22 additions to the parity table (B1).
