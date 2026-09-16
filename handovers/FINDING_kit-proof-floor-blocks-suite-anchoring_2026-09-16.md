# FINDING — kit 0.1.0's prompt file floor blocks anchoring the six suites (2026-09-16)

*Raised by the session that opened step `A-2` (PlantLibrary_PyApp) of
`repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md`. Nothing was installed or changed in PyApp; the step
stopped before its first write. Operator's decision, verbatim, to the question that described the blocker: "Stop; kit
patch first (Recommended)".*

## What blocks

- `KIT_SPEC.md` §4 and §7.2: the pin's `Prompt file floor` is "an integer ≥ 1"; the proof-surface scan must reach that
  many `PROMPT_*`/`PROMPTS_*` files directly in roots of kind `planning` or `general`, else `proof-floor`.
- The checker (`checker/repo_hygiene_check.py`, pin parser: `floor < 1` → configuration error) and the installer
  (`--floor` < 1 → `refused — bad flags`) both enforce the minimum. No decision-record directive waives it.
- Steps `A-2`…`A-7` declare `implementation\<Package>\{planning,proposal,handovers}`. `planning\` does not exist in any
  suite today and is seeded empty; `proposal\` is not scanned; `handovers\` is never scanned. So every suite scans
  0 prompt files, and the verdict would be
  `hygiene/CONSUMED_HYGIENE.md: proof-floor — scanned 0 PROMPT_/PROMPTS_ files in planning and general roots; the pin's floor is 1`
  followed by `repo-hygiene: fail — 1 violations, <n> held`. That makes the done-when "zero violations" unreachable.
  `--self-test` also refuses, because it requires the original to pass first.
- The superproject (`A-1`) passed only because its `general` root `repo-hygiene\` already holds a `PROMPTS_` file.

The rule fits SOURCE, where planning holds more than 20 prompts. It does not fit a freshly anchored repository that has
not yet written a prompt: a new repository cannot anchor green without inventing a deliverable.

## Proposed kit change (a K-style step, before `A-2` resumes)

1. Allow `Prompt file floor: 0` as an explicit declaration: `KIT_SPEC.md` §4 and §7.2 ("an integer ≥ 0; 0 only by a
   decision entry"), the checker's pin parser, and the installer's `--floor` validation. The installer default stays 1,
   so a silent zero is still not a pass.
2. `installer/INSTALL.md`: the Verify note and the Troubleshooting row for `proof-floor` name the floor-0 route and say it
   needs a decision entry.
3. `CONTRIBUTING.md` §1: one fixture for a pin with floor 0 and no prompt file, which must print
   `repo-hygiene: pass — 0 violations, 0 held`. Confirm that `--self-test` still plants and detects both proof defects
   when the floor is 0 (it plants its own prompt files).
4. `KIT_VERSION.md`: a minor bump (`0.2.0`, additive: a pin that passes today still passes), with a changelog entry and a tag.

## What the track then owes

- The runbook's §12 paste block and row table say "kit at v0.1.0". They change to the new version, and each suite's
  `D-<date>-01` entry records the floor-0 declaration (the installer is run with `--floor 0`).
- The superproject stays green on 0.1.0. A re-pin (`install.py --target` followed by `--force`, plus a decision entry)
  is optional; it is owed only if the seven repositories should share one kit version before `GA`.
- The separate `A-1` finding (root-level held names are recorded but not shown in the verdict) is unaffected.

## Next action — the continuation prompt (step `K-5`)

**Fable 5.1 · high** (the runbook's §18 ladder: building against a written specification; if Fable is unavailable, use
Opus 5 · high plus the mandatory fresh-context review of §18). One fresh session. `cwd`: KIT, then TARGET for the
runbook and index edits. Paste the block exactly as it stands.

```text
Step K-5 (kit patch: explicit prompt file floor 0) of the repo-hygiene track. TARGET = C:\Programmierung\SW_Development
(superproject branch master), KIT = C:\Programmierung\Repo_Hygiene_Template_Kit (main, tree clean at tag v0.1.0,
commit 1360c0c). cwd KIT. The authority is TARGET\handovers\FINDING_kit-proof-floor-blocks-suite-anchoring_2026-09-16.md,
whose operator decision is quoted there: "Stop; kit patch first (Recommended)". Make a repository without any
PROMPT_/PROMPTS_ file able to anchor green by an explicit, recorded declaration, release the kit as 0.2.0, and update the
track runbook so A-2...A-7 can resume. No submodule of TARGET is touched; nothing is pushed.

Read first: the finding in full; TARGET\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md sections 0, 2, 3,
12, 18 and L; KIT\KIT_SPEC.md sections 4, 6, 7, 9, 11, 14; KIT\CONTRIBUTING.md in full (the verification order and the
"what green means" table are the contract for this step); KIT\installer\INSTALL.md; KIT\KIT_VERSION.md; the floor
handling in KIT\checker\repo_hygiene_check.py (the pin parser and check_proof_surface) and KIT\installer\install.py (the
--floor validation and the pin template fill); KIT\templates\CONSUMED_HYGIENE_TEMPLATE.md; KIT\runbooks\
RUNBOOK_anchor-a-repository.md where it names the floor.

Do, in KIT: (1) KIT_SPEC.md section 4 and section 7.2 - the Prompt file floor is an integer >= 0; 0 is legal only when a
decision entry in hygiene\HYGIENE_DECISIONS.md records it (the entry's words are the justification; the checker does not
parse them); with floor 0 the scan still runs over every PROMPT_/PROMPTS_ file present and still reports proof-argv and
proof-prose; "a silent zero is not a pass" stays true because floor 0 is a pinned declaration, never a default; section
9 - --floor accepts 0, the default stays 1. (2) The checker's pin parser and the installer's --floor validation accept 0
and still reject negative and non-integer values, with the error text updated to ">= 0". (3) installer\INSTALL.md - the
flag table, the Verify note on proof-floor and the Troubleshooting row name the floor-0 route and the decision entry it
needs; templates and the anchor runbook are updated wherever they state the minimum. (4) A new committed fixture under
tests\ for a pin with floor 0 and no prompt file in its planning root, whose expected.txt is
"repo-hygiene: pass - 0 violations, 0 held" in the checker's exact verdict text; the CONTRIBUTING.md section 1 table gains
its row and the fixture count in the runner's closing line changes accordingly; confirm that --self-test over that
fixture still plants and detects both proof defects and passes, and record its verdict line in the table. (5)
KIT_VERSION.md - current version 0.2.0 (minor: additive, a pin that passes on 0.1.0 still passes), a changelog entry
naming the change, why (the finding, by path), what was verified and the verdict lines; README.md and the rule block's
{{KIT_VERSION}} default agree with it. (6) Run CONTRIBUTING.md section 1's verification order in full; every row must
report what its table says. Commit in KIT; tag v0.2.0 on that commit.

Then in TARGET: (7) the runbook - add a K-5 row to section 3 and to section L (done, with the KIT commit and tag); in
section 12 change "v0.1.0"/"0.1.0" to 0.2.0 in the prose and the paste block, and add to the paste block's Do paragraph
that the installer runs with --floor 0 where the suite has no PROMPT_/PROMPTS_ file in a planning root, and that the
D-<today>-01 entry records the floor-0 declaration with this finding cited; state in section 12 that the superproject
stays pinned to 0.1.0 until an operator-decided re-pin (not part of this step); add one sentence to section 1e or a
new dated note in section 2 saying why K-5 exists. (8) handovers\INDEX.md - flip the finding's line from "open" to
"resolved by K-5 (kit 0.2.0)"; the finding file itself is not edited. (9) Verify the superproject per KIT\installer\
INSTALL.md (it must still report its pass-with-holds verdict on its 0.1.0 checker copy); commit in TARGET.

Constraints: stdlib only; no other rule, directive, verdict line or rule id changes; no absolute path from this machine in
any kit file; LF line endings in the kit; each edited TARGET file keeps its own line endings; no .gitattributes; nothing
under any TARGET submodule, SOURCE (C:\Programmierung\Orchestrator_System) or the onboarding track's files changes; the
superproject's scripts\hygiene\ copy and pin are not re-synced in this step; no document names a test invocation beyond
what CONTRIBUTING.md section 1 and INSTALL.md already own; nothing pushed.

Done when: KIT_SPEC.md, the checker, the installer, INSTALL.md, the templates and the anchor runbook all state the floor as
>= 0 with 0 only by decision entry; CONTRIBUTING.md section 1, run exactly as written, reports what its table says for
every row, including the new floor-0 fixture and its self-test line; KIT_VERSION.md reads 0.2.0 and tag v0.2.0 is on the
head of KIT main with the tree clean; the runbook carries K-5 in sections 3 and L and section 12 names 0.2.0 and the
floor-0 route; the finding's index line reads resolved; the superproject's verdict is unchanged; one KIT commit, one
TARGET commit.

Commit line (KIT): kit: K-5 - prompt file floor 0 by decision entry; version 0.2.0; tag v0.2.0
Commit line (TARGET): repo-hygiene: K-5 - runbook resumes A-2...A-7 on kit 0.2.0; finding resolved
```

**Watch:** if the session proposes having the checker skip `proof-floor` automatically when no prompt file exists, send
it back; the zero must be declared. If it proposes installing into PyApp, stop it; `A-2` is its own session, run
afterwards from the updated runbook §12.
