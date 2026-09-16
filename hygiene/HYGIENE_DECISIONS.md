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
