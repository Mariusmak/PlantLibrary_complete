---
name: harness-upkeep
description: Which static check follows which edit in the PlantLibrary superproject and its suites, in what order, and the line each prints on success - the harness parity check after a skill, agent, `.agents/README.md`, `.codex/**` or `AGENTS.md` edit, the package checks after a batch-package edit, the hygiene checker after any markdown edit, and the Kit's parity check after a Kit install. Use in an operator session after editing any of those or a script under scripts/harness/. Operator-session only; never a row skill; it names no test run as proof.
disable-model-invocation: true
---

<!-- harness-upkeep skill version: 0.1.0-pl (2026-10-13) - adapted at master rework
     step B1-1 (RC-A1-12) from the Conductor's harness-upkeep 0.1.0
     (Orchestrator_System @ 2e7adb3, read-only) to the superproject's checks as
     B7-1 wrote and B7-2 extended them; the Conductor's v5, Section Map and
     duration-history rows are dropped. The inventory of every script, with all
     its flags, is `scripts/harness/README.md`. -->

None of these checks is a test run, and none of them is a row's proof: a
row's proof is its `validation` cell. All of them are static and read-only;
`check_harness_parity.py --self-test` works on temporary copies outside the
repository and removes them. Run every check from the superproject root
(`C:\Programmierung\SW_Development`) with `python -B`.

## 1. After which edit, which check

| Edit | Check, in this order | Success line |
|---|---|---|
| a skill or agent definition under `.claude/` of the superproject or a suite, or `.agents/README.md` | `python -B scripts/harness/check_harness_parity.py`: the Codex freeze in every repository, bridge coverage (every superproject `.claude/skills/*` folder is a frozen bridge row or a `## Claude-only skills` row of `.agents/README.md`), the suite mirrors of the shared skills, the suite's `SUITE_EXTRA_SKILLS` and the agents, and the run-batch commit contract. A new or changed Claude-only skill gets its `.agents/README.md` row in the same commit; a superproject change to a mirrored skill or agent is copied to every suite mirror before the parity check can pass | `harness parity: pass — …` |
| a PlantLibrary-only skill mirrored into a suite | the skill joins that suite's `SUITE_EXTRA_SKILLS` row in `check_harness_parity.py` in the same commit, then the parity check | `harness parity: pass — …` |
| anything under `.codex/**`, or `AGENTS.md` outside its installer-owned blocks | none applies: these are frozen (`D-2026-10-13-03`); restore the file from its freeze commit, then the parity check | `harness parity: pass — …` |
| a script under `scripts/harness/` | its row in `scripts/harness/README.md` in the same commit (the folder's truth rule); for `check_harness_parity.py`, `python -B scripts/harness/check_harness_parity.py --self-test` (its plants on a temporary copy, then the live check) | the self-test's plant lines, then `harness parity: pass — …` |
| a package contract file (`README.md`, `SCOPE.md`, `CONTEXT_INDEX.md`, `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`) | `python -B scripts/harness/check_package_newlines.py`, then `python -B scripts/harness/check_batch_packages.py` | `package-newlines: pass — …`, then `batch-packages: pass — …` |
| a new package, or a package frozen or archived | the classification tables at the top of both package checks, in the same commit, then both package checks | as above |
| any markdown file, `CLAUDE.md` or `AGENTS.md`, in the repository that holds it | `python scripts/hygiene/repo_hygiene_check.py check` | `repo-hygiene: pass — 0 violations, …` or `repo-hygiene: pass with holds — 0 violations, …` |
| the Kit skills (`design-gate`, `design-audit`, `gallery-governance`, `impeccable`) in a suite | edited through the Design Template Kit only; after a Kit install, the Kit's `node scripts/design/check-parity.mjs` in that suite (its four mirrors), then the harness parity check | `design-kit parity: pass`, then `harness parity: pass — …` |

## 2. What the parity check covers

`scripts/harness/README.md` lists its checks, flags and diagnostics. Since
the Codex freeze (`D-2026-10-13-03`, step `B7-2`) it checks that `.codex/**`
(the four Kit folders excepted) and `AGENTS.md` outside its installer-owned
marker blocks are unchanged since each repository's freeze commit, instead
of comparing them with `.claude/**` and `CLAUDE.md`. The `.claude` ↔
`.codex` compare stays defined behind `--with-codex-compare` for an unfreeze.

## 3. On a failure

Fix the file the diagnostic names and run the same check again; never re-run
an unchanged check on an unchanged tree. A diagnostic about a frozen
`.codex/**` path or `AGENTS.md` means something edited a frozen file:
restore it from the freeze commit, never re-mirror. A suite-mirror
diagnostic after a superproject skill or agent change means the suite copy
has not been refreshed yet: copy the superproject's bytes into the suite in
the suite's own commit, keeping the suite file's line endings.

## 4. Report and stop

```text
Harness upkeep: <edit> -> <checks run, in order>: <success lines or the first diagnostic>
```
