# PlantLibrary master rework — program runbook (lanes `A1`…`A9`, `B1`…`B8`, `C1`)

*Opened 2026-10-13 at `R-0` by the orchestrating session (Fable 5.1 · high) of
`PROMPT_master-rework-kickoff_2026-10-13.md`. One program, many lanes: this file is the authority for **what runs,
in which order, beside what, with which model and reasoning**, and its §L is the only status. §3 is written at
`R-3` from the analysis registers, never from memory of the sources; where a step needs a fact, it cites the
register that holds it.*

## 0. What this is, and what it is not

| | |
|---|---|
| Scope | Bring `C:\Programmierung\SW_Development` (the superproject) and its six submodules `PlantLibrary_Workspace`, `PlantLibrary_PyApp`, `PlantLibrary_AndroidApp`, `PlantLibrary_Dashboard`, `PlantLibrary_Server`, `PlantLibrary_SharedContracts` up to the standards, skills, kits, harnesses and conventions the Conductor program developed since 2026-09: (A) a parallel read-only analysis of the Conductor and kit repositories, (B) the transfer in eight lanes — skills and agents, instructions, hygiene and archive, batch packages, the Design Configuration and anchoring, the GUI rework per client, the harness port, the Conductor onboarding alignment — and (C) the hand-back to validated batch work |
| Roots | **TARGET** — the seven repositories above, the only trees this program writes (superproject `master`, each submodule `main`; every submodule has its own GitHub remote; gitlinks in the superproject's index). **SOURCE-C** — `C:\Programmierung\Orchestrator_System` (`main`, `2e7adb3`) and every `Orchestrator_System*` worktree beside it; read-only by absolute path, `git` reads with `--no-optional-locks` only, a live Conductor works on `main`. **SOURCE-K** — `C:\Programmierung\Design_Template_Kit` (`master`, `f08e588` = Kit 1.7.0, tag `v1.0.0`) and `Design_Template_Kit_wt\*`; `C:\Programmierung\Repo_Hygiene_Template_Kit` (`0.2.1`); read-only, a kit defect is recorded, never patched from here. **SOURCE-R** — `C:\Programmierung\Conductor_GUI_Reconciliation_2026-10-12`, `C:\Programmierung\Working_Folder`; read-only |
| Ledger of record | §L at the end of this file, one row per step; flipped in the same commit as the step's output. Operator answers are recorded in `REGISTER_operator-questions_2026-10-13.md` (the register of record) and mirrored in §Q, same commit. Deferred validations in `REGISTER_deferred-validations_2026-10-13.md`. Reuse verdicts in `REGISTER_conductor-reuse-candidates_2026-10-13.md` |
| Models | Orchestrator Fable 5.1 · high (xhigh for `R-3`); analysis lanes Opus 5.5 · high; mechanical census lanes Sonnet 5.5 · high; execution lanes Opus 5.5 · high; IA, mockup and design-decision steps Opus 5.5 · xhigh; operator sessions Opus 5.5 · high. Every §3 row names its own |
| What this file never does | Run or name a test. No step of Phases A and B runs a unit or integration test runner, browser automation, an emulator, a Gradle test task, a Docker stack or an app launch for validation; the one test slot of this machine is the Conductor's for the whole program. A step that needs one writes a row into the deferred-validation register and goes on. Name a proof surface: a paste block states scope, read-first, constraints, done-when and the commit line; what counts as proof belongs to the batch-package row's `validation` cell and the executing skill's standing legs, which Phase C resumes. Override a skill: Phase B lanes are runbook steps, not `run-batch` batches, and every batch-package edit follows `plan-batch`'s row schema with a dated decision in the package's `STATE.md`. Write a source: a finding about the Conductor, a kit or the reconciliation folder is a register row. Push: no session pushes (`Q-G-03`) |

## 1. Where things stand (re-measured 2026-10-13 at `R-0`)

Kickoff facts (`PROMPT_master-rework-kickoff_2026-10-13.md` §1) hold except where this table says otherwise; only
what `R-0` names was re-verified. Refreshed when three days old or when a lane closes.

| Fact | Measured at `R-0` |
|---|---|
| Superproject | `master` at `67dcc51`, tracking `origin/master`; working tree clean except the `PlantLibrary_Workspace` gitlink (pinned `752ff51`, checkout `6b4b88b` = `a5ab0a7` methodology 4.1.0 + `6b4b88b` DTI G-close). `R-0` bumps it |
| Submodules | all six on `main`, clean: Workspace `6b4b88b`, PyApp `35ddc63`, AndroidApp `5d6410f`, Dashboard `7795fc8`, Server `f1a31b9`, SharedContracts `d43f7a2`. Dashboard, Server and SharedContracts are each **one commit ahead of their origin, unpushed** — an operator push item (`Q-G-03`), not a program action |
| Worktrees | none beyond the seven checkouts (`git worktree list` in all seven) |
| Disk | C: 77 GB free of 299 GB (25 %); the kickoff's 69 GB (23 %) was the earlier reading. Floor for a new worktree: 20 % |
| Sessions | ListAgents at `R-0`: one idle peer session on this repository, no orchestrator owning it; the Conductor's own orchestrator session busy on `Orchestrator_System` (never touched) |
| Hygiene | checker verdict before `R-0`: `repo-hygiene: pass with holds — 0 violations, 3 held` (the three onboarding-runbook holds of `D-2026-09-16-01`/`-03`). Pin kit `0.2.1`, module `root-allowlist`, floor 1. Last decision id `D-2026-09-16-03`; `R-0` writes `D-2026-10-13-01` (root `rework`, allowlist) |
| Line endings | superproject: index LF throughout (`core.autocrlf=true`); working tree CRLF for `CLAUDE.md`, `AGENTS.md`, `hygiene/HYGIENE_DECISIONS.md`, the three root indexes; LF for `hygiene/CONSUMED_HYGIENE.md`. Per-submodule summary is `A8`'s |
| Skills and agents | superproject `.claude/skills`: 13 folders as the kickoff lists; `.claude/agents`: 3; `.claude/settings.json` is `{}`; `settings.local.json` denies the destructive git commands rule 8 names. `.codex/` present (agents, hooks, hooks.json, skills). Conductor-side counts (17 skills, 4 agents, Codex frozen) are `A1`'s to verify |
| Claude CLI | 2.1.292; headless lanes: `claude -p` with `--model`, `--effort`, `--permission-mode`, `--add-dir`, `-w/--worktree`, `--bg`, `--output-format` (seen in `claude --help` at `R-0`) |
| Two prior tracks | `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md`: `M-1`…`M-7` done, `M-8` and `M-9` open, K-7 undecided. `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md`: steps `0`…`5` done, `6` held (Conductor `S-2`), §N owes six notes |

## 2. Rules

The ten rules of `PROMPT_master-rework-kickoff_2026-10-13.md` §2 bind every session of this program and are not
restated here. In one line each, for the reader who opens this file first: (1) no test, ever — record the need in
the deferred-validation register; (2) sources are read-only; (3) the hygiene rule blocks apply to every file
created or moved, checker before every markdown commit; (4) a prompt never overrides a skill, package edits follow
`plan-batch` and are decisions in `STATE.md`; (5) one writer per repository, worktrees for a second, gitlinks bumped
one commit per step with the ledger flip; (6) analysis lanes fan out as subagents with a fixed return schema, at
most four write sessions beside the orchestrator, verdicts are claims verified once on the critical path; (7)
operator questions never block — register row, `waits Q-…`, operator session (§O); (8) bytes and shells — own line
endings, no heredoc Python with Windows paths, per-submodule grep; (9) models per row; (10) two lines to the
operator per step start and finish, HANDOVER at every stop.

## 3. Lanes and step map

*Filled at `R-3` from the registers of `R-1`/`R-2`. Until then this section holds the lane list and the per-step
row shape only.*

### 3.0 Row shape (every step)

| Field | Content |
|---|---|
| id · title | `<lane>-<n>` — what the step produces |
| model · reasoning | from §0's ladder |
| route | `session` (a headless `claude -p` or an interactive paste) · `subagent` (spawned by the orchestrator, worktree-isolated when it writes) · `procedure` (the orchestrator's own hands) · `gate` (an operator decision recorded in the register) · `operator` (the operator session, §O) |
| cwd · branch | the repository and branch the step writes; a worktree path when rule 5 requires one |
| precondition | steps done, questions answered |
| writes | the files and repositories the step changes |
| paste block | scope, read-first, constraints, done-when, commit line — never a proof surface |
| waits | `Q-…` rows that gate it, or `—` |

### 3.1 Lanes (the kickoff's list; each becomes a numbered step set at `R-3`)

| Lane | What | Repositories |
|---|---|---|
| `A1`…`A9` | Phase A, read-only analysis (skills and agents; harnesses and scripts; instructions; design kit and methodology; runbook conventions; corpus census ×7; batch packages; git structure; GUI current state ×3) | reads SOURCE-*, writes `rework/` only |
| `B1` | skills and agents sync: the superproject `.claude/` first, then the six mirrors, parity green, Codex as `Q-G-09` decides | all seven |
| `B2` | `CLAUDE.md` and `AGENTS.md` reconciliation from `A3`'s blueprint, plus `PyApp/.claude/CLAUDE.md` | all seven |
| `B3` | hygiene, restructure and archive: new roots, renames, holds released, archive trees, `M-8`/`M-9` closed, stale sequencers as `Q-G-05` decides | all seven |
| `B4` | batch packages: schema and model column, requires tokens, `DRIVER_SCRIPT.md` retired, sequencers replaced by the hand-back section, instance 2's bind contract met (static check) | the six suites (seven packages) |
| `B5` | Design Configuration: canon imported, DRAFT, design gate (operator), BINDING; anchoring in Dashboard, AndroidApp, PyApp with stacks, rule blocks, the four Kit skills and impeccable; design-adoption as `Q-G-07` decides | SharedContracts (`Q-G-01`), Dashboard, AndroidApp, PyApp |
| `B6` | GUI rework per client: design-migration workspaces (methodology 4.1.0), census, screen contracts, IA and mockups, gap map, change classification, direct implementation with mechanical design checks only; order as `Q-G-08` decides | Dashboard, AndroidApp, PyApp, Workspace |
| `B7` | harness port: hygiene guards, proof-surface guard, parity checker extended, package checker, scratch policy, living-docs standard where it fits | all seven |
| `B8` | Conductor onboarding alignment: §N notes discharged, bindings re-verified statically, onboarding ledger updated | superproject, PyApp, Server |
| `C1` | hand-back: the deferred-validation register turned into the first batches by `plan-batch`, the resume prompt for validated batch work, a HANDOVER | superproject, the suites |

### 3.2 Steps

*To be written at `R-3`.*

## 3a. What may run beside what

*To be written at `R-3`. Standing rule until then: one writer per repository; at most four write sessions beside
the orchestrator; read-only analysis lanes have no limit beyond context.*

## Q. Operator questions — mirror of the register

The register of record is `REGISTER_operator-questions_2026-10-13.md`; this table mirrors its ID, state and answer
columns and is flipped in the same commit. (a) is always the recommendation.

| ID | Question (short) | Recommended | Waits | State | Answer (verbatim, date) |
|---|---|---|---|---|---|
| `Q-G-01` | Where the Design Configuration lives | (a) `SharedContracts/design/`, clients pinned via `CONSUMED_DESIGN.md` | `B5`, `B6` | open | |
| `Q-G-02` | Repository structure | (a) keep superproject + six submodules | `B3`, `B4` | open | |
| `Q-G-03` | Pushing | (a) no session pushes; operator pushes per wave | all write lanes | open | |
| `Q-G-04` | Mechanical checks allowed in Phase B | (a) linters, formatters, type checks, Kit static checks only | `B5`, `B6`, `B7` | open | |
| `Q-G-05` | Stale sequencers | (a) archive `IMPLEMENTATION_PLAN.md`/`WORKSPACE_STATE.md` after `B4`'s hand-back; `Todo.md` ideas to a REGISTER | `B3`, `B4` | open | |
| `Q-G-06` | Kit finding K-7 | (a) record, hold, queue a Kit session for the operator | `B3` | open | |
| `Q-G-07` | The design-adoption skill | (a) retire for the Kit's design-gate after `B5`, leave a pointer | `B5`, `B1` | open | |
| `Q-G-08` | GUI rework order | (a) plan all three, implement Dashboard first | `B6` | open | |
| `Q-G-09` | Codex | (a) freeze as the Conductor did | `B1`, `B2`, `B7` | open | |

## O. The operator session

Start a fresh session — **Opus 5.5 · high**, cwd `C:\Programmierung\SW_Development` — and paste the block below.
Keep it current: the orchestrator rewrites it whenever the open set changes.

```text
You are the operator session of the PlantLibrary master rework program (cwd C:\Programmierung\SW_Development,
branch master). Scope: walk the operator through every open row of rework/REGISTER_operator-questions_2026-10-13.md
in dependency order (Q-G-02 and Q-G-03 first, then Q-G-01, Q-G-04 … Q-G-09, then any lane question), record the
answers verbatim, flip the rows, mirror them into §Q of rework/PROMPTS_master-rework-runbook_2026-10-13.md, and
commit. Read first: the register (the Why (a) column is the orchestrator's reasoning), the runbook §0 and §1, and
for a question that cites one, the register or audit row it names. For each question, say in plain words what is
being decided, what (a) is and why it is recommended, what the other options cost, and which steps wait on it;
then ask. Constraints: never answer a question yourself; never edit a file outside the register and the runbook's
§Q; never run a test; never push unless the operator says so in this session (Q-G-03 (a) makes the end-of-wave
push an operator act — if they ask for it, push the superproject and each submodule's main with plain git push,
nothing forced). Done-when: every row the operator answered reads `answered` with the words and the date, §Q
mirrors it, the hygiene checker is green, and the commit is made. Commit line:
`rework: operator - questions answered <date> (<ids>)`.
```

## L. Ledger — flip as you go

| Step | What | Model · reasoning | Status |
|---|---|---|---|
| `R-0` | verify and open the track: `D-2026-10-13-01` (root `rework`), index, kickoff prompt, runbook skeleton, three registers, Workspace gitlink `6b4b88b` | Fable 5.1 · high | done 2026-10-13 — this commit |
| `R-1` | Phase A: `A1`…`A9` fanned out as subagents, one REGISTER or AUDIT each under `rework/`, the three most consequential claims per lane verified by the orchestrator | Fable 5.1 · high (lanes Opus 5.5 · high; `A4` xhigh; `A6` Sonnet 5.5 · high ×7; `A9` ×3) | done 2026-10-13 — 18 audits under `rework/`, 54 lane claims re-checked by the orchestrator (all held); this commit |
| `R-2` | the reuse register merged from `A1`…`A9` | Fable 5.1 · high | todo |
| `R-3` | §3, §3a, §Q, §O, §L filled; the operator told where the runbook and register are | Fable 5.1 · xhigh | todo |
| `R-4` | execution of every runnable lane step, worktrees merged at boundaries, register re-read at every boundary | Fable 5.1 · high (lanes per row) | todo |
| `R-5` | close: §L complete, §1 final, final HANDOVER, Phase C resume prompt | Fable 5.1 · high | todo |
