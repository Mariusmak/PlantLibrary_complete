# scripts/harness — the superproject's static guards

This index **is** the inventory of the superproject's harness scripts. Every script here is a static
check or a one-off migration tool: Python stdlib only, read-only unless its row says otherwise, no
bytecode written, and none of them launches an app, a build or a test of any kind. The checks cover the
superproject and every submodule folder named in `.gitmodules` that is present; an absent submodule
folder is skipped with a printed line, never failed.

Written at step `B7-1` of the master rework program
(`rework/PROMPTS_master-rework-runbook_2026-10-13.md` §3.3) on 2026-10-13, on base `55a0a28`; its run
evidence is `rework/EVIDENCE_harness-guards_2026-10-13.md`. Rules adapted from the Conductor's
`docs/harness/README.md` (Orchestrator_System, read-only).

## The folder's rules

1. **One row per script.** Every file in this folder has exactly one row in the inventory below.
2. **The row.** Purpose, invocation and every flag, what it reads and writes, exit codes and the
   verdict line, the register row it implements, the owning lane, and the commit its row was verified
   at.
3. **One verdict line, three exit codes.** A check prints its findings, then exactly one verdict line
   `<name>: pass — …`, `<name>: fail — …` or `<name>: error — could not run: …`, and exits 0 (pass),
   1 (findings) or 2 (could not run), like the hygiene kit's checker.
4. **Static and read-only.** A check never fixes what it finds. It reads git facts with
   `git --no-optional-locks` only and never runs a git write command, in this repository, a submodule
   or the Conductor checkout. It sets `sys.dont_write_bytecode` before any import; run it with
   `python -B` as well.
5. **The truth rule.** A row describes what the script does at its verified commit. A row that is no
   longer true is a defect. A step that changes a script updates its row, and the verified commit, in
   the same commit.
6. **No proof surface.** This page names the static checks only. A batch row's proof is its
   `validation` cell, never a line of this page, and this page names no test runner.
7. **Self-checks are static.** A `--self-test` mode works on temporary copies outside the repository,
   plants one defect per check, proves each is reported, and then checks the real tree. It is a mode of
   the checker, not a test.

## The inventory

| Script | Purpose | Invocation and flags | Reads · writes | Exit and verdict line | Register · lane | Verified at |
|---|---|---|---|---|---|---|
| `check_harness_parity.py` | Harness mirrors: (1) the superproject's `.claude/skills` against `.codex/skills` (`validate-real-stack/SKILL.md` may differ) and the agent stem pairing `.md`↔`.toml`; (2) in each present suite, the five shared skills (`plan-batch`, `real-stack-testing`, `run-batch`, `test-driven-development`, `validate-real-stack`), any skill on the suite's `SUITE_EXTRA_SKILLS` row, and every superproject `.claude/agents/*.md` equal to the superproject's copy; (3) the run-batch commit-proposal strings (four required, two retired) in every `run-batch/SKILL.md` copy. Every content compare normalizes CRLF to LF; `__pycache__/` is ignored. Same-name suite skill folders outside the compared set are listed as notes | `python -B scripts/harness/check_harness_parity.py [--self-test] [--with-codex-compare \| --no-with-codex-compare]`. `--self-test`: ten plants on a temporary copy (one per check, plus the extra-skill table, the multi-root skip and a CRLF↔LF flip that must not count), then the real verdict. `--with-codex-compare`: on by default; `B7-2` switches it off when the Codex freeze lands | reads the working-tree `.claude/` and `.codex/` trees of all seven repositories and `.gitmodules` · writes nothing (the self-test's copy lives in the system temp folder and is removed) | 0 · 1 · 2; `harness parity: pass — 7 repositories (superproject + 6 suites, 0 skipped); …` | RC-A2-08, RC-A1-21; Q-A2-04 (a) assumed · `B7` (`B7-2` adds the freeze) | `B7-1` |
| `check_package_newlines.py` | Package contract files (`README.md`, `SCOPE.md`, `CONTEXT_INDEX.md`, `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`) hold one line-ending style each. A package is a git-tracked folder holding a tracked `BATCH_PLAN.md`. The seven live packages (and any unclassified one) are counted; frozen MVP, `Archive_PreMVP`, archive and the frozen Workspace trees are listed, not counted | `python -B scripts/harness/check_package_newlines.py` (no flags) | `git ls-files` per repository; tracked files only, `.tmp/` never; the working-tree bytes · writes nothing, fixes nothing | 0 · 1 · 2; `package-newlines: pass — 0 mixed contract files in 7 counted packages …` | RC-A2-13 · `B7` | `B7-1` |
| `check_batch_packages.py` | Census of every package through the Conductor's own parser (`conductor.batch_package.parse_package`), printing the parser's provenance first: module path, its git checkout and commit, or the instance's `_sync_stamp.json`. The seven live packages are counted; the four frozen Workspace packages are listed | `python -B scripts/harness/check_batch_packages.py [--parser-src <src>]`. `--parser-src`: a `src` folder holding `conductor/`, put first on the path; refused (exit 2) if another install shadows it. Without it: the importable `conductor`, else `CONDUCTOR_SRC`, else instance 2's `src` | the package folders under each suite's `implementation/` and Workspace `strategy/`, `system_description/`; the parser module; git facts of the parser checkout · writes nothing | 0 · 1 · 2; `batch-packages: pass — 0 errors in 7 counted packages (…); … parser <path>` | RC-A2-09; F-A7-02 · `B7`, used by `B4` | `B7-1` |
| `migrate_checklist_schema.py` | One-off migration of a package's `TASK_CHECKLIST.md` from the 14-column V3 schema to the Conductor's 15-column schema, keeping the file's line endings (onboarding runbook Appendix B). **Writes** the checklist it is given; refuses an already-migrated one. Not a check | see its docstring | the named checklist and `BATCH_PLAN.md` · rewrites the named `TASK_CHECKLIST.md` | see its docstring | onboarding steps 2a/2b · closed | not re-verified at `B7-1` |

## Which check after which edit

| The edit | The check(s) |
|---|---|
| any file under `.claude/skills/**` or `.claude/agents/**`, in the superproject or a suite | `check_harness_parity.py` |
| any file under `.codex/**` | `check_harness_parity.py` (the codex compare; after `B7-2`, the freeze) |
| a mirror of a PlantLibrary-only skill added to a suite (RC-A1-22) | add the skill to that suite's `SUITE_EXTRA_SKILLS` row in the same commit, then `check_harness_parity.py` |
| any `run-batch/SKILL.md` copy | `check_harness_parity.py` (the commit-contract strings) |
| any package contract file (`README.md`, `SCOPE.md`, `CONTEXT_INDEX.md`, `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`) | `check_package_newlines.py`, then `check_batch_packages.py` |
| a package's batch order, goals, `**Model:**`, primary rows, `**Requires:**` or checklist rows | `check_batch_packages.py` twice: with the default parser and with `--parser-src` at instance 2's `src` |
| a new package, or a package frozen or archived | the classification tables at the top of `check_package_newlines.py` and `check_batch_packages.py`, in the same commit |
| any markdown file, `CLAUDE.md` or `AGENTS.md` | the hygiene checker (`scripts/hygiene/repo_hygiene_check.py check`) |
| a script in this folder | its row above (rule 5); for `check_harness_parity.py`, also its `--self-test` |

## Known limits

- The codex compare covers the superproject only; the suites' `.codex/` trees are checked only for the
  run-batch commit-contract strings. Their fate is the Codex freeze (`B7-2`, Q-G-09).
- The suite compare covers the five shared skills and the agents. Same-name PlantLibrary-only folders
  in a suite (today PyApp's `gui-validation` pointer and six Workspace copies) are listed, not compared,
  until `B1` mirrors them and fills `SUITE_EXTRA_SKILLS` (RC-A1-22, Q-A1-04).
- The two package checks classify live and frozen packages by fixed tables; a package neither table
  names is counted, so a new package is guarded by default.
