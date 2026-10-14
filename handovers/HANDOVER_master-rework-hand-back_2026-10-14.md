# HANDOVER — master rework hand-back (2026-10-14)

*File name `HANDOVER_<topic>_<YYYY-MM-DD>.md` in the `handovers` root, listed in that root's `INDEX.md` in the same
commit. Written in the Repo Hygiene Template Kit's continuation shape (kit `0.3.0`) by step `C1-4` of
`rework/PROMPTS_master-rework-runbook_2026-10-13.md` (the orchestrator, Fable 5.1). The continuation section, like a
prompt, names no proof surface and no invocation; proof belongs to each package row's `validation` cell and to the
documents the runbook §H names. The runbook's §L is the only status; this file is the one-time map to it.*

## 1. What was done

| Lane | Result | Commits of record (suite `sha`) |
|---|---|---|
| `R-0`…`R-3` | the track opened (`rework/` root, `D-2026-10-13-01`), seventeen Phase A audits, the registers merged, the runbook with its ladder, question mirror, operator prompt and ledger | super `8702e0a`, `b5daba2`, `554a591`, `4678e35` |
| `B1` skills and agents | the superproject's `.claude/` synced to the Conductor's set (17 skill folders, 3 agents verbatim), six byte-identical suite mirrors, three operator-only review skills with provenance, `reviews/` as their default root | super `d144d78`, `58e18e7`, `0f75802`; the six mirrors at `B1-2` |
| `B2` instructions | all seven `CLAUDE.md` reconciled to one shape (Authority, layout, Workflow, standards, session rules, roster); the Testing block's worker sentence reworded | super `3c8ae25`, `3be260b`; six suites at `B2-2`/`B2-3` |
| `B3` hygiene | M-8 closing pass; superproject leftovers and the backlog register; Workspace archive; M-9 hold releases; stale scripts and links; the sequencers archived (`archive/` roots); the residual prose sweep; all seven re-pinned to kit `0.3.0` with the Workspace restructure set released and renamed | super `69d10de`, `5e9dce2`, `e9680e0`, `203f790`; Workspace `cead813`, `25b91bc`, `a9b9e6c`; the other suites at `B3-4`, `B3-5`, `B3-7`, `B3-8` |
| `B4` packages | parser-honest edits, out-of-band markers, `DRIVER_SCRIPT.md` pointer stubs, SDA superseded (41 rows deferred), decision lines and traceability sections, the static package proof (0 errors, both parsers) | super `0597766`; the packages at `B4-1`…`B4-4` |
| `B5` design | the Configuration `1.0.0 BINDING` in SharedContracts `design/` (set A; 23 component contracts; Gallery page; matrix seeded); Dashboard, PyApp and AndroidApp anchored to Design Template Kit `1.11.0` with synced copies and emitted stacks; `design-adoption` retired for `design-gate`; readiness rows 1–7 measured | SharedContracts `a3f863d`, `eb521b2`, `8e16658`, `fc60b5a`, `c3ab790`; Dashboard `f03a0eb`; PyApp `52aaed5`; AndroidApp `ffa3214`; super `71e2d5b`, `da64629` |
| `B6` GUI lane (pointed file) | stages 00–06a in all three clients: workspaces bootstrapped, censuses, screen contracts (13 / 37 / 15), gap maps (72 / 118 / 62 gaps), forward surfaces and settings classifications; three gates put to the operator | Dashboard `6eca8eb`; AndroidApp `762bc1e`; PyApp `cac2e5f` (the lane file's §L has every step) |
| `B7` harness | the multi-root parity checker, the package census and newline guards, Codex frozen block-aware in all seven, the scratch gate and harness docs | super `a25b62e`, `ddab755`; PyApp `e17d7ba`; Server `d6a6497` |
| `B8` onboarding | the instance-2 bindings recorded obsolete, the onboarding ledger and §N corrected, GC-1132 reviewed | super `c8fa93d`, `2644ef9`, `a4809ac`; PyApp `2e81a34`, `0d71d71` |
| `K-1`, `K-2` | Design Template Kit `1.11.0` (`612e634`, `v1.11.0`) and Repo Hygiene Template Kit `0.3.0` (`d5b9742`, `v0.3.0`), both merged, tagged and pushed | the kits' own repositories |
| `C1` hand-back | 52 deferred validations planned as 47 rows in eight first-placed batches; §H (H.1 run-next, H.2 order, H.3 decisions, H.4 backlog, H.5 rules, H.6 instance 2, H.7 archive plan, H.8 resume blocks); `SUITE_HANDOFFS.md` reshaped to the living H.1 | super `07ef063`, `f4b814a`; the five packages at `C1-1`; Workspace `1c02549` |

Verified at hand-over: every repository's hygiene checker reads `0 violations` (superproject 3 held, Workspace 10 held, the
other five 0 held); harness parity `pass` over 7 repositories with the Codex freeze green 7/7; the package census `0 errors`
in 10 counted packages (84 batches, 263 rows); the newline guard 0 mixed files. No test, build, browser, emulator or app
launch ran in Phases A and B (kickoff rule 1).

## 2. State at hand-over

- **Heads.** Superproject `master` at the commit that adds this file (its parent `f97de55`); Workspace `a9b9e6c`,
  Server `0e491d3`, SharedContracts `11d33eb`, Dashboard `3b50594`, AndroidApp `a30fc61`, PyApp `50375b7`, each on
  `main`, each clean, each pushed; every gitlink contained in its suite's remote. The superproject is pushed at every
  boundary and after every flip since `R-4.3`.
- **Kits.** All seven pin Repo Hygiene Template Kit `0.3.0` (`D-2026-10-14-03`…`-10`); the three anchored clients and
  SharedContracts pin Design Template Kit `1.11.0` @ `612e634`. Both kits are read-only from this program; their
  findings are rows `RC-B5-01..05` and `RC-B6-01..07` of the reuse register.
- **Held names.** Superproject: the three onboarding-runbook citers. Workspace: 10 (the live-package proposals and the
  terminal-STATE citers; the restructure set is released). The five suites: none.
- **Conductor.** No instance is bound; the instance-2 bindings are obsolete by the operator's word (Q-A8-02). Every
  suite runs out of band from its folder until the operator binds anew (§H.6).
- **Packages.** The seven live packages carry their deferred-validation batches first in plan order (`SV1-B08`,
  `SC1-B04`, `WD1-B09`/`B10`, `AN1-B15`/`B16`, `PY1-B09`/`B10`); the three design-migration workspaces hold no live
  rows until their stage-07 plan acts (`B6a-7b`, `B6c-7b`, `B6b-7b`).
- **Registers.** Questions: 180+ rows, open set below. Deferred validations: every PlantLibrary row `planned (<key>)`;
  `DV-K1-01` planned through AndroidApp `AN1-B15`. Reuse candidates: 264 + 12 Kit findings. Unplanned backlog:
  `UB-01`…`UB-21`.

## 3. Open items by owner

**The operator (decisions; the §O prompt of the runbook walks them in order):**

1. Owed item 18 — the GitHub repository variables `DESIGN_KIT_REPOSITORY` and `DESIGN_KIT_REF=v1.11.0` on the three
   anchored clients (`Q-B5-13`); the design-conformance workflow is red until set.
2. The three GUI gates — `Q-G-a-1-01..09` (Dashboard), `Q-G-b-1-01..09` (AndroidApp), `Q-G-c-1-01..08` (PyApp) — each
   row with its recommended (a) first; the `-6a` steps of the lane file wait on them.
3. `Q-G-10` — the standing answer for the later gates (G-x-2/3/4): "recommended unless flagged" lets the lanes run
   through; otherwise up to nine more stops.
4. The Phase C decisions the hand-back puts on the path: `Q-C1-23` (AndroidApp token storage), `Q-C1-24` (Server
   security sign-offs), `Q-C1-26` (an interim Server harness port before `SV1-B00`), `Q-C1-31` (may Phase C's
   unattended validation batches start before the GUI lanes close).
5. The veto walk over the orchestrator's (a) answers, the flagged rows first: `Q-B6a-10` (Configuration tokens),
   `Q-C1-03` (Gallery baselines as `1.0.1`), `Q-B6c-10` and `Q-B6a-07` (page-contract additions), `Q-B6c-07`,
   `Q-B6c-08`, `Q-C1-21`, `Q-C1-25`.
6. Owed item 11 — the Conductor's `OP-RB` copy into the Workspace (Q-A5-01); owed item 19 — the Kit's two Conductor
   role overrides at the next bind; readiness row 8 (owed item 15) at the next bind.

**The orchestrator (this program, until `R-5`):**

- The GUI lanes from `-6a` on, as the gates are answered: `B6a-6a` first (its SharedContracts writes are serialized),
  then `B6c-6` and `B6b-6` (AndroidApp's after PyApp's SharedContracts writes); `-7a`/`-7b` plan acts (they seed the
  design-migration rows, retire the deferred phase rows, write the anchor notes and record the implementation base
  sha); `-8` implementation batches under Q-R-01 (a) with mechanical design checks only.
- `R-4.4` after this file; `R-5` (close, §0 "Closed", `rework/INDEX.md` `history`, the close HANDOVER, the Phase C
  resume prompt) after the last `B6` step.

**Phase C sessions (after `R-5`), as owed acts that are not batches (§H.3):**

- The superproject `android-validation` skill extended for RC-A9A-11 (capture naming, theme switching), mirrored byte
  for byte, parity green — before `AN1-B16` (`Q-C1-13`).
- The Server harness port (interim per `Q-C1-26` (a), or the Conductor's half) — before the first Server closeout that
  must be green (`Q-C1-02`); the four other suites without `scripts/harness/` read the same way (`Q-C1-27`).
- The next Server package writer adds the hygiene-bookkeeping hard-scope line (`Q-C1-01`); the next Dashboard V1
  package writer adds the `DVC-`/`DV-`/`GAP-` traceability tokens (`Q-C1-10`); the next Workspace package writer amends
  the `_ACT_STATE.md` anchors (`Q-C1-28`) and the `proposal/INDEX.md:23` row (`Q-B3-15`); the next superproject hygiene
  writer appends B3-4's M-9 lines to the track runbook (`Q-B3-14`).
- The onboarding §N pointers GC-2006, GC-6082, GC-2431, GC-2437, GC-7053 resolve through the batches §H.1 names.

## 4. Continuation

```text
Scope: resume the PlantLibrary master rework program from its runbook, rework/PROMPTS_master-rework-runbook_2026-10-13.md, as its orchestrating session (Fable 5.1 · high), from the first todo or waiting row of §L (the GUI lane's rows live in rework/PROMPTS_gui-rework-runbook_2026-10-13.md §L); the operator's answers to the gates and the open rows arrive through the register rework/REGISTER_operator-questions_2026-10-13.md (the §O session) or in chat and are recorded there first.
Read first: the runbook §0, §1, §2 (the rules, the bytes rule, the flip rule), §3a (what may run beside what), §H (this program's hand-back; H.8 holds the Phase C resume blocks), §L; the lane file §L; the register's open rows; this file §3.
Constraints: kickoff §2 unchanged — no test, build, browser, emulator or app launch before R-5; one writer per repository; lanes never write the runbooks or registers, the orchestrator flips in one superproject commit per step with the gitlink; the bytes rule; the Kits and the Conductor checkouts read-only; a kit defect is a finding; a prompt never overrides a skill; pushes by the orchestrator at every boundary and flip.
Done when: every B6 step reads done or retired in the lane file §L, R-4.4 and R-5 read done in §L, the close HANDOVER is written, and the Phase C resume prompt (§H.8's first block, Server SV1-B08) has been printed to the operator.
Commit line: rework: <step id> - <title>
```

**Phase C's first act** is §H.8's first block (Server `SV1-B08`, unattended; its closeout cannot run until the Server
harness exists, `Q-C1-02`), run from the suite folder in a fresh session after `R-5`; the Workspace's convenient first
act is `SY1-B03` (`Q-C1-30`). `R-5` prints that block with its orchestrator note.
