# PlantLibrary master rework — program runbook (lanes `A1`…`A9`, `B1`…`B8`, `C1`)

*Opened 2026-10-13 at `R-0` by the orchestrating session (Fable 5.1 · high) of
`PROMPT_master-rework-kickoff_2026-10-13.md`; §3 written at `R-3` (Fable 5.1 · xhigh) from the seventeen Phase A
audits and the three registers, never from memory of the sources. One program, many lanes: this file is the authority
for **what runs, in which order, beside what, with which model and reasoning**, and its §L is the only status. A
finding made while following it goes to its own `FINDING_`/`AUDIT_` file and an inserted step, never into this file
as a chapter. The template it follows is `AUDIT_runbook-conventions_2026-10-13.md` §7.*

## 0. What this is, and what it is not

| | |
|---|---|
| Scope | Bring `C:\Programmierung\SW_Development` (the superproject) and its six submodules `PlantLibrary_Workspace`, `PlantLibrary_PyApp`, `PlantLibrary_AndroidApp`, `PlantLibrary_Dashboard`, `PlantLibrary_Server`, `PlantLibrary_SharedContracts` up to the standards, skills, kits, harnesses and conventions the Conductor program developed since 2026-09: (A) a parallel read-only analysis of the Conductor and kit repositories, (B) the transfer in eight lanes — skills and agents, instructions, hygiene and archive, batch packages, the Design Configuration and anchoring, the GUI rework per client, the harness port, the Conductor onboarding alignment — and (C) the hand-back to validated batch work |
| Not here | batch-package content (the packages are truth); decision texts (`STATE.md`, `hygiene/HYGIENE_DECISIONS.md`: cited by id, never copied); analysis findings (their `AUDIT_`/`REGISTER_` files under `rework/`); the Conductor's runbooks; Phase C batch runs; the GUI rework's per-step blocks (pointed: `PROMPTS_gui-rework-runbook_2026-10-13.md`) |
| Tag | `rw`; step ids `<lane>-<n>` (§2 rule 2) |
| Home branch and absolute path | superproject `master` — `C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md`; every other checkout and worktree reads it by this path, read-only |
| Roots | **TARGET** — the seven repositories above, the only trees this program writes (superproject `master`, each submodule `main`; every submodule has its own GitHub remote; gitlinks in the superproject's index; the submodules are old-form and uninitialized, each with an embedded `.git` directory). **SOURCE-C** — `C:\Programmierung\Orchestrator_System` (`main`, `2e7adb3`) and every `Orchestrator_System*` worktree beside it; read-only by absolute path, `git` reads with `--no-optional-locks` only, a live Conductor works on `main`. **SOURCE-K** — `C:\Programmierung\Design_Template_Kit` (`master`, `f08e588` = Kit 1.7.0, tag `v1.0.0`) and `Design_Template_Kit_wt\*`; `C:\Programmierung\Repo_Hygiene_Template_Kit` (`0.2.1`); read-only, a kit defect is recorded, never patched from here. **SOURCE-R** — `C:\Programmierung\Conductor_GUI_Reconciliation_2026-10-12`, `C:\Programmierung\Working_Folder`; read-only |
| Ledger of record | §L here, nowhere else; flipped in the commit that carries the step's output, or, for a step whose output commits outside the superproject `master`, in the orchestrator's gitlink-and-flip commit (§2 rule 4). Questions: `REGISTER_operator-questions_2026-10-13.md` (register of record), mirrored in §Q in the same commit. Deferred validations: `REGISTER_deferred-validations_2026-10-13.md`. Reuse verdicts: `REGISTER_conductor-reuse-candidates_2026-10-13.md` |
| Inputs (decision ids) | `D-2026-10-13-01` (root `rework`); answered `Q-…` rows by id as they land (§Q); each `D-…` a step writes, appended to §L's Decision column as it lands |
| Models | §2a; every §3 row names its own |
| What this file never does | Run or name a test, a test runner, a tests root, a selection flag or a whole-suite phrase; widen, delete or rewrite a validation cell; carry status outside §L; copy a block from another file (it points); put a launch value (a base SHA, a D-id, an earlier step's commit) inside a fence; decide (every choice is a `Q-…` row or a `gate` step); write a source; push |

## 1. Where things stand — measured at `4dcf737` on 2026-10-13 (R-4.2)

≤ 15 rows, rewritten whole when three days old or when a lane closes; no step status here.

| Fact | Measured |
|---|---|
| Superproject | `master` at `4dcf737` before this boundary's commits, 36 commits ahead of `origin/master` until this boundary's push; tree clean |
| Submodules | all six on `main`, clean: Workspace `41fd24c`, PyApp `e17d7ba`, AndroidApp `2353b6c`, Dashboard `604d1d0`, Server `d6a6497`, SharedContracts `72e5a38`; each 5–10 commits ahead of its origin until this boundary's push |
| Submodule form | unchanged: old-form, uninitialized, embedded `.git` directories; index LF everywhere; no repo-wide attributes (path-scoped `eol=lf` lines now exist in SharedContracts `design/` and the three anchored clients) |
| Worktrees | none in TARGET; the two kit worktrees of `K-1`/`K-2` removed after their merges |
| Disk | C: 73 GB free of 299 GB (24.4 %); floor 20 % |
| Hygiene | superproject `pass with holds — 0 violations, 3 held`; Workspace 10 held; the other five suites `0 held` (the five V1 proposal holds released at `B3-4`); all seven still pinned to kit `0.2.1` (re-pin to `0.3.0` is `B3-8`); the K-7 finding resolved by kit 0.3.0 |
| Harness guards | parity `pass` over 7 repositories (Codex frozen 7/7 at `B7-2`, mirrors equal, bridge coverage checked); package census 0 errors (60 batches, 185 rows) under main's parser and instance 2's; newline guard 0 mixed contract files |
| Skills and agents | the superproject carries 17 skill folders (13 original, plan-batch 1.5.1-pl, 3 Conductor agents verbatim, harness-upkeep, scratch-gate in PyApp/Server, three third-party review skills; design-adoption a pointer); every suite mirrors the shared five plus its named extras as byte copies; `.claude/settings.json` tracked |
| Instructions | all seven `CLAUDE.md` reconciled (`B2-1`…`B2-3`, `B2-1.1`); every `AGENTS.md` frozen outside its installer-owned blocks with a banner; PyApp `.claude/CLAUDE.md` a stub |
| Packages | seven live packages at plan-batch 1.5.1-pl with decision lines, Traceability sections, SCOPE procedure lines; `DRIVER_SCRIPT.md` pointer stubs; SDA superseded (41 rows deferred); six skill cells on design-gate; PyApp plan-contract hash unchanged since `35ddc63` |
| Design | SharedContracts `design/` is the canonical Configuration **1.0.0 BINDING** (set A; validator 110/110; 23 component contracts; Gallery page; matrix seeded; coverage 100 %); Dashboard, PyApp and AndroidApp anchored to Kit 1.11.0 with synced copies, own pins, emitted `web-css`/`web-ts`, `tokens.py`, `Tokens.kt` (unwired); `design-tokens/` follows set A |
| Kits | Design Template Kit `master` 1.11.0 @ `612e634` (tag `v1.11.0`, pushed; browser legs deferred DV-K1-01); Repo Hygiene Template Kit `main` 0.3.0 @ `d5b9742` (tag `v0.3.0`, pushed) |
| Conductor | `main` at `7610926` (the audits read `2e7adb3`); its orchestrator session busy there; instance 2 untouched and its bindings obsolete by the operator's word |
| Operator items open | owed item 18 (GitHub variables for the design-conformance workflow, before the next push of an anchored client); the veto list in §Q; nothing else gates a step |
| Registers | questions 150+ rows, one open (`Q-B5-13`); deferred validations 38 rows; reuse candidates 264 + the Kit findings added at this boundary |

## 2. Rules

The ten rules of `PROMPT_master-rework-kickoff_2026-10-13.md` §2 bind every session of this program and are not
restated: (1) no test, ever — the need becomes a deferred-validation row; (2) sources read-only; (3) hygiene rule
blocks on every file created or moved, checker before every markdown commit; (4) a prompt never overrides a skill,
package edits follow `plan-batch` and are decisions in `STATE.md`; (5) one writer per repository, worktrees for a
second, gitlinks bumped one commit per step with the ledger flip; (6) analysis as subagents with a fixed schema, at
most four write sessions beside the orchestrator, verdicts verified once on the critical path; (7) operator questions
never block; (8) bytes and shells; (9) models per row; (10) two lines to the operator per step, HANDOVER at every stop.

File rules of this runbook:

1. **Paste protocol.** One fresh session per step. Set the model and effort from the step's model line before launching, then paste the fence unchanged. Launch values go in the orchestrator note, never in the fence. The **Watch** paragraph is for the orchestrator and the operator and is never pasted.
2. **Ids.** `<lane>-<n>` in run order within a lane. An insert after `P` is `P.1`. Parts are letters and the parent becomes `split`. A re-run keeps its id and is noted `-r<k>`. Ids are never renumbered or reused. Sub-lanes carry a fixed letter (`A6a`…`A6g` = superproject, Workspace, PyApp, AndroidApp, Dashboard, Server, SharedContracts; `A9a`…`A9c` and `B6a`…`B6c` = Dashboard, AndroidApp, PyApp). Boundaries are `R-4.<k>`. A gate step's title starts with its gate name.
3. **Fill rule.** Status and Decision in §L take what the step produced: the short SHA and the D-id, never a planned value. A block names an earlier step's outcome by pointer.
4. **Flip rule.** No lane edits this file or the registers (exceptions: `C1-2` and `C1-3` write §H). Every step's final message names its §L row, the commit its gitlink takes (for a submodule step) and its proposed register rows (`Q-…`, `DV-…`); the orchestrator writes one superproject commit per step carrying the gitlink where there is one, the flip and those rows, at the boundary or as soon as the step reports. A step the orchestrator runs with its own hands flips its row in the commit of its output.
5. **Sync rule.** One home branch (§0). No other branch or worktree edits this file. A lane reads it by absolute path.
6. **Questions and waits.** A step with `waits Q-…` is skipped until the register records the answer verbatim. A step written "if Q-… (a)" is `retired` by any other answer. An answer outside the options is recorded verbatim with the step the orchestrator inserts. No session asks through a blocking question tool; when the operator is present in the orchestrator's chat, the orchestrator may ask there in text and keep working (Q-A5-04). A lane that meets an unsettled choice proposes a `Q-<lane>-<nn>` row in its report and continues with everything independent of it. A step may carry a partial wait (one named item waits, the rest proceeds) when its block says so.
7. **Launch.** Routes: `session (headless)` — `claude -p` from the step's cwd with `--model` (`claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`), `--effort` and `--permission-mode`, all in the orchestrator note; `session (paste)` — interactive; `subagent` — spawned by the orchestrator, worktree-isolated when it writes; `procedure` — the orchestrator's hands; `gate` — an operator decision recorded; `operator` — the operator session (§O); `plan` — a `/plan-batch` act with validation cells untouched; `check` — a headless session whose only writes are its evidence file and its INDEX line, launched like `session (headless)`. `batch` is not a route in Phases A or B. In a headless session subagents run in the foreground.
8. **Boundaries.** Every wave ends in an `R-4.<k>` procedure step that runs §3a's ritual. A worktree merges only there.
9. **Size and close.** Past about 900 lines the largest lane moves to a pointed lane file (`B6` is pointed from the start). At `R-5` §L is complete, §0 gains "Closed", the `rework/INDEX.md` line turns `history`, §1 is final.

## 2a. Model · reasoning ladder

| Shape | Model · reasoning | Reason |
|---|---|---|
| orchestrator | Fable 5.1 · high; xhigh for `R-3` | one Fable session at a time; the runbook is where a wrong judgment costs weeks |
| read-only analysis | Opus 5.5 · high | breadth with a written schema |
| mechanical census, byte copies, static checks | Sonnet 5.5 · high | fixed method, verifiable output |
| execution (instructions, hygiene, packages, anchoring, harness) | Opus 5.5 · high | bounded, recorded work with many cross-references |
| IA, mockups, design decisions, the design evidence pack | Opus 5.5 · xhigh | a wrong design costs weeks |
| operator sessions | Opus 5.5 · high | plain words, verbatim record |

Substitution: if Fable 5.1 is unavailable, Opus 5.5 · xhigh plus one fresh-context adversarial review. Every Sonnet subagent is Sonnet 5.5. Never Haiku for a session or a subagent.

## 3. Lanes and step map

### 3.0 Row shape (every step)

| Field | Content |
|---|---|
| id | `<lane>-<n>` (§2 rule 2) |
| title | what the step produces |
| model · reasoning | from §2a |
| route | §2 rule 7 vocabulary |
| where (cwd · branch) | the repository and branch the step writes; `C:\Programmierung\SW_Development_wt\<repo>-<lane>` on `rework/<lane>` when §3a gives it a worktree; worktrees only for steps that neither read nor check sibling repositories (Q-A8-01) |
| precondition | steps done (step ids of §3.2 or `R-n` rows of §L); events — `event:R-3-committed`, `event:wave-<k>-merged`, `event:Q-…-answered`, `event:G-<client>-<n>` (a GUI gate recorded), `event:Kit-session-done` (owed item 12) |
| writes | the files and repositories the step changes |
| waits | `Q-…` ids, or — |
| block | `§3.<n> <id>` · `pointed: <file> §<n>` · `procedure: §3a boundary` · `none (operator)` |

### 3.1 Lanes

| Lane | What | Repositories | Sub-lanes |
|---|---|---|---|
| `A1`…`A9` | Phase A, read-only analysis — done at `R-1` (`b5daba2`); seventeen audits under `rework/` | reads SOURCE-*, writes `rework/` only | `A6a`…`A6g`, `A9a`…`A9c` |
| `B7` | harness port: static guards (package newline guard, parser-provenance census, multi-root mirror parity), the Codex freeze guard (block-aware `AGENTS.md`), scratch and harness docs; never the Conductor's closeout (Q-A2-01) | superproject; PyApp, Server (`.claude` scratch-gate) | — |
| `B2` | `CLAUDE.md`/`AGENTS.md` reconciliation from `A3`'s blueprint: the superproject first, then Dashboard, AndroidApp, PyApp (+ `PyApp/.claude/CLAUDE.md`), then Server, SharedContracts, Workspace | all seven | — |
| `B1` | skills and agents sync after the freeze: the superproject `.claude/` (plan-batch 1.5.1-pl, run-batch §7 rule, agents verbatim, settings, `.agents/README.md` rewritten), then the six mirrors incl. the PlantLibrary-only skills the rows name, parity green; the Conductor's `OP-RB` copy as Q-A5-01 decides; the runbook skill stays record-only | all seven | — |
| `B3` | hygiene: M-8 closing pass, graphify leftovers and the backlog register, Workspace archive and restated exempt-tree notes, M-9 hold releases in five suites, stale scripts, and (after the hand-back) the archived sequencers as Q-G-05 decides | all seven | — |
| `B4` | batch packages: parser-honest edits (range tokens, plan order, out-of-band markers), `DRIVER_SCRIPT.md` to pointer stubs, SDA superseded, decision lines (1.5.1 adopted, model tiers, mechanical readings, validation cells pointed at the deferred register), `CONTEXT_INDEX.md` traceability, the static bind proof | the six suites (seven packages) | — |
| `B5` | Design Configuration: the design-gate evidence pack, the canonical Configuration in SharedContracts `design/` (DRAFT), the gate `G-DS` (BINDING 1.0.0), the anchoring of Dashboard, PyApp and AndroidApp with their stacks, design-adoption retired as Q-G-07 decides, readiness rows 1–7 | SharedContracts, Dashboard, PyApp, AndroidApp | — |
| `B6` | GUI rework per client under methodology 4.1.0 (pointed file): workspace, census, contracts, gap map, forward surface, IA and mockups, mockup audit, change classification, plan-batch, implementation with mechanical checks only; Dashboard → PyApp → AndroidApp (Q-G-08) | Dashboard, PyApp, AndroidApp; SharedContracts (contracts, gallery pages) | `B6a` Dashboard, `B6b` AndroidApp, `B6c` PyApp |
| `B8` | Conductor onboarding alignment: bindings re-verified statically, §L corrections, §N notes discharged, step 8 superseded by proposal A, the GC-1132 operator review | superproject (`onboarding/`), PyApp | — |
| `C1` | hand-back: deferred validations planned by `plan-batch`, the hand-back section (H.1–H.7) replacing the sequencers and `SUITE_HANDOFFS.md`'s table as Q-G-05/Q-A7-07 decide, the resume blocks per suite, the HANDOVER | superproject, the suites | — |

### 3.2 Step map

Route and block vocabulary per §3.0. `super` = `C:\Programmierung\SW_Development` on `master`; `<Suite>` = `C:\Programmierung\SW_Development\PlantLibrary_<Suite>` on `main`, in place unless a worktree path is given.

| Step | Title | Model · reasoning | Route | Where (cwd · branch) | Precondition | Writes | Waits | Block |
|---|---|---|---|---|---|---|---|---|
| `B7-1` | static guards and the multi-root parity checker | Opus 5.5 · high | session (headless) | super | `R-3` | `scripts/harness/*`, `scripts/harness/README.md`, `rework/EVIDENCE_…` | — | §3.3 `B7-1` |
| `B5-1` | design-gate evidence pack | Opus 5.5 · xhigh | session (headless) | super | `R-3` | `rework/EVIDENCE_design-gate-pack_<date>.md` | — | §3.7 `B5-1` |
| `B3-1` | M-8 closing pass over seven repositories (the Kit-side item owed) | Opus 5.5 · high | session (headless) | super | `R-3` | `repo-hygiene/REGISTER_…`, `AUDIT_…`, `handovers/HANDOVER_…`, hygiene runbook §L | — | §3.5 `B3-1` |
| `B4-1` | parser-honest package edits without a question | Opus 5.5 · high | session (headless) | Server, Workspace, SharedContracts (serial, in place) | `B7-1` | three packages' `BATCH_PLAN.md`/`STATE.md` | — | §3.6 `B4-1` |
| `B8-1` | bindings recorded obsolete; ledger and §N corrections; PyApp `.gitignore` and `graphify-out/` | Opus 5.5 · high | session (headless) | super; PyApp | `B4-1` | `onboarding/…runbook` §L/§N; PyApp `.gitignore` | Q-A2-03 (step-8 line only) | §3.8 `B8-1` |
| `R-4.1` | wave 1 boundary | Fable 5.1 · high | procedure | super | all wave-1 steps done; register re-read | gitlinks, flips, register rows, §O | — | procedure: §3a |
| `B2-1` | superproject `CLAUDE.md` reconciled; `AGENTS.md` untouched until the freeze | Opus 5.5 · high | session (headless) | super | `R-4.1` | `CLAUDE.md` | Q-A3-03 | §3.4 `B2-1` |
| `B2-2` | Dashboard, AndroidApp, PyApp guides reconciled; PyApp `.claude/CLAUDE.md` folded | Opus 5.5 · high | session (headless) | the three suites (serial, in place) | `B2-1` | three `CLAUDE.md`; PyApp `.claude/CLAUDE.md` | Q-A3-05, Q-A6A-04 | §3.4 `B2-2` |
| `B2-3` | Server, SharedContracts, Workspace guides reconciled | Opus 5.5 · high | session (headless) | the three suites (serial, in place) | `B2-1` | three `CLAUDE.md` | — | §3.4 `B2-3` |
| `B7-2` | Codex freeze: block-aware `AGENTS.md` banners and digests, the freeze guard, seven D-entries | Opus 5.5 · high | session (headless) | super, then the six suites (serial, in place) | `B7-1`, `B2-2`, `B2-3` | `scripts/harness/check_harness_parity.py`, seven `AGENTS.md`, seven `hygiene/HYGIENE_DECISIONS.md` | Q-G-09, Q-A3-01 | §3.3 `B7-2` |
| `B1-1` | superproject `.claude/` synced; `.agents/README.md` rewritten; settings | Opus 5.5 · high | session (headless) | super | `B7-2` | `.claude/**`, `.agents/README.md`, `.claude/settings.json` | Q-A1-01, Q-A1-03, Q-A5-01 | §3.3 `B1-1` |
| `B1-2` | six mirrors synced incl. the PlantLibrary-only skills the rows name; parity green | Sonnet 5.5 · high | session (headless) | the six suites (serial, in place) | `B1-1` | each suite's `.claude/**` | Q-A1-04 | §3.3 `B1-2` |
| `B2-1.1` | the superproject Testing block's "Sonnet/Terra worker" sentence reworded to the Conductor's E-03r form (Q-A3-02) | Sonnet 5.5 · high | session (headless) | super | `B1-1` | `CLAUDE.md` lines 10-12 only | — | §3.4 `B2-1.1` |
| `B1-3` | third-party-derived Conductor skills adopted or declined | Opus 5.5 · high | session (headless) | super | `B1-1` | `.claude/skills/*`, `.agents/README.md` | Q-A1-02 | §3.3 `B1-3` |
| `B7-3` | scratch gate, harness docs page, Server ledger file | Opus 5.5 · high | session (headless) | super; PyApp; Server (serial; all six suites if Q-A2-06 (a)) | `B1-2` | `scripts/harness/README.md`, `.agents/README.md`, PyApp/Server `.claude/skills/scratch-gate`, Server package `validation/KNOWN_FAILURES.md`, suite pins | Q-A2-06 | §3.3 `B7-3` |
| `B3-2` | superproject leftovers: graphify, `update_graph.bat`, the unplanned-backlog register from `Todo.md` and `IMPLEMENTATION_PLAN.md` §7 | Opus 5.5 · high | session (headless) | super | `R-4.1` | `rework/REGISTER_unplanned-backlog_<date>.md`, `hygiene/HYGIENE_DECISIONS.md`, root entries | Q-G-05, Q-A6S-03, Q-A6S-04 | §3.5 `B3-2` |
| `B3-3` | Workspace: `archive/` declared (empty but for its README), exempt-tree notes restated | Opus 5.5 · high | session (headless) | Workspace | `R-4.1` | `archive/`, `hygiene/HYGIENE_DECISIONS.md` | Q-A6W-01, Q-A6W-04 | §3.5 `B3-3` |
| `B3-4` | M-9: the five V1 proposal holds released and renamed; Dashboard's two pinned `docs/` holds | Opus 5.5 · high | session (headless) | PyApp, AndroidApp, Dashboard, Server, SharedContracts (serial, in place) | `B3-1` | five `hygiene/HYGIENE_DECISIONS.md`, `proposal/INDEX.md`, citers | Q-A6P-03, Q-A6A-02, Q-A6D-02, Q-A6D-03, Q-A6V-02, Q-A6C-04 | §3.5 `B3-4` |
| `B3-5` | stale `run_next_batch.py` scripts retired; Server docs links fixed | Sonnet 5.5 · high | session (headless) | Dashboard, Server, Workspace (serial, in place) | `B4-2` | three `scripts/run_next_batch.py`, Server `docs/*.md`, READMEs | Q-A6V-04, Q-A6V-05 | §3.5 `B3-5` |
| `B4-2` | out-of-band markers; `DRIVER_SCRIPT.md` to pointer stubs; README run lines | Opus 5.5 · high | session (headless) | the six suites (serial, in place) | `B4-1`, `R-4.1` | seven packages' `BATCH_PLAN.md`, `DRIVER_SCRIPT.md`, `README.md`, `STATE.md` | Q-A7-02, Q-A7-05 | §3.6 `B4-2` |
| `B4-3` | SDA package superseded | Opus 5.5 · high | session (headless) | Workspace | `B4-1` | `System_Design_Architecture/*` | Q-A7-06, Q-G-01 | §3.6 `B4-3` |
| `B4-4` | decision lines: plan-batch 1.5.1 adopted, model tiers, mechanical readings, validation cells pointed, `CONTEXT_INDEX.md` traceability | Opus 5.5 · high | session (headless) | the six suites (serial, in place) | `B1-2`, `B4-2` | seven `STATE.md`, `CONTEXT_INDEX.md`, `SCOPE.md` | Q-A7-01, Q-A7-03, Q-A7-04 | §3.6 `B4-4` |
| `B4-5` | static package proof (main's parser; instance 2 informational) | Sonnet 5.5 · high | check | super | `B4-2`, `B4-3`, `B4-4` | `rework/EVIDENCE_bind-proof_<date>.md` | — | §3.6 `B4-5` |
| `B5-2` | the Configuration in SharedContracts `design/`, DRAFT 0.1.0 | Opus 5.5 · high | session (headless) | SharedContracts | `B5-1`, `B2-3`, `R-4.1` | `design/**`, `CLAUDE.md`, `SCOPE.md`, `hygiene/HYGIENE_DECISIONS.md` | Q-G-01, Q-A4-01, Q-A6C-02 | §3.7 `B5-2` |
| `B5-3` | `G-DS`: the design gate; Configuration 1.0.0 BINDING | operator; Opus 5.5 · high records | gate | SharedContracts | `B5-2` | `design/CONFIGURATION.md`, `DESIGN_VERSION.md`, decisions | Q-A4-02, Q-A9D-02, Q-A4-03, Q-A4-04, Q-A9A-04, Q-A9P-08 | §3.7 `B5-3` |
| `B5-3.1` | component contracts and the generated Gallery page in the Configuration; `.gitattributes` lines (Q-B5-05, Q-B5-07) | Opus 5.5 · high | session (headless) | SharedContracts | `B5-3` | `design/contracts/components/**`, `design/gallery/index.html`, `.gitattributes` | — | §3.7 `B5-3.1` |
| `B5-3.2` | the canonical conformance matrix seeded (23 rows), the Map cells, the remaining attribute lines | Sonnet 5.5 · high | session (headless) | SharedContracts | `B5-3.1`, `B1-2` | `design/conformance/CONFORMANCE_MATRIX.md`, `design/CONFIGURATION.md`, `design/decisions/*`, `.gitattributes` | — | §3.7 `B5-3.2` (the block is the launch message of 2026-10-13; its text is recorded in §H when the step closes) |
| `B5-3.3` | the client mapping files synced back into the canonical Configuration (byte-equality restored) | Sonnet 5.5 · high | session (headless) | SharedContracts | `B5-5`, `B5-6` | `design/stacks/{qt-qss,compose}/mapping.md` | — | §3.7 `B5-3.3` (the block is the launch message of 2026-10-13) |
| `B5-4` | Dashboard anchored (installer, impeccable, `web-css`+`web-ts` emitted, pin) | Opus 5.5 · high | session (headless) | Dashboard | `B5-3`, `B2-2`, `B7-2`, `B1-2` | `design/**`, `scripts/design/**`, `.claude/.codex/.agents/.github` skills, `CLAUDE.md` block, `.gitattributes` | Q-A8-03 | §3.7 `B5-4` |
| `B5-5` | PyApp anchored (installer, `qt-qss` emitted, adapter decision recorded) | Opus 5.5 · high | session (headless) | PyApp | `B5-3`, `B2-2`, `B7-2`, `B1-2` | as `B5-4`; `design/stacks/qt-qss/**` | Q-A9P-01 | §3.7 `B5-5` |
| `B5-6` | AndroidApp anchored (installer, `compose` emitted, placement recorded; compile deferred) | Opus 5.5 · high | session (headless) | AndroidApp | `B5-3`, `B2-2`, `B7-2`, `B1-2` | as `B5-4`; `design/stacks/compose/**` | Q-A9A-01, Q-A4-05 | §3.7 `B5-6` |
| `B5-7` | design-adoption retired; six skill cells repointed to design-gate | Opus 5.5 · high | session (headless) | super; Dashboard, AndroidApp, PyApp, Workspace (serial) | `B5-4`, `B5-5`, `B5-6`, `B1-2` | `.claude/skills/design-adoption/*` (super, Workspace), three `STATE.md`/`TASK_CHECKLIST.md` | Q-G-07 | §3.7 `B5-7` |
| `B5-8` | Conductor readiness rows 1–7 per anchored client | Sonnet 5.5 · high | check | super | `B5-4`, `B5-5`, `B5-6` | `rework/EVIDENCE_design-readiness_<date>.md` | — | §3.7 `B5-8` |
| `B8-2` | §N notes closed by `B4`; step 8 superseded; §L step 6 facts | Opus 5.5 · high | session (headless) | super | `B4-5` | `onboarding/…runbook` §L/§N | Q-A2-03 | §3.8 `B8-2` |
| `K-1` | Design Template Kit session: the emitter and tool gaps `A4`/`B5-1` recorded, on a Kit branch | Opus 5.5 · high | session (headless) | `C:\Programmierung\Design_Template_Kit` on a branch `pl/kit-gaps-2026-10` from `master` | `B5-3` | the Kit only (never TARGET) | — | §3.7 `K-1` |
| `K-2` | Repo Hygiene Template Kit session: K-7 and the pilot lessons as release 0.3.0, on a Kit worktree branch, merged and tagged | Opus 5.5 · high | session (headless) | `C:\Programmierung\Repo_Hygiene_Template_Kit_wt\k7` on `pl/k7-2026-10` from `master` | `R-4.1` | the hygiene kit only (never TARGET) | — | §3.5 `K-2` |
| `B3-8` | all seven repositories re-pinned to kit 0.3.0; the Workspace restructure set released and renamed (M-9) | Opus 5.5 · high | session (headless) | super, then the six suites (serial, in place) | `K-2`, `B3-6` | seven `hygiene/CONSUMED_HYGIENE.md`, `HYGIENE_DECISIONS.md`, `scripts/hygiene/repo_hygiene_check.py`, rule blocks; Workspace `docs/proposals/**`, five suites' `implementation/README.md` | — | §3.5 `B3-8` |
| `B8-3` | GC-1132: the operator's review of `IMPORTABLE_SOURCE_TREES` recorded | operator; Sonnet 5.5 · high records | operator | PyApp; super | `R-4.1` | PyApp `validation/ONBOARDING_harness-port.md`; onboarding §L step 4 | Q-A2-02 | §3.8 `B8-3` |
| `R-4.2` | wave 2 boundary | Fable 5.1 · high | procedure | super | all wave-2 steps done or waiting; register re-read | gitlinks, flips, rows, §1, §O | — | procedure: §3a |
| `B6a-1`…`B6a-8` | Dashboard GUI rework (pointed) | per step | per step | Dashboard; SharedContracts for contracts | `B5-4`, `R-4.2` | see the pointed file | see the pointed file | pointed: `PROMPTS_gui-rework-runbook_2026-10-13.md` §3 |
| `B6c-1`…`B6c-5` | PyApp GUI rework, planning (pointed) | per step | per step | PyApp | `B5-5`, `R-4.2` | pointed | pointed | pointed: same file §4 |
| `B6c-6`…`B6c-8` | PyApp GUI rework, IA to implementation (pointed) | per step | per step | PyApp; SharedContracts | `B6c-5`, `B6a-6` (SharedContracts serialized) | pointed | pointed | pointed: same file §4 |
| `B6b-1`…`B6b-5` | AndroidApp GUI rework, planning (pointed) | per step | per step | AndroidApp | `B5-6`, `R-4.2` | pointed | pointed | pointed: same file §5 |
| `B6b-6`…`B6b-8` | AndroidApp GUI rework, IA to implementation (pointed; implementation waits the Kit session) | per step | per step | AndroidApp; SharedContracts | `B6b-5`, `B6c-6` | pointed | Q-A4-05 | pointed: same file §5 |
| `R-4.3` | wave 3 boundary | Fable 5.1 · high | procedure | super | all `B6` steps done or waiting | gitlinks, flips, rows, §1, §O | — | procedure: §3a |
| `C1-1` | deferred validations planned, one `/plan-batch` act per package with `DV-…` rows | Opus 5.5 · high | plan | each suite (serial, in place) | `R-4.3` | packages' rows and `STATE.md` | — | §3.9 `C1-1` |
| `C1-2` | the hand-back section H.1–H.7; `SUITE_HANDOFFS.md` reshaped; the backlog register pointed | Opus 5.5 · high | session (paste) | super; Workspace | `C1-1` | this file §H; Workspace V1 `SUITE_HANDOFFS.md` | Q-G-05, Q-A7-07 | §3.9 `C1-2` |
| `B3-6` | the stale sequencers archived (superproject, Workspace) | Opus 5.5 · high | session (headless) | super; Workspace | `C1-2` | `archive/**`, two `hygiene/HYGIENE_DECISIONS.md`, root allowlist | Q-G-05, Q-A6S-01, Q-A6S-05 | §3.5 `B3-6` |
| `B3-7` | residual prose sweep: lines that still name the retired scripts, the driver or the graphify sanction | Sonnet 5.5 · high | session (headless) | AndroidApp, Server, Workspace, PyApp (serial, in place) | `B3-6` | AndroidApp `README.md`; Server `README.md`, `docs/SV-DOMAIN-01_domain_port_notes.md`, `docs/SV-B07_dashboard_endpoint_coverage_report.md`; Workspace `docs/local_development.md`, `implementation/README.md`, V1 `DRIVER_SCRIPT.md`; PyApp `tests/test_repo_hygiene.py` allowlist entry, package `STATE.md` line | — | §3.5 `B3-7` |
| `C1-3` | resume blocks per suite | Opus 5.5 · high | session (paste) | super | `C1-2` | this file §H | — | §3.9 `C1-3` |
| `C1-4` | the hand-back HANDOVER | Fable 5.1 · high | procedure | super | `C1-3`, `B3-6` | `handovers/HANDOVER_master-rework-hand-back_<date>.md`, INDEX | — | §3.9 `C1-4` |
| `R-4.4` | wave 4 boundary | Fable 5.1 · high | procedure | super | `C1-4` | gitlinks, flips, push list | — | procedure: §3a |
| `R-5` | close | Fable 5.1 · high | procedure | super | `R-4.4` | §0 Closed, §1, §L, INDEX `history`, final HANDOVER | — | §3.9 `R-5` |

Dependencies not in the table: `B7-2` and `B1-2` precede the first edit of any `.claude/skills/**`, `.claude/agents/**` or `.claude/settings.json` file by another lane (`CLAUDE.md` files are `B2`'s and precede `B7-2`); `B5-2`'s writes into SharedContracts serialize with `B4-1` (SharedContracts) and `B3-4` there; the three `B6` sub-lanes serialize on SharedContracts at their IA and mockup steps.

### 3.3 Lane B7 — harness port, and lane B1 — skills and agents

#### `B7-1` — static guards and the multi-root parity checker

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master` (in place) · **Precondition:** `R-3` · **Writes:** superproject `scripts/harness/*`, `scripts/harness/README.md`, `rework/EVIDENCE_harness-guards_<date>.md` · **Waits:** —

```text
B7-1 — static guards and the multi-root parity checker
Deliver the four static guards the hygiene kit does not cover, as stdlib-only scripts under the superproject's scripts/harness/, each printing one verdict line and exiting 0/1/2 like the kit's checker.
Context: step B7-1 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3, lane B7), read by that absolute path and never edited; the program's rules are §2 of C:\Programmierung\SW_Development\rework\PROMPT_master-rework-kickoff_2026-10-13.md; the register rows it executes: RC-A2-08, RC-A2-09, RC-A2-13, RC-A1-21; the findings: AUDIT_harnesses-and-scripts_2026-10-13.md §7.2 and §7.5, AUDIT_skills-and-agents_2026-10-13.md §7.7 items 1, 2, 5, 8, AUDIT_batch-packages_2026-10-13.md §0 item "the checker measures main's parser".
Where: cwd C:\Programmierung\SW_Development on branch master. This session writes only the superproject; it never runs a git write command in, and never writes, any submodule.
Scope: (1) scripts/harness/check_package_newlines.py — one line-ending style per contract file (README.md, SCOPE.md, CONTEXT_INDEX.md, BATCH_PLAN.md, TASK_CHECKLIST.md, TASK_CONTEXT.md, STATE.md) in every git-tracked folder holding a BATCH_PLAN.md across the superproject and the six submodule folders (git ls-files per repository; .tmp/ and untracked files never scanned; frozen MVP, Archive_PreMVP and archive packages listed, not counted), read as bytes; (2) scripts/harness/check_batch_packages.py — print the parser's provenance (module file path and the git commit of its checkout when readable), take --parser-src <path> to point at instance 2's src, never write bytecode, read git facts in the Conductor checkout with --no-optional-locks only, exit 1 only for live packages (the four frozen Workspace packages are listed, not counted); (3) scripts/harness/check_harness_parity.py — iterate the superproject and each present submodule folder, compare each suite's shared skill folders and agents against the superproject's with CRLF normalized to LF, keep today's .claude-vs-.codex compare behind --with-codex-compare (default on until B7-2 switches it), extend the planted-drift self-check (a static mode of the checker over temporary copies, not a test) to plant one drift per new check, add the run-batch commit-contract strings check (AUDIT_skills-and-agents §7.7 item 5); Q-A2-04 (a) is assumed here — a (b) answer retires the suite compare, not the script; (4) scripts/harness/README.md — the inventory and the "which check after which edit" table (the Conductor's docs/harness/README.md rules, adapted). Not here: the Codex freeze (B7-2), the docs link checker (B7-3), any closeout, any change under .claude/ or .codex/.
Read first: AUDIT_harnesses-and-scripts_2026-10-13.md §7.2 and §7.5; AUDIT_skills-and-agents_2026-10-13.md §7.7; the current three scripts under scripts/harness/; C:\Programmierung\Orchestrator_System\scripts\harness\check_harness_parity.py (read-only, lines 1-60 and 213-272 for the digest method) and C:\Programmierung\Orchestrator_System\tests\test_repo_hygiene.py lines 216-275 (the newline guard's rule); C:\Programmierung\Orchestrator_System\docs\harness\README.md (the page rules).
Write: the three scripts, the README, and rework/EVIDENCE_harness-guards_<date>.md holding each script's verdict line over the seven repositories at this commit and the self-test output.
Constraints: sources read-only; no test of any kind, no app launch, no build — the scripts are run once each as static checks and their output is the evidence; the parser-backed census runs with bytecode writing disabled; line endings as found; no edit to any package, skill, agent or instruction file; subagents in the foreground; no push; rework/INDEX.md gets the evidence file's line in the same commit; the hygiene checker's verdict before the commit shows zero violations.
Questions: a choice this block does not settle goes into the final message as a proposed Q-B7-<nn> row; continue with everything independent of it; never ask through a blocking question tool.
If the context runs short: commit what is complete, mark the rest "not done" in the evidence file, and stop; the same block is restarted as B7-1-r2.
Done when: the four deliverables exist; each script prints its verdict over all seven repositories (the parity checker green today, the newline guard reporting 0 mixed contract files on the seven live packages with the mixed-file list of AUDIT_git-structure_2026-10-13.md §7.1 quoted in the evidence as the do-not-fix set, the census 0 errors on the seven live packages with the parser path printed); the planted-drift self-check passes; one commit on master; the final message gives the §L row and the proposed register rows.
Commit line: rework: B7-1 - static guards and multi-root parity checker - 3 scripts, 1 README, 1 evidence
```

*Orchestrator note:* base `554a591` or later; `claude -p --model claude-opus-5-5 --effort high --permission-mode auto`; the superproject is this step's only writer until it ends; §L row `B7-1`.
**Watch:** a script that imports `conductor` without printing where from; a newline guard that "fixes" a file; a parity compare done on working-tree bytes without LF normalization (mirrors of `run-batch/SKILL.md` are mixed in every repository); any runner name in the README (the program never names one).

#### `B7-2` — Codex freeze: block-aware `AGENTS.md` banners, digests, the freeze guard

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master`, then each `PlantLibrary_<Suite>` on `main` (serial, in place) · **Precondition:** `B7-1`, `B2-2`, `B2-3` · **Writes:** `scripts/harness/check_harness_parity.py`, seven `AGENTS.md` (banner line only), seven `hygiene/HYGIENE_DECISIONS.md` · **Waits:** Q-G-09, Q-A3-01

```text
B7-2 — Codex freeze across seven repositories
Freeze .codex/** and AGENTS.md (outside its marked blocks) at this commit in each repository, as the Conductor did (D-2026-10-02-23), with the guard that keeps the frozen bytes checkable.
Context: step B7-2 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3, lane B7); the program's rules are §2 of the kickoff prompt; the answers this step rests on: Q-G-09 and Q-A3-01 as recorded in §Q; the register rows: RC-A1-18, RC-A1-19, RC-A1-20, RC-A3-20, RC-A3-21; the shape: AUDIT_skills-and-agents_2026-10-13.md §7.6 items 1-5 and §7.7 item 3.
Where: cwd C:\Programmierung\SW_Development on master for the superproject half, then each submodule folder on main, one repository at a time; each repository gets its own commit; nothing in a worktree.
Scope: per repository (1) one hygiene decision entry (next free D-id by grep) recording the freeze: what is frozen (.codex/** except the Kit folders under .codex/skills/ once B5 installs them, settings.local.json, __pycache__; AGENTS.md outside the repo-hygiene and design-kit marker blocks), the freeze commit defined as the commit immediately preceding this entry's commit in that repository (its tree holds the pre-banner AGENTS.md and the .codex/** bytes; this avoids a hash fixed point), the unfreeze recipe; (2) the one-line banner inserted directly under the file's first heading line (as line 1 when the file opens with a heading-less block), in the Conductor's form, naming the entry; (3) in the superproject only: scripts/harness/check_harness_parity.py gains the freeze check — digests of CRLF-normalized bytes taken from git show <freeze commit>:<path> per repository (the freeze commit as defined above, so the digest table and the superproject's own banner can land in one commit), never from the working tree; AGENTS.md digested with each marked block's interior removed; the .claude-vs-.codex compare switched off by default; a FROZEN_AT table per repository; a bridge-coverage check that every .claude/skills/* folder in the superproject is either a frozen bridge row or a Claude-only row in .agents/README.md (the README is rewritten at B1-1; until then the check reports "README pending" without failing). Not here: any edit under .claude/ or .codex/; the .agents/README.md rewrite (B1-1).
Read first: §Q rows Q-G-09 and Q-A3-01 (the operator's words); AUDIT_skills-and-agents_2026-10-13.md §7.6, §7.7; AUDIT_instructions-reconciliation-blueprint_2026-10-13.md §7.4; C:\Programmierung\Orchestrator_System\.agents\README.md lines 1-26 and scripts\harness\check_harness_parity.py lines 213-272 (read-only); each repository's hygiene/HYGIENE_DECISIONS.md tail (the entry shape and the next free id).
Write: the seven decision entries, the seven banner lines, the one checker; nothing else.
Constraints: sources read-only; no test, no build; AGENTS.md is written back with its own line endings and no byte outside the banner line changes (compare git hash-object before and after with the banner removed); the hygiene block parity between CLAUDE.md and AGENTS.md stays green (the banner sits outside the block); each repository's hygiene verdict before its commit shows zero violations; one commit per repository; subagents in the foreground; no push.
Questions: a choice this block does not settle goes into the final message as a proposed Q-B7-<nn> row; continue with everything independent of it.
If the context runs short: commit the repositories that are complete, list the rest as "not done", and stop; restart as B7-2-r2 for the remaining repositories only.
Done when: seven commits exist; the parity checker run from the superproject reports the freeze green in all seven and the old compare off; the final message lists per repository the commit and the D-id for the orchestrator's gitlink-and-flip commits.
Commit line: rework: B7-2 - codex frozen; AGENTS.md banner; D-<date>-<nn>
```

*Orchestrator note:* launch after `B2-2`/`B2-3` landed and their gitlinks are bumped; free D-id candidates per repository are listed in the note at launch; the superproject line for each suite: `rework: B7-2 - bump <repo> gitlink; ledger B7-2`.
**Watch:** a whole-file `AGENTS.md` digest (the Conductor's shape — it let the design block drift, F-A1-12); a digest taken from the working tree; a banner inside a marker block; a freeze entry that names a commit SHA inside the fence of a later step.

#### `B7-3` — scratch gate, harness docs page, Server ledger file

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master`; then `PlantLibrary_PyApp`, `PlantLibrary_Server` on `main` (serial, in place) · **Precondition:** `B1-2` · **Writes:** superproject `scripts/harness/README.md`, `.agents/README.md` (one row); PyApp and Server `.claude/skills/scratch-gate/*`; Server `implementation/System_V1_Implementation/validation/KNOWN_FAILURES.md`; if Q-A2-06 (a): each suite's pin and a decision entry · **Waits:** Q-A2-06

```text
B7-3 — scratch gate and harness docs
Deliver the scratch-gate procedure where a reclaim script exists, the harness docs page rules, and the empty Server ledger the harness contract requires.
Context: step B7-3 of the master rework runbook (§3, lane B7); rules: kickoff §2; the answer it rests on: Q-A2-06 (§Q); the register rows: RC-A1-13, RC-A2-18, RC-A2-24, RC-A7 rows naming KNOWN_FAILURES.md; AUDIT_harnesses-and-scripts_2026-10-13.md §7.3 and §7.4; AUDIT_batch-packages_2026-10-13.md §7.2 (Server validation/).
Where: superproject first, then PyApp, then Server, each in place on its branch, one commit each.
Scope: (1) superproject scripts/harness/README.md: the page rules of the Conductor's docs/harness/README.md adapted (inventory, one page per script, which check after which edit), the scratch layout per suite as the suite CLAUDE.md files state it, and the kit's scratch module state per Q-A2-06; (2) PyApp and Server: the Conductor's scratch-gate skill adapted (reclaim_scratch.py path, the .tmp layout of the 7ad02b1 port, no sweep and no lock until a re-port), installed under .claude/skills/scratch-gate/ only (Codex is frozen); (3) Server implementation/System_V1_Implementation/validation/KNOWN_FAILURES.md created empty with the header PyApp's implementation/System_V1_Implementation/validation/KNOWN_FAILURES.md carries; (4) the scratch-gate row added to the superproject's .agents/README.md Claude-only table; (5) if Q-A2-06 (a): per suite the kit installer re-run with the scratch module (its INSTALL.md procedure, --force re-pin) and the decision entry it requires, .gitignore untouched where .tmp/ is already ignored. Not here: any closeout or re-port (Q-A2-01); the living-documentation standard (Q-A2-05 is held); docs link checking.
Read first: AUDIT_harnesses-and-scripts_2026-10-13.md §7.3, §7.4; C:\Programmierung\Orchestrator_System\.claude\skills\scratch-gate\SKILL.md and docs\harness\README.md (read-only); PlantLibrary_PyApp/scripts/harness/reclaim_scratch.py header; PlantLibrary_PyApp/implementation/System_V1_Implementation/validation/KNOWN_FAILURES.md; the two suites' CLAUDE.md scratch sections; the kit's installer/INSTALL.md if (5) applies.
Write: the README, two skill folders, one ledger file.
Constraints: sources read-only; no test, no build, no reclaim run; .codex untouched; line endings as found; a suite's hygiene verdict before its commit shows zero violations; subagents in the foreground; no push.
Questions: proposed Q-B7-<nn> rows in the final message; continue with everything independent.
If the context runs short: commit the complete repositories, list the rest, stop; restart as B7-3-r2.
Done when: the three repositories each carry one commit; the parity checker stays green (scratch-gate is a Claude-only row, listed in .agents/README.md); the final message names the commits and the §L row.
Commit line: rework: B7-3 - scratch gate, harness docs, Server ledger
```

*Orchestrator note:* PyApp and Server lines: `rework: B7-3 - bump <repo> gitlink; ledger B7-3`.
**Watch:** a scratch-gate copy that names the Conductor's `src/conductor/scratch_sweep.py`; a ledger with an invented row; a README that names a runner.

#### `B1-1` — superproject `.claude/` synced; `.agents/README.md` rewritten; settings

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master` (in place) · **Precondition:** `B7-2` · **Writes:** `.claude/skills/**`, `.claude/agents/*.md`, `.claude/settings.json`, `.agents/README.md` · **Waits:** Q-G-09, Q-A1-01, Q-A1-03, Q-A5-01

```text
B1-1 — the superproject .claude/ synced to the Conductor's current skills and agents
Bring the superproject's skills and agents to the verdicts of the reuse register, nothing copied blindly, with the bridge README that records what is frozen, what is Claude-only and why.
Context: step B1-1 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3, lane B1); rules: kickoff §2; the answers it rests on: Q-G-09, Q-A1-01, Q-A1-03, Q-A5-01 (§Q); the register rows: RC-A1-01 … RC-A1-09, RC-A1-12, RC-A1-14, RC-A1-20, RC-A1-21, RC-A1-24, RC-A5-19; the evidence: AUDIT_skills-and-agents_2026-10-13.md §7.1-§7.5.
Where: cwd C:\Programmierung\SW_Development on master; this session writes only the superproject and only under .claude/, .agents/README.md and .claude/settings.json.
Scope: (1) plan-batch → 1.5.1-pl: the Conductor's 1.5.1 text with its §7 closeout-budget item replaced by the 1.4.0 cap item and a version line saying so (§7.3 of the audit); (2) run-batch: the Conductor's §7 newline rule adopted verbatim; §6 per Q-A1-01 (its (a) keeps this repository's §6 text, since no suite has the one-command closeout); (3) real-stack-testing item 7, test-driven-development, systematic-debugging adapted per RC-A1-03, RC-A1-08, RC-A1-09 (no runner taught in Kotlin/TS suites; no "ask the human" for a headless worker); (4) the three shared agents adopted verbatim from the Conductor (batch-closeout-reviewer on Opus, the "before you report" and "judge against contract" paragraphs, the validator's foreground rule and timeout env) — in the same commit as (1) and (3), because the agents preload those skills; (5) harness-upkeep adapted to this repository's checks (B7-1's scripts); instance-sync not taken; (6) .claude/settings.json: the tracked deny list with PowerShell twins and the timeout env per Q-A1-03; (7) .agents/README.md rewritten as PlantLibrary's bridge file: freeze notice and unfreeze recipe, the bridge table with frozen statuses, the agent roster with models, the Claude-only table with source, pin and licence; the runbook skill recorded as not installed (Q-A5-01). Not here: the six mirrors (B1-2); the third-party-derived skills (B1-3); design skills (B5); anything under .codex/.
Read first: AUDIT_skills-and-agents_2026-10-13.md §7.1-§7.5; the §Q answers; the Conductor's .claude/skills/{plan-batch,run-batch,real-stack-testing,test-driven-development,systematic-debugging,harness-upkeep}/SKILL.md, .claude/agents/*.md, .claude/settings.json and .agents/README.md (read-only, absolute paths); this repository's current copies.
Write: the listed files only.
Constraints: sources read-only; no test, no build; every skill file written back as bytes with its own line endings (run-batch/SKILL.md is mixed); the parity checker's freeze and bridge-coverage checks stay green (freeze intact, bridge coverage complete) — its suite mirror compare is expected red until B1-2 lands and is quoted as such; no edit to any suite; subagents in the foreground; no push.
Questions: proposed Q-B1-<nn> rows in the final message; continue with everything independent.
If the context runs short: commit the complete items, list the rest as not done, stop; restart as B1-1-r2.
Done when: the superproject carries one commit; the freeze and bridge checks are green and the mirror compare's red list equals the files this step changed; .agents/README.md lists every .claude/skills/* folder; the final message names the commit and the §L row.
Commit line: rework: B1-1 - superproject skills and agents synced - plan-batch 1.5.1-pl, 3 agents, bridge README
```

*Orchestrator note:* `--permission-mode auto` may deny `.claude/**` edits to a headless session (F-A5-15); if the launch is refused, route this step as `session (paste)` in the orchestrator's own terminal with the same block.
**Watch:** plan-batch's `--predict` item adopted without the command (every audit would then fail); a run-batch §6 replaced wholesale under (a); an agent file with a Conductor path; a settings file that allows `cat .env`.

#### `B1-2` — six mirrors synced incl. the PlantLibrary-only skills the rows name; parity green

**Model · reasoning:** Sonnet 5.5 · high · **Route:** session (headless) · **Where:** each `C:\Programmierung\SW_Development\PlantLibrary_<Suite>` on `main` (serial, in place) · **Precondition:** `B1-1` · **Writes:** each suite's `.claude/skills/**`, `.claude/agents/*.md` · **Waits:** Q-A1-04

```text
B1-2 — the six suite mirrors synced
Copy the superproject's five shared skill folders and three agents into every suite as bytes, add the PlantLibrary-only skills each suite's rows name, and leave the parity checker green.
Context: step B1-2 of the master rework runbook (§3, lane B1); rules: kickoff §2; the answers: Q-A1-04 (§Q); the register rows: RC-A1-22, RC-A1-23 and the per-suite rows of AUDIT_skills-and-agents_2026-10-13.md §7.1 (android-validation → AndroidApp; verify-stack → PyApp, AndroidApp, Dashboard; sync-contracts → Server, SharedContracts, PyApp; webapp-testing → Dashboard; gui-validation full mirror → PyApp, replacing its pointer; verify-stack's stale Workspace copy refreshed); AUDIT_batch-packages_2026-10-13.md §0 item 6 (38 rows naming absent skills).
Where: one suite at a time, in place on main, one commit per suite; the superproject is read, never written.
Scope: per suite, the shared set as byte copies of the superproject's finished files; the PlantLibrary-only skills listed above as byte copies; .codex untouched (frozen); the suite's .agents/README.md is not created (the superproject's covers all seven). Not here: any edit to a skill's text; design skills; impeccable.
Read first: AUDIT_skills-and-agents_2026-10-13.md §7.1 and §7.6 item 4; the superproject's scripts/harness/check_harness_parity.py usage.
Write: the mirror files only.
Constraints: byte copies (no text-mode read or write; compare git hash-object of source and copy); sources read-only; no test, no build; each suite's hygiene verdict before its commit shows zero violations; subagents in the foreground; no push.
Questions: proposed Q-B1-<nn> rows; continue with everything independent.
If the context runs short: commit the complete suites, list the rest, stop; restart as B1-2-r2.
Done when: six commits; the parity checker from the superproject reports every mirror equal and the freeze green; the final message lists the six commits.
Commit line: rework: B1-2 - skill and agent mirrors synced - <n> folders, 3 agents
```

*Orchestrator note:* six superproject lines `rework: B1-2 - bump <repo> gitlink; ledger B1-2`, in one boundary.
**Watch:** a copy made through a text tool (CRLF churn turns parity red); PyApp's `.agents/skills/gui-validation` pointer left beside the full mirror without a README row.

#### `B1-3` — third-party-derived Conductor skills adopted or declined

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master` (in place) · **Precondition:** `B1-1` · **Writes:** `.claude/skills/{code-quality-review,security-audit,pathfinder,dependency-audit}/**`, `.agents/README.md` · **Waits:** Q-A1-02

```text
B1-3 — the four third-party-derived skills
Install into the superproject only those of code-quality-review, security-audit, pathfinder and dependency-audit that Q-A1-02 admits, with their licences, their Conductor paths replaced by this repository's, and a Claude-only row each.
Context: step B1-3 of the master rework runbook (§3, lane B1); rules: kickoff §2; the answer: Q-A1-02 (§Q); the register rows: RC-A1-15, RC-A1-16; AUDIT_skills-and-agents_2026-10-13.md §7.1 (the four rows).
Where: cwd C:\Programmierung\SW_Development on master; superproject only.
Scope: per admitted skill, the folder copied with LICENSE/NOTICE, the deliverable path and read-exclusions parameterised to this repository, the bridge README row. A declined skill gets one README line saying why. Not here: suites; any skill run.
Read first: the §Q answer; the four Conductor skill folders (read-only).
Write: the admitted folders and the README.
Constraints: sources read-only; no test; no token or host configured; parity checker green; no push.
Questions: proposed Q-B1-<nn> rows; continue.
If the context runs short: commit the complete skills, list the rest, stop; restart as B1-3-r2.
Done when: one commit; every admitted skill resolves its paths inside this repository; the final message names the commit.
Commit line: rework: B1-3 - third-party skills - <n> installed, <m> declined
```

**Watch:** a dependency-audit copy that keeps the GitHub token route; a security-audit that writes into `implementation/Conductor_V2/planning/`.

### 3.4 Lane B2 — `CLAUDE.md` and `AGENTS.md` reconciliation

#### `B2-1` — superproject `CLAUDE.md` reconciled

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master` (in place) · **Precondition:** `R-4.1` · **Writes:** `CLAUDE.md` · **Waits:** Q-A3-03

```text
B2-1 — the superproject CLAUDE.md
Give the superproject the instruction surface the Conductor's CLAUDE.md gives its repository, parameterised for seven repositories, with the operator's Testing block and the installer-owned hygiene block untouched.
Context: step B2-1 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3, lane B2); rules: kickoff §2; the answers it rests on: Q-A3-03 (§Q), and for single sentences left marked: Q-A3-02, Q-A3-04, Q-A3-07, Q-G-03, Q-A3-06; the register rows: RC-A3-03 … RC-A3-11, RC-A3-13, RC-A3-17; the blueprint: AUDIT_instructions-reconciliation-blueprint_2026-10-13.md §7.1, §7.2 (file 1) and §7.2.1.
Where: cwd C:\Programmierung\SW_Development on master; this session writes CLAUDE.md only; AGENTS.md is not touched (its freeze lands at B7-2).
Scope: the title and purpose above the Testing block; Authority; Repository layout; Workflow; Engineering standards (the generic core, no product invariants); the ten session rules of §7.2.1 with rule 1's model sentence, rule 4 and rule 5 written as the blueprint drafts them and marked "[waits Q-…]" where §Q has no answer yet; the Testing block stays byte-identical (its lines 10-12 change only in a later B2 step once Q-A3-02 is answered); the Claude subagent roster from the decided agent set (the three agents, Opus for the closeout reviewer, Sonnet for the other two; pointer to .agents/README.md); Living documentation held (Q-A3-06). Not here: AGENTS.md; suites; the hygiene block's bytes; any skill.
Read first: the blueprint sections named; C:\Programmierung\Orchestrator_System\CLAUDE.md (read-only, lines 1-60, 101-217, 234-258); this repository's CLAUDE.md and hygiene/CONSUMED_HYGIENE.md.
Write: CLAUDE.md.
Constraints: sources read-only; no test; written back CRLF as found, the hygiene block byte-identical (compare its marker-to-marker bytes before and after); the hygiene checker's block parity stays green; no runner named anywhere in the file; subagents in the foreground; no push.
Questions: proposed Q-B2-<nn> rows; continue with everything independent.
If the context runs short: commit what is complete, mark the rest in the file as "[B2-1-r2]" placeholders, stop; restart as B2-1-r2.
Done when: one commit; the file reads top to bottom as one instruction surface; the final message names the commit and lists the sentences still marked.
Commit line: rework: B2-1 - superproject CLAUDE.md reconciled - <n> sections added
```

**Watch:** the roster written before the agent set is decided (it is decided by the register: RC-A1-04..06); a session rule that restates the Conductor's instance-1 facts; an edit inside the markers.

#### `B2-1.1` — the Testing block's worker sentence (inserted 2026-10-13, Q-B2-01 (a))

**Model · reasoning:** Sonnet 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master` (in place) · **Precondition:** `B1-1` · **Writes:** `CLAUDE.md` (the one sentence) · **Waits:** —

```text
B2-1.1 — one sentence of the operator's Testing block
Replace the "Its Sonnet/Terra worker" sentence of the superproject CLAUDE.md Testing block (lines 10-12) with the Conductor's E-03r wording, adapted to the roster B1-1 landed; nothing else in the block changes.
Context: step B2-1.1 of C:\Programmierung\SW_Development
ework\PROMPTS_master-rework-runbook_2026-10-13.md (§3.4); rules: kickoff §2; the answers: Q-A3-02 (a), Q-B2-01 (a), recorded 2026-10-13; the wording source: C:\Programmierung\Orchestrator_System\CLAUDE.md lines 122-125 (read-only); the roster as B1-1 committed it (the §L row B1-1, by pointer).
Where: cwd C:\Programmierung\SW_Development on master; this session writes CLAUDE.md only.
Scope: that one sentence. Not here: any other line; AGENTS.md (frozen); the hygiene block.
Read first: the Conductor lines; the superproject CLAUDE.md Testing block; .claude/agents/real-stack-validator.md as B1-1 left it.
Write: CLAUDE.md.
Constraints: Edit tool only (CRLF as found); the rest of the Testing block and the hygiene block byte-identical before and after; no runner named; the hygiene checker zero violations before the commit; no test; no push.
Done when: the sentence reads in the E-03r form and names the validator agent and its model; one commit; the final message gives the §L row and the commit.
Commit line: rework: B2-1.1 - Testing block worker sentence reworded (Q-A3-02)
```

**Watch:** any byte outside the sentence.

#### `B2-2` — Dashboard, AndroidApp, PyApp guides reconciled; PyApp `.claude/CLAUDE.md` folded

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `PlantLibrary_Dashboard`, `PlantLibrary_AndroidApp`, `PlantLibrary_PyApp` on `main` (serial, in place) · **Precondition:** `B2-1` · **Writes:** three `CLAUDE.md`; PyApp `.claude/CLAUDE.md` · **Waits:** Q-A3-05, Q-A6A-04

```text
B2-2 — the three client guides
Reconcile the Dashboard, AndroidApp and PyApp CLAUDE.md files to the blueprint, in that order, each in its own commit, so that B5's design block lands above the roster heading.
Context: step B2-2 of the master rework runbook (§3, lane B2); rules: kickoff §2; the answers: Q-A3-03, Q-A3-05 (§Q); the blueprint: AUDIT_instructions-reconciliation-blueprint_2026-10-13.md §7.2 files 4, 5, 8, 9 and §7.6; the register rows: RC-A3-04, RC-A3-14, RC-A3-15, RC-A3-17.
Where: one suite at a time, in place on main, one commit each; the superproject is read, never written.
Scope per suite: the Build-and-test bullet(s) the blueprint names (cheapest gate first; a skipped browser run is never evidence); Engineering standards; Session rules as a pointer section to the superproject's with the suite's parameter (per Q-A3-03); Scratch policy addition (never elevated); the Claude subagent roster placed between Deliverable naming and the hygiene block; the "Procedure" skill list left for B1-2 to be reflected (write the list B1 will land: the shared five plus the PlantLibrary-only skills the register assigns to this suite); Design context kept until B5. PyApp additionally: .claude/CLAUDE.md replaced by the three-line stub and its Architecture rules folded into CLAUDE.md, deduplicated (Q-A3-05 (a)); line 5's delegation sentence replaced. Not here: AGENTS.md (frozen at B7-2); the hygiene block bytes; any package file.
Read first: the blueprint sections; each suite's CLAUDE.md and AGENTS.md; PlantLibrary_PyApp/.claude/CLAUDE.md.
Write: the four files.
Constraints: sources read-only; no test, no build; CRLF as found; the hygiene block byte-identical; block parity green per suite; no runner named; subagents in the foreground; no push.
Questions: proposed Q-B2-<nn> rows; continue.
If the context runs short: commit the complete suites, list the rest, stop; restart as B2-2-r2.
Done when: three (PyApp: one covering both files) commits; each suite's hygiene verdict unchanged; the final message lists the commits and the §L row.
Commit line: rework: B2-2 - CLAUDE.md reconciled - <sections>
```

*Orchestrator note:* three superproject lines `rework: B2-2 - bump <repo> gitlink; ledger B2-2`.
**Watch:** the roster heading placed above Deliverable naming (B5's installer would then put the design block in the wrong place, F-A3-16); a PyApp stub that drops a rule no other file carries.

#### `B2-3` — Server, SharedContracts, Workspace guides reconciled

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `PlantLibrary_Server`, `PlantLibrary_SharedContracts`, `PlantLibrary_Workspace` on `main` (serial, in place) · **Precondition:** `B2-1` · **Writes:** three `CLAUDE.md` · **Waits:** —

```text
B2-3 — the Server, SharedContracts and Workspace guides
Reconcile the three remaining suite CLAUDE.md files to the blueprint, each in its own commit.
Context: step B2-3 of the master rework runbook (§3, lane B2); rules: kickoff §2; the answer: Q-A3-03 (§Q); the blueprint: AUDIT_instructions-reconciliation-blueprint_2026-10-13.md §7.2 files 3, 6, 7; the register rows: RC-A3-04, RC-A3-15, RC-A3-17, RC-A3-29.
Where: one suite at a time, in place on main, one commit each.
Scope per suite as in B2-2 (gate bullet, Engineering standards, Session rules pointer, Scratch addition, roster placement, the skill list B1 will land); Server additionally the Docker wording of RC-A3-29; Workspace additionally the SUITE_HANDOFFS.md citation left as is until C1-2. Not here: AGENTS.md; hygiene blocks; packages.
Read first: the blueprint sections; each suite's CLAUDE.md.
Write: the three files.
Constraints: as B2-2.
Questions: proposed Q-B2-<nn> rows; continue.
If the context runs short: commit the complete suites, list the rest, stop; restart as B2-3-r2.
Done when: three commits; verdicts unchanged; the final message lists them.
Commit line: rework: B2-3 - CLAUDE.md reconciled - <sections>
```

**Watch:** as `B2-2`.

### 3.5 Lane B3 — hygiene, restructure and archive

#### `B3-1` — M-8 closing pass over seven repositories

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master` (in place) · **Precondition:** `R-3` · **Writes:** the M-8 deliverables §16 names inside TARGET (a REGISTER and an AUDIT under `repo-hygiene/`, a HANDOVER under `handovers/`), their INDEX lines, the hygiene runbook §L · **Waits:** —

```text
B3-1 — M-8: the closing pass of the repo-hygiene track
Close step M-8 of the repo-hygiene track as that runbook's §16 defines it, from the seven repositories as they stand, and record it in that runbook's ledger.
Context: step B3-1 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3, lane B3); rules: kickoff §2; the register rows: RC-A6S-* and RC-A6W-* naming M-8; the seven census audits AUDIT_corpus-census-*_2026-10-13.md §7.4 (today's verdict and census totals per repository) and §7.2 (every hold and its state).
Where: cwd C:\Programmierung\SW_Development on master; this session writes the superproject only; the submodules are read (git reads and the kit checker run read-only in each).
Scope: read §16 of repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md first and deliver every M-8 item that lies inside TARGET, under the names §16 gives them (the post-migration census REGISTER, the migration-record AUDIT, the HANDOVER into handovers/, each with its INDEX line): the per-repository verdict and census totals against the baseline of REGISTER_target-corpus-census_2026-09-15.md, every held name with its citer re-verified by grep at HEAD across all seven repositories, the holds whose release precondition is met listed for M-9 (B3-4), the two FINDINGs' states, the kit pin in all seven. The one §16 item that writes the Kit (its changelog commit) is not done here (SOURCE-K is read-only): it is owed item 17 of the master runbook §3b, and the §L row M-8 of the hygiene runbook is flipped "done except the Kit changelog (owed)" with the deliverables named. Not here: any rename, move, release or decision entry (those are B3-2 … B3-6); any edit in a submodule or the Kit.
Read first: that runbook's §16 and §L; the seven census audits' §7.2 and §7.4; REGISTER_target-corpus-census_2026-09-15.md §4 (the per-repo totals); handovers/INDEX.md.
Write: the §16 deliverables inside TARGET, their INDEX lines, the §L row.
Constraints: sources read-only; no test; the kit checker runs read-only in each repository; line endings as found (the hygiene runbook is CRLF in the working tree); subagents in the foreground; no push; the superproject hygiene verdict before the commit shows zero violations.
Questions: proposed Q-B3-<nn> rows; continue.
If the context runs short: commit what is complete, mark unread repositories "not measured", stop; restart as B3-1-r2.
Done when: the §16 deliverables inside TARGET exist and cover seven repositories; §L M-8 reads done except the Kit changelog; one commit; the final message names it and lists the M-9-ready holds.
Commit line: repo-hygiene: M-8 - closing pass - 7 repositories measured; M-9 set listed
```

**Watch:** a "closing pass" that renames anything; totals copied from the audits instead of re-run.

#### `B3-2` — superproject leftovers: graphify, `update_graph.bat`, the unplanned-backlog register

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master` (in place) · **Precondition:** `R-4.1` · **Writes:** `rework/REGISTER_unplanned-backlog_<date>.md`, `rework/INDEX.md`, `hygiene/HYGIENE_DECISIONS.md`, `update_graph.bat` (removed), `.agents/README.md` untouched · **Waits:** Q-G-05, Q-A6S-03, Q-A6S-04

```text
B3-2 — superproject leftovers and the backlog register
Retire the graphify residue, and harvest the live ideas of Todo.md and the unplanned backlog of IMPLEMENTATION_PLAN.md §7 into one register under rework/, so the sequencers can be archived later without losing a line.
Context: step B3-2 of the master rework runbook (§3, lane B3); rules: kickoff §2; the answers: Q-G-05, Q-A6S-03, Q-A6S-04 (§Q); the evidence: AUDIT_corpus-census-superproject_2026-10-13.md §0, §7.1-§7.3; AUDIT_batch-packages_2026-10-13.md §7.4 (what the sequencers uniquely carry).
Where: cwd C:\Programmierung\SW_Development on master; superproject only.
Scope: (1) rework/REGISTER_unplanned-backlog_<date>.md: one row per item from IMPLEMENTATION_PLAN.md §7 (Android cleartext/HTTPS, server setup guide, Gradle 9, server-side enrichment, Fable5 follow-through, MVP folders read-only) and from Todo.md's live ideas as Q-A6S-04 admits, each with its target suite and "needs plan-batch", never a copy of Todo.md's text beyond the idea's one line; the §5 operator decisions of IMPLEMENTATION_PLAN.md (SDA-DEC, the two security sign-offs, VGAP-020) listed as rows for C1's Q- entries; (2) graphify per Q-A6S-03 and its reading: this session deletes the untracked, git-ignored graphify-out/ folder itself (verify it is ignored and untracked first; delete through a short script, never a shell rm in a compound command), removes update_graph.bat by git rm, and writes one decision entry (next free id by grep) with allowlist-remove lines for both entries now gone from disk and retired-name for both; (3) Todo.md itself untouched unless Q-A6S-04 says otherwise. Not here: IMPLEMENTATION_PLAN.md or WORKSPACE_STATE.md moves (B3-6, after the hand-back); any submodule.
Read first: the §Q answers; AUDIT_corpus-census-superproject_2026-10-13.md §7.1-§7.3; IMPLEMENTATION_PLAN.md §5 and §7; Todo.md (read once, cite by line, copy nothing but the idea lines Q-A6S-04 admits); hygiene/HYGIENE_DECISIONS.md tail.
Write: the register, its INDEX line, the decision entry, the removal.
Constraints: sources read-only; no test; an allowlist-remove line only in the commit that removes the entry from disk (the checker fails otherwise); line endings as found; subagents in the foreground; no push; hygiene verdict zero violations before the commit.
Questions: proposed Q-B3-<nn> rows; continue.
If the context runs short: commit the register, list the rest, stop; restart as B3-2-r2.
Done when: the register exists with every §7 item and the admitted ideas; the decision entry folds green; one commit; the final message names it.
Commit line: rework: B3-2 - backlog register; graphify leftovers retired; D-<date>-<nn>
```

**Watch:** an `allowlist-remove` for `graphify-out` while the folder still exists on disk; Todo.md content copied wholesale (the operator keeps it untouched, P3 2026-07-15).

#### `B3-3` — Workspace: `archive/` declared, exempt-tree notes restated

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development\PlantLibrary_Workspace` on `main` (in place) · **Precondition:** `R-4.1` · **Writes:** `archive/README.md`, `hygiene/HYGIENE_DECISIONS.md` · **Waits:** Q-A6W-01, Q-A6W-04

```text
B3-3 — the Workspace archive and the restated exempt trees
Declare archive/ at its final path (its README the only member until B3-6 moves the sequencers after the hand-back) and restate the two stale exempt-tree notes, in one decision commit.
Context: step B3-3 of the master rework runbook (§3, lane B3); rules: kickoff §2; the answers: Q-A6W-01, Q-A6W-04 (§Q); the evidence and draft entries: AUDIT_corpus-census-workspace_2026-10-13.md §7.2, §7.3.
Where: cwd the Workspace submodule on main, in place; one commit; the superproject is read only.
Scope: (1) archive/README.md with an empty mapping table | old path | new path | date | entry |; (2) one decision entry (next free id by grep) in the shape the audit drafts: exempt-tree: archive — legacy (the path exists in this commit through its README); and a second entry restating methodology/Design_Template_Initiative as frozen (47 files, closed 2026-10-12) and methodology/GUI_Improvement_Methodology as pinned 4.1.0 (74 files), no file moved. Not here: WORKSPACE_STATE.md, SUITE_HANDOFFS.md and V1_IMPLEMENTATION_SEQUENCE.md (B3-6, after C1-2 and Q-G-05); any frozen or pinned tree (K-7); the Repo_Restructure set folder (M-9 after the Kit session).
Read first: the §Q answers; the audit sections named; the Workspace hygiene/HYGIENE_DECISIONS.md tail and CONSUMED_HYGIENE.md.
Write: the files listed.
Constraints: sources read-only; no test; the declared path exists in the commit that declares it; nothing under an existing exempt-tree or exempt-subfolder line moves; line endings as found; the Workspace hygiene verdict shows zero violations and ten held before and after; no push.
Questions: proposed Q-B3-<nn> rows; continue.
If the context runs short: commit what folds green, list the rest, stop; restart as B3-3-r2.
Done when: one commit; the verdict is unchanged in count; archive/ exists with its README; the final message names the commit and the D-ids.
Commit line: rework: B3-3 - archive/ declared; exempt-tree notes restated; D-<date>-<nn>
```

*Orchestrator note:* superproject line `rework: B3-3 - bump PlantLibrary_Workspace gitlink; ledger B3-3`.
**Watch:** an `exempt-tree` line whose path is created in a later commit; any sequencer moved before the hand-back exists.

#### `B3-4` — M-9: the five V1 proposal holds released and renamed; Dashboard's two pinned `docs/` holds

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `PlantLibrary_PyApp`, `PlantLibrary_AndroidApp`, `PlantLibrary_Dashboard`, `PlantLibrary_Server`, `PlantLibrary_SharedContracts` on `main` (serial, in place) · **Precondition:** `B3-1` · **Writes:** five `hygiene/HYGIENE_DECISIONS.md`, `implementation/System_V1_Implementation/proposal/INDEX.md` (+ Dashboard `implementation/System_V1_Implementation/planning/INDEX.md`), the renamed files, their citers · **Waits:** Q-A6P-03, Q-A6A-02, Q-A6D-02, Q-A6D-03, Q-A6V-02, Q-A6C-04

```text
B3-4 — M-9 hold releases in five suites
Release and rename the five <SUITE>_V1_PROPOSAL.md holds whose precondition (onboarding 2a/2b) is met, and Dashboard's two pinned docs/ holds, one suite per commit, per the kit's release rule (K-6): the release line in the commit of the git mv.
Context: step B3-4 of the master rework runbook (§3, lane B3); rules: kickoff §2; the answers: the six Q-A6 rows in §Q; the drafts: AUDIT_corpus-census-{pyapp,androidapp,dashboard,server,sharedcontracts}_2026-10-13.md §7.2-§7.3 (the entry text, the INDEX line and the Renamed row per suite); the repo-hygiene runbook §17 (M-9's shape); B3-1's evidence file (the M-9-ready list).
Where: one suite at a time, in place on main, one commit each.
Scope per suite: git mv proposal/<SUITE>_V1_PROPOSAL.md proposal/PROPOSAL_<suite>-v1_2026-07-10.md; the decision entry (next free id by grep) with the release line and the operator's words verbatim; the proposal/INDEX.md line replaced and the Renamed row flipped from held to the new name; every citer swept by git grep at HEAD in that suite (STATE.md, README.md, CONTEXT_INDEX.md lines the audits list); Dashboard additionally the two docs/ files moved to the targets D-2026-09-17-02 names, with their INDEX lines. Not here: any exempt-tree path; the Workspace set folder (K-7); any package row.
Read first: the §Q answers; the five audit sections; each suite's hygiene/HYGIENE_DECISIONS.md tail; the repo-hygiene runbook §17.
Write: the files listed.
Constraints: sources read-only; no test; a package STATE.md citer line is edited only in its path text, never its row content (a STATE line that names a row id beside "blocked" is a parser record — the swept lines carry none); line endings as found (package files are CRLF); each suite's verdict after the commit reads zero violations, zero held (Dashboard, Server: the docs/ code-group holds outside roots remain in the record); no push.
Questions: proposed Q-B3-<nn> rows; continue.
If the context runs short: commit the complete suites, list the rest, stop; restart as B3-4-r2.
Done when: five commits; each verdict as stated; the final message lists commits and D-ids per suite.
Commit line: rework: M-9 - <SUITE>_V1_PROPOSAL released and renamed; D-<date>-<nn>
```

*Orchestrator note:* five superproject lines; the repo-hygiene runbook's §L row M-9 is flipped by the orchestrator at the boundary with the five commits named.
**Watch:** a `release` line in a different commit from the `git mv`; a citer in a frozen MVP tree edited (served by the mapping table instead); the SharedContracts proposal's citer inside `STATE.md:11` rewritten beyond the path.

#### `B3-5` — stale `run_next_batch.py` scripts retired; Server docs links fixed

**Model · reasoning:** Sonnet 5.5 · high · **Route:** session (headless) · **Where:** `PlantLibrary_Dashboard`, `PlantLibrary_Server`, `PlantLibrary_Workspace` on `main` (serial, in place) · **Precondition:** `B4-2` · **Writes:** Dashboard and Server `scripts/run_next_batch.py`, Workspace `implementation/System_V1_Implementation/scripts/run_next_batch.py`, Server `docs/*.md`, two READMEs · **Waits:** Q-A6V-04, Q-A6V-05

```text
B3-5 — stale sequencer scripts and broken doc links
Retire the three run_next_batch.py scripts that read files moved in July, and fix the Server docs links that point at retired Workspace paths.
Context: step B3-5 of the master rework runbook (§3, lane B3); rules: kickoff §2; the answers: Q-A6V-04, Q-A6V-05 (§Q); the evidence: AUDIT_corpus-census-{dashboard,server,workspace}_2026-10-13.md (F-A6D-*, F-A6V-07, F-A6V-08, the links table), AUDIT_batch-packages_2026-10-13.md §7.2 rows naming run_next_batch.py.
Where: one suite at a time, in place on main, one commit each.
Scope: per Q-A6V-04 the three scripts removed by git rm (or given a two-line refusal banner if the answer keeps them), the README sentences that name them repointed to the run-batch invocation; Server's eight docs/ notes and two scaffold READMEs with ../PlantLibrary_Workspace links repointed to the current paths or marked "retired path, see <mapping table>" per Q-A6V-05; metrics.py:4's dangling citation left for a batch (code; a deferred row is proposed). Not here: any code file; any package row; docs bodies.
Read first: the §Q answers; the audit sections; the three scripts' headers.
Write: the files listed.
Constraints: sources read-only; no test; no code edit; line endings as found; each suite's verdict unchanged; no push.
Questions: proposed Q-B3-<nn> rows; continue.
If the context runs short: commit the complete suites, stop; restart as B3-5-r2.
Done when: three commits; no README names a retired script; the final message lists them.
Commit line: rework: B3-5 - run_next_batch.py retired; docs links fixed
```

**Watch:** a link "fix" that rewrites a frozen file; a script deleted that a package row's validation cell names (none does — grep first).

#### `B3-7` — residual prose sweep (inserted at the B8-1/B3-5 flip, 2026-10-13)

**Model · reasoning:** Sonnet 5.5 · high · **Route:** session (headless) · **Where:** `PlantLibrary_AndroidApp`, `PlantLibrary_Server`, `PlantLibrary_Workspace`, `PlantLibrary_PyApp` on `main` (serial, in place) · **Precondition:** `B3-6` · **Writes:** the files the step map row names · **Waits:** —

```text
B3-7 — the residual prose sweep
Repoint or mark the live lines that still name the retired run_next_batch.py scripts, the superseded driver procedure, retired Workspace paths or PyApp's removed graphify sanction, each in its own suite commit, text only.
Context: step B3-7 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3.5); rules: kickoff §2; the answers: Q-B4-03 (a), Q-B3-05 (a), Q-B3-06 (a), Q-B3-07 (a), Q-B8-01 (a), all recorded 2026-10-13; the lines, by the reports of B3-5 and B8-1: AndroidApp suite README.md ("DRIVER_SCRIPT.md scope rules remain binding"); Server root README.md "Derivation" links, docs/SV-DOMAIN-01_domain_port_notes.md lines 4-5 (the ../PlantLibrary_PyApp paths, wrong from docs/), docs/SV-B07_dashboard_endpoint_coverage_report.md line 48 (an ACCEPTANCE_GATES.md path that does not resolve); Workspace docs/local_development.md line 7, implementation/README.md line 16, implementation/System_V1_Implementation/DRIVER_SCRIPT.md line 27 ("its fate is master rework step B3-5"); PyApp tests/test_repo_hygiene.py lines 45-47 (the graphify-out allowlist entry) with a dated STATE.md line in the V1 package naming the removal; AndroidApp docs/README.md line 3 ("Populated starting Batch AN-B00") and a dated "superseded in part" line in docs/module_architecture.md (the two remaining Q-A6A-04 (a) items, Q-B2-02 (a)).
Where: one suite at a time, in place on main, one commit each; the superproject is never written.
Scope: the lines named; a retired path is marked "(retired path, see <the mapping or canonical file>)" as B3-5 did; a driver mention is restated as "superseded by the run-batch skill and SCOPE.md"; the PyApp allowlist entry removed (a test file edit limited to the allowlist list; no test is run) and the STATE line added. Not here: frozen trees; any package row cell; any validation cell; code.
Read first: B3-5's and B8-1's reports as quoted in the master runbook §L notes; each line in place.
Write: the files listed.
Constraints: sources read-only; no test, no build, no app; line endings as found (Edit tool); each suite's hygiene verdict unchanged; no push; subagents in the foreground.
Questions: proposed Q-B3-<nn> rows; continue.
If the context runs short: commit the complete suites, stop; restart as B3-7-r2.
Done when: four commits; no live line names the retired scripts or calls the driver binding; the final message gives the §L row and the commits the gitlinks take.
Commit line: rework: B3-7 - residual prose sweep - <n> lines
```

**Watch:** a frozen file edited; a line in a package row.

#### `K-2` — Repo Hygiene Template Kit session: K-7 and the pilot lessons (inserted 2026-10-13, Q-G-06 "a (run yourself)")

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\Repo_Hygiene_Template_Kit_wt\k7` on branch `pl/k7-2026-10` (a worktree the orchestrator creates from `master`; the main checkout, which every consumer pins by path, is never touched until the merge) · **Precondition:** `R-4.1` · **Writes:** the hygiene kit only; never a TARGET repository · **Waits:** —

```text
K-2 — the Repo Hygiene Template Kit: K-7 and the pilot lessons, release 0.3.0
Close finding K-7 in the kit (an exempt tree or subfolder can be released and a set folder can be held), add the pilot-lessons changelog entry, and ship them as one minor release 0.3.0: branch, tests, changelog, version, merge to master, tag.
Context: step K-2 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3.5), read by that absolute path and never edited; this session is outside the PlantLibrary program's write scope: it writes the kit and nothing else; the kit's own rules are its CONTRIBUTING.md, KIT_SPEC.md and its tests; the finding: C:\Programmierung\SW_Development\handovers\FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md (its "Next action" K-7 section and proposed fix: a release that ends an exempt-tree/exempt-subfolder declaration, a directory held-name, three fixtures); the lessons: C:\Programmierung\SW_Development\handovers\HANDOVER_repo-hygiene-pilot-closeout_2026-10-13.md (the ten lessons owed to the kit changelog); the version choice: register row Q-B3-02 (a).
Where: cwd C:\Programmierung\Repo_Hygiene_Template_Kit_wt\k7 on branch pl/k7-2026-10 (a linked worktree of C:\Programmierung\Repo_Hygiene_Template_Kit); the merge to master and the tag are done from the main checkout at the end, fast-forward only; nothing under C:\Programmierung\SW_Development is written.
Scope: (1) the checker: `release` may name an exempt-tree or exempt-subfolder path (the declaration ends; existence is judged after folding, as K-6 did for held-name), and `held-name` may name a directory; KIT_SPEC.md §1.6/§6 updated; (2) three negative fixtures and the self-test extended to plant them; (3) the pytest wrapper and the installer unchanged unless the spec change requires it; (4) CHANGELOG with the K-7 entry and the ten pilot lessons; KIT_VERSION.md 0.3.0; the example anchored target updated if its record shape changes; (5) merge pl/k7-2026-10 into master fast-forward, tag v0.3.0. Not here: any consumer re-pin (B3-8); any PlantLibrary file.
Read first: the finding; the handover's lessons section; KIT_SPEC.md; checker/repo_hygiene_check.py (the record folding around lines 420-460 and 740-770); the existing fixtures and tests; CONTRIBUTING.md; installer/INSTALL.md "The pin" (what a re-pin needs).
Write: the kit files the scope names, on the branch; then master by fast-forward and the tag.
Constraints: the kit's own checker self-test and its unit tests are the kit's contract and run here (seconds; no browser; this is not a PlantLibrary lane); nothing else runs; no push unless the kit has a remote the operator pushes (check `git remote -v`; if there is one, push the branch and the tag — the operator allowed pushing); line endings as the kit keeps them.
Done when: master carries 0.3.0 tagged v0.3.0 with K-7 and the lessons; the self-test and the kit tests are green; the final message lists the commits, the tag, the re-pin command a consumer runs (from INSTALL.md), and gives the §L row.
Commit line: kit: <item> - <summary>
```

*Orchestrator note:* the worktree is created by the orchestrator before launch (`git -C C:\Programmierung\Repo_Hygiene_Template_Kit worktree add C:\Programmierung\Repo_Hygiene_Template_Kit_wt\k7 -b pl/k7-2026-10 master`); after the merge the orchestrator removes it. §L row `K-2`.
**Watch:** a `release` that silently drops the existence check for still-held paths; a version bump without the changelog.

#### `B3-8` — re-pin to kit 0.3.0 and the Workspace set-folder release (M-9, after K-2)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master`, then each suite on `main` (serial, in place) · **Precondition:** `K-2`, `B3-6` · **Writes:** seven pins and records, seven checker copies, fourteen rule blocks; Workspace `docs/proposals/**` (the set folder renamed) and its INDEX; five suites' `implementation/README.md` one-line path fix · **Waits:** —

```text
B3-8 — the seven repositories re-pinned to kit 0.3.0; the Workspace restructure set released
Re-pin every repository to the released kit with the installer (its documented re-pin: a plain run, then --force, one decision entry each), then do the one M-9 action K-7 held: rename the Workspace set folder with its release line and new exempt-tree line in one entry, the sweep, the INDEX flip, and the five one-line path citers in the suites.
Context: step B3-8 of the master rework runbook (§3.5); rules: kickoff §2 (rule 3: the installer's INSTALL.md is the procedure; the checker is the contract); the answers: Q-G-06 (a, "run yourself"), Q-B3-02 (a); the release: K-2's final message (by pointer: the §L row K-2) and the kit's CHANGELOG; the M-9 recipe for the set folder: AUDIT_corpus-census-workspace_2026-10-13.md §7.2 "What M-9 would release once K-7 is decided"; the hygiene runbook §17.
Where: the superproject first, then the six suites, one commit each, in place.
Scope: per repository the installer re-run (--target alone, then --force) with the decision entry it requires, the verdict before and after quoted; Workspace additionally: git mv of docs/proposals/Repo_Restructure_MVP_V1_Split/ to docs/proposals/PROPOSAL_repo-restructure-mvp-v1-split_2026-07-15/, the release of the old REVIEW_LIST.md exempt-tree path and the new exempt-tree line in the same entry, the two sweeps the audit names, the manifests restored byte for byte, the docs/proposals/INDEX.md line and Renamed row; the five suites' implementation/README.md path lines; the hygiene runbook §L M-9 line appended. Not here: any other hold; any package row.
Read first: K-2's report; the kit's INSTALL.md; the audit section; the hygiene runbook §17.
Write: the files listed.
Constraints: no test; the installer writes only what INSTALL.md lists; line endings as found; every verdict after reads zero violations; no push.
Questions: proposed Q-B3-<nn> rows; continue.
If the context runs short: commit the complete repositories, stop; restart as B3-8-r2.
Done when: seven pins read 0.3.0; the Workspace set is renamed and its hold released; the final message lists commits and D-ids and gives the §L row.
Commit line: hygiene: B3-8 - re-pinned to kit 0.3.0; <per repository>
```

**Watch:** an installer run that rewrites a rule block's neighbours; the set folder renamed before the kit's `release` form exists.

#### `B3-6` — the stale sequencers archived (superproject, Workspace)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master`; then `PlantLibrary_Workspace` on `main` · **Precondition:** `C1-2` · **Writes:** superproject `archive/**`, `hygiene/HYGIENE_DECISIONS.md`, root; Workspace `archive/**`, `hygiene/HYGIENE_DECISIONS.md`, `implementation/System_V1_Implementation/*` citers · **Waits:** Q-G-05, Q-A6S-01, Q-A6S-05

```text
B3-6 — the sequencers archived after the hand-back
Archive IMPLEMENTATION_PLAN.md (superproject) and SUITE_HANDOFFS.md's superseded body plus V1_IMPLEMENTATION_SEQUENCE.md (Workspace) now that the runbook's hand-back section replaces them.
Context: step B3-6 of the master rework runbook (§3, lane B3); rules: kickoff §2; the answer: Q-G-05 (§Q) and Q-A7-07; the hand-back section §H of this runbook, written at C1-2 (by pointer); the drafts: AUDIT_corpus-census-superproject_2026-10-13.md §7.3, AUDIT_corpus-census-workspace_2026-10-13.md §7.3 (entry D-…-03), AUDIT_batch-packages_2026-10-13.md §7.4.
Where: superproject first (one commit), then the Workspace (one commit); in place.
Scope: superproject — archive/ created with archive/README.md mapping table, git mv IMPLEMENTATION_PLAN.md archive/root/IMPLEMENTATION_PLAN.md, one decision entry (allowlist: archive; exempt-tree: archive — legacy; allowlist-remove: IMPLEMENTATION_PLAN.md; the exempt-name line left as inert), the onboarding runbook's ten citing lines left as they are (held names resolve through the mapping table; the runbook is live, never edited by B3), the root hold of D-2026-09-16-01 already released, the dead `.gitignore` lines 11-12 (the graphify ignore line and its comment) removed (Q-B3-09 (a)); a general root `reviews/` (pattern standard) declared for the operator-run review skills' deliverables with its allowlist entry, roots-table row and seeded INDEX.md in the same entry (Q-B1-04 (a)); Workspace — git mv WORKSPACE_STATE.md archive/WORKSPACE_STATE.md with its two citers (README.md and docs/PROPOSAL_fable5-product-strategy-v2_2026-07-11/README.md) repointed, git mv implementation/System_V1_Implementation/V1_IMPLEMENTATION_SEQUENCE.md archive/ and, if Q-A7-07 (a) reshaped SUITE_HANDOFFS.md in place, nothing else, else git mv it too; archive/README.md's mapping rows; the decision entry without directive (archive/ already declared at B3-3); the package CONTEXT_INDEX.md read order repointed per C1-2. Not here: Todo.md (Q-A6S-04); any frozen tree.
Read first: §H of this runbook; the drafts; both decision records' tails.
Write: the files listed.
Constraints: sources read-only; no test; nothing moves that an exempt-tree line names; the superproject allowlist change in the same commit as the disk change; line endings as found; verdicts zero violations; no push.
Questions: proposed Q-B3-<nn> rows; continue.
If the context runs short: commit the complete repository, stop; restart as B3-6-r2.
Done when: two commits; both verdicts green; the final message names them and the D-ids.
Commit line: rework: B3-6 - sequencers archived (WORKSPACE_STATE.md, IMPLEMENTATION_PLAN.md, V1_IMPLEMENTATION_SEQUENCE.md); D-<date>-<nn>
```

**Watch:** archiving before §H exists; editing the onboarding runbook's citing lines (a kit constraint, and B8's file).

### 3.6 Lane B4 — batch packages

#### `B4-1` — parser-honest package edits without a question

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `PlantLibrary_Server`, `PlantLibrary_Workspace`, `PlantLibrary_SharedContracts` on `main` (serial, in place) · **Precondition:** `B7-1` (its committed census script is the one quoted) · **Writes:** three packages' `BATCH_PLAN.md` and `STATE.md` · **Waits:** —

```text
B4-1 — the three package edits that need no answer
Make the parser read what the plans mean: SV1-B06's range token expanded, SY1-B07 moved before SY1-B05, SC1-B02's cross-suite range written as four tokens; each with its dated STATE decision.
Context: step B4-1 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3, lane B4); rules: kickoff §2 (rule 4: plan-batch's row schema, a decision in STATE.md, validation cells untouched); the register rows: RC-A7-* for these three edits; the exact edits and decision texts: AUDIT_batch-packages_2026-10-13.md §7.2 rows "Server · BATCH_PLAN.md:126", "Workspace V1 · BATCH_PLAN.md:95-146", "SharedContracts · BATCH_PLAN.md:60", and its conventions paragraph (decision-line shape, no row id beside "blocked"/"deferred").
Where: one suite at a time, in place on main, one commit each; the superproject is read only.
Scope: exactly the three edits and their three STATE.md decision lines under "Continuation updates". Not here: out-of-band markers (B4-2), DRIVER_SCRIPT.md (B4-2), SDA (B4-3), any PyApp file (its plan contract is pinned by instance 2), any validation cell.
Read first: the audit rows named; each package's STATE.md tail and the plan-batch skill §5.4 (the decision-line shape) in this suite's .claude/skills/plan-batch/SKILL.md.
Write: the six files.
Constraints: sources read-only; no test; the superproject's static package census is run read-only after each package (bytecode writing disabled) and its classification lines are quoted in the final message — expected SV1-B06 blocked, everything else unchanged; CRLF as found; each suite's hygiene verdict unchanged; no push.
Questions: proposed Q-B4-<nn> rows; continue.
If the context runs short: commit the complete suites, stop; restart as B4-1-r2.
Done when: three commits; the census reads 0 errors with the expected classifications; the final message lists commits and census lines.
Commit line: rework: B4-1 - <package> parser-honest edit - <what>
```

*Orchestrator note:* three superproject lines `rework: B4-1 - bump <repo> gitlink; ledger B4-1`.
**Watch:** a decision line that writes a row id next to "blocked" (the parser reads it as a record); a moved batch section that loses a line; any touch of PyApp.

#### `B4-2` — out-of-band markers; `DRIVER_SCRIPT.md` to pointer stubs; README run lines

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** the six suites on `main` (serial, in place) · **Precondition:** `B4-1`, `R-4.1` · **Writes:** seven packages' `BATCH_PLAN.md` (heading tails), `DRIVER_SCRIPT.md`, `README.md`, `STATE.md`; two suite READMEs · **Waits:** Q-A7-02, Q-A7-05

```text
B4-2 — attended batches marked, the legacy driver reduced to a pointer
Append the Conductor's out-of-band marker to the attended batch headings, reduce every DRIVER_SCRIPT.md to a pointer stub with a section-to-owner table, and repoint every README run line to the run-batch invocation.
Context: step B4-2 of the master rework runbook (§3, lane B4); rules: kickoff §2; the answers: Q-A7-02, Q-A7-05 (§Q); the exact edits: AUDIT_batch-packages_2026-10-13.md §7.2 table A (DRIVER_SCRIPT.md, README.md) and the per-package marker rows (PyApp PY1-B06/PY1-B00 — heading tails only, PyApp's plan contract unaffected; Dashboard WD1-B00; AndroidApp AN1-B10; Workspace V1 SY1-B04); the precedent stub: PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/DRIVER_SCRIPT_TEMPLATE.md:1-14; the §N note GC-7053.
Where: one suite at a time (Workspace carries two packages), in place on main, one commit per suite.
Scope: the markers; the seven stubs (H1 kept; "Superseded <date> by the run-batch skill and SCOPE.md; full text at <the commit before this one, by pointer>"; the owner table); the package README.md run lines and file-table rows; the suite READMEs of Dashboard and SharedContracts; one STATE.md decision line per package. Not here: any row cell; SDA's other files (B4-3); PyApp's BATCH_PLAN body beyond the two heading tails.
Read first: the audit rows; the §Q answers; each DRIVER_SCRIPT.md once (to write the owner table), each package README.
Write: the files listed.
Constraints: sources read-only; no test; the census after each suite reads 0 errors with classifications unchanged; PyApp's plan-contract hash unchanged (the parser's own computation, quoted before and after in the final message); CRLF as found; verdicts unchanged; no push.
Questions: proposed Q-B4-<nn> rows; continue.
If the context runs short: commit the complete suites, stop; restart as B4-2-r2.
Done when: six commits; no DRIVER_SCRIPT.md instructs _ACT_STATE.md; the final message lists commits, census lines and the PyApp hash.
Commit line: rework: B4-2 - out-of-band markers; DRIVER_SCRIPT.md stubs; README run lines
```

**Watch:** a marker appended to a batch that is not attended; a PyApp edit outside heading tails (the hash moves; instance 2 then refuses the retry).

#### `B4-3` — SDA package superseded

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `PlantLibrary_Workspace` on `main` (in place) · **Precondition:** `B4-1` · **Writes:** `implementation/System_Design_Architecture/*` · **Waits:** Q-A7-06, Q-G-01

```text
B4-3 — the System_Design_Architecture package superseded by the design lanes
Record, row by row, that the SDA package's open work is carried by B5 (the Configuration) and B6 (the GUI rework), keeping every row, id and validation cell.
Context: step B4-3 of the master rework runbook (§3, lane B4); rules: kickoff §2; the answers: Q-A7-06, Q-G-01 (§Q); the exact edits: AUDIT_batch-packages_2026-10-13.md §7.2 rows "SDA · whole package", "SDA · BATCH_PLAN.md:86…179" (only under (b)), "SDA · TASK_CHECKLIST.md:12", "SDA · CONTEXT_INDEX.md:10, README.md:49,67, MODEL_RECOMMENDATION.md"; §7.3's SDA rows (what each family maps to); AUDIT_design-kit-and-methodology_2026-10-13.md §7.4 (Q-G-01's form) and F-A4-17 (SDA-DEC-01..05 still open though accepted at G1).
Where: the Workspace submodule on main, in place; one commit.
Scope under (a): the package decision line; each open row's status set to deferred with one dated STATE line per row naming the B5/B6 deliverable (so the deferral resolves); SDA-DEC-01..05 recorded as overtaken (DEC-01 by Q-G-01, DEC-02..05 as Configuration decisions for B5); the TASK_CHECKLIST header's status list replaced by the six-value set and its three nonexistent skills named "historical"; CONTEXT_INDEX.md row 10 and the "Do not read as context" section; README run line; MODEL_RECOMMENDATION.md banner; row SDA-QA-02's artifact repointed from WORKSPACE_STATE.md to "the master rework runbook's hand-back section, written at its step C1-2" (a pointer to a section that lands later, stated as such). Not here: any validation cell; any file outside the package.
Read first: the §Q answers; the audit rows; the package's five files.
Write: the package files.
Constraints: sources read-only; no test; plan-batch's row schema and status set; the census after the edit reads 0 errors (the package is unbound; its classifications may change and are quoted); CRLF as found; the Workspace verdict unchanged; no push.
Questions: proposed Q-B4-<nn> rows; continue.
If the context runs short: commit what parses, stop; restart as B4-3-r2.
Done when: one commit; 0 errors; every open SDA row carries a dated deferral line; the final message names the commit.
Commit line: rework: B4-3 - SDA package superseded by B5/B6 - <n> rows deferred
```

**Watch:** a status outside the six-value set; a deferral line without the row's own dated rationale (F-A7-18).

#### `B4-4` — decision lines and traceability sections

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** the six suites on `main` (serial, in place) · **Precondition:** `B1-2`, `B4-2` · **Writes:** seven `STATE.md`, `CONTEXT_INDEX.md`, `SCOPE.md` · **Waits:** Q-A7-01, Q-A7-03, Q-A7-04

```text
B4-4 — the decision lines every package owes, and the traceability section
Record in each package, as STATE lines only (no cell changes): plan-batch 1.5.1-pl adopted with its one unrunnable self-review item, the model-tier reading, the mechanical already_done readings, which open rows' validation cells the deferred register points at (by DV id), the plan-order notes; add the Traceability section to CONTEXT_INDEX.md and the "Procedure: the run-batch skill" line to SCOPE.md.
Context: step B4-4 of the master rework runbook (§3, lane B4); rules: kickoff §2; the answers: Q-A7-01, Q-A7-03, Q-A7-04 (§Q); the exact texts: AUDIT_batch-packages_2026-10-13.md §7.2 table A rows "STATE.md" (three) and the package-specific STATE rows; AUDIT_instructions-reconciliation-blueprint_2026-10-13.md §7.5 (RC-A3-23, RC-A3-24); the deferred register's rows for each package (by id).
Where: one suite at a time, in place on main, one commit per suite.
Scope: the decision lines as drafted; CONTEXT_INDEX.md gains ## Traceability (row → anchor → evidence, as the Conductor's files do) in all seven; SCOPE.md's header line reads "Procedure: the run-batch skill (DRIVER_SCRIPT.md is a pointer)" and keeps ## Standing invariants verbatim; SharedContracts' CONTEXT_INDEX.md gains ## External context only if the package reads an external file; SharedContracts additionally: the three package lines that still say the Workspace SDA package owns design artifacts (README.md:17-18, CONTEXT_INDEX.md:21, STATE.md:14) repointed to design/ and the STATE decision line the SCOPE.md amendment of B5-2 owes (Q-B5-06 (a)). Not here: any row cell; any plan move (Q-A7-04 (a) keeps PY1-B05 in place; the note is a STATE line).
Read first: the audit rows; the §Q answers; each package's STATE.md, CONTEXT_INDEX.md, SCOPE.md; this suite's plan-batch skill §5.4.
Write: the files listed.
Constraints: as B4-2 (census 0 errors, PyApp hash unchanged — STATE.md is not part of it; CRLF; no push).
Questions: proposed Q-B4-<nn> rows; continue.
If the context runs short: commit the complete suites, stop; restart as B4-4-r2.
Done when: six commits; every package carries the lines; the final message lists commits and census lines.
Commit line: rework: B4-4 - STATE decisions; CONTEXT_INDEX traceability; SCOPE procedure line
```

**Watch:** a decision line that names a row id beside "deferred" where no deferral is meant; a Standing invariants heading reworded.

#### `B4-5` — static bind proof under both parsers

**Model · reasoning:** Sonnet 5.5 · high · **Route:** check · **Where:** `C:\Programmierung\SW_Development` on `master` · **Precondition:** `B4-2`, `B4-3`, `B4-4` · **Writes:** `rework/EVIDENCE_bind-proof_<date>.md`, `rework/INDEX.md` · **Waits:** —

```text
B4-5 — the static proof that the seven packages stay bindable
Prove, without calling any instance, that the seven packages parse clean under the Conductor's main parser (instance 2's bindings are obsolete per Q-G-02/Q-A8-02 of 2026-10-13, so its parser leg is informational only), that every git toplevel is its suite folder and every tree is clean; PyApp's plan-contract hash is quoted before and after as a fact, no longer as a gate.
Context: step B4-5 of the master rework runbook (§3, lane B4); rules: kickoff §2; the proof list: AUDIT_batch-packages_2026-10-13.md §7.2 "What B4's static proof must show" and §7.5 "What a B4 static check must prove"; the census script with its --parser-src option from B7-1 (by pointer).
Where: cwd C:\Programmierung\SW_Development on master; writes the superproject only.
Scope: the six proofs, each quoted verbatim into the evidence file, with the parser provenance line of both runs; the PyApp plan-contract hash computed by the parser on the tree before B4 (the commit §L row R-4.1 records) and after; the config roots of C:\Programs\AI_Orchestrator_2\config.yaml lines 505-517 read once and checked to exist. Not here: any edit; any instance call; any database read.
Read first: the audit sections; scripts/harness/check_batch_packages.py usage.
Write: the evidence file and its INDEX line.
Constraints: sources and the instance read-only; bytecode writing disabled; no test; no push.
Questions: proposed Q-B4-<nn> rows; continue.
If the context runs short: commit the proofs done, mark the rest "not measured", stop; restart as B4-5-r2.
Done when: the evidence file holds the proofs with their outputs; one commit; the final message names it; the final message gives the §L row and the commit the gitlink takes.
Commit line: rework: B4-5 - static bind proof - 7 packages, 2 parsers
```

**Watch:** a proof that runs the instance's REST or opens its database; a hash computed by anything but the parser.

### 3.7 Lane B5 — Design Configuration and anchoring

#### `B5-1` — design-gate evidence pack

**Model · reasoning:** Opus 5.5 · xhigh · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master` (in place) · **Precondition:** `R-3` · **Writes:** `rework/EVIDENCE_design-gate-pack_<date>.md`, `rework/INDEX.md` · **Waits:** —

```text
B5-1 — the evidence pack for the design gate
Give the operator everything the design gate needs in one file: the canon imported as a Configuration in scratch, the validator's report, the seven failing contrast pairs with the smallest value change that passes each, the template defaults the import adds, the P-DS survival table and the ban-scope choice.
Context: step B5-1 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3, lane B5); rules: kickoff §2; the questions it feeds: Q-A4-02, Q-A9D-02, Q-A4-03, Q-A4-04, Q-A4-01; the evidence: AUDIT_design-kit-and-methodology_2026-10-13.md §7.1, §7.3, §7.4, §7.7, F-A4-06, F-A4-07; AUDIT_gui-current-state-dashboard_2026-10-13.md §0 item 4; AUDIT_gui-current-state-androidapp_2026-10-13.md §7.7 (iii).
Where: cwd C:\Programmierung\SW_Development on master; every Kit tool output goes into the session's scratch folder outside every repository; the superproject receives the evidence file only.
Scope: (1) the Kit's flat-token import tool run with its output in the session's scratch directory outside every repository, and the Kit's validator run in its no-write-back mode, both quoted; (2) a table of the 7 failing pairs: pair, measured ratio, required ratio, the candidate value that passes with the smallest perceptual change, what P-DS-03/P-DS-07 said and what the canon's own usage notes say; (3) the template defaults the import adds (elevation policy, motion, z) as design facts the gate must accept or amend; (4) the P-DS-01..10 survival table; (5) BAN-02's scoped form against the usage notes' "anywhere" ban, with the Dashboard drift checker and the Android ARGB spelling as consequences; (6) the Kit pin proposal (f08e588 / v1.0.0) and what Kit master's methodology 4.0.0 pin means for the methodology pointer; (7) the hybrid layout of §7.4 drawn as the folder tree each repository would carry under Q-A4-01 (a). Not here: any write into SharedContracts or the Kit; any emitter output committed; any decision — every item ends in the question it feeds.
Read first: the audit sections named; C:\Programmierung\Design_Template_Kit\HOW_TO_INSTANTIATE_A_NEW_PROJECT.md and template\TEMPLATE_SPEC.md §3.1 and the a11y section (read-only); PlantLibrary_SharedContracts/design-tokens/TOKEN_USAGE_NOTES.md; the P-DS record PlantLibrary_Workspace/implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md.
Write: the evidence file and its INDEX line.
Constraints: sources read-only (the Kit's node tools run only with outputs in scratch; node_modules exist, nothing is installed); no test, no build, no browser; no push; the superproject verdict zero violations before the commit.
Questions: proposed Q-B5-<nn> rows for anything the seven questions above do not cover; continue.
If the context runs short: commit the items done, mark the rest "not done", stop; restart as B5-1-r2.
Done when: the file carries the seven items with quoted tool output; one commit; the final message names it and restates in ten lines what the operator must decide at G-DS.
Commit line: rework: B5-1 - design-gate evidence pack - 7 pairs, defaults, P-DS table, ban scope
```

**Watch:** a tool run whose output path lies inside a repository; a "fix" proposed as a token edit in SharedContracts.

#### `B5-2` — the Configuration in SharedContracts `design/`, DRAFT 0.1.0

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development\PlantLibrary_SharedContracts` on `main` (in place) · **Precondition:** `B5-1`, `B2-3`, `R-4.1` · **Writes:** `design/**`, `CLAUDE.md`, `SCOPE.md` (the V1 package's), `hygiene/HYGIENE_DECISIONS.md` · **Waits:** Q-G-01, Q-A4-01, Q-A6C-02

```text
B5-2 — the canonical Design Configuration, DRAFT
Create the one PlantLibrary Design Configuration in SharedContracts design/ by import, as DRAFT 0.1.0, with the hand-written core-adjacent documents, the stack mappings for the four client stacks, and the ownership text amended.
Context: step B5-2 of the master rework runbook (§3, lane B5); rules: kickoff §2; the answers: Q-G-01, Q-A4-01, Q-A6C-02 (§Q); the evidence pack of B5-1 (by pointer: the commit §L row B5-1 records); the layout: AUDIT_design-kit-and-methodology_2026-10-13.md §7.1, §7.3, §7.4; the hygiene prerequisites: AUDIT_corpus-census-sharedcontracts_2026-10-13.md §7.3 last part (design/ catalogued, not a root; CLAUDE.md:31-34 and SCOPE.md:14-19 amended); the register rows RC-A4-* for the import and the examples folder; RC-A6C-05.
Where: the SharedContracts submodule on main, in place; one commit; the Kit is read-only (its tools run with outputs into design/ of this repository only).
Scope: the import into design/ (tokens.json, semantic-roles.json, banned-colors.json with BAN-02 scoped), CONFIGURATION.md (identity, status DRAFT, the Stacks table naming web-css, web-ts, compose, qt-qss), DESIGN_VERSION.md 0.1.0 with a Consumers line per stack naming the suite's adoption row, conduct-rules.md with this project's parameters (P-DS-08's accent share), decisions/DECISION_RECORD_<date>.md restating P-DS-01..10 and the template defaults as pending gate items, stacks/<stack>/mapping.md per the A9 audits' naming facts (no generated/ yet: emission is per client at B5-4..6), conformance/ seeded (literal_allowlist.txt, CONFORMANCE_MATRIX.md); the roundtrip report kept in scratch, not committed; the CLAUDE.md paragraph and the V1 package's SCOPE.md lines that say design-system artifacts are owned by Workspace SDA and read-only here (cited by their wording, since B2-3 shifts line numbers) amended so this repository owns design artifacts; one prose decision entry in hygiene/HYGIENE_DECISIONS.md (design/ catalogued as product documentation; next free id by grep) and, only if the emitters later write markdown under design/stacks, the generated exempt-tree line is left to B5-4. design-tokens/ stays at its path as the flat export (Q-A6C-02 (a)). Not here: BINDING (B5-3); any client; the gallery capture; any token value change beyond what the gate decides (none yet).
Read first: the §Q answers; the evidence pack; the audit sections; C:\Programmierung\Design_Template_Kit\template\TEMPLATE_SPEC.md §3 and the CONFIGURATION/DESIGN_VERSION templates under template\docs\ (read-only); the Kit's examples\plantlibrary-field-ledger\design\ as the round-tripped reference (read-only, never copied as a whole: the import regenerates it).
Write: design/**, the two amended files, the decision entry.
Constraints: sources read-only; no test, no build, no browser; the Kit's validator run with --no-write-back and its exit quoted (the 7 pairs still fail at DRAFT — expected); line endings: new files LF (the Configuration is machine-read), amended files as found; the SharedContracts verdict as at the commit before (zero violations; the held count as it then stands); no push.
Questions: proposed Q-B5-<nn> rows; continue.
If the context runs short: commit the core files that validate structurally, list the rest, stop; restart as B5-2-r2.
Done when: one commit; design/ holds the core, the documents, four mappings and conformance/; the validator reports schema 0 errors and the 7 known pairs; the final message names the commit and the D-id.
Commit line: rework: B5-2 - Design Configuration imported, DRAFT 0.1.0; design/ catalogued; D-<date>-<nn>
```

*Orchestrator note:* superproject line `rework: B5-2 - bump PlantLibrary_SharedContracts gitlink; ledger B5-2`; SharedContracts is B5-2's only writer until it ends (B4-1's and B3-4's SharedContracts commits are serialized before or after).
**Watch:** a Configuration pasted from the Kit's examples folder instead of imported; DRAFT strings inside hashed core files (the pilot paid a re-pin for that, F-A4-09); a write into `design-tokens/`.

#### `B5-3` — `G-DS`: the design gate; Configuration 1.0.0 BINDING

**Model · reasoning:** operator; Opus 5.5 · high records · **Route:** gate · **Where:** `PlantLibrary_SharedContracts` on `main` (in place) · **Precondition:** `B5-2` · **Writes:** `design/CONFIGURATION.md`, `DESIGN_VERSION.md`, `semantic-roles.json`/`tokens.json` (only the gate's value changes), `decisions/*`, `banned-colors.json` · **Waits:** — (all answered; the operator's advance answer "G-DS: all recommended, set A" is recorded in the register on Q-B5-01/03/04 and applies to every G-DS item of the evidence pack)

```text
B5-3 — G-DS, the design gate recorded
Record the operator's gate answers in the Configuration and raise it to 1.0.0 BINDING.
Context: step B5-3 of the master rework runbook (§3, lane B5); rules: kickoff §2; the answers this step records: Q-A4-02 (the seven pairs), Q-A9D-02 (ban scope), Q-A4-03 (the Kit pin), Q-A4-04 (DTI-05 ended, SDA batches superseded), quoted verbatim from §Q; the evidence pack B5-1; the Kit's DRAFT→BINDING workflow (C:\Programmierung\Design_Template_Kit\template\TEMPLATE_SPEC.md, the status workflow section, read-only).
Where: the SharedContracts submodule on main, in place; one commit.
Scope: the value changes the operator chose for the failing pairs, applied to the core files; banned-colors.json per Q-A9D-02; the decision record gaining the gate section with the operator's words; CONFIGURATION.md status BINDING; DESIGN_VERSION.md 1.0.0 with the changelog; the validator run with --no-write-back now exiting 0 (quoted); design-tokens/ regenerated from the Configuration only if the gate changed a value the flat export carries (the export tool, outputs into design-tokens/, diff quoted) — else untouched. Not here: emission (B5-4..6); any client file.
Read first: the §Q answers; the evidence pack; the Configuration as committed at B5-2.
Write: the Configuration files; design-tokens/ only under the condition stated.
Constraints: sources read-only; no test, no browser; the Kit's static tools only; LF for the Configuration; the verdict unchanged; no push.
Questions: an answer outside the options goes back to the register as the reading the orchestrator inserts; continue with the rest.
If the context runs short: commit what the operator settled, stop; restart as B5-3-r2.
Done when: one commit; status BINDING, version 1.0.0; validator exit 0; the final message names the commit and whether design-tokens/ changed.
Commit line: rework: B5-3 - G-DS recorded; Design Configuration 1.0.0 BINDING
```

*Orchestrator note:* the four answers arrive here verbatim from the register; if design-tokens/ changed, the Dashboard's generated CSS (`tokens.generated.css`) no longer equals the canon — a B6a-2 census fact, not a B5 fix.
**Watch:** BINDING without validator exit 0; a value changed that no gate answer names.

#### `B5-3.1` — component contracts, the Gallery page, `.gitattributes` (inserted 2026-10-13, Q-B5-05/Q-B5-07 (a))

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development\PlantLibrary_SharedContracts` on `main` (in place) · **Precondition:** `B5-3` · **Writes:** `design/contracts/components/**`, `design/gallery/index.html` and its generated files, `.gitattributes` · **Waits:** —

```text
B5-3.1 — the Configuration's component contracts and Gallery page, and the line-ending attributes
Give the BINDING Configuration its component contracts and its generated Gallery page so the clients' synced copies carry them, and pin the Configuration's machine-read files to LF with path-scoped attributes.
Context: step B5-3.1 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3.7); rules: kickoff §2; the answers: Q-B5-05 (a), Q-B5-07 (a), Q-A8-03 (a) (recorded 2026-10-13); the register rows RC-A4-21 (contracts/components) and RC-A4-22 (gallery/index.html); the Kit's template for component contracts and its gallery generator (C:\Programmierung\Design_Template_Kit\template\ and gallery\generate-gallery.mjs, read-only); the Configuration as B5-3 left it (by pointer: the §L row B5-3).
Where: the SharedContracts submodule on main, in place; one commit.
Scope: (1) design/contracts/components/ — one contract per Gallery component type the Kit's template set defines, with the Configuration's roles; (2) the Gallery page generated by the Kit's generator into design/gallery/ (static HTML; digests recorded as the generator does; no capture — baselines are DV-B5-01); (3) .gitattributes gaining `design/*.json text eol=lf` and `design/conduct-rules.md text eol=lf` (path-scoped only). Not here: a browser; any client; any token value.
Read first: the Kit's TEMPLATE_SPEC.md contracts section and gallery README; the two register rows; the Configuration.
Write: the files listed.
Constraints: sources read-only; the Kit's node tools only, outputs inside design/; no browser, no test; LF for design files; the SharedContracts verdict unchanged; no push.
Questions: proposed Q-B5-<nn> rows; continue.
If the context runs short: commit what validates, stop; restart as B5-3.1-r2.
Done when: the contracts and the Gallery page exist and the Kit's coverage check reports the component set complete (baselines not applicable); one commit; the final message gives the §L row and the commit the gitlink takes.
Commit line: rework: B5-3.1 - component contracts; Gallery page; design/ eol attributes
```

**Watch:** a capture attempted; a hand-written token value in a contract.

#### `B5-4` — Dashboard anchored

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development\PlantLibrary_Dashboard` on `main` (in place) · **Precondition:** `B5-3`, `B2-2`, `B7-2`, `B1-2` · **Writes:** `design/**` (synced copy + `conformance/`, `stacks/web-css/generated/`, `stacks/web-ts/generated/`), `scripts/design/**`, `.claude/.codex/.agents/.github` design skills, `.github/workflows/design-conformance.yml`, `CLAUDE.md`/`AGENTS.md` design block, `.gitattributes` (path-scoped), `DESIGN.md`, `.impeccable/design.json`, `hygiene/HYGIENE_DECISIONS.md` · **Waits:** Q-A8-03

```text
B5-4 — the Dashboard anchored to the Configuration
Install the Kit's anchoring into the Dashboard against the BINDING Configuration in the hybrid form: a synced copy of the Configuration under design/ with this client's own conformance/ pin, the web-css and web-ts artifacts emitted into design/stacks/, impeccable vendored, the design block written, the design skills installed.
Context: step B5-4 of the master rework runbook (§3, lane B5); rules: kickoff §2; the answers: Q-G-01, Q-A4-01, Q-A8-03 (§Q); the install order: C:\Programmierung\Design_Template_Kit\anchoring-kit\INSTALL.md (read-only); the facts: AUDIT_design-kit-and-methodology_2026-10-13.md §7.1, §7.2 (web-css, web-ts rows), §7.4; AUDIT_gui-current-state-dashboard_2026-10-13.md §7.7 and §0 items 5 and 8; AUDIT_skills-and-agents_2026-10-13.md §7.1 (impeccable row, RC-A1-11); AUDIT_git-structure_2026-10-13.md §7.6 (Dashboard row).
Where: the Dashboard submodule on main, in place; one commit (two if the installer and the emission are better separated).
Scope: the synced Configuration copy (the four core files and the documents from SharedContracts at its BINDING commit, by pointer) under design/, with conformance/CONSUMED_DESIGN.md pinning the Kit (relative path, version per Q-A4-03) and the Configuration (SharedContracts commit); the installer run with --with-impeccable; emit-stack for web-css and web-ts into design/stacks/<stack>/generated/; the drift, pin, literal and parity checks run and quoted; the design block landing above the roster heading (B2-2 wrote it) in CLAUDE.md and AGENTS.md (the installer writes both; the freeze guard treats the block as installer-owned); a path-scoped .gitattributes line (text eol=lf) for design/stacks/**/generated/* per Q-A8-03; the .github hook and workflow files; one decision entry (next free id) recording design/ as catalogued and design/stacks as a generated exempt tree only if it holds markdown. Not here: any src/ change (B6a); the alias layer (Q-A9D-04, B6a); generate-theme.mjs's fate (B6a); the gallery capture (deferred).
Read first: the §Q answers; INSTALL.md; the audit sections; the Dashboard CLAUDE.md as B2-2 left it.
Write: the files listed.
Constraints: sources read-only; the Kit's node tools only, no npm install, no build, no browser, no test; a design check that exits non-zero is quoted, never patched around; CRLF/LF as the bytes rule says (generated artifacts LF under the attribute line); the parity checkers (harness and Kit) green; the Dashboard verdict unchanged; no push.
Questions: proposed Q-B5-<nn> rows; continue.
If the context runs short: commit the installer's output if its pin check passes, list the rest, stop; restart as B5-4-r2.
Done when: the pin check, drift check and Kit parity check pass; the literal check's report is quoted as a census fact (not a gate); one or two commits; the final message names them and the D-id.
Commit line: rework: B5-4 - Dashboard anchored - Kit <version>, web-css+web-ts emitted, impeccable
```

*Orchestrator note:* superproject line `rework: B5-4 - bump PlantLibrary_Dashboard gitlink; ledger B5-4`; the freeze guard (B7-2) must already exempt the four Kit folders under `.codex/skills/` and the design block in `AGENTS.md`.
**Watch:** an installer run against SharedContracts' folder instead of the client's copy (the pin would hash the wrong files); the design block landing below the hygiene block; a `.gitattributes` line wider than the generated paths.

#### `B5-5` — PyApp anchored

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development\PlantLibrary_PyApp` on `main` (in place) · **Precondition:** `B5-3`, `B2-2`, `B7-2`, `B1-2` · **Writes:** as `B5-4` for PyApp; `design/stacks/qt-qss/generated/tokens.py`; the adapter decision in `design/stacks/qt-qss/mapping.md` · **Waits:** Q-A9P-01

```text
B5-5 — PyApp anchored to the Configuration
Install the anchoring into PyApp in the hybrid form, emit the qt-qss artifact, and record the adapter decision; the adapter itself and every GUI change belong to B6c.
Context: step B5-5 of the master rework runbook (§3, lane B5); rules: kickoff §2; the answers: Q-G-01, Q-A4-01, Q-A9P-01 (§Q); INSTALL.md (read-only); the facts: AUDIT_design-kit-and-methodology_2026-10-13.md §7.2 (qt-qss row) and the "what that means for PyApp" paragraph; AUDIT_gui-current-state-pyapp_2026-10-13.md §7.7 (the shape that fits, the six emitter requirements, the 124 composed role keys); AUDIT_git-structure_2026-10-13.md §7.6 (PyApp row: pyproject.toml and .gitignore are mixed — Edit tool only).
Where: the PyApp submodule on main, in place; one commit.
Scope: the synced Configuration copy and pin; the installer without --with-impeccable (PyApp already carries 3.8.0; the installer's parity check must accept the existing copies or the reason is quoted as a Kit finding); emit-stack for qt-qss into design/stacks/qt-qss/generated/tokens.py; a Python AST parse of the emitted module quoted; design/stacks/qt-qss/mapping.md stating the adapter route per Q-A9P-01, the flattening rule for role names, the units rule, the 124 composed keys as an open design decision for B6c; the literal check configured for app/gui/**/*.py and resources/styles/*.qss with design_tokens.py and tokens.py allow-listed; the design block above the roster heading; the decision entry. Not here: theme_utils.py, design_tokens.py, any QSS (B6c); the harness's refusal of resources/styles (Q-A9P-04, B7/B6c).
Read first: the §Q answers; INSTALL.md; the audit sections; PlantLibrary_PyApp/app/gui/theme_utils.py lines 1-110 (read, not changed).
Write: the files listed.
Constraints: as B5-4; no app import, no app launch.
Questions: proposed Q-B5-<nn> rows; continue.
If the context runs short: commit the installer's output if its pin check passes, list the rest, stop; restart as B5-5-r2.
Done when: pin, drift and Kit parity pass; tokens.py parses; mapping.md records the adapter route; one commit; the final message names it and the D-id.
Commit line: rework: B5-5 - PyApp anchored - Kit <version>, qt-qss emitted, adapter route recorded
```

**Watch:** an emitted `tokens.py` placed where the harness's unmapped-path refusal catches a later batch (record it as a deferred row, not a fix); a hand-transcribed value anywhere.

#### `B5-6` — AndroidApp anchored; compile deferred

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development\PlantLibrary_AndroidApp` on `main` (in place) · **Precondition:** `B5-3`, `B2-2`, `B7-2`, `B1-2` · **Writes:** as `B5-4` for AndroidApp; `design/stacks/compose/generated/Tokens.kt`; `design/stacks/compose/mapping.md` · **Waits:** Q-A9A-01, Q-A4-05

```text
B5-6 — AndroidApp anchored to the Configuration; the Compose artifact emitted but not wired
Install the anchoring into AndroidApp in the hybrid form, emit Tokens.kt where Q-A9A-01 places it, record what the Kit must still emit for Compose, and defer the compile.
Context: step B5-6 of the master rework runbook (§3, lane B5); rules: kickoff §2 (rule 1: no Gradle task); the answers: Q-G-01, Q-A4-01, Q-A9A-01, Q-A4-05 (§Q); INSTALL.md (read-only); the facts: AUDIT_design-kit-and-methodology_2026-10-13.md §7.2 (compose row), F-A4-02, F-A4-03; AUDIT_gui-current-state-androidapp_2026-10-13.md §7.7 (what the theme expects, what the Kit emits, the six requirements (i)-(vi), the compile-free checks table).
Where: the AndroidApp submodule on main, in place; one commit.
Scope: the synced Configuration copy and pin; the installer (impeccable already present); emit-stack for compose into design/stacks/compose/generated/Tokens.kt; mapping.md recording the placement, the package-name gap, the missing TextStyle/weights/ColorScheme emission and the ARGB ban spellings as Kit findings for the Q-A4-05 session (by id), and the hand-adapter plan for B6b; the literal check noted as blind to Kotlin (a Kit finding, quoted); no Gradle source-set change (B6b, after the compile is possible); the design block; the decision entry. Not here: Theme.kt, Color.kt or any Kotlin (B6b); settings.gradle.kts; any Gradle invocation.
Read first: the §Q answers; INSTALL.md; the audit sections.
Write: the files listed.
Constraints: as B5-4; no Gradle; the deferred-validation row for the compile proposed in the final message (DV-A9A-a by id).
Questions: proposed Q-B5-<nn> rows; continue.
If the context runs short: commit the installer's output if its pin check passes, list the rest, stop; restart as B5-6-r2.
Done when: pin, drift and Kit parity pass; Tokens.kt exists unwired; mapping.md records the Kit gaps; one commit; the final message names it, the D-id and the deferred row.
Commit line: rework: B5-6 - AndroidApp anchored - Kit <version>, compose emitted unwired, gaps recorded
```

**Watch:** `Tokens.kt` added to a Gradle source set (nothing may compile it in Phase B); a ban list without the ARGB spellings.

#### `K-1` — Design Template Kit session (inserted at `R-4.1` under Q-A4-05's reading)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\Design_Template_Kit` on branch `pl/kit-gaps-2026-10` (from `master`, created by the orchestrator) · **Precondition:** `B5-3` · **Writes:** the Kit only; never a TARGET repository · **Waits:** —

```text
K-1 — the Design Template Kit gaps PlantLibrary needs closed
Close, on a Kit branch and under the Kit's own contribution rules, the gaps the PlantLibrary analysis recorded against Kit 1.7.0, each with its own commit and test, and leave the branch for the Kit owner's merge and version step.
Context: step K-1 of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3.7), read by that absolute path and never edited; this session is outside the PlantLibrary program's write scope: it writes the Kit and nothing else, and the program's rule that sources are read-only still binds every other step; the Kit's rules are C:\Programmierung\Design_Template_Kit\CONTRIBUTING.md and its tests; the gaps, by id: AUDIT_design-kit-and-methodology_2026-10-13.md §2 (the Kit defects marked "record only") and EVIDENCE_design-gate-pack_2026-10-13.md (the two record-only notes and Q-B5-01's cause).
Where: cwd C:\Programmierung\Design_Template_Kit on branch pl/kit-gaps-2026-10; master and every other branch untouched; nothing under C:\Programmierung\SW_Development is written.
Scope: (1) check-literals: Kotlin and Qt spellings (Color(0xAARRGGBB), N.dp/N.sp, QColor(r,g,b)); (2) banned-colors: ARGB aliases honoured by the product scan, and BAN scope honoured outside design/; (3) the compose emitter: typography weights and TextStyle, a package-name option, an emitter test; (4) the qt-qss emitter: a header carrying the Configuration name and version, a documented role-name flattening rule, numeric dimensions, shadows kept, an emitter test; (5) import-flat-tokens: an --input path; export-flat-tokens: a write mode that regenerates the flat layout; (6) a changelog entry and the version step the Kit's rules require, left uncommitted to master. Not here: any PlantLibrary file; any Conductor file; a Kit test that needs a browser is left as a documented follow-up.
Read first: CONTRIBUTING.md; anchoring-kit/checks/check-literals.mjs; anchoring-kit/emitters/emit-stack.mjs; tools/import-flat-tokens.mjs and export-flat-tokens.mjs; the Kit's existing emitter tests; the two PlantLibrary files named above (read-only).
Write: the Kit files the scope names, on the branch.
Constraints: the Kit's own unit tests for emitters and checks are the Kit's contract and may run here (this session is not a PlantLibrary lane; the one test slot belongs to the Conductor, so no browser test and no long run — node unit tests only); no npm install; no push; line endings as the Kit keeps them.
Done when: the branch carries one commit per gap with its test green; the final message lists the commits, the Kit version proposed, and what PlantLibrary's B5-6, B6b-8 and B5-3 (Q-B5-01) can now consume once the Kit owner merges and tags; the final message gives the §L row.
Commit line: kit: <gap> - <summary>
```

*Orchestrator note:* the branch is created by the orchestrator before launch; the Kit's merge to `master` and its tag are the Kit owner's (the operator) — the program re-pins only after that; §L row `K-1`.
**Watch:** a Kit edit that changes an existing emitter's output for the pilot (Conductor) without a version step; any write outside the Kit.

#### `B5-7` — design-adoption retired; six skill cells repointed to design-gate

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master`; then Dashboard, AndroidApp, PyApp and Workspace on `main` (serial, in place) · **Precondition:** `B5-4`, `B5-5`, `B5-6`, `B1-2` · **Writes:** superproject `.claude/skills/design-adoption/SKILL.md` (pointer), `.agents/README.md`; three packages' `TASK_CHECKLIST.md` (skill cells) and `STATE.md`; the Workspace's mirrored skill folder (pointer) · **Waits:** Q-G-07

```text
B5-7 — design-adoption retired in favour of design-gate
Replace the house gate by a pointer now that every client is anchored, and repoint the six rows that name it through plan-batch's amendment rule.
Context: step B5-7 of the master rework runbook (§3, lane B5); rules: kickoff §2 (rule 4: the skill cell is a row cell — changed only as a recorded plan amendment; validation cells untouched); the answer: Q-G-07 (§Q); the evidence: AUDIT_design-kit-and-methodology_2026-10-13.md §7.6; AUDIT_skills-and-agents_2026-10-13.md §7.1 (design-adoption row, F-A1-15); AUDIT_batch-packages_2026-10-13.md §7.3 (the six rows WD-V1-DS-01/06, AN-V1-DS-01/05, PY-V1-DS-01/03).
Where: superproject first (one commit), then the three clients (one commit each), in place.
Scope: the superproject skill folder reduced to a SKILL.md pointer ("retired <date>, Q-G-07; use design-gate; the P-DS map lives in SharedContracts design/decisions/, the adoption rows in DESIGN_VERSION.md Consumers") and the bridge README row flipped; the .codex twin untouched (frozen); per client, the six rows' skill cell set to design-gate (plus the row's other skill where one is named) with one dated STATE decision line per package. Not here: any row status; any validation cell; the Workspace copy of the skill (B1-2 mirrored it: give it the same pointer in the same step if it exists there).
Read first: the §Q answer; the audit sections; each package's TASK_CHECKLIST.md rows named.
Write: the files listed.
Constraints: sources read-only; no test; CRLF as found; the census after each package reads 0 errors; the PyApp plan-contract hash unchanged (the skill cell is in TASK_CHECKLIST.md — confirm with the parser, quote before and after; if the hash moves, stop PyApp and propose the B8 re-intake item instead); parity green; no push.
Questions: proposed Q-B5-<nn> rows; continue.
If the context runs short: commit the complete repositories, stop; restart as B5-7-r2.
Done when: four commits (or three plus the PyApp stop reported); no live row names design-adoption; the final message lists commits and hashes.
Commit line: rework: B5-7 - design-adoption retired; <n> rows repointed to design-gate
```

**Watch:** a PyApp cell edit that moves the plan-contract hash; the `.codex` twin edited.

#### `B5-8` — Conductor readiness rows 1–7 per anchored client

**Model · reasoning:** Sonnet 5.5 · high · **Route:** check · **Where:** `C:\Programmierung\SW_Development` on `master` · **Precondition:** `B5-4`, `B5-5`, `B5-6` · **Writes:** `rework/EVIDENCE_design-readiness_<date>.md`, `rework/INDEX.md` · **Waits:** —

```text
B5-8 — the Kit's Conductor readiness rows 1-7, statically, per client
Run the Kit's readiness check against each anchored client with instance 2's data directory read-only, and record rows 1-7; row 8 (one dispatched UI batch) is a deferred row.
Context: step B5-8 of the master rework runbook (§3, lane B5); rules: kickoff §2; the tool: C:\Programmierung\Design_Template_Kit\anchoring-kit\conductor\check-conductor-readiness.mjs and CONDUCTOR_READINESS_CHECKLIST.md (read-only); AUDIT_design-kit-and-methodology_2026-10-13.md §7.7 (its row).
Where: cwd C:\Programmierung\SW_Development; writes the superproject only; the three clients and C:\Programs\AI_Orchestrator_2 are read.
Scope: three runs of the readiness tool, one per client, each given the client's suite folder, the instance-2 data directory C:\Programs\AI_Orchestrator_2 (read-only) and the client's implementation/System_V1_Implementation package, outputs quoted; any red row explained against the step that owns it; the role overrides the Kit expects in the instance's data directory listed as a B8 owed item if absent (never written here). Not here: any write outside the evidence file; any instance call.
Read first: the checklist; the tool's usage.
Write: the evidence file and its INDEX line.
Constraints: read-only everywhere else; no test; no push.
Questions: proposed Q-B5-<nn> rows; continue.
If the context runs short: commit what ran, stop; restart as B5-8-r2.
Done when: three quoted runs; one commit; the final message names it and the deferred row for row 8.
Commit line: rework: B5-8 - design readiness rows 1-7 - 3 clients
```

**Watch:** a run that writes into the instance's data directory.

### 3.8 Lane B8 — Conductor onboarding alignment

#### `B8-1` — bindings recorded obsolete; ledger and §N corrections; PyApp `.gitignore` and `graphify-out/`

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master`; then `PlantLibrary_PyApp` on `main` · **Precondition:** `B4-1` · **Writes:** `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` §L and §N; PyApp `.gitignore` · **Waits:** — (Q-A2-03 and Q-A6P-04 answered 2026-10-13)

```text
B8-1 — the onboarding runbook brought up to the measured facts
Record that the instance-2 bindings are obsolete (Q-G-02 and Q-A8-02, answered 2026-10-13), correct the onboarding ledger's two miscounts, discharge the §N notes that need no operator, and clean PyApp's .gitignore (the four dead lines and the graphify sanction) together with its graphify-out/ folder.
Context: step B8-1 of the master rework runbook (§3, lane B8); rules: kickoff §2; the facts: AUDIT_batch-packages_2026-10-13.md §7.5 (what the bindings require; nothing since 2026-09-16 invalidates them), §7.6 (the six §N notes and what B8 does for each), its "Also owed in B8" lines (F-A7-01: AndroidApp ten will_run; F-A7-04: instance 2's config lacks max_scope_targets and soak); AUDIT_git-structure_2026-10-13.md §7.4 (what must stay stable); B4-1's commit (by pointer) for GC-6082.
Where: superproject first (one commit), then PyApp (one commit), in place; the instance's config.yaml is read once, its database and API never.
Scope: in the onboarding runbook — §L step 2b's AndroidApp count corrected; §L step 6 gains the config facts; §N rows GC-6082 (B4-1 moved SY1-B07; the attended-batch marker is B4-2's — write "marker at B4-2"), GC-2006 (pointer to the deferred register and the hand-back), GC-2431 (nothing; owner named), GC-2437 (closed by this step's PyApp commit), GC-7053 (closed by B4-2 — write "pending B4-2" if it has not landed), GC-1132 (operator act: B8-3); step 8's §L line reads "superseded by the Conductor's proposal A (project contract and validation profiles); harness half todo there" only once Q-A2-03 is answered, else left; a dated line under §L step 5 recording that the six bindings are obsolete per the operator's words of 2026-10-13 (quoted from the register rows Q-G-02 and Q-A8-02), that instance 2 is neither resumed nor given intake and its store stays untouched, and that no re-verification is owed; §L step 6's hold noted as lapsed for the same reason. PyApp: .gitignore lines 11-14 and the graphify-out sanction line (c48aa17) removed with the Edit tool (the file is mixed-eol), and the untracked, git-ignored PlantLibrary_PyApp/graphify-out/ folder deleted by this session (verify ignored and untracked first; a short script, never a shell rm in a compound command). Not here: any instance call; any package file.
Read first: the audit sections; the runbook §L and §N; C:\Programs\AI_Orchestrator_2\config.yaml lines 500-520 (read-only).
Write: the two files.
Constraints: sources and the instance read-only; no test; the runbook is CRLF in the working tree — append and edit with its own endings, never a rewrite; the three held names it cites are untouched (the kit constraint); the superproject verdict zero violations; no push.
Questions: proposed Q-B8-<nn> rows; continue.
If the context runs short: commit the superproject, stop; restart as B8-1-r2 for PyApp.
Done when: two commits; §L and §N read as stated; the final message names them.
Commit line: rework: B8-1 - onboarding ledger and notes updated; bindings re-verified statically
```

**Watch:** a `git mv` or rename of anything the runbook cites; an instance REST call "just to check".

#### `B8-2` — §N notes closed by `B4`; step 8 superseded; §L step 6 facts

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development` on `master` · **Precondition:** `B4-5` · **Writes:** the onboarding runbook §L and §N · **Waits:** Q-A2-03

```text
B8-2 — the onboarding runbook after B4
Close the §N rows B4 settled (GC-7053 by the pointer stubs, GC-6082's marker), record B4-5's package proof under §L step 5, and flip step 8 to superseded per Q-A2-03.
Context: step B8-2 of the master rework runbook (§3, lane B8); rules: kickoff §2; the answer: Q-A2-03 (§Q); the evidence: B4-2 and B4-5 commits (by pointer: the §L rows), AUDIT_harnesses-and-scripts_2026-10-13.md §7.6 (proposal A, ob-25), AUDIT_batch-packages_2026-10-13.md §7.6.
Where: superproject on master, in place; one commit.
Scope: the §N rows' state text; §L step 5's proof line; §L step 8's line; a §L step 7 note that the Server port now waits the Conductor's profile rollout (Q-A2-01/Q-A2-03). Not here: step 6's hold; any package.
Read first: the runbook §L/§N; the two commits' messages; the audit sections.
Write: the runbook.
Constraints: as B8-1.
Questions: proposed Q-B8-<nn> rows; continue.
If the context runs short: commit, stop; restart as B8-2-r2.
Done when: one commit; the final message names it.
Commit line: rework: B8-2 - onboarding notes closed by B4; step 8 superseded
```

**Watch:** as `B8-1`.

#### `B8-3` — GC-1132: the operator's review of `IMPORTABLE_SOURCE_TREES` recorded

**Model · reasoning:** operator; Sonnet 5.5 · high records · **Route:** operator · **Where:** `PlantLibrary_PyApp` on `main`; then the superproject · **Precondition:** `R-4.1` · **Writes:** PyApp `implementation/System_V1_Implementation/validation/ONBOARDING_harness-port.md`; onboarding runbook §L step 4 · **Waits:** Q-A2-02

```text
B8-3 — GC-1132 discharged
Record the operator's review of the one table entry PlantLibrary_PyApp/scripts/harness/regression_scope.py:273 (IMPORTABLE_SOURCE_TREES = app/, backend/) against PyApp's importable source trees, as the §N note asks.
Context: step B8-3 of the master rework runbook (§3, lane B8); rules: kickoff §2; the answer: Q-A2-02 (§Q, the operator's words); AUDIT_batch-packages_2026-10-13.md §7.6 row GC-1132; AUDIT_harnesses-and-scripts_2026-10-13.md (the port facts).
Where: PyApp on main, in place (one commit), then the superproject (one commit).
Scope: one dated line in ONBOARDING_harness-port.md with the operator's words and the outcome; "reviewed" appended to §L step 4 of the onboarding runbook; a note that a re-port must carry the table again. Not here: any change to regression_scope.py (a code edit is a batch).
Read first: the §Q answer; the two files' tails.
Write: the two files.
Constraints: no test; line endings as found; no push.
Done when: two commits; the final message names them.
Commit line: rework: B8-3 - GC-1132 reviewed; onboarding step 4 marked reviewed
```

**Watch:** an edit to the script itself.

### 3.9 Lane C1 — hand-back, and the orchestrator's boundaries

#### `C1-1` — deferred validations planned

**Model · reasoning:** Opus 5.5 · high · **Route:** plan · **Where:** each suite on `main` (serial, in place) · **Precondition:** `R-4.3` · **Writes:** each package's `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md` (new rows and batches only) · **Waits:** —

```text
C1-1 — the deferred validations become the first batches of Phase C
For every package that has deferred-validation rows, one plan-batch act that turns them into rows and batches with their validation cells as the register states them, sequenced first.
Context: step C1-1 of the master rework runbook (§3, lane C1); rules: kickoff §2 (rule 4: plan-batch's schema; existing validation cells untouched — new rows carry the deferred validations; rule 1 ends here: no validation runs in this step either); the register: rework/REGISTER_deferred-validations_2026-10-13.md (every row in state deferred or proposed with this package in its Repository column); the hand-back shape: AUDIT_batch-packages_2026-10-13.md §7.4 (H.1 columns, DV ids).
Where: one suite at a time, in place on main, one commit per suite; the plan-batch skill of that suite is the procedure (/plan-batch <suite folder> <package> with the register rows as its input); the superproject is read only.
Scope: per package, new rows for the deferred validations (one row per DV id or one per natural group, each row's validation cell = the register's "What would be run" and skill), a batch per attended/unattended split placed first in plan order (with the out-of-band marker where attended), anchors to the deferred register by id, a STATE decision; the register's rows flip planned (<batch key>) in the orchestrator's flip commit (the final message lists id → key). Not here: PyApp's plan contract beyond what plan-batch's amendment rule allows while PY1-B08 is held — if the act would move it, stop PyApp and propose the re-intake item.
Read first: the register; the package's five files; this suite's plan-batch skill in full (its self-review checklist is the proof of the package shape, run through the batch-plan-auditor agent in the foreground).
Write: the package files.
Constraints: no test; CRLF as found; the census reads 0 errors after each package; the PyApp hash rule as stated; no push.
Questions: proposed Q-C1-<nn> rows; continue.
If the context runs short: commit the complete packages, stop; restart as C1-1-r2.
Done when: every package with DV rows carries them as rows; the final message lists commits and id → key pairs.
Commit line: rework: C1-1 - deferred validations planned - <n> rows, <m> batches
```

**Watch:** a validation cell narrowed to make a row "fit"; a batch placed behind work it is meant to validate.

#### `C1-2` — the hand-back section; `SUITE_HANDOFFS.md` reshaped; the backlog register pointed

**Model · reasoning:** Opus 5.5 · high · **Route:** session (paste) · **Where:** `C:\Programmierung\SW_Development` on `master`; `PlantLibrary_Workspace` on `main` · **Precondition:** `C1-1` · **Writes:** this file §H (hand-back); Workspace V1 `SUITE_HANDOFFS.md`, `CONTEXT_INDEX.md` · **Waits:** Q-G-05, Q-A7-07

```text
C1-2 — the hand-back section
Write §H of this runbook (H.1 run-next table from the census, H.2 cross-suite order, H.3 operator decisions on the path, H.4 backlog pointer, H.5 binding rules and environment pointers, H.6 instance 2, H.7 archived sequencers), and reshape SUITE_HANDOFFS.md to carry H.1 as the row-maintained living table.
Context: step C1-2 of the master rework runbook (§3, lane C1); rules: kickoff §2; the answers: Q-G-05, Q-A7-07 (§Q); the shape and the unique contents to carry: AUDIT_batch-packages_2026-10-13.md §7.4; the census at this commit (the superproject's static package census, bytecode writing disabled, quoted); the backlog register of B3-2 (by pointer); the deferred register after C1-1.
Where: the superproject (this file) and, for SUITE_HANDOFFS.md and the CONTEXT_INDEX.md read order, the Workspace; two commits.
Scope: §H written in full with the H.1 columns of the audit (Order, Package, Batch, Classification, Route, Model, Waits on, Deferred validations); the Wave C preference, the SV1-B00 early-handoff note and "SY1-B07 before SY1-B05" in H.2; the security sign-offs, VGAP-020 and the open Q- rows in H.3; H.6 from the onboarding register's step-5 record with the S-2 hold cited by pointer; H.7 as the plan for B3-6; SUITE_HANDOFFS.md reduced to a header, H.1's table and the binding-rules recap, with a dated STATE line in the V1 package; CONTEXT_INDEX.md's read order starting at SCOPE.md. Not here: the archive moves (B3-6); any row.
Read first: the audit §7.4; §Q; the census output; the backlog and deferred registers; SUITE_HANDOFFS.md and IMPLEMENTATION_PLAN.md §4-§7 (to carry, not copy).
Write: this file's §H; the two Workspace files.
Constraints: no test; this file is LF, the package files CRLF; no runner named in §H; the superproject verdict zero violations; no push.
Questions: proposed Q-C1-<nn> rows; continue.
If the context runs short: commit §H as far as written with "[C1-2-r2]" markers, stop; restart as C1-2-r2.
Done when: §H complete; SUITE_HANDOFFS.md carries H.1; two commits; the final message names them.
Commit line: rework: C1-2 - hand-back section H.1-H.7; SUITE_HANDOFFS reshaped
```

**Watch:** a copied row; a run-next order that contradicts a Requires token.

#### `C1-3` — resume blocks per suite

**Model · reasoning:** Opus 5.5 · high · **Route:** session (paste) · **Where:** `C:\Programmierung\SW_Development` on `master` · **Precondition:** `C1-2` · **Writes:** this file §H.8 · **Waits:** —

```text
C1-3 — the resume blocks
Write one two-line resume block per suite into §H.8 of this runbook, each naming the suite folder and the batch key H.1 puts first for it, with the precondition check in the orchestrator note.
Context: step C1-3 of the master rework runbook (§3, lane C1); rules: kickoff §2; the shape: AUDIT_runbook-conventions_2026-10-13.md §7.6 (the resume block, the batch route's two lines); §H.1 (by pointer).
Where: the superproject, in place; one commit.
Scope: six blocks (every suite runs out of band until a Conductor instance is bound anew — the instance-2 bindings are obsolete per Q-G-02/Q-A8-02; H.6 records that); each block's orchestrator note carries the key and the clean-tree check. Not here: any run.
Read first: §H.1 and §H.3; the audit section.
Write: §H.8 of this file.
Constraints: no proof surface in a block (the row's validation cell owns it); no runner named; LF; no push.
Done when: six blocks; one commit; the final message names it.
Commit line: rework: C1-3 - resume blocks per suite
```

**Watch:** a block with a placeholder left inside.

#### `C1-4` — the hand-back HANDOVER

**Model · reasoning:** Fable 5.1 · high · **Route:** procedure · **Where:** `C:\Programmierung\SW_Development` on `master` · **Precondition:** `C1-3`, `B3-6` · **Writes:** `handovers/HANDOVER_master-rework-hand-back_<date>.md`, `handovers/INDEX.md` · **Waits:** —

The orchestrator writes the HANDOVER in the kit's continuation shape: what was done per lane with commit lines; the state at hand-over (seven heads, held names, open owed items of §3b); open items by owner; a continuation fence (scope, read-first, constraints, done-when, commit line) that names §H.1 as the run-next and `C1-3`'s first block as Phase C's first act. Commit line: `rework: C1-4 - hand-back HANDOVER`.

#### `R-4.1` … `R-4.4` — wave boundaries

**Model · reasoning:** Fable 5.1 · high · **Route:** procedure · **Where:** `C:\Programmierung\SW_Development` on `master` · **Block:** procedure: §3a (the ritual) · **Writes:** gitlink-and-flip commits, register rows, §Q, §O, §1 when due.

Each boundary runs §3a's ritual in order and ends with the push list in its §L Note and two lines to the operator. `R-4.1` closes wave 1 and opens wave 2 only for the steps whose `waits` are answered; `R-4.2` opens wave 3 (`B6`); `R-4.3` opens `C1`; `R-4.4` precedes `R-5`.

#### `R-5` — close

**Model · reasoning:** Fable 5.1 · high · **Route:** procedure · **Precondition:** `R-4.4` · **Writes:** §0 "Closed", §1 final, §L complete, `rework/INDEX.md` line `history`, `handovers/HANDOVER_master-rework-close_<date>.md`.

The orchestrator closes the runbook per §2 rule 9 and prints the Phase C resume prompt (§H.8's first block with its note) to the operator.

## 3a. What may run beside what

**1. The occupancy rule.** One writer per repository at a time, in place. A second lane on the same repository gets a worktree (`git -C <repo> worktree add C:\Programmierung\SW_Development_wt\<repo>-<lane> -b rework/<lane> main`, admin dir under `<repo>\.git\worktrees\`), but only for a step that neither reads nor checks sibling repositories (Q-A8-01): every step of this program reads a sibling (the superproject's registers, SharedContracts' Configuration, the Kit by relative path) or writes the superproject, so **no step in §3 takes a worktree**; concurrency comes from steps writing different repositories, and same-repository steps serialize in the order of §3.2. The superproject is never written from a worktree. The superproject's in-place writer is either one superproject lane step or the orchestrator's boundary commits, never both at once. At most four write sessions beside the orchestrator; one Fable session at a time; read-only subagents unlimited. A new worktree, if ever needed, requires C: free ≥ 20 %. Never during the program: any initializing `git submodule update`, `absorbgitdirs`, `deinit`, or a superproject worktree.

**2. The lane table.**

| Lane | Steps | Repositories written | Checkout | Runs beside | Never beside |
|---|---|---|---|---|---|
| `B7` | `B7-1`, `B7-2`, `B7-3` | super; (B7-2) all seven; (B7-3) PyApp, Server | in place | `B4-1` (suites) | another superproject writer; `B1` before `B7-2` |
| `B2` | `B2-1`…`B2-3` | super; then the six suites, serial | in place | `B3-2` when `B2-1` is done; `B5-2` (SharedContracts) only when `B2-3` is not on SharedContracts | `B1` (same files' neighbours: `.claude` vs `CLAUDE.md` are different files, but the freeze orders them) |
| `B1` | `B1-1`…`B1-3` | super; then the six suites | in place | `B3-4`/`B4-2` on suites `B1-2` has finished | any `.claude` edit by another lane |
| `B3` | `B3-1`…`B3-6` | super; Workspace; five suites | in place | `B4-1`, `B5-2` on other repositories | `B4` on the same suite in the same window |
| `B4` | `B4-1`…`B4-5` | the six suites (seven packages) | in place | superproject steps | `B3-4` on the same suite |
| `B5` | `B5-1`…`B5-8` | super (evidence); SharedContracts; the three clients | in place | `B2-3`'s Server/Workspace steps | `B4-1`/`B3-4` on SharedContracts during `B5-2`/`B5-3` |
| `B6` | pointed file | the three clients; SharedContracts (contracts, gallery pages) | in place | the other two clients' steps, except at the SharedContracts-writing steps | `B5-7` on the same client |
| `B8` | `B8-1`…`B8-3` | super (`onboarding/`); PyApp | in place | suite steps other than PyApp | another superproject writer |
| `C1` | `C1-1`…`C1-4` | the suites; super | in place | — (wave 4 is serial) | everything else |

**3. The repository matrix** (`W` writes in place · `r` reads · `—`; static, never a status).

| Repository | B7 | B2 | B1 | B3 | B4 | B5 | B6 | B8 | C1 |
|---|---|---|---|---|---|---|---|---|---|
| superproject | W | W | W | W | r (evidence W) | W (evidence) | r | W | W |
| Workspace | W (B7-2) | W | W | W | W | W (B5-7) | r | r | W |
| PyApp | W | W | W | W | W | W | W | W | W |
| AndroidApp | W (B7-2) | W | W | W | W | W | W | r | W |
| Dashboard | W (B7-2) | W | W | W | W | W | W | r | W |
| Server | W | W | W | W | W | r | r | r | W |
| SharedContracts | W (B7-2) | W | W | W | W | W | W | r | W |

**4. The waves.** Each wave starts when its event holds and ends in its `R-4.<k>` step.

1. **Wave 1** — starts at `event:R-3-committed`. Steps: superproject queue in this order, one at a time — `B7-1`, `B5-1`, `B3-1`, `B8-1` (its PyApp half after `B4-1`); beside the queue once `B7-1` is committed: `B4-1` (Server → Workspace → SharedContracts); the operator session (§O) on the open set. Closes at `R-4.1`: register re-read, steps released, §O refreshed, push list (super; Server, Workspace, SharedContracts, PyApp).
2. **Wave 2** — starts at `event:wave-1-merged` and `event:Q-answered` per step. Order of the superproject queue, strictly serial: `B2-1` → `B3-2` → (after `B2-2`/`B2-3`) `B7-2` → `B1-1` → `B1-3` → `B7-3` (its superproject half) → `B8-3` (its superproject half) → `B4-5` (after the `B4` suite steps) → `B5-7` (its superproject half) → `B5-8` (after the anchorings) → `B8-2` (after `B4-5`). The chains below are one-writer queue order among ready steps per repository, not preconditions: a step whose own preconditions and waits hold may run when its repository is free, and the orchestrator keeps at most four write sessions live, releasing in the order listed. Suite steps, each repository serial: Dashboard `B2-2` → `B7-2` → `B1-2` → `B5-4` → `B5-7`; AndroidApp `B2-2` → `B7-2` → `B1-2` → `B5-6` → `B5-7`; PyApp `B2-2` → `B7-2` → `B1-2` → `B7-3` → `B5-5` → `B5-7` → `B8-3`; Server `B2-3` → `B7-2` → `B1-2` → `B7-3` → `B4-2` → `B4-4` → `B3-4` → `B3-5`; SharedContracts `B2-3` → `B7-2` → `B1-2` → `B5-2` → `B5-3` → `B4-2` → `B4-4` → `B3-4`; Workspace `B2-3` → `B7-2` → `B1-2` → `B4-2` → `B4-3` → `B4-4` → `B3-3` → `B3-5`; Dashboard/AndroidApp/PyApp also `B4-2` → `B4-4` → `B3-4` after `B1-2`; `B4-5` when every `B4` suite step is done. Closes at `R-4.2`.
3. **Wave 3** — opened 2026-10-13 at `R-4.2`; starts at `event:wave-2-merged` and `B5-4` done. `B6a` (Dashboard) in full; `B6c` (PyApp) starts after `B5-5`, its SharedContracts-writing steps after `B6a`'s; `B6b` (AndroidApp) planning steps after `B5-6`, its implementation waits Q-A4-05. Closes at `R-4.3`.
4. **Wave 4** — `C1-1` → `C1-2` → `B3-6` → `C1-3` → `C1-4`; closes at `R-4.4`; then `R-5`.

**5. The boundary ritual** (every `R-4.<k>`, in order): (1) drain — no write session of this program running in any repository with wave work, every main checkout clean, instance 2 untouched; (2) re-read the question register; flip waiting steps to `todo` or `retired`; update §Q and §O in the boundary's first commit; (3) merge each worktree branch, if any (none planned): `merge --ff-only`, `worktree remove`, `branch -d`, `worktree prune`; an `INDEX.md` conflict resolves as a union; (4) one superproject commit per step in step order carrying the gitlink at that step's own commit (`git update-index --cacheinfo 160000,<sha>,<repo>` for earlier steps, `git add <repo>` for the last), the §L flip and the step's proposed register rows, each preceded by the superproject hygiene verdict; (5) refresh §1 if three days old or a lane closed; rewrite §O for the new open set; read C: free space; (6) push (Q-G-03's answer of 2026-10-13: "You are allowed to push." — the orchestrator pushes at every boundary, no lane session does): plain `git push` of each submodule whose `main` moved, in the order SharedContracts, Server, Dashboard, AndroidApp, PyApp, Workspace, then the containment check `branch -r --contains` per gitlink, then the superproject; nothing forced; the pushed heads go into the `R-4.<k>` Note and two lines to the operator; (7) open the next wave and flip `R-4.<k>` done.

## 3b. Owed items

| # | Item | Source | Discharged at (step) | Status |
|---|---|---|---|---|
| 1 | GC-1132 — operator review of PyApp `IMPORTABLE_SOURCE_TREES` | onboarding §N | `B8-3` | open |
| 2 | GC-2006 — AndroidApp has no test sources; "unit tests pass" is not evidence | onboarding §N | `B8-1` (pointer), `C1-2` H.1 | open |
| 3 | GC-6082 — D7 reorder (`SY1-B07` before `SY1-B05`) and attended markers | onboarding §N | `B4-1`, `B4-2`, `B8-1` | open |
| 4 | GC-2431 — SharedContracts version drift (`SC-SYNC-REGEN-01`) | onboarding §N | never here (a batch); `B8-1` records the owner | open |
| 5 | GC-2437 — PyApp `.gitignore` dead lines | onboarding §N | `B8-1` | open |
| 6 | GC-7053 — `DRIVER_SCRIPT.md` instructs `_ACT_STATE.md` | onboarding §N | `B4-2`, `B8-2` | open |
| 7 | M-8 closing pass | repo-hygiene §L | `B3-1` | done except the Kit changelog (item 17) |
| 8 | M-9 hold releases (five suites; the Workspace set after K-7) | repo-hygiene §L | `B3-4` done 2026-10-13 for the five suites; Workspace set: after the Kit session (`K-2`) | open — Workspace set only |
| 9 | K-7 Kit session (exempt tree cannot retire on rename) | `handovers/FINDING_…_2026-09-17.md` | `K-2` done 2026-10-13 (kit 0.3.0, `d5b9742`); `B3-8` re-pins all seven and releases the Workspace set | done — kit side |
| 10 | Onboarding step 6 hold (S-2, instance 2 is staging) | onboarding §L | lapsed: the instance-2 bindings are obsolete (Q-G-02, Q-A8-02 readings, 2026-10-13); `C1-2` H.6 records it | lapsed |
| 11 | The Conductor's `OP-RB` copy into `PlantLibrary_Workspace` | `AUDIT_runbook-conventions` F-A5-06 | operator (Q-A5-01); `B1-1` records | open |
| 12 | Kit session for Compose/Qt emission, Kotlin literal patterns, ARGB bans, TextStyle, the import tool's input path and an export write mode | `AUDIT_design-kit-and-methodology` §2; `EVIDENCE_design-gate-pack` | `K-1` done 2026-10-13 (Kit 1.11.0 @ `612e634`); F-A4-10/F-A4-11 remain the Kit owner's design decisions | done — K-1 |
| 13 | `graphify-out/` removal from disk (superproject, PyApp) | `A6a`, `A6c` | `B8-1` (PyApp, 45 MB) and `B3-2` (superproject, 282 MB) deleted them 2026-10-13 | done |
| 14 | The end-of-wave pushes (three submodule commits already unpushed) | `A8` F-A8-03 | the orchestrator at each `R-4.<k>` (Q-G-03 reading, 2026-10-13) | open — first push at `R-4.1` |
| 15 | Readiness row 8 (one dispatched UI batch per anchored client) and the instance's role overrides | `A4` §7.1 | Phase C; `B5-8` records | open |
| 16 | `PyApp` re-intake at `PY1-B08` if any step moves its plan contract | `A7` F-A7-09 | lapsed with the bindings (Q-A7-04, Q-A8-02 readings, 2026-10-13) | lapsed |
| 17 | M-8's Kit changelog commit (hygiene runbook §16) | `B3-1` | `K-2` done 2026-10-13 (the ten lessons in the 0.3.0 changelog) | done |
| 19 | The Kit's two Conductor role overrides, to be deployed to whichever Conductor instance is bound next (none today) | `B5-8` | Phase C, at the next Conductor bind | open |
| 18 | GitHub repository variables `DESIGN_KIT_REPOSITORY` and `DESIGN_KIT_REF` (`v1.11.0`) for the design-conformance workflow in Dashboard, PyApp and AndroidApp; until set, that workflow goes red on push | `B5-4` (Q-B5-13) | operator, at any time before the next push (the orchestrator cannot set repository variables) | open |

## Q. Operator questions — mirror of the register

The register of record is `REGISTER_operator-questions_2026-10-13.md` (nine program rows `Q-G-01`…`09`, the lane rows, and the orchestrator's `Q-R-01`; its columns include Source, When and Reading; the kickoff's "options and recommended (a)" live there in full, this mirror carries the (a) text and the ids). This mirror lists the program rows in full and the lane rows by id and waiting steps; states and answers are flipped here in the same commit as the register. (a) is always the recommendation; † marks a recommendation the orchestrator made where lanes disagreed.

**What changes if you answer all recommended** (ten lines): the superproject keeps six submodules in their current form; no session pushes, you push at each boundary; Phase B runs linters, formatters, type checks and the Kit's static checks and nothing that builds or launches; the stale sequencers are archived after the hand-back section replaces them, `Todo.md` stays untouched with its live ideas copied into a register; the K-7 Kit session is queued for you; design-adoption retires once the three clients are anchored; the Dashboard is implemented first, PyApp after its static proof, Android after the Kit session; Codex is frozen block-aware (outside the installer-owned blocks); the Configuration lives in SharedContracts with a synced copy and its own pin per client; the seven failing contrast pairs are settled at the design gate; `DRIVER_SCRIPT.md` becomes a pointer stub in place (no suite archive folders except Workspace's).

| ID | Question (short) | Recommended | Waits | State | Answer (verbatim, date) |
|---|---|---|---|---|---|
| `Q-G-01` | Where the Design Configuration lives | (a) SharedContracts `design/`, in the hybrid form of Q-A4-01 (canonical there; synced copy + own `conformance/` per client) | `B5-2`, `B4-3`, `B6` | answered | "all other recommended." — 2026-10-13 18:05 UTC, §O session 2d91d072; (a) |
| `Q-G-02` | Repository structure | (a) keep superproject + six submodules, form unchanged (old-form, uninitialized; no init/update/absorbgitdirs/deinit during the program) | `B3`, `B4`, `B8` | answered | "We can keep repo structure but dont need to keep instance 2 bindings. They are obsolete." — 2026-10-13 18:05 UTC, §O session 2d91d072; (a); bindings clause: Reading at Q-A8-02 |
| `Q-G-03` | Pushing | (a) no session pushes; operator pushes at each boundary, submodules first | all write lanes | answered | "You are allowed to push." … "Do everything you can on your own. Reduce the operator steps to a minimum." … "all other recommended." — 2026-10-13 18:05 UTC, §O session 2d91d072; (a), the boundary push done by the orchestrator (Reading in the register) |
| `Q-G-04` | Mechanical checks allowed in Phase B | (a) linters, formatters, type checks, Kit static checks only (no Gradle, no web build) | `B5`, `B6`, `B7` | answered | "all other recommended." — 2026-10-13 18:05 UTC, §O session 2d91d072; (a) |
| `Q-G-05` | Stale sequencers | (a) archive `IMPLEMENTATION_PLAN.md`/`WORKSPACE_STATE.md`/`V1_IMPLEMENTATION_SEQUENCE.md` after §H replaces them; `Todo.md` ideas to a register (see Q-A6S-04 on "emptied") | `B3-2`, `B3-3`, `B3-6`, `C1-2` | answered | "all other recommended." — 2026-10-13 18:05 UTC, §O session 2d91d072; (a) |
| `Q-G-06` | Kit finding K-7 | (a) record, hold, queue a Kit session (run by the orchestrator as `K-2`) | `K-2`, `B3-8` | answered | "Q-G-06: a (run yourself)" — 2026-10-13 19:07 UTC, orchestrator chat; (a) with the Reading in the register |
| `Q-G-07` | The design-adoption skill | (a) retire for design-gate after `B5` anchors the three clients, leave a pointer | `B5-7` | answered | "all other recommended." — 2026-10-13 18:05 UTC, §O session 2d91d072; (a) |
| `Q-G-08` | GUI rework order | (a) all three planned; Dashboard implemented first, PyApp after its static proof, Android after the Kit session | `B6` | answered | "all other recommended." — 2026-10-13 18:05 UTC, §O session 2d91d072; (a) |
| `Q-G-09` | Codex | (a) freeze as the Conductor did, but block-aware: `.codex/**` and `AGENTS.md` outside the installer-owned blocks, digests from the freeze commit | `B7-2`, `B1`, `B2` (banner) | answered | "all other recommended." — 2026-10-13 18:05 UTC, §O session 2d91d072; (a) |

**Operator answers and directives, 2026-10-13 18:05 UTC, §O session 2d91d072:** "You are allowed to push." · "We can keep repo structure but dont need to keep instance 2 bindings. They are obsolete." · "What are K-7 kit questions?" · "Do everything you can on your own. Reduce the operator steps to a minimum." · "all other recommended." Reading: every act a session can do itself moves from the operator to a session or to the orchestrator (pushes at each boundary, the `graphify-out/` deletions, the Design-Kit session launch); decisions stay the operator's (open `Q-…` rows and the gate steps). Instance 2's bindings are no longer kept (Q-A8-02's Reading). `Q-G-06` was asked back and stays open; `Q-B7-01` and `Q-B7-02` were registered (`fbdf813`) after the questions were put and stay open. To reconcile at `R-4.1` (raised when the rows were put, not by the answer): Q-A6V-04 (a) archives `run_next_batch.py` to `archive/scripts/` while `B3-5`'s block removes three scripts by `git rm`; Q-A6W-01 (a) lists `SUITE_HANDOFFS.md` for the Workspace archive while Q-A7-07 (a) keeps it live.

**Lane rows** (ids → the steps that wait; options and reasons in the register):

| Lane | Rows | Waiting steps |
|---|---|---|
| A1 | `Q-A1-01` run-batch §6 shape · `Q-A1-02` third-party skills · `Q-A1-03` tracked settings · `Q-A1-04` PlantLibrary-only skills mirrored into the suites whose rows name them | `B1-1`, `B1-3`, `B1-1`, `B1-2` |
| A2 | `Q-A2-01` when to re-port the harness · `Q-A2-02` GC-1132 review · `Q-A2-03` step 8 superseded by proposal A · `Q-A2-04` parity checker extended to suites · `Q-A2-05` living-docs standard (hold) · `Q-A2-06` kit scratch module in the suites | (`B7` records), `B8-3`, `B8-1`/`B8-2`, (`B7-1` does (a)), `B2` (held section), `B7-3` |
| A3 | `Q-A3-01` block-aware freeze · `Q-A3-02` Testing block line 10-12 · `Q-A3-03` where session rules live · `Q-A3-04` `haiku/luna` sentence · `Q-A3-05` PyApp `.claude/CLAUDE.md` · `Q-A3-06` living documentation · `Q-A3-07` drained-boundary rule | `B7-2`, `B2-1` (sentence), `B2-1`…`B2-3`, `B2-1` (sentence), `B2-2`, `B2` (section), `B2-1` (sentence) |
| A4 | `Q-A4-01` hybrid Configuration form · `Q-A4-02` the 7 failing pairs · `Q-A4-03` Kit pin · `Q-A4-04` DTI-05 ended, SDA superseded · `Q-A4-05` Kit session for Compose/Qt · `Q-A4-06` workspace location and binding · `Q-A4-07` re-skin or restructure † superseded by the per-client rows `Q-A9D-01`, `Q-A9A-07`, `Q-A9P-09` · `Q-A4-08` round-6 render tools deferred | `B5-2`, `B5-3`, `B5-3`, `B5-3`, `B5-6`/`B6b`, `B6*-1`, —, (`B6` records) |
| A5 | `Q-A5-01` hold `OP-RB`'s copy · `Q-A5-02` keep `PROMPTS_` (R-3 proceeds with (a)) · `Q-A5-03` one-line answers · `Q-A5-04` chat asking | `B1-1`, —, §O, — |
| A6a super | `Q-A6S-01` top-level `archive/` · `Q-A6S-02` the three onboarding holds stay · `Q-A6S-03` graphify leftovers · `Q-A6S-04` `Todo.md` untouched, ideas copied · `Q-A6S-05` spent track files leave after M-8/M-9 | `B3-6`, —, `B3-2`, `B3-2`, `B3-6` |
| A6b Workspace | `Q-A6W-01` root `archive/` for retired organs · `Q-A6W-02` `V1_IMPLEMENTATION_SEQUENCE.md` in the set † folded into Q-G-05 · `Q-A6W-03` live-package anchors not retargeted · `Q-A6W-04` restate the two methodology trees · `Q-A6W-05` SDA's fate † folded into Q-A7-06 | `B3-3`, —, —, `B3-3`, — |
| A6c PyApp | `Q-A6P-01` `implementation/archive/` † superseded: no suite archive needed under Q-A7-05 (a) · `Q-A6P-02` DRIVER_SCRIPT fate † superseded by Q-A7-05 · `Q-A6P-03` release `PYAPP_V1_PROPOSAL` at M-9 · `Q-A6P-04` graphify sanction · `Q-A6P-05` `improvements.md` hold permanent · `Q-A6P-06` `GUI/` live until census · `Q-A6P-07` generated docs kept | —, —, `B3-4`, `B3-2`/`B8-1`, —, —, — |
| A6d AndroidApp | `Q-A6A-01` archive layout † superseded by Q-A7-05 · `Q-A6A-02` release at M-9 · `Q-A6A-03` code-group hold stays · `Q-A6A-04` prose fixes scope · `Q-A6A-05` impeccable not declared · `Q-A6A-06` pre-restructure paths served by mapping | —, `B3-4`, —, `B2-2`, —, — |
| A6e Dashboard | `Q-A6D-01` archive DRIVER_SCRIPT † superseded by Q-A7-05 · `Q-A6D-02` release `DASHBOARD_V1_PROPOSAL` · `Q-A6D-03` release the two pinned `docs/` holds | —, `B3-4`, `B3-4` |
| A6f Server | `Q-A6V-01` DRIVER_SCRIPT fate † superseded by Q-A7-05 · `Q-A6V-02` release `SERVER_V1_PROPOSAL` · `Q-A6V-03` no code edits; deferred row · `Q-A6V-04` retire `run_next_batch.py` · `Q-A6V-05` fix docs links · `Q-A6V-06` setup guide not authored here | —, `B3-4`, (`B3-5` records), `B3-5`, `B3-5`, — |
| A6g SharedContracts | `Q-A6C-01` no `archive/` · `Q-A6C-02` `design/` source, `design-tokens/` the flat view · `Q-A6C-03` GC-7053 † superseded by Q-A7-05 · `Q-A6C-04` release the hold at M-9 · `Q-A6C-05` stale platform mappings superseded after B5 | —, `B5-2`, —, `B3-4`, (`B5-4`…`6` record) |
| A7 | `Q-A7-01` `haiku/luna` cells · `Q-A7-02` out-of-band marker · `Q-A7-03` `already_done` readings · `Q-A7-04` PyApp plan contract stays · `Q-A7-05` DRIVER_SCRIPT as pointer stub · `Q-A7-06` SDA superseded · `Q-A7-07` living run-next table in `SUITE_HANDOFFS.md` · `Q-A7-08` B6 versus functional screen rows | `B4-4`, `B4-2`, `B4-4`, `B4-4`, `B4-2`, `B4-3`, `C1-2`, `B6*-7` |
| A8 | `Q-A8-01` worktrees only for single-repository steps (none planned) · `Q-A8-02` instance 2 stays paused until C1 · `Q-A8-03` path-scoped `.gitattributes` at B5 · `Q-A8-04` D-ids pre-assigned per step · `Q-A8-05` `absorbgitdirs` deferred | —, —, `B5-4`, (§3 notes), — |
| B1 | `Q-B1-04` a standing deliverable root for the operator-run review skills: (a) a general root `reviews/` by D-entry and allowlist entry at `B3-6` — answered (a) 2026-10-13 · `Q-B1-03` who fills the checker's `SUITE_EXTRA_SKILLS` table: (a) the orchestrator in the B1-2 flip commit — answered (a) 2026-10-13, done · `Q-B1-01` `ui-ux-pro-max` and `webapp-testing` have no recorded upstream, pin or licence: (a) `B1-3` records them in the README's provenance table — answered (a) 2026-10-13 · `Q-B1-02` the B7-1 inventory in `scripts/harness/README.md` still says "B7-2 switches it off": (a) refreshed at `B7-3` — answered (a) 2026-10-13 | `B1-3`, `B7-3` |
| B7 | `Q-B7-05` Server's scratch-gate copy has no script yet: (a) keep, it stops at step 0 until the Server harness port — answered (a) 2026-10-13 · `Q-B7-06` Server `validation/README.md` does not list `KNOWN_FAILURES.md`: (a) the next Server package writer (`C1-1`) adds the row with a STATE line — answered (a) 2026-10-13 · `Q-B7-07` PyApp's ledger prose still describes the central-ledger fallback: (a) at the PyApp re-port (Q-A2-01, Phase C) — answered (a) 2026-10-13 · `Q-B7-03` where the superproject's AGENTS.md banner sits (the file opens heading-less): (a) line 1 — answered (a) 2026-10-13 · `Q-B7-04` AGENTS.md normalised before digesting with the marker blocks removed whole and blank runs collapsed: (a) keep (blank-line-only edits go undetected; the design block insert stays green) — answered (a) 2026-10-13 · `Q-B7-01` same-name suite skill copies the parity check lists but does not compare (PyApp `gui-validation` pointer; six Workspace copies, `verify-stack` diverged): (a) leave to `B1-2` under Q-A1-04 · `Q-B7-02` a per-suite `.codex` compare now: (a) no, the freeze covers it — both answered (a) by the orchestrator 2026-10-13 | `B1-2`, `B7-2` |
| B4 | `Q-B4-06` five driver stubs' owner rows still say "not carried — proposed for SCOPE.md": (a) `C1-2` repoints them to Standing invariants — answered (a) 2026-10-13 · `Q-B4-07` the three clients' CONTEXT_INDEX "Design system authority" rows still point at the SDA package: (a) `B6a-1`, `B6c-1`, `B6b-1` repoint them — answered (a) 2026-10-13 · `Q-B4-08` the new Traceability tables cite two held Workspace files: (a) the next Workspace hygiene D-entry (`B3-8`) adds the citers to the hold notes — answered (a) 2026-10-13 · `Q-B4-01` the Workspace record cites `BATCH_PLAN.md:133` for a held file now at line 176: (a) fix the cite in the next Workspace hygiene D-entry — answered (a) by the orchestrator 2026-10-13 · `Q-B4-02` driver-only suite rules (contract-decision files, contract-version lines, screenshot naming, report lines) now readable only at the pointer commit: (a) copy each into that package's `SCOPE.md` standing invariants in `B4-4` with a decision line — answered (a) by the orchestrator 2026-10-13 · `Q-B4-03` live text still pointing at drivers or `_ACT_STATE.md` (AndroidApp and Workspace suite READMEs, Workspace V1 `TASK_CONTEXT.md:47,98`, V1 `README.md:56,99`): (a) READMEs to `B3-5`, the two anchor lines to `C1` as anchor amendments — answered (a) by the orchestrator 2026-10-13 · `Q-B4-04` SDA-DEC-01..05 recorded as overtaken in SDA `STATE.md` by `B4-3`: (a) `B5-3` records the five in the Configuration's decision record only — answered (a) 2026-10-13 · `Q-B4-05` SDA `SCOPE.md:11-12` still says the package binds after SDA-DEC: (a) leave, informational — answered (a) 2026-10-13 | `B3-3`, `B4-4`, `B3-5`/`C1`, `B5-3`, — |
| B2 | `Q-B2-01` no step applied Q-A3-02 (a) to the Testing block's "Sonnet/Terra worker" sentence: (a) a one-sentence step `B2-1.1` after `B1-1` — answered (a) 2026-10-13 · `Q-B2-02` the two remaining Q-A6A-04 items (AndroidApp `docs/README.md:3`, the dated line for `docs/module_architecture.md`): (a) folded into `B3-7` — answered (a) 2026-10-13 · `Q-B2-03` the three AndroidApp README files B2-2 edited beyond the block's Write line (per the orchestrator's note): (a) recorded as B2-2's writes in the ledger — answered (a) 2026-10-13 | `B2-1.1`, `B3-7`, — |
| B3 | `Q-B3-08` the ambiguous `Todo.md` lines and the off-repository backup item: (a) keep as cited by line in the backlog register §4; the operator re-adds a live line — answered (a) 2026-10-13 · `Q-B3-09` the dead `.gitignore:11-12` graphify lines: (a) removed in `B3-6` — answered (a) 2026-10-13 · `Q-B3-04` the B3-3 fence's stale commit-line clause: (a) fence fixed, clause carried by `B3-6` — answered (a) 2026-10-13 · `Q-B3-05` Workspace `docs/local_development.md:7` · `Q-B3-06` Workspace V1 `DRIVER_SCRIPT.md:27` and `SUITE_HANDOFFS.md:5` · `Q-B3-07` Server README derivation links, SV-DOMAIN-01 PyApp paths, SV-B07 link: (a) a follow-up text sweep — all answered (a) 2026-10-13 and folded into the inserted step `B3-7` · `Q-B3-03` Renamed-table form for the M-9 releases: (a) in-place flips of the existing Renamed rows — answered (a) 2026-10-13 · `Q-B3-01` who flips the hygiene runbook's §3 row M-8: (a) the orchestrator, in this flip commit — answered (a) 2026-10-13 · `Q-B3-02` the Kit version for the pilot lessons (item 17) and K-7: (a) one minor release 0.3.0 with both, then a re-pin of all seven as an M-9 pre-step; (b) a patch 0.2.2 first — open, tied to `Q-G-06` | —, `K-2` |
| B6c | `Q-B6c-05` contracts record behaviour differing from the page contracts: (a) today's tree stays; defects become `B6c-4` gap rows classified at `B6c-7`; page-contract absences to `B6c-6` — answered (a) 2026-10-14 · `Q-B6c-06` dialogs over dialogs, modal validation, native destructive confirms: (a) record the first as deviations, classify the last two as rows — answered (a) 2026-10-14 · `Q-B6c-07` category hues with no role: (a) neutral chips, one series per section, tag colours as user data, no Configuration change — answered (a) 2026-10-14, design reading listed for veto · `Q-B6c-08` missing link/menu/status/readiness roles: (a) adapter aliases only; readiness via C-16 on `states.*` — answered (a) 2026-10-14, listed for veto · `Q-B6c-09` sentence-case copy and integer margins in scope: (a) yes — answered (a) 2026-10-14 · `Q-B6c-10` a desktop Add-flow page contract: (a) `PageContract_add.md` in SharedContracts at `B6c-6` — answered (a) 2026-10-14, **a SharedContracts addition, listed for veto** · `Q-B6c-03` plan-batch's vocabulary has no `superseded`: (a) retired phase rows read `deferred` with a STATE line naming Q-B6a-02, in all three clients — answered (a) 2026-10-13 · `Q-B6c-04` `check-literals.mjs --paths` refuses directories: (a) rows name files or use `--paths-from`; Kit finding — answered (a) 2026-10-13 · `Q-B6c-01` the form of `B6c-5`…`B6c-7` under the re-skin answer: (a) keep the steps and gates in re-skin form (06a forward surface and settings only; 06b records today's view tree plus desktop page mockups as targets; 06c/06d as written) — answered (a) 2026-10-13 · `Q-B6c-02` the new `.qss` harness route selects only the two sentinels, not `tests/test_design_tokens.py`: (a) a table-driven asset→consumer route owned by `B6c-8`'s first QSS batch with its own DV row — answered (a) 2026-10-13 | `B6c-5`, `B6c-8` |
| B6a | `Q-B6a-10` the Configuration has no token for border width (45 literals), opacity, scrim or breakpoints: (a) propose border-width, opacity and scrim tokens/roles as a Configuration addition in `B6a-6`'s serialized SharedContracts version step; layout literals onto `size.*`; only the misc remainder allow-listed at `B6a-7` — answered (a) 2026-10-14, **a Configuration content change, listed for veto** · `Q-B6a-07` where the `/login` page contract lives: (a) workspace WSC-02 now, written into the Configuration's `contracts/pages/` at 06b (`B6a-6`) — answered (a) 2026-10-13 · `Q-B6a-08` the web's "offline" state-quartet member: (a) "connection lost — showing last loaded data", server actions disabled with the reason; offline editing stays deferred (SYS-GOAL-DEFER-001) — answered (a) 2026-10-13 · `Q-B6a-09` the approved artifact TGT-02 referenced by URL and version, not copied — answered (a) 2026-10-13 · `Q-B6a-04` the Kit's web-css stack emits `[data-theme="LIGHT"/"DARK"]` while the app writes lowercase: (a) when the stack is wired the app writes the Configuration's theme names and the old dark selectors migrate in the same wave; Kit finding — answered (a) 2026-10-13 · `Q-B6a-05` the Kit's whole-repo literal walk reads `references/`, `tests/` and the old generated theme pair: (a) `audit_exclude.txt` for the non-authored trees at `B6a-7`/`8`, the generated pair retired via Q-A9D-04 — answered (a) 2026-10-13 · `Q-B6a-06` `eslint .` walks `.tmp/`: (a) ignore it at the next lint-config touch — answered (a) 2026-10-13 · `Q-B6a-01` `eslint .` leaves 4 errors in the Kit-installed `scripts/design/run-all.mjs`: (a) `B6a-2` ignores `scripts/design/**`, a Kit finding recorded — answered (a) 2026-10-13 · `Q-B6a-02` the workspaces disagree on prompt 00 step 9 (Dashboard empty, AndroidApp 16 phase rows): (a) packages stay empty until `-7`, the ledger is the only status for 01–06d; AndroidApp's phase rows retired `superseded` at `B6b-3`, PyApp aligned at `B6c-2` — answered (a) 2026-10-13, supersedes `Q-B6b-04` · `Q-B6a-03` Dashboard `implementation/README.md` names only the V1 package: (a) `B6a-2` adds the section — answered (a) 2026-10-13 | `B6a-2`, `B6b-3`/`B6c-2`, `B6a-2` |
| B6b | `Q-B6b-08` prompts 05/06's six outputs folded into the rubric, one comparison file and the gap map's §4/§5: (a) accepted deviation at `B6b-5` — answered (a) 2026-10-14 · `Q-B6b-09` launcher drawables carry non-canon greens and 4× `108dp`: (a) recolour in the theme batch, allowlist only the viewport sizes — answered (a) 2026-10-14 · `Q-B6b-10` 98 `Text("…")` literals, `strings.xml` holds only `app_name`: (a) backlog finding `UB-17`, not a design gap — answered (a) 2026-10-14 · `Q-B6b-05` the operation count rule (adapter counts `fun` + `Flow` vals; A9 counted functions only): (a) keep 65/51 with the correction recorded — answered (a) 2026-10-13 · `Q-B6b-06` prompt 01's four inventory files folded into one report: (a) accept as a recorded workspace deviation at `B6b-3` — answered (a) 2026-10-13 · `Q-B6b-07` three dead repository operations: (a) a finding for the V1 package owner (`UB-15`), not the migration — answered (a) 2026-10-13 · `Q-B6b-01` the harness package tables count the three `Design_Migration_V1` workspaces as unclassified: (a) the orchestrator lists each as live in the flip commit that lands it — answered (a) 2026-10-13 · `Q-B6b-02` the Kit's own review owes a removal of `.github/hooks/impeccable.json` (K-12) that Q-B5-22 just added: (a) keep until the Kit stops writing it — answered (a) 2026-10-13 · `Q-B6b-03` AndroidApp `implementation/README.md` still says two packages: (a) `B6b-2` adds the workspace row — answered (a) 2026-10-13 · `Q-B6b-04` the three workspaces differ in shape (Dashboard 0 rows, AndroidApp 16 phase rows): (a) leave; the `-7` plan acts decide — answered (a) 2026-10-13 | —, Kit, `B6b-2`, `B6*-7` |
| B5 | `Q-B5-23` Workspace V1 `SKILLS.md:192` still registers design-adoption as live: (a) a Workspace plan amendment at `C1-2` flips it to design-gate with a dated STATE line — answered (a) 2026-10-13 · `Q-B5-21` the readiness tool reads the prose "Columns" line as the checklist header and scans zero rows (row 6 vacuous): (a) a Kit finding; the validation cells are rewritten at `B6*-7b` — answered (a) 2026-10-13 · `Q-B5-22` AndroidApp lacks `.github/hooks/impeccable.json` (row 4): (a) `B6b-1` adds the Kit's hook file — answered (a) 2026-10-13 · `Q-B5-15` the Kit's parity check fails on impeccable's per-runtime builds in PyApp and AndroidApp: (a) record as a Kit finding, accept exit 1 for impeccable only — answered (a) 2026-10-13 · `Q-B5-16` PyApp's and AndroidApp's `mapping.md` are ahead of the canonical copies: (a) a SharedContracts step syncs them back (`B5-3.3`) — answered (a) 2026-10-13 · `Q-B5-17` PyApp's hand-written DESIGN.md replaced by the emitted one: (a) `B6c-1`/`B6c-2` recover the valid prose into the Configuration or GUI/, repoint citers, swap CLAUDE.md's document command — answered (a) 2026-10-13 · `Q-B5-18` PyApp's root sentinel and the harness's unmapped `design/**`: (a) the first B6c writer adds both with Q-A9P-04 — answered (a) 2026-10-13 · `Q-B5-19` the extra `/DESIGN.md eol=lf` line: (a) keep — answered (a) 2026-10-13 · `Q-B5-20` AndroidApp's DESIGN.md and design.json: (a) at `B6b` with AN-V1-DS-02 — answered (a) 2026-10-13 · `Q-B5-12` the Dashboard's lint config probably reaches the vendored skill folders: (a) `B6a-1` adds ignores for `.claude`, `.codex`, `.agents`, `.github` and a prettier ignore before the first lint leg — answered (a) 2026-10-13 · `Q-B5-13` the new design-conformance workflow needs two repository variables: (a) the operator sets them before the next push — open as owed item 18; red CI accepted until then · `Q-B5-14` the Dashboard `CLAUDE.md` "Design context" section is stale: (a) `B6a-1` repoints it at `design/CONFIGURATION.md`; AGENTS.md stays frozen — answered (a) 2026-10-13 · `Q-B5-09` the canonical matrix has no component rows (coverage 0/23) and two Map cells plus the P-DS-08 cell still read "not yet present": (a) `B5-3.2` seeds 23 rows and fixes the cells — answered (a) 2026-10-13 · `Q-B5-10` C-02 Slider and C-23 Execution timeline composed by no PlantLibrary page: (a) `not_applicable` in the matrix, contracts kept — answered (a) 2026-10-13 · `Q-B5-11` `contracts/` and `gallery/` would check out CRLF under autocrlf: (a) path-scoped `eol=lf` lines here and in the clients — answered (a) 2026-10-13 · `Q-B5-08` the stale "pending at G-DS" cell in `design/stacks/compose/mapping.md:108`: (a) pointed at the decision record's section D at `B5-3.1` — answered (a) 2026-10-13 · `Q-B5-05` path-scoped `.gitattributes` lines for `design/`: (a) at `B5-3.1` — answered (a) 2026-10-13 · `Q-B5-06` three SharedContracts package lines still name SDA as the design owner: (a) `B4-4` records the STATE decision and repoints them — answered (a) 2026-10-13 · `Q-B5-07` `contracts/components/` and the Gallery page have no owning step: (a) the inserted `B5-3.1` — answered (a) 2026-10-13 · `Q-B5-01` how `design-tokens/` follows a gate value change (the Kit's export tool writes only a report): (a) `B5-3` hand-edits the flagged flat values and proves 0 diffs by round trip · `Q-B5-02` what is byte-equal in a client's synced copy: (a) core, `DESIGN_VERSION.md`, `decisions/`, `contracts/`, `gallery/`, the client's own mapping; each client's `CONFIGURATION.md` lists its own stacks — answered (a) by the orchestrator 2026-10-13 · `Q-B5-03` accept the Template defaults as design facts: (a) at `G-DS` · `Q-B5-04` who lands Q-A9D-02's four amendments: (a) `B5-3` (notes, bans), `B6a-7` (DS-06), `B6a-8` (drift checker) | `B5-3`, `B5-2`/`B5-4`…`6`, `B5-3`, `B5-3`/`B6a-7`/`B6a-8` |
| B8 | `Q-B8-01` what is left of PyApp's graphify sanction (the allowlist entry in `tests/test_repo_hygiene.py:45-47`, two STATE/evidence lines): (a) the next PyApp writer removes the entry with a dated STATE line — answered (a) 2026-10-13, folded into `B3-7` | `B3-7` |
| R | `Q-R-01` may a `B6*-8` session implement rows in Phase B and leave them at the status the plan-batch set allows for unvalidated work until Phase C runs the named validation: (a) yes, with a dated STATE line per row naming its deferred row; (b) no — implementation waits for Phase C | `B6a-8`, `B6c-8`, `B6b-8` |
| A9a Dashboard | `Q-A9D-01` restructure · `Q-A9D-02` ban scope (BAN-02) · `Q-A9D-03` DS-06/DS-01 superseded by gap rows · `Q-A9D-04` alias layer then rename · `Q-A9D-05` Phase C screenshot source · `Q-A9D-06` route drift after IA | `B6a-1`, `B5-3`, `B6a-7`, `B6a-8`, (`C1-1` records), `B6a-6` |
| A9b AndroidApp | `Q-A9A-01` `Tokens.kt` placement · `Q-A9A-02` `AN-V1-DS-05` fate · `Q-A9A-03` Kotlin literal checks interim · `Q-A9A-04` SDA-DEC recording and the icon change · `Q-A9A-05` routes and tab order · `Q-A9A-06` workspace and pin location † folded into Q-A4-06 · `Q-A9A-07` restructure or re-skin | `B5-6`, `B6b-7`, `B6b-8`, `B5-3`, `B6b-6`, —, `B6b-1` |
| A9c PyApp | `Q-A9P-01` adapter route · `Q-A9P-02` `PY-V1-DS-03` absorbed · `Q-A9P-03` "Follow system setting" · `Q-A9P-04` unpark `.qss` in the harness · `Q-A9P-05` missing icon and cwd-relative url() · `Q-A9P-06` ban scope † folded into Q-A9D-02 · `Q-A9P-07` design targets · `Q-A9P-08` close SDA-DEC-02 · `Q-A9P-09` re-skin | `B5-5`, `B6c-7`, `B6c-8`, `B6c-8`, `B6c-8`, —, `B6c-3`, `B5-3`, `B6c-1` |

**Lane rows answered 2026-10-13 18:05 UTC (§O session 2d91d072):** every lane row in the table above and `Q-R-01` resolve to (a) on "all other recommended.", except `Q-B7-01` and `Q-B7-02` (open, see above). Readings in the register on `Q-A1-01`, `Q-A3-07`, `Q-A4-05`, `Q-A4-06`, `Q-A6P-04`, `Q-A6S-03`, `Q-A7-04`, `Q-A8-02`; the same words are recorded as the operator's GC-1132 review (`Q-A2-02`) and as the release words of `Q-A6D-02` and `Q-A6D-03`.

**What a non-(a) answer changes** (program rows; a retired step counts as met in every later precondition):

| Answer | Effect on the steps |
|---|---|
| `Q-G-01` (b) per client | `B5-2` retired; three Configurations: `B5-4`…`6` each import the canon; `B6` IA/mockup writes go per client; R2 of the Kit spec broken (recorded) |
| `Q-G-02` (b) consolidate | the program stops after wave 1; a restructure runbook is written first (instance 2 rebound, pins re-anchored) |
| `Q-G-03` (b) lanes push | §2 rule 4 gains a push line per step; the operator's boundary push list retired |
| `Q-G-04` (b) compiles allowed | `B5-6`/`B6b` gain a Gradle compile step; the Dashboard `tsc -b` stays; the deferred rows for compiles flip to Phase B steps |
| `Q-G-05` (b) keep and refresh | `B3-6` retired; `C1-2` refreshes `IMPLEMENTATION_PLAN.md` §4-§7 instead of §H.4/H.7; `B3-2`'s register still written |
| `Q-G-06` (b) work around | no clean form exists (every census lane): the orchestrator inserts a FINDING step and asks again |
| `Q-G-07` (b) keep both | `B5-7` retired; `B2-2` adds a rule naming which gate fires when |
| `Q-G-08` (b) all in parallel | `B6b-8` loses its wait on Q-A4-05 and gains a compile deferred row; SharedContracts serialization unchanged |
| `Q-G-09` (b) remove mirrors | `B7-2` retired; a `B1-0` step removes `.codex/**` in seven commits with D-entries; `AGENTS.md` keeps only its blocks and a pointer; the parity checker's compare switches to suites only |

**Standing rows:** `Q-G-02`, `Q-G-03`, `Q-G-04` and `Q-G-06` gate no single step; they are the program's standing rules, assumed (a) by every block until answered otherwise, and an other answer inserts steps per the table above.

**Resolved by the orchestrator under the operator's standing instruction** ("Do everything you can on your own. Reduce the operator steps to a minimum.", 2026-10-13, Q-G-03): lane questions whose (a) is mechanical and carries no design or scope consequence are recorded as answered (a) by the orchestrator with the date, listed here for the operator's veto at the next §O session: `Q-B7-01` (a), `Q-B7-02` (a), `Q-B4-01` (a), `Q-B5-02` (a). Design-gate questions (`Q-B5-01`, `Q-B5-03`, `Q-B5-04`) are put at `G-DS` (`B5-3`), where the operator decides anyway; `Q-G-06` stays open.

**Readings applied by the orchestrator:** `Q-A4-03` (a) read "pin 1.7.0 @ f08e588 = v1.0.0"; K-1 merged into the Kit's master before any client was anchored, so `B5-4`…`6` pin the Kit's current master, 1.11.0 @ `612e634` (tag `v1.11.0`), which is 1.7.0 plus K-1's gaps closed; listed for the operator's veto. `B6b` (AndroidApp) no longer waits on a Kit session: its compile stays a deferred row (DV-A9A-a) and its `-8` step waits only Q-G-04 and the compile leg.

**Recorded deviations:** `Q-A6S-03` (a) read "git mv update_graph.bat archive/root/"; the `B3-2` block said `git rm` (no `archive/` exists yet in the superproject) and B3-2 removed it (recoverable from history), recorded in its entry. `Q-A6V-04` (a) read "archive to `archive/scripts/`"; the `B3-5` block said `git rm`, and B3-5 removed the three scripts (recoverable from history); recorded here, no re-run.

**Settled, not asked again:** the kickoff's roots and rules (`PROMPT_master-rework-kickoff_2026-10-13.md`); no test in Phases A and B; the worktree layout (none needed, Q-A8-01); `PROMPTS_` naming for this runbook (Q-A5-02 (a) applied, the enum question stays open for the kit); the D-id shape; the agent set (RC-A1-04..06); the Kit pin by path and version (Q-A4-03 asks only the version).

## O. The operator session

Start a fresh session — **Opus 5.5 · high**, cwd `C:\Programmierung\SW_Development` — and paste the block below. If the operator is present in the orchestrator's chat, the orchestrator may put a question there in text and keep working (Q-A5-04); the record is the same. The orchestrator rewrites this block at every boundary for the new open set.

```text
You are the operator session of the PlantLibrary master rework program (cwd C:\Programmierung\SW_Development, branch master).
Scope: put every open row of rework/REGISTER_operator-questions_2026-10-13.md to the operator, record the answers verbatim, flip the rows, mirror them in §Q of rework/PROMPTS_master-rework-runbook_2026-10-13.md, and commit.
Read first: the register (Why (a), Source, When; the rows marked superseded are not asked); the runbook §0, §1, §Q (its "What changes if you answer all recommended", "What a non-(a) answer changes" and "Settled" parts); for each question, the audit row its Source names, nothing wider.
Order: after R-4.2 (2026-10-13) exactly one row is open — Q-B5-13 (the two GitHub repository variables the design-conformance workflow needs; an operator act, owed item 18). Put it first, then walk the rows the orchestrator answered (a) under your standing instruction, listed in §Q under "Resolved by the orchestrator" and in the register with the words "answered by the orchestrator", for your veto; a veto is recorded as a new answer with the date, and the orchestrator inserts the step it implies.
For each row: first the read-only fact checks it depends on (named in its Source audit's §6), reported; then two plain sentences on what is decided, (a) and why, the other options and what each costs, which steps wait. The operator may answer the whole set in one line ("all recommended", or "all recommended except <ids with options>").
Record: per row the operator's words in quotes, the date and UTC time, "asked in <this session's name>", the option it resolves to, and a Reading line where the words depart from the options together with the step the orchestrator must insert; State answered.
Constraints: never answer a question yourself; edit only the register and the runbook's §Q; no test of any kind; push only when the operator says so in this session (the push list is in the runbook §3a item 6 and the latest R-4 Note): plain git push of each named submodule's main first, then the superproject, nothing forced.
Done when: every row the operator answered reads answered with the words, time and Reading; §Q mirrors it in the same commit; the superproject hygiene verdict shows zero violations; the commit is made; the final message gives the §L row and the commit the gitlink takes.
Commit line: rework: operator - questions answered <date> (<ids>)
```

## L. Ledger — flip as you go

Status vocabulary: `todo` · `running (<session name>)` · `done <YYYY-MM-DD> — <repo> <sha>[; <repo> <sha>]` (the superproject commit carrying the flip is "this commit") · `waits Q-<lane>-<nn>[, …]` · `held (<what, by id>)` · `skipped (<why>)` · `split → <id>a, <id>b` · `retired <YYYY-MM-DD> (<Q id or D-id>)`. Decision holds a D-id or —. Note ≤ 160 characters.

| Step | Title | Status | Decision | Note |
|---|---|---|---|---|
| `R-0` | verify and open the track | done 2026-10-13 — `8702e0a` | `D-2026-10-13-01` | Workspace gitlink `6b4b88b` |
| `R-1` | Phase A: seventeen audits | done 2026-10-13 — `b5daba2` | — | 51 lane claims re-checked, all held (the commit message miscounts 18/54) |
| `R-2` | registers merged | done 2026-10-13 — `554a591` | — | 264 candidates, 103 lane questions, 31 proposed deferrals |
| `R-3` | §3, §3a, §3b, §Q, §O, §L, §R written; pointed B6 file | done 2026-10-13 — `4678e35`; §R round applied in the follow-up commit | — | 38 findings, 10 blockers, all resolved |
| `B7-1` | static guards and the multi-root parity checker | done 2026-10-13 — super `a25b62e` | — | 3 guards green over 7 repos; 0 mixed, 0 parse errors on the 7 live packages; parity self-check 10 plants; Q-A2-04 (a) assumed; re-run by the orchestrator |
| `B5-1` | design-gate evidence pack | done 2026-10-13 — super `99e5143` | — | 7 pairs: 3 candidate sets each 110/110 in scratch; Kit export writes no flat files (Q-B5-01); Q-B5-01..04, DV-B5-01 proposed |
| `B3-1` | M-8 closing pass | done 2026-10-13 — super `69d10de` | — | 7 repos green with holds (3/10/1×5); 967→1072 files diffed; M-9 set 7 names; Kit changelog owed (item 17) |
| `B4-1` | parser-honest package edits | done 2026-10-13 — Server `243b13e`; Workspace `9669d19`; SharedContracts `86398fe` | — | SV1-B06 five tokens (blocked); SY1-B07 above SY1-B05; SC1-B02 four tokens; 0 census errors under both parsers; verified by the orchestrator |
| `B8-1` | bindings recorded obsolete; ledger and §N corrections; PyApp cleanup | done 2026-10-13 — super `c8fa93d`; PyApp `2e81a34` | — | bindings obsolete (Q-G-02/Q-A8-02); 2b count ten; step 6 hold lapsed; step 8 superseded; GC-6082/2437/7053 closed; graphify-out/ 45 MB deleted; commit line wording stale |
| `R-4.1` | wave 1 boundary | done 2026-10-13 — this commit | — | wave 1 done (B7-1, B5-1, B3-1, B4-1, B8-1 + B4-2, B4-3, B3-3, B3-4, B3-5); pushed: six suites' main and master; §O refreshed |
| `B2-1` | superproject `CLAUDE.md` | done 2026-10-13 — super `3c8ae25` | — | title + 6 sections; Testing and hygiene blocks byte-identical (verified); rules 4/5 per the readings; roster 3 agents; Q-B2-01 → `B2-1.1` |
| `B2-2` | Dashboard, AndroidApp, PyApp guides | done 2026-10-13 — Dashboard `47ce96b`; AndroidApp `f7b4e75`; PyApp `5f91cdc` | — | gate, standards, session pointer, scratch, skill list, roster; PyApp stub + rules folded; AndroidApp READMEs (Q-A6A-04 (a), Q-B2-03); verified |
| `B2-3` | Server, SharedContracts, Workspace guides | done 2026-10-13 — Server `590825d`; SharedContracts `1f26779`; Workspace `8f7dad5` | — | 3 sections per suite; gate bullet; Procedure list; Server Docker-pipe wording; hygiene blocks byte-identical; verified |
| `B7-2` | Codex freeze | done 2026-10-13 — super `ddab755`; PyApp `c667a7e`; AndroidApp `179a67a`; Dashboard `ebe52bf`; Server `a4d3f98`; Workspace `3efabdf`; SharedContracts `efd577d` | super `D-2026-10-13-03`; PyApp/AndroidApp/Dashboard/Server `-02`; Workspace/SharedContracts `-03` | freeze green 7/7, old compare off, 25-plant self-check; AGENTS.md pinned with marker blocks stripped; bridge README pending until B1-1; verified |
| `B1-1` | superproject `.claude/` synced | done 2026-10-13 — super `d144d78` | — | plan-batch 1.5.1-pl, run-batch §7 rule, 3 Conductor agents, TDD/debugging stack-neutral, harness-upkeep, tracked settings, bridge README; mirrors red (60) till B1-2; verified |
| `B1-2` | six mirrors synced | done 2026-10-13 — PyApp `db6af71`; AndroidApp `64ae3f6`; Dashboard `973ac71`; Server `ed315c8`; Workspace `11207d3`; SharedContracts `2ca792e` | — | byte copies: 5 shared skills + 3 agents per suite plus the named extras; PyApp gui-validation full; parity pass; extras table filled by the orchestrator; verified |
| `B1-3` | third-party skills | done 2026-10-13 — super `58e18e7` | — | code-quality-review (MIT), security-audit (CC-BY-SA-4.0), pathfinder (Apache-2.0) installed, operator-only, no network; dependency-audit declined; provenance rows; parity green |
| `B2-1.1` | the Testing block's worker sentence reworded (Q-A3-02) | done 2026-10-13 — super `3be260b` | — | sentence in the Conductor's E-03r form naming real-stack-validator (Sonnet 5.5); 2 lines changed; verified |
| `B7-3` | scratch gate, harness docs, Server ledger | done 2026-10-13 — PyApp `e17d7ba`; Server `d6a6497`; SharedContracts `72e5a38`; Dashboard `604d1d0`; AndroidApp `2353b6c`; Workspace `41fd24c`; super `14b08a4` | `D-2026-10-13-04` (each suite) | scratch-gate in PyApp and Server; scratch module decided, enabled at B3-8's re-pin; Server ledger empty; harness README refreshed; parity green; verified |
| `B3-2` | superproject leftovers; backlog register | done 2026-10-13 — super `5e9dce2` | `D-2026-10-13-02` | graphify-out deleted (282 MB), update_graph.bat removed, both allowlist-removed and retired; 14 UB rows; Todo.md untouched; verified |
| `B3-3` | Workspace archive; exempt-tree notes | done 2026-10-13 — Workspace `cead813` | `D-2026-10-13-01`, `D-2026-10-13-02` (Workspace) | archive/ declared legacy (README only); DTI restated frozen (47), methodology pinned 4.1.0 (74); Q-B4-01 cite fixed in prose; verified |
| `B3-4` | M-9 hold releases | done 2026-10-13 — PyApp `791da51`; AndroidApp `a0ea1a9`; Dashboard `f954fc9`; Server `8cb519f`; SharedContracts `4045817` | `D-2026-10-13-01` in each of the five suites | five V1 proposals renamed `PROPOSAL_<suite>-v1_2026-07-10.md`; Dashboard's two pinned docs moved; all five verdicts 0 held; verified |
| `B3-5` | stale scripts; Server docs links | done 2026-10-13 — Dashboard `c82434a`; Server `1484425`; Workspace `c209020` | — | 3 scripts removed (git rm, recoverable); Server 8 docs links fixed; residual prose lines → `B3-7`; verified |
| `B4-2` | markers; DRIVER_SCRIPT stubs; README lines | done 2026-10-13 — PyApp `e8b738d`; Server `dd62b80`; SharedContracts `93933ff`; Dashboard `98c9b0a`; AndroidApp `b780d20`; Workspace `61dd9a2` | — | 5 markers, 7 stubs with owner tables, README run lines; census unchanged; PyApp hash unchanged; GC-7053 closed in all 7 drivers; verified |
| `B4-3` | SDA superseded | done 2026-10-13 — Workspace `764c11f` | — | 41 open rows deferred with dated B5/B6 lines; DEC-01..05 overtaken; header six-value set; 9 batches already_done; verified |
| `B4-4` | decision lines; traceability | done 2026-10-13 — Server `6dd192b`; SharedContracts `986f081`; Workspace `88a6226`; Dashboard `57ecc25`; PyApp `2bd98b2`; AndroidApp `a0f614a` | — | 7 packages: 1.5.1-pl/tiers/readings/DV-pointer STATE lines; Traceability sections; SCOPE procedure line; Q-B4-02 rules in Standing invariants; SC design/ repointed (Q-B5-06); census unchanged; verified |
| `B4-5` | static package proof | done 2026-10-13 — super `0597766` | — | 0 errors under both parsers (60 batches, 185 rows); PyApp hash unchanged since 35ddc63; 7 toplevels = suites; trees clean; 28/28 required files; verified |
| `B5-2` | Configuration DRAFT | done 2026-10-13 — SharedContracts `a3f863d` | `D-2026-10-13-02` (SharedContracts) | imported core, 4 docs, 4 mappings, conformance seeded; validator 0 schema errors, 7/110 pairs fail as expected; round trip 0 diffs; verified |
| `B5-3` | `G-DS` design gate | done 2026-10-13 — SharedContracts `eb521b2` | — | set A (#636A5E/#D77606); validator 110/110 exit 0; design-tokens/ follows by 6 hand-edited values + notes, round trip 0 diffs; ARGB bans added; verified |
| `B5-3.1` | component contracts; Gallery page; eol attributes | done 2026-10-13 — SharedContracts `8e16658` | — | 23 contracts + Gallery page (Kit 1.7.0 tools from a git archive); coverage: component set 23/23, contracts 46/46; matrix 0/23 → `B5-3.2`; verified |
| `B5-3.2` | matrix seeded; Map cells; attributes | done 2026-10-13 — SharedContracts `fc60b5a` | — | Kit coverage 100% (117/117), matrix 46/46, baselines n/a; C-02/C-23 not_applicable; verified |
| `B5-3.3` | client mappings synced back to canonical | done 2026-10-13 — SharedContracts `c3ab790` | — | qt-qss and compose mapping.md byte-equal to the PyApp 52aaed5 and AndroidApp ffa3214 blobs; their header comments still say "ahead of canonical" (fixed in one place at the first B6 re-sync); verified |
| `B5-4` | Dashboard anchored | done 2026-10-13 — Dashboard `f03a0eb` | `D-2026-10-13-03` (Dashboard) | 32 files byte-equal to SC 8e16658; Kit 1.11.0 pinned; pin/drift/Kit parity pass; literal census 437 (349 in the legacy generated theme); impeccable ×4; harness green; verified |
| `B5-5` | PyApp anchored | done 2026-10-13 — PyApp `52aaed5` | `D-2026-10-13-03` (PyApp) | Kit 1.11.0; qt-qss tokens.py (parses); pin/drift pass; Kit parity fails on impeccable per-runtime builds only (Kit finding); adapter route in mapping.md; DESIGN.md emitted; verified |
| `B5-6` | AndroidApp anchored | done 2026-10-13 — AndroidApp `ffa3214` | `D-2026-10-13-03` (AndroidApp) | Kit 1.11.0; Tokens.kt emitted unwired (package via emit-options); pin/drift pass; Kit parity fails on impeccable only; KG-C-01..05 recorded; verified |
| `B5-7` | design-adoption retired | done 2026-10-13 — super `71e2d5b`; Dashboard `ad7a440`; AndroidApp `3a6e4b3`; PyApp `055e9dc`; Workspace `b0ef070` | — | pointer skill; 6 skill cells + 6 anchor lines → design-gate; PyApp hash unchanged; parity and census green; verified |
| `B5-8` | readiness rows 1–7 | done 2026-10-13 — super `da64629` | — | 3 runs at Kit 1.11.0: rows 1/3/5 green; row 2 red (impeccable variants, Q-B5-15); row 4 red AndroidApp (hook file → B6b-1); row 6 vacuous (Kit header bug, Q-B5-21); row 7 informational (no instance bound); row 8 deferred DV-B5-04 |
| `K-1` | Design Template Kit session (Kit branch) | done 2026-10-13 — Kit master `612e634`, tag `v1.11.0` (merged ff and pushed by the orchestrator) | — | 10 commits: Kotlin/Qt literals, scoped bans, Compose TextStyle + package option, Qt THEME_VARS, export --write, import --input; node 201/202 (1 pre-existing); browser + Kotlin legs → DV-K1-01 |
| `B8-2` | onboarding notes closed by B4 | done 2026-10-13 — super `2644ef9` | — | B4-5 proof under step 5; step 7 waits the profile rollout; step 8 Q-A2-03 (a) cited; GC-6082/7053 re-checked; GC-2437 SHA |
| `B8-3` | GC-1132 reviewed | done 2026-10-13 — PyApp `0d71d71`; super `a4809ac` | — | the operator's review words (Q-A2-02) recorded in ONBOARDING_harness-port.md; onboarding §L step 4 marked reviewed |
| `R-4.2` | wave 2 boundary | done 2026-10-13 — super `331b954` | — | wave 2 done (B2-1..3, B2-1.1, B7-2, B1-1..3, B7-3, B3-2..5, B4-2..5, B5-2..8 with 3.1-3.3, B8-1..3, K-1, K-2); ledger repaired (§H); pushed all seven; §1/§O refreshed; wave 3 opened |
| `B6a-1`…`B6a-8` | Dashboard GUI rework | pointed | — | see the lane file §L |
| `B6c-1`…`B6c-8` | PyApp GUI rework | pointed | — | |
| `B6b-1`…`B6b-8` | AndroidApp GUI rework | pointed | — | |
| `R-4.3` | wave 3 boundary | todo | — | |
| `C1-1` | deferred validations planned | todo | — | |
| `C1-2` | hand-back section; `SUITE_HANDOFFS.md` | todo | — | waits answered 2026-10-13 (R-4.1) |
| `B3-6` | sequencers archived | todo | — | waits answered 2026-10-13 (R-4.1) |
| `B3-7` | residual prose sweep | todo | — | inserted 2026-10-13 after `B3-6` |
| `K-2` | hygiene kit session: K-7 and the pilot lessons, release 0.3.0 | done 2026-10-13 — kit main `d5b9742`, tag `v0.3.0` (pushed) | — | release ends exempt-tree/subfolder declarations; a set folder can be held; 3 fixtures, 14/14 green; 10 lessons logged; worktree removed; verified |
| `B3-8` | re-pin to kit 0.3.0; Workspace set released | todo | — | after `K-2`, `B3-6` |
| `C1-3` | resume blocks | todo | — | |
| `C1-4` | hand-back HANDOVER | todo | — | |
| `R-4.4` | wave 4 boundary | todo | — | |
| `R-5` | close | todo | — | |

## R. Adversarial round on the R-3 draft

One fresh-context, read-only reviewer (Sonnet 5.5 · high, 2026-10-13, after the R-3 commit `4678e35`) read this file and the pointed lane file against the template's checklist (every block free of a runner name, a tests root, a selection flag and a whole-suite phrase; every precondition resolvable to a step id or event; lanes partitioned in §3a; every `waits` naming a register row; no launch value inside a fence; the flip rule applied). Findings and resolutions:

| # | Finding | Resolution |
|---|---|---|
| 1 | `B7-1` Done-when named an unsatisfiable newline clause (the mixed-file list holds no contract file) | reworded: 0 mixed contract files on the live packages; the list quoted as the do-not-fix set |
| 2 | the newline guard would scan `.tmp/` and frozen packages | git-tracked files only, `.tmp/` excluded, frozen and archive packages listed not counted |
| 3 | two Watch paragraphs named a runner | reworded (M `B7-1`, G `B6a-6`) |
| 4 | the `.claude` ordering rule was too wide and `B5-4/5/6` lacked `B7-2`/`B1-2` | rule narrowed to skills, agents, settings; preconditions added |
| 5 | `B1-1` demanded a green mirror compare it must turn red | freeze and bridge checks green; the mirror compare red until `B1-2`, quoted |
| 6 | `B3-1` flipped M-8 done without the hygiene runbook §16's deliverables; one item writes the Kit | re-scoped to §16's in-TARGET deliverables; the Kit changelog is owed item 17; M-8 flips "done except the Kit changelog" |
| 7 | the wave-2 superproject queue omitted four steps; up to seven writers against a cap of four | queue completed; chains defined as one-writer queue order among ready steps; four live sessions, release in listed order |
| 8 | B6 fences named tools and authored validation cells | tools removed; cells authored by plan-batch from the row schema; visual legs as DV rows by id |
| 9 | `B6*-8` closed rows on static legs, overriding the skills | statuses per the plan-batch status set for unvalidated work; the choice is `Q-R-01`; the orchestrator note reworded |
| 10 | gates inside one headless run (`-6`, `-7`) | each split into two sessions (`a` to the gate, `b` after `event:G-x-n`) under the split rule; ledger rows adjusted |
| 11 | `B7-2`'s freeze SHA was a hash fixed point | freeze commit = the commit preceding the entry's commit in each repository |
| 12 | rule 4 let no lane do what it said | rule 4 rewritten: the orchestrator flips and bumps; `C1-2`/`C1-3` the exceptions |
| 13 | most Done-whens lacked the final-message clause | appended to every Done-when in both files |
| 14 | `B4-1` ran beside `B7-1` while the census script was being edited | `B4-1` precondition `B7-1` |
| 15 | §Q waits disagreed with the steps' Waits; Q-G-02/03/04/06/09 unwaited | waits reconciled (`B5-3`, `B3-6`, `B8-1`, `B2-2`, `B1-1`); standing rows declared |
| 16 | `B7-3` paths did not exist | full package paths given |
| 17 | `B7-3` Done-when needed a README row no step wrote; Q-A2-06 (a) had no executor | README row and the scratch-module installer re-run added to `B7-3` |
| 18 | `B3-3` moved `WORKSPACE_STATE.md` before the hand-back | move transferred to `B3-6`; `B3-3` declares the tree with its README only |
| 19 | `B5-2` demanded a held count `B3-4` changes; lacked `B2-3`; cited shifting line numbers | "verdict as at the commit before"; `B2-3` precondition; citation by wording |
| 20 | `B5-7` edited a Workspace file outside its Where | Workspace added to Where, Writes and the matrix |
| 21 | `B6*-8` needed a launch value inside the fence | "the batch named in the first line of your launch message"; commit line generic |
| 22 | a version step after the clients pinned could fail their pin check | stated: pins hash the four core files only; a core change re-syncs in the first `-8` batch |
| 23 | master rows gave all `B6c`/`B6b` steps one precondition | rows split `-1…-5` / `-6…-8` |
| 24 | route `check` was read-only yet wrote evidence | `check` redefined as a headless session writing only its evidence and INDEX line |
| 25 | `B2-1` both kept and edited the Testing block | Testing block byte-identical; its lines change in a later `B2` step after Q-A3-02 |
| 26 | `B4-4` read as rewriting validation cells | "STATE lines only; cells untouched" |
| 27 | `B5-8` carried flags without values | concrete read-only paths; flags dropped |
| 28 | `B7-1` kept a check that does not exist; "self-tests" wording; no `--no-optional-locks` | "add"; planted-drift self-check named as static; `--no-optional-locks` required |
| 29 | `R-3` and event names outside the §3.0 vocabulary | vocabulary extended |
| 30 | duplicate `Q-G-02`/`Q-G-03` rows in the register's lane section; counts wrong | duplicates removed; counts corrected |
| 31 | §Q carried (a) only | accepted: the register of record holds the options; stated in §Q |
| 32 | existing D-ids cited in fences | accepted: citations of recorded entries are pointers, not values to fill |
| 33 | `B8-1` proceeds on a partial wait | rule 6 gains the partial-wait clause; `B8-1` says so |
| 34 | §L statuses carried parentheticals | moved to the Note column |
| 35 | two paths wrong (`B3-4`, `B3-5`) | corrected |
| 36 | `B5-1` fence held a full node command; `B7-2` banner anchored to a line number | tool named by purpose, output in scratch; banner anchored by pattern |
| 37 | a methodology bootstrap could regenerate a driver and `_ACT_STATE.md` | constraint added to `B6*-1` |
| 38 | wave-2 chains read as preconditions behind the freeze questions | covered by 7: chains are queue order, not preconditions |

Verdict recorded: after these edits `B7-1` may launch; findings 4–10 were repaired before any wave-2 or `B6` step exists in a runnable state.

## H. History and hand-back

2026-10-13 (after `B8-2`): a defect in the orchestrator's flip scripts had replaced 24 step-map rows of §3.2 with ledger text while their §L rows stayed `todo`; each step-map row was restored from the commit before its damage and the done text moved into §L (commit noted in §L's `R-4.2` row). No block text was affected.

Retired blocks are moved here whole. The hand-back section (H.1–H.8) is written at `C1-2` and `C1-3`.
