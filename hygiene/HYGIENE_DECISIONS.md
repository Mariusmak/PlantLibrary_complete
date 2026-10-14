# Hygiene decisions — SW_Development

Append-only (`KIT_SPEC.md` §6). Every exemption, hold, release, enum extension, root change, allowlist or
retired-name change, module switch, scratch-root declaration and re-pin is an entry here, never a silent
edit; neither this file nor the pin is edited retroactively — a later entry supersedes an earlier one.
Entries are `### D-YYYY-MM-DD-nn — <title>` under a dated `## YYYY-MM-DD — <heading>`; `nn` is two digits,
unique per day, the next free id verified by grep before writing. An entry carries the operator's verbatim
words where a gate answered (numbered as presented), the authority (gate, runbook step, policy clause), the
preconditions measured, the dispositions and the commit line.

## How the checker reads this file

Inside an entry, a list line `- <directive>: <value>` is machine-read; the value runs to the end of the
line or to the first ` — `, and what follows is a note the checker echoes. Entries fold in file order, so a
later `release` cancels an earlier `held-name`. An unknown directive is a `record` violation — a typo fails
loud. Prose list items never start with a lowercase hyphenated word and a colon. Text inside a fenced code
block is not read.

| Directive | Value | Note |
|---|---|---|
| `exempt-name` | a basename (every root) or a repository-relative path (one file) | why |
| `exempt-subfolder` | a repository-relative path under a root; must exist | why |
| `exempt-tree` | a repository-relative path; must exist | its class first — `frozen`, `pinned`, `generated`, `legacy` — then why |
| `held-name` | a repository-relative path; must exist | `<group>; cited by <citer>; target on release: <name>` |
| `held-line` | `<repository-relative path>:<line>` | why |
| `release` | the held path whose hold ends, in the commit of the `git mv` | the grep or the operator's words |
| `enum-add` | one TYPE, uppercase letters | why the fixed enum does not cover it |
| `allowlist` / `allowlist-remove` | one repository-root entry (file or folder name) | why |
| `retired-name` | one repository-root entry that must never reappear | why |
| `forbidden-path` | one absolute path that must not exist | why |
| `scratch-root` | the scratch folder's name (default `.tmp`) | why |

The shape of an entry:

```text
## YYYY-MM-DD — <heading>

### D-YYYY-MM-DD-01 — <title>

<authority; the operator's verbatim words where a gate answered; preconditions measured; dispositions;
commit line>

- exempt-name: <basename or path> — <why>
- held-name: <path> — <group>; cited by <citer>; target on release: <name>
```

Entries follow, oldest first.

## 2026-09-16 — anchoring

### D-2026-09-16-01 — superproject anchored to the Repo Hygiene Template Kit 0.1.0

Authority: step `A-1` of `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md`, executing the kit's
`installer/INSTALL.md`; gate `G0` (runbook §1d) and gate `GK` (runbook §4). The operator's words: (G0) "all
recommendations accepted" — resolving Q4 as "deliverable roots declared per repo; … the superproject declares
`repo-hygiene\`, `onboarding\` and a new `handovers\` that receives the root HANDOVER by `git mv`", Q8 as "the checker
everywhere; the pytest wrapper where a suite exists; a `.github\workflows\repo-hygiene.yml` template; an optional
pre-commit hook (not installed by default)", Q9 as "`hygiene\CONSUMED_HYGIENE.md` for the pin … and
`hygiene\HYGIENE_DECISIONS.md`, append-only"; (GK, 2026-09-16) "Yes, accept" — the kit at `v0.1.0` is accepted for
anchoring.

Preconditions measured 2026-09-16: superproject on `master`, tree clean at `1ed9d18`; kit clean at `1360c0c`, tag
`v0.1.0`; no pytest suite in this repository (census §4), so no wrapper; `CLAUDE.md` and `AGENTS.md` carry mixed
CRLF/LF inside each file, first line CRLF, no marker pair before this step. Installer run:
`--roots repo-hygiene,onboarding,handovers --modules root-allowlist`, no `--with-pytest-wrapper`, no
`--with-pre-commit`, no launcher, floor 1; closing line `install: done — pin written`.

Roots and routing. `repo-hygiene/` (general) is this track's deliverable root; `onboarding/` (general) is the
onboarding track's, whose `INDEX.md` already lists every file and is not edited here; `handovers/` (handovers,
date-anywhere) is new, seeded with an empty index, and receives every `HANDOVER`/`FINDING` of the superproject —
the root `HANDOVER_batch-package-schema-drift_2026-09-15.md` moves there by `git mv` at step `M-1`, not before.
Every other TYPE goes to the track folder that owns the work. `hygiene/` is the kit's anchoring folder, not a
deliverable root.

Holds (census §3, group "onboarding runbook"; citer `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md`,
which this track never edits; citing line numbers as measured today). The four names are held against renaming,
not against a move — a move keeps the basename. Three of them are already compliant, so their target on release is
their current name. For `IMPLEMENTATION_PLAN.md` the target given is the census proposal (git-created 2026-08-05,
header date 2026-08-04 — a divergence, Q5a); its disposition is `M-0`'s proposal 1, which recommends an exemption as
the living program plan, and `GM` decides. The two root-level holds sit outside every declared root, so the
checker does not list them among its `held:` lines; the record carries them so `M-0` and `M-1` map against them.

- held-name: HANDOVER_batch-package-schema-drift_2026-09-15.md — onboarding-runbook; cited by onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:5; target on release: HANDOVER_batch-package-schema-drift_2026-09-15.md (unchanged; moves to handovers/ at M-1)
- held-name: IMPLEMENTATION_PLAN.md — onboarding-runbook; cited by onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:17,52,210,213,217,221,685,820,845,898; target on release: PLAN_plantlibrary-continuation_2026-08-05.md (date divergence: git-created 2026-08-05, header 2026-08-04; disposition is M-0 proposal 1)
- held-name: onboarding/AUDIT_skill-assumptions_2026-09-15.md — onboarding-runbook; cited by onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:211,212,216,905; target on release: AUDIT_skill-assumptions_2026-09-15.md (unchanged)
- held-name: onboarding/REGISTER_package-census_2026-09-15.md — onboarding-runbook; cited by onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:251,584,911; target on release: REGISTER_package-census_2026-09-15.md (unchanged)

Root allowlist (module on here and in no submodule). The allowlist is the repository root's listing on
2026-09-16, `.git` excluded, tracked, untracked and ignored alike (`Todo.md` and `graphify-out` are git-ignored but
present), plus the three entries this anchoring creates (`.github`, `handovers`, `hygiene`). Retired names: none.
Forbidden paths: none. `HANDOVER_batch-package-schema-drift_2026-09-15.md` leaves the root at `M-1`, whose entry
removes it from the allowlist.

- allowlist: .agents — runtime skill mirror (onboarding track)
- allowlist: .claude — runtime skill mirror and settings (onboarding track)
- allowlist: .codex — runtime skill mirror and hooks (onboarding track)
- allowlist: .github — created by this anchoring: the repo-hygiene workflow
- allowlist: .gitignore — repository configuration
- allowlist: .gitmodules — submodule configuration
- allowlist: AGENTS.md — agent instructions carrying the rule block
- allowlist: CLAUDE.md — agent instructions carrying the rule block
- allowlist: HANDOVER_batch-package-schema-drift_2026-09-15.md — held at the root until M-1 moves it to handovers/
- allowlist: IMPLEMENTATION_PLAN.md — the program plan; its home and name are M-0 proposal 1
- allowlist: PlantLibrary_AndroidApp — submodule
- allowlist: PlantLibrary_Dashboard — submodule
- allowlist: PlantLibrary_PyApp — submodule
- allowlist: PlantLibrary_Server — submodule
- allowlist: PlantLibrary_SharedContracts — submodule
- allowlist: PlantLibrary_Workspace — submodule
- allowlist: Todo.md — personal notes, git-ignored but present
- allowlist: graphify-out — graphify output, git-ignored but present
- allowlist: handovers — created by this anchoring: the handovers root
- allowlist: hygiene — created by this anchoring: the kit's anchoring folder
- allowlist: onboarding — the onboarding track's deliverable root
- allowlist: repo-hygiene — this track's deliverable root
- allowlist: scripts — harness scripts and the installed checker
- allowlist: update_graph.bat — graphify refresh launcher

Scratch module: off here and deferred to the onboarding track's step `3`, which owns the per-suite scratch policy;
nothing in this step edits `.gitignore`. No enum extension. No exemption beyond the built-in `INDEX.md` and
`README.md` (the root's `CLAUDE.md`, `AGENTS.md` and `Todo.md` sit outside every declared root and are governed by
the allowlist only).

Commit line: `repo-hygiene: A-1 - superproject anchored to kit 0.1.0; GK recorded`

## 2026-09-16 — kit re-pin

### D-2026-09-16-02 — superproject re-pinned to kit 0.2.1

Authority: step `K-6` of `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md`, executing the kit's
`installer/INSTALL.md`, "The pin" (a kit upgrade is a re-run with `--target` alone, then `--force` once the re-pin is
decided); the finding `handovers/FINDING_kit-release-after-move-fails-record_2026-09-16.md`. The operator's words,
recorded there when asked how `M-1` should proceed: "Stop; kit patch first (Recommended)".

Preconditions measured 2026-09-16: superproject on `master`, tree clean at `07e2f48`; kit clean at `810733e`, tag
`v0.2.1`; the pin recorded kit `0.1.0` @ `C:/Programmierung/Repo_Hygiene_Template_Kit`; the declaration is unchanged —
roots `repo-hygiene` (general, standard), `onboarding` (general, standard), `handovers` (handovers, date-anywhere);
module `root-allowlist`; no pytest wrapper; no pre-commit hook; no launcher; prompt file floor 1. Installer runs:
`--target` alone → `install: done — pin records kit 0.1.0 @ C:/Programmierung/Repo_Hygiene_Template_Kit; this kit is
0.2.1 @ C:/Programmierung/Repo_Hygiene_Template_Kit; re-run with --force to re-pin` (the checker copy re-synced, both
rule blocks updated to `0.2.1` inside their markers, each file keeping its line endings); then `--force` →
`install: done — pin re-written (--force)`, `Pinned on` today, the roots table unchanged.

Why: kit `0.1.0` and `0.2.0` judged a `held-name`'s existence when they folded that line, so the `M-1` entry that
releases `HANDOVER_batch-package-schema-drift_2026-09-15.md` after its `git mv` into `handovers/` and holds the new
path could never pass `record` (the finding, "Why"). Kit `0.2.1` judges existence after the whole record is folded,
only for holds still active, on the `held-name` line in force; a released hold needs no file (`KIT_SPEC.md` §1.6, §6).
Dispositions: nothing in this entry changes the held set — the four holds of `D-2026-09-16-01` stand, the allowlist
stands, and the verdict is unchanged (`repo-hygiene: pass with holds — 0 violations, 2 held`, the same two `held:`
lines). `M-1` runs next, on `0.2.1`, with a `release` of the old path and a `held-name` for
`handovers/HANDOVER_batch-package-schema-drift_2026-09-15.md` in its own entry (runbook §14). No directive line.

Commit line: `repo-hygiene: K-6 - superproject re-pinned to kit 0.2.1; runbook resumes M-1; finding resolved`

## 2026-09-16 — migration

### D-2026-09-16-03 — superproject migrated per the confirmed rename map

Authority: step `M-1` of `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` (§14), executing the
superproject's section of `repo-hygiene/MATRIX_rename-map_2026-09-16.md` (§3) by the execute stage of the kit's
`runbooks/RUNBOOK_migrate-an-existing-repository.md`; gate `GM` (runbook §4). The operator's words at `GM`, verbatim:
"Yes, all recommendations accepted (Recommended)" — given to the question that listed the map's six proposals and two
map calls; for this repository that settles proposal 1 as "(a) exempt by decision as the living program plan …,
entered in the root allowlist (it already is) and listed as a never-renamed row". The kit rule that makes the move
recordable is `0.2.1`'s (`D-2026-09-16-02`; `handovers/FINDING_kit-release-after-move-fails-record_2026-09-16.md`): a
held name must exist only while held, and a released hold needs no file.

Preconditions measured 2026-09-16: superproject on `master`, tree clean at `e639e5c`; the pin reads kit `0.2.1`; the
verdict before the step `repo-hygiene: pass with holds — 0 violations, 2 held`; the four holds of `D-2026-09-16-01`
re-verified by `git grep` — the onboarding runbook still cites the handover on line 5 (by basename), the `AUDIT` on
lines 211, 212, 216, 905, the `REGISTER` on 251, 584, 911, and `IMPLEMENTATION_PLAN.md` on ten lines.

Dispositions, in the map's order:

1. Moved: `HANDOVER_batch-package-schema-drift_2026-09-15.md` → `handovers/HANDOVER_batch-package-schema-drift_2026-09-15.md`
   by `git mv` (`G0` Q4), basename unchanged. Its hold continues at the new path: the onboarding runbook cites it by
   basename, which still resolves, and never by path. The old path is released and the new path held in this entry;
   the name leaves the root allowlist. `handovers/INDEX.md` gains its line and the "Renamed 2026-09-16" row.
2. Renamed: nothing — the other superproject candidates are compliant (map §3).
3. Held, unchanged: `onboarding/AUDIT_skill-assumptions_2026-09-15.md`, `onboarding/REGISTER_package-census_2026-09-15.md`
   (`D-2026-09-16-01`); their mapping rows are carried in `repo-hygiene/INDEX.md`, since the onboarding track's index
   takes only the one-line path fix (runbook §14).
4. Exempt by decision: `IMPLEMENTATION_PLAN.md`, the living program plan (`GM` proposal 1), already allowlisted; its hold
   is moot and released here, its census target `PLAN_plantlibrary-continuation_2026-08-05.md` is not applied. It is a
   root-level file, so the `exempt-name` value below is read as a basename; no declared root holds a file of that name
   today (the frozen MVP packages' files of the same basename are in submodules, outside this repository's roots).
5. Sweep: `onboarding/INDEX.md` line 10, the relative link `../HANDOVER_…` → `../handovers/HANDOVER_…` (a path fix,
   one line). No other file cites the old path as a link; `CLAUDE.md` and `AGENTS.md` cite neither name. The onboarding
   runbook, register and audit, and every submodule, are untouched.

- release: HANDOVER_batch-package-schema-drift_2026-09-15.md — moved to handovers/ by git mv in this commit (M-1)
- held-name: handovers/HANDOVER_batch-package-schema-drift_2026-09-15.md — onboarding-runbook; cited by onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:5; target on release: HANDOVER_batch-package-schema-drift_2026-09-15.md (unchanged)
- allowlist-remove: HANDOVER_batch-package-schema-drift_2026-09-15.md — moved to handovers/ at M-1
- release: IMPLEMENTATION_PLAN.md — moot: exempt by decision per GM proposal 1
- exempt-name: IMPLEMENTATION_PLAN.md — the living program plan, never renamed (GM proposal 1); allowlisted since D-2026-09-16-01

Commit line: `repo-hygiene: M-1 - superproject migrated per the confirmed map; INDEX mapping tables`

## 2026-10-13 — master rework track opened

### D-2026-10-13-01 — general root `rework` declared for the PlantLibrary master rework program

Authority: step `R-0` of `rework/PROMPT_master-rework-kickoff_2026-10-13.md` (§3), the kickoff prompt of the
PlantLibrary master rework program, executed by its orchestrating session (Fable 5.1 · high). No operator gate
answered here: the kickoff names the root, its kind and its pattern, and §2 rule 3 of that prompt requires this
entry. The pin's own rule (`hygiene/CONSUMED_HYGIENE.md`, header): a root change is a decision entry with the roots
table edited in the same commit, and the checker reads roots from that table only.

Preconditions measured 2026-10-13: superproject on `master`, tree clean at `67dcc51` except the
`PlantLibrary_Workspace` gitlink (checkout `6b4b88b`, two already-committed Workspace commits ahead of the pinned
`752ff51`, bumped in this commit); all six submodules on `main`, clean; no worktree beyond the seven checkouts;
verdict before this step `repo-hygiene: pass with holds — 0 violations, 3 held` (the onboarding-runbook holds of
`D-2026-09-16-01`/`D-2026-09-16-03`, unchanged by this entry); last entry `D-2026-09-16-03`.

Dispositions:

1. Root: `rework/` is declared a **general** root with the **standard** pattern (`<TYPE>_<topic>_<YYYY-MM-DD>.md`),
   the deliverable root of the master rework program for its prompts, runbook, registers, audits, matrices and
   findings. Its `INDEX.md` is written in this commit (table shape, as `repo-hygiene/INDEX.md`), not seeded by the
   installer. Every HANDOVER of the program still goes to `handovers/` (`D-2026-09-16-01`, routing).
2. Allowlist: `rework` enters the root allowlist (module `root-allowlist`, on since `D-2026-09-16-01`).
3. Files born in the root in this commit: `PROMPT_master-rework-kickoff_2026-10-13.md` (the kickoff prompt,
   verbatim, its only copy), `PROMPTS_master-rework-runbook_2026-10-13.md` (the program runbook, §3 filled at
   `R-3`), `REGISTER_operator-questions_2026-10-13.md`, `REGISTER_deferred-validations_2026-10-13.md`,
   `REGISTER_conductor-reuse-candidates_2026-10-13.md`. Each has its `INDEX.md` line. Both prompt files pass the
   proof-surface rule as written.
4. Nothing else changes: no exemption, no hold, no release, no enum extension, no scratch module; the
   `IMPLEMENTATION_PLAN.md` exemption and the three holds stand (their fate is the program's `Q-G-05` and the
   `B3` lane, each a later entry).

- allowlist: rework — the master rework program's deliverable root (kickoff prompt §3 R-0 (a))

Commit line: `rework: R-0 - track opened; Workspace gitlink 6b4b88b`

### D-2026-10-13-02 — graphify leftovers retired: `graphify-out` deleted, `update_graph.bat` removed

Authority: step `B3-2` of `rework/PROMPTS_master-rework-runbook_2026-10-13.md` (§3.5), run headless (Opus 5.5 · high),
on the operator's answer to `Q-A6S-03` as recorded in `rework/REGISTER_operator-questions_2026-10-13.md`, verbatim:
"Do everything you can on your own. Reduce the operator steps to a minimum." … "all other recommended." (2026-10-13
18:05 UTC, §O session 2d91d072), resolving to (a) with the register's Reading: the step itself deletes the untracked,
git-ignored `graphify-out/` before writing this entry, and owed item 13 of the runbook's §3b is discharged here. The
step's block, written at `R-4.1` on that Reading, removes `update_graph.bat` by `git rm`; the option text's "`git mv
update_graph.bat archive/root/` (never delete)" is therefore not applied (the superproject has no `archive/` yet), and
the launcher stays recoverable as `git show 4b2027d:update_graph.bat`. This finishes the graphify drop answered as `D5`
on 2026-10-02 (hooks and instruction blocks removed in `7946483` and `53051b0`).

Preconditions measured 2026-10-13: superproject on `master` at `4b2027d`, no superproject file modified (the six
submodule gitlinks show working-tree changes made outside this step; none is staged here); verdict before the step
`repo-hygiene: pass with holds — 0 violations, 3 held`; last entry `D-2026-10-13-01`, so the next free id by grep over
this file is `-02` (the superproject's other mentions of `D-2026-10-13-02`/`-03` name entries of Workspace's record).
`git check-ignore graphify-out` matched (`.gitignore:12`) and `git ls-files graphify-out` printed nothing; the tree held
2,460 files in 6 folders, 281,673,762 bytes, with no link or junction. `update_graph.bat` was tracked and still called
`graphify update .`; its citers are `.gitignore:11` (a comment), the allowlist line of `D-2026-09-16-01` and the rework
audits and registers that describe this retirement.

Dispositions:

1. Deleted from disk: `graphify-out/` (untracked, git-ignored, the output of the dropped tool), by a short Python script
   (`shutil.rmtree` after the ignore, tracked-file and link checks), not by a shell `rm`.
2. Removed: `update_graph.bat`, by `git rm` in this commit.
3. Both names leave the root allowlist and become retired names, so a run of the graphify tool that regrows either at
   the root fails the checker (`retired`, `allowlist`) instead of growing silently.
4. Not changed here: `.gitignore:11-12` (the ignore line and its comment, now dead; their fate is a question proposed in
   the step's report), `.agents/README.md:77-85` (its graphify narrative; that file's rewrite belongs to `B2`), and the
   onboarding and repo-hygiene records that mention graphify (history). No file cites either name as a path to follow.
5. Same commit, outside this record: `rework/REGISTER_unplanned-backlog_2026-10-13.md` is born with its
   `rework/INDEX.md` line (`Q-G-05` (a), `Q-A6S-04` (a); `Todo.md` untouched).

- allowlist-remove: graphify-out — deleted from disk at B3-2 (Q-A6S-03 (a) with its Reading)
- allowlist-remove: update_graph.bat — removed by git rm at B3-2 (Q-A6S-03 (a))
- retired-name: graphify-out — output of the dropped graphify tool; must not regrow at the root
- retired-name: update_graph.bat — launcher of the dropped graphify tool; must not reappear

Commit line: `rework: B3-2 - backlog register; graphify leftovers retired; D-2026-10-13-02`

### D-2026-10-13-03 — Codex frozen: `.codex/**` and `AGENTS.md` outside its installer blocks; the freeze guard

Authority: step `B7-2` of `rework/PROMPTS_master-rework-runbook_2026-10-13.md` (§3.3), run headless (Opus 5.5 · high),
on the operator's answers to `Q-G-09` and `Q-A3-01` as recorded in `rework/REGISTER_operator-questions_2026-10-13.md`,
verbatim: "all other recommended." (2026-10-13 18:05 UTC, §O session 2d91d072), resolving each to (a): Codex is frozen
as the Conductor froze it (`D-2026-10-02-23` (c) of `C:/Programmierung/Orchestrator_System`), but block-aware, so the
installer-owned blocks of `AGENTS.md` stay live. `Q-B7-02` (a), answered by the orchestrator on the operator's standing
instruction: no separate per-suite `.claude`↔`.codex` compare; this freeze covers the suites. The shape follows
`rework/AUDIT_skills-and-agents_2026-10-13.md` §7.6 items 1-5 and §7.7 item 3.

Preconditions measured 2026-10-13: superproject on `master` at `1cd675d`, no superproject file modified (the
`PlantLibrary_SharedContracts` gitlink shows B5-2's commit `a3f863d`, not staged here); verdicts before the step
`repo-hygiene: pass with holds — 0 violations, 3 held` and `harness parity: pass` (B7-1's checker, codex compare on);
59 tracked files under `.codex/` (13 skill folders, 3 agent `.toml`, `hooks.json`, `hooks/deny_git_commands.mjs`),
none untracked; `AGENTS.md` 33 lines, CRLF in the working tree, the `repo-hygiene` block its only marker block, no title
heading (it opens with `## Testing`); last entry `D-2026-10-13-02`, so the next free id by grep over this file is `-03`
(the one other mention of `D-2026-10-13-03` in this repository, `rework/AUDIT_corpus-census-workspace_2026-10-13.md`,
names an entry of Workspace's record).

Dispositions:

1. Frozen: every file under `.codex/` as it stands at the freeze commit — kept, never deleted, not edited, not mirrored.
   Exempt: the four Kit folders `.codex/skills/design-gate/`, `design-audit/`, `gallery-governance/` and `impeccable/`
   (absent today; the Design Template Kit installs and re-pins them from `B5` on), `settings.local.json` and any
   `__pycache__/`. A skill or agent changed or added from now on lives under `.claude/` only.
2. Frozen: `AGENTS.md` outside its installer-owned marker blocks, `<!-- repo-hygiene:begin -->`…`<!-- repo-hygiene:end -->`
   now and `<!-- design-kit:begin -->`…`<!-- design-kit:end -->` once `B5` installs it. The installers keep writing their
   blocks and the hygiene checker keeps enforcing their parity with `CLAUDE.md`; every other edit goes to `CLAUDE.md`,
   the live text.
3. Freeze commit: the commit immediately preceding this entry's commit in this repository, `1cd675d`. Its tree holds the
   pre-banner `AGENTS.md` and the frozen `.codex/**` bytes; naming the parent, not this commit, avoids a hash fixed point.
4. Banner: one line, `` > Frozen 2026-10-13 (`D-2026-10-13-03`): codex disabled; `CLAUDE.md` is the live text. ``,
   inserted as line 1 of `AGENTS.md` (the file opens heading-less, with its `## Testing` section) in the line endings
   the file carries; no other byte changes (`git hash-object` of the file with the banner line removed equals the
   pre-step blob `3ddbec9`). The banner lies outside the hygiene block, so the block parity stays green.
5. Guard: `scripts/harness/check_harness_parity.py` gains the freeze check over all seven repositories — a `FROZEN_AT`
   row and a `FREEZE_DECISIONS` row per repository; SHA-256 pins of CRLF→LF-normalized bytes written once from
   `git show <freeze commit>:<path>` by its `--print-freeze-table <repo>=<commit>` mode, never from the working tree;
   `AGENTS.md` pinned with each marker block removed (markers included) and blank-line runs collapsed, so an installer
   that inserts, updates or moves its block is not drift; the banner required once, as line 1 or directly under the
   first heading line. The `.claude`↔`.codex` compare is off by default (`--with-codex-compare` turns it back on). A
   bridge-coverage check requires every `.claude/skills/*` folder to be a frozen bridge row or a Claude-only row in
   `.agents/README.md`; until `B1-1` rewrites that file it prints "README pending" and does not fail. The six suites'
   freeze commits are their entries' parents, recorded in their own records (PyApp, AndroidApp, Dashboard, Server
   `D-2026-10-13-02`; Workspace, SharedContracts `D-2026-10-13-03`).
6. Unfreeze recipe (each a later entry in the repository concerned): re-mirror `.claude/**` changes since the freeze
   commit into `.codex/**`, and `CLAUDE.md`'s text outside the blocks into `AGENTS.md`; remove the banner; flip the
   `frozen` bridge statuses in `.agents/README.md` back to `mirrored`; set the repository's `FROZEN_AT` row to `None`
   and drop its pins; for the superproject, make `--with-codex-compare` the default again.

No directive line: the entry changes no root, exemption, hold or allowlist (`.codex/` is not a declared root).

Commit line: `rework: B7-2 - codex frozen; AGENTS.md banner; D-2026-10-13-03`

## 2026-10-14 — master rework: the sequencers archived

### D-2026-10-14-01 — `archive/` declared and `IMPLEMENTATION_PLAN.md` archived into it; general root `reviews` declared

Authority: step `B3-6` of `rework/PROMPTS_master-rework-runbook_2026-10-13.md` (§3.5, lane B3), run headless (Opus 5.5 ·
high), on the hand-back section §H of that runbook (written at `C1-2`, commit `07ef063`; H.7 is this step's plan) and
on the operator's answers recorded in `rework/REGISTER_operator-questions_2026-10-13.md`, verbatim: "all other
recommended." (2026-10-13 18:05 UTC, §O session 2d91d072), resolving `Q-G-05`, `Q-A6S-01` and `Q-A6S-05` to (a): the
stale sequencers are archived once §H replaces them; one top-level `archive/`, allowlisted, `exempt-tree … legacy`,
with subfolders by origin; the spent hygiene-track files leave `repo-hygiene/` only after `M-8`/`M-9`. `Q-B3-09` (a)
and `Q-B1-04` (a), answered by the orchestrator 2026-10-13 under the operator's standing instruction (`Q-G-03`): the
dead graphify lines of `.gitignore` are removed here, and a general root `reviews` is declared here for the
operator-run review skills. Drafts: `rework/AUDIT_corpus-census-superproject_2026-10-13.md` §7.3 (layout (a)),
`rework/AUDIT_batch-packages_2026-10-13.md` §7.4.

Preconditions measured 2026-10-14: superproject on `master` at `e6545d1`, tree clean; §H present (H.1–H.7); verdict
before the step `repo-hygiene: pass with holds — 0 violations, 3 held`; `archive` and `reviews` did not exist; the
root hold on `IMPLEMENTATION_PLAN.md` of `D-2026-09-16-01` was already released (`D-2026-09-16-03`), so the move needs
no `release`; no `D-2026-10-14-*` id existed in this repository, in any of the six submodules (`git -C <suite> grep`,
tracked and untracked) or in any worktree (none beyond the seven checkouts), so this is `-01`; last entry here
`D-2026-10-13-03`. `graphify-out/` and `update_graph.bat` are gone since `D-2026-10-13-02`.

Dispositions:

1. Declared: `archive/` at the repository root, its `README.md` (purpose, rules, the mapping table
   `| old path | new path | date | entry |`) created in this commit so the declared path exists when the line folds.
   Only the top-level path is declared, never a sub-path, so the folder never has to move (finding K-7). It is not a
   deliverable root: no roots-table row, no `INDEX.md`.
2. Moved: `IMPLEMENTATION_PLAN.md` → `archive/root/IMPLEMENTATION_PLAN.md` by `git mv`, basename unchanged, no byte
   changed; its mapping row in `archive/README.md`. It leaves the root allowlist. Its `exempt-name` line of
   `D-2026-09-16-03` stays as written and is inert (no declared root holds a file of that basename; `exempt-name` has
   no existence check).
3. Citers. The ten citing lines of `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` (17, 52, 210, 213,
   217, 221, 685, 820, 845, 898) stay as they are (that runbook is live and another track's; the name resolves
   through `archive/README.md`). Repointed: `CLAUDE.md`'s repository-layout table (the `IMPLEMENTATION_PLAN.md` row
   becomes the `archive/` row; `reviews/` joins the declared-roots row). History that names the file (the
   `repo-hygiene/` records, `handovers/FINDING_kit-release-after-move-fails-record_2026-09-16.md`, the `rework/`
   audits and registers) is not edited.
4. Declared: `reviews/` as a **general** root with the **standard** pattern, the standing home of the operator-run
   review skills' deliverables (`code-quality-review`, `security-audit`, `pathfinder`; each writes
   `AUDIT_<skill>-<topic>_<YYYY-MM-DD>.md` into the general root the operator names). The roots table of
   `hygiene/CONSUMED_HYGIENE.md` gains its row in this commit (the pin's rule: a root change is a decision entry with
   the table edited in the same commit); `reviews/INDEX.md` is seeded from the kit's `templates/INDEX_TEMPLATE.md`
   (`0.2.1`) with no lines.
5. `.gitignore`: the dead graphify ignore line and its comment (lines 11-12) removed, with the blank line that
   followed them, so one blank line still separates the remaining groups.
6. Not here: the spent `repo-hygiene/` track files (`Q-A6S-05` (a): `B3-8` and the Workspace release), the onboarding
   holds (`Q-A6S-02` (a)), `Todo.md` (`Q-A6S-04` (a)), any submodule (the Workspace's own move is its entry there).

- allowlist: archive — retired material moved in by git mv with basenames unchanged (Q-A6S-01 (a))
- exempt-tree: archive — legacy; retired superproject files, moved not renamed, under subfolders by origin (archive/root/ …); declared at the top-level path only so the folder never needs to move
- allowlist-remove: IMPLEMENTATION_PLAN.md — moved to archive/root/ at B3-6 (Q-G-05 (a)); replaced by the master rework runbook's §H
- allowlist: reviews — general root for the operator-run review skills' deliverables (Q-B1-04 (a))

Commit line: `rework: B3-6 - sequencers archived (WORKSPACE_STATE.md, IMPLEMENTATION_PLAN.md, V1_IMPLEMENTATION_SEQUENCE.md); D-2026-10-14-01`

## 2026-10-14 — master rework: re-pin to kit 0.3.0

### D-2026-10-14-03 — re-pinned to kit 0.3.0

Authority: step `B3-8` of `rework/PROMPTS_master-rework-runbook_2026-10-13.md` (§3.5, lane B3), run headless (Opus 5.5 ·
high), by the kit's `installer/INSTALL.md`, "The pin" (a kit upgrade is a re-run with `--target` alone, then `--force`
once the re-pin is decided, then the verification, committed together), on `Q-B3-02` (a) as recorded in
`rework/REGISTER_operator-questions_2026-10-13.md`: one minor release `0.3.0` carrying `K-7` and the pilot's lessons,
then all seven repositories re-pinned — answered by the orchestrator 2026-10-13 under the operator's standing
instruction (`Q-G-03`) and the operator's words "Q-G-06: a (run yourself)" (2026-10-13 19:07 UTC). The release: the
kit's `main` at `d5b9742`, tag `v0.3.0` (step `K-2`, its §L row), changelog `KIT_VERSION.md` "0.3.0 — 2026-10-13": a
`release` may end an `exempt-tree` or `exempt-subfolder` declaration, a `held-name` may name a set folder; additive,
"a record that passes on `0.2.1` passes on `0.3.0` with the same lines".

Preconditions measured 2026-10-14: superproject on `master` at `6fe9cb7`, tree clean; verdict before the step
`repo-hygiene: pass with holds — 0 violations, 3 held`; the pin records kit `0.2.1` (`Pinned on` 2026-09-16), Modules
`root-allowlist`, no wrapper, rule block on, no launcher, floor 1; the kit checkout
`C:/Programmierung/Repo_Hygiene_Template_Kit` on `main` at `d5b9742` (`v0.3.0`), clean; `D-2026-10-14-01` (here) and
`-02` (the Workspace) exist from `B3-6`, and no other `D-2026-10-14-*` id existed in this repository (tracked and
untracked), in any of the six submodules (`git -C <suite> grep` and the working files) or in any worktree (none beyond
the seven checkouts), so this is `-03`; last entry here `D-2026-10-14-01`.

Dispositions:

1. Run from the superproject, the kit read-only (bytecode writing off): `python
   C:/Programmierung/Repo_Hygiene_Template_Kit/installer/install.py --target C:/Programmierung/SW_Development` →
   `wrote scripts/hygiene/repo_hygiene_check.py`, `updated CLAUDE.md — rule block`, `updated AGENTS.md — rule block`,
   the workflow `unchanged`, the five root indexes and the record `kept`, `kept hygiene/CONSUMED_HYGIENE.md — Kit
   version '0.2.1' → '0.3.0'`, then `install: done — pin records kit 0.2.1 @ C:/Programmierung/Repo_Hygiene_Template_Kit;
   this kit is 0.3.0 @ C:/Programmierung/Repo_Hygiene_Template_Kit; re-run with --force to re-pin`, exit 0; then the
   same command with `--force` → every other path `unchanged`, `skipped` or `kept`, `wrote hygiene/CONSUMED_HYGIENE.md`,
   then `install: done — pin re-written (--force)`, exit 0.
2. What changed: the checker copy, byte-identical to the kit's `checker/repo_hygiene_check.py` (`cmp`); one line in
   the installer-owned block of `CLAUDE.md` and of `AGENTS.md` (`@ 0.2.1` → `@ 0.3.0`), each file keeping its line
   endings, no byte outside the block touched; the pin's `Kit version` `0.3.0` and `Pinned on` 2026-10-14. The
   declaration is unchanged: the roots table, Modules `root-allowlist`, no wrapper, no launcher, floor 1.
3. The kit's `scratch` module stays off here (`Q-A2-06` (a): the superproject turns it on only when a step needs
   scratch); the six suites enable it in their own re-pin entries of this step.
4. No directive line: this record holds no `exempt-tree` or `exempt-subfolder` that moved and no folder hold, so
   `0.3.0` changes nothing in this repository's verdict.
5. In the same commit, outside the re-pin: `reviews/INDEX.md`'s header names the `FINDING_security-audit-…` form beside
   `AUDIT_…` (`Q-B3-13` (a), answered by the orchestrator 2026-10-14 under `Q-G-03`); the hygiene track runbook
   `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` gains its `M-9` ledger line for the Workspace set
   folder released by this step (the Workspace's `D-2026-10-14-05`).

Verify after: `repo-hygiene: pass with holds — 0 violations, 3 held`.

Commit line: `hygiene: B3-8 - re-pinned to kit 0.3.0; superproject`
