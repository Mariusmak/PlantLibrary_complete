# Corpus census — PlantLibrary_PyApp — lane A6 (read-only analysis, 2026-10-13)

Pin: `PlantLibrary_PyApp` main @ `35ddc63`, tree clean at the start. Method: `git ls-files -- '*.md'` (310 files), the hygiene checker's `check` and `census`, `git grep -F` per basename in this repository, the superproject's tracked files (root files, `onboarding/`, `repo-hygiene/`, `handovers/`, `hygiene/`, `rework/`) and the five sibling submodules. Ambiguous basenames (`README.md`, `STATE.md`, ...) were counted only where the parent folder or `PyApp` appears on the same line. Nothing was edited, committed or run beyond the two allowed checker commands.

## §0 Summary

- 310 tracked `.md` files: 64 frozen (`implementation/MVP` 1 + `implementation/Archive_PreMVP` 63), 38 legacy (`Documentation/`), 23 generated (`.docpipeline` 5 + `app/**` 18), 6 inside the declared roots, and 179 in no checker class at all (GUI 48, skill/agent mirrors and vendored trees 110, package/validation/root/hygiene files 21).
- Checker verdict: `repo-hygiene: pass with holds — 0 violations, 1 held`; census: 6 files, 2 compliant, 0 candidates, 3 exempt, 1 held, 0 set folders; 125 exempt-tree files (64 frozen / 38 legacy / 23 generated).
- Directive lines in the record: 5 `exempt-tree`, 2 `exempt-name`, 4 `held-name`; no `release`, no `held-line`, no allowlist line. Two of the four holds are moot while `Documentation/` stays exempt; one (`improvements.md`) can never be released by its citers (pinned tree, initiative closed); one (`PYAPP_V1_PROPOSAL.md`) has met its release precondition (onboarding 2a/2b done) and waits only for M-8 then M-9.
- `DRIVER_SCRIPT.md` is the only stale sequencer here: it still instructs `_ACT_STATE.md` at lines 17, 47, 60 (GC-7053), and the package `README.md` repeats it at lines 47 and 50; no test, script or Conductor source requires the file, so archiving it is statically safe. No `_ACT_STATE.md` exists.
- `Documentation/` cannot be archived: `app/gui/main_window.py:1517` opens `Documentation/PlantLibraryGUI_GPT_V3.md` at runtime and `CLAUDE.md:160` cites `Cross_Platform_Proposal_V2.md`. `Archive_PreMVP/` cannot move either: 16 `app/` and 3 `tests/` files cite its paths in docstrings.
- Recommended archive layout: a new `implementation/archive/` declared once as `exempt-tree: ... legacy` at its final path; no top-level `archive/` (it would need a root-sentinel edit in `tests/test_repo_hygiene.py`); no in-place `exempt-tree` line on a file that will later retire (the K-7 trap).
- K-7 evidence for Q-G-06: PyApp needs no kit patch for any wanted outcome; the only moves K-7 would block (relocating `Documentation/` or `Archive_PreMVP/`) are already blocked by code citers. Q-G-06 (a) stands.
- Dead weight to clear in one `.gitignore` commit: lines 11-14 (GC-2437) and the `graphify-out` sanction (c48aa17), whose tool was dropped on 2026-10-02; the 25 MB `graphify-out/` folder is still on disk and must be deleted by the operator first (Q-A6P-04).
- 7 questions (Q-A6P-01..07), 9 candidates, 3 claims to verify.

## §1 Coverage

| Item | Status (read / partly read / not read) | Reason |
|---|---|---|
| Kickoff prompt §1, §2 | read | Rule 3 (hygiene), Q-G-05, Q-G-06 taken from it |
| `PlantLibrary_PyApp/CLAUDE.md` | partly read | Lines 1-12 and 295-431 (batch/Conductor, scratch policy, deliverable naming, rule block) plus greps; the architecture middle was not needed |
| `PlantLibrary_PyApp/.claude/CLAUDE.md` | partly read | Lines 1-40 and 90-119 plus greps |
| `PlantLibrary_PyApp/AGENTS.md` | partly read | Greps only (511 lines, Codex mirror of CLAUDE.md) |
| `hygiene/CONSUMED_HYGIENE.md`, `hygiene/HYGIENE_DECISIONS.md` | read | Whole files; every directive line enumerated by pattern |
| `repo-hygiene/MATRIX_rename-map_2026-09-16.md` | partly read | PyApp section §4 (lines 122-170), rows 38, 55, 351, 389-453 |
| `handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md` | read | Whole file |
| `Repo_Hygiene_Template_Kit/KIT_SPEC.md` | partly read | §1.4-1.9 and the §6 directive table; the rest was not needed |
| Checker source `scripts/hygiene/repo_hygiene_check.py` | partly read | Lines 425-455 (directive existence rules) |
| `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | partly read | Step rows 185-192, ledger 904-916, §N rows GC-2437 and GC-7053 |
| `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` | partly read | Lines 14-18, 218-222, 984-987 (M-8, M-9 state) |
| Package files (`BATCH_PLAN`, `TASK_CHECKLIST`, `TASK_CONTEXT`) | partly read | Headings, status counts and the `DESIGN.md` hits; bodies not read |
| `DRIVER_SCRIPT.md`, `SCOPE.md`, `README.md`, `CONTEXT_INDEX.md`, `STATE.md` (package) | partly read | DRIVER_SCRIPT, SCOPE, README read in the relevant ranges; STATE.md lines 1-60, 205-228; CONTEXT_INDEX lines 1-12 |
| `validation/*` | partly read | `KNOWN_FAILURES.md` and `README.md` whole; `ONBOARDING_harness-port.md` lines 1-40; `PY1-B02`, `PY1-B07` heads |
| Three `INDEX.md` of the roots | read | Whole |
| `GUI/**` (48) | partly read | File names and citer counts; bodies not read |
| `Documentation/**` (38) | partly read | File names, citer counts, code citers; bodies not read; the five non-md assets (docx, pdf, png) are outside this census |
| `implementation/Archive_PreMVP/**` (63), `implementation/MVP` (1) | not read | Frozen; classified by path and the census listing |
| `.docpipeline/**` (5), `app/**.md` (18) | partly read | Headers and the code-versus-doc commit-date comparison |
| `.claude/**`, `.codex/**`, `.agents/**`, `.github/**` (110) | partly read | Byte comparison against the superproject copies and between the impeccable trees; contents not read |
| `DESIGN.md`, `PRODUCT.md` | partly read | Heads and git dates; DESIGN.md colour values were not compared with SharedContracts tokens 1.2.0 |
| Superproject `Todo.md`, `IMPLEMENTATION_PLAN.md`, `WORKSPACE_STATE.md`, `SUITE_HANDOFFS.md` | not read | Other lanes; only their citation by PyApp files was grepped |
| Untracked `graphify-out/` content | not read | Git-ignored tool output; only its presence and size were observed |

## §2 Findings

- **F-A6P-01 — The checker sees 131 of 310 markdown files.** `check` covers the three declared roots (6 files) plus the exempt trees (125); the pin declares only `implementation/System_V1_Implementation/{planning,proposal,handovers}` (`PlantLibrary_PyApp/hygiene/CONSUMED_HYGIENE.md:25-27`). The 179 others — `GUI/` (48), mirrors and vendored trees (110), the package, validation, root and `hygiene/` files (21) — are catalogued by convention only (`PlantLibrary_PyApp/hygiene/HYGIENE_DECISIONS.md:145-149` "Catalogued, not declared"). Consequence for B3: the archive tree is the first place a new class can be declared; nothing else in the 179 needs a directive to be moved, only a reference sweep.
- **F-A6P-02 — `DRIVER_SCRIPT.md` contradicts itself (GC-7053) and the package README repeats the contradiction.** `PlantLibrary_PyApp/implementation/System_V1_Implementation/DRIVER_SCRIPT.md:7` declares `_ACT_STATE.md` deprecated; lines 17, 47 and 60 still instruct reading, creating and appending it. `PlantLibrary_PyApp/implementation/System_V1_Implementation/README.md:47` tells a fresh session to "Execute ... DRIVER_SCRIPT.md", `:50` says "The driver creates/maintains `_ACT_STATE.md` here", `:61` lists "Batches `PY1-B00`..`PY1-B05`" while `BATCH_PLAN.md` has `PY1-B00`..`PY1-B08`, `:62` lists DRIVER_SCRIPT as the "One-batch execution prompt". The brief's GC-7053 note (onboarding runbook:934) names only the DRIVER_SCRIPT lines; README `:47,50,61,62` is new. `PlantLibrary_PyApp/CLAUDE.md:315` and `AGENTS.md:382` correctly say "do not create, read or update it". No `_ACT_STATE.md` exists on disk or in the index.
- **F-A6P-03 — Nothing static requires `DRIVER_SCRIPT.md`.** A grep over `PlantLibrary_PyApp/tests`, `PlantLibrary_PyApp/scripts` and the superproject `scripts/` returns no hit; `Orchestrator_System/src/conductor/batch_package.py` and `batch_discovery.py` return no hit either. Live citers are prose only: package `README.md:47,62`, `SCOPE.md:3` ("DRIVER_SCRIPT.md is legacy"), `STATE.md:122,177,179`. Its Hard scope (`DRIVER_SCRIPT.md:20-33`) is already duplicated in `SCOPE.md:6-22`; section 1 (`:35-43`) restates `CLAUDE.md` "Design System". Cross-repository citers (onboarding runbook:934, `onboarding/AUDIT_skill-assumptions_2026-09-15.md:41,283,300`, Workspace `MVP_Reconciliation/06_V1_KICKOFF_PROMPT.md:289`) are by name only; the Workspace manifest `REVIEW_LIST.md:30` is a generated list inside a Workspace set (not editable).
- **F-A6P-04 — `Documentation/` has two live runtime or instruction citers.** `PlantLibrary_PyApp/app/gui/main_window.py:1517` builds `PROJECT_ROOT / "Documentation" / "PlantLibraryGUI_GPT_V3.md"` for the "open user guide" action; `PlantLibrary_PyApp/CLAUDE.md:160` and `AGENTS.md:169` send readers to `Documentation/Cross_Platform_Proposal_V2.md`; `app/gui/design_tokens.py:3` cites `Documentation/Verdant_Modern_GUI_Design_System.docx`; `tests/services/test_ai_extraction_service.py:1` cites `plant_information_system_implementation_plan_v1.md` (the code-class hold). The "legacy" label is therefore a hygiene class, not a statement that the corpus is dead.
- **F-A6P-05 — `Archive_PreMVP/` is cited as a path by code.** 16 `app/` modules (for example `app/db/sync_hooks.py:3`, `app/gui/dialogs/sync_conflict_dialog.py:7`, `app/services/sync_service.py`) and 3 `tests/` files name `implementation/Archive_PreMVP/Improvements/Python_Client_Sync/docs/...` in docstrings; live prose cites it too (`CLAUDE.md:381-382`, `AGENTS.md:448-449`, `SCOPE.md:11-12`, `STATE.md` authority lines, package `README.md`). Workspace holds the old-to-new mapping (`manifests/MANIFEST_PyApp.csv`, 3 hits) and five more files cite it. The path is a de facto API.
- **F-A6P-06 — `PYAPP_V1_PROPOSAL.md` has met its release precondition.** The hold's group is live-package (Q5c): "released by onboarding 2a/2b for PyApp, then M-9" (`repo-hygiene/MATRIX_rename-map_2026-09-16.md:160`). Onboarding 2a is ledgered done (`onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:907`, PyApp `0be0e5a`), 2b done (`:908`). The only citers are the package `STATE.md:11` (state), package `README.md:5,63` (sweep-editable), the two hygiene indexes, the record itself and Workspace `00_V1_SYSTEM_PROPOSAL.md:226` (itself held in Workspace). What remains is M-8 (`repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md:986`, todo) before M-9 (`:222`, "any time after M-8").
- **F-A6P-07 — The `improvements.md` hold cannot be released by its citers.** `GUI/screen_structures/improvements.md` is cited at `PlantLibrary_Workspace/methodology/Design_Template_Initiative/INITIATIVE_PROPOSAL.md:122`, `STATE.md:1695` and `evidence/00_inventory_reverification.md:64,94` (pinned tree, `PlantLibrary_PyApp/hygiene/HYGIENE_DECISIONS.md:157`). The release condition "the Design initiative's owner or a Design-kit re-pin" (`PlantLibrary_PyApp/implementation/System_V1_Implementation/handovers/INDEX.md:17`) is not reachable: the initiative closed on 2026-10-12 (kickoff §1) and a closed pinned tree is never edited. The file also sits outside every root, so the checker neither counts nor enforces this hold; it asserts only "do not move". The Dashboard copy `references/PlantLibrary_pythonApp_old/screen_requirements/improvements.md` shares the basename.
- **F-A6P-08 — Two of the four holds are moot, one is code-class.** `Documentation/Design_Implementation_Claude.md` (`HYGIENE_DECISIONS.md:156`; citer Workspace `INITIATIVE_PROPOSAL.md:130`, pinned) and `Documentation/plant_information_system_implementation_plan_v1.md` (`:158`; citer `tests/services/test_ai_extraction_service.py:1`, code) matter only if the `Documentation/` exemption is ever lifted; neither can be released by its citers either way.
- **F-A6P-09 — The `graphify-out` sanction is dead weight but still enforced.** c48aa17 added `.gitignore:23-24`, `tests/test_repo_hygiene.py:45-47` (root allowlist entry `graphify-out`) and `implementation/System_V1_Implementation/STATE.md:225-228` ("sanctioned at this root"); `validation/ONBOARDING_harness-port.md:34` mentions it. The superproject dropped graphify (hooks removed 7946483 and 53051b0, operator answer D5, 2026-10-02). The untracked `graphify-out/` (about 25 MB, dated 2026-09-16) is still in the working tree; removing the allowlist entry before the folder would make the root sentinel fail.
- **F-A6P-10 — `.gitignore` carries dead lines.** `PlantLibrary_PyApp/.gitignore:11-14` ignore `Improvements/GUI_Improvements_V2/screenshots*`; no `Improvements/` folder exists at the root (GC-2437 confirmed). `.tmp/` is listed twice (`:7` and `:16`). The file is stored LF but checks out mixed (`git ls-files --eol`: `i/lf w/mixed`).
- **F-A6P-11 — `K-7` does not bite PyApp's wanted outcomes.** The `exempt-tree` directives are folder-level at `HYGIENE_DECISIONS.md:109,110,132,142,143` and the checker requires each path to exist (`scripts/hygiene/repo_hygiene_check.py:446-451`); the two `exempt-name` lines are bare basenames with no existence rule (`:431-440`). So only a move of `implementation/MVP`, `implementation/Archive_PreMVP`, `Documentation` or `.docpipeline` would fail `record` forever, and each is already blocked or pointless (F-A6P-04, F-A6P-05). `app/` cannot move at all.
- **F-A6P-12 — Generated module docs are mostly older than their code.** 11 of the 18 `app/**/*.md` references have a `.py` with a later last commit than the `.md` (git commit times); 25 commits touched `app/` after 2026-06-22. The pipeline script that made them, `run_docs_pipeline.sh`, reads `./prompts` which now lives at `implementation/Archive_PreMVP/Prompts/` (frozen). Class "generated", but not trustworthy as current reference.
- **F-A6P-13 — Three vendored copies of the impeccable skill, one pointer skill.** `.claude/`, `.agents/` and `.github/` each carry `impeccable` 3.8.0 (SKILL.md, 28 reference files, scripts). After CR removal 25 of the 28 reference files differ between `.claude` and `.agents`, in the command prefix only (`/impeccable` versus `$impeccable`, for example `reference/adapt.md:190`). `gui-validation` is a pointer in the suite and a full skill in the superproject (`.claude/skills/gui-validation/SKILL.md` differs at char 98). The five mirrored skills and three agents are byte-identical to the superproject in `.claude/` and `.codex/` (compared 2026-10-13).
- **F-A6P-14 — Line endings are not uniform.** In the index every checked file is LF, working copies are CRLF for `CLAUDE.md`, `AGENTS.md`, `DESIGN.md`, `PRODUCT.md`, `STATE.md` and LF for `hygiene/HYGIENE_DECISIONS.md`, `DRIVER_SCRIPT.md`, `proposal/INDEX.md` (`git ls-files --eol`). B3/B4 must check `--eol` per file before any rewrite (kickoff rule 8).
- **F-A6P-15 — Package `validation/README.md` lists evidence that does not exist.** `PlantLibrary_PyApp/implementation/System_V1_Implementation/validation/README.md` names `PY1-B00_walkthrough.md`, `PY1-B03_tags_mapping.md`, `PY1-B04_audit.md`, `PY1-B05_release_notes.md`; none is tracked (the folder holds `PY1-B02_mvp_gap_closure.md` and `PY1-B07_token_drift.md`). It is a forward-looking table, not an error, but a reader cannot tell.

## §3 Candidates

| Id | Source path @ pin | What | Verdict | Target repo and path | Lane (B3) | Q id or — |
|---|---|---|---|---|---|---|
| RC-A6P-01 | `PlantLibrary_PyApp/implementation/System_V1_Implementation/DRIVER_SCRIPT.md @ 35ddc63` | Legacy sequencer (GC-7053) | archive | `PlantLibrary_PyApp/implementation/archive/DRIVER_SCRIPT.md`; sweep package `README.md:47,50,62`, `SCOPE.md:3`, `STATE.md` pointers | B3 (archive) with B4 (package edits) | Q-A6P-01, Q-A6P-02 |
| RC-A6P-02 | `PlantLibrary_PyApp/implementation/System_V1_Implementation/proposal/PYAPP_V1_PROPOSAL.md @ 35ddc63` | Held live-package proposal | release then rename to `PROPOSAL_pyapp-v1_2026-07-10.md`, same root | `PlantLibrary_PyApp/implementation/System_V1_Implementation/proposal/` | B3 (M-9, after M-8) | Q-A6P-03 |
| RC-A6P-03 | `PlantLibrary_PyApp/.gitignore:11-14 @ 35ddc63` | Dead ignore lines (GC-2437) plus duplicate `.tmp/` | delete | `PlantLibrary_PyApp/.gitignore` | B3 | — |
| RC-A6P-04 | `PlantLibrary_PyApp/.gitignore:23-24`, `tests/test_repo_hygiene.py:45-47`, `STATE.md:225-228 @ 35ddc63` | graphify-out sanction | retire after the operator deletes `graphify-out/`; one `.gitignore` commit with RC-A6P-03 and a dated `STATE.md` line | `PlantLibrary_PyApp` same paths | B3 (guard edit needs the dated STATE.md entry its docstring requires) | Q-A6P-04 |
| RC-A6P-05 | `PlantLibrary_PyApp/GUI/screen_structures/improvements.md @ 35ddc63` | Held pinned finding | hold in place; record that the hold is permanent | stays; `HYGIENE_DECISIONS.md` note | B3 | Q-A6P-05 |
| RC-A6P-06 | `PlantLibrary_PyApp/GUI/` (48 files; `COMMON_GUI_CHANGE_PROTOCOL.md` binding) | Screen contracts and routing | keep as live input; reclassify per screen at B6 census | `PlantLibrary_PyApp/GUI/` unchanged in B3 | B3 none; B6 | Q-A6P-06 |
| RC-A6P-07 | `PlantLibrary_PyApp/DESIGN.md @ 35ddc63` | Token sheet dated 2026-07-10, CRLF, cited by 134 files (mostly vendored skill text) | keep; compare with tokens 1.2.0 and the Configuration at B5 | `PlantLibrary_PyApp/DESIGN.md` | B3 none; B5 | — |
| RC-A6P-08 | `PlantLibrary_PyApp/.claude/skills/impeccable`, `.agents/skills/impeccable`, `.github/skills/impeccable @ 35ddc63` | Three vendored trees, 87 `.md`, command-prefix variants | adapt: one source of truth and a documented regeneration, decided at B1/B5 | `PlantLibrary_PyApp/.claude/skills/impeccable` | B3 none; B1 | — |
| RC-A6P-09 | `PlantLibrary_PyApp/implementation/archive/` layout (this lane §7.3) | Archive convention reusable by the six sibling repositories | adapt per repository (`implementation/archive/` where a package folder exists) | each suite's `implementation/archive/` | B3 per repo | Q-A6P-01 |

## §4 Questions for the operator

| Id | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A6P-01 | Where does the PyApp archive live? | (a) `implementation/archive/`, declared once as `exempt-tree: ... legacy` at that final path; (b) top-level `archive/` (needs a root-sentinel edit in `tests/test_repo_hygiene.py` and a dated `STATE.md` line); (c) only in-place `exempt-tree` lines on the files to retire | (a) needs no root-allowlist change, matches the existing `implementation/Archive_PreMVP/` and `MVP/` precedent (no `BATCH_PLAN.md` at depth 1, so Conductor discovery ignores it), and the declared path never has to move again (K-7). (c) puts a K-7 trap on every retired file | B3 PyApp archive row, B4 DRIVER_SCRIPT retirement |
| Q-A6P-02 | DRIVER_SCRIPT.md: archive, bannered, or left? | (a) archive to the new folder in B3/B4 together with the package `README.md` and `CONTEXT_INDEX` sweep; (b) the smallest GC-7053 change: a one-line banner on top, file stays; (c) leave as is (D7's current state) | (a) F-A6P-03 shows nothing static depends on it, `SCOPE.md` already carries its Hard scope, and kickoff B4 already says "DRIVER_SCRIPT retired" | B4 PyApp package row, B3 archive row |
| Q-A6P-03 | Release `PYAPP_V1_PROPOSAL.md` now that 2a/2b are done? | (a) yes, in the B3 step that also closes M-8/M-9 for PyApp: `git mv` to `PROPOSAL_pyapp-v1_2026-07-10.md`, `release` line in the same entry, sweep `STATE.md:11` and `README.md:5,63`, mapping row in `proposal/INDEX.md`; (b) keep it held | (a) the precondition is met (F-A6P-06); the sweep touches two prose lines only and changes no batch-row signal | B3 PyApp hygiene row (after M-8) |
| Q-A6P-04 | The `graphify-out` sanction after the tool was dropped | (a) the operator deletes the untracked `graphify-out/` folders (about 25 MB here), then B3 retires the sanction in the same commit as the dead `.gitignore` lines; (b) keep the sanction until the deletion is convenient | (a) removes three coordinated lines that exist for a tool that no longer runs; the order (folder first) avoids a failing root sentinel | B3 `.gitignore` and sentinel edit |
| Q-A6P-05 | Fate of the `improvements.md` hold | (a) accept the hold as permanent: the file stays at `GUI/screen_structures/improvements.md` until B6 retires `GUI/` contracts; a one-line note in the next decision entry says the release condition is unreachable; (b) move it and serve the pinned citers by the mapping table only (the Design initiative's tree must not be edited) | (a) the file sits outside every root so the hold costs the checker nothing; (b) breaks four pinned citations for a gain of one file in `handovers/` | B3 hold bookkeeping; B6 |
| Q-A6P-06 | `GUI/` (48 files) during the rework | (a) keep live in place through B3-B5; B6's census decides per screen contract what is superseded; nothing under `GUI/` is archived before then; (b) archive `GUI/screen_structures/` now | (a) `GUI/COMMON_GUI_CHANGE_PROTOCOL.md` is binding for every `app/gui/` edit (`CLAUDE.md:74,322`, `.claude/CLAUDE.md:95`, `SCOPE.md:15`) and 25 contracts are cited by `GUI_CONTEXT_INDEX.md` | B6 PyApp census |
| Q-A6P-07 | The 18 generated `app/**/*.md` reference docs (11 older than their code) | (a) keep as generated, add a one-line "may be stale" note to the registry only (no edit to the files); (b) archive them; (c) regenerate through the pipeline | (a) the pipeline script is orphaned (its prompts are frozen) and regeneration is a session of its own outside this program | none (B3 only records the class) |

## §5 Reusable things this brief did not name

- `PlantLibrary_PyApp/tests/test_repo_hygiene.py` (root allowlist plus required entries plus forbidden scratch shapes, baselined 38 entries) is the pattern that makes a new top-level folder a decision; the superproject's allowlist module does the same job for its own root. Any new top-level `archive/` in a suite would trip it.
- `PlantLibrary_PyApp/implementation/System_V1_Implementation/validation/KNOWN_FAILURES.md:1-27` is the written reasoning for an empty-by-design ledger (the `resolve_ledger` "applicable or not records" clause); reusable verbatim as the pattern for the other suites' ledgers.
- `PlantLibrary_PyApp/implementation/System_V1_Implementation/validation/ONBOARDING_harness-port.md` (311 lines) is a complete proof-transcript template (digests, line-ending facts, six deliverables) usable as the shape of the B7 port record.
- `PlantLibrary_PyApp/implementation/README.md` (33 lines) already states the three-tier layout (live, `MVP/`, `Archive_PreMVP/`) and the "links inside archived files are frozen" rule; the archive folder needs one added line there, not a new document.
- The proof-of-need pair for K-7 (a moved exempt path versus a code citer) in this repository is a ready worked example for the kit session if the operator ever queues it.
- `.codex/hooks.json` and `.codex/agents/` exist in PyApp (not `.md`, outside this census) and belong to the Q-G-09 freeze decision.
- Non-markdown assets under `Documentation/` (a docx, a pdf and three png files) are cited by code (`app/gui/design_tokens.py:3`) and are unaffected by the markdown classes.

## §6 Claims to verify

1. **Claim: nothing static requires `DRIVER_SCRIPT.md`, so archiving it cannot break the Conductor bind.** Check (read-only, under a minute): `git -C C:\Programmierung\SW_Development\PlantLibrary_PyApp grep -n -i DRIVER_SCRIPT -- tests scripts` and the same pattern with `grep -n -i DRIVER_SCRIPT C:\Programmierung\Orchestrator_System\src\conductor\batch_package.py C:\Programmierung\Orchestrator_System\src\conductor\batch_discovery.py`; both must print nothing.
2. **Claim: `Documentation/PlantLibraryGUI_GPT_V3.md` is opened at runtime by the product, so `Documentation/` cannot be relocated.** Check: `sed -n 1516,1518p C:\Programmierung\SW_Development\PlantLibrary_PyApp\app\gui\main_window.py` must show `guide_path = PROJECT_ROOT / "Documentation" / "PlantLibraryGUI_GPT_V3.md"` inside `_open_user_guide`.
3. **Claim: the checker sees only 131 of 310 markdown files.** Check: `git -C C:\Programmierung\SW_Development\PlantLibrary_PyApp ls-files -- '*.md' | wc -l` prints 310; from inside the submodule `python scripts/hygiene/repo_hygiene_check.py census` prints repository totals `6 files` and 125 rows under "Exempt trees" (64 frozen, 38 legacy, 23 generated); 6 + 125 = 131.

## §7 Disposition

### §7.1 Disposition table

Counts sum to 310. "in/super/x" abbreviates citers inside this repository, in the superproject (root files, `onboarding/`, `repo-hygiene/`, `handovers/`, `rework/`) and in the five sibling submodules. All paths are under `PlantLibrary_PyApp/`.

| File or folder (n) | Class | Citers | Hold / exemption (D-id) and release | Disposition | Reason |
|---|---|---|---|---|---|
| `CLAUDE.md` (1) | live | Every suite and super doc by name (ambiguous basename, not enumerated); `.claude/CLAUDE.md:5` | Rule block lines 414-431 kit-owned, never hand-edited | keep (B2 reconciles outside the block) | Navigational rules, Conductor section, scratch policy (`CLAUDE.md:385-402`), naming pointer (`:404-412`) |
| `AGENTS.md` (1) | live (Codex-facing twin of CLAUDE.md, 511 vs 431 lines) | as above | Same rule block | keep; fate follows Q-G-09 | Frozen-versus-mirror decision belongs to B1/B2 |
| `PRODUCT.md` (1) | live | in 96 (mostly vendored skill text), super 1 (`repo-hygiene` runbook:574,968), x 8 | `exempt-name` D-2026-09-16-01 (`HYGIENE_DECISIONS.md:137`); dormant, the file is outside every root; no release needed | keep | Durable PRD, 2026-07-04 |
| `DESIGN.md` (1) | live; adoption of tokens 1.2.0 pending (`TASK_CHECKLIST.md:39`, `PY-V1-DS-03` todo) | in 134 (mostly vendored skill text, `CLAUDE.md` Design System), super 1, x 13 | `exempt-name` (`HYGIENE_DECISIONS.md:138`); dormant | keep; compare with the Configuration at B5 | Token sheet dated 2026-07-10 |
| `hygiene/` (2) | frozen-pinned (kit pin and append-only record) | in many; every sibling repo's pattern | n/a | keep; append-only | `KIT_SPEC.md` §6 forbids retroactive edits |
| `implementation/README.md` (1) | live | in 2 (`HYGIENE_DECISIONS.md:161`, `EVIDENCE_...:11`); super 4; x 3 (Workspace `VERIFICATION_REPORT.md:50,64,70`) | none | keep; B3 adds one line for `implementation/archive/` | Layout statement; cites Workspace `MANIFEST_PyApp.csv` by its current set-folder path |
| `implementation/System_V1_Implementation/BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md` (3) | live, Conductor-bound (15-column schema; 3 done, 5 blocked, 10 todo rows; next `PY1-B08`) | `BATCH_PLAN`: in 2, super 6, x 15; `TASK_CHECKLIST`: in 1, super 3, x 12; `TASK_CONTEXT`: in 1 (`scripts/check_token_drift.py:9`), super 2, x 18 | package schema files, not roots; none | keep; B4 edits only | Package contract; validation cells never widened |
| `implementation/System_V1_Implementation/STATE.md` (1) | live, append-only status | in 1 (`HYGIENE_DECISIONS.md:155,253`), super 6, x 25 | Holds `PYAPP_V1_PROPOSAL.md` as its citer (line 11); carries the graphify sanction (`:225-228`) | keep; sweep line 11 on release (Q-A6P-03) | Only dated entries are appended |
| `implementation/System_V1_Implementation/SCOPE.md` (1) | live | in 0, super 4, x 1 | none | keep | Carries the Hard scope and standing invariants (`:6-22`); line 3 marks DRIVER_SCRIPT legacy |
| `implementation/System_V1_Implementation/CONTEXT_INDEX.md` (1) | live | in 27 (Archive_PreMVP copies share the basename), super 2, x 6 | none | keep | Already says no `_ACT_STATE.md` (`:3`) |
| `implementation/System_V1_Implementation/README.md` (1) | live but stale | in 1, super 4, x 3 | none | keep; B4 refresh of `:47,50,61,62,5,63` | F-A6P-02 |
| `implementation/System_V1_Implementation/DRIVER_SCRIPT.md` (1) | superseded by `run-batch` and `SCOPE.md` | in 1 (`README.md:47,62`) plus `SCOPE.md:3`, `STATE.md:122,177,179`; super 3 (onboarding runbook:934, audit 41,283,300, kickoff); x 5 (Workspace set files, frozen prompt) | none; lines 17, 47, 60 still instruct `_ACT_STATE.md` (GC-7053, left open by D7) | archive to `implementation/archive/DRIVER_SCRIPT.md` (Q-A6P-02) | Nothing static depends on it (F-A6P-03) |
| `implementation/System_V1_Implementation/{planning,proposal,handovers}/INDEX.md` (3) | live (kit-owned indexes) | the three roots; `PROMPTS_..._runbook:980` | none | keep; B3 appends lines and "Renamed" rows | Same-commit rule |
| `.../planning/EVIDENCE_source-gui-integration-run_2026-07-04.md` (1) | live evidence (final) | in 3 (`GUI/GUI_CONTEXT_INDEX.md:25`, `planning/INDEX.md:11,19`, `HYGIENE_DECISIONS.md:266`); super 2 | compliant; none | keep | Moved by M-2; its own lines 13, 20 are history |
| `.../proposal/PROPOSAL_future-gui-development-workflow_2026-07-03.md` (1) | live, "proposed (no adoption record)" | in 3 (`GUI/README.md:32`, `proposal/INDEX.md:12,20`, `HYGIENE_DECISIONS.md:263,280`); super 2 | compliant; none | keep; B6 may mark superseded by the design-migration workflow | Still the only description of the three-layer GUI model |
| `.../proposal/PYAPP_V1_PROPOSAL.md` (1) | live, held | in 4 (`STATE.md:11`, `README.md:5,63`, `proposal/INDEX.md:11,21`, `HYGIENE_DECISIONS.md:155,160,253`); super 3 (`MATRIX:160,168,351`); x 2 (Workspace `00_V1_SYSTEM_PROPOSAL.md:226`, transcript `Fable5_Prompt_Improvements`) | `held-name` D-2026-09-16-01 (`HYGIENE_DECISIONS.md:155`), group live-package; release: onboarding 2a/2b migrated (met, F-A6P-06) then M-8 then M-9 | hold now; release and rename in the B3 M-9 step (Q-A6P-03) | Target `PROPOSAL_pyapp-v1_2026-07-10.md` |
| `.../validation/KNOWN_FAILURES.md` (1) | live, empty by design | in 5 (`CLAUDE.md:363`, `AGENTS.md:430`, `STATE.md:214`, `ONBOARDING_harness-port.md:46,90,91`); super 2 | none (validation evidence is catalogued, `KIT_SPEC.md` §1.7) | keep, empty | `resolve_ledger` admits a zero-record file |
| `.../validation/ONBOARDING_harness-port.md` (1) | frozen evidence (proof transcript) | in 5 (`CLAUDE.md:372`, `AGENTS.md:439`, `STATE.md:217`, `validation/README.md:12`); super 2 (onboarding runbook:527,910,929) | none | keep, do not edit | Digest pins are mirrored in `tests/acceptance/test_harness_port.py` |
| `.../validation/PY1-B02_mvp_gap_closure.md`, `PY1-B07_token_drift.md` (2) | frozen evidence | in 2 and 2 (`STATE.md:74,86`; `TASK_CHECKLIST.md:40`, `TASK_CONTEXT.md:237`); x 7 for B02 (Server and Workspace validation files) | none | keep | Row evidence, `<BATCH>_<slug>` shape |
| `.../validation/README.md` (1) | live, partly forward-looking | in 1; super 4 | none | keep; B4 may mark the not-yet-existing files | F-A6P-15 |
| `.../validation/evidence/PY-V1-GAP-CLOSURE-20260715-03/00_summary.md` (1) | frozen evidence | in 0 by name | none | keep | Evidence pack summary (the pack's png and txt files are not markdown) |
| `implementation/MVP/` (1: `package/IMPLEMENTATION.md`) | frozen | in 1 (`implementation/README.md:12`); x 2 (Workspace `PROPOSAL.md:103`, `REVIEW_LIST.md:30`) | `exempt-tree` frozen D-2026-09-16-01 (`HYGIENE_DECISIONS.md:109`); never released; K-7 fixes the path | keep (no move) | Terminal MVP evidence (`CLAUDE.md:311-312`) |
| `implementation/Archive_PreMVP/Improvements/Python_Client_Sync/` (27) | frozen | `CLAUDE.md:381`, `AGENTS.md:448`, `SCOPE.md:11`, `STATE.md`, `CONTEXT_INDEX.md:30`; 16 `app/` and 3 `tests/` docstrings; x 25+ (Workspace manifests, `VERIFICATION_REPORT.md` 10) | `exempt-tree` frozen (`HYGIENE_DECISIONS.md:110`); never released; K-7 fixes the path | keep (no move) | Path is cited by code (F-A6P-05) |
| `implementation/Archive_PreMVP/Archive/GUI_Improvements_V3/screen_requirements_GPT/` (14) | frozen | `SCOPE.md:12`, `CLAUDE.md:381-382`; Workspace manifests; basenames shared with `GUI/screen_structures/` and Dashboard `references/` copies | same `exempt-tree` | keep (no move) | Superseded copies of the GUI contracts, kept as record |
| `implementation/Archive_PreMVP/Prompts/` (22) | frozen | in only mutual, `.docpipeline/*` and `Documentation/Cross_Platform_Checklist.md`; `RUN.md` 0; `run_docs_pipeline.sh` reads `./prompts` | same `exempt-tree` | keep (no move) | Pipeline prompts of the pre-MVP phase |
| `Documentation/` direct pre-MVP session docs (24: the 27 less the three singled out below) | legacy | mutual and `hygiene/`, `MATRIX`, `REGISTER_target-corpus-census` rows; `Cross_Platform_Implementation_Plan_V2.md` has 17 in-repo citers | `exempt-tree` legacy D-2026-09-16-01 (`HYGIENE_DECISIONS.md:132`); lifting needs a new entry and, if moved, K-7 | keep in place | Q4b exempt corpus; no live need |
| `Documentation/Cross_Platform_Proposal_V2.md` (1) | legacy, live-cited | in 5 (`CLAUDE.md:160`, `AGENTS.md:169`, `Cross_Platform_Implementation_Plan_V2.md:3,3138`); x 2 (Workspace `FOLLOWUP_CLOSURE_PROMPT.md:54`, `VERIFICATION_REPORT.md:210,211`) | same `exempt-tree` | keep in place | Instruction files point to it |
| `Documentation/Design_Implementation_Claude.md` (1) | legacy, held (pinned) | in 4; x 1 (Workspace `INITIATIVE_PROPOSAL.md:130`, pinned) | `held-name` (`HYGIENE_DECISIONS.md:156`); moot while exempt; target `PLAN_verdant-design-system-adoption_2026-06-16.md` | hold | F-A6P-08 |
| `Documentation/plant_information_system_implementation_plan_v1.md` (1) | legacy, held (code) | in 6 (`tests/services/test_ai_extraction_service.py:1`) | `held-name` (`HYGIENE_DECISIONS.md:158`); moot while exempt; target `PLAN_plant-information-system-v1_2026-06-17.md` | hold | F-A6P-08 |
| `Documentation/PlantLibraryGUI_GPT_V3.md` (1) | legacy product spec, runtime-cited | in 5 (`app/gui/main_window.py:1517`); x 1 (`INITIATIVE_PROPOSAL.md:130`) | same `exempt-tree` | keep in place, never move | Opened by the user-guide action (F-A6P-04) |
| `Documentation/DatabaseStructure_GPT_V3.md`, `plant_information_api_keys.md`, `plant_information_sources.md` (3) | legacy product specs | in 4, 3, 3 (mutual) | same `exempt-tree` | keep in place | Product specs, cited by the long plan |
| `Documentation/adr/` (7: six ADRs and `README.md`) | legacy (product ADRs, own naming) | in 4 each (`Cross_Platform_Checklist.md:15-20`, `...Plan_V2.md:77-82`, archive prompt `P0_phase0_foundations.md`); `adr/README.md` x 3 | same `exempt-tree` | keep in place | Decisions 0001-0006 |
| `GUI/COMMON_GUI_CHANGE_PROTOCOL.md` (1) | live, binding | in 25 (`CLAUDE.md:74,322`, `.claude/CLAUDE.md:95`, `AGENTS.md:131,389`, `SCOPE.md:15`, `run-batch/SKILL.md:31` in all seven mirrors); x 11 | catalogued, not declared | keep | Binding for every `app/gui/` edit |
| `GUI/GUI_CONTEXT_INDEX.md`, `CONTEXT_LOADING_GUIDE.md`, `README.md` (3) | live routing | in 18, 4, 2; x 2-3 | catalogued | keep; B6 re-routes | Entry points for GUI work |
| `GUI/COMMON_DESIGN_REQUIREMENTS.md` (1) | live | in 7; x 1 | catalogued | keep; B5/B6 compare with the Configuration | Shared rules |
| `GUI/SCREEN_STRUCTURE_INDEX.md`, `SCREEN_STRUCTURE_SUMMARY.md` (2) | live | in 4 and 1; x 1 and 2 | catalogued | keep | Screen routing |
| `GUI/common_requirements/README.md` (1) | live | in 0 by path | catalogued | keep | Folder readme |
| `GUI/screen_structures/Screen_Structure_<id>.md` (25) | live contracts | `GUI_CONTEXT_INDEX.md`, `SCREEN_STRUCTURE_INDEX.md`, summary; x several (Dashboard `references/PlantLibrary_pythonApp_old/screen_requirements/` copies share basenames; Workspace Design initiative cites `Screen_Structure_Index.md`) | catalogued | keep; B6 census decides supersession per screen | Contract-first rule (`SCOPE.md:15`) |
| `GUI/screen_structures/` README, Index, Implementation_Policy, Screen_Coverage_From_Source, Component_Library_Coverage (5) | live | in 1-3 (mutual); x 1-9 | catalogued | keep | Same set |
| `GUI/screen_structures/improvements.md` (1) | live, held (pinned) | in 2 (`HYGIENE_DECISIONS.md:148,157,246`, `handovers/INDEX.md:17`); super 3; x 1 plus pinned initiative 4 | `held-name` (`HYGIENE_DECISIONS.md:157`); release condition unreachable (F-A6P-07) | hold (Q-A6P-05) | Target `FINDING_gpt-screen-requirement-merge_2026-07-01.md` in `handovers/` |
| `GUI/source_derived/` (8: README plus seven derived-requirement files) | live (derived from `app/`, 2026-07-04) | `GUI_CONTEXT_INDEX.md:18-24`, `app/gui/workers/login_worker.py:19`, `TASK_CONTEXT.md:366`; x 3 | catalogued | keep | Derived requirements |
| `GUI/templates/Contract_Packet_Template.md` (1) | live template | in 1; super 1; x 2 | catalogued | keep | Template |
| `.docpipeline/` (5) | generated | each other and `Archive_PreMVP/Prompts/0x_*.md` | `exempt-tree` generated (`HYGIENE_DECISIONS.md:142`) | keep in place | Pipeline step artifacts |
| `app/**/*.md` (18 module reference docs) | generated | `.docpipeline/modules_documented.md` only | `exempt-tree` generated, only the `.md` files (`HYGIENE_DECISIONS.md:143`) | keep in place (Q-A6P-07) | 11 of 18 older than their code (F-A6P-12) |
| `.claude/CLAUDE.md` (1) | live | in 10 (`CLAUDE.md:5`, archive copies); super 7; x 23 | none | keep (B2) | Detailed rules file |
| `.claude/agents/` (3) and `.claude/skills/{plan-batch,real-stack-testing,run-batch,test-driven-development,validate-real-stack}` (8) | mirror, byte-identical to the superproject | parity checker (superproject); `CLAUDE.md:325-331` | none | keep; B1 resyncs | Do not edit in place |
| `.codex/skills/` (8) | mirror (Codex), byte-identical to the superproject `.codex` | same | none | keep; Q-G-09 | Frozen or removed by B1 |
| `.claude/skills/gui-validation/SKILL.md`, `.agents/skills/gui-validation/SKILL.md`, `.github/skills/gui-validation/SKILL.md` (3) | vendored pointer | none by name | none | keep; B1 | Differs from the superproject skill (char 98) |
| `.claude/skills/impeccable/`, `.agents/skills/impeccable/`, `.github/skills/impeccable/` (87: three SKILL.md and 28 reference files each) | vendored third-party (impeccable 3.8.0) | `CLAUDE.md` Design System; reference files cite `DESIGN.md`/`PRODUCT.md` 134/96 times | none | keep; B1/B5 decide the single source | Command-prefix variants (F-A6P-13) |

### §7.2 Holds and exemptions

All lines are in `PlantLibrary_PyApp/hygiene/HYGIENE_DECISIONS.md`. No `release`, `held-line`, `enum-add`, `allowlist`, `allowlist-remove`, `retired-name`, `forbidden-path` or `scratch-root` line exists; the scratch module and the root-allowlist module are off (`:167-170`). Decisions D-2026-09-16-02 (naming pointer), -03 (re-pin to kit 0.2.1) and -04 (M-2 migration) carry no directive line. The last entry is D-2026-09-16-04; no 2026-10 entry exists, so B3's first id is `D-<B3 date>-01`.

| Line | Directive | State | Release condition |
|---|---|---|---|
| 109 | `exempt-tree: implementation/MVP` (frozen) | active, 1 file | none (terminal evidence); path locked by K-7 |
| 110 | `exempt-tree: implementation/Archive_PreMVP` (frozen) | active, 63 files | none; path locked by K-7 and by code citers |
| 132 | `exempt-tree: Documentation` (legacy) | active, 38 files | a new decision entry lifting it; a move needs K-7 and an edit of `app/gui/main_window.py:1517` and `CLAUDE.md:160` |
| 137 | `exempt-name: PRODUCT.md` | active, dormant (file outside every root; no existence rule, checker `:431-440`) | none needed |
| 138 | `exempt-name: DESIGN.md` | active, dormant | none needed |
| 142 | `exempt-tree: .docpipeline` (generated) | active, 5 files | none; path locked by K-7 |
| 143 | `exempt-tree: app` (generated, only its 18 `.md`) | active | none; `app/` cannot move |
| 155 | `held-name: .../proposal/PYAPP_V1_PROPOSAL.md` | active; the one hold the checker counts (`1 held`) | Onboarding 2a/2b migrated (met: ledger `onboarding/PROMPTS_...:907-908`), then M-8 closed (todo) then M-9: `git mv`, a `release` line in the same entry, sweep `STATE.md:11` and `README.md:5,63` |
| 156 | `held-name: Documentation/Design_Implementation_Claude.md` | active, moot while 132 stands | Citer is Workspace pinned `INITIATIVE_PROPOSAL.md:130` (closed initiative): not releasable by the citer; only by an operator decision |
| 157 | `held-name: GUI/screen_structures/improvements.md` | active, outside every root (not in the checker's `held:` list) | "Design initiative's owner or a Design-kit re-pin" — unreachable, initiative closed 2026-10-12 (Q-A6P-05) |
| 158 | `held-name: Documentation/plant_information_system_implementation_plan_v1.md` | active, moot while 132 stands | Citer is code (`tests/services/test_ai_extraction_service.py:1`); release after that docstring changes or the operator decides |

### §7.3 Archive layout proposal

**Recommendation (Q-A6P-01 (a)): `implementation/archive/`, declared once as `exempt-tree: implementation/archive — legacy`.** Reasons: (1) `implementation/` already holds the two frozen siblings and is Conductor's intake root, and a folder with no `BATCH_PLAN.md` at depth 1 is not a package (the precedent of `MVP/` and `Archive_PreMVP/`, onboarding runbook:52); (2) no root allowlist change, so `tests/test_repo_hygiene.py` and a dated `STATE.md` line stay untouched; (3) the path is declared at its final place, so it never trips K-7. The in-place alternative ("the kit's alternative": an `exempt-tree` line on each file that retires) is rejected because each such line would be stuck on a path that later moves. A top-level `archive/` is the kickoff's wording but costs a guard edit here.

What goes in on B3/B4: `DRIVER_SCRIPT.md` (RC-A6P-01) and any later retirees named by B4; nothing from `GUI/`, `Documentation/`, `Archive_PreMVP/`, `MVP/` or `.docpipeline/` (all stay, Q-A6P-05/06/07, F-A6P-04/05).

**What K-7 limits (two sentences).** Any `exempt-tree` or `exempt-subfolder` path in the append-only record fails `record` for ever once it is moved or renamed, because nothing can end the declaration (kit 0.2.1; `handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md`). In PyApp that locks `implementation/MVP`, `implementation/Archive_PreMVP`, `Documentation`, `.docpipeline` and `app`, and makes an in-place `exempt-tree` line on a file that later retires a trap; new exempt trees at a final path, files moved into them, and any `held-name` release remain allowed.

**The D-entry B3 would write** (id verified by grep at that time; the first is `-01`, verbatim operator words go where the gate answered):

```text
## <B3 date> — rework archive

### D-<B3 date>-01 — implementation/archive declared; DRIVER_SCRIPT.md retired into it

Authority: rework runbook step B3 (PyApp row); gate answers Q-A6P-01 (a), Q-A6P-02 (a), Q-G-05, Q-G-06 (a),
verbatim and dated. Preconditions measured: checker `pass with holds — 0 violations, 1 held`; git grep over tests,
scripts and Orchestrator_System src finds no DRIVER_SCRIPT dependency; `git ls-files --eol` per touched file.
Dispositions: DRIVER_SCRIPT.md moved by git mv; package README.md, SCOPE.md and STATE.md pointers swept; mapping row in
planning/INDEX.md "Renamed <B3 date>". Commit line: hygiene: B3 - PlantLibrary_PyApp archive declared; DRIVER_SCRIPT retired

- exempt-tree: implementation/archive — legacy; retired control files of the V1 package, declared at its final path, never renamed (K-7)
```

A second entry, in the M-9 step after M-8, for Q-A6P-03 (a):

```text
### D-<date>-02 — PYAPP_V1_PROPOSAL.md released and renamed

- release: implementation/System_V1_Implementation/proposal/PYAPP_V1_PROPOSAL.md — onboarding 2a/2b done; git mv to PROPOSAL_pyapp-v1_2026-07-10.md in this commit
```

**The INDEX lines B3 would write**

- `implementation/archive/INDEX.md` (not a declared root, so the checker does not read it; a plain list for readers): `- 2026-10-13 · DRIVER_SCRIPT.md · legacy sequencer retired by B3 · was implementation/System_V1_Implementation/DRIVER_SCRIPT.md · superseded by run-batch and SCOPE.md (GC-7053)`.
- `implementation/System_V1_Implementation/planning/INDEX.md`, closing section `## Renamed <B3 date>`: `| ../DRIVER_SCRIPT.md | ../../archive/DRIVER_SCRIPT.md — archived (D-<B3 date>-01) |` and, if the B3 evidence file lands here, its own `- <date> · EVIDENCE_<topic>_<date>.md · EVIDENCE · final · <summary>` line in the same commit.
- `implementation/System_V1_Implementation/proposal/INDEX.md` after Q-A6P-03 (a): the held line at the top of the list becomes `- 2026-07-10 · PROPOSAL_pyapp-v1_2026-07-10.md · PROPOSAL · live · the PyApp MVP→V1 suite proposal (renamed from PYAPP_V1_PROPOSAL.md at M-9)` and the "Renamed" table row `PYAPP_V1_PROPOSAL.md` changes from **held** to the new name.

**Q-G-06 evidence for PyApp.** (1) No wanted PyApp outcome needs an exempt path to move: the archive is a new folder (allowed), `PYAPP_V1_PROPOSAL.md` is a held file, not an exempt path (K-6 covers it), `DRIVER_SCRIPT.md` is in no exempt tree. (2) The only moves K-7 would block (`Documentation/` into an archive, `Archive_PreMVP/` into an archive) are independently blocked by code citers (`app/gui/main_window.py:1517`; 16 `app/` and 3 `tests/` docstrings) and by live prose (`CLAUDE.md:160,381`; `AGENTS.md:169,448`; `SCOPE.md:11`). (3) So option (a) "record the need, hold the affected set, queue a kit session" costs PyApp nothing now; option (b), a workaround inside the target, would add a second `exempt-tree` declaration to be abandoned later and is not needed.

### §7.4 Checker

`python scripts/hygiene/repo_hygiene_check.py check`, run inside the submodule on 2026-10-13:

`repo-hygiene: pass with holds — 0 violations, 1 held`

(the one `held:` line is `implementation/System_V1_Implementation/proposal/PYAPP_V1_PROPOSAL.md`).

`census` per-root totals:

| Root | Totals |
|---|---|
| `implementation/System_V1_Implementation/planning` (planning, standard) | 2 files, 1 compliant, 0 candidates, 1 exempt, 0 held, 0 set folders |
| `implementation/System_V1_Implementation/proposal` (proposal, standard) | 3 files, 1 compliant, 0 candidates, 1 exempt, 1 held, 0 set folders |
| `implementation/System_V1_Implementation/handovers` (handovers, date-anywhere) | 1 files, 0 compliant, 0 candidates, 1 exempt, 0 held, 0 set folders |
| Repository totals | 6 files, 2 compliant, 0 candidates, 3 exempt, 1 held, 0 set folders |

Exempt trees: 125 files (64 frozen, 38 legacy, 23 generated). The "exempt" figure inside each root is its `INDEX.md`.
