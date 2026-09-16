# FINDING — a hold released by a move always fails `record` (kit 0.1.0 / 0.2.0) (2026-09-16)

Written for: the operator of this repository and the session that patches the Repo Hygiene Template Kit.

## What happened

Step `M-1` of `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` (§14) moved the root
`HANDOVER_batch-package-schema-drift_2026-09-15.md` into `handovers/` by `git mv`, as `G0` Q4 and the confirmed map
(`repo-hygiene/MATRIX_rename-map_2026-09-16.md` §3) require. The name is held by `D-2026-09-16-01` line 83. The step's
new entry `D-2026-09-16-02` carried, in file order:

```text
- release: HANDOVER_batch-package-schema-drift_2026-09-15.md — moved to handovers/ by git mv in this commit
- held-name: handovers/HANDOVER_batch-package-schema-drift_2026-09-15.md — onboarding-runbook; cited by …:5; target on release: (unchanged)
- allowlist-remove: HANDOVER_batch-package-schema-drift_2026-09-15.md — moved to handovers/ at M-1
- release: IMPLEMENTATION_PLAN.md — moot by GM proposal 1
- exempt-name: IMPLEMENTATION_PLAN.md — the living program plan (GM proposal 1)
```

The checker's verdict:

```text
hygiene/HYGIENE_DECISIONS.md:83: record — held-name HANDOVER_batch-package-schema-drift_2026-09-15.md does not exist
repo-hygiene: fail — 1 violations, 3 held
```

Every other part of the step was correct: the three `held:` lines are the expected ones, and the
`IMPLEMENTATION_PLAN.md` release and exemption fold without a finding, because that file did not move.

## Why

`_apply_directive` in `checker/repo_hygiene_check.py` (kit `0.1.0` and `0.2.0`; installed here as
`scripts/hygiene/repo_hygiene_check.py:447-449`) checks `held-name` existence at the moment it folds that line. A later
`release` of the same path deletes the hold (lines 453-457) but cannot withdraw the problem already reported.
`KIT_SPEC.md` §6 requires both "`held-name` … must exist" and "`release` … in the commit of the `git mv`". The record
is append-only, so the earlier `held-name` line can never be edited away. The result is that **any hold that ends
with a move or rename is unreachable**. No fixture under `tests/` exercises `release`, so `K-3`/`K-5` could not see
this.

## Who else it blocks

- `M-3` (Server): proposal 6 releases two terminal-`STATE.md` holds with a move-rename.
- `M-5` (Dashboard): the same, for two names.
- `M-9`: every rolling release.
- `M-2`…`M-7`: any held file whose move waits with its rename.

## Proposed fix (for the kit session to decide)

1. Check `held-name` existence after the whole record is folded, only for holds still active, and report the problem
   on the `held-name` line that is still in force. A released hold is history and needs no file.
2. Add a fixture, `tests/held-name-released-by-move`: a `held-name` for an old path, the file moved, and a later
   `release` plus a new `held-name` at the new path. The expected result is `pass with holds — 0 violations, 1 held`.
   Also add a negative companion (an active hold whose file is gone → `record`).
3. Change `KIT_SPEC.md` §6 to read "must exist while held". Then a patch release (`0.2.1`), a tag, and the
   superproject re-pinned (it is on `0.1.0`), with a re-pin decision entry. The suites re-sync at their `M-n`.

## Decision

Asked "How should M-1 proceed?", the operator answered, verbatim, "Stop; kit patch first (Recommended)". The
recommendation was the `K-5` route: this finding, a kit-patch step in the runbook, `M-1` left `todo`, and the
`M-1` working-tree changes reverted.

## State at the stop

`M-1` is not committed. The operator reverted the draft by hand (the move, the one-line `onboarding/INDEX.md` path
fix, both mapping tables, entry `D-2026-09-16-02`). The superproject is back at `46eaf75` with a
`pass with holds — 0 violations, 2 held` verdict, and this finding is its only addition. Two notes carry over to the
`M-1` rerun:

- **The mapping tables.** The map's §3 names a "Renamed" table in `onboarding/INDEX.md` for the two held
  `onboarding/` rows, but the runbook's §14 allows only one line there, the path fix. The draft followed the runbook
  and carried those rows in `repo-hygiene/INDEX.md`. The coverage check is satisfied either way, because both names
  already appear in `onboarding/INDEX.md`.
- **`IMPLEMENTATION_PLAN.md`.** It is a root-level file, so its `exempt-name` line is read as a basename exemption. No
  declared root holds that name, and the draft's entry said so.

## Next action — the continuation prompt (step `K-6`)

**Fable 5.1 · high** (the runbook's §18 ladder: building against a written specification; if Fable is unavailable, use
Opus 5 · high plus the mandatory fresh-context review of §18). One fresh session. `cwd`: KIT first, then TARGET for the
re-pin and the runbook and index edits. Paste the block exactly as it stands.

```text
Step K-6 (kit patch: a hold released by a move) of the repo-hygiene track. TARGET = C:\Programmierung\SW_Development
(superproject branch master), KIT = C:\Programmierung\Repo_Hygiene_Template_Kit (main, tree clean at tag v0.2.0,
commit 77ab513). cwd KIT. The authority is TARGET\handovers\FINDING_kit-release-after-move-fails-record_2026-09-16.md;
the operator's decision is quoted there: "Stop; kit patch first (Recommended)". Goal: a held-name whose file later moves
or is renamed must be releasable in the commit of the git mv; release the kit as 0.2.1; re-pin the superproject so M-1
can run; update the track runbook so M-1...M-7 and M-9 run on 0.2.1. No submodule of TARGET is touched. Nothing is
pushed.

Read first: the finding in full; TARGET\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md sections 0, 2, 3,
14, 15, 17, 18 and L; KIT\KIT_SPEC.md sections 1.6, 6, 7, 9, 11; KIT\CONTRIBUTING.md in full (its verification order and
its "what green means" table are the contract for this step); KIT\installer\INSTALL.md (Install, the pin, Verify,
Troubleshooting); KIT\KIT_VERSION.md; the record folding in KIT\checker\repo_hygiene_check.py (_apply_directive and its
caller); KIT\runbooks\RUNBOOK_migrate-an-existing-repository.md where it names release; TARGET\hygiene\
HYGIENE_DECISIONS.md.

Do, in KIT:
(1) KIT_SPEC.md section 6: held-name "must exist while held". Existence is judged after the whole record is folded, only
for holds still active, and a missing file is a record violation on the held-name line still in force. A released hold
needs no file. Section 1.6 gets one matching sentence.
(2) The checker implements (1). Every other record check keeps its current timing and text.
(3) A new fixture tests\held-name-released-by-move: a held-name for an old path, the file moved, then a later entry with
the release and a held-name for the new path. Its expected.txt is the one held line plus the checker's exact
pass-with-holds verdict. Add a negative companion: an active hold whose file is gone, reported as record. Both fixtures
get rows in the CONTRIBUTING.md section 1 table, and the fixture count in the runner's closing line changes to match.
(4) The migrate runbook says that a moved held file takes a release of the old path and a held-name for the new path in
the same entry.
(5) KIT_VERSION.md: current version 0.2.1 (a patch: a record that passes on 0.2.0 still passes). Its changelog entry
names the change, why (the finding, by path), what was verified and the verdict lines. README.md and the rule block's
{{KIT_VERSION}} default agree with it.
(6) Run CONTRIBUTING.md section 1's verification order in full. Every row must report what its table says. Commit in KIT
and tag v0.2.1 on that commit.

Then in TARGET:
(7) Re-pin the superproject to 0.2.1 per INSTALL.md with --force and its current declarations unchanged (roots
repo-hygiene, onboarding, handovers; module root-allowlist; no wrapper, no hook; floor 1). Append a decision entry
D-<today>-nn for the re-pin, citing this finding, with the next free id taken by grep. The rule block in CLAUDE.md and
AGENTS.md changes only inside its markers, and each file keeps its line endings.
(8) The runbook:
  - a note in section 2 on why K-6 exists;
  - K-6 rows in sections 3 and L (done, with the KIT commit, the tag and the re-pin);
  - K-6 added to the section 3 dependency line before M-1;
  - section 15's paste block: the submodule first re-pins itself to 0.2.1 (--force, its declarations unchanged, its own
    decision entry) before its first git mv;
  - section 14 and section 15: a moved held file takes a release plus a held-name at its new path in the same entry;
  - section 17 (M-9) says the same.
(9) handovers\INDEX.md: flip this finding's line from "open" to "resolved by K-6 (kit 0.2.1)". The finding file itself
is not edited.
(10) Verify the superproject per KIT\installer\INSTALL.md. Its verdict must be unchanged in count and in its held lines.
Commit in TARGET.

Constraints: stdlib only; no other rule, directive, verdict line or rule id changes; no absolute path from this machine in
any kit file; LF line endings in the kit; each edited TARGET file keeps its own line endings; no .gitattributes; nothing
under any TARGET submodule, SOURCE (C:\Programmierung\Orchestrator_System) or the onboarding track's files changes;
HYGIENE_DECISIONS.md is appended to, never edited; M-1 itself is not executed; no document names a test invocation
beyond what CONTRIBUTING.md section 1 and INSTALL.md already own; nothing pushed.

Done when: KIT_SPEC.md, the checker and the migrate runbook agree that a released hold needs no file; CONTRIBUTING.md
section 1, run exactly as written, reports what its table says for every row, including both new fixtures; KIT_VERSION.md
reads 0.2.1 and tag v0.2.1 is on the head of KIT main with the tree clean; the superproject's pin reads 0.2.1 with its
re-pin entry, and its verdict is unchanged; the runbook carries K-6 in sections 2, 3 and L and the release-by-move rule in
sections 14, 15 and 17; the finding's index line reads resolved; one KIT commit and one TARGET commit.

Commit line (KIT): kit: K-6 - a hold released by a move needs no file; version 0.2.1; tag v0.2.1
Commit line (TARGET): repo-hygiene: K-6 - superproject re-pinned to kit 0.2.1; runbook resumes M-1; finding resolved
```

**Watch:** send the session back if it:
- proposes dropping the existence check, or making a missing held file pass silently; an active hold must still fail
  loud;
- edits the `-01` entry, which is append-only;
- starts the `M-1` move, which is its own session run afterwards from the runbook §14.
