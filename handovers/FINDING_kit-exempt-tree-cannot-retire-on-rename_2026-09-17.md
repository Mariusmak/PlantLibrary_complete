# FINDING — an exempt path that moves cannot be retired from the record (kit 0.2.1) (2026-09-17)

Written for: the operator of this repository and the session that patches the Repo Hygiene Template Kit.

## What happened

Step `M-7` of `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` (§15) renamed the Workspace set folder
`docs/proposals/Repo_Restructure_MVP_V1_Split/` to `docs/proposals/PROPOSAL_repo-restructure-mvp-v1-split_2026-07-15/`
by `git mv`, as `G0` Q5b and the confirmed map (`repo-hygiene/MATRIX_rename-map_2026-09-16.md` §9c, proposal 5) require.
The checker's verdict afterwards:

```text
hygiene/HYGIENE_DECISIONS.md:161: record — exempt-tree docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/REVIEW_LIST.md does not exist
repo-hygiene: fail — 1 violations, 10 held
```

Line 161 is the anchoring entry `D-2026-09-16-01`'s `exempt-tree` directive for the generated `REVIEW_LIST.md` inside
that set, written by path as `KIT_SPEC.md` §6 requires. Every other part of the step was green: the three `fable5_*` set
folders, the seven file renames, the sweep and the ten indexes all passed, and the ten `held:` lines are the expected
ones.

## Why

`_apply_directive` in `checker/repo_hygiene_check.py` (kit `0.2.1`; installed in every suite as
`scripts/hygiene/repo_hygiene_check.py`) checks `exempt-tree` and `exempt-subfolder` existence at the moment it folds
the line. The vocabulary of `KIT_SPEC.md` §6 ends a `held-name` by a later `release` (the `K-6` change), but nothing ends
an `exempt-tree` or `exempt-subfolder`. The record is append-only, so the earlier line can never be edited away. The
result is that **any exempt path that a later `git mv` moves or renames fails `record` for ever** — the same shape `K-6`
fixed for `held-name`. No fixture under `tests/` exercises an exempt path that moves, so `K-3`, `K-5` and `K-6` could not
see it.

A second, smaller gap surfaced when the hold was recorded: `held-name` requires the held path to be a file
(`is_file()`), so a set folder held as a whole — the shape `G0` Q5b creates whenever a numbered set waits on a citer —
cannot take a `held-name` line and is invisible to the checker's `held` count and the census.

## Who else it blocks

- `M-9` for this set: the release needs the kit change first.
- Any future move of an exempt tree or subfolder in any anchored repository: PyApp's `Documentation/` legacy corpus if
  its exemption is ever lifted into a move, SharedContracts' `generated/`, every frozen `implementation/MVP/` tree if
  archived, and every generated file declared by path.
- Every set folder that waits held on a citer: `MVP_Reconciliation/` (Workspace, proposal 4), the two `proposal/`
  sets (proposal 3) — none of them can be a `held-name` today; their holds are carried in prose and in the mapping
  tables only.

## Decision taken at `M-7`

The step did not stop. The set folder's rename was reverted by `git mv` back to its current name, the two members the
sweep had touched were restored byte for byte, and the set is **held** in Workspace's `D-2026-09-17-03` — cited by the
record's own line 161, a machine-read directive in a file that is never edited — with the map's set folder as its target
on release. Everything else the map names for Workspace was executed, and the verdict is
`repo-hygiene: pass with holds — 0 violations, 10 held`. The deviation is stated in the runbook's `M-7` ledger rows, in
`docs/proposals/INDEX.md` (its line and its "Renamed 2026-09-17" row) and in the `M-7` commit message.

Why proceed rather than stop, as `K-5` and `K-6` did: those blockers made whole steps unreachable; this one affects one
of eleven renames, the hold is explicit and reversible by one `git mv`, and stopping would have left `M-7` uncommitted
with ten green dispositions reverted. The operator may still choose otherwise below.

## Proposed fix (for the kit session to decide)

1. `KIT_SPEC.md` §1.5, §1.7 and §6: an `exempt-tree` or `exempt-subfolder` path must exist *while declared*; a later
   `release` of that path ends the declaration in the commit of the `git mv`; existence is judged after the whole record
   is folded, only for declarations still active, and reported on the line still in force. A released declaration needs
   no path. Where the moved tree still needs its class (a generated file, a legacy corpus), the same entry declares the
   new path.
2. `held-name` accepts a directory: a set folder held as a whole. Existence by `exists()`; the checker's `held:` line
   and the census's `held` count include it when it is a direct child of a root; its members stay exempt at every depth.
3. Fixtures: `tests/exempt-tree-released-by-move` (an `exempt-tree` for an old path, the tree moved into a dated set
   folder, a later entry with the `release` and the new declaration) expecting `pass`; `tests/exempt-tree-missing` (an
   active declaration whose path is gone) expecting `record`; `tests/held-set-folder` (a `held-name` on a folder that is
   a direct child of a root) expecting `pass with holds — 0 violations, 1 held`. Rows in `CONTRIBUTING.md` §1's table;
   the fixture count in the runner's closing line changes to match.
4. The migrate runbook (`M-<N>`, `M-R`) says that a moved exempt path takes a `release` plus, where still needed, a new
   declaration in the same entry.
5. `KIT_VERSION.md`: `0.2.2` if the kit session reads it as `K-6` read its change (a record that passes on `0.2.1` still
   passes) — or `0.3.0` if it reads the two vocabulary extensions as additive. Then a tag, and the suites re-pin at their
   `M-9` batches as `M-2`…`M-7` re-pinned at their `M-n`.

## Options for the operator

1. **Kit patch `K-7` per the proposed fix, then `M-9` releases the Workspace set (Recommended).** `M-8` runs on the
   current state either way; its handover lists this hold with the others.
2. Accept the hold until some later kit release; `M-8` proceeds; the set stays under its old name.
3. Reverse the `M-7` call: require the rename now. That needs the kit patch first in any case, since no record on
   `0.2.1` can pass with the tree moved.

## State at the stop

`M-7` is committed on Workspace `main` (the hash is in the runbook's §L row) and the superproject carries the gitlink
bump with the ledger flip. Workspace's verdict is `repo-hygiene: pass with holds — 0 violations, 10 held`; its census
counts 30 files, 7 compliant, 0 candidates, 12 exempt, 10 held, 3 set folders (the map anticipated 4). The five suites'
`implementation/README.md` files cite the set's current path for their `MANIFEST_<suite>.csv`; they need a one-line path
fix each when the set is released (Workspace `D-2026-09-17-03`, item 8). Nothing is pushed.

## Next action — the continuation prompt (step `K-7`)

**Fable 5.1 · high** (runbook §18: building against a written specification; if Fable is unavailable, Opus 5 · high plus
the mandatory fresh-context review). One fresh session. `cwd`: KIT first, then TARGET for the runbook edits and this
finding's index line. Paste the block exactly as it stands.

```text
Step K-7 (kit patch: an exempt path that moves) of the repo-hygiene track. TARGET = C:\Programmierung\SW_Development
(superproject branch master), KIT = C:\Programmierung\Repo_Hygiene_Template_Kit (main, tree clean at tag v0.2.1,
commit 810733e). cwd KIT. The authority is TARGET\handovers\FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md
and the operator's answer recorded there. Goal: an exempt-tree or exempt-subfolder whose path later moves or is renamed
must be releasable in the commit of the git mv; a set folder held as a whole must be declarable as a held-name; release
the kit; update the track runbook so M-9 can release the Workspace set. No submodule of TARGET is touched by this step;
the suites re-pin at their own M-9 batches. Nothing is pushed.

Read first: the finding in full; TARGET\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md sections 2, 3, 17,
18 and L; KIT\KIT_SPEC.md sections 1.5, 1.6, 1.7, 1.8, 6, 7, 11; KIT\CONTRIBUTING.md in full; KIT\installer\INSTALL.md
(Verify); KIT\KIT_VERSION.md; the record folding in KIT\checker\repo_hygiene_check.py (_apply_directive, load_record and
the census's held and exempt listing); KIT\runbooks\RUNBOOK_migrate-an-existing-repository.md where it names release;
TARGET\PlantLibrary_Workspace\hygiene\HYGIENE_DECISIONS.md entries D-2026-09-16-01 (line 161) and D-2026-09-17-03.

Do, in KIT:
(1) KIT_SPEC.md sections 1.5, 1.7 and 6: an exempt-tree or exempt-subfolder path must exist while declared; a later
release of that path ends the declaration; existence is judged after the whole record is folded, only for declarations
still active, on the line in force; a released declaration needs no path. Section 1.6 and 1.8: a held-name may name a
set folder held as a whole.
(2) The checker implements (1). Every other record check keeps its current timing and text.
(3) The three fixtures the finding proposes, each with its expected.txt; rows in CONTRIBUTING.md section 1's table; the
runner's closing count changes to match.
(4) The migrate runbook's M-<N> item and M-R say that a moved exempt path takes a release plus, where still needed, a new
declaration in the same entry, and that a held set folder is a held-name.
(5) KIT_VERSION.md: the version per the semver rule, with a changelog entry naming the change, why (this finding, by
path), what was verified and the verdict lines; README.md and the rule block's version default agree with it.
(6) Run CONTRIBUTING.md section 1's verification order in full. Every row must report what its table says. Commit in KIT
and tag on that commit.

Then in TARGET:
(7) The runbook: a note in section 2 on why K-7 exists; K-7 rows in sections 3 and L (done, with the KIT commit and the
tag); K-7 in the section 3 dependency line before M-8; section 17 (M-9) says that a release batch re-pins its repository
to the new kit first and that an exempt path released by a move takes the release line; the M-7 rows point at this
finding as resolved.
(8) handovers\INDEX.md: flip this finding's line from "open" to "resolved by K-7 (kit <version>)". The finding file itself
is not edited.
(9) Verify the superproject per KIT\installer\INSTALL.md; its verdict must be unchanged. Commit in TARGET.

Constraints: stdlib only; no other rule, directive, verdict line or rule id changes; no absolute path from this machine in
any kit file; LF line endings in the kit; each edited TARGET file keeps its own line endings; no .gitattributes; nothing
under any TARGET submodule, SOURCE (C:\Programmierung\Orchestrator_System) or the onboarding track's files changes; no
record is edited retroactively; M-9 itself is not executed; no document names a test invocation beyond what
CONTRIBUTING.md section 1 and INSTALL.md already own; nothing pushed.

Done when: KIT_SPEC.md, the checker and the migrate runbook agree that a released exempt declaration needs no path and
that a set folder can be held; CONTRIBUTING.md section 1, run exactly as written, reports what its table says for every
row including the three new fixtures; KIT_VERSION.md and the tag agree on the version with the tree clean; the runbook
carries K-7 in sections 2, 3, 17 and L; the finding's index line reads resolved; one KIT commit and one TARGET commit.

Commit line (KIT): kit: K-7 - a released exempt path needs no file; a set folder can be held; version <version>; tag
Commit line (TARGET): repo-hygiene: K-7 - runbook carries K-7; M-9 may release the Workspace set; finding resolved
```

**Watch:** send the session back if it proposes dropping the existence check for exempt paths (an active declaration
must still fail loud), edits any earlier entry, or starts the Workspace `git mv` — that is `M-9`'s own session.
