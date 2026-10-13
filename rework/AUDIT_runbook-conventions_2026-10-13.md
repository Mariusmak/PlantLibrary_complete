# Runbook conventions — lane A5 (read-only analysis, 2026-10-13)

*Lane `A5` of `R-1` (Opus 5.5 · high, subagent, read-only). Sources read at SOURCE-C `main` `2e7adb3`, the design
worktree `Orchestrator_System-design` at `eae340a` (`design/dti-pilot`), SOURCE-K `Repo_Hygiene_Template_Kit` 0.2.1,
SOURCE-R `Working_Folder` as found; TARGET superproject `master` at `8702e0a`. Nothing was written outside this file;
no test, build or install was run; every git command was a read (`--no-optional-locks` in SOURCE-C).*

## 0. Summary

1. The R-0 skeleton descends from the local track runbooks and the kit's `RUNBOOK_TEMPLATE.md`, not from the Conductor's runbook contract. It lacks four §0 rows (Not here, Tag, Home branch, Inputs), a SHA stamp on §1, numbered file rules in §2, a Block column, an owed-items section, a ladder with reasons, an adversarial round and a history section (F-A5-01).
2. The §L column order puts `Model · reasoning` third. The Conductor's ledger reader takes the third cell as the status, so §L should be `Step | Title | Status | Decision | Note`, with the brief's status words plus `split` and `retired` (F-A5-02).
3. The submodules do **not** resolve through `.git/modules/<name>`. Each one has its own embedded `.git` directory, and the superproject has no `.git/modules`. A `git -C <repo> worktree add` therefore lands its admin directory in `<repo>/.git/worktrees/<name>`, with no `core.worktree` hazard. The exact sequence is in §7.4 (F-A5-03).
4. The hygiene checker scans only `PROMPT_`/`PROMPTS_` files in planning and general roots, and `rework` is general, so this runbook is scanned. Its argv detector has no negation guard, so even a "never do X" sentence that names the runner and the tests root trips it (F-A5-04).
5. Keep `PROMPTS_`. The Conductor decided on `RUNBOOK_` but has not enforced it (`CD-V2-HRN-142` is todo), and the runbook skill is installed in neither repository. The Conductor's planned `OP-RB` act would copy that skill into `PlantLibrary_Workspace`, which means a SOURCE program writing TARGET (F-A5-05, F-A5-06; Q-A5-01, Q-A5-02).
6. Adopt the Conductor's flip rule. A lane that commits outside the superproject's `master` names its §L row and gitlink in its report, and the orchestrator writes the gitlink bump and the flip in one superproject commit. The registers are also superproject files, so lanes propose question and deferred-validation rows and do not write them (F-A5-09, F-A5-18).
7. Waves are event-driven: each step starts when its preconditions hold. Boundaries are explicit `procedure` steps (`R-4.<k>`), each with its own ledger row. The ritual is: drain, re-read the register, fast-forward merge each worktree branch, remove the worktree, gitlink and flip commits, refresh §1 and §O, then the operator's push (§7.4).
8. The Conductor's question-pack conventions are richer than R-0's register. They add a one-line answer form, a "what changes if all recommended" summary, a settled list, a Source column, the † marker, a UTC time, a Reading line and a "what a non-(a) answer changes" table. Twelve deltas are named in §7.3.
9. For the hand-back (C1), the precedent is the reconciliation runbook's Phase D (`rc-13`): it writes the next runbooks and re-points every track's "next act" through a board table. C1 follows that shape, plus the lane-close rule and the kit's HANDOVER continuation (§7.6).
10. This lane raises 4 operator questions, has 29 candidates and found 21 findings. 34 skeleton deltas are numbered in §7.5.

## 1. Coverage

Path aliases used in every citation below (`alias:line`):

| Alias | Path (root, pin) |
|---|---|
| `KO` | TARGET `rework/PROMPT_master-rework-kickoff_2026-10-13.md` (`8702e0a`) |
| `SK` | TARGET `rework/PROMPTS_master-rework-runbook_2026-10-13.md` (`8702e0a`) |
| `QR` | TARGET `rework/REGISTER_operator-questions_2026-10-13.md` |
| `DVR` | TARGET `rework/REGISTER_deferred-validations_2026-10-13.md` |
| `HR` | TARGET `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` |
| `OB` | TARGET `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` |
| `HC` | TARGET `scripts/hygiene/repo_hygiene_check.py` |
| `HD` / `CH` | TARGET `hygiene/HYGIENE_DECISIONS.md` / `hygiene/CONSUMED_HYGIENE.md` |
| `MG2` | SOURCE-C `implementation/Conductor_V2/planning/PLAN_master-guide-v2_2026-10-09.md` (`2e7adb3`) |
| `QP` | SOURCE-C `implementation/Conductor_V2/planning/PROMPTS_quality-program_2026-10-02.md` |
| `RBS` | SOURCE-C `implementation/Conductor_V2/planning/PROPOSAL_runbook-skill_2026-10-02.md` |
| `CN` | SOURCE-C `implementation/Conductor_V2/planning/PLAN_conductor-native_2026-10-10.md` |
| `RC` | SOURCE-C `implementation/Conductor_V2/planning/PROMPTS_program-reconciliation-and-restart_2026-09-21.md` |
| `TC` / `BP` | SOURCE-C `implementation/Conductor_V2/TASK_CHECKLIST.md` / `BATCH_PLAN.md` |
| `ST` | SOURCE-C `implementation/Conductor_V2/STATE.md` |
| `DR6` | SOURCE-C worktree `C:\Programmierung\Orchestrator_System-design` `implementation/Design_Migration_V1/planning/PLAN_design-round-6_2026-10-12.md` (`eae340a`) |
| `ORCH` | SOURCE-R `Working_Folder\Orchestrator_System_Work\orchestrator-tools-2026-09-28\orch.py` |
| `QP6` / `AN6` | SOURCE-R same folder, `QUESTION-PACK_round-6_2026-10-03.md` / `ANSWERS_round-6_2026-10-03.md` |
| `AOG` | SOURCE-R same folder, `ANSWERS_operator-guide_2026-10-13.md` |
| `H1112` | SOURCE-R same folder, `HANDOVER_a11-to-a12_2026-10-09.md` |
| `KRT` / `KHT` | SOURCE-K `Repo_Hygiene_Template_Kit\templates\RUNBOOK_TEMPLATE.md` / `HANDOVER_CONTINUATION_TEMPLATE.md` |

| Item | Status | Reason |
|---|---|---|
| `KO` | read | in full, as the brief requires |
| `SK` | read | in full |
| `QR`, `DVR`, `rework/INDEX.md` | read | in full (header rows only exist) |
| `MG2` §0, §1, §2, §2a, §3, §3a, §5, §6, §7, §8 | read | §4 read for `mg-4`, `mg-5`, `mg-6`, `mg-11`, `mg-18`, `mg-19`, `mg-31`, `mg-32`, `mg-32.1`, the docs-lane preamble |
| `MG2` §4 remaining blocks (`mg-22`…`mg-29`, `mg-32.2`…`mg-36`) | partly read | headings only; the block shape was already established by the read blocks |
| `QP` §0–§5 | read | in full |
| `QP` §6 | partly read | intro, `rb-1`, `qi-1`; the other wave-1/2 blocks by heading only |
| `QP` §7, §8 intro, §8.1, §8.3 `qi-2a`, §8.6, §8.7, §8.8, §9, §10 | read | §8.2, §8.4, §8.5, §8.9 by heading only |
| `RBS` §3, §4.1, §4.5, §5, §7 (skill draft) | read | §0–§2, §4.2–§4.4, §4.6, §6, §8 by heading only (§8 Q1 first lines read) |
| `CN` §2, §3, §3a, `cn-5` block, §6a, §7 | read | §0, §0a, §1, §2a, other blocks by heading only |
| `DR6` §2, §3 merge-point rows, §3a | read | other sections by heading only |
| `RC` §9 (Phase D, `rc-13`), §10 | read | headings of the rest |
| `ORCH` `block`, `launch`, `run`, `step`, the ledger parsers, `NUDGE` | read | `lane`, `incomplete`, `wait` skimmed |
| `QP6` header, answer form, "what changes", §0, group A | read | groups B–E by heading only |
| `AN6` lines 1–40; `AOG` lines 1–45 | read | the rest not read (the shape repeats) |
| `H1112` §1, §2, §5 | read | §0, §3, §4, §6 not read |
| `HR` §0, §2, §3, §4, §12 (A-2…A-7 step), §16 (`M-8`), §17 (`M-9`), §18 ladder, §L | read | §1, §5–§11, §13–§15 not read |
| `OB` §0, §2, §3, §4, §11 (step `5`), §L, §N | read | §1, §5–§10, §12–§15, appendices not read |
| `HC` 100–130, 640–700 | read | the proof-surface rule and its scope; rest not read |
| `HD` 1–60, 150–233; `CH` 1–28 | read | the entry shape, a runbook-driven entry (`D-2026-09-16-03`), `D-2026-10-13-01` |
| SOURCE-C `hygiene/HYGIENE_DECISIONS.md` | not read | does not exist: `git ls-files` in SOURCE-C lists no `HYGIENE_DECISIONS.md` or `CONSUMED_HYGIENE.md`; the Conductor records runbook-driven decisions in `ST` (e.g. `ST:44146`) |
| `KRT`, `KHT` | read | in full (not named by the brief; §5) |
| `TC:1086`, `BP:12905`–`:12909` | read | the `RUNBOOK_` naming row and its batch, to establish its state |
| Submodule git layout (all seven repositories) | read | `rev-parse --git-dir`, `.git` type, `config`, branches, `core.autocrlf`, longest tracked path; no write |
| `PLAN_worker-console_2026-10-10.md` | not read | the conductor-native and round-6 lane runbooks covered the lane-runbook shape |

## 2. Findings

**F-A5-01 — The skeleton is the local family, not the Conductor contract.** The Conductor's contract (`RBS:235-246`) requires these §0 rows: Scope · Not here · Tag · Home branch and absolute path · Ledger of record · Inputs (decision ids) · What this file never does. It also requires a §1 "measured at `<sha>` on `<date>`" (`RBS:240`), ≤ 10 numbered file rules (`RBS:241`), a step map with a `Block` column (`RBS:242`), owed items (`RBS:244`), a ladder with reasons (`RBS:245`), the ledger (`RBS:246`), and an adversarial round for runbooks over 10 steps (`RBS:257`). `SK:11-17` has Scope, Roots, Ledger of record, Models and "never does". `SK:19` is unstamped. `SK:37-48` restates no file rules. `SK:57-66` has no Block column, and owed items, the ladder and the adversarial round are absent. The skeleton's shape follows the local precedents (`HR:10-19`, `OB:13-19`) and the kit's template (`KRT:20-30`, `KRT:104-109`). *Meaning:* R-3 adds the missing rows and sections under the kickoff's fixed letters (§7.5).

**F-A5-02 — §L column order breaks the Conductor's ledger reader.** `ORCH:171` matches `| \`<id>\` | <one cell> | <rest>` and takes the rest as the status. Its `step` loop (`ORCH:177-191`) resumes a session until that cell stops starting with `todo`, and `RBS:246` states that rule ("status the third cell"). `SK:132` is `Step | What | Model · reasoning | Status`, so such a reader would see `Opus 5.5 · high | todo`. `HR:956` has the same order, while `OB:902` (`Step | What | Status`) is compatible. *Meaning:* R-3 puts Status third and keeps the model in §3 only (one fact, one place).

**F-A5-03 — Submodule worktrees resolve through the submodule's own `.git` directory.** In all six submodules, `git -C <repo> rev-parse --git-dir --git-common-dir` returns `.git .git`. `<repo>/.git` is a directory, and `C:\Programmierung\SW_Development\.git\modules` does not exist (measured 2026-10-13). The submodule configs carry no `core.worktree` (grep of each `<repo>/.git/config`: only `bare = false`), and `core.autocrlf=true` in all seven repositories. Git is `2.55.0.windows.2`. A `git -C <repo> worktree add <path> -b rework/<lane> main` therefore writes its admin directory to `<repo>/.git/worktrees/<basename of path>`, and the new worktree's `.git` file points there. That path holds no `../.git/modules/<name>`. The brief's premise does not hold here. *Meaning:* the sequence in §7.4 is valid as written. Two consequences follow. First, no lane may run `git submodule absorbgitdirs` while a worktree exists. Second, a worktree of the superproject would have empty submodule folders, so the superproject is always written in place.

**F-A5-04 — The proof-surface rule as the checker applies it.** `HC:117-124` holds two argv patterns (the runner's name followed by the bare tests root, or broad selection flags) and one prose pattern (a re-run of the full, whole or entire suite). `HC:654-657` applies the argv patterns to any line containing the runner's name, unless the pin's sanctioned launcher is on the line. The launcher is empty here (`CH:18`). `HC:660-664` shields only the prose pattern, by a negation word before the match. `HC:671-674` scans only basenames that start with `PROMPT_` or `PROMPTS_`, in planning and general roots, and `rework` is general (`CH:28`). `HC:680` skips held lines, and `HC:688-692` enforces a floor (`CH:19`: 1). *Meaning:* every line of the runbook, of each block, of §O and of the C1 resume prompt is scanned. A "never X" sentence still trips the argv detector, so the template never names the runner at all. Any substring in which the verb "run" is followed directly by "the full", "the whole" or "the entire" and then the word for the test collection trips the prose detector unless a negation precedes it on that line, so the template uses "a whole-suite phrase" instead.

**F-A5-05 — `RUNBOOK_` naming is decided at the Conductor, not enforced, and the skill is not installed.** `MG2:5-8` explains why the master guide is a `PLAN_`: the skill is staged, not installed, and `OP-RB` renames it later. `TC:1086` (`CD-V2-HRN-142`, "Teach the naming test the `RUNBOOK` type and close `PROMPTS_`") is `todo`. `BP:12905` is its batch `CD2-B462`. Neither `C:\Programmierung\Orchestrator_System\.claude\skills\` nor `PlantLibrary_Workspace\.claude\skills\` contains `runbook` (directory listings). The TARGET kit 0.2.1 enum has no `RUNBOOK` (`HD:3-9` names `enum-add` as the only route), and its proof-surface scan does not reach a `RUNBOOK_` name (`HC:674`). *Meaning:* this program's runbook and any lane runbook stay `PROMPTS_` (Q-A5-02).

**F-A5-06 — A Conductor act is planned to write into TARGET.** `QP:1763` (`OP-RB`, act 8 of `qi-5`) says "the same sitting copies the skill into `C:\Programmierung\SW_Development\PlantLibrary_Workspace\.claude\skills\runbook\` and nothing else there (`E12`, `d.2`)". `QP:1994` lists `OP-RB` as open. If it runs during this program, a second program writes a TARGET repository, which breaks the one-writer rule (`KO:26`). *Meaning:* Q-A5-01 asks the operator to hold that copy and fold it into `B1`.

**F-A5-07 — Block grammar in the two families.** In the Conductor, the title line is the first line inside the fence and the model/route/where line sits directly above it. The fence holds `Context`, `Read`, `Write`, `Constraints`, an optional `If the context runs short`, `Done when` and `Commit line`. Below it come an *Orchestrator note* for launch values and a **Watch** paragraph, never pasted (`RBS:262-297`; executed: `MG2:156-170`, `MG2:210-226`, `CN:461-478`). The local family opens "Step X of <path>. cwd …, tree clean", then `Read first`, `Do`, `Constraints`, `Done when`, and two commit lines (submodule and superproject) (`HR:581-617`, `HR:908-934`, `KRT:71-87`). *Meaning:* §7.2 merges the two. It takes the Conductor's title line, model line and note, the kickoff's field names (scope, read-first, constraints, done-when, commit line; `KO:51`), and the local family's explicit cwd line. The superproject commit line moves to the orchestrator note (F-A5-09).

**F-A5-08 — Input placeholders: the families conflict.** `RBS:299-308` forbids inside a fence any value known before launch, such as a base SHA, a decision id or an earlier step's commit. The fence names an earlier outcome by pointer, and the orchestrator note carries launch values. `MG2:42` and `MG2:47` apply the same rule. The local family fills `<SUITE>` and the step id before pasting (`HR:142`, `HR:562-563`, `HR:906`). *Meaning:* the template writes one block per step, with no `<SUITE>` templates. That way the committed block is the pasted block, which is also what lets a reader extract it unchanged (`ORCH:47-61`).

**F-A5-09 — Who flips, and who bumps the gitlink.** In the Conductor, a step off the home branch names its row, and the orchestrator writes it at the merge or in an `ops` commit (`RBS:316-319`, `MG2:46`, `CN:204-205`). Locally, the step session itself bumps the gitlink and flips the ledger in one superproject commit (`HR:147-150`, `HR:616`; `OB:173-177`). Under parallel lanes, the superproject is one repository with many would-be writers (`KO:26`). *Meaning:* adopt the Conductor's rule. A lane commits only in its repository and its report names the row and the gitlink commit. The orchestrator writes "gitlink + flip" per step at the boundary. Only a step whose output is a superproject commit on `master` flips its own row.

**F-A5-10 — Ledger cells grew into narratives locally.** Local ledger cells run to several hundred characters (`HR:959-985`, `OB:907-912`). The Conductor caps the note at 160 characters, and anything longer goes to an evidence file or `STATE.md` (`RBS:246`, `RBS:858-860`). Its executed ledger keeps commit and decision in their own cells (`MG2:641-685`). *Meaning:* the §L Note cell keeps ≤ 160 characters; detail goes to the step's deliverable or the HANDOVER.

**F-A5-11 — Waves are event-driven, and boundaries are steps.** `DR6:135` says "each step starts the moment its preconditions hold". Merge points are `procedure` steps in the step map with their own ledger rows (`DR6:117-120`). `QP:165-172` groups sessions (A, B, C, D) and names events (`event:quality-branches-merged-into-work`). A boundary is a *drained* one: the merge happens only when nothing writes the target (`H1112:50-51`, `QP:136`, `QP:1806-1807`). *Meaning:* this program's boundaries become `R-4.<k>` procedure steps (§7.4), and preconditions may name events.

**F-A5-12 — Question-pack conventions beyond the R-0 register.** The Conductor packs add the following:
- a one-line answer form: "all recommended", or "all recommended except A.2 (b)" (`QP6:15-20`);
- a ten-line "what changes if you answer all recommended" (`QP6:22-33`);
- sources, a settled-not-asked list and an out-of-round list (`QP6:37-76`);
- groups ordered by when they block (`QP6:78-81`);
- per question: two plain sentences, (a) in bold with its reason, other options, **Waits**, **Source** (`QP6:83-93`);
- † for a recommendation the compiler made where the source made none (`QP6:10-13`).

The answer files record facts checked before asking (`AN6:6-14`), the verbatim answer with its time (`AN6:16-21`; `AOG:16-17`), the context as put (`AOG:8-14`), and a "Reading" line when an answer departs from the options (`AOG:26-31`). `QR:11-19` has ID, Question, Options, Why (a), Waits, State, Answer. *Meaning:* §7.3 lists twelve deltas.

**F-A5-13 — Gate practice.** Gates are asked in the orchestrator's chat "in text, while it keeps working, never through a blocking question tool" (`CN:196-200`; `MG2:418`). A step written "if Q (a)" is retired by any other answer, with status `retired` and the decision id (`MG2:45`, `CN:197-198`). An answer outside the options is recorded verbatim, together with the step the orchestrator must insert (`MG2:164`, `CN:472`). A table says what each non-(a) answer changes (`CN:611-622`). *Meaning:* `KO:28`'s "never block" is the same rule. The template adds the retire-on-other-answer status, the insert rule and that table.

**F-A5-14 — Session caps.** `QP:96-99` allows at most four headless sessions beside the main row and one Fable session at a time. The cap was lifted for read-only sessions by the operator, while one Fable at a time stays (`QP:906-908`). This matches `KO:27`. *Meaning:* §3a states it once and counts write sessions only.

**F-A5-15 — Headless launch facts.** `ORCH:94-96` launches with `claude -p --model <id> --effort <effort> --permission-mode auto --output-format stream-json --verbose`, in the step's exact cwd. `ORCH:74` is the `--bg` variant. `QP:143` names the family ids (`claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`). `ORCH:82-87`: a headless process ends when its turn ends, so background readers die. Subagents of a headless lane must therefore run in the foreground. `QP:103-104` notes that a headless session's edits under `.claude/**` were denied by permission mode in the Conductor. *Meaning:* §7.2 puts the flags in the orchestrator note, never in the fence. `B1` steps that edit `.claude/**` are flagged as a route risk (claim; §6 of this file does not verify it here).

**F-A5-16 — Hand-back precedent.** `RC:1091-1136` (Phase D, `rc-13`) writes the execution runbooks that the gates imply, then updates the program board "so that every track's next act points into the new runbooks". Its prompts after it are "not written here, deliberately" (`RC:1093-1094`), and its board is `Lane | Your next act | Where the prompt is | My recommendation` (`RC:1145-1150`). `CN:236-240` closes a lane with last flips, §0 "closed `<date>` at `<sha>`", the INDEX line turned `history`, then the merge. `RBS:336-337` states the same. `KHT:29-42` shapes a continuation. *Meaning:* §7.6.

**F-A5-17 — Size.** `RBS:333-335` sets an advisory ≤ 600 lines: past it, close and start the next runbook. The local runbooks ran to 987 (`HR`) and 934 (`OB`) lines. The Conductor's master guide carries big lanes as *pointed* rows whose blocks live in a lane runbook (`MG2:102-104`). *Meaning:* with 18 lanes, `B6` (three clients) is the candidate for a pointed lane file in `rework/` if §3 passes about 900 lines (an orchestrator call at R-3; no question).

**F-A5-18 — The registers have one writer.** `KO:22` (deferred validations) and `KO:28` (questions) have steps "record" rows in superproject files. Lanes that write a submodule would then also write the superproject, which `KO:26` forbids beside the orchestrator's commits. *Meaning:* a lane's report proposes rows (`DV-…`, `Q-<lane>-<nn>`), and the orchestrator writes them in the step's flip commit. Analysis lanes write only their own `rework/` file, which the orchestrator commits (`KO:37`).

**F-A5-19 — Sub-lane id collisions.** `A6` fans out ×7 and `A9` ×3 (`KO:43`, `KO:46`), so seven parallel subagents would each mint `Q-A6-01`. Rule 5's branch `rework/<lane>` would also collide if two sub-lanes ever wrote the same repository. *Meaning:* fix letters in §3.1 (`A6a`…`A6g`, `A9a`…`A9c`, and `B6a`…`B6c` if `B6` fans out per client) and use them in Q ids, step ids and branch names.

**F-A5-20 — The hygiene decision shape for runbook-driven entries is TARGET's own.** SOURCE-C has no `hygiene/HYGIENE_DECISIONS.md` (`git ls-files`); the Conductor writes decisions into `ST` (e.g. `ST:44146`, `D-2026-10-02-23`). TARGET's shape is `HD:33-45`. An entry has a heading `### D-YYYY-MM-DD-nn — <title>` under a dated `##` heading, then: `Authority:` naming the runbook step (`HD:159-161`, `HD:203-207`), the operator's words verbatim where a gate answered (`HD:161-163`), "Preconditions measured" (`HD:168-171`, `HD:209-213`), numbered dispositions (`HD:173-189`, `HD:215-229`), machine-read directive lines (`HD:191-195`, `HD:231`; vocabulary `HD:19-31`), and the commit line (`HD:197`, `HD:233`). *Meaning:* §7.1 points every root, hold, release or allowlist step at this shape.

**F-A5-21 — §1 is not stamped.** `SK:19` says "re-measured 2026-10-13 at `R-0`" with no SHA. `RBS:240` requires "measured at `<sha>` on `<date>`", ≤ 15 lines, rewritten whole, with no step status. `SK:35` carries two other runbooks' step status. *Meaning:* §7.5 deltas 6 and 7.

## 3. Candidates

| ID | Source path @ pin | What | Verdict | Target repo and path | Lane | Q id |
|---|---|---|---|---|---|---|
| RC-A5-01 | SOURCE-C `…/planning/PROPOSAL_runbook-skill_2026-10-02.md` §3.1 @ `2e7adb3` | the runbook contract: fixed §0 rows, a stamped §1, numbered file rules, a step map with a Block column, owed items, ladder, ledger | adapt: keep the kickoff's fixed letters (§0, §1, §2, §3, §3a, §Q, §O, §L) and add the contract's missing parts as lettered sections (§2a ladder, §3b owed, §R adversarial, §H history) | superproject `rework/PROMPTS_master-rework-runbook_2026-10-13.md` | R-3 | — |
| RC-A5-02 | same file §3.3 | the block grammar: title line inside the fence, model line above it, note and Watch below | adapt: the kickoff's field names plus an explicit `Where:` line (rule 5's worktree cwd) | superproject runbook §3 | R-3 | — |
| RC-A5-03 | same file §3.4 | input placeholders forbidden in a fence; output placeholders allowed | adopt verbatim | superproject runbook §2 | R-3 | — |
| RC-A5-04 | same file §3.5; `MG2` §2 rule 5 | the flip rule: off the home branch, the session names its row and the orchestrator writes it | adapt: also covers the gitlink bump (one superproject commit per step, written by the orchestrator) | superproject runbook §2 | R-3, R-4 | — |
| RC-A5-05 | same file §3.6 | one home branch; others read the runbook by absolute path | adopt verbatim (home is the superproject `master`) | superproject runbook §0, §2 | R-3 | — |
| RC-A5-06 | same file §4.1 | numbering: inserts `P.1`, parts by letter, re-runs `-r<k>`, never renumber or reuse | adapt: keep the kickoff's uppercase `<lane>-<n>` prefix (`B1-1`) rather than the lowercase tag grammar | superproject runbook §2 | R-3 | — |
| RC-A5-07 | same file §3.1 row 7; `ORCH` `row_status` | ledger with status in the third cell and a capped note | adapt: `Step \| Title \| Status \| Decision \| Note`, with the brief's status vocabulary plus `split` and `retired` | superproject runbook §L | R-3 | — |
| RC-A5-08 | `MG2` §6; `QP` §9 | a model ladder with reasons and the substitution rule | adapt to kickoff rule 9 | superproject runbook §2a | R-3 | — |
| RC-A5-09 | `MG2` §3a | a lane table (`Lane \| Steps \| Holds \| Runs beside`) | adapt: a repository column replaces the test-slot column | superproject runbook §3a | R-3 | — |
| RC-A5-10 | `DR6` §3 rows `dr6-26`…`dr6-28`, §3a @ `eae340a` | waves are event-driven; merge points are procedure steps with ledger rows | adapt: boundaries `R-4.<k>`, one per wave, with the ritual of §7.4 | superproject runbook §3, §3a, §L | R-3, R-4 | — |
| RC-A5-11 | SOURCE-R `QUESTION-PACK_round-6_2026-10-03.md`; `ANSWERS_*` | pack conventions: one-line answer, what changes, settled list, Source, †, verbatim + time + Reading | adapt into §O and the register (§7.3) | superproject runbook §O; `rework/REGISTER_operator-questions_2026-10-13.md` | R-3 | Q-A5-03 |
| RC-A5-12 | `CN` §6a | a "what a non-(a) answer changes" table | adopt verbatim as a §Q sub-table | superproject runbook §Q | R-3 | — |
| RC-A5-13 | `CN` §2 rule 2; `MG2:418` | gates asked in chat in text, work continues, no blocking question tool | adopt | superproject runbook §2 | R-3, R-4 | Q-A5-04 |
| RC-A5-14 | `RBS` §3.2 row 8; `MG2` §8 | an adversarial round on the draft by one fresh read-only reviewer, findings table | adopt (more than 10 steps) | superproject runbook §R | R-3 | — |
| RC-A5-15 | `RBS` §3.1 row 5; `MG2` §5 | owed items `# \| Item \| Source \| Discharged at \| Status` | adopt as §3b (seeded with `OB` §N's six notes, `M-8`, `M-9`, K-7, onboarding step 6's hold) | superproject runbook §3b | R-3 | — |
| RC-A5-16 | `ORCH` `run`, `launch`, `NUDGE` | headless launch flags; a headless turn's end kills background readers | adapt: the orchestrator note carries the flags; blocks say "subagents in the foreground" | superproject runbook §2, §3 notes | R-3, R-4 | — |
| RC-A5-17 | SOURCE-K `templates/RUNBOOK_TEMPLATE.md` (0.2.1) | the local runbook family's template (the skeleton's actual ancestor) | keep PlantLibrary's: it stays the base where the Conductor contract is silent (Watch, cwd line, "never does" wording) | superproject runbook | R-3 | — |
| RC-A5-18 | SOURCE-K `templates/HANDOVER_CONTINUATION_TEMPLATE.md` | a HANDOVER whose continuation is a prompt-shaped block with no proof surface | adopt verbatim for every stop HANDOVER and C1's | superproject `handovers/` | R-4, C1, R-5 | — |
| RC-A5-19 | `RBS` §7 (skill draft 0.1.0) | the `runbook` skill | record only: installed nowhere; the Conductor's `OP-RB` is open; `B1` decides at its time | superproject `.claude/skills/` (not now) | B1 | Q-A5-01 |
| RC-A5-20 | `TC:1086`, `BP:12905` | the `RUNBOOK_` type and the `PROMPTS_` cutoff | keep PlantLibrary's `PROMPTS_` (kit 0.2.1 enum and scan, `HC:674`) | all seven `hygiene/` | R-3, B3 | Q-A5-02 |
| RC-A5-21 | `QP:894-901` | the Codex freeze stated inside the operator-act rules | record only (`A1`/`B1`'s, `Q-G-09`) | — | B1 | — |
| RC-A5-22 | `RC` §9, §10 | the hand-back: the next runbooks written, the board re-pointed (`Lane \| Your next act \| Where the prompt is \| My recommendation`) | adapt for C1 (the suites' packages instead of runbooks) | superproject runbook §3 lane C1 | C1 | — |
| RC-A5-23 | `CN` §2 rule 13; `RBS` §3.7 | close: last flips, §0 "closed `<date>` at `<sha>`", INDEX line `history` | adopt | superproject runbook §0, `rework/INDEX.md` | R-5 | — |
| RC-A5-24 | `QP` §6 `qi-1` | two-phase integration: phase 1 writes the pack, phase 2 resumes with the answers | adapt: R-3 writes the open set in §O's pack form; each answered row releases its steps at the next boundary | superproject runbook §O | R-3, R-4 | — |
| RC-A5-25 | `QP:170-172` | named events in preconditions | adapt (`event:wave-<k>-merged`, `event:Q-…-answered`) | superproject runbook §3 | R-3 | — |
| RC-A5-26 | `H1112:50-51`; `QP:136` | the drained boundary | adapt: "drained" means no running write session in the repository, its checkouts clean, Conductor instance 2 untouched | superproject runbook §3a | R-4 | — |
| RC-A5-27 | `QP:1799` | an `INDEX.md` conflict resolves as a union of lines | adopt | superproject runbook §3a | R-4 | — |
| RC-A5-28 | `HR:615-616` | two commit lines in a submodule block | adapt: the block keeps the repository's line; the superproject line moves to the orchestrator note | superproject runbook §3 | R-3 | — |
| RC-A5-29 | `MG2:687-707` finding 1 | an adversarial finding: "a fence named a proof surface — moved to the orchestrator note" | adopt as a §R checklist item (with `HC`'s two detectors read, never run against a test runner) | superproject runbook §R | R-3 | — |

## 4. Questions for the operator

| ID | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A5-01 | The Conductor's planned operator act `OP-RB` copies its draft `runbook` skill into `PlantLibrary_Workspace\.claude\skills\runbook\` (`QP:1763`). Should that copy happen during this program? | (a) Hold that half of `OP-RB` until `B1` closes. `B1` then decides the runbook skill for all seven repositories from the reuse register (record only today). (b) Let `OP-RB` write it whenever it runs, and `B1` adapts after. (c) `B1` installs the draft now. | One writer per repository (`KO:26`). The skill is not installed even in the Conductor (`TC:1086` todo), and a copy landing mid-lane would collide with `B1`'s mirror and parity work. | the `B1` steps that write `PlantLibrary_Workspace/.claude/` |
| Q-A5-02 | Runbook file names: keep `PROMPTS_` or adopt the Conductor's `RUNBOOK_`? | (a) Keep `PROMPTS_` for this runbook and any lane runbook. The kit 0.2.1 enum and its proof-surface scan reach `PROMPT_`/`PROMPTS_` only (`HC:674`). (b) Add `RUNBOOK` by `enum-add` decision entries in all seven repositories now. | Under (b), a `RUNBOOK_` file escapes the proof-surface scan until a kit patch. Today the Conductor itself still writes `PLAN_` and `PROMPTS_` (`MG2:5-8`). | R-3 (lane-file names), `B3` (enum) |
| Q-A5-03 | May the operator session accept one-line answers ("all recommended", or "all recommended except Q-G-05 (b)")? | (a) Yes. Each row is recorded with the operator's words, the UTC time, how it was asked, and a Reading line where needed. (b) No: every row is answered on its own. | It is the proven pack form (`QP6:15-20`; `CN:632` records "operator's advance answer 'all recommended'"). It keeps the sitting short, and the verbatim record stays exact. | §O only |
| Q-A5-04 | When you are present in the orchestrator's chat, may it put an open question to you there, as well as in §O sessions? | (a) Yes. It asks in text and keeps working, and the answer is recorded verbatim in the register and §Q in the next commit. (b) Only through §O sessions. | It is the Conductor's practice (`CN:196-200`). Steps that wait are released one boundary sooner. | any `waits Q-…` step |

## 5. Reusable things this brief did not name

- The kit's `templates/RUNBOOK_TEMPLATE.md` (`KRT:1-109`). The R-0 skeleton is effectively its instance, and it carries the `Ledger (<where>, separate commit …)` line (`KRT:86`) that this program's flip rule replaces.
- The kit's `templates/HANDOVER_CONTINUATION_TEMPLATE.md` (`KHT:29-42`): the shape of every stop HANDOVER required by `KO:31`.
- `orch.py` (`ORCH:47-61` block extraction from the committed file, `ORCH:94-96` headless argv, `ORCH:177-191` step-until-flipped, `ORCH:82-87` NUDGE). It lives out of the repository and is read-only. It is the reason for the third-cell status rule.
- The question pack and answer files in SOURCE-R (`QP6`, `AN6`, `AOG`): working models for §O's pack and the register's answer record.
- `DR6` §3a's waves and merge points (`DR6:117-120`, `DR6:135-147`): the closest precedent for this program's waves.
- `CN` §6a (`CN:611-622`): the "what the other answers do" table.
- `RC` §9–§10 (`RC:1091-1150`): the hand-back precedent.
- `MG2` §8 (`MG2:687-707`): a worked adversarial round. Its thirteen findings are a ready checklist (a proof surface in a fence, unconditioned steps, a missing INDEX line, overlapping lanes, an off-home flip).
- `QP:112-116` rule 9: the proof-surface detectors may be called as plain functions to check a new prompt text, never by a test run.
- `ORCH:65-69` `claude agents --json --all`: the read-only way to see which sessions run, which helps the drain check at a boundary.

## 6. Claims to verify

1. **The submodules have embedded `.git` directories, and there is no `.git/modules`.** Check (read-only, under a minute):
   `git -C C:\Programmierung\SW_Development\PlantLibrary_PyApp rev-parse --git-dir --git-common-dir` should print `.git` twice, and `Test-Path C:\Programmierung\SW_Development\.git\modules` should print `False`.
2. **The proof-surface scan reads only `PROMPT_`/`PROMPTS_` basenames, in planning and general roots, and the argv detector has no negation guard.** Check: read `C:\Programmierung\SW_Development\scripts\hygiene\repo_hygiene_check.py` lines 654–692. Line 655 returns early only on a missing runner name or a sanctioned launcher. Lines 671 and 674 restrict the scan.
3. **The Conductor's `RUNBOOK_` row is still `todo`, the runbook skill is installed in neither repository, and `OP-RB` plans a copy into `PlantLibrary_Workspace`.** Check:
   - `git --no-optional-locks -C C:\Programmierung\Orchestrator_System show HEAD:implementation/Conductor_V2/TASK_CHECKLIST.md | Select-String "CD-V2-HRN-142 \| todo"` should give one hit.
   - `Test-Path C:\Programmierung\Orchestrator_System\.claude\skills\runbook` and `Test-Path C:\Programmierung\SW_Development\PlantLibrary_Workspace\.claude\skills\runbook` should both print `False`.
   - Line 1763 of `C:\Programmierung\Orchestrator_System\implementation\Conductor_V2\planning\PROMPTS_quality-program_2026-10-02.md` names the `PlantLibrary_Workspace` path.

## 7. The template

### 7.1 The runbook, section by section

The sections keep the kickoff's fixed names (`KO:35` d): §0, §1, §2, §3, §3a, §Q, §O, §L. The Conductor contract's other required parts enter as lettered sections after the section they extend (`RBS:233`): §2a ladder, §3b owed items, §R adversarial round, §H history. Final order: §0, §1, §2, §2a, §3, §3a, §3b, §Q, §O, §L, §R, §H.

**§0 — What this is, and what it is not.** A two-column table, rows in this order:

| Row | Content |
|---|---|
| Scope | as `SK:13` |
| Not here | batch-package content (the packages are truth); decision texts (`STATE.md`, `hygiene/HYGIENE_DECISIONS.md`: cited by id, never copied); analysis findings (their `AUDIT_`/`REGISTER_` files); the Conductor's runbooks; Phase C batch runs |
| Tag | `rw` — step ids are `<lane>-<n>` per §2 rule 2 |
| Home branch and absolute path | superproject `master` — `C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md`. Every other checkout and worktree reads it by this path, read-only |
| Roots | as `SK:14` |
| Ledger of record | §L here, nowhere else; flipped in the commit that carries the step's output, or, for a step whose output commits outside the superproject `master`, in the orchestrator's gitlink-and-flip commit (§2 rule 4). Questions: the register of record, mirrored in §Q in the same commit. Deferred validations and reuse verdicts: their registers |
| Inputs (decision ids) | `D-2026-10-13-01` (root `rework`); each answered `Q-…` row by id; each `D-…` a step writes, appended as it lands |
| What this file never does | name a proof surface or a test invocation; widen, delete or rewrite a validation cell; carry status outside §L; copy a block from another file (it points); put a launch value inside a fence; decide (every choice is a `Q-…` row or a `gate` step); write a source; push |
| Closed | (added at `R-5`) `closed <date> at <sha>` |

**§1 — Where things stand — measured at `<sha>` on `<date>`.** A table `Fact | Measured`, ≤ 15 rows, each a world fact measured at that SHA. It is rewritten whole when three days old or when a lane closes (`KO:63`, `MG2:50`), never appended. It holds no step status and no "(was: …)". Another runbook's ledger is cited by pointer ("its §L says"), not restated.

**§2 — Rules.** The first paragraph is the one-line summary of the kickoff's ten rules by reference (`SK:39-48`, kept). Then the file rules, numbered so blocks can cite "§2 rule n":

1. **Paste protocol.** One fresh session per step. Set the model and effort from the step's model line before launching, then paste the fence unchanged. Launch values go in the orchestrator note, never in the fence. The **Watch** paragraph is for the orchestrator and the operator and is never pasted.
2. **Ids.** `<lane>-<n>`, in run order within a lane (`B1-1`, `B1-2`). An insert after `P` is `P.1`, and between `P.1` and `P.2` it is `P.1.1`. Parts (a split or a fan-out) are letters, and the parent becomes `split`. A re-run keeps its id and is noted `-r<k>` in the run name and the Note. Ids are never renumbered or reused. Parallel sub-lanes carry a fixed letter from §3.1 (`A6a`…`A6g`, `A9a`…`A9c`). Orchestrator boundaries are `R-4.<k>`. Gate steps are lane steps whose title starts with the gate name (`B5-3 — G-DS: …`).
3. **Fill rule.** The ledger's Status and Decision take what the step produced: the short SHA and the D-id, never a planned value. A block names an earlier step's outcome by pointer ("the commit §L row `B1-1` records").
4. **Flip rule.** A step whose output is a superproject commit on `master` flips its own row in that commit. Any other step's final message names its row (`| \`<id>\` | <title> | done <date> — <repo> <sha> | <D-id or —> | <note> |`), the submodule commit its gitlink takes, and its proposed register rows. At the boundary the orchestrator writes one superproject commit per step carrying the gitlink, the flip and those rows (§3a).
5. **Sync rule.** One home branch (§0). No other branch or worktree edits this file. A lane that reads it does so by absolute path.
6. **Questions and waits.** A step with `waits Q-…` is skipped until the register records the answer verbatim. A step written "if Q-… (a)" is `retired` by any other answer. An answer outside the options is recorded verbatim, together with the step the orchestrator inserts. No session asks through a blocking question tool. A lane that meets an unsettled choice proposes a `Q-<lane>-<nn>` row in its report and continues with everything that does not depend on it (`KO:28`, `CN:196-200`, `CN:227-229`).
7. **Launch.** The step's route says how it runs. `session (headless)`: `claude -p` from the step's cwd, with `--model <family id>` (`claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`), `--effort <low|medium|high|xhigh>` and `--permission-mode <mode>`, written in the orchestrator note. `session (paste)`: an interactive session. `subagent`: spawned by the orchestrator, with worktree isolation when it writes. In a headless session subagents run in the foreground, because an ended turn ends the process (`ORCH:82-87`).
8. **Boundaries.** Every wave ends in an `R-4.<k>` procedure step that runs §3a's ritual. A worktree merges only there.
9. **Size and close.** Past about 900 lines, the largest lane moves to a pointed lane file `rework/PROMPTS_<lane-topic>-runbook_<date>.md`, and its §3 row reads "pointed". At `R-5` the §L rows are complete, §0 gains "closed", the `rework/INDEX.md` line turns `history`, and §1 is final.

**§2a — Model · reasoning ladder.** A table `Shape | Model · reasoning | Reason`, from kickoff rule 9 (`KO:30`):

| Shape | Model · reasoning | Reason |
|---|---|---|
| orchestrator | Fable 5.1 · high, xhigh for `R-3` | one Fable session at a time |
| read-only analysis | Opus 5.5 · high | breadth with a written schema |
| mechanical census | Sonnet 5.5 · high | fixed method |
| execution | Opus 5.5 · high | bounded, recorded work |
| IA, mockups, design decisions | Opus 5.5 · xhigh | a wrong design costs weeks |
| operator sessions | Opus 5.5 · high | |

Then the substitution rule. If Fable is unavailable, use Opus 5.5 · xhigh plus one fresh-context adversarial review (`QP:1951-1952`, `HR:949-952`). Every Sonnet subagent is Sonnet 5.5. Never Haiku for a session (`MG2:637`).

**§3 — Lanes and step map.**
- **§3.0, the row shape.** As `SK:57-66`, plus the `Block` field.
- **§3.1, the lanes.** As `SK:70-81`, plus a `Sub-lanes` column.
- **§3.2, the step map.** One table in run order: `Step | Title | Model · reasoning | Route | Where (cwd · branch) | Precondition | Writes | Waits | Block`.
  - Route ∈ `session (headless)` · `session (paste)` · `subagent` · `procedure` · `gate` · `operator` · `plan` (a `/plan-batch` act; allowed for `B4` and `C1`, with the package's own validation cells untouched) · `check` (read-only).
  - `batch` is not a route in Phases A or B (`KO:25`).
  - Block ∈ `§3.<n> <id>` · `procedure: §3a boundary` · `none (operator)` · `pointed: <file> §<n>`.
  - No status column.
- **§3.3 and on.** One subsection per lane (`### 3.3 Lane B1 — …`). Each step in it has exactly this shape:

````text
#### `<id>` — <title>

**Model · reasoning:** <Family x.y> · <effort> · **Route:** <route> · **Where:** `<absolute cwd>` on `<branch>` (from `<base branch>`) · **Precondition:** <ids done; events> · **Writes:** <repositories and files> · **Waits:** <`Q-…` ids, or —>

```text
<the paste block of §7.2>
```

*Orchestrator note (outside the block):* <launch values: base SHA, the worktree created and its free-disk reading, the
headless flags, free D-id candidates in the step's repository, the answers quoted when a gate records them; the
superproject commit line `rework: <id> - bump <repo> gitlink; ledger <id>`>.
**Watch:** <traps; what a defective result looks like; when to send it back — never pasted>.
````

A gate step uses the same shape. Its block records answers the orchestrator collected, and they arrive in the orchestrator note, verbatim (`CN:461-478`). A gate is also a `Waits` source for later steps.

A step that declares a root, an exemption, a hold, a release, an allowlist entry or an enum extension writes one entry in its repository's `hygiene/HYGIENE_DECISIONS.md` in the shape of `HD:33-45`:
- `### D-<date>-<nn> — <title>` under a dated `##` heading;
- `Authority:` this runbook's step id and the `Q-…` answer quoted verbatim;
- the preconditions measured, with the verdict line before the step;
- numbered dispositions;
- the directive lines;
- the commit line.

The D-id is the next free one by grep over that repository. Every candidate goes in the orchestrator note; the block says "the next free id".

**§3a — What may run beside what.** Four parts:

1. **The occupancy rule.** One writer per repository at a time, in place. A second lane on the same repository gets a worktree (§7.4). The superproject is never written from a worktree: its submodule folders would be empty. The superproject's in-place writer is either one superproject lane (`B1`, `B2`, `B3`, `B7`, `B8`, `C1` in their superproject steps) or the orchestrator's boundary commits, never both at once. At most four write sessions beside the orchestrator. One Fable session at a time. Read-only lanes are unlimited (`KO:27`, `QP:906-908`). A new worktree needs C: free ≥ 20 % (`KO:18`).
2. **The lane table.** `Lane | Steps | Repositories written | Checkout (in place / worktree <path>) | Runs beside | Never beside`.
3. **The repository matrix.** Seven rows (the superproject and the six submodules) by the lanes. Each cell is `W` (writes in place), `wt` (writes in a worktree), `r` (reads) or `—`. It is static and is never a status.
4. **The waves.** A numbered list in the style of `DR6:135-147`. Each wave names its steps, the event that starts it, the `R-4.<k>` step that closes it, and that boundary's push list for the operator (`Q-G-03` (a)).

**§3b — Owed items.** A table `# | Item | Source | Discharged at (step) | Status`, where "none" is written as a row (`RBS:244`). Seed it with:
- the six notes of `OB` §N (`OB:927-934`);
- `M-8` and `M-9` (`HR:986-987`);
- K-7 (`Q-G-06`);
- onboarding step 6's hold (`OB:912`);
- `OP-RB`'s PlantLibrary copy (Q-A5-01).

**§Q — Operator questions, mirror of the register.**
1. The mirror table: `ID | Question (short) | Recommended | Waits | State | Answer (verbatim, date)`, as `SK:97`.
2. Under it, "What a non-(a) answer changes": `Answer | Effect on the steps` (`CN:611-622`). A retired step counts as met in every later precondition (`CN:622`).
3. Under that, "Settled, not asked again": `Item | Where it is settled` (`QP6:54-64`).

**§O — The operator session.** The R-0 block (`SK:114-128`) with the improvements of §7.3. Its shape is under §7.3 below.

**§L — Ledger, flip as you go.** One line above the table gives the status vocabulary, exactly:

`todo` · `running (<session name>)` · `done <YYYY-MM-DD> — <repo> <sha>[; <repo> <sha>]` (the superproject commit that carries the flip is "this commit") · `waits Q-<lane>-<nn>[, …]` · `held (<what holds it, by id>)` · `skipped (<why>)` · `split → <id>a, <id>b` · `retired <YYYY-MM-DD> (<Q id or D-id>)`.

Then the table `Step | Title | Status | Decision | Note`, one row per step id in step-map order: `R-0`…`R-5`, every lane step, every gate step, every `R-4.<k>`. Decision holds a D-id or `—`. Note is ≤ 160 characters, and anything longer goes to the step's deliverable or the HANDOVER (`RBS:246`). A session that died short of context keeps its row at `running (<session>)` until the restart, and the Note says "attempt k".

**Gate rows.** A gate is a step in the lane where the decision falls. In the map: Route `gate`, Model "operator; Opus 5.5 · high records", Block its recording block, Waits its `Q-…` ids. In §L it is an ordinary row, flipped `done <date> — this commit` with the answer's register id in Note.

**Wave boundaries.** `R-4.1`, `R-4.2`, … are procedure steps in the map: Route `procedure`, Model "Fable 5.1 · high", Block `procedure: §3a boundary`, Writes "every repository merged at it; superproject gitlinks and flips". Each has its own §L row.

**§R — Adversarial round on this draft.** Before the first lane step: one fresh-context, read-only reviewer (Opus 5.5 · high, or a Sonnet 5.5 subagent) with this §7 as its checklist. The table is `# | Finding | Resolution`. The checklist includes every block against `HC:654-664` (read, never run), every precondition resolvable, lanes partitioned in §3a, and every `waits` naming a register row (`MG2:687-707`).

**§H — History.** Blocks of retired steps, moved here whole.

### 7.2 The paste block

````text
```text
<id> — <title>
<one-sentence goal: what this step delivers>.
Context: step <id> of C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md (§3, lane <lane>), read by that absolute path and never edited; the program's rules are §2 of C:\Programmierung\SW_Development\rework\PROMPT_master-rework-kickoff_2026-10-13.md; the answers this step rests on: <Q-ids, by id>; the register and audit rows it executes: <ids>.
Where: cwd <absolute cwd> on branch <branch>. This session writes only this repository<, in this worktree>; it never runs a git write command in, and never writes, any other checkout, the superproject's registers included.
Scope: <what is delivered>; not here: <what it does not touch>.
Read first: <files and sections, narrowly; SOURCE paths by absolute path; git reads in SOURCE-C with --no-optional-locks>.
Write: <the exact files this step creates or edits, and nothing else>.
Constraints: sources read-only; no test of any kind, no app launch, no build for validation — a needed validation goes into the final message as a proposed deferred-validation row (what, by which skill, for which change, after which lane); line endings as found (git ls-files --eol before the commit, no text-mode rewrite, no core.autocrlf change); a package edit follows plan-batch's row schema with a dated decision in that package's STATE.md, and no validation cell is widened, deleted or rewritten; the repository's hygiene/HYGIENE_DECISIONS.md takes the next free D-id by grep for any root, hold, release or allowlist change; subagents run in the foreground; no push; <step-specific>.
Questions: a choice this block does not settle goes into the final message as a proposed Q-<lane>-<nn> row (question, options with (a) recommended, why (a), which steps wait); continue with everything that does not depend on it; never ask through a blocking question tool.
If the context runs short: commit what is complete, mark the rest "not read" or "not done" in the deliverable, and stop; the same block is restarted as <id>-r2.
Done when: <observable end state>; this repository's hygiene verdict (the kit's INSTALL.md, Verify section) shows zero violations; one commit on <branch>; the final message gives the §L row for the orchestrator, the commit the gitlink takes, and the proposed register rows.
Commit line: <repo prefix>: <id> - <summary> - <n> <counters>
```
````

- **What the fence never contains.** A proof surface. No test runner name, no tests-root argument, no selection flag, no whole-suite phrase, no named validation command, no harness invocation. No instruction to widen, delete or rewrite a validation cell. No input placeholder: base SHA, D-id, an earlier step's commit or a worktree path that is not the convention's. No status or count measured after writing. No model or effort, which go on the model line above the fence. No launch flag. No Windows path inside an inline script. A done-when cites the verdict of the document that owns verification (`KHT:5-7`). It never spells how to produce it.
- **Model and effort for a headless lane.** The bold line above the fence says, for example, `Opus 5.5 · high · **Route:** session (headless)`. The orchestrator note turns it into the launch: `claude -p --model claude-opus-5-5 --effort high --permission-mode <mode> --output-format stream-json` started in the `Where` cwd (rule 7). The flags are the orchestrator's to fill. The block never names them, so the same block also serves an interactive paste.
- **Worktree cwd per rule 5.** The `Where` line names `C:\Programmierung\SW_Development_wt\<repo>-<lane>` on `rework/<lane>` (from `main`) when §3a gives the step a worktree. Otherwise it names `C:\Programmierung\SW_Development\<repo>` on `main` (in place), or `C:\Programmierung\SW_Development` on `master`. Both are conventions known when R-3 writes the block, so they are not input placeholders. The base SHA is one, and goes in the note.
- **Repository prefixes for commit lines.** In submodules: `rework: <id> - …` (one prefix across all seven; the submodule's own history then shows the program). The orchestrator's superproject line: `rework: <id> - bump <repo> gitlink; ledger <id>`.

### 7.3 The question register

**Columns** (register of record, `rework/REGISTER_operator-questions_2026-10-13.md`): `ID | Question | Options | Why (a) | Waits | Source | When | State | Answer (verbatim, date) | Reading`.
- `Source` is the `AUDIT_`/`REGISTER_` row or step that raised it (`QP6:93`).
- `When` is the latest step it must be answered before, which is the ordering key for §O (`QP6:78-81`).
- `Reading` is empty unless the answer departs from the options (`AOG:28-31`).

**ID scheme.** `Q-<lane>-<nn>`, two digits, never reused:
- lane `G` for program-wide rows (the kickoff's nine);
- `A1`…`A9`, `B1`…`B8`, `C1` for rows a lane raises;
- sub-lanes use their fixed letter (`Q-A6c-01`);
- `R` for the orchestrator's own rows.

**State vocabulary.** `open` · `answered` · `withdrawn (<why>)` · `superseded (<Q id>)`. The first three are from `QR:18`; `superseded` is new, for a question folded into another.

**The verbatim rule.** The Answer cell holds:
- the operator's words unedited, in quotes;
- the date and UTC time;
- how it was asked (`§O session <name>` or `orchestrator chat`).

`(a)` alone means "as recommended" only when the operator said exactly that. When the operator answered in one line for many rows ("all recommended except …"), each row quotes that line and names the option it resolves to. An answer outside the options is quoted whole, with a Reading line and the step the orchestrator inserts (`MG2:164`). The register commit and the §Q mirror are the same commit.

**The Conductor's conventions that improve on R-0's seed (deltas).**
1. **Source column.** It says where the question came from and what to read before answering (`QP6:24`, `MG2:172` "Evidence").
2. **When column and grouping by when it blocks.** §O asks in that order ("A. Blocks the next wave", "B. Blocks a later lane", "C. Informational") (`QP6:78`).
3. **One-line answer form.** "all recommended", or "all recommended except Q-G-05 (b), Q-A5-02 (b)" (`QP6:15-20`; Q-A5-03).
4. **"What changes if you answer all recommended".** A summary of ≤ 10 lines at the top of the open set, which §O reads out first (`QP6:22-33`).
5. **"What a non-(a) answer changes".** The §Q sub-table (`CN:611-622`).
6. **† marker.** It marks a recommendation that is the orchestrator's own where the raising lane gave none, or two lanes disagree, and it says what it departs from (`QP6:10-13`).
7. **"Settled, not asked again" list.** It stops re-litigation (`QP6:54-64`).
8. **Facts checked before asking.** The operator session first runs the read-only checks a question depends on and reports them (`AN6:6-14`).
9. **Context as put.** The record keeps the one-paragraph "Put:" text the operator saw (`AOG:8-14`).
10. **UTC time and a Reading line.** `AOG:16-17`, `AOG:26-31`.
11. **"If Q (a)" steps are retired by any other answer.** They take `retired` in §L with the Q id (`MG2:45`).
12. **Chat asking (Q-A5-04).** When the operator is present, the orchestrator may ask in its chat, in text, while it keeps working. The record is identical (`CN:196-200`).

**§O shape** (the R-0 block with these deltas, written as a fenced block under §O; no proof surface):

```text
You are the operator session of the PlantLibrary master rework program (cwd C:\Programmierung\SW_Development, branch master).
Scope: put every open row of rework/REGISTER_operator-questions_2026-10-13.md to the operator, record the answers verbatim, flip the rows, mirror them in §Q of rework/PROMPTS_master-rework-runbook_2026-10-13.md, and commit.
Read first: the register (Why (a), Source, When); the runbook §0, §1, §Q (its "What a non-(a) answer changes" and "Settled" tables); for each question, the row its Source names, nothing wider.
Order: open with the "What changes if you answer all recommended" lines; then the rows grouped by When (the next wave first), Q-G-02 and Q-G-03 at the head.
For each row: first the read-only fact checks it depends on, reported; then two plain sentences on what is decided, (a) and why, the other options and what each costs, which steps wait. The operator may answer the whole set in one line ("all recommended", or "all recommended except <ids with options>").
Record: per row the operator's words in quotes, the date and UTC time, "asked in <this session's name>", the option it resolves to, and a Reading line where the words depart from the options together with the step the orchestrator must insert; State answered.
Constraints: never answer a question yourself; edit only the register and the runbook's §Q; no test of any kind; push only when the operator says so in this session (the end-of-wave push list is in §3a): plain git push of the superproject and each named submodule's main, nothing forced.
Done when: every row the operator answered reads answered with the words, time and Reading; §Q mirrors it in the same commit; the superproject hygiene verdict shows zero violations; the commit is made.
Commit line: rework: operator - questions answered <date> (<ids>)
```

### 7.4 Waves and worktrees

**The Conductor's boundary ritual,** as read:
- a *drained* boundary: dispatch paused, no open run, read-only store reads (`H1112:50-51`, `QP:136`, `QP:1806-1807`);
- the merge, then `pushall.sh` (`MG2:49`, `H1112:87`);
- the re-stamp only between batches (`H1112:52-53`);
- the ledger flipped in the merge or an `ops` commit (`MG2:46`);
- worktrees removed after their merge is on `origin` (`QP:94-95`, `QP:1804`);
- `INDEX.md` conflicts resolved as a union (`QP:1799`);
- §1 refreshed when three days old (`MG2:50`);
- disk read before a new worktree (`H1112:94-96`).

**Adapted to seven repositories with gitlinks.** Each `R-4.<k>` step runs these in order:

1. **Drain.** For every repository with work in this wave: no write session of this program running in it (`claude agents --json --all` read-only, or the orchestrator's own session list), and `git -C <checkout> status --porcelain` empty in its main checkout and in each of its worktrees. Conductor instance 2 is never touched (its PyApp intake is held at `PY1-B08`; `OB:912`).
2. **Re-read the register** (`KO:28`). For each newly `answered` row: flip its waiting steps from `waits Q-…` to `todo` (or `retired` per §2 rule 6), and update §Q and §O. Both go in the boundary's first superproject commit.
3. **Merge each worktree branch, repository by repository.** For a submodule `<repo>` and lane `<lane>`, the main checkout is `C:\Programmierung\SW_Development\<repo>` on `main`:
   ```text
   git -C C:\Programmierung\SW_Development\<repo> merge-base --is-ancestor main rework/<lane>
   (exit 1 only: git -C C:\Programmierung\SW_Development_wt\<repo>-<lane> merge --no-edit main   — a conflict stops the boundary for that repository: FINDING, HANDOVER)
   git -C C:\Programmierung\SW_Development\<repo> merge --ff-only rework/<lane>
   git -C C:\Programmierung\SW_Development\<repo> worktree remove C:\Programmierung\SW_Development_wt\<repo>-<lane>
   git -C C:\Programmierung\SW_Development\<repo> branch -d rework/<lane>
   git -C C:\Programmierung\SW_Development\<repo> worktree prune
   ```
   `branch -d` refuses an unmerged branch, which makes it the safety check. Nothing is pushed here. An `INDEX.md` conflict at the merge-in resolves as a union of lines.
4. **Superproject commits, one per step, in step order.** Each carries the gitlink at that step's own commit, the §L flip, and the step's proposed register rows. When a repository merged several steps at once, an earlier step's gitlink is staged at its own commit with `git update-index --cacheinfo 160000,<sha>,<repo>`, and the last one with `git add <repo>`. Each commit is preceded by the superproject hygiene verdict. Commit line: `rework: <id> - bump <repo> gitlink; ledger <id>`.
5. **Refresh.** Rewrite §1 whole if three days old or a lane closed. Rewrite §O for the new open set. Read C: free space: below 20 %, no new worktree.
6. **Push list.** Write the boundary's push list (the superproject and each submodule whose `main` moved) into the `R-4.<k>` Note and tell the operator in two lines (`KO:31`). The push is the operator's (`Q-G-03` (a)).
7. **Open the next wave.** Create its worktrees and launch its steps (rule 6 caps), then flip `R-4.<k>` `done`.

**Creating a worktree** (static check against this layout):

```text
git -C C:\Programmierung\SW_Development\<repo> status --porcelain          (must be empty)
git -C C:\Programmierung\SW_Development\<repo> worktree add C:\Programmierung\SW_Development_wt\<repo>-<lane> -b rework/<lane> main
```

- The submodules have embedded `.git` directories (F-A5-03). Git therefore writes the admin directory to `C:\Programmierung\SW_Development\<repo>\.git\worktrees\<repo>-<lane>`, and the worktree's `.git` file reads `gitdir: C:/Programmierung/SW_Development/<repo>/.git/worktrees/<repo>-<lane>`. There is no `.git/modules` anywhere.
- `core.worktree` is unset in every submodule config, so the new worktree resolves to itself.
- `core.autocrlf=true` sits in the shared config and applies to the worktree's checkout, so it gets the same working-tree bytes as the main checkout.
- The `SW_Development_wt` folder lies outside the superproject, so the superproject's root allowlist never sees it.
- Path length: the longest tracked path is 169 characters (`PlantLibrary_Workspace`), so `C:\Programmierung\SW_Development_wt\PlantLibrary_Workspace-B3\` plus 169 stays under 260 with `core.longpaths` unset.
- Never in a worktree: `git submodule absorbgitdirs` (in any repository, while any worktree exists), `git submodule update`, or a superproject worktree.

**Branch naming.** `rework/<lane>` exactly as the lane id is spelled (`rework/B1`, `rework/A6c`, `rework/B6a`). Never create a branch named `rework` alone, because a ref cannot be both a file and a folder. Never create two names that differ only by case: loose refs are files on a case-insensitive file system (claim, not tested here). A lane with two sequential worktree steps in one repository reuses `rework/<lane>` after the first was merged and deleted.

### 7.5 Delta list for the R-0 skeleton

1. **§0, after "Scope".** Insert the row `| Not here | batch-package content; decision texts (cited by id); analysis findings (their AUDIT/REGISTER files); the Conductor's runbooks; Phase C batch runs |`.
2. **§0.** Insert `| Tag | \`rw\`; step ids \`<lane>-<n>\` (§2 rule 2) |`.
3. **§0.** Insert `| Home branch and absolute path | superproject \`master\` — \`C:\Programmierung\SW_Development\rework\PROMPTS_master-rework-runbook_2026-10-13.md\`; every other checkout reads it by this path, read-only |`.
4. **§0.** Insert `| Inputs (decision ids) | \`D-2026-10-13-01\`; answered \`Q-…\` rows by id as they land |`.
5. **§0 "Models" row.** Replace with `| Models | §2a; every §3 row names its own |`. **§0 "What this file never does".** Append "Carry status outside §L. Copy a block from another file. Put a launch value inside a fence. Decide."
6. **§1 heading.** Change `SK:19` to `## 1. Where things stand — measured at \`8702e0a\` on 2026-10-13` (or the SHA of the R-3 commit's parent when R-3 re-measures). Add "≤ 15 rows, rewritten whole, no step status".
7. **§1 row "Two prior tracks"** (`SK:35`). Reword as pointers: "their own §L ledgers (`repo-hygiene/…` §L, `onboarding/…` §L) are of record; owed items in §3b".
8. **§2.** After the one-line summary (`SK:39-48`), append file rules 1–9 of §7.1.
9. **New §2a.** Add the model · reasoning ladder of §7.1 with the substitution rule.
10. **§3.0** (`SK:57-66`). Split "id · title" into two fields, add `Block` and `Waits` rows, and replace the route row with the route vocabulary of §7.1 (adding `session (headless)`, `session (paste)`, `plan`, `check`; `batch` excluded).
11. **§3.1** (`SK:70-81`). Add a `Sub-lanes` column: `A6a`…`A6g` (superproject, Workspace, PyApp, AndroidApp, Dashboard, Server, SharedContracts), `A9a`…`A9c` (Dashboard, AndroidApp, PyApp), and `B6a`…`B6c` if `B6` fans out per client.
12. **§3.2** (`SK:83-85`). Replace "To be written at `R-3`" with the step-map header `| Step | Title | Model · reasoning | Route | Where (cwd · branch) | Precondition | Writes | Waits | Block |`, plus one subsection per lane carrying the per-step shape of §7.1 and the block of §7.2.
13. **§3a** (`SK:87-90`). Replace with the four parts of §7.1 (occupancy rule, lane table, repository matrix, waves) and the boundary ritual of §7.4.
14. **New §3b.** Add owed items, seeded per §7.1.
15. **§Q** (`SK:92-107`). Keep the mirror columns. Add the sub-tables "What a non-(a) answer changes" and "Settled, not asked again", and add `superseded (<Q id>)` to the states.
16. **§O** (`SK:114-128`). Replace the block with §7.3's §O block. Add one line above it: "If the operator is present in the orchestrator's chat, the orchestrator may put a question there (Q-A5-04); the record is the same."
17. **§L header** (`SK:132`). Replace with `| Step | Title | Status | Decision | Note |` and add the status-vocabulary line of §7.1 above it.
18. **§L row `R-0`** (`SK:134`). Rewrite as `| \`R-0\` | verify and open the track | done 2026-10-13 — \`8702e0a\` | \`D-2026-10-13-01\` | Workspace gitlink \`6b4b88b\` |`. The model moves to §3; "this commit" becomes the SHA, now known (fill rule).
19. **§L rows `R-1`…`R-5`** (`SK:135-139`). Move the model text to §3. Keep the titles. Status stays `todo` or as flipped.
20. **§L.** At R-3, add one row per lane step, gate step and `R-4.<k>` boundary.
21. **New §R.** Add the adversarial round on the R-3 draft (§7.1).
22. **New §H.** Add the history section, empty: "Retired blocks, moved here whole."
23. **Title line** (`SK:1`). Keep it. Append nothing; the tag sits in §0.
24. **Italic preface** (`SK:3-7`). Append "A finding made while following it goes to its own `FINDING_`/`AUDIT_` file and an inserted step, never into this file as a chapter" (`QP:10-11`, `RBS:803-805`).
25. **`rework/REGISTER_operator-questions_2026-10-13.md`.** Add the columns `Source`, `When` and `Reading` to "How to read a row" and to the table header. Add the `superseded` state. Add the verbatim rule's wording of §7.3.
26. **`rework/REGISTER_deferred-validations_2026-10-13.md`** (`DVR:11-21`). Add one sentence: "Rows are written by the orchestrator from the lane's report in the step's flip commit; a lane outside the superproject never writes this file."
27. **`rework/INDEX.md`, the runbook's line.** At R-3, change it to name the added sections (§2a, §3b, §R, §H).
28. **Kickoff rule 1 and rule 7 (`KO:22`, `KO:28`).** These are not edited (the kickoff is the verbatim prompt). The runbook's §2 rule 4 and rule 6 carry the "lanes propose, the orchestrator writes" reading, citing F-A5-18.
29. **The sentence "the superproject bumps gitlinks in one commit per step"** (`KO:26`). §7.4 step 4's `update-index --cacheinfo` form keeps it exact when one repository merged several steps at one boundary.
30. **Write the R-3 text with no runner name at all.** That covers §2, §3, §O, C1 and every Watch paragraph. Keep the whole-suite wording out, even when negated (F-A5-04).
31. **§3.1 lane `C1` row** (`SK:81`). Append "the hand-back table replaces `SUITE_HANDOFFS.md`'s run-next table and the two sequencers as `Q-G-05` decides; the C1 resume prompt is a block of §7.6's shape".
32. **§3.1 lane `B1` row** (`SK:73`). Append "the Conductor's `OP-RB` copy into `PlantLibrary_Workspace` as Q-A5-01 decides; the runbook skill stays record-only (RC-A5-19)".
33. **§0 "Ledger of record" row** (`SK:15`). Append "; for a step whose output commits outside the superproject `master`, in the orchestrator's gitlink-and-flip commit (§2 rule 4)".
34. **Size check at R-3.** If the file passes about 900 lines, lane `B6`'s steps move to `rework/PROMPTS_gui-rework-runbook_<date>.md`, and its §3 rows read `pointed` (`MG2:102-104`). The INDEX line comes in the same commit.

### 7.6 The hand-back (C1)

**The Conductor's precedent.** No Conductor runbook hands a program back to package-driven batch work under that name. The nearest shape is the reconciliation runbook's Phase D:
- `rc-13` writes the next runbooks and updates the program board so that "every track's next act points into the new runbooks";
- prompts that depend on later measurements are left "not written yet, deliberately", each naming the step that writes them (`RC:1091-1136`);
- the board's shape is `Lane | Your next act | Where the prompt is | My recommendation` (`RC:1145`).

A lane closes with last flips, then §0 "closed `<date>` at `<sha>`", the INDEX line turned `history`, then the merge (`CN:236-240`). The master guide supersedes its predecessor by a §0 row (`MG2:21`).

**C1 in this runbook** is a lane subsection with these steps:

| Step | Title | Route | Writes |
|---|---|---|---|
| `C1-1` | the deferred validations planned: one `/plan-batch <suite folder> <package>` act per package that has `DV-…` rows, serialized per package | `plan` | that package (its rows, a `STATE.md` decision); the `DV-…` rows flip `planned (<batch key>)` |
| `C1-2` | the hand-back table written into this runbook's C1 subsection, and `Q-G-05`'s disposition of the sequencers applied by pointer | `session (paste)` | the superproject runbook |
| `C1-3` | the resume prompt: one block per suite | `session (paste)` | the superproject runbook |
| `C1-4` | the hand-back HANDOVER in `handovers/` | `procedure` | `handovers/HANDOVER_master-rework-hand-back_<date>.md`, its INDEX line |
| `R-5` | close (`KO:65`) | `procedure` | §0 closed, §1 final, §L complete, INDEX `history` |

**The hand-back table** has the columns `Suite · package | Next batch (key) | Why next | Requires (by id) | Attended? | Runs where (Conductor instance 2 per its binding / out of band per onboarding step 9) | Model (the batch's own line) | Deferred rows it carries (DV ids)`. It points at the packages: a package's `BATCH_PLAN.md` and `STATE.md` are truth, and the table never copies a row. Onboarding step 6's hold (`S-2`) is cited by pointer, never released by this program.

**The resume block** is in a `PROMPTS_` file, so it holds no proof surface. A `batch` route's block is two lines (`RBS:294-295`), and the row's own validation cell owns the proof.

```text
<suite> — resume validated batch work after the master rework
git -C C:\Programmierung\SW_Development\<suite folder> status --porcelain is empty; the hand-back table's row for this suite names the batch.
/run-batch <suite folder> <batch key>
```

The orchestrator note carries the batch key and its precondition check. Both are known when C1 writes it, and the block is written per suite with no `<…>` left inside.

**The HANDOVER** (`KHT:1-42`) contains:
1. what was done, per lane, with commit lines;
2. the state at handover: the seven heads, held names, open owed items;
3. open items by owner;
4. a continuation in fence form (scope, read-first, constraints, done-when, commit line, no proof surface). It names the hand-back table as the run-next and Phase C's first act as `C1-3`'s first block.
