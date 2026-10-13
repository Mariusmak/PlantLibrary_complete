# Corpus census — superproject — lane A6 (read-only analysis, 2026-10-13)

Lane A6-super of the PlantLibrary master rework program, Phase A. Subject: `C:\Programmierung\SW_Development` itself on `master` @ `8702e0a`, its own tracked files only (the six `PlantLibrary_*` submodule folders are other lanes'), plus the git-ignored `Todo.md`. Nothing was edited except this file; no test, build or install was run; the only commands that ran were git reads, `grep`, and the hygiene checker's `check` and `census` modes. This file has no `INDEX.md` line yet (the orchestrator adds it in the commit).

## 0. Summary

- Corpus: 68 tracked `.md` files (`git ls-files -- '*.md'` minus submodules) plus the git-ignored `Todo.md` (280 lines, 0 markdown headings, 67 blank-separated blocks) and 24 root entries.
- Class: 38 live (16 own files + 22 `.claude` skill/agent files), 19 generated-mirror (`.codex/skills`), 2 pinned/append-only (`hygiene/`), 2 superseded (`IMPLEMENTATION_PLAN.md`, the schema-drift HANDOVER), 7 archive-candidates (spent track records, evidence and resolved findings).
- Disposition: keep 59 (one of them, `.agents/README.md`, needs a rewrite: it is the Conductor repository's bridge README, not this repository's); hold 3 (the onboarding-runbook group); archive after a gate 6 (`IMPLEMENTATION_PLAN.md` after B4 and Q-G-05; five repo-hygiene track files after M-8/M-9); retire 0.
- Holds: 3 active `held-name` lines, all citing `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md`; the runbook is live (steps 6, 7, 8, 9 open), so none of the three ends in Phase B unless the operator records a release (Q-A6S-02). `IMPLEMENTATION_PLAN.md`'s exemption is an inert `exempt-name`. The superproject record has no `exempt-tree`, no `exempt-subfolder`, no `retired-name`.
- Stale sequencers: `IMPLEMENTATION_PLAN.md` still carries live content nobody else holds (five open `SDA-DEC-*` decisions, two security sign-offs, six unhomed backlog items); harvest it before archiving. `Todo.md` was edited today (17:29) and is protected by a 2026-07-15 operator decision (P3 "keep untouched"), so Q-G-05 (a)'s "emptied" needs an explicit word (Q-A6S-04).
- Graphify: dropped in `7946483`/`53051b0` (hooks, instruction blocks), but `update_graph.bat` (tracked), `graphify-out/` (275 MB, ignored) and their two allowlist lines remain; the allowlist entries are not dead until the two files are gone (removing them first would fail the `allowlist` rule).
- Archive recommendation: a top-level `archive/`, allowlisted and declared `exempt-tree: archive — legacy`, top-level path only and never renamed (the K-7 limit), not a deliverable root; undeclared per-root `archive/` subfolders are the zero-K-7 alternative. Q-G-06 evidence: the superproject needs no K-7 workaround; recommend (a).
- Checker: `repo-hygiene: pass with holds — 0 violations, 3 held`; census 21 files in 4 roots, 14 compliant, 0 candidates, 4 exempt (the four `INDEX.md`), 3 held, 0 set folders.

## 1. Coverage

| Item | Status (read / partly read / not read) | Reason |
|---|---|---|
| Kickoff prompt §1, §2, §4 | read | `rework/PROMPT_master-rework-kickoff_2026-10-13.md:1-77` |
| `CLAUDE.md` (hygiene rule block) | read | `CLAUDE.md:19-33`; byte-identical to `AGENTS.md` (`cmp`) |
| `hygiene/CONSUMED_HYGIENE.md`, `hygiene/HYGIENE_DECISIONS.md` | read | every entry (`D-2026-09-16-01/-02/-03`, `D-2026-10-13-01`) |
| K-7 finding | read | `handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md:1-156` |
| Kit `KIT_SPEC.md`, `KIT_VERSION.md`, migrate runbook | partly read | `KIT_SPEC.md` §1.4-1.9, §6, §7, §10, §12 and runbook sections 1, 8, 9 read; derive and anchor runbooks only searched for archive/legacy wording (no kit runbook has an archive procedure; the only wording is `KIT_SPEC.md:88-91`, "archive and hide, never delete") |
| Checker `scripts/hygiene/repo_hygiene_check.py` | partly read | directive folding (`:426-490`), scan (`:555-610`), allowlist (`:748-753`), census exempt-tree table (`:881-893`) |
| `IMPLEMENTATION_PLAN.md` | partly read | header, headings, §5-§8 (`:271-394`) read; §1-§4 (status, waves) only headings checked |
| `Todo.md` | partly read | block starts, about 12 blocks sampled for liveness; content not copied |
| `handovers/*.md` (5) | partly read | K-7 finding in full; schema-drift HANDOVER head; the two resolved FINDINGs via `INDEX.md` and citer lines only |
| `onboarding/*.md` (4) | partly read | runbook headings, ledger §L, §N, citer lines; `AUDIT` and `REGISTER` heads only |
| `repo-hygiene/*.md` (6) | partly read | `INDEX.md` in full, runbook ledger rows `:955-987`; census, map, inventory, bootstrap prompt not read beyond citer lines |
| `rework/*.md` (6) | partly read | kickoff in full; runbook skeleton checked for Q-G-05, Q-G-06 and B3 rows only |
| `.claude/**` and `.codex/**` markdown (41 files) | not read | lane A1 owns them; counted and classified by tree only |
| `.agents/README.md` | read | `:1-86` |
| Citers inside the superproject | read | `git grep -n -F <basename>` for each of the 27 non-skill files |
| Citers inside submodules | partly read | `git -C <suite> grep` for `IMPLEMENTATION_PLAN.md`, the HANDOVER, the onboarding runbook, `AUDIT`, `REGISTER_package-census`, the K-7 finding, `Todo.md`, `graphify`, the track runbook and the map; hits for the basename `IMPLEMENTATION_PLAN.md` mostly name the suites' own same-named MVP package files and were filtered by reading |
| Non-markdown root entries | read | listing, `update_graph.bat`, `graphify-out/` listing, `.agents`, `scripts/`, `.codex/hooks.json`, `.claude/settings.json`, head of `.github/workflows/repo-hygiene.yml` |

## 2. Findings

- **F-A6S-01 — `IMPLEMENTATION_PLAN.md` is stale as a sequencer but holds three bodies of live content no other file owns.** (a) §5.1 `SDA-DEC-01..05` (`IMPLEMENTATION_PLAN.md:276-292`) are still `open` in the Workspace package (`PlantLibrary_Workspace/implementation/System_Design_Architecture/STATE.md:21-25`); STATE.md is the record, the plan is the only place that says "nothing waits on them". (b) §5.2 names two release-blocking security sign-offs (`:294-304`) and §5.3 a release-scope confirmation (`:306-314`). (c) §7 lists six items "with no batch row" (`:358-376`); the Android cleartext/HTTPS item is still unhomed: no hit for `cleartext` in `PlantLibrary_AndroidApp/implementation/System_V1_Implementation` (the only hits are the frozen MVP evidence and `Server_VM_Setup`). §6's environment gotchas (`:316-356`) also live nowhere else in one place. Archive only after B4's hand-back section and a REGISTER absorb §5-§7.
- **F-A6S-02 — `Todo.md` is protected and in active use.** Mtime 2026-10-13 17:29; its last three blocks (lines 261-280) are the master-rework prompt. The 2026-07-15 operator decision "P3: keep at outer root untouched (active personal scratchpad with live reminders)" is recorded at `PlantLibrary_Workspace/docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_complete.csv:4` and `.../manifests/REVIEW_LIST.md:40`. Frozen Workspace records cite it by line range (`methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md:136` "Todo.md lines 236–244"; `KICKOFF_PROMPT.md:182`), so emptying it would orphan those citations. Q-G-05 (a) ("the file emptied") therefore reverses P3 and needs the operator's explicit word (Q-A6S-04).
- **F-A6S-03 — `Todo.md` structure.** 0 headings (free prose), 67 blank-separated blocks. My estimate (not the operator's) of ideas still live, by start line: 34 (build artefacts under SharedContracts excluded from git), 76 (clean old folders; `IMPLEMENTATION_PLAN.md:373-376` already says keep MVP read-only, so probably resolved), 91 (server-side data enrichment), 94 (prioritised value audit), 123 (no cleartext HTTP on Android, plan HTTPS), 195 (security-assessment proposal before release), 201 (backup-creation batches for `C:\Backups`). Lines 1-50 and 98-193 read as done or superseded (MVP closed, V1 packages exist, skills authored); lines 235-280 are the rework origin notes. About 6-7 live, 3 ambiguous (lines 80, 114, 119), the rest done.
- **F-A6S-04 — `.agents/README.md` describes the Conductor repository, not this one.** `:3` and `:26-29` point at `../.Claude/skills` (wrong case and folder); `:10` names "Harness_V1 batch"; `:36` and `:57` list `v5-section-reader` (this repository has three agents: `batch-closeout-reviewer`, `batch-plan-auditor`, `real-stack-validator`); `:52-55` calls `C:\Programmierung\SW_Development` the "PlantLibrary" copy of another repository; `:62-68` says six skills (`design-adoption`, `gui-validation`, `sync-contracts`, `verify-stack`, `webapp-testing`, `ui-ux-pro-max`) were relocated out of `.claude/skills/` and `.codex/skills/`, yet all six are tracked there today (`git ls-files .claude/skills`). `:77-85` says graphify hooks were removed on 2026-08-19 and `graphify-out/` moved off-repo; the hook removal actually happened on 2026-10-02 (`7946483`, `53051b0`) and `graphify-out/` sits at the root. The file is cited by `CLAUDE.md:23`, `AGENTS.md:23`, `.claude/skills/plan-batch/SKILL.md:174`, `scripts/hygiene/repo_hygiene_check.py:53`. Disposition: rewrite in A1/B1 together with the Codex freeze (Q-G-09), not archive.
- **F-A6S-05 — the three onboarding-runbook holds cannot end by an edit.** Kit rule: "a name whose citer still cites it stays held — no edit to a state file, an anchor, another track's runbook ... to force a release" (`Repo_Hygiene_Template_Kit/runbooks/RUNBOOK_migrate-an-existing-repository.md:307-309`); a hold whose citer is a live runbook is "released when that runbook retires" (`:54`); a hold whose citer is a frozen state file is released "only by a decision that the mapping table serves such citations" (`:51-52`). The onboarding runbook's steps `6`, `7`, `8`, `9` are `todo`/held (`onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:910-916`), and the runbook is itself cited from every suite (below), so it retires only after the Conductor program. Citers of the runbook: `scripts/harness/migrate_checklist_schema.py:3`, `handovers/INDEX.md:20`, the suites' `implementation/System_V1_Implementation/STATE.md` (Server `:207`, SharedContracts `:89`, Dashboard `:112`, AndroidApp `:182`, Workspace `:217`), `PlantLibrary_Workspace/implementation/System_Design_Architecture/STATE.md:79`, `PlantLibrary_PyApp/implementation/System_V1_Implementation/validation/ONBOARDING_harness-port.md:3`.
- **F-A6S-06 — `AUDIT_skill-assumptions_2026-09-15.md` has a second, code-class citer the record does not mention.** `PlantLibrary_PyApp/scripts/harness/scope_cap.py:5`, `.../regression_scope.py:33` and `.../validation/ONBOARDING_harness-port.md:4` cite it by basename. Kit principle: a file that code cites does not move (`KIT_SPEC.md:89-90`, A.0.5). The hold record (`hygiene/HYGIENE_DECISIONS.md:85`) names only the runbook; if the runbook retires, the AUDIT still should not move. The HANDOVER and `REGISTER_package-census` have no submodule citer (`git -C <suite> grep -l` over all six suites returned nothing).
- **F-A6S-07 — `exempt-name: IMPLEMENTATION_PLAN.md` is inert.** The file sits at the repository root, outside every declared root, and the checker scans only roots (`scripts/hygiene/repo_hygiene_check.py:588-610`); the entry itself says so (`hygiene/HYGIENE_DECISIONS.md:185-186`). A basename `exempt-name` has no existence check (`:432-436`), so archiving the file creates no K-7 problem; only the allowlist line wants an `allowlist-remove` for tidiness (a stale allowlist line is not a violation: the check is `entries - allowlist`, `:748-751`).
- **F-A6S-08 — K-7 does not touch the superproject today.** The superproject's record contains no `exempt-tree` and no `exempt-subfolder` (`hygiene/HYGIENE_DECISIONS.md:49-233`; the census prints no "Exempt trees" table). The existence checks that cause K-7 are at `scripts/hygiene/repo_hygiene_check.py:442-445` (subfolder) and `:446-452` (tree), judged when the line folds, with no directive that ends them. The live casualty is Workspace's set folder, held under Workspace `D-2026-09-17-03` and carried by the record line the finding cites (`handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md:17-18`). The kit is still `0.2.1` at `810733e`, with no K-7 commit or branch (`git log` in the kit).
- **F-A6S-09 — graphify remains, and the allowlist lines are live until the files go.** What remains: `update_graph.bat` (tracked, still calls `graphify update .`, `update_graph.bat:8`), `graphify-out/` (275 MB; `graph.json` 57 MB, `GRAPH_REPORT.md` 0.5 MB; newest write 2026-09-17 in `cache/`), `.gitignore:11-12`, allowlist lines `hygiene/HYGIENE_DECISIONS.md:111,117`, narrative at `.agents/README.md:77-85`, mentions in `onboarding/` and `repo-hygiene/` records. Gone: the hook entries (`7946483`: `.codex/hooks.json`, `CLAUDE.md`, `AGENTS.md`; `53051b0`: `.claude/settings.json`, now `{}`), and nothing under `.claude/` or `.codex/` mentions graphify (`git grep -i graphify -- .claude .codex` is empty). The `graphify` CLI is still installed on this machine (`.../Python312/Scripts/graphify`), so the `.bat` still runs. An `allowlist-remove` while either entry is present on disk fails the `allowlist` rule (`:748-751`).
- **F-A6S-10 — `scripts/harness/migrate_checklist_schema.py` is a spent one-shot.** Written for onboarding steps `2a`/`2b` (docstring `:1-4` cites the runbook Appendix B); all seven packages are migrated (kickoff §1). Keep while the onboarding runbook is live; A2/B7 decides its final home. Not markdown; listed for completeness.
- **F-A6S-11 — resolved findings are cited by the append-only record.** `FINDING_kit-release-after-move-fails-record_2026-09-16.md` is cited by path at `hygiene/HYGIENE_DECISIONS.md:132,165`; `FINDING_kit-proof-floor-blocks-suite-anchoring_2026-09-16.md` by the track runbook (`:158,568,967`). A move leaves those path citations dangling in a record that is never edited; the kit's remedy is the root's "Renamed" table. Both sit in the correct root (`handovers/`) and cost nothing, so the recommendation is keep.
- **F-A6S-12 — archive moves lose proof-surface and name coverage by design.** The checker's `proof-argv`/`proof-prose` scan reads `PROMPT`/`PROMPTS` files inside declared roots only; spent prompts moved to `archive/` leave the scan. Relative links inside `IMPLEMENTATION_PLAN.md` (`[Todo.md](Todo.md)`, `PlantLibrary_Workspace/...`) break on a move; archived files are frozen and are not swept.

## 3. Candidates

| RC id | Source path @ pin | What | Verdict | Target repo and path | Lane (B3) | Q id |
|---|---|---|---|---|---|---|
| RC-A6S-01 | `Repo_Hygiene_Template_Kit/KIT_SPEC.md:76-80` (§1.7) and `:88-91` (§1.9) @ `810733e` (0.2.1) | `exempt-tree` class `legacy` for an exempt legacy corpus; "archive and hide, never delete" | adopt (declare `archive` as one tree, top level only) | superproject `hygiene/HYGIENE_DECISIONS.md` (new D-entry) | B3 | Q-A6S-01 |
| RC-A6S-02 | `Repo_Hygiene_Template_Kit/runbooks/RUNBOOK_migrate-an-existing-repository.md:284-322` (§9 step `M-R`) @ `810733e` | the release-batch procedure, its "no edit to force a release" constraint and the Watch paragraph | adopt as B3's rule for the three holds | B3 runbook step text | B3 | Q-A6S-02 |
| RC-A6S-03 | `.../runbooks/RUNBOOK_migrate-an-existing-repository.md:48-55` @ `810733e` | the hold-class table (live package, frozen state file, pinned, code, live runbook) and what releases each | adopt as the classification column of §7.2 | B3 | B3 | — |
| RC-A6S-04 | `.../templates/AUDIT_migration-record_TEMPLATE.md` and `.../runbooks/RUNBOOK_migrate-an-existing-repository.md:252-262` (step `M-C`) @ `810733e` | the `M-8` closing-pass record (disposition table, counts reconciled, holds outstanding) | adopt for `M-8` | superproject `repo-hygiene/` or `rework/` | B3 | — |
| RC-A6S-05 | `handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md:59-77` @ `8702e0a` | the K-7 proposed fix (release for exempt paths, directory `held-name`, three fixtures, runbook wording, version) as the Kit-session brief | queue for a separate Kit session; never patch the kit from this program | `Repo_Hygiene_Template_Kit` (operator session) | B3 | Q-G-06 |
| RC-A6S-06 | `retired-name` directive, `KIT_SPEC.md:218,324` @ `810733e` | "a recreation must fail loud" for `IMPLEMENTATION_PLAN.md`, `graphify-out`, `update_graph.bat` after they leave the root | adopt | superproject `hygiene/HYGIENE_DECISIONS.md` | B3 | Q-A6S-03 |

## 4. Questions for the operator

| Q id | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A6S-01 | Where do archived superproject files go? | (a) one top-level `archive/` (allowlisted, `exempt-tree ... legacy`, top-level path only, never renamed; subfolders `archive/root/`, `archive/handovers/`, `archive/onboarding/`, `archive/repo-hygiene/`); (b) an undeclared `archive/` subfolder inside each root (no declaration, no allowlist line); (c) archive nothing, keep in place under holds | One place, uniform with the other six repositories, census shows it as `legacy`, and declaring only the top path keeps K-7 exposure at zero | `B3` archive step; execution of `Q-G-05` |
| Q-A6S-02 | The three onboarding-runbook holds (`HANDOVER_batch-package-schema-drift`, `AUDIT_skill-assumptions`, `REGISTER_package-census`): release now or at runbook retirement? | (a) leave them held until the onboarding runbook retires; `B8` records in the runbook ledger that this is the retirement gate; (b) the operator records a release in words and `B3` writes the `release` lines (files stay where they are, since each target on release is its own name) so the verdict drops to `pass`; (c) edit the runbook's citing lines | (a) costs nothing (the names are already compliant); (b) is legal (`RUNBOOK_migrate-an-existing-repository.md:51-52`) but leaves live-runbook basename citations pointing at files that may later move; (c) is forbidden by the kit constraint | `B3` hold-release substep, `B8` |
| Q-A6S-03 | Graphify leftovers: retire them? | (a) `git mv update_graph.bat archive/root/` (never delete), the operator removes or moves `graphify-out/` off-repo himself, then one D-entry with `allowlist-remove` for both and `retired-name` for both; (b) keep both and their allowlist lines; (c) delete outright | (a) finishes the drop answered as `D5` on 2026-10-02 and makes a re-run of `graphify update .` fail loud instead of silently regrowing 275 MB at the root | `B3`; `B2` (the `.agents/README.md` rewrite mentions it) |
| Q-A6S-04 | Q-G-05 (a) says `Todo.md` is "emptied". It was edited today and the 2026-07-15 decision P3 says keep it untouched. | (a) copy the live ideas (estimate 6-7, F-A6S-03) into a new REGISTER under `rework/` and leave `Todo.md` untouched; the operator empties it by hand when he wants; (b) do as Q-G-05 (a) says and empty it | (a) honours P3 and the line-range citations in frozen Workspace records (F-A6S-02), and `Todo.md` is git-ignored so nothing is at risk either way | `B3`/`B4` Todo harvest |
| Q-A6S-05 | When do the spent hygiene-track files leave `repo-hygiene/`? | (a) after `M-8` (closing pass) for `PROMPT_kit-bootstrap-session`, `REGISTER_hygiene-harness-inventory`, `REGISTER_target-corpus-census`; after `M-9` for `MATRIX_rename-map` and the track runbook; each with a "Renamed" row in `repo-hygiene/INDEX.md`; (b) leave the whole folder in place as history | `M-8` diffs against the corpus census and `M-9` reads the map's targets; archiving earlier removes the baselines their steps name | `B3` archive substep |

## 5. Reusable things this brief did not name

- `hygiene/HYGIENE_DECISIONS.md` has no entry that ever records a `retired-name`; the directive exists in the checker (`scripts/hygiene/repo_hygiene_check.py:487-488`) and is the right tool for sequencers that must not return (RC-A6S-06).
- The `census` mode already prints an "Exempt trees" table by class (`:881-893`); a declared `archive` tree would appear there with every archived `.md`, which gives `M-8` a free before/after count.
- `scripts/harness/check_harness_parity.py:5` names `CLAUDE.md` and `AGENTS.md` and the shared-block end markers; when B2 rewrites the instruction files and Codex is frozen (Q-G-09), the parity checker and the `.agents/README.md` rewrite change together.
- `.github/workflows/repo-hygiene.yml:8-13` runs `check` on every push and pull request; it will start failing on any archive move that forgets the allowlist line.
- `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:918-934` (§N, six notes owed) is a ready list for B8; item `GC-2437` (PyApp `.gitignore` dead lines) names a cleanup no row owns.

## 6. Claims to verify

1. The three holds cite only the onboarding runbook, and the verdict is `pass with holds`: from `C:\Programmierung\SW_Development`, `python scripts/hygiene/repo_hygiene_check.py check` must print exactly three `held:` lines each ending in `cited by onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:...` and the last line `repo-hygiene: pass with holds — 0 violations, 3 held`; then `git grep -n -F -e HANDOVER_batch-package-schema-drift -e REGISTER_package-census -- onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` must show lines 5, 251, 584, 911.
2. The graphify residue is exactly four places outside the track records and nothing under the skill trees: `git grep -il graphify -- . ':!PlantLibrary_*' ':!rework' ':!repo-hygiene' ':!onboarding' ':!.claude' ':!.codex'` must list only `.agents/README.md`, `.gitignore`, `hygiene/HYGIENE_DECISIONS.md`, `update_graph.bat`; and `git grep -i graphify -- .claude .codex` must be empty.
3. The Android cleartext item of `IMPLEMENTATION_PLAN.md` §7 is still unhomed in the V1 packages and the `SDA-DEC` items are still open: `git -C PlantLibrary_AndroidApp grep -n -i cleartext -- implementation/System_V1_Implementation` must print nothing, and `git -C PlantLibrary_Workspace grep -n "SDA-DEC-0[1-5] .*open" -- implementation/System_Design_Architecture/STATE.md` must print five table rows (lines 21-25).

## 7. Deliverables

### 7.1 Disposition table

Class key: live; superseded; archive (historical, spent, a candidate); pinned/append-only; generated-mirror. "Hold / exemption" names the D-id and what releases it. Citers are `path:line` from `git grep -n -F <basename>`; long lists are abbreviated to the principal citers. `INDEX.md` lines of the same root are not counted as citers.

**Tracked `.md`, outside the skill trees (27 files)**

| File | Class | Citers (path:line, or none) | Hold / exemption (D-id) and what releases it | Disposition | Reason |
|---|---|---|---|---|---|
| `CLAUDE.md` | live | `scripts/hygiene/repo_hygiene_check.py:54,725`; `scripts/harness/check_harness_parity.py:5`; `.agents/README.md:11,14`; `hygiene/HYGIENE_DECISIONS.md:63,101,121,188`; six suites mirror the shared block | allowlist `D-2026-09-16-01` (`:101`); nothing to release | keep | Instruction file carrying the rule block; B2 rewrites from A3's blueprint |
| `AGENTS.md` | live | as `CLAUDE.md`, plus `IMPLEMENTATION_PLAN.md:203-204` | allowlist `:100`; Codex freeze is Q-G-09 | keep | Byte-identical to `CLAUDE.md`; frozen, not deleted, if Q-G-09 (a) |
| `.agents/README.md` | live (stale content) | `CLAUDE.md:23`; `AGENTS.md:23`; `.claude/skills/plan-batch/SKILL.md:174`; `.codex/skills/plan-batch/SKILL.md:174`; `scripts/hygiene/repo_hygiene_check.py:53` | allowlist `.agents` (`:94`) | keep (rewrite in A1/B1) | F-A6S-04: describes the Conductor repository; contradicts the tracked skill list and the graphify timeline |
| `IMPLEMENTATION_PLAN.md` | superseded (partly live) | `hygiene/HYGIENE_DECISIONS.md:78,84,103,171,183,194,195,228`; onboarding runbook `:17,52,210,213,217,221,685,820,845,898`; `repo-hygiene/INDEX.md:28`; track runbook `:74,184,235,535,555,730,777,788`; `rework/PROMPT_master-rework-kickoff_2026-10-13.md:17,43,73`; `rework/REGISTER_operator-questions_2026-10-13.md:29`; Workspace `WORKSPACE_STATE.md:3` (by `../IMPLEMENTATION_PLAN.md`); PyApp `hygiene/HYGIENE_DECISIONS.md:110` ("superproject `IMPLEMENTATION_PLAN.md` §7"); Workspace `hygiene/HYGIENE_DECISIONS.md:510` (names `:370`) | `exempt-name` `D-2026-09-16-03` (`:195`, inert, F-A6S-07); its hold released moot (`:194`); allowlist `:103`; the archive move needs `allowlist-remove` | archive to `archive/root/IMPLEMENTATION_PLAN.md` after B4's hand-back section and a REGISTER absorb §5-§7 (F-A6S-01) | Dated 2026-08-04 (git-created 2026-08-05); sequencing is now the batch packages and the rework runbook; waits `Q-G-05` and `Q-A6S-01` |
| `hygiene/CONSUMED_HYGIENE.md` | pinned | `CLAUDE.md:19`; `AGENTS.md:19`; `scripts/hygiene/repo_hygiene_check.py:16,50,504`; `hygiene/HYGIENE_DECISIONS.md:58,206` | rewritten only by a `--force` re-pin | keep | The pin (kit `0.2.1`, 4 roots); a new root edits its table in the commit of the D-entry |
| `hygiene/HYGIENE_DECISIONS.md` | pinned (append-only) | `CLAUDE.md:20,29`; `AGENTS.md:20,29`; `scripts/hygiene/repo_hygiene_check.py:17,51`; every suite's record by name | not applicable | keep | Never edited retroactively; every B3 change appends |
| `handovers/INDEX.md` | live | `onboarding/INDEX.md:10` (link); `repo-hygiene/INDEX.md:25` | exempt by construction | keep | Gains "Renamed" rows on any move |
| `handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md` | live (open) | `handovers/INDEX.md:11`; track runbook `:217,985`; kickoff `:14`; Workspace `docs/proposals/INDEX.md:12,24`; Workspace `hygiene/HYGIENE_DECISIONS.md:453` | none | keep | K-7 undecided (Q-G-06); closes when a Kit session ships the patch |
| `handovers/FINDING_kit-proof-floor-blocks-suite-anchoring_2026-09-16.md` | archive (resolved by K-5, kit 0.2.0) | `handovers/INDEX.md:13`; `repo-hygiene/MATRIX_rename-map_2026-09-16.md:54`; track runbook `:158,568,967` | none | keep (optional archive after `M-9`, F-A6S-11) | Correct root, zero cost; path citations in the track runbook |
| `handovers/FINDING_kit-release-after-move-fails-record_2026-09-16.md` | archive (resolved by K-6, kit 0.2.1) | `hygiene/HYGIENE_DECISIONS.md:132,165` (never edited); `handovers/INDEX.md:12`; track runbook `:178,776,978` | none | keep (optional archive after `M-9`) | The append-only record cites it by path |
| `handovers/HANDOVER_batch-package-schema-drift_2026-09-15.md` | superseded (migration done at onboarding `2a`/`2b`) | `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:5`; `onboarding/INDEX.md:10`; `handovers/INDEX.md:14,20`; `repo-hygiene/INDEX.md:25`; kickoff `:17`; `hygiene/HYGIENE_DECISIONS.md:71,83,91,102,145,151,175,191-193`; submodules: none | `held-name` `D-2026-09-16-03` (`:192`), group onboarding-runbook; released when the onboarding runbook retires, or by an operator-recorded release (Q-A6S-02) | hold; then archive to `archive/handovers/` | Only the runbook's `:5` pins it |
| `onboarding/INDEX.md` | live | `repo-hygiene/INDEX.md:25-27`; `handovers/INDEX.md` | exempt by construction | keep | |
| `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | live (steps `6`-`9` open, last edit 2026-10-02) | `scripts/harness/migrate_checklist_schema.py:3`; `handovers/INDEX.md:20`; `hygiene/HYGIENE_DECISIONS.md:75,83-86,192`; `rework/PROMPT_master-rework-kickoff_2026-10-13.md:14`; `rework/PROMPTS_master-rework-runbook_2026-10-13.md:35`; Server STATE `:207`, SharedContracts STATE `:89`, Dashboard STATE `:112`, AndroidApp STATE `:182`, Workspace V1 STATE `:217`, Workspace SDA STATE `:79` (all `implementation/.../STATE.md`); PyApp `validation/ONBOARDING_harness-port.md:3` | not itself held; it is the citer of all three holds | keep | Retires only after the Conductor program closes step `9`; B8 owns its ledger and §N |
| `onboarding/AUDIT_skill-assumptions_2026-09-15.md` | archive (evidence of finished step `1`) | runbook `:211,212,216,905`; `hygiene/HYGIENE_DECISIONS.md:85,180`; PyApp `scripts/harness/scope_cap.py:5`, `scripts/harness/regression_scope.py:33`, `validation/ONBOARDING_harness-port.md:4` | `held-name` `D-2026-09-16-01` (`:85`), group onboarding-runbook; releasing the group does not free it from the PyApp code citers (F-A6S-06) | hold (do not move even after release) | A file that code cites does not move |
| `onboarding/REGISTER_package-census_2026-09-15.md` | live (running record) | runbook `:251,584,911`; `hygiene/HYGIENE_DECISIONS.md:86,180`; `repo-hygiene/INDEX.md:27`; kickoff `:17`; submodules: none | `held-name` `D-2026-09-16-01` (`:86`), group onboarding-runbook; released when the runbook retires | hold; archive to `archive/onboarding/` then | Receives the table of step 5 and later captures |
| `repo-hygiene/INDEX.md` | live | track runbook; `handovers/INDEX.md` | exempt by construction | keep | Carries the superproject's held/exempt rows in its "Renamed 2026-09-16" table |
| `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` | live (`M-8` todo, `M-9` rolling) | `hygiene/HYGIENE_DECISIONS.md:53,130,159`; `repo-hygiene/INDEX.md:13`; the FINDINGs; kickoff `:14`; runbook skeleton `:35`; every suite's `hygiene/HYGIENE_DECISIONS.md:53` | none | archive to `archive/repo-hygiene/` after `M-9` (Q-A6S-05) | Ledger of record until `M-8`/`M-9` close; a `PROMPTS` file is proof-surface scanned |
| `repo-hygiene/PROMPT_kit-bootstrap-session_2026-09-15.md` | archive (spent single paste block) | `repo-hygiene/INDEX.md:10`; runbook `:3`; map `:113`; census `:3,27,66,79`; inventory `:3` | none | archive to `archive/repo-hygiene/` after `M-8` | Opened a finished track; superseded by the runbook |
| `repo-hygiene/REGISTER_hygiene-harness-inventory_2026-09-15.md` | archive (input of the finished kit derive) | `repo-hygiene/INDEX.md:11`; map `:54`; runbook `:15,23,248,407,451` | none | archive after `M-8` | Kit derived (0.1.0 to 0.2.1) |
| `repo-hygiene/REGISTER_target-corpus-census_2026-09-15.md` | archive (baseline for `M-8`) | `repo-hygiene/INDEX.md:12`; map `:5,54`; runbook `:15,43,250,526,716,775,816,866` | none | archive after `M-8` | `M-8` diffs the final census against it |
| `repo-hygiene/MATRIX_rename-map_2026-09-16.md` | archive (record of gate `GM`; `M-9` reads its targets) | `repo-hygiene/INDEX.md:14,18`; FINDINGs `:9`; `hygiene/HYGIENE_DECISIONS.md:160`; runbook `:235,976`; suites' INDEX "Renamed" rows (e.g. Workspace `docs/proposals/INDEX.md:18`, PyApp `implementation/System_V1_Implementation/proposal/INDEX.md:16`) | none | archive after `M-9` (suites cite it by name, so a "Renamed" row is mandatory) | Release targets live in it until the last hold ends |
| `rework/INDEX.md` | live | none beyond the kickoff | exempt by construction | keep | |
| `rework/PROMPT_master-rework-kickoff_2026-10-13.md` | live | `rework/INDEX.md:11`; runbook `:4,21,39`; the three REGISTERs `:3`; `hygiene/HYGIENE_DECISIONS.md:203,222` | none | keep | The program's only copy of the prompt |
| `rework/PROMPTS_master-rework-runbook_2026-10-13.md` | live | `rework/INDEX.md:12`; kickoff `:35,51`; `hygiene/HYGIENE_DECISIONS.md:223` | none | keep | Ledger of record |
| `rework/REGISTER_operator-questions_2026-10-13.md` | live | runbook `:15,94,116`; kickoff `:28,35`; `hygiene/HYGIENE_DECISIONS.md:224` | none | keep | Receives this file's Q-A6S rows |
| `rework/REGISTER_deferred-validations_2026-10-13.md` | live | runbook `:15`; kickoff `:22,35` | none | keep | |
| `rework/REGISTER_conductor-reuse-candidates_2026-10-13.md` | live | runbook `:15`; kickoff `:35,49` | none | keep | Receives §3 |

**Tracked `.md` in the skill and agent trees (41 files, lane A1's; not read)**

| File | Class | Citers (path:line, or none) | Hold / exemption (D-id) and what releases it | Disposition | Reason |
|---|---|---|---|---|---|
| `.claude/skills/**` (19 `.md`) | live | cites `CLAUDE.md` at `plan-batch/SKILL.md:162` and `run-batch/SKILL.md:30,326`, and `.agents/README.md` at `plan-batch/SKILL.md:174`; six-suite mirror | allowlist `.claude` (`:95`) | keep | A1/B1 sync |
| `.claude/agents/*.md` (3) | live | `.agents/README.md:34-36`; `.claude/agents/batch-closeout-reviewer.md:19` cites `CLAUDE.md` | allowlist `.claude` | keep | A1/B1 |
| `.codex/skills/**` (19 `.md`, byte mirror of `.claude/skills`) | generated-mirror | `.agents/README.md:26-29` | allowlist `.codex` (`:96`); Q-G-09 | keep (frozen if Q-G-09 (a)) | A1/B1 |

**Git-ignored: `Todo.md`** (280 lines, 0 headings, 67 blocks)

| File | Class | Citers (path:line, or none) | Hold / exemption (D-id) and what releases it | Disposition | Reason |
|---|---|---|---|---|---|
| `Todo.md` | live idea backlog (git-ignored), 6-7 ideas live by my estimate (F-A6S-03) | `IMPLEMENTATION_PLAN.md:5,15,26,51-67,358`; onboarding runbook `:820`; `hygiene/HYGIENE_DECISIONS.md:89,110,121`; PyApp `scripts/harness/regression_scope.py:243,246,2854` (a doc-name table); Workspace `methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md:136`, `KICKOFF_PROMPT.md:174,182`, `MVP_Reconciliation/00_SOURCE_INVENTORY.md:13`, `docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_complete.csv:4` | allowlist only (`:110`); no hold; decision P3 2026-07-15 "keep untouched" | keep; ideas copied to a REGISTER, the file left for the operator to empty (Q-A6S-04) | Protected by P3; edited today; line-range citations in frozen records |

**Old handovers under `handovers/`**: four files besides the index, one open FINDING (K-7), two resolved FINDINGs (keep), one superseded HANDOVER (hold). `handovers/INDEX.md:11-14` records their status.

### 7.1b Non-markdown root entries against the allowlist

Allowlist lines are `hygiene/HYGIENE_DECISIONS.md:94-117` (D-2026-09-16-01) plus `:231` (`rework`). Of the 24 root entries (`.git` excluded) every one is allowlisted.

| Root entry | Allowlist line | State | Verdict |
|---|---|---|---|
| `.agents/` | `:94` | one file, stale content (F-A6S-04) | live; rewrite |
| `.claude/` | `:95` | `settings.json` is `{}` since `53051b0`; `settings.local.json` and `worktrees/` are untracked; 13 skills, 3 agents | live |
| `.codex/` | `:96` | `skills/`, `agents/*.toml`, `hooks.json` (git-deny hook only since `7946483`), `hooks/deny_git_commands.mjs` | live now; frozen under Q-G-09 (a) |
| `.github/` | `:97` | `workflows/repo-hygiene.yml`, a `check` job on every push and pull request | live |
| `.gitignore`, `.gitmodules` | `:98-99` | `.gitignore:11-12` carries the graphify line | live; the graphify lines go with Q-A6S-03 (a) |
| `AGENTS.md`, `CLAUDE.md` | `:100-101` | identical | live |
| `IMPLEMENTATION_PLAN.md` | `:103` | root file, see 7.1 | leftover after B4; `allowlist-remove` on archive |
| six `PlantLibrary_*` | `:104-109` | submodules | live |
| `Todo.md` | `:110` | git-ignored, present | live; stays (Q-A6S-04) |
| `graphify-out/` | `:111` | git-ignored, 275 MB, newest write 2026-09-17 | leftover; allowlist line not dead until the folder is gone |
| `handovers/`, `hygiene/`, `onboarding/`, `repo-hygiene/` | `:112-115` | roots and the anchoring folder | live |
| `rework/` | `:231` | root `D-2026-10-13-01` | live |
| `scripts/` | `:116` | `harness/` (3 files) and `hygiene/` (the pinned checker); `migrate_checklist_schema.py` is a spent one-shot (F-A6S-10) | live; A2/B7 |
| `update_graph.bat` | `:117` | tracked; calls `graphify update .` | leftover; allowlist line not dead until the file is gone |

### 7.2 Holds and the record

State of every directive in `hygiene/HYGIENE_DECISIONS.md` as folded by the checker (entries `D-2026-09-16-01` `:51`, `-02` `:128`, `-03` `:157`, `D-2026-10-13-01` `:201`).

| Directive and value | Line | Status | Group / citer / class | Still needed? | Released by |
|---|---|---|---|---|---|
| `held-name: HANDOVER_batch-package-schema-drift_2026-09-15.md` (root path) | `:83` | released at `M-1` (`:191`) | onboarding-runbook | no | `git mv` to `handovers/` |
| `held-name: handovers/HANDOVER_batch-package-schema-drift_2026-09-15.md` | `:192` | **active** | onboarding-runbook; runbook `:5`; live-runbook class | only against a rename or move; its target on release is its own name | the onboarding runbook retiring (`RUNBOOK_migrate-an-existing-repository.md:54`), or an operator-recorded release (Q-A6S-02) |
| `held-name: IMPLEMENTATION_PLAN.md` | `:84` | released moot (`:194`) | onboarding-runbook | no | `D-2026-09-16-03` |
| `held-name: onboarding/AUDIT_skill-assumptions_2026-09-15.md` | `:85` | **active** | onboarding-runbook; runbook `:211,212,216,905`; live-runbook class plus PyApp code class (F-A6S-06) | the code class keeps the file in place regardless | as above; the file should still not move |
| `held-name: onboarding/REGISTER_package-census_2026-09-15.md` | `:86` | **active** | onboarding-runbook; runbook `:251,584,911`; live-runbook class | as above | as above |
| `allowlist` (24 lines) and `allowlist-remove: HANDOVER_...` | `:94-117`, `:193` | 23 active from `D-01` plus `rework` (`:231`) = 24 active, one per root entry | n/a | `graphify-out` and `update_graph.bat` are leftovers kept alive by the files' presence; `IMPLEMENTATION_PLAN.md` and `.agents` follow B4 and A1 | `allowlist-remove` in a later D-entry, in the commit that removes the entry from disk |
| `exempt-name: IMPLEMENTATION_PLAN.md` | `:195` | active, inert (F-A6S-07) | exempt by decision, `GM` proposal 1 | no effect on the root file; would exempt a same-named file in any declared root | no directive ends an `exempt-name`; leave it |
| built-in exempt `INDEX.md`, `README.md` | `KIT_SPEC.md` §1.4 | active | by construction | yes | n/a |
| `exempt-tree`, `exempt-subfolder`, `retired-name`, `forbidden-path`, `scratch-root`, `enum-add`, `held-line` | none | none in the record | n/a | n/a | n/a |
| root `rework` (general, standard) with the roots-table edit | `:231`, `hygiene/CONSUMED_HYGIENE.md:27` | active | `D-2026-10-13-01` | yes | n/a |

**What a release of the three onboarding-runbook holds would need.** The three names are held only against renaming (target on release = current name), so a release changes the verdict from 3 held to 0 held and nothing else, unless the file also moves. The kit offers two honest ends. (1) The runbook retires: only the Conductor program's step `9` and the S-2 gate on step `6` do that (`onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:910-916`); then lane B3 appends one D-entry with three `release` lines quoting `git grep` at HEAD across all seven repositories, and moves the files under `archive/` only where no code citer remains (the AUDIT does not qualify). (2) The operator records a release in words (Q-A6S-02 (b)); B3 appends the `release` lines and, because the runbook is live and cites by basename, the files do not move. Editing the runbook's citing lines is not an option for B3 (kit constraint `RUNBOOK_migrate-an-existing-repository.md:307-309`). The lane that touches the runbook is B8 (ledger, §N notes); B8 can declare the runbook retired only if the operator closes the Conductor onboarding track, which lies outside this program.

### 7.3 Archive layout proposal

**The declaration (option (a), recommended).**

- Folder: `archive/` at the repository root, not a deliverable root and not in the pin's roots table, so `hygiene/CONSUMED_HYGIENE.md` is untouched.
- Contents, by origin folder, basenames unchanged (a move, not a rename): `archive/root/` (`IMPLEMENTATION_PLAN.md`, `update_graph.bat`), `archive/handovers/` (the schema-drift HANDOVER once released), `archive/onboarding/` (`REGISTER_package-census` once released), `archive/repo-hygiene/` (the five track files of 7.1, in the `M-8`/`M-9` order). Not in: `AUDIT_skill-assumptions` (code citers), the two resolved FINDINGs (record citations), anything the pinned record or the checker cites, `CLAUDE.md`, `AGENTS.md`.
- One D-entry, id by grep at execution (`D-2026-10-13-01` exists; take the next free id), with directives:

```text
- allowlist: archive — retired material moved by git mv, basenames unchanged
- exempt-tree: archive — legacy; retired superproject files, moved not renamed; declared at the top-level path only so the folder never needs to move
```

  Per file that leaves the repository root: `allowlist-remove: IMPLEMENTATION_PLAN.md` (and `update_graph.bat`, plus `graphify-out` under Q-A6S-03), optionally `retired-name` for the same names. Per file that leaves a root: a row in that root's "Renamed <date>" table (`old name | archive/<origin>/<name>`) and a one-line reference sweep outside the archive; the old name then resolves through that table (CLAUDE.md rule block). No `INDEX.md` line is needed for a file in `archive/` (not a root), but a plain `archive/INDEX.md` listing `file | origin | archived on | D-id | reason` is recommended for people.
- Checker effect: the file rule never reads `archive/` (it scans declared roots only); the allowlist module sees one new entry; `census` lists every archived `.md` under "Exempt trees" as `legacy`.

**How the K-7 finding limits it.** The kit checker (0.2.1) tests that an `exempt-tree` path exists at the moment it folds the line and has no `release` for it, so once `archive` is declared the path `archive` must exist for ever, and any later `git mv` of a declared path fails `record` permanently (finding `:24-30`, proposed fix `:61-65`). Therefore declare only the top-level `archive`, never a sub-path, never rename or relocate it, and move files freely under it; the same limit is why the Workspace set folder stays under its old name until a Kit session ships K-7.

**Alternatives the kit supports.**

| Alternative | Declaration needed | K-7 exposure | Cost |
|---|---|---|---|
| (b) undeclared `archive/` subfolder inside a root (e.g. `handovers/archive/`) | none; the checker lists it as `subfolder` (`KIT_SPEC.md:60-62`) | none | archives scatter across four roots; no census visibility as `legacy`; the root's "Renamed" table is still needed |
| `exempt-subfolder: <root>/archive` | one D-entry; the checker asserts existence | same as a declared tree | gives nothing more than (b) |
| (c) keep in place under `held-name` or `exempt-name` | existing mechanism (`KIT_SPEC.md:64-69`) | none | the sequencers stay at the root and keep two allowlist lines |
| `retired-name` | one D-entry per name | none | prevents recreation only; moves nothing |

**K-7 options and the Q-G-06 evidence.** The finding's own options are 1 (kit patch K-7, then `M-9` releases the Workspace set; recommended), 2 (accept the hold), 3 (reverse the `M-7` rename). Q-G-06 (a) "record the need, hold the affected set, queue a separate Kit session" is option 1 with the patch run outside this program; Q-G-06 (b) "work around it inside TARGET" has no clean form, because the offending directive is an append-only line that the checker re-reads on every run, and the only way to satisfy it is a stub file at the old path. Evidence for recommending (a): (1) the superproject has zero `exempt-tree`/`exempt-subfolder` lines, so nothing here is blocked, and the archive plan above avoids K-7 by construction (F-A6S-08); (2) the casualties named by the finding (`:36-44`) are Workspace's set folder, PyApp `Documentation/`, SharedContracts `generated/` and frozen `MVP/` trees, in other repositories and other lanes; (3) the kit is read-only for this program and unpatched at `0.2.1`/`810733e`; (4) the finding proposes a small change (a `release` that ends the declaration, a directory `held-name`, three fixtures, version `0.2.2` or `0.3.0`, `:61-77`). B3 should therefore avoid every move of an existing `exempt-tree`/`exempt-subfolder` in all seven repositories until the Kit session ships it.

### 7.4 Checker

`python scripts/hygiene/repo_hygiene_check.py check` (superproject, 2026-10-13, `master` @ `8702e0a`) printed three `held:` lines (the onboarding-runbook holds of 7.2) and the verdict line:

```text
repo-hygiene: pass with holds — 0 violations, 3 held
```

Per-root totals of `census` (this audit file is not yet indexed, so a re-run after it lands needs its `INDEX.md` line first):

```text
repo-hygiene: totals: 6 files, 5 compliant, 0 candidates, 1 exempt, 0 held, 0 set folders
onboarding:   totals: 4 files, 1 compliant, 0 candidates, 1 exempt, 2 held, 0 set folders
handovers:    totals: 5 files, 3 compliant, 0 candidates, 1 exempt, 1 held, 0 set folders
rework:       totals: 6 files, 5 compliant, 0 candidates, 1 exempt, 0 held, 0 set folders
repository:   totals: 21 files, 14 compliant, 0 candidates, 4 exempt, 3 held, 0 set folders
```

The "exempt" count is the four `INDEX.md` files (one per root); no "Exempt trees" table is printed because none is declared.
