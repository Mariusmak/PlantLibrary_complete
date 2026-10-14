# PlantLibrary master rework — GUI rework lane runbook (`B6a` Dashboard, `B6c` PyApp, `B6b` AndroidApp)

*Pointed lane file of `PROMPTS_master-rework-runbook_2026-10-13.md` (§3.2 rows `B6a-*`, `B6b-*`, `B6c-*`), written at
`R-3` (2026-10-13, Fable 5.1 · xhigh). Its §L is the ledger of record for these steps; the master runbook's §L rows
read "pointed". The rules are the master runbook's §2 and the kickoff prompt's §2. Stage names follow methodology
4.1.0 (`PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology`, restructure order 00 → 01 → 01a → 02 → 03 →
04 → 05 → 06 → 06a → 06b → 06c → 06d → 07/08 → implementation). Nothing here runs a test, a build, a browser, an
emulator or the app; capture (03), visual gates (09/10) and the mockup render tools are deferred-validation rows.*

## 0. What this is, and what it is not

| | |
|---|---|
| Scope | one design-migration workspace per client at `PlantLibrary_<Client>/implementation/Design_Migration_V1/` (the pilot's layout and naming deviation, recorded in each workspace README), from bootstrap to the direct implementation of the classified changes with mechanical design checks only |
| Not here | the Configuration and the anchoring (lane `B5`); row cells of the V1 packages beyond the recorded supersessions (lane `B4`'s rule); captures, gates and visual proof (Phase C) |
| Order | `B6a` Dashboard in full; `B6c` PyApp after `B5-5`, its SharedContracts-writing steps after `B6a`'s; `B6b` AndroidApp planning after `B5-6`, its implementation after the Kit session (Q-A4-05) — Q-G-08 (a) |
| Inputs | `AUDIT_gui-current-state-{dashboard,androidapp,pyapp}_2026-10-13.md` (the census inputs, §7.6; the stack facts, §7.7), `AUDIT_design-kit-and-methodology_2026-10-13.md` §7.5 (the stage list, the pilot's rounds, what transfers), `AUDIT_batch-packages_2026-10-13.md` §7.3 (the GUI rows and their relation), the deferred register's `DV-A9*` rows |
| Models | census and comparison steps Opus 5.5 · high; forward surface, IA, mockups and change classification Opus 5.5 · xhigh; implementation Opus 5.5 · high; gates: operator, Opus 5.5 · high records |

## 1. Common shape of the three sub-lanes

| Step | Stage | Route | Writes | Gate |
|---|---|---|---|---|
| `-1` | 00 bootstrap | session (headless) | the workspace from the methodology templates; `STATE.md` with the re-skin/restructure decision; hygiene D-entry declaring the workspace's `planning/`, `proposal/`, `handovers/` roots | — |
| `-2` | 01 mechanical census + 01a function/UI census | session (headless) | `01_*` census files from the A9 input, re-measured at the client's current commit; the Kit's static checks quoted | — |
| `-3` | 02 screen contracts + 04 target normalisation (03 capture recorded unavailable) | session (headless) | contracts per screen in the workspace; `DV` rows for capture | — |
| `-4` | 05 comparison (static) + 06 gap map | session (headless) | the gap map | — |
| `-5` | 06a forward surface + information model | session (headless) · xhigh | the forward-surface table (open V1 rows: reserve / absorbed / no-UI), the settings classification, the information model | `G-<client>-1` (operator) |
| `-6` | 06b IA, then page/pattern contracts and fixture-driven page mockups into SharedContracts `design/contracts/` and `design/gallery/pages/` + 06c mockup audit (mechanical + rubric; the operator opens the HTML) | session (headless) · xhigh; SharedContracts serialized | the IA; the contracts and mockups (SharedContracts, version step); the audit | `G-<client>-2` (operator, after the IA) and `G-<client>-3` (after the audit) |
| `-7` | 06d change classification + amendment + waves; then 07 `/plan-batch` into the V1 package and 08 `SCOPE.md` | plan | the classification; new rows and batches in the V1 package; the superseded/absorbed rows' STATE lines | `G-<client>-4` (operator) |
| `-8` | implementation of the classified changes, batch by batch, mechanical design checks only | session (headless), one per batch | the client's source; `STATE.md`; `DV` rows for every visual leg | — |

Every step's block below follows the master runbook's paste-block shape; each gate is an ordinary step whose block records the operator's words.

## 2. Hygiene and dispatch facts for every workspace

- `implementation/` is not a declared root in the three clients; the workspace's `planning/`, `proposal/` and `handovers/` become roots by a D-entry in the client's `hygiene/HYGIENE_DECISIONS.md` and a roots-table edit of `hygiene/CONSUMED_HYGIENE.md` in the `-1` step, with their `INDEX.md` seeded; methodology file names inside the workspace (`00_…`, `STATE.md`) are package files, not deliverables (the pilot's accepted deviation, restated in the workspace README).
- Dispatch: the workspace is a second package in the suite, bootstrapped unbound (Q-A4-06's reading: the instance-2 bindings are obsolete; no instance project is created); every `-7`/`-8` act names the package by path.
- The SharedContracts writes of `-6` (contracts, gallery pages, fixtures, a `DESIGN_VERSION.md` step) serialize across the three clients and with `B5`/`B4`/`B3` steps on that repository.
- Closeout coupling (PyApp): the harness refuses `resources/styles/*.qss` as an unmapped touched path (Q-A9P-04); `B6c-8` records a deferred row per QSS-touching batch until that is settled.

## 3. Lane `B6a` — Dashboard

#### `B6a-1` — workspace bootstrap (00)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development\PlantLibrary_Dashboard` on `main` (in place) · **Precondition:** `B5-4`, `R-4.2` · **Writes:** `implementation/Design_Migration_V1/**`, `hygiene/HYGIENE_DECISIONS.md`, `hygiene/CONSUMED_HYGIENE.md` · **Waits:** Q-A4-06, Q-A9D-01

```text
B6a-1 — the Dashboard design-migration workspace
Bootstrap the Dashboard's design-migration workspace from the methodology 4.1.0 templates, pinned to the BINDING Configuration through this client's design/conformance/CONSUMED_DESIGN.md, with the restructure-or-re-skin decision recorded.
Context: step B6a-1 of C:\Programmierung\SW_Development\rework\PROMPTS_gui-rework-runbook_2026-10-13.md (§3), pointed from the master runbook §3.2; rules: kickoff §2; the answers: Q-A4-06, Q-A9D-01 (master §Q); the layout: AUDIT_design-kit-and-methodology_2026-10-13.md §7.5 ("Where each workspace lives", "Hygiene"); the pilot: C:\Programmierung\Orchestrator_System\implementation\Design_Migration_V1\README.md (read-only) for the folder set and the naming deviation; the methodology: PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/PROMPTS/00_* and its templates folder.
Where: the Dashboard submodule on main, in place; one commit.
Scope: the workspace folder with the methodology's required files and hierarchy v4 (README recording the naming deviation, STATE.md with the Q-A9D-01 decision, SCOPE.md §1 pinning the Configuration version and the Kit version by pointer to design/conformance/CONSUMED_DESIGN.md, planning/ proposal/ handovers/ with seeded INDEX.md); the D-entry (next free id by grep) declaring the three roots and the roots-table edit. Not here: any census content; any src/ file.
Read first: the methodology's 00 prompt and templates; the pilot README; the hygiene files' tails.
Write: the workspace; the two hygiene files.
Constraints: sources read-only; no DRIVER_SCRIPT.md and no _ACT_STATE.md are generated in the new workspace (the methodology's driver template is not instantiated; the run-batch skill is the procedure); no test, no build, no browser; the Dashboard hygiene verdict shows zero violations after the roots are declared (seeded indexes, floor 0); CRLF for package files; no push.
Questions: proposed Q-B6a-<nn> rows; continue.
If the context runs short: commit what folds green, stop; restart as B6a-1-r2.
Done when: the workspace exists with the required files; the verdict is green; one commit; the final message names it and the D-id.
Commit line: rework: B6a-1 - Design_Migration_V1 workspace bootstrapped; roots declared; D-<date>-<nn>
```

**Watch:** a root declared whose folder lacks `INDEX.md`; a pin copied as values instead of a pointer.

#### `B6a-2` — census (01, 01a)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** Dashboard, in place · **Precondition:** `B6a-1` · **Writes:** workspace `01_*` files · **Waits:** —

```text
B6a-2 — the Dashboard census
Re-issue the mechanical design census (01) and the function/UI census (01a) at the current commit, starting from lane A9's static draft, with the Kit's static checks as the detector.
Context: step B6a-2 of the GUI rework runbook (§3); rules: kickoff §2; the input: AUDIT_gui-current-state-dashboard_2026-10-13.md §7.1-§7.6 (the census draft, the 13 routes, the 42 operations, the unconsumed role layer, the drift facts); the methodology prompts 01 and 01a and the FUNCTION_UI_CENSUS_TEMPLATE; the Kit's static checks installed at B5-4, their output quoted into the census file (never a cited report outside it).
Where: the Dashboard submodule on main, in place; one commit.
Scope: the two census files in the methodology's shape; every CM-* candidate of A9's §2 confirmed or dropped by hand; the role-layer gap, the dark-theme gap and the generated-CSS-versus-canon state after B5-3 measured and stated; the literal counts from the Kit's check. Not here: any fix; any screenshot (DV rows proposed instead).
Read first: the A9 audit sections; the two prompts and the template; src/app/router.tsx and routes.ts; the Server route modules by listing.
Write: the census files and their INDEX lines.
Constraints: sources read-only; the Kit's node checks only; no build, no browser, no test; CRLF; no push.
Questions: proposed Q-B6a-<nn> rows; continue.
If the context runs short: commit the census as far as filled with "not measured" rows, stop; restart as B6a-2-r2.
Done when: both files complete; one commit; the final message names it and the DV rows it proposes.
Commit line: rework: B6a-2 - Dashboard census 01/01a - <routes> routes, <ops> operations, <gaps> CM candidates
```

**Watch:** a census that cites a screenshot nobody took.

#### `B6a-3` — screen contracts and target normalisation (02, 04)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** Dashboard, in place · **Precondition:** `B6a-2` · **Writes:** workspace `02_*`, `04_*`; `03_*` as "unavailable in Phase B" · **Waits:** —

```text
B6a-3 — screen contracts and the normalised target
Write one screen contract per route (roles and Gallery ids per region) from the existing SharedContracts page contracts and the Configuration, normalise the target, and record 03 capture as deferred.
Context: step B6a-3 of the GUI rework runbook (§3); rules: kickoff §2; inputs: the census (B6a-2, by pointer), AUDIT_gui-current-state-dashboard_2026-10-13.md §7.4 (routes against the 11 desktop-web page contracts; /login without one; the settings and plant-detail drift), PlantLibrary_SharedContracts/page-contracts/desktop-web/*, the Configuration's roles; the methodology prompts 02, 03, 04.
Where: the Dashboard submodule on main, in place; one commit.
Scope: 13 contracts (one per route, /login included as new); 04's normalised target table; 03 recorded as "capture deferred: rule 1" with the DV rows DVC-A9D-01/02 named by id. Not here: a page contract edit in SharedContracts (B6a-6's IA decides the route drift, Q-A9D-06); any src/ change.
Read first: the prompts; the page contracts; the census.
Write: the workspace files and INDEX lines.
Constraints: as B6a-2.
Questions: proposed Q-B6a-<nn> rows; continue.
If the context runs short: commit the contracts written, list the rest, stop; restart as B6a-3-r2.
Done when: 13 contracts and the target; one commit; the final message names it.
Commit line: rework: B6a-3 - Dashboard screen contracts 02; target 04; capture 03 deferred
```

#### `B6a-4` — comparison and gap map (05, 06)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** Dashboard, in place · **Precondition:** `B6a-3` · **Writes:** workspace `05_*`, `06_*` · **Waits:** —

```text
B6a-4 — the static comparison and the gap map
Compare source and contracts against the normalised target (no visual leg) and write the gap map with its severity and class columns.
Context: step B6a-4 of the GUI rework runbook (§3); rules: kickoff §2; inputs: B6a-2 and B6a-3 by pointer; the methodology prompts 05 and 06 and the gap-map template; AUDIT_gui-current-state-dashboard_2026-10-13.md §2 findings F-A9D-01…20 as candidate gaps.
Where: the Dashboard submodule on main, in place; one commit.
Scope: 05's comparison table (source and contracts only; the visual column reads "deferred: DVC-A9D-01"); 06's gap map; each A9 finding placed or dismissed with a reason. Not here: any fix.
Read first: the prompts and template; the three earlier workspace files.
Write: the two files and INDEX lines.
Constraints: as B6a-2.
Questions: proposed Q-B6a-<nn> rows; continue.
If the context runs short: commit, stop; restart as B6a-4-r2.
Done when: the gap map is complete; one commit; the final message names it.
Commit line: rework: B6a-4 - Dashboard comparison 05 and gap map 06 - <n> gaps
```

#### `B6a-5` — forward surface and information model (06a); gate `G-a-1`

**Model · reasoning:** Opus 5.5 · xhigh · **Route:** session (headless), then gate · **Where:** Dashboard, in place · **Precondition:** `B6a-4` · **Writes:** workspace `06a_*` · **Waits:** — (the gate's answer is recorded in `B6a-6`'s precondition as `event:G-a-1`)

```text
B6a-5 — the Dashboard forward surface and information model
Class every open Dashboard V1 row as reserve / absorbed / no-UI, classify the settings, and write the information model the IA will rest on; put the result to the operator as gate G-a-1.
Context: step B6a-5 of the GUI rework runbook (§3); rules: kickoff §2; inputs: the gap map (B6a-4), AUDIT_batch-packages_2026-10-13.md §7.3 (the Dashboard rows and the relation B6 has to each), AUDIT_gui-current-state-dashboard_2026-10-13.md §7.6 (§2 tier-1 candidates, §3 subsystems), the methodology prompt 06a and its template; the question Q-A7-08 (functional screen rows stay functional).
Where: the Dashboard submodule on main, in place; one commit.
Scope: the forward-surface table (every open row of PlantLibrary_Dashboard/implementation/System_V1_Implementation/TASK_CHECKLIST.md with a UI effect; status untouched), the settings classification, the information model, and the gate section listing the decisions the operator takes at G-a-1 with (a) recommendations. Not here: the IA (B6a-6); any row edit.
Read first: the prompt and template; the gap map; the checklist rows.
Write: the file and its INDEX line.
Constraints: as B6a-2; no row cell changed.
Questions: the gate's decisions are the step's output, not Q rows; anything else as proposed Q-B6a-<nn> rows.
If the context runs short: commit, stop; restart as B6a-5-r2.
Done when: the file is complete and ends with the gate section; one commit; the final message names it and restates the gate's decisions in plain words for the operator.
Commit line: rework: B6a-5 - Dashboard forward surface and information model 06a; G-a-1 put
```

*Orchestrator note:* `G-a-1` is put to the operator (chat or §O session); the answer is recorded in the workspace `STATE.md` by `B6a-6` and quoted in its note.

#### `B6a-6` — IA and mockups (06b), mockup audit (06c); gates `G-a-2`, `G-a-3`

**Model · reasoning:** Opus 5.5 · xhigh · **Route:** session (headless) · **Where:** Dashboard, then `PlantLibrary_SharedContracts` on `main` (serialized) · **Precondition:** `B6a-5`, `event:G-a-1` · **Writes:** workspace `06b_*`, `06c_*`; SharedContracts `design/contracts/{pages,patterns}/**`, `design/gallery/pages/**`, `design/gallery/fixtures/**`, `DESIGN_VERSION.md` · **Waits:** Q-A9D-06

```text
B6a-6 — the Dashboard IA, the page and pattern contracts, the mockups, the mockup audit
Write the information architecture first and put it to the operator (G-a-2); then author the page and pattern contracts and the fixture-driven page mockups into the Configuration as static HTML (the round-6 mockup kit's authoring shape), step the Configuration version, run the mechanical and rubric legs of the mockup audit, and put the audit to the operator who opens the HTML (G-a-3).
This block runs as two sessions (B6a-6a, then B6a-6b): session a does everything up to the gate G-a-2, ends with the gate's decisions in its final message and stops; session b starts only after event:G-a-2 (the operator's words recorded in the workspace STATE.md by the orchestrator) and does the rest; both sessions paste this same block and say which part they are in their first line.
Context: step B6a-6 of the GUI rework runbook (§3); rules: kickoff §2; the answers: G-a-1 (workspace STATE.md), Q-A9D-06 (master §Q); inputs: 06a (B6a-5), AUDIT_design-kit-and-methodology_2026-10-13.md §7.5 (what of the round-6 tooling transfers: the mockup kit's AUTHORING.md, BRIEFS.md, kit.js, data.js, pages.css — read-only at C:\Programmierung\Conductor_GUI_Reconciliation_2026-10-12\mockups\; shot.py and sweep.py do not transfer), the methodology prompts 06b and 06c; the Kit's gallery-governance skill for the Gallery-first rule.
Where: the Dashboard workspace for 06b's IA and 06c's audit; SharedContracts for the contracts, mockups, fixtures and the version step; one commit per repository; SharedContracts is written only when no other step writes it (the orchestrator confirms in the note).
Scope: the IA (page tree, navigation, the route drift resolved per Q-A9D-06); the contracts under design/contracts/; the mockups under design/gallery/pages/ with fixtures, authored from the generated tokens.css and the gallery's pages.css, no build; DESIGN_VERSION.md stepped (minor) with the Consumers line — the clients' pins hash only the four core files, so a step that changes no core file needs no re-pin, and if the gate's contracts require a core change the client re-syncs in its first -8 batch as a row; 06c's mechanical leg (the Kit's checks over the mockup files) and rubric leg written; the operator's review recorded as G-a-3. Not here: a screenshot or a browser run (DV rows); any src/ change.
Read first: the prompts; the round-6 AUTHORING.md and BRIEFS.md; the Gallery's structure in SharedContracts design/gallery/; the Configuration's contracts folder.
Write: the files listed.
Constraints: sources read-only; the Kit's static checks only; no browser, no build, no test; LF for Configuration files, CRLF for workspace files; the SharedContracts verdict unchanged; no push.
Questions: G-a-2 and G-a-3 are the step's outputs; anything else as proposed Q-B6a-<nn> rows.
If the context runs short: commit the IA (Dashboard) and whatever Configuration files validate, list the rest, stop; restart as B6a-6-r2.
Done when: the IA is recorded with G-a-2's words; the contracts and mockups exist and the mechanical leg passes; G-a-3 is put; two commits; the final message names them.
Commit line: rework: B6a-6 - Dashboard IA 06b; contracts and mockups; mockup audit 06c; G-a-2/3
```

*Orchestrator note:* SharedContracts occupancy is granted here explicitly; the superproject lines are two (`bump PlantLibrary_Dashboard gitlink`, `bump PlantLibrary_SharedContracts gitlink`).
**Watch:** mockups rendered by a tool (the round-6 render tools need a browser — deferred); a token value typed into a mockup.

#### `B6a-7` — change classification (06d); plan-batch (07); SCOPE (08); gate `G-a-4`

**Model · reasoning:** Opus 5.5 · xhigh for 06d; the `/plan-batch` act Opus 5.5 · high · **Route:** session (headless), then plan · **Where:** Dashboard, in place · **Precondition:** `B6a-6`, `event:G-a-3` · **Writes:** workspace `06d_*`; `implementation/Design_Migration_V1/{BATCH_PLAN,TASK_CHECKLIST,TASK_CONTEXT,STATE}.md` (new rows and batches — Q-A7-08 (a), G-a-4 item 2, Q-B6a-19 (a), corrected 2026-10-14); V1 `TASK_CONTEXT.md` anchor notes, `STATE.md` supersession lines and the traceability rows only; workspace `SCOPE.md` · **Waits:** Q-A9D-03, Q-A7-08

```text
B6a-7 — the Dashboard change classification and the batches
Classify every change the gap map and the mockup audit imply as bugfix / additive-silent / amendment / already-owned, draft the amendment in PlantLibrary's format, cut the waves, put them to the operator (G-a-4), then write the rows and batches through plan-batch and the workspace SCOPE.
This block runs as two sessions (B6a-7a, then B6a-7b): session a does everything up to the gate G-a-4, ends with the gate's decisions in its final message and stops; session b starts only after event:G-a-4 (the operator's words recorded in the workspace STATE.md by the orchestrator) and does the rest; both sessions paste this same block and say which part they are in their first line.
Context: step B6a-7 of the GUI rework runbook (§3); rules: kickoff §2 (rule 4: plan-batch's schema; existing validation cells untouched; supersessions as STATE decisions); the answers: Q-A9D-03, Q-A7-08 (master §Q), G-a-3; inputs: 06c (B6a-6), AUDIT_batch-packages_2026-10-13.md §7.3 (which rows B6 supersedes or absorbs: WD-V1-DS-01/02/03/05/06; which it leaves), AUDIT_gui-current-state-dashboard_2026-10-13.md §0 items 3, 5 (the alias layer, Q-A9D-04), the methodology prompts 06d, 07, 08; the Dashboard's plan-batch skill.
Where: the Dashboard submodule on main, in place; two commits (06d + G-a-4; then plan-batch + SCOPE).
Scope: 06d's classification and amendment; the waves; G-a-4 put and recorded; the /plan-batch act into the V1 package (new rows whose validation cells the plan-batch skill authors from the row schema and the methodology's templates; every leg that needs a running app is carried as a deferred row by DV id; the superseded rows deferred with dated STATE lines; the alias-layer row per Q-A9D-04 first); the workspace SCOPE.md. Not here: any implementation; any validation.
Read first: the prompts; 06c; the package's five files; the plan-batch skill in full (its self-review through the batch-plan-auditor agent, in the foreground).
Write: the files listed.
Constraints: no test; CRLF; the census after the act reads 0 errors; the Dashboard verdict unchanged; no push.
Questions: G-a-4 is the step's output; others as proposed Q-B6a-<nn> rows.
If the context runs short: commit 06d, stop; restart as B6a-7-r2 for the plan-batch act.
Done when: the rows and batches exist; G-a-4 recorded; two commits; the final message names them and the batch keys in order.
Commit line: rework: B6a-7 - Dashboard change classification 06d; <n> rows in <m> batches; SCOPE 08
```

**Watch:** a validation cell that names a browser run as a Phase B proof (it is a deferred row); a renumbered id.

#### `B6a-8` — implementation of the classified changes, batch by batch

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless), one per batch · **Where:** Dashboard, in place · **Precondition:** `B6a-7`, `event:G-a-4` · **Writes:** `src/**`, `scripts/generate-theme.mjs` (fate per the alias row), `design/conformance/CONFORMANCE_MATRIX.md`, package `STATE.md`/`TASK_CHECKLIST.md` (statuses of the new rows) · **Waits:** Q-A9D-04, Q-R-01

```text
B6a-8 — one Dashboard batch implemented with mechanical checks only
Implement the rows of the batch named in the first line of your launch message with the mechanical checks Q-G-04 (a) admits, record every visual leg as a deferred row, and leave the package honest: a row's status is what the plan-batch status set allows for work whose named validation has not run.
Context: step B6a-8 of the GUI rework runbook (§3), one session per batch, the batch key in the orchestrator note; rules: kickoff §2 (rule 1: no browser, no build beyond the type check Q-G-04 (a) admits; rule 4); the answers: Q-A9D-04 and G-a-4; the package: PlantLibrary_Dashboard/implementation/Design_Migration_V1 (the batch's rows, their validation cells as the Phase B legs; corrected 2026-10-14 per Q-B6a-19 (a) — the V1 package receives notes and STATE lines only); the Kit's design-gate skill (run before touching a rendered surface) and design-audit (after); AUDIT_gui-current-state-dashboard_2026-10-13.md §7.7 (the mechanical checks it names).
Where: the Dashboard submodule on main, in place; one commit per batch.
Scope: the batch's rows only; the design gate before the first edit; the design audit over the touched paths after; the mechanical checks Q-G-04 (a) admits on the touched files; the conformance matrix rows updated; row statuses per Q-R-01: a row is done only when its validation cell is fully met by the admitted checks, else it keeps the status the plan-batch status set allows for implemented-but-unvalidated work, with a dated STATE line naming its deferred row. Not here: any other batch; any browser; any screenshot; any status the skills do not allow.
Read first: the batch's rows and anchors; the design-gate skill; the alias-layer decision.
Write: the files the rows name; the package status cells and STATE lines.
Constraints: sources read-only; no test, no browser, no production build (the type check only); design-audit green on the touched paths; CRLF/LF as found; the Dashboard verdict unchanged; no push.
Questions: proposed Q-B6a-<nn> rows; continue.
If the context runs short: commit the rows complete with their statuses, list the rest, stop; restart as B6a-8-r<k> for the same batch.
Done when: every row of the batch is done or honestly left; the audit is green; one commit; the final message names it, the row statuses and the deferred rows.
Commit line: rework: B6a-8 <the batch key from the launch message> - <rows> rows - mechanical checks
```

*Orchestrator note:* the batch key and its Requires state are launch values, given in the first line of the launch message. This is a runbook step under kickoff rule 4: it implements rows and records what it could not prove; a row closes only on its named validation, which Phase C runs, and the status rule is Q-R-01's answer.
**Watch:** a row set done on a validation that did not run; a drift-checker run against an unamended ban list.

## 4. Lane `B6c` — PyApp

#### `B6c-1` — workspace bootstrap (00)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development\PlantLibrary_PyApp` on `main` (in place) · **Precondition:** `B5-5`, `R-4.2` · **Writes:** `implementation/Design_Migration_V1/**`, the two hygiene files · **Waits:** Q-A4-06, Q-A9P-09

```text
B6c-1 — the PyApp design-migration workspace
Bootstrap PyApp's design-migration workspace from the methodology 4.1.0 templates, pinned to the BINDING Configuration through design/conformance/CONSUMED_DESIGN.md, with the re-skin decision (Q-A9P-09) and the adapter route (B5-5's mapping.md, by pointer) recorded in STATE.md.
Context: step B6c-1 of C:\Programmierung\SW_Development\rework\PROMPTS_gui-rework-runbook_2026-10-13.md (§4); rules: kickoff §2; the answers: Q-A4-06, Q-A9P-09 (master §Q); the layout: AUDIT_design-kit-and-methodology_2026-10-13.md §7.5; the pilot README (read-only); the methodology's 00 prompt and templates; the history note of AUDIT_gui-current-state-pyapp_2026-10-13.md (the methodology was first derived from PyApp work: name in the README what still applies).
Where: the PyApp submodule on main, in place; one commit.
Scope: the workspace with the required files and hierarchy v4; the D-entry (next free id by grep) declaring planning/, proposal/, handovers/ with seeded INDEX.md and the roots-table edit. Not here: census content; any app/ or resources/ file.
Read first: the 00 prompt and templates; the pilot README; the hygiene files' tails; B5-5's mapping.md.
Write: the workspace; the two hygiene files.
Constraints: sources read-only; no DRIVER_SCRIPT.md and no _ACT_STATE.md are generated in the new workspace (the methodology's driver template is not instantiated; the run-batch skill is the procedure); no test, no app launch; the PyApp verdict green after the declaration; CRLF; no push.
Questions: proposed Q-B6c-<nn> rows; continue.
If the context runs short: commit what folds green, stop; restart as B6c-1-r2.
Done when: the workspace exists; the verdict is green; one commit; the final message names it and the D-id.
Commit line: rework: B6c-1 - PyApp Design_Migration_V1 workspace bootstrapped; roots declared; D-<date>-<nn>
```

#### `B6c-2` — census (01, 01a)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** PyApp, in place · **Precondition:** `B6c-1` · **Writes:** workspace `01_*` · **Waits:** —

```text
B6c-2 — the PyApp census
Re-issue the mechanical design census (01) at the current commit from lane A9's draft — 164 hex literals in design_tokens.py, 0 in QSS, the 18 files bypassing the role layer, the 126 px literals, the sub-scale font sizes — with the Kit's literal check as the detector over app/gui/**/*.py and resources/styles/*.qss; 01a as input only (re-skin), its pass-A totals re-measured by name match.
Context: step B6c-2 of the GUI rework runbook (§4); rules: kickoff §2; inputs: AUDIT_gui-current-state-pyapp_2026-10-13.md §7.1-§7.6; the methodology prompts 01 and 01a; the Kit's static checks installed at B5-5, their output quoted into the census file.
Where: the PyApp submodule on main, in place; one commit.
Scope: the 01 census file complete; the 01a header and pass-A table as the re-skin's input; the PRIMARY-versus-canon table and the 26 DARK_THEME role differences restated at this commit. Not here: any fix; any app import or launch; screenshots (DV-A9P-01 by id).
Read first: the audit sections; the prompts; app/gui/design_tokens.py and theme_utils.py (read, not changed).
Write: the census files and INDEX lines.
Constraints: sources read-only; the Kit's static checks and plain text scans only; no app import; CRLF; no push.
Questions: proposed Q-B6c-<nn> rows; continue.
If the context runs short: commit the census as filled, stop; restart as B6c-2-r2.
Done when: 01 complete, 01a input recorded; one commit; the final message names it.
Commit line: rework: B6c-2 - PyApp census 01/01a - <literals> literals, <bypass> role-bypass files
```

#### `B6c-3` — screen contracts and target normalisation (02, 04)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** PyApp, in place · **Precondition:** `B6c-2` · **Writes:** workspace `02_*`, `04_*`, `03_*` (deferred note) · **Waits:** Q-A9P-07

```text
B6c-3 — PyApp screen contracts and the normalised target
Write one contract per view, dialog and wizard step from the desktop-web page contracts and the suite's own GUI/screen_structures/ set (the design targets per Q-A9P-07: contracts and Gallery, the V3 mockups as history only), normalise the target, record 03 capture as deferred (DV-A9P-01).
Context: step B6c-3 of the GUI rework runbook (§4); rules: kickoff §2; the answer: Q-A9P-07; inputs: AUDIT_gui-current-state-pyapp_2026-10-13.md §7.4 (11 views, 1 wizard of 6 steps, 14 dialogs; the 31 screen structures), PlantLibrary_SharedContracts/page-contracts/desktop-web/*, PlantLibrary_PyApp/GUI/screen_structures/*; the prompts 02, 03, 04.
Where: the PyApp submodule on main, in place; one commit.
Scope: the contracts; 04's target; 03 deferred. Not here: any GUI file; any capture.
Read first: the prompts; the contracts and screen structures; the census.
Write: the workspace files and INDEX lines.
Constraints: as B6c-2.
Questions: proposed Q-B6c-<nn> rows; continue.
If the context runs short: commit the contracts written, stop; restart as B6c-3-r2.
Done when: every view, dialog and wizard step has a contract; one commit; the final message names it.
Commit line: rework: B6c-3 - PyApp screen contracts 02; target 04; capture 03 deferred
```

#### `B6c-4` — comparison and gap map (05, 06)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** PyApp, in place · **Precondition:** `B6c-3` · **Writes:** workspace `05_*`, `06_*` · **Waits:** —

```text
B6c-4 — the PyApp static comparison and gap map
Compare source and contracts against the normalised target with no visual leg, and write the gap map; every A9 finding (F-A9P-01…) is placed or dismissed with a reason, the 124 composed role keys are one gap row for the adapter decision.
Context: step B6c-4 of the GUI rework runbook (§4); rules: kickoff §2; inputs: B6c-2, B6c-3 by pointer; AUDIT_gui-current-state-pyapp_2026-10-13.md §2 and §7.7; the prompts 05 and 06 and the gap-map template.
Where: the PyApp submodule on main, in place; one commit.
Scope: 05 (visual column "deferred: DV-A9P-01"); 06. Not here: any fix.
Read first: the prompts; the earlier workspace files.
Write: the two files and INDEX lines.
Constraints: as B6c-2.
Questions: proposed Q-B6c-<nn> rows; continue.
If the context runs short: commit, stop; restart as B6c-4-r2.
Done when: the gap map is complete; one commit; the final message names it.
Commit line: rework: B6c-4 - PyApp comparison 05 and gap map 06 - <n> gaps
```

#### `B6c-5` — forward surface and information model (06a); gate `G-c-1`

**Model · reasoning:** Opus 5.5 · xhigh · **Route:** session (headless), then gate · **Where:** PyApp, in place · **Precondition:** `B6c-4` · **Writes:** workspace `06a_*` · **Waits:** —

```text
B6c-5 — the PyApp forward surface and information model
Class every open PyApp V1 row with a UI effect as reserve / absorbed / no-UI (PY-V1-UX-01..03 functional and kept per Q-A7-08; PY-V1-DS-01/02/03 per AUDIT_batch-packages §7.3), classify the eight settings tabs, write the information model, and put the decisions to the operator as G-c-1.
Context: step B6c-5 of the GUI rework runbook (§4); rules: kickoff §2; inputs: the gap map (B6c-4), AUDIT_batch-packages_2026-10-13.md §7.3 (PyApp rows), AUDIT_gui-current-state-pyapp_2026-10-13.md §7.6 (the 06a inputs: forward rows, the settings tabs, the page tree, the provenance markers); the prompt 06a and template.
Where: the PyApp submodule on main, in place; one commit.
Scope: the forward-surface table (statuses untouched), the settings classification, the information model, the gate section with (a) recommendations. Not here: the IA; any row edit.
Read first: the prompt and template; the gap map; the checklist rows.
Write: the file and INDEX line.
Constraints: as B6c-2; no row cell changed.
Questions: the gate decisions are the output; others as proposed Q-B6c-<nn> rows.
If the context runs short: commit, stop; restart as B6c-5-r2.
Done when: the file ends with the gate section; one commit; the final message restates the gate's decisions in plain words.
Commit line: rework: B6c-5 - PyApp forward surface and information model 06a; G-c-1 put
```

#### `B6c-6` — IA and mockups (06b), mockup audit (06c); gates `G-c-2`, `G-c-3`

**Model · reasoning:** Opus 5.5 · xhigh · **Route:** session (headless) · **Where:** PyApp, then SharedContracts (serialized, after `B6a-6`) · **Precondition:** `B6c-5`, `event:G-c-1`, `B6a-6` · **Writes:** workspace `06b_*`, `06c_*`; SharedContracts `design/contracts/**`, `design/gallery/pages/**`, `design/gallery/fixtures/**`, `DESIGN_VERSION.md` · **Waits:** —

```text
B6c-6 — the PyApp IA, contracts, mockups and mockup audit
Write the IA for the desktop client and put it to the operator (G-c-2); author the page and pattern contracts and the fixture-driven page mockups into the Configuration as static HTML (desktop variants beside the Dashboard's, the Gallery-first rule), step the Configuration version, run the mechanical and rubric legs of the mockup audit, and put it to the operator (G-c-3).
This block runs as two sessions (B6c-6a, then B6c-6b): session a does everything up to the gate G-c-2, ends with the gate's decisions in its final message and stops; session b starts only after event:G-c-2 (the operator's words recorded in the workspace STATE.md by the orchestrator) and does the rest; both sessions paste this same block and say which part they are in their first line.
Context: step B6c-6 of the GUI rework runbook (§4); rules: kickoff §2; the answer: G-c-1 (workspace STATE.md); inputs: 06a (B6c-5), the Dashboard's contracts and mockups as landed at B6a-6 (by pointer; a shared page gets a desktop variant, not a copy), the round-6 mockup kit's AUTHORING.md and BRIEFS.md (read-only), the prompts 06b and 06c, the gallery-governance skill.
Where: the PyApp workspace for the IA and the audit; SharedContracts for the Configuration writes, only when the orchestrator grants occupancy; one commit per repository.
Scope: the IA (view tree, sidebar order, dialogs; the "Follow system setting" theme question Q-A9P-03 carried as an IA item); the contracts and mockups; DESIGN_VERSION.md stepped; 06c's two static legs; G-c-3 put and recorded. Not here: a Qt render or screenshot (DV rows); any app file.
Read first: the prompts; the Dashboard's landed contracts; AUTHORING.md; the Gallery structure.
Write: the files listed.
Constraints: as B6a-6.
Questions: G-c-2 and G-c-3 are the outputs; others as proposed Q-B6c-<nn> rows.
If the context runs short: commit the IA and the validated Configuration files, list the rest, stop; restart as B6c-6-r2.
Done when: the IA recorded with G-c-2's words; the contracts and mockups exist and the mechanical leg passes; G-c-3 put; two commits; the final message gives the §L row and the commit the gitlink takes.
Commit line: rework: B6c-6 - PyApp IA 06b; contracts and mockups; mockup audit 06c; G-c-2/3
```

#### `B6c-7` — change classification (06d); plan-batch (07); SCOPE (08); gate `G-c-4`

**Model · reasoning:** Opus 5.5 · xhigh for 06d; the `/plan-batch` act Opus 5.5 · high · **Route:** session (headless), then plan · **Where:** PyApp, in place · **Precondition:** `B6c-6`, `event:G-c-3` · **Writes:** workspace `06d_*`; `implementation/Design_Migration_V1/{BATCH_PLAN,TASK_CHECKLIST,TASK_CONTEXT,STATE}.md` (new rows and batches — Q-A7-08 (a), G-c-4 item 2, Q-B6c-21 (a), corrected 2026-10-14); the V1 package receives the anchor notes, the DS-row supersession lines and statuses, the eight DV rows' `requirements` cells (CC-78) and the one engineering row (CC-80) only; workspace `SCOPE.md` · **Waits:** Q-A9P-02, Q-A7-08 (Q-A9P-08 is recorded at `B5-3`)

```text
B6c-7 — the PyApp change classification and the batches
Classify every change as bugfix / additive-silent / amendment / already-owned, draft the amendment, cut the waves, put them to the operator (G-c-4); then write the rows and batches through plan-batch and the workspace SCOPE — with the adapter (B5-5's route) as the first batch, the role-layer migration of the 18 bypassing files second, the dark-theme roles third, the defects (missing check-white.svg, the theme mapping, the off-scale radii and sub-scale sizes) as bugfix rows.
This block runs as two sessions (B6c-7a, then B6c-7b): session a does everything up to the gate G-c-4, ends with the gate's decisions in its final message and stops; session b starts only after event:G-c-4 (the operator's words recorded in the workspace STATE.md by the orchestrator) and does the rest; both sessions paste this same block and say which part they are in their first line.
Context: step B6c-7 of the GUI rework runbook (§4); rules: kickoff §2 (rule 4; PyApp's plan contract: instance 2 holds PY1-B08 — the V1 package's batch order, goals, Model lines, primary rows and Requires are not changed; new rows and batches are appended after the existing ones, or, if plan-batch's amendment rule cannot append without moving the contract, the rows go into the workspace package and a re-intake item is proposed for B8); the answers: Q-A9P-02, Q-A9P-08, Q-A7-08, G-c-3; inputs: 06c, AUDIT_batch-packages_2026-10-13.md §7.3 (PyApp rows), AUDIT_gui-current-state-pyapp_2026-10-13.md §0 items 2-4, 6; the prompts 06d, 07, 08; the PyApp plan-batch skill.
Where: the PyApp submodule on main, in place; two commits.
Scope: 06d; G-c-4; the plan-batch act (validation cells authored by the plan-batch skill from the row schema; every leg that needs the running app carried as a deferred row by DV id); the PY-V1-DS-01/02/03 supersessions as STATE lines; SCOPE 08 listing resources/styles/*.qss as touchable and the harness refusal (Q-A9P-04) as a standing note. Not here: implementation.
Read first: the prompts; 06c; the package's five files; the plan-batch skill (self-review through the batch-plan-auditor agent in the foreground); the parser's plan-contract hash before (quoted) and after.
Write: the files listed.
Constraints: no test; CRLF; census 0 errors; the plan-contract hash unchanged or the PyApp stop reported; no push.
Questions: G-c-4 is the output; others as proposed Q-B6c-<nn> rows.
If the context runs short: commit 06d, stop; restart as B6c-7-r2 for the act.
Done when: rows and batches exist (or the stop is reported with the re-intake item); G-c-4 recorded; two commits; the final message gives the §L row and the commit the gitlink takes.
Commit line: rework: B6c-7 - PyApp change classification 06d; <n> rows in <m> batches; SCOPE 08
```

**Watch:** a plan-contract hash that moves (instance 2 refuses the retry; the step stops and reports).

#### `B6c-8` — implementation of the classified changes, batch by batch

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless), one per batch · **Where:** PyApp, in place · **Precondition:** `B6c-7`, `event:G-c-4` · **Writes:** `app/gui/**`, `resources/styles/*.qss`, `design/conformance/CONFORMANCE_MATRIX.md`, package status cells and `STATE.md` · **Waits:** Q-A9P-03, Q-A9P-04, Q-A9P-05, Q-R-01

```text
B6c-8 — one PyApp batch implemented with mechanical checks only
Implement the rows of the batch named in the first line of your launch message — the adapter in theme_utils.py over the emitted tokens.py first, design_tokens.py re-exporting generated data until its importers migrate, then the role-layer and dark-theme rows, then the bugfix rows — with the mechanical checks Q-G-04 (a) admits, record every visual leg as a deferred row, and keep the package honest (statuses per Q-R-01).
Context: step B6c-8 of the GUI rework runbook (§4), one session per batch, the key in the orchestrator note; rules: kickoff §2 (rule 1: no app launch, no Qt, no screenshot; rule 4); the answers: Q-A9P-03, Q-A9P-04, Q-A9P-05, G-c-4; the package rows; the design-gate skill before, design-audit after; AUDIT_gui-current-state-pyapp_2026-10-13.md §7.7 (the adapter shape, the units rule, the flattening rule, the allow-listed files, the closeout coupling).
Where: the PyApp submodule on main, in place; one commit per batch.
Scope: the batch's rows only; design gate before the first edit; design audit over touched paths after; the admitted mechanical checks on touched files; a syntax parse of every changed module; the conformance matrix; row statuses per Q-R-01 with a dated STATE line per row naming its deferred row (every QSS-touching batch proposes the harness row of Q-A9P-04 by id until settled). Not here: any other batch; any run of the app.
Read first: the batch's rows and anchors; the design-gate skill; B5-5's mapping.md.
Write: the files the rows name; the package status cells and STATE lines.
Constraints: sources read-only; no test, no app import; design-audit green; line endings as found (pyproject.toml and .gitignore are mixed: byte-exact substitution, never the Edit tool — Q-B6b-42 (a), corrected 2026-10-14); the PyApp verdict unchanged; no push.
Questions: proposed Q-B6c-<nn> rows; continue.
If the context runs short: commit the complete rows with statuses, stop; restart as B6c-8-r<k>.
Done when: every row done or honestly left; the audit green; one commit; the final message names it, the statuses and the deferred rows.
Commit line: rework: B6c-8 <the batch key from the launch message> - <rows> rows - mechanical checks
```

**Watch:** a QSS edited by a text tool that changes its endings; a value transcribed by hand into design_tokens.py (the adapter derives, never copies).

## 5. Lane `B6b` — AndroidApp

#### `B6b-1` — workspace bootstrap (00)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** `C:\Programmierung\SW_Development\PlantLibrary_AndroidApp` on `main` (in place) · **Precondition:** `B5-6`, `R-4.2` · **Writes:** `implementation/Design_Migration_V1/**`, the two hygiene files · **Waits:** Q-A4-06, Q-A9A-07

```text
B6b-1 — the AndroidApp design-migration workspace
Bootstrap the AndroidApp's design-migration workspace from the methodology 4.1.0 templates, pinned to the BINDING Configuration through design/conformance/CONSUMED_DESIGN.md, with the restructure-or-re-skin decision (Q-A9A-07) and the Kit-session dependency (Q-A4-05, by id) recorded in STATE.md.
Context: step B6b-1 of C:\Programmierung\SW_Development\rework\PROMPTS_gui-rework-runbook_2026-10-13.md (§5); rules: kickoff §2; the answers: Q-A4-06, Q-A9A-07; the layout: AUDIT_design-kit-and-methodology_2026-10-13.md §7.5; the pilot README (read-only); the 00 prompt and templates.
Where: the AndroidApp submodule on main, in place; one commit.
Scope: the workspace; the D-entry declaring the three roots with seeded INDEX.md and the roots-table edit. Not here: census; any Kotlin or Gradle file.
Read first: the 00 prompt and templates; the pilot README; the hygiene tails; B5-6's mapping.md.
Write: the workspace; the two hygiene files.
Constraints: sources read-only; no DRIVER_SCRIPT.md and no _ACT_STATE.md are generated in the new workspace (the methodology's driver template is not instantiated; the run-batch skill is the procedure); no Gradle, no emulator, no test; the AndroidApp verdict green after the declaration; CRLF; no push.
Questions: proposed Q-B6b-<nn> rows; continue.
If the context runs short: commit what folds green, stop; restart as B6b-1-r2.
Done when: the workspace exists; the verdict green; one commit; the final message names it and the D-id.
Commit line: rework: B6b-1 - AndroidApp Design_Migration_V1 workspace bootstrapped; roots declared; D-<date>-<nn>
```

#### `B6b-2` — census (01, 01a)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** AndroidApp, in place · **Precondition:** `B6b-1` · **Writes:** workspace `01_*` · **Waits:** Q-A9A-03

```text
B6b-2 — the AndroidApp census
Re-issue the mechanical design census (01) at the current commit from lane A9's draft — the hand mirror's 59/26/49 split against the canon, the six banned-green lines, the 82 raw dp literals, the 17 of the Material3 colour roles set — using the interim Kotlin literal scan Q-A9A-03 admits (plain text patterns for Color(0x…) and N.dp, since the Kit's check is blind to them), and 01a (61 repository operations, 47 reached, the four capability-missing candidates) re-measured.
Context: step B6b-2 of the GUI rework runbook (§5); rules: kickoff §2; the answer: Q-A9A-03; inputs: AUDIT_gui-current-state-androidapp_2026-10-13.md §7.1-§7.6; the prompts 01 and 01a; the Kit checks installed at B5-6 (quoted with their Kotlin blindness stated).
Where: the AndroidApp submodule on main, in place; one commit.
Scope: 01 and 01a complete; the CM-* candidates confirmed by hand. Not here: any fix; Gradle; the emulator; screenshots (DV-A9A-b, -i, -l by id).
Read first: the audit sections; the prompts; core/design/src/main/java/com/plantlibrary/android/core/design/*.kt (read, not changed); the navigation graph.
Write: the census files and INDEX lines.
Constraints: sources read-only; text scans and the Kit's static checks only; no Gradle; CRLF; no push.
Questions: proposed Q-B6b-<nn> rows; continue.
If the context runs short: commit as filled, stop; restart as B6b-2-r2.
Done when: both files complete; one commit; the final message names it.
Commit line: rework: B6b-2 - AndroidApp census 01/01a - <literals> literals, <ops> operations
```

#### `B6b-3` — screen contracts and target normalisation (02, 04)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** AndroidApp, in place · **Precondition:** `B6b-2` · **Writes:** workspace `02_*`, `04_*`, `03_*` (deferred) · **Waits:** —

```text
B6b-3 — AndroidApp screen contracts and the normalised target
Write one contract per destination (15 views: 3 gate, 5 bottom-nav, 7 pushed) from the five Android page contracts and the approved mockup's four phones, note the route-name drift between contracts and code for the IA, normalise the target, and record 03 capture as deferred (DV-A9A-b).
Context: step B6b-3 of the GUI rework runbook (§5); rules: kickoff §2; inputs: AUDIT_gui-current-state-androidapp_2026-10-13.md §7.4 and §0 item 5; PlantLibrary_SharedContracts/page-contracts/android/*; the approved mockup record in PlantLibrary_Workspace/implementation/System_Design_Architecture; the prompts 02, 03, 04.
Where: the AndroidApp submodule on main, in place; one commit.
Scope: 15 contracts; the drift table; 04's target; 03 deferred. Not here: any Kotlin; any emulator.
Read first: the prompts; the contracts; the census.
Write: the workspace files and INDEX lines.
Constraints: as B6b-2.
Questions: proposed Q-B6b-<nn> rows; continue.
If the context runs short: commit the contracts written, stop; restart as B6b-3-r2.
Done when: 15 contracts and the target; one commit; the final message gives the §L row and the commit the gitlink takes.
Commit line: rework: B6b-3 - AndroidApp screen contracts 02; target 04; capture 03 deferred
```

#### `B6b-4` — comparison and gap map (05, 06)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless) · **Where:** AndroidApp, in place · **Precondition:** `B6b-3` · **Writes:** workspace `05_*`, `06_*` · **Waits:** —

```text
B6b-4 — the AndroidApp static comparison and gap map
Compare source and contracts against the normalised target with no visual leg and write the gap map; the Material3 baseline fallbacks, the light-only launch theme, the background binding (NEUTRAL.50 against the canon's NEUTRAL.100), the icon set (SDA-DEC-04 does not hold) and the raw dp literals are gap rows; every F-A9A-* finding is placed or dismissed.
Context: step B6b-4 of the GUI rework runbook (§5); rules: kickoff §2; inputs: B6b-2, B6b-3; AUDIT_gui-current-state-androidapp_2026-10-13.md §2 and §0 items 3, 4, 9; the prompts 05 and 06.
Where: the AndroidApp submodule on main, in place; one commit.
Scope: 05 (visual column "deferred: DV-A9A-b"); 06. Not here: any fix.
Read first: the prompts; the earlier workspace files.
Write: the two files and INDEX lines.
Constraints: as B6b-2.
Questions: proposed Q-B6b-<nn> rows; continue.
If the context runs short: commit, stop; restart as B6b-4-r2.
Done when: the gap map complete; one commit; the final message gives the §L row and the commit the gitlink takes.
Commit line: rework: B6b-4 - AndroidApp comparison 05 and gap map 06 - <n> gaps
```

#### `B6b-5` — forward surface and information model (06a); gate `G-b-1`

**Model · reasoning:** Opus 5.5 · xhigh · **Route:** session (headless), then gate · **Where:** AndroidApp, in place · **Precondition:** `B6b-4` · **Writes:** workspace `06a_*` · **Waits:** —

```text
B6b-5 — the AndroidApp forward surface and information model
Class every open AndroidApp V1 row with a UI effect (the functional screen rows AN-V1-SHELL/HOME/PLANTS/DETAIL/ADD/CARE/MEDIA/SYNC/SETTINGS/MORE stay functional per Q-A7-08 and are routed as reserve with notes to their anchors; AN-V1-DS-01/02/03/04/05 per AUDIT_batch-packages §7.3), classify the settings, write the information model (bottom-nav order against the approved mockup's), and put the decisions to the operator as G-b-1.
Context: step B6b-5 of the GUI rework runbook (§5); rules: kickoff §2; inputs: the gap map (B6b-4), AUDIT_batch-packages_2026-10-13.md §7.3 (AndroidApp rows), AUDIT_gui-current-state-androidapp_2026-10-13.md §7.6; the prompt 06a and template; Q-A7-08.
Where: the AndroidApp submodule on main, in place; one commit.
Scope: the forward-surface table (statuses untouched), the settings classification, the information model, the gate section. Not here: the IA; any row edit.
Read first: the prompt and template; the gap map; the checklist rows.
Write: the file and INDEX line.
Constraints: as B6b-2; no row cell changed.
Questions: the gate decisions are the output; others as proposed Q-B6b-<nn> rows.
If the context runs short: commit, stop; restart as B6b-5-r2.
Done when: the file ends with the gate section; one commit; the final message restates the decisions.
Commit line: rework: B6b-5 - AndroidApp forward surface and information model 06a; G-b-1 put
```

#### `B6b-6` — IA and mockups (06b), mockup audit (06c); gates `G-b-2`, `G-b-3`

**Model · reasoning:** Opus 5.5 · xhigh · **Route:** session (headless) · **Where:** AndroidApp, then SharedContracts (serialized, after `B6c-6`) · **Precondition:** `B6b-5`, `event:G-b-1`, `B6c-6` · **Writes:** workspace `06b_*`, `06c_*`; SharedContracts `design/contracts/**`, `design/gallery/pages/**`, `design/gallery/fixtures/**`, `DESIGN_VERSION.md` · **Waits:** Q-A9A-05

```text
B6b-6 — the AndroidApp IA, contracts, mockups and mockup audit
Write the IA for the phone client (routes, tab order and nav selection per Q-A9A-05) and put it to the operator (G-b-2); author the page and pattern contracts and the fixture-driven page mockups into the Configuration as static HTML phone variants (the Gallery renders dp as px — stated in each mockup's note), step the Configuration version, run the mechanical and rubric legs of the mockup audit, put it to the operator (G-b-3).
This block runs as two sessions (B6b-6a, then B6b-6b): session a does everything up to the gate G-b-2, ends with the gate's decisions in its final message and stops; session b starts only after event:G-b-2 (the operator's words recorded in the workspace STATE.md by the orchestrator) and does the rest; both sessions paste this same block and say which part they are in their first line.
Context: step B6b-6 of the GUI rework runbook (§5); rules: kickoff §2; the answers: G-b-1, Q-A9A-05; inputs: 06a (B6b-5), the Dashboard's and PyApp's landed contracts (by pointer), the approved mockup's four phones, the round-6 mockup kit's AUTHORING.md (read-only), the prompts 06b and 06c, gallery-governance.
Where: the AndroidApp workspace for the IA and audit; SharedContracts for the Configuration writes when occupancy is granted; one commit per repository.
Scope: the IA; the contracts and mockups; DESIGN_VERSION.md stepped; 06c's two static legs; G-b-3 put and recorded. Not here: an emulator, a screenshot; any Kotlin.
Read first: the prompts; the landed contracts; AUTHORING.md; the Gallery structure.
Write: the files listed.
Constraints: as B6a-6.
Questions: G-b-2 and G-b-3 are the outputs; others as proposed Q-B6b-<nn> rows.
If the context runs short: commit the IA and the validated Configuration files, stop; restart as B6b-6-r2.
Done when: the IA recorded with G-b-2's words; contracts and mockups exist and the mechanical leg passes; G-b-3 put; two commits; the final message gives the §L row and the commit the gitlink takes.
Commit line: rework: B6b-6 - AndroidApp IA 06b; contracts and mockups; mockup audit 06c; G-b-2/3
```

#### `B6b-7` — change classification (06d); plan-batch (07); SCOPE (08); gate `G-b-4`

**Model · reasoning:** Opus 5.5 · xhigh for 06d; the `/plan-batch` act Opus 5.5 · high · **Route:** session (headless), then plan · **Where:** AndroidApp, in place · **Precondition:** `B6b-6`, `event:G-b-3` · **Writes:** workspace `06d_*`; `implementation/Design_Migration_V1/{BATCH_PLAN,TASK_CHECKLIST,TASK_CONTEXT,STATE}.md` (new rows and batches — Q-A7-08 (a), the Q-B6a-19 / Q-B6c-21 precedent, corrected 2026-10-14); the V1 package receives anchor notes, the DS-row supersession lines and statuses, and the DV rows' `requirements` cells the classification maps (AN-V1-DV-06 incl., Q-B6b-18) only; workspace `SCOPE.md` · **Waits:** Q-A9A-02, Q-A7-08

```text
B6b-7 — the AndroidApp change classification and the batches
Classify every change as bugfix / additive-silent / amendment / already-owned, draft the amendment, cut the waves, put them to the operator (G-b-4); then write the rows and batches through plan-batch and the workspace SCOPE — the Tokens.kt wiring and the hand-written ColorScheme/Typography/Shapes adapter as the first batch (its compile a deferred row, DV-A9A-a), the spacing-literal replacement second, the dark theme and launch theme third, the icon-set decision as an amendment row.
This block runs as two sessions (B6b-7a, then B6b-7b): session a does everything up to the gate G-b-4, ends with the gate's decisions in its final message and stops; session b starts only after event:G-b-4 (the operator's words recorded in the workspace STATE.md by the orchestrator) and does the rest; both sessions paste this same block and say which part they are in their first line.
Context: step B6b-7 of the GUI rework runbook (§5); rules: kickoff §2 (rule 4); the answers: Q-A9A-02, Q-A7-08, G-b-3; inputs: 06c, AUDIT_batch-packages_2026-10-13.md §7.3 (AndroidApp rows), AUDIT_gui-current-state-androidapp_2026-10-13.md §7.7 (the adapter minimum, the six requirements); the prompts 06d, 07, 08; the AndroidApp plan-batch skill.
Where: the AndroidApp submodule on main, in place; two commits.
Scope: 06d; G-b-4; the plan-batch act (validation cells authored by the plan-batch skill from the row schema; every leg that needs a compile, an emulator or a device carried as a deferred row by DV id); the AN-V1-DS-01/02/03/04/05 supersessions as STATE lines; SCOPE 08. Not here: implementation; Gradle.
Read first: the prompts; 06c; the package's five files; the plan-batch skill (self-review through the batch-plan-auditor agent, in the foreground).
Write: the files listed.
Constraints: no test; CRLF; census 0 errors; no push.
Questions: G-b-4 is the output; others as proposed Q-B6b-<nn> rows.
If the context runs short: commit 06d, stop; restart as B6b-7-r2 for the act.
Done when: rows and batches exist; G-b-4 recorded; two commits; the final message gives the §L row and the commit the gitlink takes.
Commit line: rework: B6b-7 - AndroidApp change classification 06d; <n> rows in <m> batches; SCOPE 08
```

#### `B6b-8` — implementation of the classified changes, batch by batch (after the Kit session)

**Model · reasoning:** Opus 5.5 · high · **Route:** session (headless), one per batch · **Where:** AndroidApp, in place · **Precondition:** `B6b-7`, `event:G-b-4`, `event:Kit-session-done` (the owed item 12 of the master runbook §3b, Q-A4-05) · **Writes:** `core/design/**`, `feature/**`, `app/**`, `design/conformance/CONFORMANCE_MATRIX.md`, package status cells and `STATE.md` · **Waits:** Q-A4-05, Q-G-04, Q-R-01

```text
B6b-8 — one AndroidApp batch implemented with mechanical checks only
Implement the rows of the batch named in the first line of your launch message — the Tokens.kt wiring and the adapter first — with the Kit's static checks (Kotlin-aware after the Kit session) and the interim text scan, record every leg the row's cell names that Phase B cannot run as a deferred row by DV id (if Q-G-04 (b) admitted a compile, it is a named leg of the row and runs as such), and keep the package honest (statuses per Q-R-01).
Context: step B6b-8 of the GUI rework runbook (§5), one session per batch, the key in the orchestrator note; rules: kickoff §2 (rule 1: no Gradle task unless Q-G-04 (b); no emulator; rule 4); the answers: Q-A4-05 (the Kit session's result by pointer), Q-G-04, G-b-4; the package rows; the design-gate skill before, design-audit after; AUDIT_gui-current-state-androidapp_2026-10-13.md §7.7 (the adapter minimum items 1-6).
Where: the AndroidApp submodule on main, in place; one commit per batch.
Scope: the batch's rows only; design gate before the first edit; design audit after; the text scan for 0xFF… and .dp literals on touched files; the conformance matrix; row statuses per Q-R-01 with a dated STATE line per row naming its deferred rows (DV-A9A-a, -j by id). Not here: any other batch; the emulator; a Gradle task unless admitted.
Read first: the batch's rows and anchors; the design-gate skill; B5-6's mapping.md and the Kit session's findings.
Write: the files the rows name; the package status cells and STATE lines.
Constraints: sources read-only; no test; design-audit green; line endings as found (eight .kt files and three build.gradle.kts are mixed: byte-exact substitution, never the Edit tool — Q-B6b-42 (a), corrected 2026-10-14); the AndroidApp verdict unchanged; no push.
Questions: proposed Q-B6b-<nn> rows; continue.
If the context runs short: commit the complete rows with statuses, stop; restart as B6b-8-r<k>.
Done when: every row done or honestly left; the audit green; one commit; the final message names it, the statuses and the deferred rows.
Commit line: rework: B6b-8 <the batch key from the launch message> - <rows> rows - mechanical checks
```

**Watch:** `Tokens.kt` wired into a source set with no compile deferred row; a hand-transcribed colour.

## L. Lane ledger — flip as you go

Status vocabulary as the master runbook §L. The master runbook's rows `B6a-1`…`B6b-8` read "pointed" and this table is of record for them.

| Step | Title | Status | Decision | Note |
|---|---|---|---|---|
| `B6a-1` | Dashboard workspace bootstrap | done 2026-10-13 — Dashboard `a3f5211` | — | restructure brief (DM-DEC-01); pin by pointer; roots D-2026-10-13-05; package seeded empty (DM-DEC-05); lint ignores, Design context, authority row; Q-B6a-01..03 (a) |
| `B6a-2` | Dashboard census | done 2026-10-13 — Dashboard `c4e348b` | — | 13 routes/12 views; 42 ops, 13 reached; CM-01..31 (24 T1, 7 T2); literals 1c+87d; legacy theme 3 values off canon; role layer unused; Q-B6a-04..06 (a) |
| `B6a-3` | Dashboard contracts, target | done 2026-10-13 — Dashboard `7098108` | — | 13 contracts WSC-01..13 (/login new); 78 regions on roles; GM-01..08; RD-01..06 for the IA; 28 captures deferred (DVC-A9D-01/02); 16 targets, 1 active; Q-B6a-07..09 (a) |
| `B6a-4` | Dashboard comparison, gap map | done 2026-10-13 — Dashboard `5a2d9c7` | — | 72 gaps: P0 1 (role layer unused), P1 11, P2 38, P3 22; A9 15 placed / 5 dismissed; owners B6a-5 20, B6a-6 22, B6a-7 8, B6a-8 22; Q-B6a-10 (a) |
| `B6a-5` | Dashboard forward surface; `G-a-1` | done 2026-10-14 — Dashboard `6eca8eb` | — | 16 open rows: reserve 6 / absorbed 4 / no-UI 6, 13 notes owed at B6a-7 (DS-03 done by B5-4); settings 47 keys 3/16/28; UQ-1..11; D-1 defect; G-a-1 put as Q-G-a-1-01..09 (open); Q-B6a-11/12 (a); UB-20 |
| `B6a-6` → split `B6a-6a` (to the gate), `B6a-6b` (after `event:G-a-2`) | Dashboard IA, mockups, audit; `G-a-2`, `G-a-3` | done 2026-10-14 — Dashboard `7279eb2` (6a), SharedContracts `a532496` + Dashboard `4cc67d5` (6b) | — | IA 14 pages; Configuration 1.1.0 (14 web page contracts, 2 patterns, 14 mockups, 15 fixtures; no core change; C-24/C-25 and the token groups refused by the Kit's schemas → K-3); audit 43 findings, 29 fixed; G-a-3: 11 items (a) under Q-G-10, items 2/3/4 flagged → the operator |
| `B6a-7` → split `B6a-7a` (to the gate), `B6a-7b` (after `event:G-a-4`) | Dashboard classification, plan-batch, SCOPE; `G-a-4` | done 2026-10-14 — Dashboard `25712d6` (7a), `e951f65` (7b); G-a-4 item 5 open (the amendment, B6a-7.1) | — | 84 changes → 44 rows / 20 batches WDM1-B01..B20 (30 todo, 14 blocked on G-a-3 items 2/3/4, item 5, K-3, Server rows); SCOPE; base sha 25712d6; 14 V1 notes, DS-01/06 superseded, GAP-69 cell fixed; Q-B6a-23..26 (a) |
| `B6a-8` | Dashboard implementation (per batch) | running (WDM1-B10 session) | — | one row per batch below; Q-R-01 (a): rows end needs-reverify until Phase C |
| `B6a-8 WDM1-B01` | foundation: alias layer, theme names, legacy pipeline, token test, drift checker, Configuration sync | done 2026-10-14 — Dashboard `fecdfae` | — | 3 rows needs-reverify (vitest and build legs to Phase C, DV-B6a-15/16); pin 1.1.0; drift/pin/bans green; literals 88 pre-existing (TOK-08), coverage red (live Kit 1.12.0, B5-9); 4 deviations recorded; Q-B6a-27..30 (a) |
| `B6a-8 WDM1-B02` | shared layer on roles and dark; charts | done 2026-10-14 — Dashboard `cb27b56` (+ amendment `26b7a66`) | — | 2 rows needs-reverify; 123 role refs, 0 dark overrides, charts on series roles; no new literal vs baseline; coverage red-external; 4 deviations (Q-B6a-32); Q-B6a-31 (a) |
| `B6a-8 WDM1-B03` | page layer on roles; rename and alias removal; literals | done 2026-10-14 — Dashboard `b792f63` (+ amendment `b524da7`) | — | 3 rows needs-reverify (coverage red-external until TOK-10; TOK-07's vitest leg DV-B6a-15); literal census 0 beyond the allowlist (9 entries, owner TOK-10); alias file and generator removed; tsc/eslint/prettier clean; closeout reviewer 0 blocking; 5 deviations recorded; Q-B6a-33..35 (a); DV-B6a-19..21 |
| `B6a-8 WDM1-B21` | Configuration 1.3.0 re-pin (TOK-10, moved out of B19 by Q-B6a-34) | done 2026-10-14 — Dashboard `977d990` (+ amendment `c578c70`, DM-DEC-40/41) | — | TOK-10 needs-reverify (vitest DV-B6a-15, build DV-B6a-16); 120 Configuration files synced byte-equal from `bc37a0e`, pin design 1.3.0 / Kit 1.12.0 `b01d8cc`; coverage 23/25 → 25/25, run-all green; 40 widths on `border.width.*`; 7 allowlist entries kept (no scrim role yet, revisit B5-10, owner TOK-09); installer re-run NOT done (outside SCOPE §2) → Q-B6a-36; auditor FAIL→PASS after 3 static legs added; reviewer 0 blocking; 6 deviations; Q-B6a-36..38 (a) |
| `B6a-8 WDM1-B22` | Kit 1.12.0 installer re-run (TOK-11, Q-B6a-36); TOK-03/08 re-verify (Q-B6a-37) | done 2026-10-14 — Dashboard `075a3d8` (+ amendment `4ea8ce0`, DM-DEC-42) | — | installer from a staged mirror: 5 paths changed (workflow, the `Kit:` line of CLAUDE.md and AGENTS.md, check-literals.mjs, run-all.mjs), 13 byte-equal, `.codex` untouched; harness parity 7/7 green; TOK-03, TOK-08, TOK-11 `done`; B03's prettier record corrected (Q-B6a-38); `DESIGN_KIT_REF` variable still v1.11.0 → Q-B6a-44 (the operator) |
| `B6a-8 WDM1-B04` | shell frame: navigation, status block, toolbar, connection state | done 2026-10-14 — Dashboard `96c3183` | — | 3 rows needs-reverify (vitest DV-B6a-15, visual DV-B6a-10, live banner DV-B6a-22); closeout reviewer pass-with-fixes (offline banner via `onlineManager`, Add plant gated by availability, tests added); nav current item as tint + weight, the stripe waits B5-10 / SHELL-08; 6 deviations; Q-B6a-45..48 (a) |
| `B6a-8 WDM1-B05` | shell behaviour: quick switcher, compact rail, routes and URL state, notifications and motion | done 2026-10-14 — Dashboard `cee0831` (+ amendment `3bec684`, DM-DEC-43) | — | 4 rows needs-reverify (vitest DV-B6a-15, build DV-B6a-16, visual DV-B6a-10/23/24, WD-V1-DV-06/10); auditor pass-with-fixes; reviewer (fresh, after a turn-limit loss) pass-with-fixes — B-1 fixed (centred-frame routes set title and focus); rail at the 1.3.0 900px value, waits the TOK-09 re-pin (1024); 9 deviations; Q-B6a-49..55 (a) |
| `B6a-8 WDM1-B06` | shared patterns: page anatomy; disabled reasons | done 2026-10-14 — Dashboard `7e5fbdf` (+ the B9-5 cherry-pick `357a130` on top) | — | 2 rows needs-reverify (vitest DV-B6a-15, visual DV-B6a-12, WD-V1-DV-11, DV-B6a-25); the page header on all 11 pages, breadcrumb, C-21 rows, confidence as a word (meter retired), `Button reason` + `useWriteReason()` on every write control, true reasons replace the shared false ones; reviewer (fresh) pass-with-fixes (a Shell test's `current` boolean); SHELL-03 not flipped (vitest leg); 8 deviations; Q-B6a-56..61 (a) |
| `B6a-8 WDM1-B07` | pages: sign in; the garden plant's page (read) | done 2026-10-14 — Dashboard `1308fda` (+ amendment `dc9f3a2`, DM-DEC-44) | — | 2 rows needs-reverify (vitest DV-B6a-15, visual DV-B6a-12, live DV-B6a-26/27); the first web page bound under D-V1-13; reviewer pass-with-fixes (NoticePanel, loading width); coverage red-external — the live Kit checkout sits mid-K-4 (`v1.12.0-6`, C-27/C-28 listed), green against the pinned `b01d8cc` export (Q-B6a-62; RC-B6-13 in K-4's scope); 10 deviations; Q-B6a-62..67 (a) |
| `B6a-8 WDM1-B08` | pages: Dashboard (the D-1 fix first) | done 2026-10-14 — Dashboard `35e45c6` | — | 2 rows needs-reverify (vitest DV-B6a-15, visual DV-B6a-12/WD-V1-DV-13, live DV-B6a-28/29); **D-1 fixed**: due-task links now `/plants/:profileId/instances/:instanceId` (was the instance id in the profile route), asserted by test; reviewer pass (0 findings, 5 notes); coverage green against the pinned export and, from Kit `6b822b3` on, on the live route too (RC-B6-13 fixed); Q-B6a-67 applied (lowercase task words); 6 deviations; Q-B6a-68..73 (a) |
| `B6a-8 WDM1-B09` | pages: Plants; plant profile | done 2026-10-14 — Dashboard `16b6f55` | — | 2 rows needs-reverify (vitest DV-B6a-15, visual DV-B6a-12, live DV-B6a-30/31; PAGE-06's "nothing links to it" clause waits PAGE-10/13); Plants on C-03 roles with URL filters, sort and a health facet, selection and the bulk write controls removed (Q-B6a-60); the profile reduced to the breadcrumb, title and "Your plants of this species" (Q-B6a-53); reviewer (fresh) pass 0 findings; coverage green on both routes; 2 files deleted as orphaned; Q-B6a-74..78 (a) |
| `B6c-1` | PyApp workspace bootstrap | done 2026-10-13 — PyApp `62b5dd9` | — | re-skin, pin by pointer, unbound; roots D-2026-10-13-05; sentinel+harness routes (Q-B5-18/Q-A9P-04); DESIGN prose recovered, 71 cites; Q-B6c-01/02 (a) |
| `B6c-2` | PyApp census | done 2026-10-13 — PyApp `e203c95` | — | 164 hex (design_tokens.py, 0 QSS); Kit: 2 colour+369 dim open, 4 banned; 18 role-bypass files; 14 phase rows deferred (Q-B6a-02); Q-B6c-03/04 (a) |
| `B6c-3` | PyApp contracts, target | done 2026-10-13 — PyApp `de5551d` | — | 37 contracts (11 views, wizard frame+6 steps, 19 dialogs); Gallery the sole active target; 03 deferred DV-A9P-01 (74 rows); Q-B6c-05..10 (a); DV-B6c-02; UB-18 |
| `B6c-4` | PyApp comparison, gap map | done 2026-10-14 — PyApp `573590c` | — | 118 gaps: P0 1 (tokens.py unused), P1 13, P2 79, P3 25; owners B6c-5 11 / B6c-6 6 / B6c-7 41 / B6c-8 60; F-A9P 11 placed, 5 dismissed; AVD-PY-01..06; Q-B6c-11..13 (a) |
| `B6c-5` | PyApp forward surface; `G-c-1` | done 2026-10-14 — PyApp `cac2e5f` (r2) | — | re-skin form: 8 open rows reserve 3 / absorbed 2 / no-UI 3; 9 notes owed at B6c-7; settings 47 entries 25/9/13, 9 never read; G-c-1 put as Q-G-c-1-01..08 (open); Q-B6c-14 (a); UB-21 |
| `B6c-6` → split `B6c-6a` (to the gate), `B6c-6b` (after `event:G-c-2`) | PyApp IA, mockups, audit; `G-c-2`, `G-c-3` | done 2026-10-14 — PyApp `c1a48aa` (6a), SharedContracts `51f2bf5` + PyApp `12c27c1` (6b) | — | IA 12 pages (today's tree); Configuration 1.2.0 (11 desktop contracts, 11 mockups, 12 fixtures, 104 regions; no core change); audit 68 findings, 30 fixed; GUI routers retired; G-c-3: 13 items (a) under Q-G-10, item 7 follows Q-G-a-3-03 |
| `B6c-7` → split `B6c-7a` (to the gate), `B6c-7b` (after `event:G-c-4`) | PyApp classification, plan-batch, SCOPE; `G-c-4` | done 2026-10-14 — 7a PyApp `47d2ffc`, 7b PyApp `1336b22` (`cfb9fdb` plan + SCOPE, `e31b179` V1 writes, `1336b22` PRODUCT.md) | — | 68 rows / 22 batches PYDM1-B08..B29 in `implementation/Design_Migration_V1/` (65 todo in 20 batches; FIELD-01 blocked on `B5-10`; VGATE-02/QA-02 deferred); G-c-4 18/18 (a); auditor FAIL→PASS→PASS (3 rounds); guards 0 errors (128 batches / 380 rows), hygiene 0/0; V1: 9 anchor notes, DS-01..03 deferred, 8 DV requirements cells (CC-78, "implemented" not "done" — Q-B6c-25), PY1-B11 OPS-01, PRODUCT.md §4.1/§4.4; base sha `47d2ffc`; AVD-PY-07..11; ids CMP-02..05/SRC-02..03 (DMD-23); Q-B6c-24..29, -33..-36 (a); DV-B6c-17..19 |
| `B6c-8` | PyApp implementation (per batch) | running (PYDM1-B14 session) | — | one row per batch below; Q-R-01 (a): mechanical checks only in Phase B, rows end needs-reverify; the harness closeout and every pytest/app leg wait Phase C (DV-B6c-*) |
| `B6c-8 PYDM1-B08` | foundation: Configuration 1.3.0 re-anchor, the adapter, the composed keys, `design_tokens` re-exports | done 2026-10-14 — PyApp `304dd54` (DMD-29..31) | — | TOK-01 done; TOK-02/03/04 needs-reverify (pytest DV-B6c-20; DV-B5-03, DV-A9P-06/08); pin 1.3.0 / Kit 1.12.0 (installer run, `.codex` untouched, harness parity 7/7); coverage 117/119 → 127/127; census 176 allowlisted → 0, banned 4 → 0; 132 aliases, 175 placeholders; `design_tokens.py` 623 → 77 lines; check-parity red-external (45 pre-existing impeccable mirror diffs, Q-B6c-37); reviewer pass with notes, both should-fix applied (DMD-31 cell amendment); 7 deviations; Q-B6c-37..42 (a) |
| `B6c-8 PYDM1-B30` | tooling: impeccable mirror re-sync; design file eol attributes (Q-B6c-37/42) | done 2026-10-14 — PyApp `50bf4a1` (+ amendment `bf6109f`, DMD-32) | — | TOOL-03/04 done; Kit check-parity 45 FAIL → pass; 32 design files `eol=lf`, no renormalisation diff; three `.agents`-only Codex-harness files deleted (deviation, **listed for veto**, Q-B6c-47); superproject harness parity 7/7 |
| `B6c-8 PYDM1-B09` | theme behaviour; the check glyph and url(); the harness asset → consumer route | done 2026-10-14 — PyApp `dc418ea` (DMD-33) | — | 4 rows needs-reverify (pytest DV-B6c-17/22; DV-A9P-02..05); run-all green, 0 new literals; icon route 3 targets, QSS route 8; C-08 and Settings `partial` in the matrix; reviewer pass with notes; 8 deviations; Q-B6c-43..46 (a) |
| `B6c-8 PYDM1-B10` | the role layer; drift tooling and the detector; scenario variants | done 2026-10-14 — PyApp `209920b` (+ amendment `6af60e2`, DMD-34/35) | — | 5 rows needs-reverify (pytest DV-B6c-25, DV-A9P-01/06, the real-import drift leg DV-B6c-24); 93 role reads converted, greps empty; the checker reads the emitted tokens and `banned-colors.json`; TOOL-05 bytecode-free loader; auditor pass, reviewer (fresh) pass; 5 deviations; Q-B6c-48..50 (a) |
| `B6c-8 PYDM1-B11` | dark-theme roles; category hues | done 2026-10-14 — PyApp `b201d39` (+ amendment `8812de3`, DMD-36/37; + the B9-5 cherry-pick `3357a39` on top) | — | 2 rows needs-reverify (pytest DV-B6c-26, DV-A9P-06); 49 light-only reads converted, `domain_color()` accessor; calendar chips and provider labels neutral; tag text by contrast; run-all 0 new literals, coverage 127/127; auditor fail→fixed, reviewer pass; new late batch PYDM1-B31 (closeout path coverage, TOOL-06); 5 deviations; Q-B6c-51..55 (a) |
| `B6c-8 PYDM1-B12` | the literal defects; colour literals and `pill_input`; per-widget sheets | done 2026-10-14 — PyApp `294a477` (+ amendment `462ff97`, DMD-38/39: B31 gains TOOL-07 and DARK-03) | — | 3 rows needs-reverify (DV-B6c-03/27/28, DV-A9P-07); 25 font sizes on `typography.*`; 83 → 13 `setStyleSheet` calls, component rules in both templates, 6 new placeholders; run-all 0 new literals (324 → 255); reviewer fail → fixed (the dialog scaffold's radius stays in code — `test_wg19`; DLG-01 moves it); coverage 127/127 against the pinned export (the live Kit is mid-K-4); 7 deviations; Q-B6c-56..60 (a) |
| `B6c-8 PYDM1-B13` | layout literals: views, dialogs and widgets; the wizard | done 2026-10-14 — PyApp `ad7e4b1` (+ amendment `74b1deb`, DMD-40/41: B31 TOOL-08, the pinned-export audit rule) | — | 2 rows needs-reverify (DV-B6c-03/29/30); 282 dimension reads + 410 layout integers on `token()` with no value change; off-scale values to the contract token or the nearest step; 51 layout sizes with no token allow-listed (Q-B6c-61: a Configuration layout-size group); wizard sheets 71 → 9; LIT-04 audit 3 → 0; reviewer (fresh) pass with notes (FORM-01's 1 px error border — veto-listed); Q-B6c-61..65 (a) |
| `B6b-1` | AndroidApp workspace bootstrap | done 2026-10-13 — AndroidApp `6ad8087` | — | restructure brief, unbound; 16 phase rows in ADM1-B00..B07; roots D-2026-10-13-05; hook file added; design-authority row repointed; Q-B6b-01..04 (a) |
| `B6b-2` | AndroidApp census | done 2026-10-13 — AndroidApp `e9ac4a8` | — | 215 literals (87 colour, 128 dim; 82 dp UI); 6 banned lines; mirror 58/27/49; 65 ops/51 reached; CM-01..04 confirmed; README fixed; Q-B6b-05..07 (a) |
| `B6b-3` | AndroidApp contracts, target | done 2026-10-13 — AndroidApp `c02f9bb` | — | 15 contracts (3/5/7; 8 contracted, 7 partial); 4 of 9 routes drift; 11 targets, 4 active; 03 deferred DV-A9A-b; 15 ADM1 rows deferred; Q-B6b-06 closed; UB-16 |
| `B6b-4` | AndroidApp comparison, gap map | done 2026-10-13 — AndroidApp `e6247a7` | — | 62 gaps: P0 1, P1 10, P2 39, P3 12; owners B6b-5 21 / B6b-6 13 / B6b-7→8 27 / C 1; F-A9A 14 placed, 9 dismissed; Q-B6b-08..10 (a); UB-17 |
| `B6b-5` | AndroidApp forward surface; `G-b-1` | done 2026-10-14 — AndroidApp `762bc1e` | — | 28 rows: reserve 21 / absorbed 3 / no-UI 4; 12 mandated absent; 40 settings keys 4/5/31; IM-Q1..8; G-b-1 put as Q-G-b-1-01..09 (open); Q-B6b-11/12 (a) |
| `B6b-6` → split `B6b-6a` (to the gate), `B6b-6b` (after `event:G-b-2`) | AndroidApp IA, mockups, audit; `G-b-2`, `G-b-3` | done 2026-10-14 — 6a AndroidApp `32ad3e6`; 6b SharedContracts `9e76d06` (Configuration 1.4.0: 16 phone page contracts, 2 pattern sections, 16 mockups + index, 17 fixtures, 3 product-contract amendments) + AndroidApp `28101da` (IA §0, audit 06c, G-b-3 put) | — | 1.4.0 is non-core (digests stay 1.3.0's); each client re-syncs the non-core files and moves its pin to 1.4.0 in its first -8 row; validator 110/0, coverage 127/127, literal census 0 over 19 files; 52 findings (26 fix-now applied, 14 fix-in-batch, 13 escalated); G-b-3: items 1–8, 13 (a) under Q-G-10, items 9–12, 14–18 flagged → the operator (§O step 4a); Q-B6b-16..19 (a); DV-B6b-07..09 |
| `B6b-7` → split `B6b-7a` (to the gate), `B6b-7b` (after `event:G-b-4`) | AndroidApp classification, plan-batch, SCOPE; `G-b-4` | done 2026-10-14 — 7a AndroidApp `c11052d`, 7b AndroidApp `a82cc91` (`32f2b37` plan + SCOPE, `a82cc91` V1 writes) | — | 45 rows / 16 batches ADM1-B08..B23 in `implementation/Design_Migration_V1/` (41 todo in B08–B21; B22 blocked skeleton; B23 deferred); CC-01 split into TOK-01 (re-sync 1.3.0+1.4.0+1.5.0, re-pin) and TOK-06 (installer re-run, SCOPE §2 paths); auditor FAIL→FAIL→PASS; guards 0 errors (146 batches / 430 rows), hygiene 0/0; V1: 30 anchor notes, DS-01/05 deferred, DV-02/03/10/11/12/13 cells name the rows (implemented, not done), DV-06 todo with TGT-12, 25 design-audit legs; base sha `c11052d`; the PLANTS-02 / item-15 blocks are stale (answered 17:05 UTC) → the ADM1-B08 session's amendment; Q-B6b-25..28 (a); DV-B6b-15; RC-B6-18 |
| `B6b-6c` | SharedContracts patch: the Configuration halves of the operator's G-b-3/G-b-4 answers (Q-B6b-19 (a)) | done 2026-10-14 — SharedContracts `7911c98` (Configuration 1.5.1, patch; no digest moved) | — | inserted 2026-10-14 after the operator's "all recommended" 17:05 UTC: viewer specimens + `shell.disabled.viewer` (G-b-3 9), the lifecycle word on the Plants row + the "Plant status" facet (10), the Add page's "In your catalog" primary (11), "Also complete {type} task" (12), the ghost "Sign in with another account" (14), Retry on the plant page's job (15), APG-08.R4 product-gap markers (16), MobilePageContract_add.md's product text (17), C-14's tab list and nav-label role, the facet list, the stale Settings line and "reminder defaults" (G-b-4 15, 17); design 1.5.1; after B5-10 (`b4b389d`), before B6b-8's first row; DR-1.5.1-01..13: items 9, 10, 11, 12, 14, 15, 16, 17 and G-b-4 15/17 done, item 18 to the Workspace lane (CC-82), item 6 recorded only (the chip stays); Q-B5-31 done; validator 124/0, coverage 127/127, census 0 over 19 files; three writes in `page-contracts/android/` (the product contracts the items name); Q-B6b-29..33 (a); DV-B6b-16/17 |
| `B6b-8` | AndroidApp implementation (per batch) | running (ADM1-B12 session, with the 1.13.0/1.6.0 re-pin batch ADM1-B24 amendment first) | — | one row per batch below; Q-R-01 (a): mechanical checks only in Phase B (no Gradle, emulator or test), rows end needs-reverify; the closeout at Phase C |
| `B6b-8 ADM1-B08` | foundation: Configuration 1.5.1 re-sync and re-pin; `Tokens.kt`; the ColorScheme on roles; typography and shapes | done 2026-10-14 — AndroidApp `eb61d18` (+ amendment `b25b68c`: gate blocks lifted, CC-83, IM-P05/06) | — | 5 rows needs-reverify (DV-A9A-*, DV-B6b-10/18; the Phase C Gradle closeout); pin design 1.5.1 / Kit 1.12.0 (installer: 5 paths, `.codex` untouched, harness parity 7/7); 90 files byte-equal; coverage 117/117 → 127/127, contrast 124/0; `Color.kt` orphaned (TOK-05 deletes); Material 3 1.2.1 slot mapping corrected after the reviewer (cards on `surface_1`, chips `full`); `border.width.*` absent from `Tokens.kt` — Kit compose emitter gap (RC-B6-19, sent to K-4); auditor fail→fixed, reviewer pass-with-findings (nudged, not fresh — veto-listed); Q-B6b-34..40 (a) |
| `B6b-8 ADM1-B09` | the role layer and the spacing aliases; the 82 dp literals; the hand mirror retired; the launcher | done 2026-10-14 — AndroidApp `7a6c811` (+ amendment `5260a0b`: TOK-06 done, TOK-05 files, V1 CARE-02 cells) | — | 4 rows needs-reverify (DV-A9A-a/b/j, DV-B6b-08/19); `PlantLibraryRoles.kt` light/dark; census 87 colour · 121 dimension · 4 banned → 0 · 14 · 6 allowlisted · 0; `Color.kt`, `Spacing.kt`, the drift script deleted (THEME-01's banned clause closes); LIT-01 68/82 — 14 literals wait a `:core:design` dependency in `feature/auth` and `feature/more` (Q-B6b-41, the ADM1-B10 session's amendment); auditor fail→fixed, reviewer pass-with-findings (one run); 4 deviations; Q-B6b-41..45 (a) |
| `B6b-8 ADM1-B10` | launch theme; Appearance | done 2026-10-14 — AndroidApp `02b56e6` (+ amendment `071efd1`: LIT-01's `:core:design` dependency and its last 14 literals, the byte-exact rule) | — | 2 rows + LIT-01 needs-reverify on Phase C legs only (DV-A9A-a/h/j, DV-B6b-08/10/20/21); product census 0 colour · 0 dimension · 6 allowlisted; `plant_library_device_prefs` DataStore read before `setContent`; `Theme.DeviceDefault.DayNight`; auditor fail→fixed, reviewer pass-with-findings (the Theme radio group's help inside the group); 7 deviations; Q-B6b-46..49 (a) (49: the runbook's "Edit tool only" phrases corrected in this commit) |
| `B6b-8 ADM1-B11` | the bottom bar; the icons | done 2026-10-14 — AndroidApp `17a2bef` | — | 2 rows needs-reverify (DV-A9A-a/b/g/j, DV-B6b-08/09/22); bar order Home · Plants · Add · Tasks · More on `surface_2`/`text_secondary`, the current tab's `selected_bg` indicator; six Material Symbols drawables replace `material-icons-extended` (12 `24dp` literals allowlisted permanent, Q-B6b-50); the hairline waits the re-pin to Kit 1.13.0 / Configuration 1.6.0 (`border.width` emitted at K-4) → a re-pin batch before ADM1-B14 (Q-B6b-51); reviewer pass-with-findings; 5 deviations |
