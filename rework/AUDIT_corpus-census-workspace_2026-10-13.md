# Corpus census — PlantLibrary_Workspace — lane A6 (read-only analysis, 2026-10-13)

Pin read: PlantLibrary_Workspace `main` @ `6b4b88b` (working tree clean, 454 tracked `.md` of 774 tracked files). Paths in the tables of §7 are relative to `PlantLibrary_Workspace/`; every citation in prose is written in full as `PlantLibrary_Workspace/<path>:line`. Citer counts are `git grep -l -F <basename or folder>` hits, today: inside this repository (hygiene record and own tree excluded), in the superproject's tracked `.md` outside `rework/` (root files, `onboarding/`, `repo-hygiene/`, `handovers/`, `IMPLEMENTATION_PLAN.md`, mirrored skills), and per suite (any file, so a suite's own hygiene record counts). The Design Template Kit and the Conductor were grepped read-only where a hold names them. `Archive_PreMVP` does not exist in this repository (`git ls-files | grep -i archive` is empty); the frozen MVP material here is `implementation/System_Integration_MVP` and `implementation/System_Tooling`.

## 0. Summary

- 454 tracked `.md`: 25 byte-mirrored skill and agent files, 327 under exempt trees (205 frozen, 121 pinned, 1 generated), 102 other documents (package files, product docs, roots' files, indexes, hygiene record). Checker: `repo-hygiene: pass with holds — 0 violations, 10 held`; census 30 files in 10 declared roots, 7 compliant, 0 candidates, 12 exempt, 10 held, 3 set folders.
- Class tally of the 454 files (one row each in §7.1): live 73 (25 of them mirrors), superseded 9, archive 45, frozen 205, pinned 121, generated 1. Dispositions: nothing moves except the retired sequencers; the 45 archive files stay in compliant places.
- 16 holds in force: the 15 `held-name` lines of `D-2026-09-16-01` (6 live-package, 1 terminal-STATE, 4 pinned, 4 code) plus one prose hold on a folder (`docs/proposals/Repo_Restructure_MVP_V1_Split/`, record group, `D-2026-09-17-03` item 2). Every citer is unchanged today; none is releasable by hygiene alone.
- K-7 (kit 0.2.1, still open): it blocks exactly one pending Workspace action, the set-folder rename of the 16th hold (release at M-9 after a kit patch, a re-pin and five one-line fixes in the suites' `implementation/README.md`). It would block any move of the seven path-declared exempt trees; under the recommended layout nothing here moves them.
- Archive recommendation: one new `archive/` at the repository root declared `exempt-tree: legacy` by a new `D-2026-10-13-01`, holding only newly retired organs (`WORKSPACE_STATE.md` first, then `SUITE_HANDOFFS.md` and `V1_IMPLEMENTATION_SEQUENCE.md` once B4 has repointed 14 live files). Frozen and pinned trees stay where their existing lines declare them. `exempt-name` lines carry no existence check, so these moves do not need K-7 (`PlantLibrary_Workspace/scripts/hygiene/repo_hygiene_check.py:431-452`).
- Q-G-06 evidence: (a) is cheap in this repository; the finding already carries the ready Kit-session prompt.
- Q-G-05 evidence: `WORKSPACE_STATE.md` carries no fact that exists nowhere else; `SUITE_HANDOFFS.md` carries no unique fact but is wired into 14 live files (five checklist rows name it as their artifact), so its retirement is a B4 package edit, not a hygiene move.
- Third stale sequencer found, not named in the brief: `implementation/System_V1_Implementation/V1_IMPLEMENTATION_SEQUENCE.md` (model names Opus 4.8 / Sonnet 5 / Haiku 4.5; no citer).
- Five questions: Q-A6W-01..05; none blocks anything outside B3, B4 and B5.


## 1. Coverage

| Item | Status (read / partly read / not read) | Reason |
|---|---|---|
| `git ls-files -- '*.md'` (454) and the folder histogram | read | every file placed in one row of §7.1 (row counts sum to 454, checked by a column sum) |
| Brief: `rework/PROMPT_master-rework-kickoff_2026-10-13.md` §1, §2, §4 | read | in full |
| `CLAUDE.md` rule block, `hygiene/CONSUMED_HYGIENE.md`, `hygiene/HYGIENE_DECISIONS.md` | read | rule block and pin in full; decisions: every directive line by grep; file lines 1-260 and 273-539 read in full (entries D-2026-09-16-01 up to line 260, D-2026-09-16-02, D-2026-09-17-01/02/03); lines 261-272 (the end of D-2026-09-16-01) not read |
| Checker `scripts/hygiene/repo_hygiene_check.py` | partly read | `_apply_directive` (lines 426-470) read; `check` and `census` executed (read-only, printed) |
| `SW_Development/handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md` | read | in full |
| `SW_Development/repo-hygiene/MATRIX_rename-map_2026-09-16.md` Workspace section (§9, 239-345) | read | in full; §10, §12, §13 by grep only |
| `Repo_Hygiene_Template_Kit/KIT_SPEC.md` | partly read | §1.5-§1.9 and the §6 directive table; exempt-tree classes taken from line 212 |
| `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` §15-§17 | partly read | M-7 ledger row, M-9 step block, grep for K-7 |
| `WORKSPACE_STATE.md`, `SUITE_HANDOFFS.md`, `V1_IMPLEMENTATION_SEQUENCE.md` (lines 1-60) | read | in full except the SEQUENCE execution table below line 60 |
| Superproject `IMPLEMENTATION_PLAN.md` | partly read | §1, §3.2, §4 waves read; §5-§8 by grep |
| `implementation/System_V1_Implementation` (STATE 1-60, DRIVER_SCRIPT 1-30, SKILLS 1-12, TASK_CHECKLIST rows 26-30 and status counts) and `implementation/System_Design_Architecture` (STATE 1-15, SCOPE 1-15, DRIVER_SCRIPT 1-20, MODEL_RECOMMENDATION 1-12) | partly read | class, status and citers only; BATCH_PLAN, TASK_CONTEXT, proposal bodies not read |
| `methodology/GUI_Improvement_Methodology` (VERSION.md 1-15, folder listing) and `methodology/Design_Template_Initiative` (STATE 1-25, RUNBOOK_GUI_REWORK 1-30, INITIATIVE_CLOSEOUT 1-20, NEXT_STEPS and HANDOVER heads) | partly read | class, version and closed state; the 74 + 47 bodies not read |
| `docs/INDEX.md`, `docs/proposals/INDEX.md` | read | in full (statuses of the proposal sets are from these index lines) |
| `docs/PROPOSAL_*` sets (23), `docs/EVIDENCE_*`, `docs/PROMPT_*`, `docs/proposals/*` bodies | not read | classified from index lines and citers only |
| `MVP_Reconciliation` (README 1-20, 05 lines 80-110) | partly read | the other six files by citers only |
| `strategy/` (17), `system_description/` (138), `implementation/System_Integration_MVP` (36), `implementation/System_Tooling` (14) | not read | frozen trees; counted by the census, citers measured by grep |
| `.claude/` and `.codex/` mirrors (25 files) | not read | counted; not diffed against the superproject (lane A1/B1) |
| `docs/Fable5_Prompt_Improvements` and the HTML export | not read | not `.md`; outside the file rule |
| Cross-repository citers | read | per held name by `git grep -n -F` in the Workspace and the five suites, superproject `.md`/`.json`/`.csv`, and the Design Template Kit (read-only) |
| Todo.md | not read | not in this repository (superproject, git-ignored) |

## 2. Findings

- F-A6W-01 Checker is green with holds: `repo-hygiene: pass with holds — 0 violations, 10 held`; ten declared roots (`PlantLibrary_Workspace/hygiene/CONSUMED_HYGIENE.md:25-34`), kit `0.2.1` (`:11`), modules none (`:15`), prompt file floor 0 (`:19`). The 10 `held:` lines are the 8 in the two `proposal/` roots plus `docs/proposals/PlantLibrary_Full_Implementation_Update.md` and `prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md`; the other 5 file holds sit outside every declared root and are carried in the record only.
- F-A6W-02 The decision record has five entries and exactly 34 directive lines, all in `D-2026-09-16-01`: 7 `exempt-tree` (`PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md:134-137,141,142,161`), 12 `exempt-name` (`:146-157`), 15 `held-name` (`:182-187,191,195-198,202-205`). No `release`, `exempt-subfolder`, `held-line`, `enum-add`, `allowlist`, `retired-name`, `forbidden-path` or `scratch-root` line exists. `D-2026-09-16-02` (`:275`), `D-2026-09-17-01` (`:310`), `-02` (`:344`) and `-03` (`:393`) carry no directive line (each says so).
- F-A6W-03 K-7 mechanics read in the checker: `exempt-subfolder` and `exempt-tree` are existence-checked at the moment the line folds (`PlantLibrary_Workspace/scripts/hygiene/repo_hygiene_check.py:443-444,450-451`), `release` only accepts an earlier `held-name` (`:458-460`), while `exempt-name` (basename `:433-434`, path `:440-441`) is only added to a set, with no existence check. So moving an exempt-name file is free; moving any exempt-tree path fails `record` for ever on 0.2.1.
- F-A6W-04 The set-folder hold is real and visible only in prose: `PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md:438` (item 2 of `D-2026-09-17-03`), mirrored in `PlantLibrary_Workspace/docs/proposals/INDEX.md` ("Renamed 2026-09-17" row). The checker's `held` count does not include it (`held-name` requires a file, `repo_hygiene_check.py:420-422`).
- F-A6W-05 Two `exempt-tree` notes are stale against the tree: `methodology/GUI_Improvement_Methodology` is declared "VERSION.md 4.0.0 ... 62 .md files" (`PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md:141`) but `PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/VERSION.md:3` says 4.1.0 and the tree has 74 `.md`; `methodology/Design_Template_Initiative` is declared "live initiative (Phase 6) ... 45 .md files" (`:142`) but it has 47 and `G-close` closed on 2026-10-12 (commit `6b4b88b`). The class can be restated without K-7: a later `exempt-tree` line for the same path overwrites the class by plain dict assignment (`repo_hygiene_check.py:452`).
- F-A6W-06 The Design Template Kit pins this repository by absolute path: `Design_Template_Kit/METHODOLOGY_SOURCE.md:14` names `C:\Programmierung\SW_Development\PlantLibrary_Workspace\methodology\GUI_Improvement_Methodology\`. That tree cannot move, consistent with "live, 4.1.0, do not archive".
- F-A6W-07 `WORKSPACE_STATE.md` (63 lines, 2026-07-06) says it is superseded (`PlantLibrary_Workspace/WORKSPACE_STATE.md:3`, the pointer added by `752ff51`). It carries no unique fact (see §7.5). Live citers: `PlantLibrary_Workspace/README.md:21` (folder-map row) and three lines of the live, not-yet-bound `System_Design_Architecture` package that name it as a deliverable to update (`PlantLibrary_Workspace/implementation/System_Design_Architecture/TASK_CHECKLIST.md:56` row `SDA-QA-02`, `BATCH_PLAN.md:173`, `TASK_CONTEXT.md:339`). Frozen citers (mapping-covered, never edited): `implementation/System_Integration_MVP/{CHANGELOG.md:17,STATE.md:80,105,TASK_CHECKLIST.md:9,TASK_CONTEXT.md:38,39}`, `MVP_Reconciliation/00_SOURCE_INVENTORY.md:15`, `strategy/Cross_Platform_Strategy/validation/B09_DERIVATION_REPORT.md:59`, three `system_description` lines; outside: `PlantLibrary_AndroidApp/implementation/MVP/evidence/MVP_TASK_DERIVATION_UPDATE.md:23` and the superproject onboarding runbook (ledger row at `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:898`).
- F-A6W-08 `SUITE_HANDOFFS.md` is stale in date, not in row status: the table was re-read on 2026-08-04 (`PlantLibrary_Workspace/implementation/System_V1_Implementation/SUITE_HANDOFFS.md:14`) and no batch has run since (every suite's `TASK_CHECKLIST.md` last changed 2026-09-15, the schema migration; Server still shows `SV-SYNC-PUSH-02`, `SV-SYNC-REFDATA-01`, `SV-OPENAPI-01` as `todo`). But it is wired in: five live Workspace rows name it as their artifact (`PlantLibrary_Workspace/implementation/System_V1_Implementation/TASK_CHECKLIST.md:26-30`, rows `SY1-SEQ-01`, `SY1-GATE-01`, `SY1-GATE-02`, `SY1-SEQ-02`, `SY1-DSG-01`), and it is cited by `BATCH_PLAN.md:10,32,42`, `CONTEXT_INDEX.md:6`, `README.md:54,95`, `SCOPE.md:22`, `STATE.md:6,8,48,51,176`, `TASK_CONTEXT.md:50,75,175,359`, `DRIVER_SCRIPT.md:32,51,65`, `proposal/00_V1_SYSTEM_PROPOSAL.md:152` (held), `validation/SY1_checkpoints.md:92,114`, `scripts/run_next_batch.py:11,114,130`, `PlantLibrary_Workspace/CLAUDE.md:73`, and by Server `implementation/System_V1_Implementation/TASK_CHECKLIST.md:27` and SharedContracts `implementation/System_V1_Implementation/DRIVER_SCRIPT.md:52`. `exempt-name` line `HYGIENE_DECISIONS.md:152`.
- F-A6W-09 Third stale sequencer, not in the brief: `PlantLibrary_Workspace/implementation/System_V1_Implementation/V1_IMPLEMENTATION_SEQUENCE.md` (105 lines) allocates Sol/Terra/Luna to "Claude Opus 4.8 / Sonnet 5 / Haiku 4.5" (`:12-14`) and lists `/run-batch PlantLibrary_X/... <key>` commands (`:35`). No Workspace file cites it (only the hygiene record and the superproject's census and map); `exempt-name` line `HYGIENE_DECISIONS.md:153`. Same age class: `implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md` (written 2026-07-08 against that lineup, held in the code group, `HYGIENE_DECISIONS.md:203`).
- F-A6W-10 The two `DRIVER_SCRIPT.md` differ in how legacy they look: `System_V1_Implementation/DRIVER_SCRIPT.md:3-10` opens with a "Process note (2026-07-10)" saying the procedural sections are superseded by run-batch; `System_Design_Architecture/DRIVER_SCRIPT.md` has no banner, `System_Design_Architecture/CONTEXT_INDEX.md:10` still calls it "Active execution prompt" and `System_Design_Architecture/README.md:49` says "Run ...DRIVER_SCRIPT.md", against `System_Design_Architecture/SCOPE.md:3` ("DRIVER_SCRIPT.md is legacy"). Onboarding decision D7 chose the SCOPE.md marker over amending the file (`onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md`, section N row `GC-7053`). Pointers that still send a reader to the drivers: `PlantLibrary_Workspace/README.md:38,62`, `docs/local_development.md:7`, `implementation/System_V1_Implementation/scripts/run_next_batch.py:129`, `implementation/System_V1_Implementation/README.md:79`.
- F-A6W-11 `REPOSITORY_MAP.md` (2026-07-05, `exempt-name` `HYGIENE_DECISIONS.md:147`) is stale as a map: `D:\libraries\...` host paths and "Not yet a Git repository" for four suites (`PlantLibrary_Workspace/REPOSITORY_MAP.md:5-9`); cited by `README.md`, `docs/local_development.md`, `scripts/bootstrap_all.{ps1,sh}` and package rows. `PlantLibrary_Workspace/implementation/README.md:20` still says "The first active package is `System_Integration_MVP/`".
- F-A6W-12 Cross-repository citers of every held name are unchanged today (table in §7.2). The live-package group is not releasable by M-9 even though onboarding steps 2a/2b are done: the citing lines are `STATE.md`/`BATCH_PLAN.md`/`TASK_CONTEXT.md` anchors in all six packages (for example `PlantLibrary_Workspace/implementation/System_V1_Implementation/STATE.md:12`, `PlantLibrary_PyApp/implementation/System_V1_Implementation/STATE.md:12`), and the M-9 block forbids editing an anchor to force a release (`repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` section 17, "Constraints").
- F-A6W-13 Archiving the frozen trees would hit very large citer sets that can only be served by mapping tables: `system_description` 41 Workspace files + 4 superproject + 7 suite files; `strategy/Cross_Platform_Strategy` 29 + 2 + 46; `implementation/System_Integration_MVP` 61 + 11 (incl. `IMPLEMENTATION_PLAN.md` and `.claude/skills/gui-validation/SKILL.md`) + 36; `MVP_Reconciliation` 19 + 5 + 17. `PlantLibrary_Workspace/implementation/README.md:31-36` declares the terminal packages in place and outside the Conductor intake root.
- F-A6W-14 The Workspace `.claude/skills` carries 11 skills and `.codex/skills` 5: the five common mirrors plus six Workspace-only skills (`design-adoption`, `gui-validation`, `sync-contracts`, `ui-ux-pro-max`, `verify-stack`, `webapp-testing`); the superproject has 13 (it also has `android-validation`, `systematic-debugging`). Not diffed; a note for A1/B1.
- F-A6W-15 `PlantLibrary_Workspace/scripts/check_markdown_links.py` (with `scripts/check_markdown_links_baseline.txt`) is a standing markdown link checker that reads link syntax. It is one of the allowed mechanical checks of kickoff rule 1 and is the right after-move check for B3.

## 3. Candidates

Pin for every source path: PlantLibrary_Workspace `6b4b88b`.

| ID | Source path @ pin | What | Verdict | Target repo and path | Lane (B3) | Q id or — |
|---|---|---|---|---|---|---|
| RC-A6W-01 | `WORKSPACE_STATE.md` | Stale 2026-07-06 snapshot, superseded by its own line 3; no unique fact | archive after B4's hand-back section exists | PlantLibrary_Workspace `archive/WORKSPACE_STATE.md` (git mv, name unchanged); mapping row in `archive/README.md`; `README.md:21` row repointed; row `SDA-QA-02` repointed by B4 | B3 (after B4) | Q-G-05, Q-A6W-01 |
| RC-A6W-02 | `implementation/System_V1_Implementation/SUITE_HANDOFFS.md` | Run-next table (9 rows), global order, rules recap; no unique fact; wired into 14 live files (12 Workspace, 2 suite lines) | absorb into the runbook hand-back section (B4), then archive | B4 edits the 14 files through plan-batch (decision in `implementation/System_V1_Implementation/STATE.md`); B3 then `git mv` to `archive/` | B4 then B3 | Q-G-05, Q-A6W-01 |
| RC-A6W-03 | `implementation/System_V1_Implementation/V1_IMPLEMENTATION_SEQUENCE.md` | Third sequencer, obsolete model names, no citer | archive with RC-A6W-02 | PlantLibrary_Workspace `archive/V1_IMPLEMENTATION_SEQUENCE.md` | B3 | Q-A6W-02 |
| RC-A6W-04 | `implementation/System_V1_Implementation/DRIVER_SCRIPT.md`, `implementation/System_Design_Architecture/DRIVER_SCRIPT.md` | Legacy per SCOPE.md; SDA's has no banner and two live files call it active | keep in place; B4 adds the one-line banner to SDA's file and fixes `CONTEXT_INDEX.md:10`, `README.md:49` | PlantLibrary_Workspace, same paths | B4 | Q-A6W-02 |
| RC-A6W-05 | `hygiene/HYGIENE_DECISIONS.md` (new entry) | Declare `archive/` as `exempt-tree: legacy`; draft in §7.3 | adopt | PlantLibrary_Workspace `hygiene/HYGIENE_DECISIONS.md` as `D-2026-10-13-01` | B3 | Q-A6W-01 |
| RC-A6W-06 | `hygiene/HYGIENE_DECISIONS.md:141-142` | Restate class and counts of the two methodology trees by a later line for the same path (GUIM stays pinned; DTI pinned to frozen) | adopt, low priority | PlantLibrary_Workspace `hygiene/HYGIENE_DECISIONS.md` as `D-2026-10-13-02` | B3 | Q-A6W-04 |
| RC-A6W-07 | `docs/proposals/Repo_Restructure_MVP_V1_Split/` | The 16th hold; target `PROPOSAL_repo-restructure-mvp-v1-split_2026-07-15/` | hold now; release at M-9 after K-7 | PlantLibrary_Workspace `docs/proposals/`; one-line path fix in five suites' `implementation/README.md` (PyApp lines 4 and 25, Server 27, SharedContracts 19, Dashboard 19, AndroidApp 16) | B3 (M-9) | Q-G-06 |
| RC-A6W-08 | `REPOSITORY_MAP.md`, `README.md:21,38,62`, `docs/local_development.md:7`, `implementation/README.md:20` | Stale host paths and pointers to the legacy drivers and to a "first active package" now terminal | refresh in the B2/B3 sweep (exempt-name files are editable) | PlantLibrary_Workspace, same paths | B2/B3 | — |
| RC-A6W-09 | `implementation/System_Design_Architecture/` (package, proposal 00-04, MODEL_RECOMMENDATION) | Design-authority package gated on SDA-DEC-01..05, overlapping the Kit's Configuration route (B5) | decision needed before B4/B5 touch it | PlantLibrary_Workspace, same path | B4/B5 | Q-A6W-05 |
| RC-A6W-10 | `scripts/check_markdown_links.py` | Allowed after-move link check | reuse | run from the Workspace root in every B3 move step | B3 | — |
| RC-A6W-11 | `docs/PROPOSAL_fable5-*` (3 sets, 23 files), `docs/proposals/PROPOSAL_{enrichment-v2,garden-designer}_*.md` | Unapproved proposals, uncited by live files, compliant dated names | keep in place; mine for the ideas register of Q-G-05 | PlantLibrary_Workspace, same paths | — | Q-G-05 |
| RC-A6W-12 | `methodology/GUI_Improvement_Methodology/` (4.1.0) | Live methodology, pinned by the Kit by absolute path | keep; source for B6 | PlantLibrary_Workspace, same path | — | — |

## 4. Questions for the operator

| ID | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A6W-01 | Where do the retired sequencers of this repository go? | (a) a new root-level `archive/` declared `exempt-tree: legacy` for newly retired organs only (`WORKSPACE_STATE.md`, later `SUITE_HANDOFFS.md`, `V1_IMPLEMENTATION_SEQUENCE.md`); frozen and pinned trees stay in place; (b) leave them where they are with a tombstone banner (as `WORKSPACE_STATE.md:3` already has); (c) also move the frozen trees into `archive/` (needs the K-7 kit patch first) | A new path needs no K-7, exempt-name files move freely, and `archive and hide, never delete` (KIT_SPEC §1.9) is met; moving a frozen tree breaks 100+ citers that can only be served by tables | B3 steps that move `WORKSPACE_STATE.md` and the two package organs |
| Q-A6W-02 | Is `V1_IMPLEMENTATION_SEQUENCE.md` part of the Q-G-05 retirement set, and do the two legacy `DRIVER_SCRIPT.md` stay in place? | (a) yes to the first, yes to the second (SDA's file gets a banner and its two live pointers are fixed, SV1's already has one); (b) retire all three; (c) leave all | The sequence file has no citer and obsolete model names; the drivers are cited by SCOPE.md legacy markers and by run_next_batch.py, and onboarding D7 already decided not to amend them | B4 (package edits), B3 |
| Q-A6W-03 | May B4 retarget the six live-package anchors that cite the held `proposal/` and `MVP_Reconciliation/` names so M-9 can release them? | (a) no, leave the six held; (b) yes, in the same plan-batch edit that changes the model column | The hold costs nothing (checker green with holds), the release only renames two proposal folders cosmetically, and it means STATE.md/BATCH_PLAN anchor edits in six repositories | M-9 only |
| Q-A6W-04 | Restate the class of `methodology/Design_Template_Initiative` (pinned to frozen) and refresh the counts of both methodology trees by a new D-entry? | (a) yes, `D-2026-10-13-02`, no file moves; (b) leave the notes stale | The record says "live initiative (Phase 6), 45 files" for a tree that closed on 2026-10-12 with 47 files; the later line wins by the checker's own fold, so it is free and exact | B3 only (cosmetic) |
| Q-A6W-05 | What is the fate of the `System_Design_Architecture` package and its approved proposals once B5 imports the canon into a Design Configuration? | (a) keep the package as the design-authority record, add one STATE.md decision saying design artifacts move to the Configuration (Q-G-01) and `SDA-B01..B08` are re-planned by B5; do not archive anything; (b) mark the package terminal and move the proposals to the archive; (c) leave untouched | Five approved proposals are cited by pinned and code citers (including the Kit's template spec and importer) and the 04 revision is the binding P-DS record; archiving them is blocked by their holds anyway | B4 (SDA package edit), B5 |

## 5. Reusable things this brief did not name

- The K-7 continuation block in `SW_Development/handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md` ("Next action", step K-7) is a finished paste-ready prompt for a separate Kit session (scope, read-first, constraints, done-when, two commit lines). It is the deliverable for Q-G-06 (a); it asks the Kit session to run the kit's own verification order, which is the kit's business and not this program's.
- The "Renamed <date>" mapping tables in each root's `INDEX.md` (`PlantLibrary_Workspace/docs/INDEX.md`, `docs/proposals/INDEX.md`) are the model for the `archive/README.md` mapping table that serves frozen citers.
- `census` output as a baseline to diff after B3: 30 files, 7 compliant, 0 candidates, 12 exempt, 10 held, 3 set folders; exempt trees frozen 205 / pinned 121 / generated 1.
- `PlantLibrary_Workspace/MVP_Reconciliation/05_NEXT_STEPS_AND_USAGE.md:86-95` ("Rules for the next batch-plan derivation") already holds five of the six bullets of the SUITE_HANDOFFS rules recap (contract regeneration before client consumption, Android V1 waiting on the MVP gate, Dashboard honest empty states, PyApp local-only mode, the release-candidate ledger); only the security-gate bullet is elsewhere (`implementation/System_V1_Implementation/BATCH_PLAN.md` rows `SY1-SEC-01`, and `IMPLEMENTATION_PLAN.md` section 4, Wave F). The hand-back section can cite them instead of copying.
- `PlantLibrary_Workspace/implementation/System_V1_Implementation/scripts/run_next_batch.py` prints the run-next recommendation and names `SUITE_HANDOFFS.md` as its authority at three lines; B4 must retarget or retire it together with the table.
- `implementation/System_V1_Implementation/validation/SY1_checkpoints.md:92,114` records "SUITE_HANDOFFS.md impact" per checkpoint: the only history of how the table was maintained.

## 6. Claims to verify

1. Moving an `exempt-name` file never needs K-7; only `exempt-tree` and `exempt-subfolder` lines are existence-checked. Check: `sed -n 431,452p PlantLibrary_Workspace/scripts/hygiene/repo_hygiene_check.py` shows the `exempt-name` branches (lines 433-434, 440-441) returning without an `exists()` call, and `exists()`/`is_dir()` only at lines 443 and 450.
2. 454 tracked `.md`, of which 327 sit under exempt trees (205 frozen, 121 pinned, 1 generated). Check: `git -C PlantLibrary_Workspace ls-files -- '*.md' | wc -l` prints 454; `python scripts/hygiene/repo_hygiene_check.py census | grep -c -E ' (frozen|pinned|generated) '` from inside the submodule prints 327.
3. The retirement of the two sequencers is a package edit, not a move: five live rows name `SUITE_HANDOFFS.md` as their artifact and one live SDA row names `WORKSPACE_STATE.md`. Check: `grep -n 'SUITE_HANDOFFS.md' implementation/System_V1_Implementation/TASK_CHECKLIST.md` returns lines 26-30, and `grep -n 'WORKSPACE_STATE.md' implementation/System_Design_Architecture/TASK_CHECKLIST.md` returns line 56 (both from the submodule root).

## 7. Disposition and hygiene detail

### 7.1 Disposition table

Columns: folder or file row, class, citers of the folder or file (Workspace files outside its own tree and the hygiene record / superproject `.md` outside `rework/` / suite files; `n/a` where the basename is generic), hold, disposition. Class vocabulary: `live`, `superseded` (by what), `archive` (historical, uncited by live files), `frozen`, `pinned`, `generated` (the three exempt-tree classes). "Mirror" rows are `live`: byte-identical copies, owned by lane B1. `INDEX.md` rows are `live` (the checker reads them). Counts in parentheses sum to 454.

| folder/ or file (n files) | class | citers | hold | disposition |
|---|---|---|---|---|
| `AGENTS.md`, `CLAUDE.md` (2 files) | live | the instruction layer; `CLAUDE.md:73` cites SUITE_HANDOFFS.md | — | keep; B2 reconciles from A3's blueprint; the rule block is installer-owned |
| `README.md` (1 file) | live | n/a | — | keep; lines 21, 38, 62 refreshed at the retirement (F-A6W-10, -11) |
| `REPOSITORY_MAP.md` (1 file) | live (stale host paths) | WS 10 files (README, local_development, SDA package x4, bootstrap scripts, system_description x2) / super 3 records / suites 0 | exempt-name `:147` | refresh paths (RC-A6W-08); never rename |
| `WORKSPACE_STATE.md` (1 file) | superseded (by IMPLEMENTATION_PLAN.md and SUITE_HANDOFFS.md, its own line 3) | WS 14 files (README:21, SDA package x3, System_Integration_MVP x4, MVP_Reconciliation/00:15, v2 README:39, strategy B09 report, system_description x3) / super 4 (onboarding runbook:898, three track records) / AndroidApp 1 | exempt-name `:146` | archive after B4's hand-back section (RC-A6W-01); no unique fact (§7.5) |
| `hygiene/` (2 files) | live | the pin and the append-only record | — | B3 appends entries; nothing edited retroactively |
| `.claude/agents/` (3 files) | live (mirror) | parity checker in the superproject | — | B1 |
| `.claude/skills/` (14 files, 11 skills) | live (mirror; 5 common, 6 Workspace-only) | `design-adoption/SKILL.md:35` cites held 04_APPROVED | — | B1; Q-G-07 decides design-adoption |
| `.codex/skills/` (8 files, 5 skills) | live (mirror; Codex frozen if Q-G-09 (a)) | — | — | B1 per Q-G-09 |
| `methodology/VALIDATION_METHODOLOGY.md` (1 file) | live | WS 8 (README, SV1 SKILLS/TASK_CHECKLIST/TASK_CONTEXT/proposal 02, validation x2) / super 3 records / suites 5 | exempt-name `:148` | keep |
| `methodology/GUI_Improvement_Methodology/` (74 files: 43 + PROMPTS 19 + SKILL_SPECS 12) | pinned (live, 4.1.0 ACTIVE) | WS 37 / super 5 records / PyApp 2 / Kit `METHODOLOGY_SOURCE.md:14` pins it by absolute path | exempt-tree `:141` (note stale: 4.0.0, 62 files) | keep in place; source for B6; refresh note by a later line (RC-A6W-06) |
| `methodology/Design_Template_Initiative/` (47 files: 12 + PROMPTS 24 + evidence 11) | pinned (initiative closed 2026-10-12; STATE.md, HANDOVER.md, HANDOVER_PROMPT12, NEXT_STEPS.md, RUNBOOK_GUI_REWORK.md and the 24 prompts are the closed sequencers of a finished initiative; the runbook there drives the Conductor GUI, not PlantLibrary) | WS only records and held-name citers / super 6 records / PyApp 3 and Dashboard 3 (their own hygiene records) / Conductor `design/DESIGN_VERSION.md` | exempt-tree `:142` (note stale: "live, Phase 6", 45 files); it is the pinned citer of held SDA 00-04 and MODEL_RECOMMENDATION | keep in place, no archive; restate as frozen by a later line (RC-A6W-06, Q-A6W-04) |
| `strategy/Cross_Platform_Strategy/` (17 files: 11 + PROMPTS 3 + validation 3) | frozen (closed 2026-07-06; last change 2026-07-10) | WS 29 / super 2 / suites 46 (PyApp 14, Server 12, Dashboard 9, AndroidApp 6, SharedContracts 5) | exempt-tree `:136` | keep in place |
| `system_description/` (138 files, 17 chapter folders) | frozen (canonical reference, still the most-cited tree; last change 2026-07-17) | WS 41 / super 4 / suites 7 | exempt-tree `:137` | keep in place; "frozen" means never renamed, edits only by the registers' own rows |
| `MVP_Reconciliation/` `00_SOURCE_INVENTORY`, `01_CURRENT_SYSTEM_BASELINE`, `03_SUBSYSTEM_RECONCILIATION`, `06_V1_KICKOFF_PROMPT`, `README` (5 files) | archive (snapshot "frozen 2026-07-09" per its README; V1 planning input; registers supersede it) | WS 19 / super 5 records / suites 17, each counted for the folder as a whole | none for these five; the folder is outside every root (catalogued) | keep in place; on release becomes `docs/SNAPSHOT_mvp-reconciliation_2026-07-10/` (proposal 4) |
| `MVP_Reconciliation/` `02_GAPS_AND_DEFERRED_REGISTER`, `04_MVP_TO_V1_PROPOSAL`, `05_NEXT_STEPS_AND_USAGE` (3 files) | archive, live-cited | AndroidApp and Workspace SV1 BATCH_PLAN:35 / :23, PyApp TASK_CONTEXT:22, Dashboard BATCH_PLAN:12 | held-name `:185`, `:186`, `:187` (live-package) | stays held (§7.2) |
| `docs/INDEX.md` (1 file) | live | checker | — | B3 maintains |
| `docs/local_development.md` (1 file) | live (line 7 points at the legacy drivers) | WS 5 / super 3 records | exempt-name `:149` | refresh line 7 |
| `docs/EVIDENCE_garden-apps-13-products_2026-07-11.md`, `docs/EVIDENCE_garden-apps-4-products_2026-07-11.md`, `docs/PROMPT_fable5-business-gtm-proposal_2026-07-11.md`, `docs/PROMPT_fable5-system-strategy-proposal_2026-07-11.md` (4 files) | archive | INDEX and the strategy sets only / super 1 (rename map) | — | keep in place (compliant) |
| `docs/PROPOSAL_fable5-business-gtm_2026-07-11/` (11 files) | archive (proposal only, nothing approved) | WS inside docs only / super 2 records / suites 0 | — | keep in place; ideas feed the Q-G-05 register |
| `docs/PROPOSAL_fable5-product-strategy-v1_2026-07-11/` (7 files) | archive (proposal only) | same | — | keep in place |
| `docs/PROPOSAL_fable5-product-strategy-v2_2026-07-11/` (5 files) | archive (working decisions WD-01..17 vetoable, not approved; `README.md:39` links WORKSPACE_STATE.md) | same | — | keep in place; repoint `README.md:39` when `WORKSPACE_STATE.md` moves |
| `docs/proposals/INDEX.md` (1 file) | live | checker | — | B3 maintains |
| `docs/proposals/PROPOSAL_enrichment-v2_2026-07-10.md`, `docs/proposals/PROPOSAL_garden-designer_2026-07-10.md` (2 files) | archive (proposal only, no batches planned) | INDEX only / super 1 | — | keep in place; ideas feed the Q-G-05 register |
| `docs/proposals/PlantLibrary_Full_Implementation_Update.md` (1 file) | archive (2026-07-16 recommendation on a full implementation package; no header date) | WS 4 incl. `MANIFEST_complete.csv:2` / super 3 records | held-name `:204` (code) | stays held |
| `docs/proposals/Repo_Restructure_MVP_V1_Split/` `EXECUTION_PROMPTS`, `FOLLOWUP_CLOSURE_PROMPT`, `PROPOSAL`, `VERIFICATION_REPORT` (4 files) | archive (track executed and closed 2026-07-16) | WS 5 / super 4 (finding, map, runbook, census) / suites 5 (`implementation/README.md` of each) | the 16th hold, prose only (`D-2026-09-17-03` item 2, record group) | stays; M-9 renames it after K-7 |
| `docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/REVIEW_LIST.md` (1 file) | generated (roll-up of the `MANIFEST_*.csv` REVIEW rows) | INDEX, EXECUTION_PROMPTS / super 4 | exempt-tree `:161` (the K-7 line) | moves with its set on release |
| `implementation/README.md` (1 file) | live (line 20 stale; lines 24-37 are the Conductor intake rule) | many | — | refresh line 20 |
| `implementation/Server_VM_Setup/` `INDEX.md` (1 file) | live | checker | — | B3 maintains |
| `implementation/Server_VM_Setup/PROMPT_docker-desktop-audit-migration_2026-07-10.md` (1 file) | archive | INDEX, ServerSetUp_MVP.md pointers | — | keep in place |
| `implementation/Server_VM_Setup/ServerSetUp_MVP.md` (1 file) | live | INDEX / super 3 records | exempt-name `:150` | keep |
| `implementation/System_Integration_MVP/` (36 files: 14 + validation 14 + evidence pack 8; includes its own `DRIVER_SCRIPT.md`, `SUITE_HANDOFFS.md`, `HANDOVER_SYS-B12_PyApp_walkthrough.md`, `validation/MVP_VALIDATION_GAP_CLOSURE_HANDOVER_2026-07-15.md`) | frozen (terminal MVP package, closed 2026-07-15) | WS 61 / super 11 (incl. `IMPLEMENTATION_PLAN.md`, `gui-validation` skill) / suites 36 | exempt-tree `:134` | keep in place ("Terminal — never bind, never migrate, never edit", `implementation/README.md:31`) |
| `implementation/System_Tooling/` (14 files) | frozen (terminal tooling package, WST-B01/B02 done) | WS 20 / super 8 records / suites 0 | exempt-tree `:135` | keep in place |
| `implementation/System_Design_Architecture/` `BATCH_PLAN`, `TASK_CHECKLIST`, `TASK_CONTEXT`, `STATE`, `SCOPE`, `CONTEXT_INDEX`, `README` (7 files) | live (package; binds as the second project only after SDA-DEC-01..05) | package-internal; super: onboarding census/audit | — | B4 edits through plan-batch; fate per Q-A6W-05 |
| `implementation/System_Design_Architecture/DRIVER_SCRIPT.md` (1 file) | superseded (by run-batch, `SCOPE.md:3`; no banner of its own) | `CONTEXT_INDEX.md:10`, `README.md:49,67`, `STATE.md:112` | — | keep; add one-line banner and fix the two live pointers (B4) |
| `implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md` (1 file) | superseded (model lineup of 2026-07-08; replaced by the runbook's model column) | `MANIFEST_Workspace.csv:3`, DTI x4, SDA CONTEXT_INDEX:12, README:54,68 | held-name `:203` (code) | stays held |
| `implementation/System_Design_Architecture/proposal/` `00_DESIGN_GOVERNANCE_PROPOSAL`, `01_DESIGN_ARTIFACT_TEMPLATES`, `02_CONFORMANCE_AND_ENFORCEMENT`, `03_CLAUDE_MD_AND_DOC_LAYERING` (4 files) | live (approved design authority of the package) | DTI (pinned) x4-5 lines each; Kit `template/TEMPLATE_SPEC.md:39,518,519`; SDA CONTEXT_INDEX/README | held-name `:195-198` (pinned) | stays held |
| `implementation/System_Design_Architecture/proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` (1 file) | live (the binding P-DS-01..10 record, tokens 1.2.0) | about 28 citing files (table in §7.2) | held-name `:202` (code) | stays held |
| `implementation/System_Design_Architecture/{proposal,planning,handovers}/INDEX.md` (3 files) | live | checker | — | B3 maintains |
| `implementation/System_V1_Implementation/` `BATCH_PLAN`, `TASK_CHECKLIST`, `TASK_CONTEXT`, `STATE`, `SCOPE`, `CONTEXT_INDEX`, `README` (7 files) | live (bound as project PlantLibrary_Workspace) | package-internal, the five suites' anchors cite the proposals | — | B4 through plan-batch; STATE.md decision per edit |
| `implementation/System_V1_Implementation/SKILLS.md` (1 file) | live (decisions for the V1 skills; cites root `Todo.md`) | WS `README`, SDA, package files | exempt-name `:151` | keep |
| `implementation/System_V1_Implementation/SUITE_HANDOFFS.md` (1 file) | live (the run-next table; to be superseded by the runbook's hand-back section at B4) | WS 27 files incl. five checklist rows, 8 package files, `CLAUDE.md:73`, `run_next_batch.py`; super 4 (`IMPLEMENTATION_PLAN.md` §3.2, onboarding runbook:898, two track records); Server `TASK_CHECKLIST.md:27`, SharedContracts `DRIVER_SCRIPT.md:52` | exempt-name `:152` | absorb, repoint 14 files, then archive (RC-A6W-02); §7.5 |
| `implementation/System_V1_Implementation/V1_IMPLEMENTATION_SEQUENCE.md` (1 file) | superseded (by IMPLEMENTATION_PLAN.md §4 waves and the runbook's model column; obsolete model names) | WS 0 / super 2 records | exempt-name `:153` | archive with RC-A6W-02 (RC-A6W-03) |
| `implementation/System_V1_Implementation/DRIVER_SCRIPT.md` (1 file) | superseded (by run-batch; banner `:3-10`; `SCOPE.md:3`) | SCOPE, STATE x4, README:79,94, SUITE_HANDOFFS:22, SKILLS:133, `run_next_batch.py:129`, root README:38 | — | keep (onboarding D7) |
| `implementation/System_V1_Implementation/proposal/` `00_V1_SYSTEM_PROPOSAL`, `01_PRODUCT_VALUE_AUDIT`, `02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10` (3 files) | live (D-V1 authority) | anchors in six packages (§7.2) | held-name `:182-184` (live-package) | stays held |
| `implementation/System_V1_Implementation/{proposal,planning,handovers}/INDEX.md` (3 files) | live | checker | — | B3 maintains |
| `implementation/System_V1_Implementation/validation/` `README`, `SY1-B06_methodology`, `SY1-B06_skills_diff`, `SY1_checkpoints` (4 files) | live (row evidence and the checkpoint log; append-only in practice) | rows' artifact cells; SY1_checkpoints.md:92,114 is the only history of the SUITE_HANDOFFS maintenance | — | keep; catalogued, not a root |
| `prompts/INDEX.md` (1 file) | live | checker | — | B3 maintains |
| `prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` (1 file) | archive (handoff of the finished process-improvement track) | System_Tooling x4 (frozen) / PyApp 2, AndroidApp 2, Dashboard 2 live anchors | held-name `:191` (terminal-STATE) | stays held; target `implementation/System_V1_Implementation/handovers/HANDOVER_process-improvements_2026-07-10.md` |
| `prompts/reference/BATCH_PLAN_V3.md`, `DRIVER_SCRIPT_V3.md`, `TASK_CHECKLIST_V3.md`, `TASK_CONTEXT_V3.md` (4 files) | superseded (V3 package templates; the 15-column schema of plan-batch replaced them; kept as the reference the legacy DRIVER_SCRIPTs, `GUI_Improvement_Methodology/EVIDENCE_DIGEST.md` and `MVP_Reconciliation/06` cite) | WS 6-9 each / super `DRIVER_SCRIPT_V3` 3 records / suites 1 each | exempt-name `:154-157` | keep |
| `prompts/reference/SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` (1 file) | archive (misfiled setup prompt, header 2026-07-06) | `MANIFEST_complete.csv:3`; AndroidApp MVP `STATE.md:457`, `TASK_CONTEXT.md:469`; Server MVP evidence report:3 | held-name `:205` (code) | stays held |

Class tally of the 454 files (summed from the rows above by a column sum): live 73 (25 of them mirrors), superseded 9, archive 45, frozen 205, pinned 121, generated 1 (total 454).

### 7.2 Holds and exemptions

Every directive line of `PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md`, all in entry `D-2026-09-16-01` (the other four entries carry none). State is "in force" for all 34; no `release` exists.

| Line | Directive | Value | State | What releases it |
|---|---|---|---|---|
| 134 | exempt-tree | `implementation/System_Integration_MVP` (frozen) | in force | nothing; K-7 needed to move it |
| 135 | exempt-tree | `implementation/System_Tooling` (frozen) | in force | same |
| 136 | exempt-tree | `strategy/Cross_Platform_Strategy` (frozen) | in force | same |
| 137 | exempt-tree | `system_description` (frozen) | in force | same |
| 141 | exempt-tree | `methodology/GUI_Improvement_Methodology` (pinned) | in force; note stale (F-A6W-05) | the Kit re-pin (Kit pins it by path); K-7 needed to move it |
| 142 | exempt-tree | `methodology/Design_Template_Initiative` (pinned) | in force; note stale | the Design initiative's owner (closed); K-7 needed to move it |
| 161 | exempt-tree | `docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/REVIEW_LIST.md` (generated) | in force; the line K-7 cannot retire | K-7 then M-9 |
| 146-157 | exempt-name x12 | `WORKSPACE_STATE.md` (146), `REPOSITORY_MAP.md` (147), `methodology/VALIDATION_METHODOLOGY.md` (148), `docs/local_development.md` (149), `implementation/Server_VM_Setup/ServerSetUp_MVP.md` (150), `.../System_V1_Implementation/SKILLS.md` (151), `SUITE_HANDOFFS.md` (152), `V1_IMPLEMENTATION_SEQUENCE.md` (153), `prompts/reference/{BATCH_PLAN,DRIVER_SCRIPT,TASK_CHECKLIST,TASK_CONTEXT}_V3.md` (154-157) | in force | nothing needed to move one (no existence check); the line goes dead, harmlessly |
| 182 | held-name | `.../System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md` (live-package) | in force | the citing anchors stop citing it (onboarding migration is done, anchors still cite); then M-9 |
| 183 | held-name | `.../proposal/01_PRODUCT_VALUE_AUDIT.md` (live-package) | in force | same |
| 184 | held-name | `.../proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md` (live-package) | in force | same; widest citer set (six packages) |
| 185 | held-name | `MVP_Reconciliation/02_GAPS_AND_DEFERRED_REGISTER.md` (live-package) | in force | AndroidApp and Workspace BATCH_PLAN anchors |
| 186 | held-name | `MVP_Reconciliation/04_MVP_TO_V1_PROPOSAL.md` (live-package) | in force | PyApp TASK_CONTEXT anchor |
| 187 | held-name | `MVP_Reconciliation/05_NEXT_STEPS_AND_USAGE.md` (live-package) | in force | Dashboard BATCH_PLAN anchor |
| 191 | held-name | `prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` (terminal-STATE) | in force | PyApp, Dashboard and AndroidApp anchors migrate (frozen `System_Tooling/STATE.md` is served by the mapping table) |
| 195 | held-name | `.../System_Design_Architecture/proposal/00_DESIGN_GOVERNANCE_PROPOSAL.md` (pinned) | in force | DTI owner or a Kit re-pin; Kit `TEMPLATE_SPEC.md:39,518` |
| 196 | held-name | `.../proposal/01_DESIGN_ARTIFACT_TEMPLATES.md` (pinned) | in force | same |
| 197 | held-name | `.../proposal/02_CONFORMANCE_AND_ENFORCEMENT.md` (pinned) | in force | same; Kit `TEMPLATE_SPEC.md:519` |
| 198 | held-name | `.../proposal/03_CLAUDE_MD_AND_DOC_LAYERING.md` (pinned) | in force | same |
| 202 | held-name | `.../proposal/04_APPROVED_DESIGN_REVISION_2026-07-10.md` (code) | in force | a code edit in a batch (SharedContracts `semantic-roles.json:3`; Kit importer and exporter) |
| 203 | held-name | `.../System_Design_Architecture/MODEL_RECOMMENDATION.md` (code) | in force | a code edit (`MANIFEST_Workspace.csv:3`); DTI citers stand |
| 204 | held-name | `docs/proposals/PlantLibrary_Full_Implementation_Update.md` (code) | in force | a code edit (`MANIFEST_complete.csv:2`) |
| 205 | held-name | `prompts/reference/SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` (code) | in force | a code edit (`MANIFEST_complete.csv:3`) |
| (prose) | 16th hold | `docs/proposals/Repo_Restructure_MVP_V1_Split/` as a folder (record group, `HYGIENE_DECISIONS.md:438`) | in force, outside the checker's count | K-7 (kit patch) then M-9 |

Roots (not directives): ten, `PlantLibrary_Workspace/hygiene/CONSUMED_HYGIENE.md:25-34`; no allowlist, retired-name, scratch or forbidden-path declarations; modules none.

**The M-7 held set.** M-7 renamed the three `docs/fable5_*` sets and seven files (all green) and reverted the fourth folder rename because line 161 failed `record` (`PlantLibrary_Workspace/hygiene/HYGIENE_DECISIONS.md:438-457`, item 2 of `D-2026-09-17-03`). The set stays under `docs/proposals/Repo_Restructure_MVP_V1_Split/`; the 15 file holds were kept unchanged (item 4).

**What M-9 would release once K-7 is decided** (kit session first, then a Workspace release batch): exactly one hold, the Repo_Restructure set folder. Steps: re-pin the Workspace to the new kit version (`--target` alone, then `--force`, own entry, per `D-2026-09-17-01`); `git mv` the folder to `docs/proposals/PROPOSAL_repo-restructure-mvp-v1-split_2026-07-15/`; in the same entry `release` the old `REVIEW_LIST.md` path and declare the new one `exempt-tree ... generated` (the vocabulary the K-7 patch adds); redo the sweep that touched `EXECUTION_PROMPTS.md` and `FOLLOWUP_CLOSURE_PROMPT.md` and restore the manifests byte for byte; flip the `docs/proposals/INDEX.md` line and "Renamed" row; fix the five one-line path citers in the suites (`PlantLibrary_PyApp/implementation/README.md:4,25`, `PlantLibrary_AndroidApp/implementation/README.md:16`, `PlantLibrary_Dashboard/implementation/README.md:19`, `PlantLibrary_Server/implementation/README.md:27`, `PlantLibrary_SharedContracts/implementation/README.md:19`); bump five gitlinks. The three code holds that the manifests cite are unaffected because the CSVs keep their relative position inside the moved folder. The other 15 holds stay: live-package 6, terminal-STATE 1, pinned 4, code 4 (reasons in the table).

**Cross-repository citers of the held names today** (hold-class citers first; `git grep -n -F`, Workspace plus five suites plus the superproject and the Design Template Kit, 2026-10-13; line numbers equal the record's except where noted). All suite lines are under `implementation/System_V1_Implementation/`.

| Held name | Hold-class citers (file:line) | Other citers worth knowing |
|---|---|---|
| 00_V1_SYSTEM_PROPOSAL | Workspace STATE:12, BATCH_PLAN:22, TASK_CONTEXT:34; PyApp STATE:12; Server BATCH_PLAN:110, STATE:16; SharedContracts STATE:12; Dashboard STATE:15 | CONTEXT_INDEX and README of all six packages, the five `*_V1_PROPOSAL.md` (:4), `system_description` DEFERRED register (:42-51) and PLATFORM_SCOPE_MATRIX (:57) |
| 01_PRODUCT_VALUE_AUDIT | Workspace STATE:14,83, TASK_CHECKLIST:25 | v2 README:36, SY1_checkpoints:47, SUITE_HANDOFFS:10 |
| 02_VALIDATION_METHODOLOGY_DECISIONS | Workspace BATCH_PLAN:133, STATE:118, TASK_CHECKLIST:37, TASK_CONTEXT:184; PyApp BATCH_PLAN:35, STATE:136; Server :165/:130; SharedContracts :85/:80; Dashboard :157/:83; AndroidApp :248/:153 | SKILLS:145, v2 README:41, VERIFICATION_REPORT:101,112 |
| MVP_Reconciliation/02 | AndroidApp BATCH_PLAN:35; Workspace BATCH_PLAN:23 | five `*_V1_PROPOSAL.md`, AndroidApp `validation/AN1-B00_reconciliation.md:9`, 05/06/README |
| MVP_Reconciliation/04 | PyApp TASK_CONTEXT:22 | 05, 06, README, proposal 00:9,55, v2 README:38 |
| MVP_Reconciliation/05 | Dashboard BATCH_PLAN:12 | proposal 00:193, SUITE_HANDOFFS:38, README:12, PyApp proposal:29, AndroidApp README:25, Dashboard proposal:22 |
| PROCESS_IMPROVEMENTS_HANDOFF | PyApp BATCH_PLAN:137, STATE:130; Dashboard BATCH_PLAN:122, STATE:77; AndroidApp BATCH_PLAN:213, STATE:147; Workspace `System_Tooling/STATE.md:6,13` (frozen, mapping-served) | System_Tooling README:8, CONTEXT_INDEX:16, proposal/ORIGIN:4 (frozen) |
| SDA 00..03 | DTI `INITIATIVE_PROPOSAL.md:80-83`, `KICKOFF_PROMPT.md:43`, `PROMPTS/02:18`, `PROMPTS/10:16` (02, 03), `evidence/00:22-25`; Kit `template/TEMPLATE_SPEC.md:39,518` (00) and `:519` (02) | SDA CONTEXT_INDEX:26-29, README:5,69-72, MVP_Reconciliation/06:73,75,266 |
| SDA 04 | SharedContracts `design-tokens/semantic-roles.json:3`, `design-tokens/TOKEN_USAGE_NOTES.md:9`, `CONTRACT_VERSION.md:23`; Kit `examples/plantlibrary-field-ledger/design/{CONFIGURATION.md:33,banned-colors.json:16,25,32,decisions/DECISION_RECORD_2026-07-10.md:16,25}` and (per the record) `tools/import-flat-tokens.mjs:456,466,468`, `tools/lib/color-extra.mjs:6`; SDA STATE:45,65; PyApp BATCH_PLAN:169, STATE:102, TASK_CONTEXT:162, `DESIGN.md:220`; AndroidApp :187/:121/:262; Dashboard :97/:51/:130; DTI five lines | `design-adoption/SKILL.md:35` in the superproject (`.claude`, `.codex`) and in this repository's `.claude`; SV1 proposal 00:112 |
| MODEL_RECOMMENDATION | `docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_Workspace.csv:3`; DTI `DRIVER.md:7`, `INITIATIVE_PROPOSAL.md:97`, `KICKOFF_PROMPT.md:49`, `evidence/00:39` | SDA CONTEXT_INDEX:12, README:54,68; REVIEW_LIST:16,43; VERIFICATION_REPORT:25 |
| PlantLibrary_Full_Implementation_Update | `MANIFEST_complete.csv:2` | Repo_Restructure PROPOSAL:40,92, VERIFICATION_REPORT:138, MVP_Reconciliation/00:14 |
| SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT | `MANIFEST_complete.csv:3`; AndroidApp `implementation/MVP/package/STATE.md:457` (frozen) | AndroidApp MVP `TASK_CONTEXT.md:469`, Server MVP `evidence/Android_Test_Environment_Setup_Report.md:3`, Repo_Restructure PROPOSAL:40,92 |
| Repo_Restructure set | the record's own line `HYGIENE_DECISIONS.md:161` | `implementation/README.md` of PyApp (:4,25), AndroidApp (:16), Dashboard (:19), Server (:27), SharedContracts (:19); superproject `handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md:8,13` |

### 7.3 Archive layout proposal

**Options.**

| Layout | Cost here | K-7 | Verdict |
|---|---|---|---|
| (A) New root-level `archive/`, declared `exempt-tree: legacy` by one new entry, receiving only newly retired organs (`WORKSPACE_STATE.md` now; `SUITE_HANDOFFS.md`, `V1_IMPLEMENTATION_SEQUENCE.md` after B4); frozen and pinned trees stay under their six existing lines | one new path (must exist when the line folds, so `archive/README.md` lands in the same commit); the `exempt-name` lines for the moved files go dead and stay harmless; no allowlist entry (pin Modules: none, `CONSUMED_HYGIENE.md:15`) | not touched | recommended |
| (B) Keep everything where it is under its current exempt line, retire sequencers by tombstone banner only | zero moves; `WORKSPACE_STATE.md:3` already is such a banner | not touched | acceptable fallback (Q-A6W-01 (b)) |
| (C) Also move the frozen and pinned trees into `archive/` | breaks 100+ citers served only by mapping tables (F-A6W-13); the Kit pins `GUI_Improvement_Methodology` by absolute path (F-A6W-06); Conductor intake reads `implementation/` | blocked: each of the seven path-declared trees fails `record` for ever after a `git mv` | rejected |
| (D) Declare `archive` as a general root instead of an exempt tree | files moved there would have to take dated `<TYPE>_<topic>_<date>.md` names, contradicting "moved with name unchanged" (KIT_SPEC §1.9) | not touched | rejected |

**What the K-7 finding means for moving an already-exempt tree** (two sentences of `SW_Development/handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md`, section "Why"): "The record is append-only, so the earlier line can never be edited away." and "The result is that **any exempt path that a later `git mv` moves or renames fails `record` for ever** — the same shape `K-6` fixed for `held-name`." Consequence for this repository: moving any of the seven path-declared exempt trees (lines 134-137, 141, 142, 161) into an archive is impossible on kit 0.2.1; a file named only by `exempt-name` (the sequencers) is free to move.

**Entries B3 would write** (ids provisional: the next free `D-2026-10-13-nn` by grep at write time; this repository's record has none for 2026-10-13 today).

```text
## 2026-10-13 — archive layout

### D-2026-10-13-01 — archive/ declared as a legacy exempt tree; WORKSPACE_STATE.md retired into it
Authority: master-rework runbook step <B3 step id>; Q-G-05 (a) and Q-A6W-01 (a), operator words verbatim with date;
the B4 hand-back section exists and replaces the file (named in the entry). Preconditions measured: checker verdict
before; README.md:21 and docs/PROPOSAL_fable5-product-strategy-v2_2026-07-11/README.md:39 repointed; row SDA-QA-02
repointed by B4. Disposition: git mv WORKSPACE_STATE.md archive/WORKSPACE_STATE.md (name unchanged, KIT_SPEC 1.9);
archive/README.md created in the same commit with the mapping table; frozen citers served by that table. Verdict after.
Commit line: hygiene: B3 - archive/ declared; WORKSPACE_STATE.md retired

- exempt-tree: archive — legacy; newly retired organs moved by git mv with names unchanged; frozen and pinned trees stay where their own lines declare them

### D-2026-10-13-02 — class and counts of the two methodology trees restated (no file moves)
- exempt-tree: methodology/Design_Template_Initiative — frozen; the closed Design & UI/UX Template Initiative (G-close closed 2026-10-12), 47 .md files; cited by pinned holds
- exempt-tree: methodology/GUI_Improvement_Methodology — pinned; VERSION.md 4.1.0, 74 .md files; pinned by the Kit by absolute path

### D-2026-10-13-03 — SUITE_HANDOFFS.md and V1_IMPLEMENTATION_SEQUENCE.md retired into archive/
Authority: B4 done (14 files repointed, decision in System_V1_Implementation/STATE.md); no directive line (exempt-name lines go dead, archive/ is already declared).
```

`INDEX.md` lines: none for the archive moves (`archive/` is not a root, so the checker neither requires nor reads one); the mapping rows live in `archive/README.md` (`README.md` is exempt by construction), shape `| old path | new path | date | entry |`. At the M-9 release after K-7, `docs/proposals/INDEX.md` gets the line `- 2026-07-15 · PROPOSAL_repo-restructure-mvp-v1-split_2026-07-15/ · PROPOSAL · executed and closed · <summary of the held line>` and its "Renamed" row flips from held to renamed.

**Recommendation for Q-G-06 evidence.** (a) is right and cheap for this repository: K-7 blocks exactly one Workspace action (the 16th hold's rename, cosmetic, with the set compliant and checked in place) and nothing in the recommended layout moves an exempt tree. The workaround (b) would have to recreate a stub file at the old `REVIEW_LIST.md` path so the existence check passes after the folder moves, which leaves an undeclared stub folder under the old name and an exempt-tree line pointing at a lie; that is worse than the hold. The Kit-session prompt is already written in the finding ("Next action", step K-7) and needs only the operator's start; the program must not run it (kickoff §1, SOURCE-K read-only; §2 rule 2).

### 7.4 Checker

Verdict line of `python scripts/hygiene/repo_hygiene_check.py check` (run inside the submodule, read-only): `repo-hygiene: pass with holds — 0 violations, 10 held`.

Per-root totals of `census` (files, compliant, candidates, exempt, held, set folders):

| Root | Files | Compliant | Candidates | Exempt | Held | Set folders |
|---|---|---|---|---|---|---|
| `implementation/System_V1_Implementation/planning` | 1 | 0 | 0 | 1 | 0 | 0 |
| `implementation/System_V1_Implementation/proposal` | 4 | 0 | 0 | 1 | 3 | 0 |
| `implementation/System_V1_Implementation/handovers` | 1 | 0 | 0 | 1 | 0 | 0 |
| `implementation/System_Design_Architecture/planning` | 1 | 0 | 0 | 1 | 0 | 0 |
| `implementation/System_Design_Architecture/proposal` | 6 | 0 | 0 | 1 | 5 | 0 |
| `implementation/System_Design_Architecture/handovers` | 1 | 0 | 0 | 1 | 0 | 0 |
| `docs` | 7 | 4 | 0 | 2 | 0 | 3 |
| `docs/proposals` | 4 | 2 | 0 | 1 | 1 | 0 |
| `prompts` | 2 | 0 | 0 | 1 | 1 | 0 |
| `implementation/Server_VM_Setup` | 3 | 1 | 0 | 2 | 0 | 0 |
| Repository | 30 | 7 | 0 | 12 | 10 | 3 |

Exempt trees by class (census closing table): frozen 205, pinned 121, generated 1 (327 files). The 10 `held:` lines: 3 + 5 in the two `proposal/` roots, plus `docs/proposals/PlantLibrary_Full_Implementation_Update.md` and `prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md`. The checker needs the superproject's `check` to be run separately; nothing was run there.

### 7.5 Sequencers

Method: for each fact the sequencer states, the Workspace, the five suites and the superproject's `IMPLEMENTATION_PLAN.md` were searched for the identifier or phrase. "Carried" means found at the named place; "unique" means not found.

**`WORKSPACE_STATE.md` (2026-07-06, 63 lines).** Unique facts: none that a successor must absorb.

| Fact in the file | Where else it lives |
|---|---|
| Six-row suite status table with the MVP-era next batches `SC-B08`, `SV-B09`, `WD-B07`, `PY-B09`, `AN-B07`, `SYS-B05` | each ID appears in 3-12 other Workspace files; `MVP_Reconciliation/01_CURRENT_SYSTEM_BASELINE.md:27`; MVP closed 2026-07-15 (`IMPLEMENTATION_PLAN.md` §1) |
| Six-step recommended run order of the MVP | closed with the MVP; `SUITE_HANDOFFS.md` rows 3 and 7 |
| Seven-row blocker table (`SD-GAP-001..006` with owner and the batch authored for it) | `system_description/PlantLibrary_System_Description/10_quality_acceptance/06_KNOWN_GAPS_REGISTER.md:46-48`; `MVP_Reconciliation/02_GAPS_AND_DEFERRED_REGISTER.md:36-39,90,98` |
| "Methodology convention" paragraph (standard package files, root-level suite control files intentionally not moved, dedicated cleanup batch) | `implementation/System_Integration_MVP/STATE.md:72`; each suite's `implementation/MVP/package/IMPLEMENTATION.md:25` (frozen) |
| "Renamed folder" `methology/` to `methodology/` | `README.md:28`, `REPOSITORY_MAP.md:53`, `implementation/System_Integration_MVP/CHANGELOG.md:18`, `STATE.md:70` |
| Line 3, added by `752ff51`: names `IMPLEMENTATION_PLAN.md` and `SUITE_HANDOFFS.md` as the successors | this is the one thing the hand-back section must take over: after retirement the named successors are the runbook's hand-back section and the archive pointer |

Owed on retirement (not facts): repoint `README.md:21`, `docs/PROPOSAL_fable5-product-strategy-v2_2026-07-11/README.md:39`, and the SDA row `SDA-QA-02` (`TASK_CHECKLIST.md:56`, `BATCH_PLAN.md:173`, `TASK_CONTEXT.md:339`), which asks for `WORKSPACE_STATE.md` to be updated by the design package.

**`SUITE_HANDOFFS.md` (re-read 2026-08-04, 9 rows).** Row statuses are still true (no batch has run since; every checklist last changed 2026-09-15). Facts and their homes:

| Fact in the file | Where else it lives |
|---|---|
| Run-next table, 9 rows with `Waits on` edges (for example `SC1-B02` waits on `SV1-B01..B04`; `AN1-B09` on `AN1-B01..B07` plus `AN-V1-SEC-01`; `AN1-B10` on `AN1-B09` plus `SY1-B04`; `PY1-B03` on `SC1-B00/B02`) | `IMPLEMENTATION_PLAN.md` §1 package table ("Not runnable yet" column) and §4 waves A-F; each package's `TASK_CHECKLIST.md` |
| Rows 3 and 7 (Android root MVP package and `System_Integration_MVP`, terminal) and row 8 (SDA gated on `SDA-DEC-01..05`, non-gating by D-V1-11) | `IMPLEMENTATION_PLAN.md` §1 and §5.1; `implementation/README.md:31-36` |
| Recommended global run order with 2026-08-04 progress markers; the ordering trap (`SY1-B07` before `SY1-B05`) | `IMPLEMENTATION_PLAN.md` §4 Wave F; onboarding runbook section N row `GC-6082` |
| Removals of `SV1-B05` and `WD1-B03` (PA-08, 2026-07-10), D-V1-11, D-V1-12 | `implementation/System_V1_Implementation/BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `STATE.md` (2026-07-10 amendments); `IMPLEMENTATION_PLAN.md` carries D-V1-11 only |
| Six-bullet rules recap | five bullets in `MVP_Reconciliation/05_NEXT_STEPS_AND_USAGE.md:91-95`; the security-gate bullet in `System_V1_Implementation/BATCH_PLAN.md` (`SY1-SEC-01`), `SKILLS.md:166`, `STATE.md:173` and `IMPLEMENTATION_PLAN.md` Wave F |
| **Unique: the maintenance protocol** (lines 3-5): "Update the Status column when a package's STATE.md changes (Workspace rows SY1-SEQ-*/SY1-GATE-* do this as part of their checkpoints)"; `scripts/run_next_batch.py` is the mechanical shortcut (authority string at `run_next_batch.py:11,114,130`) | nowhere else; `IMPLEMENTATION_PLAN.md` has no hit for `run_next_batch` |
| **Unique: its role as the named artifact** of rows `SY1-SEQ-01`, `SY1-GATE-01`, `SY1-GATE-02`, `SY1-SEQ-02`, `SY1-DSG-01` (`TASK_CHECKLIST.md:26-30`) and of the update steps in `TASK_CONTEXT.md:50,75,175,359`, `DRIVER_SCRIPT.md:51,65`, `STATE.md:48` | nowhere else; retiring it means changing those rows' artifact cells through plan-batch with a STATE.md decision |

What the runbook's hand-back section must absorb so B4 can retire both files: (1) the run-next table role, stated as "the ledger of the runbook (§L) is the status; the hand-back lists next batch per package"; (2) the maintenance protocol (who updates the status when a checkpoint observes a change); (3) the artifact-cell and pointer rewrites in the 12 live Workspace files and the two suite lines (14 in all), the three authority strings of `run_next_batch.py`; (4) the successor pointer that `WORKSPACE_STATE.md:3` carries. `V1_IMPLEMENTATION_SEQUENCE.md` carries nothing the plan, the checklists or the runbook's model column do not.
