# Git structure and worktree strategy — lane A8 (read-only analysis, 2026-10-13)

Lane A8 of the PlantLibrary master rework program, Phase A. Read-only: every git command below is a read (`status`, `log`, `ls-files`, `ls-tree`, `worktree list`, `config --get`, `rev-parse`, `branch`, `count-objects`, `hash-object` without `-w`); in SOURCE-C every git call used `--no-optional-locks`. No test, build or install ran. Git on this machine: `git version 2.55.0.windows.2`. Documentation cited as `git-doc/<file>:line` = `C:\Users\WindowsAI\AppData\Local\Programs\Git\mingw64\share\doc\git-doc\<file>`.

## §0 Summary

1. The six submodules are **old-form and uninitialized**: each has its own `.git` *directory* in place, the superproject has no `.git/modules` and no `[submodule]` sections in `.git/config`, and `git submodule status` prefixes every line with `-` (F-A8-01). The brief's premise "git dir under ../.git/modules/<name>" does not hold; rule 5's `git -C <repo> worktree add` works anyway, with metadata under `<repo>\.git\worktrees\<id>`.
2. Line endings: **zero `i/crlf` files in all seven repositories**; the index is LF everywhere and `core.autocrlf=true` comes from the *system* gitconfig, with no `.gitattributes` in any of the seven. The CRLF seen in working trees is a checkout artefact; `git add` normalises back to LF (proved by `hash-object`, F-A8-05). The real risks are byte-compared files (the parity checker reads working-tree bytes), encodings, and a new worktree checking every text file out as CRLF.
3. **origin/master already pins three submodule commits that are not on their remotes** (Dashboard 7795fc8, Server f1a31b9, SharedContracts d43f7a2; pushed 2026-10-02 22:26 while the three suites were last pushed 2026-09-16). A recursive clone of PlantLibrary_complete fails today. The push order is submodules first, superproject last (F-A8-03).
4. **Sibling-relative paths are load-bearing**: AndroidApp `settings.gradle.kts:25` (`includeBuild("../PlantLibrary_SharedContracts/generated/kotlin")`), Dashboard `vite.config.ts:20`, `tsconfig.generated.json:10,16`, `scripts/generate-theme.mjs:31`, `scripts/check-token-drift.mjs:26`, plus 109 markdown files with `../PlantLibrary_` links. A worktree at `SW_Development_wt\<repo>-<lane>` has no siblings, so these break there (F-A8-07). Worktrees therefore suit lanes that stay inside one repository; design and code lanes that read SharedContracts should serialize in place (Q-A8-01).
5. Instance 2 stores an absolute `repo`, an absolute and **immutable** `batch_package_path`, and six absolute `batch_package_roots` (`C:\Programs\AI_Orchestrator_2\config.yaml:505-517`) that are canonicalised at startup, where a missing root is fatal. A monorepo (Q-G-02 (b)) breaks all six bindings, folds the six git roots into one shared tree, and moves the skill-mirror gate to one root. A worktree breaks nothing as long as instance 2 stays paused (F-A8-09/10).
6. Recommendation Q-G-02 **(a) keep the superproject with six submodules**, unchanged in form for the whole program (no init, update, absorbgitdirs or deinit). Branches `rework/<step-id>`, fast-forward only onto each suite's `main`; the superproject is `master`, not `main`.
7. Disk: `df` shows 77 GB of 299 GB free (25.7 %), which leaves 17 GB above the 20 % floor. A worktree costs at most about 30 MB of tracked content (objects shared), so worktree count is not the disk risk; installs and builds inside worktrees are.
8. Questions: Q-G-02 (evidenced), Q-G-03 (push list evidenced), Q-A8-01..05.

## §1 Coverage

| Item | Status | Reason |
|---|---|---|
| Kickoff prompt §1, §2 (`rework/PROMPT_master-rework-kickoff_2026-10-13.md:3-31`) | read | brief requirement |
| `.gitmodules` (superproject) | read | all 18 lines |
| `git remote -v`, `log --oneline -3`, `status --short --branch` × 7 | read | full output |
| `.git` entry of each submodule and resolved git dir | read | all are directories; `.git/modules` absent |
| `core.autocrlf` / `core.eol` / `core.safecrlf` (with scope) × 7; `.gitattributes` × 7 | read | autocrlf from system scope; eol, safecrlf and attributes absent |
| `git ls-files --eol` × 7, summarised by extension class | read | full counts, every `w/mixed` path listed |
| `git count-objects -vH` × 7; `.git` size × 7; tracked blob bytes × 7 | read | |
| `du` of the populated working trees | not read | `du -sh` of the superproject did not finish within 300 s (node_modules, .venv, Gradle build dirs present); stopped. Tracked-blob size used as the worktree cost instead |
| `.gitignore` × 7 | read | scratch roots extracted |
| `git branch -a -vv`, tags, stashes, upstream, ahead/behind × 7 | read | |
| git-worktree, gitrepository-layout, git-submodule, gitsubmodules, git-config (safecrlf) docs | partly read | the passages cited only |
| Conductor `git worktree list`, `branch -a` (first 60), `.gitattributes`, `ls-files --eol` summary | read | |
| Conductor `src/conductor/batch_discovery.py` | read | lines 15-199 (all logic) |
| Conductor `src/conductor/gui.py` POST/PATCH `/api/v1/projects` | read | lines 1938-2106 |
| Conductor `src/conductor/workers/runtime.py` `create_worktree`, `_enclosing_repository` | read | lines 300-315, 3590-3600, 3855-3900 |
| Conductor `src/conductor/scheduler.py` dispatch → `create_worktree` | partly read | lines 3355-3380 |
| Conductor `docs/handbook/09-second-instance.md` | partly read | collision table, prerequisites, steps 7, 8 (act table), 10, rollback (lines 34-62, 121-135, 313-330, 418-432, 545-556, 599-613) |
| Conductor `implementation/Conductor_V2/planning/PROMPTS_quality-program_2026-10-02.md` | partly read | worktree, push, D-id and CRLF rules (lines 76-118, 147-163) |
| Instance 2 `C:\Programs\AI_Orchestrator_2\config.yaml` | partly read | `worktrees` (432-434) and `intake` (502-517) only; database and API never touched |
| `onboarding/REGISTER_package-census_2026-09-15.md` "Instance 2 registration, step 5" | read | lines 46-130 |
| `scripts/harness/check_harness_parity.py` | read | how it compares (bytes, within one root) |
| Sibling-path grep in the six suites (non-markdown) | read | `git -C <suite> grep` |
| hygiene `CONSUMED_HYGIENE.md` pins and D-id sets × 7 | partly read | pin line and D-id headings only |
| Conductor `PLAN_master-guide-v2`, `PROPOSAL_runbook-skill` | not read | A5's lane |

Counts: read 17, partly read 8, not read 2.

## §2 Findings

**F-A8-01 — The submodules are old-form and uninitialized.**
Evidence: `git -C C:\Programmierung\SW_Development submodule status` printed `-5d6410f… PlantLibrary_AndroidApp`, `-7795fc8… PlantLibrary_Dashboard`, `-35ddc63… PlantLibrary_PyApp`, `-f1a31b9… PlantLibrary_Server`, `-d43f7a2… PlantLibrary_SharedContracts`, `-6b4b88b… PlantLibrary_Workspace`, where `-` means "not initialized" (`git-doc/git-submodule.adoc:82-83`). `stat -c %F PlantLibrary_*/.git` gives `directory` for all six. `ls .git/modules` gives "No such file or directory". The superproject `.git/config:1-14` has `[core]`, `[remote "origin"]` and `[branch "master"]` only. `git rev-parse --git-dir` in each submodule prints `.git`, and `--show-superproject-working-tree` prints `C:/Programmierung/SW_Development`. Each submodule's own `.git/config` carries `[submodule] active = .` (e.g. `PlantLibrary_PyApp/.git/config:8-9`). That setting governs nested submodules of that repository (none), not the superproject. Gitlinks: `git ls-files -s | grep ^160000` shows six entries, all equal to the submodule HEADs.
Meaning: this is the "Old-form submodule: a working directory with an embedded `.git` directory" (`git-doc/gitsubmodules.adoc:133-142`). The superproject treats them as inactive (`gitsubmodules.adoc:168-183`: active only through `submodule.active` or `submodule.<name>.url` in the superproject's config, and neither is set). Superproject `git status` and `git add <path>` still read each submodule's HEAD (R-0's gitlink bump proves it). Rule 5's worktree command runs against an ordinary repository; its admin data lands in `<repo>\.git\worktrees\<id>`, not under the superproject.

**F-A8-02 — State per repository (measured 2026-10-13).** All seven are clean on their branch. The superproject is `master` @ 8702e0a, ahead 1 of origin/master (67dcc51). Workspace, PyApp and AndroidApp are level with origin. Dashboard, Server and SharedContracts are ahead 1 each. There are no stashes, one tag `mvp-final` per repository (§7.1), and no branches beyond `main`/`master`: no stale `rework/` or feature branch exists anywhere (`git branch -a -vv` × 7). `git worktree list` × 7 shows only the main checkouts, so instance 2 has never dispatched into a suite (it would register `C:\Conductor2\jobs\<ref>`). `C:\Programmierung\SW_Development_wt` does not exist yet.

**F-A8-03 — origin/master pins three unpushed submodule commits.**
Evidence: `git ls-tree origin/master` shows the Dashboard gitlink at 7795fc8, Server at f1a31b9 and SharedContracts at d43f7a2. `git -C PlantLibrary_<X> branch -r --contains <sha>` prints nothing for all three. The reflogs show `refs/remotes/origin/master@{2026-10-02 22:26:39}: update by push` while `PlantLibrary_Dashboard` `refs/remotes/origin/main@{2026-09-16 21:47:00}: update by push` (Server 21:47:03, SharedContracts 21:47:03), and the three FETCH_HEADs date from 2026-09-16. Caveat: this reflects the remote-tracking refs as of those dates. No fetch was run (rule 1), so a push made from another clone would not show here.
Meaning: anyone cloning PlantLibrary_complete with `--recurse-submodules` cannot check out three of the six pins. The end-of-wave push (§7.3) must push submodules before the superproject, and the first push of the program must include these three.

**F-A8-04 — No `.gitattributes`, autocrlf from system scope.** `git config --show-origin --show-scope --get-all core.autocrlf` prints `system file:C:/Users/WindowsAI/AppData/Local/Programs/Git/etc/gitconfig true` in all seven. `core.eol`, `core.safecrlf`, `core.longpaths`, `push.default`, `submodule.recurse` and `push.recurseSubmodules` are unset everywhere. `git ls-files | grep gitattributes` finds nothing in any of the seven. The Conductor by contrast tracks `.gitattributes` (`Orchestrator_System/.gitattributes:1-12`) pinning `text eol=lf` for `DESIGN.md`, `.impeccable/**`, `design/stacks/*/generated/**`, `design/tokens.json`, `design/semantic-roles.json`, `design/conduct-rules.md`, `design/banned-colors.json` and others.
Meaning: TARGET has no per-path eol control. When B5 lands a Design Configuration with generated stack artifacts, those artifacts will be CRLF in TARGET working trees unless TARGET adopts the Conductor's path-scoped lines (RC-A8-01, Q-A8-03).

**F-A8-05 — The index is LF everywhere; working-tree CRLF is a checkout artefact; autocrlf normalises on add.**
Evidence: `git ls-files --eol` × 7 shows no `i/crlf` and no `i/mixed`. Every `mixed` entry is `i/lf w/mixed` (§7.1 table; 4 in the superproject, 12 in Workspace, 6 in PyApp, 14 in AndroidApp, 2 in Dashboard, 10 in Server, 6 in SharedContracts). Normalisation proof on a mixed file, `PlantLibrary_PyApp/.claude/skills/run-batch/SKILL.md`: the index blob is `581b2b9e…`, `git hash-object <file>` (filtered) gives `581b2b9e…`, and `git hash-object --no-filters <file>` gives `cc3426c6…`. The working-tree bytes differ, yet git stores the identical LF blob. The git-config doc on `core.safecrlf` (HTML, `git-config.html:3303-3352`) states the commit path: "Git will convert CRLF to LF during commit and LF to CRLF during checkout", and a mixed file "cannot be recreated by Git".
Meaning for rule 8: the committed bytes cannot become CRLF through a text-mode rewrite while `autocrlf=true` holds. What a careless write *can* damage is (i) files compared by working-tree bytes (F-A8-06), (ii) encoding: a UTF-16 or BOM write, e.g. PowerShell 5 `Out-File`/`Set-Content` defaults, becomes a real content change, and (iii) binaries misdetected as text. Rule 8's "keep the file's own endings" remains right as a working-tree hygiene rule. Its guard is `git diff --stat` empty except for intended lines, plus `git ls-files --eol` showing `i/lf` for the touched paths (§7.6).

**F-A8-06 — Byte-compared files exist: the parity checker reads working-tree bytes.** `scripts/harness/check_harness_parity.py:42-48` (`path.read_bytes()`) and `:57-73` compare `.claude/skills` against `.codex/skills` byte for byte within one repository root (`:123-128`; no cross-repository comparison). `run-batch/SKILL.md` is `w/mixed` in both mirrors of all seven repositories. Parity passes only because both copies carry the same mixed bytes.
Meaning: B1 must write a mirrored skill file into both trees as *the same bytes* (a byte copy, never two independent text writes). A fresh worktree checks out both copies as CRLF, so parity also holds there. It may differ from the main checkout's bytes, but parity never compares across checkouts.

**F-A8-07 — Sibling-relative paths make a lone worktree incomplete.**
Evidence (`git -C <suite> grep`, non-markdown):
- `PlantLibrary_AndroidApp/settings.gradle.kts:25` `includeBuild("../PlantLibrary_SharedContracts/generated/kotlin")`.
- `PlantLibrary_Dashboard/vite.config.ts:20` `path.resolve(__dirname, "../PlantLibrary_SharedContracts/generated/typescript")`; `tsconfig.generated.json:10,16`; `src/api/client.ts:10` (`../../../PlantLibrary_SharedContracts/generated/typescript`); `scripts/generate-theme.mjs:31` and `scripts/check-token-drift.mjs:26` (`../PlantLibrary_SharedContracts/design-tokens/tokens.json`); `e2e/validation-smoke.spec.ts:19` (writes under `../../PlantLibrary_Workspace/...`).
- `PlantLibrary_PyApp/app/services/server_api_client.py:28-30` (an install hint only, `pip install -e ../PlantLibrary_SharedContracts/generated/python`).
- `PlantLibrary_Server/scripts/export_openapi.py:5` (docstring), `app/db/*.py` docstrings.
- Markdown files with `../PlantLibrary_` links: superproject 2, Workspace 15, PyApp 24, AndroidApp 23, Dashboard 18, Server 22, SharedContracts 7.
- The superproject's `scripts/harness/check_batch_packages.py:24-26` globs `PlantLibrary_*\implementation\*`, so it only works from the superproject root.

Meaning: in `C:\Programmierung\SW_Development_wt\PlantLibrary_Dashboard-<lane>`, `../PlantLibrary_SharedContracts` resolves to a path that does not exist. Type checks and the Dashboard's token-drift and theme scripts (B5, B6) fail there, and markdown link checkers report false breaks. This bounds rule 5 (§7.2, Q-A8-01).

**F-A8-08 — The worktree command itself is sound for these repositories (static check).** `git -C <suite> worktree add <path> -b rework/<x> main` on an old-form submodule:
- Writes `<suite>\.git\worktrees\<id>\` (`gitrepository-layout.adoc:278-290`) and a `.git` *file* in `<path>` holding `gitdir: C:/Programmierung/SW_Development/<suite>/.git/worktrees/<id>`.
- Shares the object store, so the only new cost is the checked-out tracked files (≤ 29.4 MB, §7.1).
- Refuses if `rework/<x>` already exists or if `main` is requested as the branch: `main` is checked out in the main checkout, and the lane works on its own branch.
- `git worktree remove` needs a clean tree with no untracked files (`git-worktree.adoc:144-147`), so a lane leaves only ignored scratch behind.
- The BUGS note "It is NOT recommended to make multiple checkouts of a superproject" (`git-worktree.adoc:539-542`) applies to the superproject variant only (§7.2 S).

The longest tracked path is 169 characters (Workspace). With the prefix `C:\Programmierung\SW_Development_wt\PlantLibrary_Workspace-B3\` (62 characters) that is 231, under the 260 limit with `core.longpaths` unset. A longer lane suffix than about 25 characters would cross it.

**F-A8-09 — What an instance-2 project binding stores.**
- `POST /api/v1/projects` (`Orchestrator_System/src/conductor/gui.py:1938-2000`) takes `name`, `repo` (stored verbatim, `:1983`; `model.py:350`), and optionally `batch_root_id` + `batch_relative_path`. The relative path must not be absolute (`batch_discovery.py:67-71`). It is resolved against the configured root, must stay inside it and inside `repo` (`:73-84`, `:148-152`), must parse (`:129-134`), and must not already be bound (`:138-145`). The **canonical absolute path** is stored as `batch_package_path` (`gui.py:1985`; the step-5 record shows `C:\Programmierung\SW_Development\PlantLibrary_PyApp\implementation\System_V1_Implementation`, `onboarding/REGISTER_package-census_2026-09-15.md:62-66`).
- `PATCH` can bind an unbound project once and never rebind: a 409 with "archive it and create a new project to rebind" (`gui.py:2046-2066`).
- Roots: `config.yaml:505-517` lists six ids (`pyapp`, `server`, `androidapp`, `dashboard`, `sharedcontracts`, `workspace`), each `C:\Programmierung\SW_Development\PlantLibrary_<X>\implementation`. `canonicalize_roots` resolves them strictly at startup and raises `StartupCheckError` if one is missing or not a directory (`batch_discovery.py:39-57`).
- `git_root` (`:156-179`) and `shared_tree_projects` (`:182-199`) group projects by `git rev-parse --show-toplevel`. Today the six suites resolve to six different roots.
- Dispatch creates `git worktree add <jobs_root>\<task_ref> -b conductor/<task_ref> HEAD` in `task.repo` (`runtime.py:3861-3871`, `scheduler.py:3365-3372`), with `jobs_root` = `C:\Conductor2\jobs` (`config.yaml:432-434`).
- The skill-mirror gate finds "the nearest ancestor-or-self holding a `.git` entry" (`runtime.py:304-314`).
- State: six bound projects, PyApp-V1 active, its execution **paused at PY1-B08 with a READY task** (`REGISTER_package-census_2026-09-15.md:101-130`).

**F-A8-10 — A restructure breaks the bindings; a worktree does not, unless instance 2 runs.** Q-G-02 (b) changes every absolute path in F-A8-09:
- A missing root aborts instance 2's startup.
- The six `batch_package_path` values are immutable, so rebinding means six archives and six new projects.
- All packages would share one git root, so every intake would raise the shared-tree acknowledgement.
- The skill-mirror gate's enclosing repository becomes the monorepo root.
- Every dispatched task would check out the whole monorepo.

A lane worktree under `SW_Development_wt` is invisible to instance 2: its paths point at the main checkouts. It matters only if instance 2 resumes. Then its own worktree branches from the suite's `HEAD` and becomes a second writer in that repository, and intake reads `BATCH_PLAN.md` from the main checkout (poll every 5 s, `config.yaml` `intake.batch_status_poll_s: 5`), so each B4 commit merged to `main` is live at once.

**F-A8-11 — Decision ids are repository-local and collide across branches.** `D-2026-09-16-01` exists in all seven `hygiene/HYGIENE_DECISIONS.md` files (heading grep). Rule 3 says "next free id by grep over the repository". Two lanes in two worktrees of one repository both grep `main`, both take the same id, and both append at the end of the same file. That is a textual conflict at rebase and a duplicate id if resolved carelessly. The same holds for every `INDEX.md` line appended in the same root. The Conductor solved it with a grep "over every branch and worktree" (`PROMPTS_quality-program_2026-10-02.md:106-109`).

**F-A8-12 — Scratch roots differ; the superproject does not ignore `.tmp/`.** The superproject `.gitignore:1-15` ignores `tmp_*/`, `graphify-out/`, `Todo.md`, `*.log`, `*.db*`, `pytest-gap-closure*/` and `__pycache__/`, but not `.tmp/`. All six suites ignore `.tmp/` (Workspace `:2`, PyApp `:7,16`, AndroidApp `:24`, Dashboard `:12`, Server `:9`, SharedContracts `:7`). PyApp also ignores `graphify-out/` (`:24`) and `tmp_*` (`:17`). Currently ignored in the superproject (`git status --short --ignored`): `.claude/settings.local.json`, `Todo.md`, `graphify-out/`.
Meaning: a lane that keeps scratch under `.tmp/` in the superproject leaves untracked files, and a superproject worktree with untracked files cannot be removed without `--force`.

**F-A8-13 — Conductor precedent for worktrees.** `git --no-optional-locks -C C:\Programmierung\Orchestrator_System worktree list` shows 23 entries: sibling folders `Orchestrator_System_<PREFIX>_<id>` (`_QP_*`, `_PL_*`, `_CR1_chain`, `_Codebase_Analysis`, `-design`, `_WC`, `_Work_Documentation*`) on branches `<kind>/<topic>` (`analysis/`, `plan/`, `design/`, `docs/`, `quality/`). The quality program's rule 2 (`PROMPTS_quality-program_2026-10-02.md:86-92`) says worktrees are created by the orchestrating session and never from the main checkout, sessions read other worktrees by absolute path, and merges into `main` happen only at a drained boundary owned by the orchestrator. Its rule 3 (`:93-95`) pushed every branch, which this program does not (Q-G-03 (a)). Its rule 8 (`:110-111`) is the CRLF rule this program inherited. The Conductor's own `ls-files --eol` shows the same picture: 4487 `i/lf w/crlf`, 1536 `i/lf w/lf`, 82 `i/lf w/mixed`, 0 `i/crlf`.

## §3 Candidates

| RC id | Source path @ pin | What | Verdict | Target repo and path | Lane | Q id or — |
|---|---|---|---|---|---|---|
| RC-A8-01 | Orchestrator_System/.gitattributes:2-11 @ 2e7adb3 | Path-scoped `text eol=lf` for design tokens, generated stack artifacts, DESIGN.md, `.impeccable/**` | adapt: copy only the lines matching where the Configuration lands; no repo-wide `* text=…` | the repository Q-G-01 picks (SharedContracts `design/` if (a)), plus the three clients' generated-artifact paths | B5 | Q-A8-03 |
| RC-A8-02 | Orchestrator_System/implementation/Conductor_V2/planning/PROMPTS_quality-program_2026-10-02.md:86-92 @ 2e7adb3 | Worktree per parallel session, created by the orchestrator, merged by the orchestrator at a drained boundary | adopt (already rule 5); add "never from inside another worktree" and "reads of other worktrees by absolute path, no git there" | rework/PROMPTS_master-rework-runbook_2026-10-13.md §3a | R-3 | — |
| RC-A8-03 | same file :106-109 @ 2e7adb3 | D-id taken only after a grep over every branch and worktree | adapt: the orchestrator pre-assigns D-ids per step in the runbook; the grep stays as the fallback | runbook §3 step blocks; each repo's hygiene/HYGIENE_DECISIONS.md | R-3, B3 | Q-A8-04 |
| RC-A8-04 | same file :110-111 @ 2e7adb3 | CRLF write-back rule | adopt with F-A8-05's correction (index LF; check `i/lf` plus the empty diff) | kickoff rule 8 / runbook §2 | all B | — |
| RC-A8-05 | same file :93-95 @ 2e7adb3 | Every commit pushed fast-forward by the session | reject (Q-G-03 (a): the operator pushes at the end of each wave) | — | — | Q-G-03 |
| RC-A8-06 | Orchestrator_System/src/conductor/batch_discovery.py:39-57,119-199; gui.py:1938-2106 @ 2e7adb3 | The binding contract (absolute roots, immutable absolute package path, git-root grouping) | reference: the static check B4/B8 run against | onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md §N; B4/B8 step blocks | B4, B8 | Q-A8-02 |
| RC-A8-07 | Orchestrator_System/src/conductor/workers/runtime.py:3861-3875 @ 2e7adb3 | Instance 2's per-task worktrees `conductor/<task_ref>` in the suite repos | reference: the `rework/` prefix cannot collide; record in §3a that instance 2 stays paused | runbook §3a | B8 | Q-A8-02 |
| RC-A8-08 | Orchestrator_System/.claude/skills/instance-sync/SKILL.md:24 @ 2e7adb3 | `git worktree add --detach <path> <sha>` for a clean read-only snapshot | adapt (optional): read-only verification of a merged suite at a pinned SHA without touching the main checkout | runbook C1 / Phase C resume | C1 | — |
| RC-A8-09 | Conductor sibling worktree naming `Orchestrator_System_<PREFIX>_<id>` (worktree list) | Worktrees as siblings of the main checkout | keep PlantLibrary's: one container `C:\Programmierung\SW_Development_wt\` keeps `C:\Programmierung` tidy and outside every repository | rule 5 | R-3 | Q-A8-01 |
| RC-A8-10 | Orchestrator_System/docs/handbook/09-second-instance.md:313-330, 418-432, 599-613 @ 2e7adb3 | Step 7 (what the target repo must carry), onboarding acts 1-6, rollback with `git -C $Repo worktree prune` | reference for B8's static re-verification; act 4 (`.tmp/` ignored) already holds in all six suites | onboarding runbook §N | B8 | — |

## §4 Questions for the operator

| Q id | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-G-02 | Repository structure | (a) keep the superproject with six submodules, unchanged in form (old-form, uninitialized) for the whole program; (b) consolidate into fewer repositories (monorepo by subtree merge, or a meta-tool such as a manifest of six plain clones) | (b) breaks six instance-2 roots and six immutable bindings (F-A8-09/10), seven D-id sequences that collide (F-A8-11), seven `mvp-final` tags and the frozen MVP evidence that cites per-repo commits and sibling paths (F-A8-07), seven hygiene pins and the superproject allowlist entries `hygiene/HYGIENE_DECISIONS.md:99-109`, and six GitHub remotes. Its gain (atomic cross-suite commits, one push) is small next to that, because rule 5 already gives one writer per repository and one gitlink-bump commit per step | B3 (any move of a suite folder), B4, B8 |
| Q-A8-01 | Where the second lane on a repository works, given sibling-relative paths (F-A8-07) | (a) a worktree `C:\Programmierung\SW_Development_wt\<repo>-<step>` only for steps whose writes *and* checks stay inside that repository (hygiene, docs, packages, skills); steps that read siblings (B5 anchoring, B6 GUI changes, token or contract work, link checks across suites) serialize in place on `main`; (b) a lane folder `SW_Development_wt\<step>\` holding the worktree under its own name `PlantLibrary_<X>` plus directory junctions to the sibling main checkouts (read-only by convention); (c) a full set of seven worktrees per lane | (a) needs no extra filesystem objects and cannot write through a junction into another lane's repository; (b) works but a junction makes a "read-only" sibling writable and confuses `git -C ..` calls; (c) costs about 80 MB per lane and seven merges | R-3 §3a; any second writer on one repository |
| Q-A8-02 | Instance 2 during the program | (a) stays paused at PY1-B08; no resume, no intake, no new bind or archive until C1; B4 keeps every bound path and `implementation\` root in place and parseable at every `main` commit; B8 re-verifies statically; (b) allow instance 2 to run batches in suites no lane is writing | (a) instance 2 resuming makes a second writer (its `conductor/<ref>` worktree from `HEAD`, F-A8-09) and reads half-migrated packages from the main checkout every 5 s; it also takes the test slot the program gave the Conductor | B4, B8, C1 |
| Q-A8-03 | `.gitattributes` in TARGET | (a) no repo-wide attributes during the program; add only path-scoped `text eol=lf` lines for the Design Configuration's tokens and generated artifacts when B5 lands them (RC-A8-01), each in the commit that adds those paths; (b) a full `.gitattributes` per repository now (`* text=auto` plus eol rules) with a renormalize commit; (c) none | (a) touches no existing file (all indexes are LF already, F-A8-05) and matches the Conductor's precedent; (b) rewrites working trees across seven repositories mid-program and makes every main checkout appear dirty until refreshed | B5 |
| Q-A8-04 | D-id and INDEX-line allocation when two steps write one repository | (a) the orchestrator pre-assigns each step's D-ids in the runbook step block, and INDEX lines are appended by the merging orchestrator if the rebase conflicts; (b) each step greps every branch and worktree for the next free id (the Conductor rule) | (a) is deterministic and removes the race (F-A8-11); (b) still races between two live worktrees | B3, B4, B5 |
| Q-A8-05 | Submodule form after the program | (a) keep the old-form layout for the program, and decide afterwards in a separate session whether to `absorbgitdirs` (move the six `.git` directories under `.git/modules`, `git-submodule.adoc:270-280`); (b) absorb now | (a) absorbing while lane worktrees exist relocates the git dirs those worktrees point to, and instance 2's `safe.directory` entries and `repo` strings name the current layout; nothing in the program needs the new form | — (post-program) |

## §5 Reusable things this brief did not name

- `mvp-final` tags in all seven repositories (superproject 9afa025, Workspace f874fa4, PyApp 532af8e, AndroidApp f9b2043, Dashboard e12f520, Server 929f70b, SharedContracts 68d5018). These are frozen anchors for the archive step (A6/B3) and for any "what was MVP" diff, read with `git -C <repo> diff --stat mvp-final..main`.
- `PlantLibrary_Workspace/SW_Development.code-workspace:3-7`: a VS Code multi-root file that hard-codes the sibling layout (another reason against moving folders).
- `scripts/harness/check_batch_packages.py:24-26`: its globs presuppose the superproject root, so it is run from the main checkout, never from a suite worktree.
- The local git documentation set (`git-doc/*.adoc`) is enough for static verification without network.
- `git hash-object <file>` against `git ls-files -s <file>` is a one-line proof that a rewritten file will commit as the same blob (F-A8-05). It is useful in §7.6.

## §6 Claims to verify

1. **The submodules are old-form and uninitialized.** Check: `git -C C:\Programmierung\SW_Development submodule status` (every line starts with `-`) and `test -d C:/Programmierung/SW_Development/.git/modules || echo absent` (prints `absent`).
2. **origin/master pins a Dashboard commit that origin does not have (as last fetched).** Check: `git -C C:\Programmierung\SW_Development ls-tree origin/master PlantLibrary_Dashboard` (shows 7795fc84…) then `git -C C:\Programmierung\SW_Development\PlantLibrary_Dashboard branch -r --contains 7795fc8` (prints nothing).
3. **AndroidApp builds against a sibling path.** Check: `grep -n includeBuild C:/Programmierung/SW_Development/PlantLibrary_AndroidApp/settings.gradle.kts` (line 25: `../PlantLibrary_SharedContracts/generated/kotlin`).

## §7 Deliverables

### §7.1 Measured table per repository

| Repo | HEAD · branch | Remote (origin) | Ahead/behind origin (last fetch) | Clean | autocrlf / eol / safecrlf / attributes | Tracked files · blob MB | `.git` size (pack) | Ignored scratch roots | Tag |
|---|---|---|---|---|---|---|---|---|---|
| SW_Development (super) | 8702e0a · master | Mariusmak/PlantLibrary_complete | +1 / 0 | yes | true (system) / – / – / none | 158 (6 gitlinks) · 2.0 | 3.8 MB (loose 2.31 MiB) | `tmp_*/`, `graphify-out/`, `Todo.md`, `pytest-gap-closure*/`; **no `.tmp/`** | mvp-final 9afa025 |
| PlantLibrary_Workspace | 6b4b88b · main | Mariusmak/PlantLibrary_Workspace | 0 / 0 | yes | true (system) / – / – / none | 774 · 29.4 | 21 MB (19.02 MiB) | `.tmp/` | mvp-final f874fa4 |
| PlantLibrary_PyApp | 35ddc63 · main | Mariusmak/PlantLibrary_PyApp | 0 / 0 | yes | true (system) / – / – / none | 984 · 17.5 | 94 MB (92.03 MiB) | `.tmp/`, `tmp_*`, `graphify-out/`, `.venv/`, `build/` | mvp-final 532af8e |
| PlantLibrary_AndroidApp | 5d6410f · main | Mariusmak/PlantLibrary_AndroidApp | 0 / 0 | yes | true (system) / – / – / none | 791 · 27.3 | 15 MB (14.22 MiB) | `.tmp/`, `build/` | mvp-final f9b2043 |
| PlantLibrary_Dashboard | 7795fc8 · main | Mariusmak/PlantLibrary_Dashboard | +1 / 0 | yes | true (system) / – / – / none | 266 · 2.0 | 1.3 MB (783 KiB) | `.tmp/`, `node_modules/` | mvp-final e12f520 |
| PlantLibrary_Server | f1a31b9 · main | Mariusmak/PlantLibrary_Server | +1 / 0 | yes | true (system) / – / – / none | 161 · 0.8 | 1.7 MB (134 KiB) | `.tmp/`, `.venv/` | mvp-final 929f70b |
| PlantLibrary_SharedContracts | d43f7a2 · main | Mariusmak/PlantLibrary_SharedContracts | +1 / 0 | yes | true (system) / – / – / none | 604 · 1.8 | 4.5 MB (2.27 MiB) | `.tmp/`, `/generated/**/build/` | mvp-final 68d5018 |

Disk: `df -h /c` shows 299G size, 223G used, 77G available (25.7 %). The 20 % floor is 59.8 GB, so headroom is about 17 GB. One worktree costs its tracked files (≤ 29.4 MB plus CRLF growth) plus a few KB of admin data, so even seven at once stay under 100 MB.

**EOL counts by extension class** (`git ls-files --eol`; each cell is `i/lf w/lf · i/lf w/crlf · w/mixed`; `i/crlf` is **0** in every cell of every repository; kt includes .kts; `bin` = `i/-text`, `empty` = `i/none` or a gitlink):

| Repo | .md | .py | .kt/.kts | .ts/.tsx | .json | .yaml/.yml | other | bin · empty |
|---|---|---|---|---|---|---|---|---|
| super | 60 · 6 · 2 | 16 · 2 · 0 | – | 2 · 0 · 0 | 1 · 1 · 0 | 1 · 0 · 0 | 33 · 26 · 2 | 0 · 6 |
| Workspace | 244 · 207 · 3 | 11 · 5 · 0 | – | – | 0 · 1 · 0 | 1 · 0 · 0 | 31 · 35 · 9 | 209 · 18 |
| PyApp | 61 · 245 · 4 | 31 · 322 · 0 | – | – | 0 · 12 · 0 | 1 · 3 · 0 | 6 · 247 · 2 | 33 · 17 |
| AndroidApp | 60 · 108 · 2 | 3 · 0 · 0 | 34 · 61 · 11 | – | 0 · 4 · 0 | 1 · 1 · 0 | 14 · 229 · 1 | 206 · 56 |
| Dashboard | 39 · 61 · 2 | 1 · 1 · 0 | – | 15 · 72 · 0 | 2 · 3 · 0 | 1 · 0 · 0 | 8 · 55 · 0 | 5 · 1 |
| Server | 44 · 26 · 2 | 7 · 45 · 7 | – | – | 1 · 0 · 0 | 3 · 3 · 1 | 5 · 8 · 0 | 0 · 9 |
| SharedContracts | 180 · 32 · 2 | 1 · 122 · 1 | 81 · 64 · 0 | 68 · 0 · 0 | 5 · 18 · 3 | 2 · 3 · 0 | 13 · 7 · 0 | 1 · 1 |

The `w/mixed` files (all `i/lf`) are the ones a lane must not "fix" in passing:
- super: `.claude/skills/run-batch/SKILL.md`, `.codex/skills/run-batch/SKILL.md`, `.claude/skills/ui-ux-pro-max/data/landing.csv`, `.codex/skills/ui-ux-pro-max/data/landing.csv`.
- Workspace: both `run-batch/SKILL.md`, `.claude/skills/ui-ux-pro-max/data/landing.csv`, `README.md`, four `docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_*.csv`, four frozen `implementation/System_Integration_MVP/validation/evidence/MVP-VALIDATION-20260708-01/EV-00[2-5]_*.txt`.
- PyApp: both `run-batch/SKILL.md`, `.gitignore`, `pyproject.toml`, `GUI/screen_structures/Screen_Structure_plant_list.md`, `Screen_Structure_settings.md`.
- AndroidApp: both `run-batch/SKILL.md`, three `build.gradle.kts`, eight `.kt` sources, `implementation/MVP/evidence/emulator_boot.log`.
- Dashboard: both `run-batch/SKILL.md`.
- Server: both `run-batch/SKILL.md`, `app/api/routes/plants.py`, `app/core/config.py`, `app/main.py`, `app/storage/object_storage.py`, `app/sync/registry.py`, `deploy/docker-compose.dev.yml`, two files under `tests/`.
- SharedContracts: both `run-batch/SKILL.md`, three `api-examples/*.example.json`, `scripts/validate_contracts.py`.

### §7.2 Worktree recipe, verified statically

**Preconditions** (orchestrator, read-only): free disk ≥ 20 % after the add (`df -h /c`); the target repository is clean (`git -C <repo> status --short` empty); `git -C <repo> worktree list` shows no stale entry for the step; the step qualifies under Q-A8-01 (a), i.e. it neither reads nor checks sibling repositories; instance 2 is paused (Q-A8-02).

**Submodule variant** (`<repo>` = `C:\Programmierung\SW_Development\PlantLibrary_<X>`, `<wt>` = `C:\Programmierung\SW_Development_wt\PlantLibrary_<X>-<step>`):

1. Add (orchestrator, from the main checkout): `git -C <repo> worktree add <wt> -b rework/<step> main`. The base is `main` by name, never `HEAD` of a worktree. Result: `<wt>\.git` is a file pointing at `<repo>\.git\worktrees\PlantLibrary_<X>-<step>`. Every text file in `<wt>` is CRLF (fresh checkout, autocrlf=true), and there are no ignored dirs (`node_modules`, `.venv`, `build`).
2. Work and commit (lane session, cwd `<wt>`): `git -C <wt> add <paths>` (by path, never `-A` over scratch), then `git -C <wt> commit -m "<commit line>"`. Commits land on `rework/<step>` only.
3. Merge back (orchestrator, at a boundary, in the main checkout which has `main` checked out and is clean): `git -C <repo> merge --ff-only rework/<step>`. If it refuses because `main` advanced through the in-place writer: run `git -C <wt> rebase main` (allowed, the branch was never pushed), resolve if needed (see failure modes), then repeat the ff merge.
4. Gitlink bump (orchestrator, superproject main checkout): `git -C C:\Programmierung\SW_Development add PlantLibrary_<X>`, check `git -C C:\Programmierung\SW_Development diff --cached --submodule=short` (one line `-<old> +<new>`), and commit together with the runbook ledger flip in one commit per step (rule 5).
5. Remove (orchestrator): `git -C <repo> worktree remove <wt>` (refuses on untracked or modified files; never `--force` unless the step's report is committed), then `git -C <repo> branch -d rework/<step>` (`-d` succeeds only because `main` contains it). Last, `git -C <repo> worktree list` shows the main checkout only.

**Superproject variant** (only for a step that writes superproject-only paths while another step holds the main checkout): `git -C C:\Programmierung\SW_Development worktree add C:\Programmierung\SW_Development_wt\SW_Development-<step> -b rework/<step> master`. The superproject branch is `master`. In that worktree the six submodule folders are empty, because they are uninitialized and git does not populate submodules in linked worktrees; `git-worktree.adoc:539-542` advises against multiple checkouts of a superproject. Rules for it:
- Never run `git submodule update --init` there (it would clone six repositories from GitHub into the worktree's admin dir).
- Never bump a gitlink there; gitlink bumps happen only in the main checkout.
- Stage by path.
- Run link checks that cross into submodules only in the main checkout.

Merge back with `git -C C:\Programmierung\SW_Development merge --ff-only rework/<step>` in the main checkout, then remove as above.

**The superproject's view while a suite worktree exists:** unchanged. `git status` in the superproject reads `<repo>\.git\HEAD` (`main` in the main checkout). Commits on `rework/<step>` are invisible to it until step 3 moves `main`; from then until step 4 the superproject shows the submodule as modified (new commits). The worktree lies outside `C:\Programmierung\SW_Development`, so it never appears as untracked there. `git -C <wt> rev-parse --show-superproject-working-tree` prints nothing, so the worktree is a standalone repository view and its hygiene checker runs on that repository alone.

**Failure modes:**
- *Two lanes write the same suite* (one in place, one in a worktree, or two worktrees). The second ff merge fails. A rebase is needed, and conflicts are certain where both append to the same `INDEX.md` or `hygiene/HYGIENE_DECISIONS.md` (F-A8-11), with duplicate D-ids if each took "next free" (Q-A8-04). Also, the in-place writer's uncommitted changes block step 3, because `merge --ff-only` refuses to overwrite modified files. Rule: merge at a boundary where the in-place writer has committed and stopped.
- *Sibling-path checks in a worktree* report false failures (F-A8-07). Never record them as findings; run them in the main checkout after the merge.
- *Branch name reused*: `worktree add -b` refuses if `rework/<step>` exists, for example from an earlier attempt not yet deleted. Use a new step suffix or delete after the merge.
- *Path length*: suffixes longer than about 25 characters push Workspace paths past 260 (F-A8-08).
- *Byte-compared mirrors*: a skill file edited in one mirror and copied as text into the other fails parity (F-A8-06). Copy bytes.
- *Removing with scratch present*: `.tmp/` is ignored in the suites, so remove works. In the superproject `.tmp/` is not ignored (F-A8-12): use the scratchpad outside the repository.
- *Instance 2 resumed* (Q-A8-02): a third worktree `C:\Conductor2\jobs\<ref>` on `conductor/<ref>` from `main`'s HEAD, an unplanned writer.

**Why `git submodule update` must never run during the program** (rule confirmed, reason sharpened):
- Today a plain `git submodule update` is a no-op, because no submodule is initialized or active (F-A8-01). Any variant that initializes is the danger: `--init`, `git submodule init` followed by `update`, `git clone/pull --recurse-submodules`, or setting `submodule.recurse`.
- For every submodule whose HEAD differs from the recorded gitlink, it checks out the gitlink commit on a detached HEAD (`git-submodule.adoc:157-158`; with `--force` even when equal, `:160-163`). Between step 3 and step 4 every merged suite has HEAD ≠ gitlink. An update then detaches `main` and rolls the working tree back to the old pin. Nothing is lost, since `main` still points at the merged commit, but the next lane writes on a detached HEAD and its commits belong to no branch.
- `git submodule absorbgitdirs` and `deinit` change the old-form layout (Q-A8-05) and must not run while a worktree exists.

### §7.3 Branch naming and the end-of-wave push list (Q-G-03 (a))

- Lane branches: `rework/<step-id>` in the repository the step writes (e.g. `rework/B3-02` in PlantLibrary_Server). A step that needs worktrees in two repositories uses the same name in each, since the ref namespaces are separate. Never create a branch named plain `rework` (it would block the `rework/` prefix). The prefix cannot collide with instance 2's `conductor/<task_ref>` (`runtime.py:3867`) or the remote's `main`/`master`.
- What the suites' `main` receives: fast-forwards of `rework/<step>` only (no merge commits), plus the in-place writer's direct commits. The superproject `master` receives gitlink bumps and ledger flips (one commit per step) and superproject-only content.
- Lane branches are never pushed and are deleted after their merge (§7.2 step 5). Plain `git push` with `push.default` unset (the `simple` default) pushes only the checked-out branch to its upstream. Upstreams: `origin/master` for the superproject and `origin/main` for all six suites, verified with `git rev-parse --abbrev-ref @{u}`.

**End-of-wave push list (operator, from the main checkouts, plain `git push` only):**

0. Pre-check (read-only): every repository is clean and on `main`/`master`; `git -C <repo> status -sb` shows `ahead N` and no `behind`; `git -C <repo> worktree list` shows the main checkout only (no unmerged lane).
1. Push the submodules first, those with `ahead > 0` (today Dashboard, Server, SharedContracts; later every suite a wave touched), in this order: `PlantLibrary_SharedContracts`, `PlantLibrary_Server`, `PlantLibrary_Dashboard`, `PlantLibrary_AndroidApp`, `PlantLibrary_PyApp`, `PlantLibrary_Workspace`. Git does not require an order among them; this order puts the contract producer first. Each is `git -C C:\Programmierung\SW_Development\PlantLibrary_<X> push`.
2. Containment check before the superproject: for each gitlink, `git -C C:\Programmierung\SW_Development ls-tree HEAD PlantLibrary_<X>` gives `<sha>`, and `git -C C:\Programmierung\SW_Development\PlantLibrary_<X> branch -r --contains <sha>` must print `origin/main`.
3. Push the superproject last: `git -C C:\Programmierung\SW_Development push`.

The first such push also repairs F-A8-03.

### §7.4 Instance 2's bindings and what must stay stable

What they store (F-A8-09):
- Per instance: six absolute roots `C:\Programmierung\SW_Development\PlantLibrary_<X>\implementation`; `jobs_root` `C:\Conductor2\jobs`; `branch_prefix` declared but unread.
- Per project: `repo` (an absolute path string, as submitted), `batch_package_path` (the canonical absolute path of `implementation\System_V1_Implementation`, immutable), and the paused execution of PyApp-V1 at PY1-B08.

What a restructure (Q-G-02 (b)) breaks:
- Startup: a missing root raises `StartupCheckError`.
- All six bindings: rebinding needs an archive plus a new project each, and PyApp's paused execution is lost with its project.
- Shared-tree grouping: one git root for all six.
- The skill-mirror gate's enclosing repository.
- Act 1 and act 5 of `onboard-repository`: the root must be the git toplevel, and `safe.directory` names it.
- Handbook step 7: `.claude\skills` and `.codex\skills` are expected at the worktree root, `09-second-instance.md:318-325`.

What a lane worktree breaks: nothing, while instance 2 is paused. The bound paths point at the main checkouts, and a worktree outside them is invisible to intake.

What B4 and B8 must keep stable:
1. The six folders `PlantLibrary_<X>` under `C:\Programmierung\SW_Development` (never renamed or moved).
2. `implementation\` in each suite (never renamed; B3's archive tree must not absorb it).
3. `implementation\System_V1_Implementation\` in the six suites (the bound paths), with `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md` and `SCOPE.md` present and parseable at every commit on `main`, because intake reads the main checkout.
4. `.claude\skills\` and `.codex\skills\` at each suite root, byte-identical mirrors (B1 changes them on `main` only after parity holds).
5. `.tmp/` stays ignored (act 4).
6. Each suite's `.git` stays a directory in place (Q-A8-05).
7. No resume, intake, bind or archive on instance 2 until C1 (Q-A8-02).

B8's static re-verification: read `config.yaml:505-517` and check that each root resolves to an existing directory; read each package's required files; compare the census register's bound paths (`REGISTER_package-census_2026-09-15.md:62-91`) with the tree.

### §7.5 Recommendation on Q-G-02 and further questions

**Recommendation: Q-G-02 (a) — keep the superproject with six submodules, in their current old-form, uninitialized layout, for the whole program.**

Reasons:
1. Every external pin is per repository: six instance-2 roots and immutable bindings, seven hygiene pins and D-id sequences, seven `mvp-final` tags, six GitHub remotes, and the sibling-path build wiring of AndroidApp and Dashboard.
2. Rule 5's one-writer-per-repository model maps one-to-one onto the seven repositories, and the gitlink bump gives the superproject an atomic "system state" per step without a monorepo.
3. The costs of (a) are known and small: the push order (§7.3), the never-`submodule update` rule (§7.2), and the sibling-path limit on worktrees (Q-A8-01).

Option (b), as subtree or filter-repo consolidation, would be a program of its own: rewritten history, archived remotes, rebound instance-2 projects, and re-anchored hygiene. Its benefit (atomic cross-suite commits) is already mostly covered.

Question row for the register: `Q-G-02 | Repository structure | (a) keep the superproject with six submodules, form unchanged (old-form, uninitialized; no submodule init/update/absorbgitdirs/deinit during the program); (b) consolidate into fewer repositories | (b) breaks six instance-2 roots and bindings, seven hygiene pins and D-id sequences, seven mvp-final anchors and six remotes for a benefit rule 5 already provides | B3, B4, B8`.

Further questions: Q-A8-01 (worktree scope versus sibling paths), Q-A8-02 (instance 2 paused for the program), Q-A8-03 (`.gitattributes` only path-scoped at B5), Q-A8-04 (D-ids pre-assigned per step), Q-A8-05 (absorbgitdirs deferred), all in §4.

### §7.6 The bytes rule made concrete

Common facts for all seven repositories (F-A8-04/05): the index is LF for every text file, `core.autocrlf=true` (system), and there are no attributes. Therefore:
- (i) Whatever line endings a lane writes, `git add` stores LF. The commit cannot introduce CRLF.
- (ii) Rule 8's purpose is working-tree stability and a minimal diff, plus the byte-compared mirrors.
- (iii) A new worktree has CRLF in every text file, and the main checkout is a mix (table §7.1).

**Write-back rule for every lane, every repository:**
1. Before editing, read the file's working-tree form with `git -C <repo> ls-files --eol -- <path>` (`w/crlf`, `w/lf` or `w/mixed`).
2. Edit in binary-safe mode: read bytes, change bytes, write bytes. For an append, open the file in append-binary mode and write the new lines terminated with the file's own terminator (`\r\n` if `w/crlf`, `\n` if `w/lf`). For `w/mixed` files (the list in §7.1), use the terminator of the last line and never normalize the rest. The Edit tool's in-place string replacement keeps the surrounding bytes. Never use a text-mode read-modify-write in Python (`open(..., "w")` without `newline=""`), PowerShell `Set-Content`/`Out-File` (encoding change), or a formatter run over a whole file the step does not own.
3. New files: write UTF-8 without BOM. In a suite's package folder (`implementation\**`, most `.md` there are `w/crlf`), write CRLF to match the neighbours. In `rework/` (all `w/lf`, `git ls-files --eol rework/`), write LF. Either way the blob is LF.
4. Mirrors: when B1 changes a file under `.claude/skills/**`, produce the `.codex/skills/**` twin as a byte copy of the finished `.claude` file, then run the parity checker in the main checkout.
5. Before commit:
   - `git -C <repo> ls-files --eol -- <touched paths>` shows `i/lf` for every touched text path (any `i/crlf` means a `.gitattributes` or `-text` slip: stop).
   - `git -C <repo> diff --stat` lists only the intended files.
   - `git -C <repo> diff -- <path>` shows only the intended lines, not whole-file churn.
   - For a file that should be byte-unchanged in content, `git -C <repo> hash-object <path>` equals the blob from `git -C <repo> ls-files -s -- <path>`.
6. Never change `core.autocrlf`, `core.eol` or `core.safecrlf`, and never add a repo-wide `.gitattributes` (Q-A8-03).

**Per repository** (where CRLF dominates in the main checkout and what to watch):

| Repo | Working-tree majority in the main checkout | Watch |
|---|---|---|
| super | LF for `.md` (60 of 68) and `.py`; `other` split 33/26 | `rework/`, `onboarding/`, `handovers/`, `repo-hygiene/` are mostly LF; both `run-batch/SKILL.md` and both `landing.csv` are mixed; no `.tmp/` ignore, so keep scratch outside |
| Workspace | `.md` 244 LF / 207 CRLF (package and methodology trees mostly CRLF) | frozen MVP evidence `EV-00[2-5]_*.txt` and the `MANIFEST_*.csv` are mixed: never touch; 209 binaries |
| PyApp | CRLF dominates (`.md` 245/61, `.py` 322/31, `other` 247/6) | `pyproject.toml` and `.gitignore` are mixed: edit with the Edit tool only; impeccable lives in both mirrors |
| AndroidApp | CRLF dominates (`.md` 108/60, `.kt` 61/34, `other` 229/14) | 11 `.kt`/`.kts` files mixed (list in §7.1); 206 binaries (images, jars) |
| Dashboard | CRLF dominates (`.ts` 72/15, `.md` 61/39) | generated theme output (B5) needs Q-A8-03's path-scoped `eol=lf` if it is byte-checked |
| Server | `.md` LF 44/26, `.py` CRLF 45/7 | five `app/*.py` files, two files under `tests/` and `deploy/docker-compose.dev.yml` are mixed |
| SharedContracts | `.md` LF 180/32, `.py` CRLF 122/1, `.kt` 81/64, `.ts` all LF | `design-tokens/` is the canon; three `api-examples/*.json` are mixed; the Configuration (Q-G-01 (a)) lands here, which is where RC-A8-01's lines belong |
