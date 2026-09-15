# AUDIT — what `run-batch`, `plan-batch`, `validate-real-stack` and `real-stack-testing` assume about the repository they run in

*Runbook step `1` (`onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md` §6), the handbook-step-7
items 1–2 the batch-package handover left undone. Written 2026-09-15 from direct tree reads of all six
`PlantLibrary_*` suites and from three executed measurements (§2). Nothing here is recalled; every "absent"
is a `find`/`ls`/`git ls-files` result of today, and every refusal text in §2 is copied from the run.*

> **Filename note.** The runbook's step-`1` block names `AUDIT_skill-assumptions_2026-09-16.md` but instructs
> "(use today's date)". Today is **2026-09-15** (the runbook was written the same evening, anticipating the step
> would run on the 16th), so the file carries `2026-09-15`. Rename this file and its `INDEX.md` line if the
> literal name is preferred.

## 0. Method and scope

- **Skills read end to end:** `.claude\skills\run-batch\SKILL.md` (408 lines), `.claude\skills\plan-batch\SKILL.md`
  (247 lines). **Read once:** `.claude\skills\validate-real-stack\SKILL.md` (39), `.claude\skills\real-stack-testing\SKILL.md`
  (91). Citations below are `<skill> §<section>.<item>`.
- **Suite trees:** the six per-suite checks of item 1 were delegated to one read-only `Explore` agent each
  (six agents, run in parallel), as the prompt's "if this invocation can spawn agents" branch allows; their tables
  are merged here. The three measurements of §2 were run by this session itself.
- **Legend for "satisfied today":** `PY` = PlantLibrary_PyApp, `SV` = Server, `AN` = AndroidApp, `WD` = Dashboard,
  `SC` = SharedContracts, `SY` = Workspace. A suite code listed means the assumption holds in that suite **for its
  `implementation\System_V1_Implementation` package**; `—` means no suite satisfies it.
- **Baseline fact that colours the whole table:** all six suites are their own git roots (submodules) and all six
  are **clean on `main`** as of this audit. The step-`0` freeze held.

## 1. The assumption table

### 1A. Package structure

| # | Assumption | Where the skill states it | Satisfied today | Consequence when absent | Owner step |
|---|---|---|---|---|---|
| A1 | A package is found by globbing `implementation/*/BATCH_PLAN.md` **under the cwd** | run-batch §1.1; plan-batch §1.1 | PY SV AN WD SC SY | — (all six match exactly one V1 package; every `MVP/` package sits at `implementation/MVP/package/` and is correctly invisible to the one-level glob) | — |
| A2 | If several packages match, pick the one whose `STATE.md` names a next actionable batch, **otherwise ask the user** | run-batch §1.2 | PY SV AN WD SC | **SY only.** From the Workspace cwd the glob matches **four** packages (`System_V1_Implementation`, `System_Design_Architecture`, `System_Integration_MVP`, `System_Tooling`). A headless Conductor worker cannot "ask the user" → the invocation stalls or picks wrong | `2b` (demote the two terminal packages per F-10) · `5` (bind one package per project) |
| A3 | Package siblings `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`, `validation/` | run-batch §1.3 | PY SV AN WD SC SY(V1) | `Workspace/System_Design_Architecture` has **no `validation/`** → its first evidence-producing row (run-batch §6.10) writes into a directory that does not exist | `2b` |
| A4 | A suite `DRIVER_SCRIPT.md` **or** `SCOPE.md` carrying a **Hard scope** section and **standing invariants** | run-batch §1.3, §2 (binding), §7 (passed to the closeout agent); plan-batch §4 ("standing invariants live once in the package scope file"), §6 ("`SCOPE.md` replaces it — do **not** generate a per-package DRIVER_SCRIPT.md") | Hard scope: PY SV AN WD SC SY — all seven live packages have `## 0. Hard scope` in `DRIVER_SCRIPT.md`. **`SCOPE.md`: no live package has one** (the only `SCOPE.md` across all six suites is `Workspace\implementation\System_Tooling\SCOPE.md`, a terminal package) | Hard scope is satisfiable today. But a **"Standing invariants" heading exists in exactly one file suite-wide** (that same terminal `System_Tooling\SCOPE.md`); everywhere else the invariants are loose bullets or one prose sentence, so run-batch §6.8 ("run the suite's standing invariant checks") and §7's closeout-agent input have no addressable section | `2a`/`2b` (the migration writes `SCOPE.md`, as D1/D7 already plan) |
| A5 | `CONTEXT_INDEX.md` at the package root, with a source map / external-context list and a "Do not read as V1 context" section | run-batch §4.6 (advisory context-manifest check) | PY SV AN WD SC SY(V1 + SDA) | — (all seven live packages have it; PY/AN/WD/SV carry all three sections, SC and SY(V1) carry source map + deny-list) | — |
| A6 | One `### <ROW-ID>` anchor per row in `TASK_CONTEXT.md` whose first non-blank line repeats `` `skill: …` `` and `` `design_context: …` `` identical to the row's cells | run-batch §4.1 (stop on mismatch); plan-batch §4 | PY (measured previously, F-11a); the other six packages are **unmeasured** — with a 14-column header the table never parses, so no row/anchor pair can be compared yet | A mismatch is a **hard stop before task work**: "stop task work and fix the metadata first". Latent; fires the moment F-1 is fixed | `2a`/`2b` |
| A7 | Evidence path `validation/<BATCH-KEY>_<slug>.md` | run-batch §6.10 | PY SV AN WD SC SY(V1) | see A3 (SDA) | `2b` |
| A8 | A `planning/`, `proposal/` or `handovers/` folder carries an **`INDEX.md`** that every new `<TYPE>_<topic>_<YYYY-MM-DD>.md` is added to in the same commit | run-batch §6.10; plan-batch §5.4 | **—** | `proposal/` exists in six of the seven live packages, but **no `INDEX.md` exists anywhere under any suite's `implementation\`**. The first incident write-up or handover a batch produces has nowhere to register itself; the rule is silently unenforceable | `3` |
| A9 | `_ACT_STATE.md` is deprecated and never read or updated | run-batch §2 | PY SV AN WD SC SY *(no `_ACT_STATE.md` file exists in any suite)* | Contradiction, not absence: **PyApp's `DRIVER_SCRIPT.md` still instructs reading and appending `_ACT_STATE.md` in its §2 steps 1 and 7**, while its own process note calls it deprecated. run-batch §2 wins, but the driver file is self-contradictory for any reader | `2a` (fold into the `SCOPE.md` rewrite) |

### 1B. Suite-root authority documents

| # | Assumption | Where the skill states it | Satisfied today | Consequence when absent | Owner step |
|---|---|---|---|---|---|
| B1 | A suite `CLAUDE.md` is **binding, always** — layer rules, coding standards, protocols | run-batch §2 | PY (16.6 KB, rich) · SV (52 lines, runtime-only) | **AN, WD, SC, SY have none at all** (searched the whole tree, not just the root). The skill's top authority source is missing for four of six suites: the worker has no layer rules, no coding standards, no protocol pointer, and improvises | `3` |
| B2 | An `AGENTS.md` (Codex parity) | *(not named by the four skills; carried by house convention and the `.codex` mirrors)* | PY (21.2 KB) · SV (19 lines) | AN, WD, SC, SY: none. Codex is disabled on instance 2, so this is parity debt, not a blocker | `3` |
| B3 | A suite `DESIGN.md`, read once per session for `design_context: required` rows | run-batch §4.5 | **PY only** | AN and WD both have `design_context: required` rows **and** a row that will author the file (`AN-V1-DS-02`, `WD-V1-DS-02`); both packages already record a written fallback (SharedContracts `design-tokens\` + page contracts). SV, SC, SY have no design rows. Consequence today: a `required` row takes the recorded fallback and must note it — a degraded leg, not a park | `2b` (keep the fallback wording through the migration) · the DS rows themselves |
| B4 | A suite `PRODUCT.md`, loaded independently for product-behaviour work | run-batch §4.5 | **PY only** | Same shape as B3; AN plans it in `AN-V1-DS-02` | as B3 |
| B5 | A named protocol file such as `GUI/COMMON_GUI_CHANGE_PROTOCOL.md` | run-batch §2 (explicit example) | **PY only** (`GUI\COMMON_GUI_CHANGE_PROTOCOL.md`) | The skill's one concrete protocol example is PyApp-specific; the other suites have no equivalent, so §2's "protocols such as …" resolves to nothing | `3` (name each suite's equivalent, or say there is none) |
| B6 | `CLAUDE.md` has a **"Deliverable naming"** section defining `<TYPE>_<topic>_<YYYY-MM-DD>.md` | run-batch §6.10 and plan-batch §5.4 both cite it verbatim: "(see CLAUDE.md's 'Deliverable naming' section)" | **—** | Measured: the string "deliverable naming" appears in **zero** `.md` files across all six suites, and not in the superproject `CLAUDE.md` either. Both skills enforce a rule against an authority that does not exist; the naming convention survives only by habit | `3` |

### 1C. Harness and validation plumbing

| # | Assumption | Where the skill states it | Satisfied today | Consequence when absent | Owner step |
|---|---|---|---|---|---|
| C1 | `scripts/harness/regression_scope.py` | run-batch §6 5a(i) `--merge-history-from-ledger`, 5a(iv) `--probe-targets`, §6.6 scope + `--plan-chunks` + `--classify-pytest-output` | **—** (no suite has any `scripts\harness\` directory at all) | Coordinator route: `ValidationPlanner.scope` runs it in the project git root → **`HARNESS_PLANNING_FAILED`**, the batch parks before any test runs. Worker route: run-batch §6.6 cannot be executed as written | `4` (PY) · `7` (SV) · `8` (the rest) |
| C2 | `scripts/harness/run_validation.py` | run-batch §6.1 (the long-validation rule, 540 s runner ceiling), 5a(iii) | **—** | Every validation expected to exceed 60 s has no compliant launcher; §6.1 is unexecutable and §6.0's foreground rule leaves no alternative | `4` · `7` · `8` |
| C3 | `scripts/harness/run_chunks.py` | run-batch §6.6 ("Execute the manifest **only** with …"); real-stack-testing "Harness contract" 7 | **—** | No resumable runner → no legal way to execute a chunk manifest. **Measured extra (§2c): `regression_scope.py` imports `run_chunks` at module import time**, so porting one script alone dies with `ModuleNotFoundError` before parsing any argument. The port is a minimum of three files, and the fallback import path `scripts.harness.run_chunks` additionally needs the two directories to be an importable package | `4` · `7` |
| C4 | `scripts/harness/duration_history.json` | run-batch §6 5a(i), §6.6 (`--duration-history`, "add the flag when that file exists") | **—** | Graceful: the skill says omit the flag when absent, so chunks pack flat in groups of ten instead of to a time budget. A **skipped leg**, not a park — one slow file sets the floor | `4` (seed it on the first real closeout) |
| C5 | Every touched path is reachable from a `tests/test_*.py` that imports it | run-batch §6.5 ("account for every touched path"; "never infer coverage"), §6.6 | **—** | **Measured (§2c): `app/services/sync_service.py` → exit 2, `unmapped touched path`.** PyApp has 98 test files and *no* `conftest.py`; the harness is pytest-import-graph-only by construction, so most product paths in a Qt/GUI suite are unmapped. This is the seam F-6 predicted, now with a verbatim refusal | `4` (PY) · `7` (SV) · `8` (AN/WD/SC/SY — no port can work) |
| C6 | Repo-root docs and `implementation/`, `.claude/`, `.codex/`, `scripts/` route to **standing sentinel tests** | run-batch §6.6 (implicit in the closeout matrix); `regression_scope.py` `STANDING_CHECK_PREFIXES` | **—** | **Measured (§2c):** `implementation/System_V1_Implementation/TASK_CHECKLIST.md` alone routes to `tests/gui/real/test_batch_package.py`, `tests/test_batch_package_parser.py`, `tests/test_batch_progress_refresh.py` — all three exist in the dev repo, **none exists in PyApp**. Every batch touches its own checklist, so even a suite whose product paths all mapped would still fail here. Any port must rename the sentinels to suite-local tests | `4` · `7` |
| C7 | `tests/acceptance` (a literal path in the acceptance-registry leg) | run-batch §6 5a(iii) | **—** (the dev repo has 8 files there) | `pytest -q … tests/acceptance` exits 4 (usage error, no such path) → the standing leg **fails** rather than skipping. Must be ported or explicitly waived | `4` · `7` |
| C8 | A `KNOWN_FAILURES.md` ledger resolvable by `--active-package`; "never fabricate a package-local ledger" | run-batch §6.6 (final paragraph) | **—** | **Measured (§2c): exit 2, `known_failure_ledger_unusable` → `no ledger can serve active package: implementation/System_V1_Implementation`.** `resolve_ledger()` looks for `<root>/<active-package>/validation/KNOWN_FAILURES.md`, then exactly one `<root>/implementation/*/validation/KNOWN_FAILURES.md`. Classification is mandatory at closeout, so this refuses every batch close even after C5/C6 are fixed | `4` (decide where the suite's ledger lives, and seed it empty) |
| C9 | `validation.max_scope_targets` read from **"the active `config.yaml`"**, falling back to **"the shipped `config.example.yaml`"** | run-batch §6.6 ("`<cap>` is derived, never a model-typed number and never omitted") | **—** | No suite contains a `config.yaml` or `config.example.yaml` of this shape; **zero** YAML with a `validation:` section exists in any of the six (Server/SC have app + CI YAML only; Dashboard and Workspace have no YAML at all). The only two files are outside every worker cwd: `C:\Programs\AI_Orchestrator_2\config.yaml` (**600**) / `config.example.yaml` (**30**), mirrored by `C:\Programmierung\Orchestrator_System\` (600 / 30). A worker whose cwd is a suite must therefore either type a literal — the exact defect §6.6 names as having parked `CD2-B140`–`B142` and again `CD2-B230` — or read outside its workdir. **And the two candidate files disagree 20-fold**, so taking the "fallback" silently yields `scope cap exceeded: N targets exceeds 30` | `3` (state the cap and its source in each suite's `CLAUDE.md`) · `4` (make the ported harness read a suite-local source) |
| C10 | `validation.foreground_ceiling_s` and `envelope_grace_s` for the derived `--envelope-seconds` | run-batch §6.6 (AM-44 Clause 7); real-stack-testing "Harness contract" 7 | **—** in the suites; present only in `config.example.yaml` (600 / 120 → **480**) of both Orchestrator roots — **not** in either active `config.yaml` | Recoverable: run-batch §6.6 itself states the answer for its own 600 s Bash tool (`--envelope-seconds 480` with `timeout: 600000`), and `run_chunks.py` refuses an over-ceiling value at exit 2 naming the correct one. Still, the derivation's stated source is unreadable from a suite cwd | `4` |
| C11 | `validation.parallel_ordinary` / `parallel_gui_real` are coordinator-route dials only; a worker-route or out-of-band closeout is sized for **serial** wall-clock | run-batch §6.6 ("Serial where it is paid") | n/a — instance 2 runs `parallel_ordinary: 1` | No divergence today; recorded so step `9`'s out-of-band sizing is not taken from the dials | `9` |
| C12 | A **reclaimable, gitignored** scratch root `.tmp/` at the git root, with `.tmp/chunks/<run-id>` as the chunk-artifact and ledger path | run-batch §6 5a(i) (`--merge-history-from-ledger .tmp/chunks`), §6.6 (`--chunk-artifact-dir`, `--ledger`, "point at a gitignored scratch path … never at the persisted `validation/` evidence tree"); `reclaim_scratch.py` `SCRATCH_PARENT_NAMES = (".tmp",)` | **PY only** (`.gitignore` lists `.tmp/` twice) | SV, WD, AN, SC do not ignore `.tmp`; **SY has no `.gitignore` at all** (which is also why five `__pycache__\*.pyc` are committed there). Chunk artifacts, basetemps and ledgers would appear as untracked files in the worktree → Conductor's closeout sees `unattributed_dirty` and parks the green batch. Note also that the superproject root ignores `tmp_*/` but **not** `.tmp/` | `3` |
| C13 | `python scripts/notify_telegram.py --enqueue` exists **at the repo root** and performs a purely local outbox write | run-batch §8; plan-batch §8 | **—** | Exists only at `C:\Programmierung\Orchestrator_System\scripts\notify_telegram.py`. It computes `REPO_ROOT = Path(__file__).resolve().parents[1]` and writes `<repo>\.runtime\telegram-outbox\` — so a copy placed in a suite would enqueue into **`<suite>\.runtime\telegram-outbox`**, which the user-installed drainer does not read *and* which is a new untracked directory (see C12). `C:\Programs\AI_Orchestrator_2\` has a `.runtime\` but no script; the drained outbox is the dev repo's. The script also imports `keyring` and `yaml`. Both skills treat a non-zero exit as "note and continue", so this is a **benign skipped leg** today — but four suites would fail it silently on every batch | `3` (say plainly that the enqueue is unavailable in the suites) · `8` if delivery is actually wanted |

### 1D. Toolchain, agents and invocation

| # | Assumption | Where the skill states it | Satisfied today | Consequence when absent | Owner step |
|---|---|---|---|---|---|
| D-a | `ruff check`, `ruff format --check`, targeted `mypy` for Python; **"suite equivalents otherwise"** | run-batch §6.4, §6 5a(ii) | ruff: **PY** (config + `dev` extra) and **SV** (`[tool.ruff]` + `lint` extra). mypy: **PY only** (`[tool.mypy]` + dev dep; Server has no `[tool.mypy]` and mypy is not a dependency anywhere). SC has ruff config only inside the *generated* client `generated\python\pyproject.toml`. WD: `npm run lint` (eslint 9) + prettier, **no `typecheck` script** — `tsc -b` runs only inside `build`. AN: stock `lintDebug` only — **no ktlint, no detekt, no `.editorconfig`**. SY: nothing | "Suite equivalents" is undefined per suite, so the worker guesses which command satisfies §6.4 — and §6.4 forbids widening to a repo-wide suite unless a row's `validation` cell literally names it. Each suite must name its own lint and type commands | `3` |
| D-b | A pytest corpus exists and is the closeout currency | run-batch §6.5–§6.7; real-stack-testing throughout | PY (98 `test_*.py`, **no `conftest.py`**), SV (10, flat, **no registered markers** — its `CLAUDE.md` notes `pytest -m stack` is "planned but not yet present"), SC (1) | WD has **0** Python tests (16 vitest files + 1 Playwright spec; `playwright.config.ts` has **no `webServer` block** and assumes the stack is already up). **AN has 0 test source files of any kind** — no `src/test`, no `src/androidTest` in any of its 14 modules, although the JUnit/Espresso/Compose test dependencies are wired. SY has **no build system and no test runner at all**. This is the structural reason D2 sends AN/WD/SC/SY out of band | `8` · `9` |
| D-c | The three project agents `real-stack-validator`, `batch-closeout-reviewer`, `batch-plan-auditor` are reachable from the executing session | run-batch §4.7 (AM-27 row delegation), §5 (blast-radius + section reads), §6.2, §7 (closeout review); plan-batch §5.3 | **—** — no suite has a `.claude\agents\` directory at all | Each skill has an explicit inline fallback, so absence degrades rather than parks. **But:** every agent's frontmatter declares `skills:` (`real-stack-testing`; plus `plan-batch` for the auditor), so mirroring the three agent files into a suite **without** the skills leaves each agent's declared skill unresolvable — agents and skills must be mirrored together | `3` |
| D-d | The five batch skills (`run-batch`, `plan-batch`, `real-stack-testing`, `validate-real-stack`, `test-driven-development`) resolve from the worker's cwd | F-7; `execution_table.py` ("through the workspace /run-batch skill" from "the current directory") | **—** — measured in §2a/§2b | Without a resolvable `/run-batch` the Conductor worker has no procedure at all. Each suite's own `.claude\skills\` holds only its row-gated skills: PY `gui-validation` + `impeccable`; AN `impeccable`; SY six suite skills (`design-adoption`, `gui-validation`, `sync-contracts`, `ui-ux-pro-max`, `verify-stack`, `webapp-testing`); WD an **empty** `.claude\` directory; SV and SC no `.claude\` at all | `3` |
| D-e | `validate-real-stack` runs `${CLAUDE_SKILL_DIR}\scripts\run_validation.ps1` through `powershell.exe -NoProfile -ExecutionPolicy Bypass -File` | validate-real-stack SKILL.md | present in the superproject mirror (`.claude\skills\validate-real-stack\scripts\run_validation.ps1`) | The script travels **inside the skill folder**, so a byte-identical folder copy carries it; a `SKILL.md`-only mirror would leave the skill pointing at a missing script. Same shape for `real-stack-testing\references\{gui-testing,metered-validation}.md` and `test-driven-development\testing-anti-patterns.md` | `3` (mirror whole folders, then `check_harness_parity.py`) |
| D-f | The **PlantLibrary suite-name shorthand** of run-batch §1.1: an argument `PyApp`/`Server`/… globs `PlantLibrary_<Suite>/implementation/*/BATCH_PLAN.md` | run-batch §1.1 | Works **only from `SW_Development`** | **Measured:** from `PlantLibrary_PyApp` the shorthand glob matches nothing while the general glob `implementation/*/BATCH_PLAN.md` matches exactly one; from `SW_Development` the reverse. The two branches are mutually exclusive by cwd. A Conductor worker's cwd is always the suite, so it must be invoked with **no argument or a bare batch key** — a suite-shorthand argument names neither a path nor (from that cwd) a resolvable suite, and only §1.1's general-glob fallback rescues it. The shorthand belongs to out-of-band sessions started in `SW_Development`, which is how step `9` already phrases it (`/run-batch <suite folder> <key>`) | `9` (keep the path form) · noted for `5`/`6` |
| D-g | The invocation can spawn agents (`skills:`-declared subagents, per-row model selection) | run-batch §4.7, §5, §7; plan-batch §5.3 | VS Code sessions: yes. Conductor's headless worker: **unverified** | Both skills' fallbacks are explicit and mandatory, so this degrades honestly. The canary (step `6`) is the first place it is observed | `6` |

## 2. Measured, not argued

### 2a. Parent-folder skill discovery from `PlantLibrary_PyApp` — **does not work**

```
cwd:      C:\Programmierung\SW_Development\PlantLibrary_PyApp
command:  printf '%s' '<prompt>' | claude -p --model claude-haiku-4-5-20251001
prompt:   Answer only from the list of available skills in your system prompt. Do not use any tool.
          Output ONLY: one skill name per line, then a final line exactly like
          RUNBATCH=yes|no PLANBATCH=yes|no PLANTLIB=<...>
version:  2.1.263 (Claude Code)
```

Observed, verbatim (the whole skill list the fresh session reported):

```
graphify
gui-validation
impeccable
design
dataviz
artifact-design
artifact-diagramming
artifact-capabilities
update-config
keybindings-help
code-review
simplify
fewer-permission-prompts
loop
schedule
claude-api
workflow-authoring
run
init
security-review

RUNBATCH=no PLANBATCH=no PLANTLIB=
```

Reading: exactly three non-built-in skills, and all three are accounted for without the parent —
`gui-validation` and `impeccable` are PyApp's own `.claude\skills\`, and `graphify` is the **user-global**
`C:\Users\WindowsAI\.claude\skills\graphify` (verified: that directory contains `graphify` and nothing else,
which is what makes this measurement clean). **None of the 13 skills in `SW_Development\.claude\skills\`
appears.** Parent-folder discovery from a submodule cwd does not happen.

Side observation to carry into step `5`: the run also printed
`Ignoring 3 permissions.allow entries from .claude/settings.local.json: this workspace has not been trusted.`
A Conductor worker starting in an untrusted suite folder loses that suite's own allow-list.

### 2b. The same from `PlantLibrary_Server` — **does not work**

```
cwd:      C:\Programmierung\SW_Development\PlantLibrary_Server   (no .claude\ directory at all)
command:  identical to 2a
version:  2.1.263 (Claude Code)
```

Observed, verbatim:

```
graphify
design
dataviz
artifact-design
artifact-diagramming
artifact-capabilities
update-config
keybindings-help
code-review
simplify
fewer-permission-prompts
loop
schedule
claude-api
workflow-authoring
run
init
security-review
RUNBATCH=no|no PLANBATCH=no|no PLANTLIB=
```

(The final line's format was garbled by the worker model; the list above it is unambiguous.) Only the
user-global `graphify` plus built-ins. **`run-batch` and `plan-batch` are not discovered.**

> **Verdict for D3: the runbook's default stands.** Discovery does **not** cross from a submodule cwd to the
> superproject's `.claude\skills\`, so the five batch skills *and* the three agents must be mirrored into every
> live suite. D3's "unless step 1 proves parent-folder discovery works" branch does not fire.

### 2c. The dev-repo harness against a scratch copy of PyApp — **three distinct refusals**

Setup (all under `PlantLibrary_PyApp\.tmp\`, which PyApp's `.gitignore` already ignores; nothing committed):

```
scratch root: C:\Programmierung\SW_Development\PlantLibrary_PyApp\.tmp\audit-harness-probe\pyapp
contents:     all 938 git-tracked PyApp files, copied unchanged
harness:      C:\Programmierung\Orchestrator_System\scripts\harness\regression_scope.py
              copied unchanged to <scratch>\scripts\harness\  (md5 32620d601dcca82a22f6e618afb69b2a
              on both sides; dev-repo commit a596e64 "CD2-B326", 2026-08-30)
interpreter:  C:\Programs\AI_Orchestrator_2\.venv\Scripts\python.exe
```

**(i) The script is not standalone.** With only `regression_scope.py` copied:

```
Traceback (most recent call last):
  File "...\.tmp\audit-harness-probe\pyapp\scripts\harness\regression_scope.py", line 43, in <module>
    from run_chunks import (
ModuleNotFoundError: No module named 'run_chunks'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "...\.tmp\audit-harness-probe\pyapp\scripts\harness\regression_scope.py", line 53, in <module>
    from scripts.harness.run_chunks import (  # type: ignore[no-redef]
ModuleNotFoundError: No module named 'scripts.harness'
```

exit `1`. The port is at minimum `regression_scope.py` + `run_chunks.py` (+ `run_validation.py`, which §6.1
and 5a(iii) invoke directly), and the second import path needs `scripts/harness/` to be an importable package.

**(ii) The touched-path set the prompt names is refused.** With `run_chunks.py` and `run_validation.py` also
copied:

```
command: python scripts/harness/regression_scope.py app/services/sync_service.py \
         implementation/System_V1_Implementation/TASK_CHECKLIST.md --format json --max-targets 600
```

stderr, verbatim, exit `2`:

```
remedy [unmapped_touched_path]: the path has no test that reaches it, so the matrix cannot prove it: add a test that imports the module (or names the shipped data file), or record the path in the row's file(s) with a literal non-pytest validation that covers it; then retry the batch
regression scope: unmapped touched path: app/services/sync_service.py
```

stdout: empty. **This is the verbatim refusal F-6 predicted and the evidence runbook D2 asked for.**

**(iii) The doc half of the set routes to sentinels that do not exist here.** The checklist path *alone*
is accepted, and maps to three standing sentinels:

```
command: python scripts/harness/regression_scope.py \
         implementation/System_V1_Implementation/TASK_CHECKLIST.md --format json --max-targets 600
```

```
scope cap: enforcing max targets 600 over 3 discovered target(s)
[
  { "node_id": "tests/gui/real/test_batch_package.py::test_strict_shared_tree_batch_package_lifecycle",
    "reasons": ["standing ledgered shared-tree lifecycle sentinel; changed: implementation/System_V1_Implementation/TASK_CHECKLIST.md"] },
  { "node_id": "tests/test_batch_package_parser.py",
    "reasons": ["standing batch-package parser check; changed: implementation/System_V1_Implementation/TASK_CHECKLIST.md"] },
  { "node_id": "tests/test_batch_progress_refresh.py",
    "reasons": ["standing ledgered progress-contract sentinel; changed: implementation/System_V1_Implementation/TASK_CHECKLIST.md"] }
]
```

All three files **exist in `C:\Programmierung\Orchestrator_System`** and **none exists in PyApp** (verified
both ways). A control run on a real PyApp test (`tests/test_phase3_repositories.py`) maps correctly to itself,
so the import-graph machinery works fine on this tree — the failure is entirely that the sentinels and the
product-path coverage are Orchestrator-specific.

**(iv) The ledger leg refuses before any classification.**

```
command: python scripts/harness/regression_scope.py --classify-pytest-output <artifact> \
         --active-package implementation/System_V1_Implementation
```

verbatim, exit `2`:

```
remedy [known_failure_ledger_unusable]: the active route has no single valid ledger, or a record in it is malformed or ownerless: repair the named ledger record (or name the right --active-package) - never fabricate a package-local ledger - then re-classify
regression scope: no ledger can serve active package: implementation/System_V1_Implementation
```

Taken together: **a PyApp harness port is not a copy.** It needs three scripts, an importable package, suite-named
sentinels for the doc prefixes, a seeded `KNOWN_FAILURES.md`, a `tests/acceptance` target, and a suite-local
source for `max_scope_targets` — six deliverables, not one. That is the real size of step `4`.

*Cleanup:* the scratch tree's files were deleted; three now-empty directories
(`PlantLibrary_PyApp\.tmp\audit-harness-probe\pyapp`) survived removal because a shell still held the path open.
They sit inside PyApp's gitignored `.tmp\`, and `git -C PlantLibrary_PyApp status --porcelain` is empty, so nothing
is committable; delete the `.tmp` folder at the next convenient moment.

## 3. Per suite — what `CLAUDE.md` / `AGENTS.md` must state (the input for step `3`)

Common to all six (write once, adapt the values): **package location** (`implementation\System_V1_Implementation`,
and for Workspace which of its four folders is live); **progress truth** — checklist row status is the single source
of truth, `_ACT_STATE.md` is deprecated, batch done-ness is derived from the rows; **scratch policy** — `.tmp\` is
the one reclaimable scratch parent, it is gitignored, chunk artifacts go to `.tmp\chunks\<run-id>` and never into
`validation\`; **the closeout cap** — `validation.max_scope_targets` is `600` on instance 2 and the shipped example's
`30` is *not* the value to use (C9); **notification** — `scripts\notify_telegram.py` does not exist in this suite, so
the §8 enqueue is expected to fail and is never a batch failure (C13); **deliverable naming** — the
`<TYPE>_<topic>_<YYYY-MM-DD>.md` + `INDEX.md` rule both skills cite (B6/A8).

| Suite | Has today | Must additionally state |
|---|---|---|
| **PyApp** | `CLAUDE.md` (16.6 KB) + `AGENTS.md` (21.2 KB) + `.claude\CLAUDE.md`, all rich | Build/test are already there (`pip install -e ".[dev]"`, `pytest`, `ruff check .`, `ruff format .`, `mypy .`). Add: the **offline startup smoke** as a named standing invariant with its exact command (run-batch §6.8 cites PyApp by name, yet the invariant lives only as a bullet inside `DRIVER_SCRIPT.md` §0); the `GUI\COMMON_GUI_CHANGE_PROTOCOL.md` pointer as binding; the package location. **Remove the stale pointers**: `Improvements/GUI_Improvements_V3/DRIVER_SCRIPT_V3.md` and `TASK_CONTEXT_V3.md` (`CLAUDE.md` l.30/37, `AGENTS.md` l.113/120) name files that exist nowhere in the suite, and `.gitignore` still ignores a root `Improvements/` that no longer exists. Note too that CI's `--ignore=backend/tests` points at an absent path |
| **Server** | `CLAUDE.md` (52 lines: Docker runtime, test-environment distinction, evidence discipline) + `AGENTS.md` (19 lines) | Keep the Docker recipe; add build/test explicitly as run-batch §6.4 needs it: `pip install -e ".[test,lint]"`, `ruff check .`, `pytest -q`, `alembic upgrade head` (from `.github\workflows\ci.yml`). State that **`mypy` is not configured and not a dependency**, so §6.4's type leg is `ruff` only — otherwise a worker installs mypy mid-batch. State that `[tool.pytest.ini_options]` registers **no markers** (the planned `pytest -m stack` tier does not exist). Add package location, progress truth, scratch policy |
| **AndroidApp** | *nothing* | Whole file needed. Build/test: `.\gradlew.bat :app:assembleDebug`, `:app:testDebugUnitTest`, `:app:connectedDebugAndroidTest`, `lintDebug`; Gradle 8.13 wrapper, JDK 17, compileSdk 34. Two facts a worker must not discover the hard way: the build **composite-includes `..\PlantLibrary_SharedContracts\generated\kotlin`**, so the sibling repo must be on disk; and **there is not one test source file in any of the 14 modules** — "unit tests pass" is vacuous until the `AN-V1-TEST-*` rows write some, so §6.4's "suite equivalents" is `lintDebug` + `assembleDebug` only. Standing invariant to promote from `DRIVER_SCRIPT.md` §2.5: "build success alone never marks a runtime row done". `DESIGN.md`/`PRODUCT.md` do not exist yet — record the written fallback (B3). Add `.tmp\` to `.gitignore` |
| **Dashboard** | *nothing* | Whole file needed. Build/test from `package.json`: `npm run lint` (eslint 9), `npm test` (`vitest run`), `npm run build` (`tsc -b && vite build`), `npm run test:e2e` (`playwright test`), `npm run generate:theme`. State there is **no `typecheck` script** — the type leg is `tsc -b` via `build`. State that `playwright.config.ts` has **no `webServer`**: `test:e2e` assumes the dev server *and* the local Docker/OIDC stack are already up (`verify-stack` first) and writes into the MVP evidence folder — it is an evidence harness, not a regression suite. Design: the tokens canon is the sibling `PlantLibrary_SharedContracts\design-tokens\tokens.json`; `DESIGN.md` arrives with `WD-V1-DS-02`. Add `.tmp\` to `.gitignore` |
| **SharedContracts** | *nothing* | Whole file needed. Build/test: `python scripts\validate_contracts.py`, `python scripts\generate_clients.py [--check] [--target …]`, `pytest tests\contract_validation\`, and CI's drift gate `git diff --exit-code -- generated/`. Standing invariants to promote from `DRIVER_SCRIPT.md` §0: never hand-edit generated client code, only regenerate; every regen wave bumps `CONTRACT_VERSION.md` + changelog in the same batch. Flag the live drift: `CONTRACT_VERSION.md` is at **1.2.0** while `generated\CLIENT_MANIFEST.md` still cites **1.1.0**. Note the only ruff config is generator-emitted inside `generated\python\` — there is no repo-level lint. Add `.tmp\` to `.gitignore` |
| **Workspace** | *nothing*, and **no `.gitignore` at all** | Whole file needed, plus a `.gitignore` (its absence is also why `.claude\skills\ui-ux-pro-max\scripts\__pycache__\*.pyc` are committed). State plainly: **this suite has no build system and no test runner**; the only runnable commands are `scripts\check_markdown_links.py` and `scripts\check_contract_version_drift.py`, so those two *are* the "suite equivalents" of §6.4 and the standing-invariant leg. State which of the four `implementation\*` folders is live (`System_V1_Implementation`; `System_Design_Architecture` is gated on `SDA-DEC-01..05`) and that `System_Integration_MVP` and `System_Tooling` are **terminal** — this is the A2 fix, and `implementation\README.md` must carry the same note per F-10 |

## 4. Recommendations for `G1`

| ID | Verdict | Evidence (one sentence) |
|---|---|---|
| **D1** — which packages migrate | **Confirm as written** | The seven live packages are the only ones a worker can reach: every `MVP\` and `Archive_PreMVP\` package sits at `implementation\<X>\package\`, one level too deep for run-batch §1.1's glob, so they are already invisible and need only the README note. |
| **D2** — the closeout harness | **Confirm the decision, revise its size** | §2c reproduces the refusals verbatim (`unmapped touched path`; `no ledger can serve active package`) and adds four things a "port the three scripts" reading would miss — `regression_scope.py` imports `run_chunks` at module load, the doc prefixes route to three Orchestrator-only sentinel tests, `tests/acceptance` is a literal path, and `max_scope_targets` has no readable source from a suite cwd — so step `4` should be scoped as **six deliverables, not a copy**, with step `7` re-using that recipe rather than re-deriving it. |
| **D3** — where the batch skills live | **Confirm as written; the "unless" branch does not fire** | §2a/§2b measured a fresh `claude` 2.1.263 session from both suite cwds listing neither `/run-batch` nor `/plan-batch`, so the full mirror (five skills **and** three agents) is required — and mirror **whole folders**, because `validate-real-stack` calls `${CLAUDE_SKILL_DIR}\scripts\run_validation.ps1` and each agent's frontmatter declares `skills:` that must resolve in the same session (D-e, D-c). |
| **D4** — project topology | **Confirm, with one addition** | One project per package is right, but Workspace's cwd matches **four** `implementation/*/BATCH_PLAN.md` folders and run-batch §1.2's tiebreak ends in "ask the user", which a headless worker cannot do — so the two terminal packages must be demoted (or their `BATCH_PLAN.md` renamed) in step `2b`, not merely README-noted, before Workspace is ever bound. |
| **D5** — `SDA-DEC-01..05` | **Confirm as written** | Non-gating either way, and `System_Design_Architecture` additionally has **no `validation/` directory**, so accepting the five recommendations now costs nothing and lets step `2b` create the missing folder in the same pass. |
| **D6** — canary batch | **Confirm `PY1-B08`** | It is the only candidate that is `skill: none`, pure pytest, no Docker and no GUI driving — and §2c(iii)'s control run shows PyApp's import graph resolves real test paths correctly, so the canary will exercise the ported harness rather than the GUI stack. |
| **D7** — batch order inside each plan | **Confirm, and widen the `SCOPE.md` half** | The reorder is right; note that **no live package has a `SCOPE.md`** and a "Standing invariants" heading exists in exactly one file across all six suites (`Workspace\implementation\System_Tooling\SCOPE.md`, terminal), so the migration must actually author `SCOPE.md` per plan-batch §6 rather than keep amending `DRIVER_SCRIPT.md` — which in PyApp's case still contradicts itself about `_ACT_STATE.md` (A9). |
| **D8** — model defaults | **Confirm as written** | Nothing measured here touches it; the `opus/sol · sonnet/terra · haiku/luna` pairs are exactly `vendors.claude.ladder`/`vendors.codex.ladder` as plan-batch §3 states, and instance 2 has `codex` disabled, so only the left half is ever applied. |

**One item for `G1` that is not in D1–D8:** both skills cite a **"Deliverable naming" section of `CLAUDE.md`**
(run-batch §6.10, plan-batch §5.4) that exists in **no** `.md` file in any of the six suites or in the superproject
`CLAUDE.md`, and no `implementation\**\INDEX.md` exists either (B6/A8). Step `3` should either author the section
and the per-folder `INDEX.md` files, or the gap should be routed into step `8` — as it stands, two skills enforce a
rule against an authority that is not there.
