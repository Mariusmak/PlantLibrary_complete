# SW_Development — PlantLibrary superproject

The superproject of the PlantLibrary repository set. It owns no product code: it pins the six
suite repositories as submodules (Workspace, Server, SharedContracts, PyApp, AndroidApp,
Dashboard), carries the Claude skills and agents the suites mirror, the static hygiene and
harness checks that span all seven repositories, and the records of the cross-repository
programs. This file is the instruction surface for every session started here; its session
rules bind in the suites too, and each suite `CLAUDE.md` adds that suite's parameters.

## Testing

- **Never fake the layer under test.** Tests substitute only *process
  boundaries* — subprocesses, third-party HTTP, the clock, randomness. The
  composition root, domain services, persistence, and routes/rendering always
  run for real. A fixture class that re-implements logic living in `src/` is a
  defect, not a fixture: it makes the suite green while the product is broken.
- Any test spanning more than one module (integration, e2e, browser,
  acceptance, batch-row validation) must follow the `real-stack-testing` skill.
- After implementation, invoke `validate-real-stack` with the exact named
  validation. Its `real-stack-validator` subagent (Sonnet 5.5) runs in isolated
  context and returns compact evidence; the parent implementation agent remains
  responsible for fixes and completion.
- UI tests fail on uncaught console exceptions, unasserted 4xx/5xx, and
  server-side exceptions — not only on missing selectors.

## Authority

- **Requirements live in the batch packages, never in this file.** Each suite's live package is
  `implementation/System_V1_Implementation/` inside that suite (`BATCH_PLAN.md`,
  `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`, `SCOPE.md`, `CONTEXT_INDEX.md`). Every
  other package under a suite's `implementation/` (`MVP/`, `Archive_PreMVP/`, the Workspace's
  terminal and superseded packages) is history: read for context, never consulted for
  requirements, never edited.
- Precedence: where prose conflicts with a SharedContracts schema, contract or generated
  artifact, **the contract wins**. A suite `CLAUDE.md` adds parameters to this file's session
  rules and never relaxes them.
- **A prompt never overrides a skill.** Pasted instructions — operator prompts, `PROMPTS_*.md`
  runbook entries (for example under `rework/`), a handover's continuation section — say *what*
  to work on and may narrow it (what not to touch, when to stop). `run-batch`, `plan-batch` and
  `real-stack-testing` say *how*, including what counts as proof. Where they conflict **the
  skill wins**: name the conflict in one line, do the skill's version, and record it in the
  report. A prompt that asks for a proof surface the skill forbids — an unscoped whole-suite
  run, a skipped named validation, a hand-rolled chunk driver — is a defect in the prompt, never
  a licence. The only way to widen a proof surface is a package amendment to the row's
  `validation` cell, recorded as a decision in that package's `STATE.md`.
- **Deviations require an explicit operator decision**, recorded where the rule lives: a package
  deviation in the package's `STATE.md`; an exemption, hold, release, root or allowlist change as
  a `D-YYYY-MM-DD-nn` entry in that repository's `hygiene/HYGIENE_DECISIONS.md`; a program's
  choice as an answered row of that program's question register (the open program's is
  `rework/REGISTER_operator-questions_2026-10-13.md`, mirrored in its runbook's §Q).
- **Codex is frozen; `CLAUDE.md` is the live text.** The freeze is block-aware (master rework
  Q-G-09 (a)): `AGENTS.md` and `.codex/**` are kept, never deleted and never mirrored from
  `.claude/`; only the installer-owned marker blocks inside `AGENTS.md` stay live, written by
  their installers. The banner, the decision entry and the digest guard belong to the freeze step
  (master rework `B7-2`); outside that step neither is edited by hand.

## Repository layout

| Path | Purpose |
|---|---|
| `PlantLibrary_Workspace/` | Coordination suite, no product code: methodology, the canonical system description, the system-level packages (live: `implementation/System_V1_Implementation/`) |
| `PlantLibrary_Server/` | The API server; Docker is its authoritative local runtime |
| `PlantLibrary_SharedContracts/` | The contract bundle every suite pins: OpenAPI export, schemas, sync and page contracts, design tokens, generated Python/TypeScript/Kotlin clients |
| `PlantLibrary_PyApp/` | Offline-first desktop client (Python, PySide6, SQLite) |
| `PlantLibrary_AndroidApp/` | Android client (Kotlin, Jetpack Compose) |
| `PlantLibrary_Dashboard/` | Web dashboard (React, TypeScript, Vite) |
| `.claude/skills/`, `.claude/agents/` | The shared skills and agents; each suite mirrors the shared set byte for byte |
| `.agents/README.md` | The bridge file: what is frozen, what is Claude-only, the agent roster |
| `.codex/`, `AGENTS.md` | Codex mirrors, frozen (see Authority) |
| `scripts/harness/` | Static guards over all seven repositories; its `README.md` is the inventory and says which check follows which edit |
| `scripts/hygiene/`, `hygiene/`, `.github/workflows/repo-hygiene.yml` | The installed hygiene checker; the pin and roots (`hygiene/CONSUMED_HYGIENE.md`) and the append-only decision record (`hygiene/HYGIENE_DECISIONS.md`); its CI job |
| `repo-hygiene/`, `onboarding/`, `rework/`, `reviews/` | Declared deliverable roots: the hygiene track, the Conductor onboarding track, the master rework program (opened 2026-10-13), the operator-run review skills' audits |
| `handovers/` | Declared deliverable root: handovers and findings |
| `archive/` | Retired material, moved by `git mv` with names unchanged (legacy exempt tree, `D-2026-10-14-01`); `archive/README.md` maps old to new paths. Holds `archive/root/IMPLEMENTATION_PLAN.md`, the 2026-08-04 program sequencer replaced by the master rework runbook's §H: never a requirements source |

The root-allowlist module is on: a new top-level path needs an allowlist entry, and that entry
is a decision entry in `hygiene/HYGIENE_DECISIONS.md`.

## Workflow

- **Seven repositories, one writer each at a time.** Each suite is its own repository on `main`
  with its own GitHub remote; the superproject is on `master` (remote
  `Mariusmak/PlantLibrary_complete`) and records each suite as a gitlink. A suite change commits
  in the suite first; the superproject then bumps that gitlink in one commit per step, carrying
  the step's ledger flip where a runbook keeps one. A second writer on the same repository waits
  or works in its own worktree.
- **Plan:** from the suite's folder, `/plan-batch implementation/System_V1_Implementation <what to plan>`.
- **Execute:** `/run-batch implementation/System_V1_Implementation [batch-key]` — one batch per
  invocation. Always pass the package path: with no argument run-batch globs
  `implementation/*/BATCH_PLAN.md` under the cwd, and the Workspace holds several packages.
- **Progress truth** is the `status` cell of the package's `TASK_CHECKLIST.md` rows; a batch
  heading's `(done)` follows its rows. `_ACT_STATE.md` and `DRIVER_SCRIPT.md` are legacy: never
  created, read as instructions or followed.
- **Programs** that span repositories run from a `PROMPTS_*.md` runbook in a declared root, one
  fresh session per step; the runbook's ledger is the only status, and its question register
  holds what waits on the operator. The open program is
  `rework/PROMPTS_master-rework-runbook_2026-10-13.md`.
- **Checks before a commit:** the repository's hygiene checker
  (`python scripts/hygiene/repo_hygiene_check.py check`, zero violations) before every commit
  that touches markdown, `CLAUDE.md` or `AGENTS.md`, and the harness check that
  `scripts/harness/README.md` names for the edit made.

## Engineering standards

- **Product invariants live with the product:** in each live package's `SCOPE.md`
  `## Standing invariants` and in the suite guides, never in this file.
- **Windows-first.** The machine is Windows 11 with PowerShell and Git Bash: paths, shells and
  line endings follow Windows; no POSIX-only assumptions. The literal `python` resolves to the
  base interpreter regardless of an active virtual environment: use the interpreter the suite
  guide names.
- Never put real secrets, tokens, or chat IDs in code, config examples, fixtures, logs, or
  commits — placeholders only.
- **Leave what you did not make.** Remove only the dead code your own change orphaned.
  Pre-existing dead or duplicated code is reported as a finding, never deleted in passing. State
  the assumptions a change rests on in its report.
- **Cheapest gate first; narrowest rerun after a red.** The suite's lint and format checks on
  the touched files come before any run wider than the row's named validation. After a failure:
  the failing case → its file → the owning named command. The batch's scoped closeout is the
  only wider surface, and it runs when `run-batch` says — once, as a stated new generation after
  any touched-path edit — never as a diagnostic rerun. An improvised whole-suite run is never
  part of a batch's proof surface. Each suite guide names its commands.
- **Scratch stays under the suite's `.tmp/`**, as that suite's `## Scratch policy` lays it out:
  git-ignored, reclaimable, never committed. Nothing runs elevated, and no scratch path points
  outside the repository.

## Session rules (operator and orchestrated sessions)

These bind every session an operator or orchestrator starts in this superproject or in a
submodule; each suite `CLAUDE.md` points here and adds that suite's parameters (master rework
Q-A3-03 (a)). A batch worker dispatched by a Conductor instance follows `run-batch`/`plan-batch`
and the package `SCOPE.md` instead: it never commits or pushes.

1. **Models.** `fable`, `opus`, `sonnet` resolve to Fable 5.1, Opus 5.5 and Sonnet 5.5;
   "Fable 5"/"Opus 5"/"Sonnet 5" in older text means the current model. A session runs on
   Opus 5.5 at high or xhigh; Fable 5.1 only where a wrong judgment costs weeks (open design,
   cross-repository synthesis, a security miss), with the reason stated; Sonnet 5.5 only for
   subagents. A package `model` cell (`opus/sol`, `sonnet/terra`, `haiku/luna`) is a worker tier
   tuple a Conductor instance resolves through its own config: a parsed contract, never
   rewritten in passing, its Codex half inert while Codex is frozen. `haiku` is a worker tier
   only, never a session or subagent model; a re-tier is a `plan-batch` amendment of that row
   when the row is next touched.
2. **One test slot.** One closeout at a time on the machine, and no test load beside it. A
   validation a session starts on its own uses its own slug under the suite's `.tmp/` (the
   suite's `## Scratch policy`), never a path another run holds. A program may take the slot
   away entirely: the master rework program runs no test.
3. **Headless.** A headless session cannot ask: it stops with the question in its report (inside
   a program, as a proposed row for that program's question register). It never ends its turn
   while background work runs: long commands run in the foreground with a tool timeout up to
   3,600,000 ms.
4. **Bound suites.** A tracked file in a suite whose project is bound on a Conductor instance —
   currently none; the instance-2 bindings are obsolete — changes only while that project is
   held and no attempt is open (read from the instance's store `mode=ro`).
5. **Commits.** A session commits only in the repositories it was given, on their branch (`main`
   in a suite, `master` here), and never pushes. Pushes happen at a boundary, by the
   orchestrating session or the operator: plain `git push`, each moved suite's `main` first, the
   superproject last after checking that every gitlink's commit is on its suite's remote
   (`git -C <suite> branch -r --contains <sha>`); never forced, never another session's branch.
6. **Bytes.** Instruction and package files are LF in the index and mostly CRLF in this
   checkout: write a file back with its own line endings (`git ls-files --eol` before the
   commit); never a text-mode rewrite, never a `core.autocrlf` change.
7. **Decision ids.** Mint a `D-<date>-<nn>` only after a grep over the superproject, each
   submodule (`git -C <suite> grep`; `--recurse-submodules` from here returns superproject hits
   only) and every worktree.
8. **Subagents.** Fan out in one message with a fixed return schema; a verdict is a claim,
   verified once on the critical path; one that dies on a limit is finished inline or recorded
   as not read. In a headless session subagents run in the foreground.
9. **Read-only sources.** The Conductor checkouts (`C:\Programmierung\Orchestrator_System` and
   its worktrees) and the two template kits (`C:\Programmierung\Design_Template_Kit`,
   `C:\Programmierung\Repo_Hygiene_Template_Kit`) are read-only from here: git reads there use
   `--no-optional-locks` and nothing writes; a live instance is read from its store `mode=ro`,
   never polled over REST; a kit defect is recorded as a finding, never patched from here.
10. **Elevation.** Nothing runs elevated unless the operator's own act says so, and nothing is
    quoted from a credential or a config file beyond the keys a step names. A sandbox
    permission (the Server's Docker pipe) is not elevation.

## Claude subagent roster

`.claude/agents/` defines the project subagents; each suite carries byte-identical copies,
checked by `scripts/harness/check_harness_parity.py`. Skills reference them only behind "if this
invocation can spawn agents" with a mandatory inline fallback.

- `real-stack-validator` (Sonnet) — executes one named validation, invoked via
  `validate-real-stack`.
- `batch-plan-auditor` (Sonnet) — fresh-context adversarial run of plan-batch's self-review on a
  draft before the package is written.
- `batch-closeout-reviewer` (Opus) — pre-commit batch diff review against each row's done-when,
  the package `SCOPE.md`, and its standing invariants.

The three are the Conductor's shared agents, adopted verbatim at master rework `B1-1`. Bridge
table, the Claude-only skills and the frozen Codex counterparts: `.agents/README.md` (rewritten
at `B1-1`).

<!-- repo-hygiene:begin -->
## Repository hygiene (installed by the Repo Hygiene Template Kit — do not hand-edit this block)

Deliverable roots, exemptions and holds are declared in `hygiene/CONSUMED_HYGIENE.md` and
`hygiene/HYGIENE_DECISIONS.md`; read both before creating, renaming or moving a markdown file. A new
file in a declared root is `<TYPE>_<topic>_<YYYY-MM-DD>.md`, `TYPE ∈ {PROPOSAL, PROMPT, PROMPTS, PLAN,
EVIDENCE, AUDIT, REGISTER, MATRIX, SNAPSHOT, HANDOVER, FINDING}`, dated by its git-created date, with a
line in that root's `INDEX.md` in the same commit; `INDEX.md`/`README.md` are exempt; a numbered chapter
set is one dated folder with one index line. A rename is `git mv` plus a mapping-table row and a
reference sweep; a name cited by a file that must not be edited is held, and old names resolve through
the root's "Renamed" table. A `PROMPT`/`PROMPTS` file and a handover's continuation section state scope,
constraints, done-when and the commit line — never a proof surface or a test invocation; proof belongs
to the document that owns the verification order. An exemption, a hold, a release, an enum extension,
a root change or an allowlist change is a `D-YYYY-MM-DD-nn` entry in `hygiene/HYGIENE_DECISIONS.md`,
never a silent edit. The checker under `scripts/hygiene/` is the contract; how it is run and read is
the kit's `installer/INSTALL.md`, Verify section. Kit: `C:/Programmierung/Repo_Hygiene_Template_Kit` @ `0.3.0`. A prompt never
overrides this block.
<!-- repo-hygiene:end -->
