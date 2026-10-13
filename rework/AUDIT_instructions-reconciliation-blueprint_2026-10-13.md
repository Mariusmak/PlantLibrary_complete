# Instructions reconciliation blueprint — lane A3 (read-only analysis, 2026-10-13)

**Lane:** `A3` of `rework/PROMPT_master-rework-kickoff_2026-10-13.md` §3 (R-1). **Model:** Opus 5.5 · high, no subagent.
**Pins read:** TARGET superproject `8702e0a`, PlantLibrary_Workspace `6b4b88b`, PlantLibrary_PyApp `35ddc63`,
PlantLibrary_AndroidApp `5d6410f`, PlantLibrary_Dashboard `7795fc8`, PlantLibrary_Server `f1a31b9`,
PlantLibrary_SharedContracts `d43f7a2`; SOURCE-C `C:/Programmierung/Orchestrator_System` main `2e7adb3`; SOURCE-K
`C:/Programmierung/Repo_Hygiene_Template_Kit` 0.2.1 and `C:/Programmierung/Design_Template_Kit` `f08e588`.
**Posture:** nothing was edited anywhere except this file; git reads only (`--no-optional-locks` in SOURCE-C); no test,
build or install. TARGET paths are written `<repository>/<path>:<line>`, the superproject as `SW_Development/…`.

## §0 Summary

1. The Conductor's reconciliation is executed, not just planned: OP-IR-1 landed at `9de949f` (2026-10-04,
   `D-2026-10-04-07`) on `CLAUDE.md` only, after the Codex freeze (`10177e3`); `AGENTS.md` is the freeze blob plus a
   two-line notice. The template for TARGET is the Conductor `CLAUDE.md` at `2e7adb3`, not the PLAN's E-05 draft.
2. TARGET's instruction surface has no session rules, no authority section and no roster anywhere; the superproject
   `CLAUDE.md` (= `AGENTS.md`, byte-identical) is the operator's Testing block plus the hygiene block.
3. The six suite guides share one parameterised skeleton (onboarding step 3) and one byte-identical `## Deliverable
   naming` section directly above the installer-owned hygiene block; B2 can add sections as a fixed template.
4. Of the Conductor's ten session rules, six transfer with parameters, rule 5 (push) collides with Q-G-03, rule 4
   (drained boundary) needs an instance-2 fact, rule 7 needs the seven-repository D-id grep.
5. Package `model` cells (`opus/sol`, `sonnet/terra`, `haiku/luna`) are a parsed machine contract; they are mapped by
   rule 1's wording, never rewritten. `haiku/luna` (Haiku 4.5) rows exist in five packages.
6. A freeze of `AGENTS.md` collides with two installers that own blocks inside it (hygiene, design kit); the
   Conductor paid for this twice (`fe4618a`, a design block stuck at Kit 0.8.0). Q-A3-01 asks for a block-aware freeze.
7. `PyApp/.claude/CLAUDE.md` is a stale July duplicate loaded beside `CLAUDE.md`; recommended: fold and stub.
8. `CONTEXT_INDEX.md`/`SCOPE.md`: all seven packages have both; TARGET's CONTEXT_INDEX headings are the very words
   `run-batch` cites, so keep them; add a Traceability section; SCOPE needs no heading change.
9. B2 order: B1's superproject `.claude/` sync first, then `SW_Development/CLAUDE.md` (the rules the suites point at),
   then Dashboard, AndroidApp, PyApp (so B5's design block lands above the new roster heading), then Server,
   SharedContracts, Workspace.
10. Seven questions (Q-A3-01…07); 29 candidates; 19 findings.

## §1 Coverage

| Item | Status (read / partly read / not read) | Reason |
|---|---|---|
| `rework/PROMPT_master-rework-kickoff_2026-10-13.md` §1, §2 (and §3, §4) | read | whole file (77 lines) |
| `C:/Programmierung/Orchestrator_System/CLAUDE.md` | read | whole, 258 lines |
| `C:/Programmierung/Orchestrator_System/AGENTS.md` | read | whole, 203 lines; diffed against the freeze commit `10177e3` |
| `C:/Programmierung/Orchestrator_System/.claude/CLAUDE.md` | read (absent) | no such file at `2e7adb3` |
| `C:/Programmierung/Orchestrator_System/.agents/README.md` | read | lines 1-120 (whole) |
| `C:/Programmierung/Orchestrator_System/scripts/harness/check_harness_parity.py` | partly read | docstring :6-26 and the freeze/marker lines by grep (:47-95, :204-253) |
| `…/implementation/Conductor_V2/planning/AUDIT_instructions-and-skills-reconciliation_2026-10-02.md` | read | whole, 522 lines |
| `…/implementation/Conductor_V2/planning/PLAN_instructions-and-skills-reconciliation_2026-10-02.md` | read | whole, 741 lines |
| `…/planning/PLAN_instructions-and-skills-reconciliation-addendum_2026-10-02.md` | partly read | header :1-12, §3 "The Codex freeze" :416-540, grep for F-01; §2 (Tier A diffs) and §4-§7 not read (skills: lane A1) |
| `…/planning/PLAN_instructions-and-skills-reconciliation-addendum-2_2026-10-02.md` | not read | not named by the brief; 789 lines; its subject (later acts) is visible in the executed `CLAUDE.md` |
| `…/implementation/Conductor_V2/STATE.md` | partly read | `D-2026-10-02-23` :44146-44176 only |
| `CONTEXT_INDEX.md`/`SCOPE.md` of Conductor_V2, Design_Migration_V1, Harness_V1, Worker_Console_V1 | partly read | headings of all eight; opening windows of Conductor_V2 (SCOPE :1-30, :286-300; CI :1-12, :85-90), Design_Migration_V1 (SCOPE :1-20, :128-135; CI :1-25), Harness_V1 CI :1-10, :46-58, Worker_Console_V1 SCOPE :1-8, :47-56 |
| Conductor `.claude/skills/plan-batch/SKILL.md`, `run-batch/SKILL.md`, `.claude/agents/*.md` | partly read | model rule :99-110, :128-140, :170-195; run-batch :24-36, :94-118; agent frontmatter by grep |
| `…/src/conductor/batch_package.py` | partly read | `REQUIRED_FILES` :53-58, `parse_model_tuple` :176-210 |
| `…/config.example.yaml` | partly read | the `claude` vendor block :186-230 (ladder and tiers keys only) |
| `…/docs/handbook/03-batch-workflow.md` | partly read | :60-80 |
| `…/docs/authoring/standard.md` | partly read | headings and :1-20, only as far as `CLAUDE.md:254` cites it |
| `C:/Programmierung/Repo_Hygiene_Template_Kit/rule-block/HYGIENE_RULES_BLOCK.md` | read | whole |
| `C:/Programmierung/Repo_Hygiene_Template_Kit/installer/INSTALL.md` | partly read | :40-46, :100-112, grep |
| `C:/Programmierung/Design_Template_Kit/anchoring-kit/INSTALL.md` | partly read | :40-56 (the block placement rule F-J) |
| `SW_Development/CLAUDE.md`, `SW_Development/AGENTS.md` | read | whole (33 lines each; diff empty) |
| `PlantLibrary_Workspace/CLAUDE.md`, `AGENTS.md` | read | whole |
| `PlantLibrary_AndroidApp/CLAUDE.md` | read | :1-100 whole text plus the block |
| `PlantLibrary_Dashboard/CLAUDE.md`, `PlantLibrary_Server/CLAUDE.md`, `PlantLibrary_SharedContracts/CLAUDE.md` | read | heads read (:1-37, :1-72, :1-35); the shared sections by `diff` against AndroidApp's |
| `PlantLibrary_Server/AGENTS.md` | read | :1-44 plus the block |
| `PlantLibrary_AndroidApp/AGENTS.md`, `PlantLibrary_Dashboard/AGENTS.md`, `PlantLibrary_SharedContracts/AGENTS.md` | read | by `diff` against Workspace's (differences: lines 1, 21-22, 24-25) |
| `PlantLibrary_PyApp/CLAUDE.md` | partly read | :1-110, :155-215, :307-414 and the block; :111-154 (mermaid) and :215-306 (module index) not read |
| `PlantLibrary_PyApp/AGENTS.md` | partly read | :1-52, :107-166, :210-243, :481-511; :53-106, :167-209, :244-480 not read (headings only; :374-480 equals CLAUDE.md's batch/scratch/naming text by the naming-section hash) |
| `PlantLibrary_PyApp/.claude/CLAUDE.md` | read | whole, 119 lines |
| `onboarding/AUDIT_skill-assumptions_2026-09-15.md` §3 | read | :270-289 |
| `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` §9 | read | :437-487 |
| `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` §12a | read | :627-705 |
| `SW_Development/.agents/README.md` | partly read | :1-40 |
| `SW_Development/scripts/harness/check_harness_parity.py` | partly read | :1-30 and grep |
| `SW_Development/scripts/hygiene/repo_hygiene_check.py` | partly read | grep (marker and proof-detector lines) |
| Seven packages' `SCOPE.md`, `CONTEXT_INDEX.md` | partly read | headings of all fourteen; PyApp's two read whole; Workspace V1 CI :1-12 |
| Seven packages' `BATCH_PLAN.md`/`STATE.md`/`TASK_CHECKLIST.md` model cells | partly read | grep counts and `**Model:**` line numbers |
| `PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/SCOPE_TEMPLATE.md`, `CONTEXT_INDEX_TEMPLATE.md` | partly read | SCOPE template :1-82; CI template headings only |
| `PlantLibrary_Workspace/implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md` | partly read | grep for model names |

## §2 Findings

**F-A3-01 — The Conductor's reconciliation was executed in a fixed order, and the template is the result.**
`D-2026-10-02-23` froze Codex at `10177e3` (`C:/Programmierung/Orchestrator_System/implementation/Conductor_V2/STATE.md:44166-44176`);
the addendum re-stated every ir-2 edit under the freeze (`…/PLAN_instructions-and-skills-reconciliation-addendum_2026-10-02.md:420-475`);
OP-IR-1 landed at `9de949f` per `D-2026-10-04-07` and OP-SK-H at `83a7d30` (git log of `CLAUDE.md`). In the executed
file: session rules 1-10 (`C:/Programmierung/Orchestrator_System/CLAUDE.md:180-217`) with rule 1 in the addendum's
E-05r form (`:186-191`), not ir-2's (`…/PLAN_instructions-and-skills-reconciliation_2026-10-02.md:167-173`);
"Leave what you did not make" (`CLAUDE.md:135-137`, K-02); E-01 (`:55-57`), E-02 (`:97-99`), E-03r (`:122-125`),
E-04 (`:50-53`), E-08 (`:64-69`), roster E-06r/E-07r/F-03 (`:236-248`), K-16 (`:156-157`). K-22 (the `RUNBOOK` type)
did not land (`:162-163`). *Meaning:* B2 copies from the file at `2e7adb3`; the PLAN is the "why" and the order.

**F-A3-02 — The frozen `AGENTS.md` is stale by design and guarded by digest.** `git diff 10177e3 HEAD -- AGENTS.md`
is two inserted lines, the notice at `C:/Programmierung/Orchestrator_System/AGENTS.md:3`. Its text still says 5,316
lines (`:16`), `AC1`–`AC76` (`:58`), `SCHEMA_VERSION=2` (`:98`), "Sonnet/Terra" (`:123`). The checker pins the
blob (`…/scripts/harness/check_harness_parity.py:54-76`, `:239-253`). A docs-track section added to both files made
every closeout refuse at preflight until it was reverted (`fe4618a`, 2026-10-12). *Meaning:* a TARGET freeze needs a
guard and a one-line rule "never add to `AGENTS.md`".

**F-A3-03 — Two installers own blocks inside `AGENTS.md`.** The hygiene installer writes its block into `CLAUDE.md`
and `AGENTS.md` (`C:/Programmierung/Repo_Hygiene_Template_Kit/installer/INSTALL.md:40`); the design installer does too
and creates `AGENTS.md` if missing (`C:/Programmierung/Design_Template_Kit/anchoring-kit/INSTALL.md:42`). The
Conductor's design block is at Kit 1.3.1 in `CLAUDE.md:231` and still 0.8.0 in the frozen `AGENTS.md:187`. All
thirteen TARGET hygiene blocks are identical (one hash over the marker regions of the fourteen files, superproject
included). *Meaning:* Q-G-09 (a) as worded ("compared against the freeze commit") turns red at the next hygiene
re-pin or at B5's install, unless the compare strips marker blocks (Q-A3-01).

**F-A3-04 — The superproject has no instruction surface of its own beyond two blocks.** `SW_Development/CLAUDE.md`
and `SW_Development/AGENTS.md` are byte-identical, 33 lines, no title: the operator's `## Testing` (`:1-14`) and the
hygiene block (`:16-33`). `SW_Development/CLAUDE.md:10-12` carries "Its Sonnet/Terra worker", the sentence the
Conductor replaced by E-03r (`C:/Programmierung/Orchestrator_System/CLAUDE.md:122-125`). *Meaning:* B2 adds
authority, layout, workflow, session rules and roster; the Testing block stays (Q-A3-02 for its one sentence).

**F-A3-05 — The six suite guides share a parameterised skeleton.** Written at onboarding step 3
(`onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:452-463`, from
`onboarding/AUDIT_skill-assumptions_2026-09-15.md:272-288`): title and intro, `## Build and test`, optional `## Design
context`, `## Batch packages and Conductor` (seven bullets whose diffs are only the live-package bullet, the
standing-invariant headline and the last suite rule, e.g. `PlantLibrary_AndroidApp/CLAUDE.md:47-79` against
`PlantLibrary_Dashboard/CLAUDE.md:38-72`), `## Scratch policy` (three variants), `## Deliverable naming`
(byte-identical in seven copies, `PlantLibrary_*/CLAUDE.md` and `PlantLibrary_PyApp/AGENTS.md:471-480`) and the
hygiene block last. Server (`PlantLibrary_Server/CLAUDE.md:3-53`) and PyApp (`PlantLibrary_PyApp/CLAUDE.md:9-306`) add
suite sections in front. *Meaning:* B2 adds sections as one template with at most three parameters, like A-8 did.

**F-A3-06 — The suite guides name five skills and three agents; reality differs.** "The skills `run-batch`,
`plan-batch`, `real-stack-testing`, `validate-real-stack`, `test-driven-development` … are byte-identical mirrors"
(`PlantLibrary_AndroidApp/CLAUDE.md:59-65`, same in every suite). AndroidApp also carries `impeccable` in
`.claude/skills` and `.agents/skills`, PyApp `impeccable` and `gui-validation`; AndroidApp's guide never names
impeccable, PyApp's governs it (`PlantLibrary_PyApp/CLAUDE.md:24-96`, row-activated only). *Meaning:* the procedure
bullet and the roster are B1-dependent text.

**F-A3-07 — The suite `AGENTS.md` files already drift.** Their Codex section claims live mirroring ("They mirror
`.claude/` byte-for-byte", `PlantLibrary_Workspace/AGENTS.md:8-11`); their deliverable bullet names only three folders
(`PlantLibrary_Workspace/AGENTS.md:28`, `PlantLibrary_Server/AGENTS.md:30`) because A-8 rewrote only the `CLAUDE.md`
sections and PyApp's `AGENTS.md` (`repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md:633`). *Meaning:*
under a freeze the banner must say that `CLAUDE.md` is the live text, or a Codex reader trusts stale rules.

**F-A3-08 — TARGET's `.agents/README.md` is a stale Conductor copy.** It names Harness_V1, the v5 proposal, a
`CLAUDE.md`/`AGENTS.md` shared-block diff, a `v5-section-reader` row and `../.Claude`
(`SW_Development/.agents/README.md:3`, `:10-20`, `:36`), while TARGET's checker says "this workspace has no
CLAUDE.md/AGENTS.md shared-block contract" (`SW_Development/scripts/harness/check_harness_parity.py:4-6`). *Meaning:*
B1 rewrites it from the Conductor's freeze paragraph (`C:/Programmierung/Orchestrator_System/.agents/README.md:6-22`)
before B2's roster section points at it.

**F-A3-09 — Nothing mechanical guards TARGET's instruction files except the hygiene block.** The hygiene checker
compares the marker region (`SW_Development/scripts/hygiene/repo_hygiene_check.py:696-710`); TARGET's parity checker
compares only `.claude`/`.codex` trees and agent stems (`SW_Development/scripts/harness/check_harness_parity.py:58-85`).
The Conductor's checker also pins `CLAUDE.md`'s proposal facts (`C:/Programmierung/Orchestrator_System/scripts/harness/check_harness_parity.py:30`,
`:324-330`), which is Conductor-specific. *Meaning:* a shared session-rules text in seven files (Q-A3-03 (b)) would
need a B7 parity check; the recommended pointer form needs none.

**F-A3-10 — Four of the Conductor's ten session rules carry Conductor values.** Rule 4 (drained boundary, an
auto-committing instance, `unattributed_dirty`; `CLAUDE.md:198-202`), rule 5 (push every commit; `:203-204`), rule 7
(D-id grep over `main`, `work`, `docs/*`, `quality/*`; `:208-209`), rule 9 (instance store `mode=ro`; `:213-214`).
Rule 5 contradicts this program's rule 5 and Q-G-03 (a) ("No session pushes", kickoff §2 item 5). Server tells
sessions to "request elevated host execution for Docker commands" (`PlantLibrary_Server/CLAUDE.md:8-9`,
`PlantLibrary_Server/AGENTS.md:10-11`), a sandbox permission that rule 10 (`CLAUDE.md:215-217`) would read as
elevation. *Meaning:* adapt as drafted in §7.2.1; rule 4 waits Q-A3-07, rule 5 waits Q-G-03.

**F-A3-11 — Package `model` cells are a parsed contract, not prose.** `parse_model_tuple` reads the leading
`<claude>/<codex>[/<cursor>]` tuple into raw tokens (`C:/Programmierung/Orchestrator_System/src/conductor/batch_package.py:176-210`);
the instance resolves them through `vendors.claude.ladder ["fable","opus","sonnet","haiku"]` and `tiers`
(`C:/Programmierung/Orchestrator_System/config.example.yaml:195-198`), CLI aliases that resolve to Fable 5.1, Opus 5.5,
Sonnet 5.5 and Haiku 4.5 (`…/AUDIT_instructions-and-skills-reconciliation_2026-10-02.md:107`). The Conductor's own
plan-batch 1.5.1 still defines the pairs as "Opus 5 ≡ GPT 5.6 Sol, Sonnet 5 ≡ GPT 5.6 Terra, Haiku 4.5 ≡ GPT 5.6
Luna" (`C:/Programmierung/Orchestrator_System/.claude/skills/plan-batch/SKILL.md:101-108`); D-OP's rewrite has not
landed. *Meaning:* B2 and B4 never rewrite a package `model` cell into "Opus 5.5 · high"; rule 1 states the mapping.
`haiku/luna` rows exist in Workspace V1, SDA, PyApp, AndroidApp, Dashboard, Server and SharedContracts (§7.3), which
map to Haiku 4.5, outside the Fable/Opus/Sonnet set (Q-A3-04).

**F-A3-12 — Old model words outside the nine files are historical records.**
`PlantLibrary_Workspace/implementation/System_Design_Architecture/MODEL_RECOMMENDATION.md:3-23` (Sonnet 5, Opus 4.8,
Fable 5); "Opus 5 ·"/"Sonnet 5 ·" ladders in `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` (51 lines),
`onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` (21), `PlantLibrary_Workspace/methodology/Design_Template_Initiative/RUNBOOK_GUI_REWORK.md`
(35), three `handovers/FINDING_kit-*` files and `repo-hygiene/PROMPT_kit-bootstrap-session_2026-09-15.md` (3).
*Meaning:* not edited; rule 1's "older text means the current model" covers them (`C:/Programmierung/Orchestrator_System/CLAUDE.md:186-188`).

**F-A3-13 — PyApp loads two overlapping guides, one stale.** `PlantLibrary_PyApp/.claude/CLAUDE.md` (119 lines,
last commit `5510798`, 2026-07-04) sits beside `PlantLibrary_PyApp/CLAUDE.md`, which delegates to it
(`PlantLibrary_PyApp/CLAUDE.md:5`); Claude Code reads both `./CLAUDE.md` and `./.claude/CLAUDE.md` as project
instructions (documented behaviour, not measured here). Stale facts: "59 test files" (`.claude/CLAUDE.md:66`) against
102 tracked test files; no real-stack doctrine, no package or Conductor rule; its architecture rules
(`:70-95`) duplicate `PlantLibrary_PyApp/AGENTS.md:53-97`. Archived prompts cite the path
(`PlantLibrary_PyApp/implementation/Archive_PreMVP/Prompts/P0_phase0_foundations.md:14` among nine citing files). `claude-sonnet-4-6`
(`.claude/CLAUDE.md:20`) is the product's `AI_EXTRACTION_MODEL` (`PlantLibrary_PyApp/app/constants.py:108`), correct
and not a session model. *Meaning:* Q-A3-05.

**F-A3-14 — Three PyApp command lists offer an unscoped test-runner line as "all tests".**
`PlantLibrary_PyApp/CLAUDE.md:15`, `PlantLibrary_PyApp/AGENTS.md:41`, `PlantLibrary_PyApp/.claude/CLAUDE.md:30`; the
batch section narrows correctly (`PlantLibrary_PyApp/CLAUDE.md:376-378`). The Conductor's "Cheapest gate first;
narrowest rerun after a red" (`C:/Programmierung/Orchestrator_System/CLAUDE.md:138-144`) is the rule that settles it.
*Meaning:* B2 adds the rule and rewords the comment of that line (the command list is the suite's, the wording B2's).

**F-A3-15 — `SCOPE.md`/`CONTEXT_INDEX.md` have no machine contract; the skill's vocabulary is TARGET's.** Conductor
requires four files only (`C:/Programmierung/Orchestrator_System/src/conductor/batch_package.py:53-58`); the handbook
calls the other two convention (`…/docs/handbook/03-batch-workflow.md:69-75`). run-batch reads only "Hard scope" and
"standing invariants" (`SW_Development/.claude/skills/run-batch/SKILL.md:32`) and checks reads against the CONTEXT_INDEX
"source map / external-context entries" and "Do not read as V1 context" (`C:/Programmierung/Orchestrator_System/.claude/skills/run-batch/SKILL.md:94-97`,
TARGET's copy `:96`). TARGET's seven CONTEXT_INDEX files use exactly those headings; the Conductor's own use "May
read"/"Must NOT read" (`…/implementation/Conductor_V2/CONTEXT_INDEX.md:5`, `:46`). *Meaning:* §7.5: keep TARGET's
headings; add a Traceability section.

**F-A3-16 — The design installer places its block before a heading that names "Claude", else appends.**
`C:/Programmierung/Design_Template_Kit/anchoring-kit/INSTALL.md:48-55`. No TARGET suite guide has such a heading,
so B5's block would land after the hygiene block. In the Conductor it sits above `## Claude subagent roster`
(`C:/Programmierung/Orchestrator_System/CLAUDE.md:219-234`). *Meaning:* B2 adds `## Claude subagent roster` before B5
installs in Dashboard, AndroidApp and PyApp.

**F-A3-17 — Living documentation needs a standard TARGET does not have.** The Conductor section
(`C:/Programmierung/Orchestrator_System/CLAUDE.md:250-258`) binds `docs/**` to `docs/authoring/standard.md` (538 lines,
"the complete living contract for everything under `docs/`", `…/docs/authoring/standard.md:7-9`) and a link gate.
TARGET suites with `docs/`: AndroidApp, Dashboard, Server, Workspace. *Meaning:* hold for A2/B7 (Q-A3-06).

**F-A3-18 — The Conductor's scratch paragraph names a skill and a script TARGET only half has.**
`C:/Programmierung/Orchestrator_System/CLAUDE.md:145-157` (`reclaim_scratch.py`, the `scratch-gate` skill). PyApp has
`reclaim_scratch.py` (`PlantLibrary_PyApp/CLAUDE.md:344-350`); no suite has `scratch-gate`. *Meaning:* the pointer
sentence waits on B1's skill decision.

**F-A3-19 — The Conductor's deliverable-naming section is weaker than TARGET's.** It is Conductor_V2-specific and
points at its own register (`C:/Programmierung/Orchestrator_System/CLAUDE.md:159-178`); TARGET has the kit block plus a
pointer section that run-batch §6.10 and plan-batch §5.4 cite (`PlantLibrary_Workspace/CLAUDE.md:86-94`). The
Conductor also closed `PROMPTS_` to new files (`…/Conductor_V2/STATE.md:44153-44154`, answer d.1). *Meaning:* keep
PlantLibrary's; record only.

## §3 Candidates

| RC | Source path @ pin | What | Verdict | Target repo and path | Lane | Q id |
|---|---|---|---|---|---|---|
| RC-A3-01 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:180-217` @ `2e7adb3` | The session-rules block (ten rules, scoped "operator and orchestrated sessions; a worker follows run-batch/SCOPE.md") | adapt: six rules with TARGET values, rule 4 and 5 conditional, draft in §7.2.1; replaces nothing (no such section exists); if wrong, sessions keep following runbook-only rules | `SW_Development/CLAUDE.md` new `## Session rules`; pointer section in six suite `CLAUDE.md` | B2 | Q-A3-03, Q-A3-07, Q-G-03 |
| RC-A3-02 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:186-191` @ `2e7adb3` | Rule 1, models: aliases → Fable 5.1/Opus 5.5/Sonnet 5.5, older words mean 5.5, session ladder | adapt: drop "v5 §5.4, AM-134"; add the package-tuple sentence (instance 2 resolves `opus/sol` etc.); if wrong, a session rewrites `model` cells and breaks instance-2 parsing | inside RC-A3-01 | B2 | Q-A3-04 |
| RC-A3-03 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:135-137` @ `2e7adb3` | "Leave what you did not make" bullet | adopt verbatim minus "(AC51)" (a Conductor id); replaces nothing; if wrong, sessions delete pre-existing dead code in passing | `SW_Development/CLAUDE.md` `## Engineering standards`; one bullet in each suite `CLAUDE.md` | B2 | — |
| RC-A3-04 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:138-144` @ `2e7adb3` | "Cheapest gate first; narrowest rerun after a red" | adapt: the per-suite gate commands (§7.2) and no closeout-matrix sentence where the suite has no harness; replaces the "all tests" comment's implied default (F-A3-14); if wrong, sessions keep improvising unscoped runs | each suite `CLAUDE.md` `## Build and test`; generic form in `SW_Development/CLAUDE.md` | B2 | — |
| RC-A3-05 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:21-34` @ `2e7adb3` | "A prompt never overrides a skill" and "deviations need a recorded decision" | adapt: paths to TARGET (package `STATE.md`, `hygiene/HYGIENE_DECISIONS.md`, `rework/` runbook); the D-2026-08-26-07 reference becomes "a package amendment to the row's `validation` cell recorded in `STATE.md`"; replaces the same sentence living only in the hygiene block; if wrong, a pasted runbook prompt widens a proof surface | `SW_Development/CLAUDE.md` `## Authority` | B2 | — |
| RC-A3-06 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:19-20` @ `2e7adb3` | Precedence: a schema, state table or config wins over prose | adapt: "a SharedContracts schema, contract or generated artifact wins over prose"; if wrong, a guide's prose overrides a contract | `SW_Development/CLAUDE.md` `## Authority` | B2 | — |
| RC-A3-07 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:36-46` @ `2e7adb3` | Repo layout table | adapt: the seven repositories and the superproject roots (`hygiene/`, `repo-hygiene/`, `onboarding/`, `handovers/`, `rework/`, `scripts/harness/`, `scripts/hygiene/`, `.claude/`); if wrong, sessions guess roots and trip the root allowlist | `SW_Development/CLAUDE.md` `## Repository layout` | B2 | — |
| RC-A3-08 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:48-60` @ `2e7adb3` | Workflow: plan/run with an explicit package path; progress truth; batch sizing | adapt: suite cwd plus package path; one gitlink commit per step (kickoff §2 item 5); batch sizing only if a TARGET decision exists (not found; omit); if wrong, bare `/run-batch` picks the wrong package (Workspace has four) | `SW_Development/CLAUDE.md` `## Workflow` | B2 | — |
| RC-A3-09 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:62-69` @ `2e7adb3` | Reading v5 cheaply (pinned facts, section reader) | retire: no v5 proposal and no `v5-section-reader` in TARGET | — | — | — |
| RC-A3-10 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:71-99` @ `2e7adb3` | Architecture invariants (v5) | keep PlantLibrary's: product invariants live in each package `SCOPE.md` `## Standing invariants` and the suite guides | — | — | — |
| RC-A3-11 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:131-134` @ `2e7adb3` | Windows-first; no secrets in code, config examples, fixtures, logs or commits | adopt the secrets bullet verbatim, adapt Windows-first (drop Job Objects/NSSM); replaces PyApp's narrower keyring line only in the superproject; if wrong, a chat id or key lands in evidence | `SW_Development/CLAUDE.md` `## Engineering standards` | B2 | — |
| RC-A3-12 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:114-121` @ `2e7adb3` | Never fake the layer under test | keep PlantLibrary's: `SW_Development/CLAUDE.md:3-7` is the operator's generic version | — | — | — |
| RC-A3-13 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:122-125` @ `2e7adb3` | E-03r: "After implementing a `real-stack-testing` row … Its `real-stack-validator` subagent …" | adapt: replaces exactly `SW_Development/CLAUDE.md:10-12`'s "After implementation … Its Sonnet/Terra worker …"; if wrong (operator wants the block untouched), the stale rung word stays | `SW_Development/CLAUDE.md:10-12` | B2 | Q-A3-02 |
| RC-A3-14 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:126-129` @ `2e7adb3` | GUI tests assert DOM, request and persisted state; a skipped browser test is never evidence | adapt: the skip sentence into `PlantLibrary_Dashboard/CLAUDE.md` `## Build and test` (the one Playwright suite); the rest is the operator's `SW_Development/CLAUDE.md:13-14`; if wrong, a skipped e2e run is cited as evidence | `PlantLibrary_Dashboard/CLAUDE.md` | B2 | — |
| RC-A3-15 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:145-157` @ `2e7adb3` | Scratch: never elevated, never a basetemp outside the repository, the scratch gate | adapt: the two "never" clauses into each Python suite's `## Scratch policy` (PyApp has the second at `PlantLibrary_PyApp/CLAUDE.md:399-400`); the gate sentence only if B1 ports `scratch-gate`; if wrong, an elevated run leaves scratch the operator cannot reclaim (`CD2-B305`) | `PlantLibrary_PyApp`, `PlantLibrary_Server`, `PlantLibrary_SharedContracts` `CLAUDE.md` | B2 (after B1) | — |
| RC-A3-16 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:159-178` @ `2e7adb3` | Deliverable naming and proof-surface paragraph | keep PlantLibrary's (kit block + pointer section, F-A3-19) | — | — | — |
| RC-A3-17 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:234-248` @ `2e7adb3` | Claude subagent roster with one model word per agent and the `.agents/README.md` pointer | adapt: three agents (no section reader) with the models B1 lands; the pointer only after B1 rewrites `.agents/README.md`; new section, replaces the agent half of the suites' "Procedure" bullet; if wrong, the roster names models the agent files do not carry | `SW_Development/CLAUDE.md` and six suite `CLAUDE.md`, above the hygiene block | B2 (after B1) | — |
| RC-A3-18 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:219-232` @ `2e7adb3` | The design-kit marker block | record only: installer-owned; B5 installs it; B2 never hand-writes it but adds the roster heading it is placed above (F-A3-16) | Dashboard, AndroidApp, PyApp `CLAUDE.md`/`AGENTS.md` | B5 | Q-G-01, Q-A3-01 |
| RC-A3-19 | `C:/Programmierung/Orchestrator_System/CLAUDE.md:250-258` @ `2e7adb3` | Living documentation section | hold until A2/B7 decide a docs standard for TARGET | AndroidApp, Dashboard, Server, Workspace `CLAUDE.md` | B7 then B2 | Q-A3-06 |
| RC-A3-20 | `C:/Programmierung/Orchestrator_System/AGENTS.md:3` @ `2e7adb3` | The one-line frozen notice under the title | adapt: the decision reference becomes the Q-G-09 answer's record; inserted after line 1 (+ blank) in each suite `AGENTS.md`, as line 1 in the superproject's (it has no title); if wrong, Codex readers trust stale "Rules restated" text | seven `AGENTS.md` | B2 | Q-G-09, Q-A3-01 |
| RC-A3-21 | `C:/Programmierung/Orchestrator_System/scripts/harness/check_harness_parity.py:54-76`, `:239-253` @ `2e7adb3` | `check_agents_frozen`: `AGENTS.md` equals its frozen blob, the notice line excepted | adapt: digest with every `<!-- *:begin -->`…`<!-- *:end -->` region removed, so installers keep their blocks; replaces the `.claude`/`.codex` tree compare for `AGENTS.md`; if wrong, the first hygiene re-pin or B5 install is a parity red | `SW_Development/scripts/harness/check_harness_parity.py` | B7 | Q-A3-01, Q-G-09 |
| RC-A3-22 | `C:/Programmierung/Orchestrator_System/.agents/README.md:6-22` @ `2e7adb3` | The freeze paragraph: kept, never deleted, not mirrored; unfreeze act; the checker's freeze mode | adapt (B1's file): TARGET decision reference; replaces `SW_Development/.agents/README.md:3-20` | `SW_Development/.agents/README.md` | B1 | Q-G-09 |
| RC-A3-23 | `PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/SCOPE_TEMPLATE.md:20-67` @ `6b4b88b` | Hard scope split into touchable / read-only / never touched; standing invariants; optional configuration binding and Conductor execution rules | adapt for the seven packages' `## Hard scope` body (headings unchanged); the Conductor-execution rules stay in the suite guides, not duplicated | seven `implementation/*/SCOPE.md` | B4 (A7 owns rows) | — |
| RC-A3-24 | `C:/Programmierung/Orchestrator_System/implementation/Harness_V1/CONTEXT_INDEX.md:54-58`; `…/Conductor_V2/CONTEXT_INDEX.md:85-90` @ `2e7adb3` | A Traceability section: what a row's `baseline_id` may cite | adapt: one `## Traceability` per package with its own baseline vocabulary (A7 supplies values); if wrong, untraceable rows go unflagged | seven `implementation/*/CONTEXT_INDEX.md` | B4 | — |
| RC-A3-25 | `…/PLAN_instructions-and-skills-reconciliation_2026-10-02.md:504-532`, `:547-660` @ `2e7adb3` | Act shape: decision first, text-anchored edits, acceptance list, paste blocks naming no proof surface | adapt for B2's step blocks: acceptance = hygiene checker verdict unchanged, `git ls-files --eol` unchanged, `git diff --stat` only the listed files; no drained-boundary item unless Q-A3-07 | `rework/PROMPTS_master-rework-runbook_2026-10-13.md` §3 (B2 rows) | R-3 | — |
| RC-A3-26 | `…/PLAN_instructions-and-skills-reconciliation-addendum_2026-10-02.md:424-439` @ `2e7adb3` | Order: freeze first, checker freeze mode, then `CLAUDE.md`-only edits | adopt as B1 → B2 → B7 dependency; replaces nothing | runbook §3a | R-3 | Q-G-09 |
| RC-A3-27 | `PlantLibrary_PyApp/.claude/CLAUDE.md` @ `35ddc63` | Stale duplicate guide | adapt: fold unique rules into `PlantLibrary_PyApp/CLAUDE.md`, leave a pointer stub (archived citers resolve); if wrong, two contradicting guides load per session | `PlantLibrary_PyApp/.claude/CLAUDE.md`, `PlantLibrary_PyApp/CLAUDE.md` | B2 | Q-A3-05 |
| RC-A3-28 | `…/AUDIT_instructions-and-skills-reconciliation_2026-10-02.md:181-198` @ `2e7adb3` | Review of instructions written for a weaker model (emphatic absolutes) | record only: method for B2's read-through of the suite guides; no site found in the nine files beyond PyApp's "No exceptions." (`PlantLibrary_PyApp/CLAUDE.md:54`), which is a product rule | — | B2 | — |
| RC-A3-29 | `PlantLibrary_Server/CLAUDE.md:8-9` @ `f1a31b9` | "request elevated host execution" for Docker | adapt: "request the sandbox permission for the Docker named pipe; this is not Windows elevation (session rule 10)"; if wrong, rule 10 and the Server guide contradict | `PlantLibrary_Server/CLAUDE.md:8-9` (AGENTS.md stays frozen) | B2 | — |

## §4 Questions for the operator

| Q | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A3-01 | If Codex is frozen (Q-G-09 (a)), what exactly is frozen in an `AGENTS.md` that carries installer-owned blocks? | (a) the text outside marker blocks: a banner line is added once, the hygiene and design installers keep owning their blocks, and B7's guard digests `AGENTS.md` with every `<!-- *:begin -->…<!-- *:end -->` region removed; (b) the whole bytes, and every installer run is followed by restoring `AGENTS.md`; (c) no freeze: `AGENTS.md` becomes a five-line pointer plus the blocks | The hygiene checker's block-parity check requires the block in `AGENTS.md` (F-A3-03); the design installer creates or rewrites `AGENTS.md`; (b) is what left the Conductor's design block at 0.8.0 and cost a parked closeout (`fe4618a`) | B2 banner steps; B7 guard; B5 install in the three clients |
| Q-A3-02 | May B2 change one sentence of the operator's `## Testing` block, `SW_Development/CLAUDE.md:10-12` ("Its Sonnet/Terra worker …")? | (a) yes, to the Conductor's executed E-03r wording (`C:/Programmierung/Orchestrator_System/CLAUDE.md:122-125`), rest of the block byte-for-byte; (b) no, keep the block verbatim and let session rule 1 explain the old word | The same sentence was already replaced in the Conductor under `D-2026-10-04-07`; "Terra" names a frozen Codex rung, and "after implementation" is wider than run-batch's "after a `real-stack-testing` row" (ir-1 C-11) | B2 superproject step (that sentence only) |
| Q-A3-03 | Where do the session rules live across seven repositories? | (a) the full block in `SW_Development/CLAUDE.md`; each suite `CLAUDE.md` gets a short `## Session rules` section: one pointer line naming the superproject file plus that suite's parameters; (b) the identical full block in all seven `CLAUDE.md` with a B7 parity check; (c) superproject only | One text, no drift (F-A3-09); suites are always checked out as submodules here and instance 2 binds them under `SW_Development`; the pointer still names the path when a suite is opened alone | B2 suite steps |
| Q-A3-04 | `haiku/luna` package rows resolve to Haiku 4.5, outside the Fable/Opus/Sonnet set. What does rule 1 say about them? | (a) keep every `model` cell as it is (a parsed contract); rule 1 says `haiku` is a worker tier only, never a session or subagent model; a re-tier is a plan-batch amendment per row by B4 when the row is next touched; (b) B4 re-tiers every `haiku/luna` row to `sonnet/terra` now | Rewriting cells is a package edit with a `STATE.md` decision per package (kickoff §2 item 4) for no executed change; most `haiku/luna` rows are `risk: L` mechanical rows by plan-batch's own rule | B2 (rule 1's last sentence); B4 |
| Q-A3-05 | `PlantLibrary_PyApp/.claude/CLAUDE.md` (stale, loaded beside `CLAUDE.md`) | (a) fold its unique rules (layer rules, threading, sessions, schema changes, providers, testing, do-not) into `PlantLibrary_PyApp/CLAUDE.md` and reduce the file to a three-line pointer stub; (b) refresh it in place; (c) remove it | (a) ends double loading of contradicting text; the stub keeps the path that archived prompts cite (F-A3-13); (c) leaves those citers dangling | B2 PyApp step |
| Q-A3-06 | Does TARGET adopt the Conductor's living-documentation rule now? | (a) hold until A2/B7 decide whether a docs standard and link gate are adopted per suite; B2 writes nothing; (b) B2 adds one line "a batch that changes user-visible behaviour updates the affected `docs/**` pages and names them in its row" to the four suites with `docs/` | A rule without its standard and gate is the half the Conductor did not adopt (`D-2026-09-08-14` adopted both together, `C:/Programmierung/Orchestrator_System/CLAUDE.md:254-258`) | B2 (that section only) |
| Q-A3-07 | Rule 4 (drained boundary) for suites bound to Conductor instance 2 | (a) adapt: "a tracked file in a suite whose project is bound on instance 2 changes only while that project is held and no attempt is open (store read `mode=ro`)"; (b) omit until B8 verifies statically whether instance 2 auto-commits a suite repository | The Conductor's reason (a foreign edit during an attempt parks `unattributed_dirty`, `C:/Programmierung/Orchestrator_System/CLAUDE.md:198-202`) is product behaviour, not repository-specific; PyApp is held at `PY1-B08` today | B2 (rule 4 text); B8 |

## §5 Reusable things this brief did not name

- The addendum's freeze application table (`…/PLAN_instructions-and-skills-reconciliation-addendum_2026-10-02.md:441-475`):
  every edit classified "CLAUDE.md only / dropped / re-stated" under the freeze. The same table shape fits B1/B2.
- The `fe4618a` commit message: the concrete failure mode of a frozen `AGENTS.md` (a docs section added to both files).
- The operator's model rule as recorded (`…/Conductor_V2/STATE.md:44159-44165`, `D-2026-10-02-23` (b)(2)): sessions on
  Opus 5.5 high/xhigh, Fable 5.1 where it pays off, Sonnet 5.5 only for subagents; read-only work first, in parallel.
- `config.example.yaml:195-198` as the authority for alias → tier (`fable: T4, opus: T3, sonnet: T2, haiku: T1`) and
  its note "fable tuples are for `…P` planning batches only" — useful for B4 if a package ever writes a `fable` tuple.
- The design kit's `--rule-block-before "CLAUDE.md=## …"` flag (`C:/Programmierung/Design_Template_Kit/anchoring-kit/INSTALL.md:52-54`):
  B5 can name the roster heading explicitly instead of relying on the word "Claude".
- The Conductor checker's `INSTRUCTION_SHARED_END_MARKER` idea (`…/scripts/harness/check_harness_parity.py:88-95`): a
  named heading as the end of a shared region — the mechanism for Q-A3-03 (b) if chosen.
- The methodology's own `SCOPE_TEMPLATE.md` "Conductor execution rules" (`PlantLibrary_Workspace/methodology/GUI_Improvement_Methodology/SCOPE_TEMPLATE.md:58-67`),
  already TARGET-owned, for B6's design-migration workspaces.
- ir-1's CLI fact table (`…/AUDIT_instructions-and-skills-reconciliation_2026-10-02.md:100-115`): alias resolution,
  `--effort` levels, `--fallback-model`, `--permission-prompts none` — the facts B2's rule 1 and rule 3 rest on.

## §6 Claims to verify

1. **The Conductor's `AGENTS.md` is its freeze blob plus two lines.** Check:
   `git --no-optional-locks -C C:\Programmierung\Orchestrator_System diff --stat 10177e3 HEAD -- AGENTS.md`
   prints `1 file changed, 2 insertions(+)`.
2. **Both installers write `AGENTS.md`.** Check: `sed -n 42p C:/Programmierung/Design_Template_Kit/anchoring-kit/INSTALL.md`
   names `CLAUDE.md`, `AGENTS.md` and "`AGENTS.md` is created if missing"; `sed -n 40p C:/Programmierung/Repo_Hygiene_Template_Kit/installer/INSTALL.md`
   names `CLAUDE.md`, `AGENTS.md` and the marked rule block.
3. **Package `model` cells are positional tokens resolved by the instance ladder.** Check:
   `sed -n 183,210p C:/Programmierung/Orchestrator_System/src/conductor/batch_package.py` shows
   `MODEL_TUPLE_VENDOR_ORDER = ("claude", "codex", "cursor")` and the raw-token parse; `sed -n 195,198p
   C:/Programmierung/Orchestrator_System/config.example.yaml` shows `ladder: ["fable", "opus", "sonnet", "haiku"]`.

## §7 The blueprint

### §7.1 The Conductor `CLAUDE.md` anatomy (`C:/Programmierung/Orchestrator_System/CLAUDE.md` @ `2e7adb3`)

| Section (lines) | Purpose | Class | Parameters / why specific | Model names today |
|---|---|---|---|---|
| Title and intro (:1-8) | what the repository is | parameterised | name, one paragraph | none (names the Claude Code, Codex and Cursor CLIs, no versions) |
| `## Authority` (:10-34) | normative source, history, precedence, a prompt never overrides a skill, deviations need a recorded decision | parameterised (generic core :19-31) | active package path, proposal path and its line count (:12-14), the amendment decision shape `D-2026-08-26-07` (:31), the `STATE.md` path and §18 gate (:32-34) | none |
| `## Repo layout` (:36-46) | path → purpose table | parameterised | the package, proposal, `SCOPE.md`, `CONTEXT_INDEX.md`, `src/`, `tests/` rows | none |
| `## Workflow` (:48-60) | plan/run commands, progress truth, traceability, batch sizing | parameterised | package path; baseline vocabulary (`AC<n>`, `AM-<n>`, …); sizing decision `D-2026-07-17-02` | none |
| `### Reading v5 cheaply` (:62-69) | how to read the 5,808-line proposal | Conductor-specific | line count and Section-Map range pinned by the parity checker | names the `v5-section-reader` agent |
| `## Architecture invariants (v5)` (:71-99) | product invariants | Conductor-specific | v5 AC/AM ids | `claude-haiku-4-5`, `claude-sonnet-5` (:76, the Decision Brain's product config) |
| `## Engineering standards` (:101-157) | runtime deps (:103-109, specific), dev tooling (:110-111, specific), offline tests (:112-113, specific values), never fake the layer under test (:114-121, generic with module names), validate-real-stack (:122-125, generic), GUI test failure modes (:126-129, generic), executable assertions not screenshots (:130, specific refs), Windows-first (:131-132, generic for this machine), secrets (:133-134, generic), leave what you did not make (:135-137, generic), cheapest gate first (:138-144, parameterised: gate commands, closeout matrix), scratch under `.tmp/` and the scratch gate (:145-157, parameterised: paths, `reclaim_scratch.py`, `scratch-gate`, `CD2-B305`) | mixed | as listed | none ("subagent" only) |
| `## Deliverable naming` (:159-178) | file naming and the proof-surface rule for prompts and handovers | parameterised | folders, TYPE list, index register, retrofit note, enforcing test name | none |
| `## Session rules` (:180-217) | ten rules for operator and orchestrated sessions; workers excluded (:182-184) | generic in shape | 1 models (generic); 2 one closeout at a time, `.tmp/p/<slug>` (parameterised); 3 headless, cannot ask, Telegram enqueue, foreground timeout (generic + Telegram); 4 drained boundary (instance-specific); 5 push policy (parameterised); 6 bytes (generic); 7 D-id grep branch set (parameterised); 8 subagents (generic); 9 live checkout `--no-optional-locks`, store `mode=ro` (parameterised); 10 elevation (generic) | :186-191: `fable`/`opus`/`sonnet` → Fable 5.1, Opus 5.5, Sonnet 5.5; "Sonnet 5"/"Opus 5" mean the 5.5 model; sessions Opus 5.5 high/xhigh, Fable 5.1 with a stated reason, Sonnet 5.5 only for subagents |
| design-kit block (:219-232) | design system rules | installer-owned (Kit 1.3.1) | Kit path and version | none |
| `## Claude subagent roster` (:234-248) | the agents, "if this invocation can spawn agents" rule, pointer to `.agents/README.md` | parameterised | the agent set (four) | :239-246: Sonnet (validator, section reader, plan auditor), Opus (closeout reviewer) |
| `## Living documentation` (:250-258) | `docs/**` updated in the batch that changes behaviour | parameterised | `docs/` tree, the standard, adoption decision `D-2026-09-08-14`, gate test | none |

The shared-block end for the frozen compare was `## Claude subagent roster` (`…/scripts/harness/check_harness_parity.py:93-95`); since the freeze only `CLAUDE.md` is live.

### §7.2 Per TARGET file

Nine blueprints: the superproject's `CLAUDE.md` and `AGENTS.md`, one per suite covering its `CLAUDE.md` and `AGENTS.md`,
and PyApp's `.claude/CLAUDE.md`. **Installer-owned bytes, never touched by hand:** the hygiene block between
`<!-- repo-hygiene:begin -->` and `<!-- repo-hygiene:end -->` in all fourteen `CLAUDE.md`/`AGENTS.md` (line ranges in each
table), and from B5 on the design-kit block. **Bytes:** every one of the fifteen files is `i/lf w/crlf`; B2 checks
`git ls-files --eol` before and after and writes CRLF back. **Placement rule for every suite `CLAUDE.md`:** new sections
go above `## Deliverable naming`, except `## Claude subagent roster`, which goes between `## Deliverable naming` and the
hygiene block so B5's design block lands directly above it (F-A3-16); the hygiene block stays last.

#### §7.2.1 Draft of the adapted session rules (for `SW_Development/CLAUDE.md`; wording is B2's)

```markdown
## Session rules (operator and orchestrated sessions)

These bind every session an operator or orchestrator starts in this superproject or a
submodule. A Conductor instance-2 worker follows run-batch/plan-batch and the package
SCOPE.md instead: it never commits or pushes.

1. Models. `fable`, `opus`, `sonnet` resolve to Fable 5.1, Opus 5.5 and Sonnet 5.5;
   "Fable 5"/"Opus 5"/"Sonnet 5" in older text means the current model. A session runs on
   Opus 5.5 at high or xhigh; Fable 5.1 only where a wrong judgment costs weeks, with the
   reason stated; Sonnet 5.5 only for subagents. A package `model` cell (`opus/sol`,
   `sonnet/terra`, `haiku/luna`) is a worker tier tuple that instance 2 resolves through its
   config; it is never rewritten, and its Codex half is inert while codex is disabled.
   [Q-A3-04: the `haiku` sentence.]
2. One test slot. One closeout at a time on the machine and no test load beside it; a run a
   session starts on its own uses `.tmp/p/<slug>` in that suite.
3. Headless. A headless session cannot ask: it stops with the question in its report (and in
   the open program's question register). It never ends its turn while background work runs:
   long commands run in the foreground with a tool timeout up to 3,600,000 ms.
4. [Q-A3-07] Bound suites: …
5. [Q-G-03] Commits: …
6. Bytes. Instruction and package files are LF in the index and CRLF in this checkout: write
   back the file's own line endings (`git ls-files --eol`); never a text-mode rewrite, never a
   `core.autocrlf` change.
7. Decision ids. Mint a `D-<date>-<nn>` only after a grep over the superproject and each
   submodule (`git -C <repo> grep`; `--recurse-submodules` returns superproject hits only) and
   every worktree.
8. Subagents. Fan out in one message with a fixed return schema; a verdict is a claim,
   verified once on the critical path; one that dies on a limit is finished inline or
   recorded as not read.
9. Read-only sources. Git reads in a Conductor checkout use `--no-optional-locks`; instance 2
   is read from its store `mode=ro`, never polled over REST.
10. Elevation. Nothing runs elevated unless the operator's own act says so, and nothing is
    quoted from a credential or a config file beyond the keys a step names. A sandbox
    permission (Server's Docker pipe) is not elevation.
```

#### 1. `SW_Development/CLAUDE.md` (33 lines)

| Section | Action | Source / parameters | Notes |
|---|---|---|---|
| (title) | add | `# SW_Development — PlantLibrary superproject` and a three-line purpose (seven repositories, the program roots) | above `## Testing`; changes no operator byte |
| `## Testing` (:1-14) | keep as is, except :10-12 | the operator's block | :10-12 hold (Q-A3-02); RC-A3-13 |
| `## Authority` | add | RC-A3-05, RC-A3-06 | names package `STATE.md`, `hygiene/HYGIENE_DECISIONS.md`, the rework runbook |
| `## Repository layout` | add | RC-A3-07 | seven repositories + roots |
| `## Workflow` | add | RC-A3-08 | explicit package path; gitlink bump per step |
| `## Engineering standards` | add | RC-A3-03, RC-A3-04 (generic form), RC-A3-11 | no product invariants (RC-A3-10) |
| `## Session rules (operator and orchestrated sessions)` | add | §7.2.1 | rules 4, 5 hold (Q-A3-07, Q-G-03); placement per Q-A3-03 |
| `## Claude subagent roster` | add (after B1) | RC-A3-17: three agents, the models B1 lands; pointer to `.agents/README.md` once B1 rewrote it | — |
| `## Living documentation` | hold | Q-A3-06 | — |
| hygiene block (:16-33) | keep — installer-owned | — | stays last |

#### 2. `SW_Development/AGENTS.md` (33 lines, byte-identical to `CLAUDE.md` today)

| Section | Action | Source / parameters | Notes |
|---|---|---|---|
| line 1 | add (Q-G-09 (a)) | RC-A3-20: `> Frozen <date> (<Q-G-09 record>): codex disabled; `CLAUDE.md` is the live text.` + blank line | no title to put it under |
| `## Testing` (:1-14) | keep as is (frozen) | — | not mirrored from `CLAUDE.md` after the freeze, so Q-A3-02's edit does not apply here |
| hygiene block (:16-33) | keep — installer-owned | — | Q-A3-01 decides how the freeze guard treats it |
| everything B2 adds to `CLAUDE.md` | remove from scope | the freeze | under Q-G-09 (b) this file's fate is B1's |

#### 3. `PlantLibrary_Workspace` (`CLAUDE.md` 113 lines; `AGENTS.md` 47)

| Section | Action | Source / parameters | Notes |
|---|---|---|---|
| title/intro (:1-6) | keep | — | — |
| `## Build and test` (:8-19) | keep; add one bullet | RC-A3-04, gate = the two checkers at :13-14 | no lint exists |
| `## Packages: live, gated, terminal` (:21-34) | keep | — | B3/B4 may change the table (archive) |
| `## Batch packages and Conductor` (:36-74) | keep; replace the skill list in "Procedure" (:53-59) | B1's final set | :71-74 cites `SUITE_HANDOFFS.md`: replace when B4 retires it (Q-G-05) |
| `## Engineering standards` | add | RC-A3-03 | one bullet |
| `## Session rules` | add | Q-A3-03 (a): pointer to `../CLAUDE.md` + rule-2 parameter (no test runner here) | — |
| `## Scratch policy` (:76-84) | keep | — | — |
| `## Deliverable naming` (:86-94) | keep as is | A-8 text, byte-identical | directly above the roster/block |
| `## Claude subagent roster` | add (after B1) | RC-A3-17 | — |
| `## Living documentation` | hold | Q-A3-06 | `docs/` exists |
| hygiene block (`CLAUDE.md:96-113`) | keep — installer-owned | — | — |
| `AGENTS.md` | add banner after :1 (Q-G-09 (a)); otherwise keep frozen | RC-A3-20 | :8-17, :28 stale (F-A3-07); hygiene block `AGENTS.md:30-47` installer-owned |

#### 4. `PlantLibrary_AndroidApp` (`CLAUDE.md` 118; `AGENTS.md` 47)

| Section | Action | Source / parameters | Notes |
|---|---|---|---|
| title/intro (:1-5), `## Build and test` (:7-34) | keep; add one bullet | RC-A3-04, gate = `lintDebug` then `:app:assembleDebug` | runtime rows out of band (:30-34) |
| `## Design context` (:36-43) | keep until B5; then replace by a pointer to the design-kit block | B5, Q-G-01, Q-G-07 | — |
| `## Batch packages and Conductor` (:45-79) | keep; replace the skill list (:59-65) | B1's set, which must name `impeccable` if it stays (F-A3-06) | — |
| `## Engineering standards`, `## Session rules` | add | as Workspace; rule-2 parameter: the emulator is the test slot's | — |
| `## Scratch policy` (:81-89), `## Deliverable naming` (:91-99) | keep as is | — | — |
| `## Claude subagent roster` | add (after B1, before B5) | RC-A3-17 | B5's block lands above it |
| `## Living documentation` | hold | Q-A3-06 | `docs/` exists |
| hygiene block (`CLAUDE.md:101-118`; `AGENTS.md:30-47`) | keep — installer-owned | — | — |
| `AGENTS.md` | banner after :1; frozen | RC-A3-20 | — |

#### 5. `PlantLibrary_Dashboard` (`CLAUDE.md` 110; `AGENTS.md` 47)

| Section | Action | Source / parameters | Notes |
|---|---|---|---|
| title/intro (:1-5), `## Build and test` (:7-28) | keep; add two bullets | RC-A3-04 (gate = `npm run lint`, then `npm run build` for `tsc -b`); RC-A3-14 (a skipped browser run is never evidence) | — |
| `## Design context` (:30-36) | keep until B5 | as AndroidApp | — |
| `## Batch packages and Conductor` (:38-72) | keep; replace the skill list | B1 | — |
| `## Engineering standards`, `## Session rules` | add | as Workspace | — |
| `## Scratch policy` (:73-81), `## Deliverable naming` (:83-91) | keep as is | — | — |
| `## Claude subagent roster` | add (after B1, before B5) | RC-A3-17 | — |
| `## Living documentation` | hold | Q-A3-06 | `docs/` exists |
| hygiene block (`CLAUDE.md:93-110`; `AGENTS.md:30-47`) | keep — installer-owned | — | — |
| `AGENTS.md` | banner after :1; frozen | RC-A3-20 | — |

#### 6. `PlantLibrary_Server` (`CLAUDE.md` 149; `AGENTS.md` 62)

| Section | Action | Source / parameters | Notes |
|---|---|---|---|
| `## Docker is the authoritative local runtime` (:3-25) | keep; replace :8-9's wording | RC-A3-29 | reconciles with rule 10 |
| `## Test-environment distinction` (:27-46), `## Evidence discipline` (:48-52) | keep | — | — |
| `## Build and test` (:54-71) | keep; add one bullet | RC-A3-04, gate = `ruff check` and `ruff format --check` on touched files | — |
| `## Batch packages and Conductor` (:73-108) | keep; replace the skill list | B1 | — |
| `## Engineering standards`, `## Session rules` | add | as Workspace | — |
| `## Scratch policy` (:110-120) | keep; add | RC-A3-15 (never elevated) | — |
| `## Deliverable naming` (:122-130) | keep as is | — | — |
| `## Claude subagent roster` | add (after B1) | RC-A3-17 | — |
| `## Living documentation` | hold | Q-A3-06 | `docs/` exists |
| hygiene block (`CLAUDE.md:132-149`; `AGENTS.md:45-62`) | keep — installer-owned | — | — |
| `AGENTS.md` | banner after :1; frozen | RC-A3-20 | its :10-11 keeps the old Docker wording (frozen) |

#### 7. `PlantLibrary_SharedContracts` (`CLAUDE.md` 108; `AGENTS.md` 47)

| Section | Action | Source / parameters | Notes |
|---|---|---|---|
| title/intro (:1-5), `## Build and test` (:7-34) | keep; add one bullet | RC-A3-04, gate = `python scripts/validate_contracts.py` (no repo lint, :28-30) | — |
| `## Batch packages and Conductor` (:36-67) | keep; replace the skill list | B1 | — |
| `## Engineering standards`, `## Session rules` | add | as Workspace | — |
| `## Scratch policy` (:69-79) | keep; add | RC-A3-15 | — |
| `## Deliverable naming` (:81-89) | keep as is | — | — |
| `## Claude subagent roster` | add (after B1) | RC-A3-17 | — |
| hygiene block (`CLAUDE.md:91-108`; `AGENTS.md:30-47`) | keep — installer-owned | — | — |
| `AGENTS.md` | banner after :1; frozen | RC-A3-20 | — |

#### 8. `PlantLibrary_PyApp` (`CLAUDE.md` 431; `AGENTS.md` 511)

| Section | Action | Source / parameters | Notes |
|---|---|---|---|
| title/intro (:1-5) | keep; replace :5 | Q-A3-05 (a): the delegation sentence goes when `.claude/CLAUDE.md` becomes a stub | — |
| `## Commands` (:9-20) | keep; reword the comment of :15 | F-A3-14, RC-A3-04 | the command list stays the suite's |
| `## Design System` (:24-96) | keep until B5; then reconcile with the design-kit block | B5, Q-G-07 | impeccable activation already row-gated |
| `## Architecture`, `## Cross-Platform`, `## Conventions`, `## Module Index` (:100-306) | keep; add an `### Architecture rules` subsection | Q-A3-05 (a): the rules folded from `.claude/CLAUDE.md:70-119` | — |
| `## Batch packages and Conductor` (:307-383) | keep; replace the skill list (:325-331) | B1 (PyApp also carries `impeccable`, `gui-validation`) | — |
| `## Engineering standards`, `## Session rules` | add | as Workspace; rule-2 parameter: `.venv\Scripts` first on `PATH` (already :369-371) | — |
| `## Scratch policy` (:385-402) | keep; add | RC-A3-15 (never elevated) | the basetemp clause exists (:399-400) |
| `## Deliverable naming` (:404-412) | keep as is | — | — |
| `## Claude subagent roster` | add (after B1, before B5) | RC-A3-17 | — |
| hygiene block (`CLAUDE.md:414-431`; `AGENTS.md:494-511`) | keep — installer-owned | — | — |
| `AGENTS.md` | banner after :1; frozen | RC-A3-20 | its `## Deliverable naming` (:471-480) is A-8's text and stays |

#### 9. `PlantLibrary_PyApp/.claude/CLAUDE.md` (119 lines)

| Section | Action | Source / parameters | Notes |
|---|---|---|---|
| whole file | replace with a three-line pointer stub (Q-A3-05 (a)) | "Project rules live in `../CLAUDE.md`." plus the date and the Q-A3-05 record | archived citers keep resolving |
| `## Architecture` (:70-95), `## Coding Standards` (:97-104), `## Testing` (:106-111), `## Do Not` (:113-119) | move to `PlantLibrary_PyApp/CLAUDE.md` | deduplicated against `PlantLibrary_PyApp/CLAUDE.md:204-211` | no change of meaning |
| `## Tech Stack` (:11-24), `## Project Structure` (:37-68), `## Commands` (:26-35) | remove | duplicated by `PlantLibrary_PyApp/CLAUDE.md` and `AGENTS.md:20-49`, :244-282; "59 test files" is stale | `claude-sonnet-4-6` stays recorded in `AGENTS.md:29` |

### §7.3 Model names

**In the nine files** (all other grep hits for opus, sonnet, fable, haiku, terra, luna, sol and gpt are absent):

| Place | Text | Maps to | Disposition |
|---|---|---|---|
| `SW_Development/CLAUDE.md:11` | "Its Sonnet/Terra worker" | Sonnet 5.5 (`real-stack-validator`, `model: sonnet`); Terra = `gpt-5.6-terra`, Codex, disabled | Q-A3-02 (E-03r wording) |
| `SW_Development/AGENTS.md:11` | same | same | frozen (Q-G-09) |
| `PlantLibrary_PyApp/.claude/CLAUDE.md:20` | `claude-sonnet-4-6` | the product's `AI_EXTRACTION_MODEL` (`PlantLibrary_PyApp/app/constants.py:108`) | record only: product config, not a session model; leaves with Q-A3-05 (a), still named in `PlantLibrary_PyApp/AGENTS.md:29` |
| suite `AGENTS.md` Codex sections (e.g. `PlantLibrary_Workspace/AGENTS.md:12-13`) | `real_stack_validator`, `batch_closeout_reviewer`, `batch_plan_auditor` | Codex role names, no model | frozen |

**In the superproject's skills and agents** (lane A1 edits them; listed because B2's roster quotes them):
`SW_Development/.claude/skills/plan-batch/SKILL.md:98-103`, `:198` and `SW_Development/.claude/skills/run-batch/SKILL.md:104`
(the tier pairs and "Opus 5 ≡ GPT 5.6 Sol, Sonnet 5 ≡ GPT 5.6 Terra, Haiku 4.5 ≡ GPT 5.6 Luna");
`SW_Development/.claude/agents/batch-closeout-reviewer.md:4-7` (`sonnet`, high, 20), `batch-plan-auditor.md:4-7`
(`sonnet`, medium, 12), `real-stack-validator.md:4-7` (`sonnet`, low, 10); `SW_Development/.agents/README.md:35-38`
(includes `haiku`/`gpt-5.6-luna` for an agent TARGET does not have).

**In the seven packages** — no hit for `Opus 5 ·`, `Sonnet 5 ·`, `Fable 5 ·`, `Opus 5.5`, `Sonnet 5.5`, `Fable 5.1` or
`Haiku`; every hit is a tier tuple. `**Model:**` lines in `BATCH_PLAN.md` (line: tuple):

| Package (`<repo>/implementation/<pkg>/BATCH_PLAN.md`) | `**Model:**` lines | `TASK_CHECKLIST.md` lines with `opus/sol` · `sonnet/terra` · `haiku/luna` | `STATE.md` lines with a tuple |
|---|---|---|---|
| `PlantLibrary_Workspace/…/System_V1_Implementation` | :20 sonnet/terra, :36 haiku/luna, :52 sonnet/terra, :71 haiku/luna, :86 opus/sol, :103 opus/sol, :130 opus/sol, :155 sonnet/terra | 9 · 5 · 5 | :158, :166, :219-227 |
| `PlantLibrary_Workspace/…/System_Design_Architecture` | :17 sonnet/terra, :46 opus/sol, :65 opus/sol, :84 sonnet/terra, :103 sonnet/terra, :122 haiku/luna, :141 sonnet/terra, :159 opus/sol, :177 opus/sol | 16 · 22 · 7 | :91-94 |
| `PlantLibrary_PyApp/…/System_V1_Implementation` | :25, :50, :68 sonnet/terra; :84, :103 opus/sol; :121, :143, :161, :183 sonnet/terra | 6 · 16 · 1 | :162-164 |
| `PlantLibrary_AndroidApp/…/System_V1_Implementation` | :32 haiku/luna; :47, :63 sonnet/terra; :78 opus/sol; :102, :114 sonnet/terra; :127 opus/sol; :139, :159, :180 sonnet/terra; :201 opus/sol; :219, :236 sonnet/terra; :259, :272 opus/sol | 15 · 24 · 3 | :184, :186, :187, :190 |
| `PlantLibrary_Dashboard/…/System_V1_Implementation` | :26, :42, :71, :91 sonnet/terra; :111 opus/sol; :128, :145, :171 sonnet/terra | 6 · 18 · 1 | :114, :120 |
| `PlantLibrary_Server/…/System_V1_Implementation` | :24 opus/sol; :50 sonnet/terra; :65, :80 opus/sol; :98 sonnet/terra; :123 opus/sol; :152 sonnet/terra | 23 · 15 · 1 | :187, :209, :210, :216 |
| `PlantLibrary_SharedContracts/…/System_V1_Implementation` | :22 haiku/luna; :38, :58 opus/sol; :77 haiku/luna | 7 · 1 · 5 | :91 |

**Mapping** (rule 1 wording; cells unchanged, F-A3-11):

| Tuple | Claude half → model | Codex half → model | Session/subagent use |
|---|---|---|---|
| `opus/sol` | `opus` → Opus 5.5 (tier T3) | `gpt-5.6-sol` (frozen, disabled) | Opus 5.5 is the session default |
| `sonnet/terra` | `sonnet` → Sonnet 5.5 (T2) | `gpt-5.6-terra` (frozen) | Sonnet 5.5 only for subagents |
| `haiku/luna` | `haiku` → Haiku 4.5 (T1) | `gpt-5.6-luna` (frozen) | never a session or subagent model (Q-A3-04) |
| (`fable/…`, no rows) | `fable` → Fable 5.1 (T4) | — | sessions only with a stated reason |

**What the Conductor's roster says the roles map to now:** `real-stack-validator` Sonnet, `v5-section-reader` Sonnet,
`batch-plan-auditor` Sonnet, `batch-closeout-reviewer` Opus (`C:/Programmierung/Orchestrator_System/CLAUDE.md:239-246`),
backed by `model: sonnet` low 16 turns, `sonnet` low 20, `sonnet` high 24, `opus` high 30 in `.claude/agents/*.md`.
Sol/Terra/Luna appear in no Conductor instruction text any more: only as the right slot of plan tuples
(`…/.claude/skills/plan-batch/SKILL.md:101-108`) and as frozen Codex roles (`…/.agents/README.md:42-45`: terra low, luna
low, terra medium, terra high, each "(frozen)").

### §7.4 Codex frozen: what `AGENTS.md` says afterwards (evidence for Q-G-09, not a decision)

**The template.** The Conductor kept `AGENTS.md` byte-for-byte at the freeze commit and added one line under its
title (`C:/Programmierung/Orchestrator_System/AGENTS.md:3`): `> Frozen 2026-10-02 (`D-2026-10-02-23`): codex disabled;
`CLAUDE.md` is the live text.` The bridge README carries the rule and the unfreeze path
(`C:/Programmierung/Orchestrator_System/.agents/README.md:6-11`); the checker enforces it (`…/check_harness_parity.py:6-26`).

**What stays identical to `CLAUDE.md`, what differs, after a TARGET freeze under (a):**
- Superproject: `AGENTS.md` equals today's `CLAUDE.md` (diff empty), so at the freeze it is identical to the pre-B2
  `CLAUDE.md` plus the banner; everything B2 adds afterwards exists in `CLAUDE.md` only.
- Suites: `AGENTS.md` was never a copy (pointer, Codex section, "Rules restated"); after the freeze nothing in it is
  kept in sync; its hygiene block stays identical to `CLAUDE.md`'s because the installer owns both (Q-A3-01).
- From B5 on, the design block too, if Q-A3-01 (a): installers write both files; hand edits write `CLAUDE.md` only.

**Evidence for Q-G-09:**
1. Codex is disabled on instance 2 (`PlantLibrary_Workspace/AGENTS.md:14-17`, the same line in every suite).
2. TARGET carries `.codex/` in the superproject (skills, agents, `hooks.json`, `hooks/`) and in all six suites (five
   skills, three `.toml` each); TARGET's checker compares `.claude` with `.codex` byte for byte
   (`SW_Development/scripts/harness/check_harness_parity.py:58-85`), so any B1 skill update turns it red unless B7
   switches it to a freeze compare or the mirrors go.
3. The Conductor's reason to keep the files is its own product invariant (AC51, "nothing normative is
   auto-deleted", `C:/Programmierung/Orchestrator_System/CLAUDE.md:89-91`; `D-2026-10-02-23` (c)). No equivalent
   rule was found in TARGET's instruction surface; history keeps a removed mirror recoverable either way.
4. The freeze has two recorded costs in the Conductor: the `fe4618a` incident and the stale design block in
   `AGENTS.md:187` (F-A3-02, F-A3-03).
5. The superproject `.codex/hooks.json` is a git-deny hook for Codex sessions (by name; not read): under (b) it goes,
   under (a) it stays inert.

### §7.5 `CONTEXT_INDEX.md` and `SCOPE.md` shapes (lane A7 owns the package rows and values)

**Required headings (what a skill reads):**

| File | Heading | Who reads it | Conductor practice |
|---|---|---|---|
| `SCOPE.md` | `## Hard scope` | run-batch §2 (`SW_Development/.claude/skills/run-batch/SKILL.md:32`) | touchable / read-only / never (`…/Conductor_V2/SCOPE.md:3-30`; methodology template :25-38) |
| `SCOPE.md` | `## Standing invariants` | run-batch §2, §6.8; plan-batch §4 (`SW_Development/.claude/skills/plan-batch/SKILL.md:132`); cited by name in every suite guide (e.g. `PlantLibrary_AndroidApp/CLAUDE.md:55`) | Conductor heading adds "(checked at every batch close; never restated per row)" (`…/Conductor_V2/SCOPE.md:290`) |
| `CONTEXT_INDEX.md` | source map, external context, "Do not read as V1 context" | run-batch §4 item 6 (`SW_Development/.claude/skills/run-batch/SKILL.md:96`; the Conductor's copy :94-97) | the Conductor's own files say "May read" / "Must NOT read" (`…/Conductor_V2/CONTEXT_INDEX.md:5`, `:46`) and add "Trace targets" (`:85`) |

No parser requires either file (`…/src/conductor/batch_package.py:53-58`).

**What the seven TARGET packages have:**

| Package | `SCOPE.md` headings | `CONTEXT_INDEX.md` headings |
|---|---|---|
| Workspace `System_V1_Implementation` | Hard scope :14, Standing invariants :29, Scratch :35 | Cross-package map :11, Do not read as V1 context :23 (read order :6 starts at `SUITE_HANDOFFS.md`) |
| Workspace `System_Design_Architecture` | Hard scope :14, Standing invariants :29, Scratch :36 | Start-here :5, Execution :14, Design authority :22, External authority :31, Evidence and closure :41 |
| PyApp | Hard scope :6, Standing invariants :20, Scratch :25 | Source map :10, External context :24, Do not read as V1 context :35 |
| AndroidApp | :6, :22, :26 | :10, :23, :34 |
| Dashboard | :6, :20, :24 | :10, :22, :32 |
| Server | :6, :22, :28 | :12, :26, :34 |
| SharedContracts | :6, :23, :30 | Source map :10, Do not read as V1 context :23 (no External context) |

**The exact delta:**
1. `SCOPE.md`: no heading change. `## Standing invariants` keeps its exact text (cited by name); the Conductor's
   parenthesis goes in as the first body line if A7 wants it. The `## Hard scope` body takes the three-part split
   (RC-A3-23). The "DRIVER_SCRIPT.md is legacy" header line (e.g. `PlantLibrary_PyApp/implementation/System_V1_Implementation/SCOPE.md:3-4`)
   becomes "Procedure: the run-batch skill" when B4 retires the driver files.
2. `CONTEXT_INDEX.md`: keep the three skill-cited headings; add `## Traceability` (RC-A3-24) to all seven; SDA's and
   Workspace V1's differing headings stay (SDA is methodology-shaped, Workspace V1 is a coordination index); Workspace
   V1's read order :6 changes when B4 replaces `SUITE_HANDOFFS.md` (Q-G-05). SharedContracts lacks
   `## External context`: add it only if A7 finds external reads.
3. New design-migration workspaces (B6) use the methodology templates as they are.

### §7.6 Order of operations for lane B2

1. **Preconditions (B1 must have landed in the superproject `.claude/` and the six mirrors):** the final skill set per
   repository (which Conductor skills come over, the fate of `test-driven-development`, `impeccable`, `gui-validation`,
   `scratch-gate`); the three agent definitions at their final `model`/`effort`/`maxTurns`; `SW_Development/.agents/README.md`
   rewritten (freeze paragraph, bridge, roster). Without these, the roster and every "Procedure" skill list would be
   written twice. Q-G-09 answered for the banner; Q-A3-01 answered before B7 guards the freeze.
2. **First file: `SW_Development/CLAUDE.md`**, with the `SW_Development/AGENTS.md` banner in the same superproject
   commit. Reason: it carries the session rules every suite section points at (Q-A3-03 (a)); it is the orchestrator's
   own cwd; and its two waiting items (Q-A3-02, rules 4/5) are single sentences B2 can leave marked.
3. **Then Dashboard, AndroidApp, PyApp** (each: `CLAUDE.md` sections + `AGENTS.md` banner in one suite commit; PyApp
   also `.claude/CLAUDE.md` per Q-A3-05). Reason: B5 installs the design block in these three, and the installer places
   it above the roster heading only if B2 wrote that heading first (F-A3-16).
4. **Then Server, SharedContracts, Workspace.**
5. After each suite commit: the hygiene checker's verdict and held count unchanged; `git ls-files --eol` unchanged;
   `git diff --stat` shows only the listed files; then one superproject commit bumps the gitlink with the ledger flip
   (kickoff §2 item 5). One writer per repository: B2 serialises with B1, B3, B4, B5, B7 per repository or takes a worktree.
6. **What waits, and only that:** rule 4 (Q-A3-07), rule 5 (Q-G-03), `SW_Development/CLAUDE.md:10-12` (Q-A3-02),
   rule 1's `haiku` sentence (Q-A3-04), PyApp's `.claude/CLAUDE.md` (Q-A3-05), the living-documentation section
   (Q-A3-06). Everything else in §7.2 runs.
7. **After B2:** B7 adds the `AGENTS.md` freeze guard (RC-A3-21); B5 installs the design blocks; B4 edits the packages'
   `SCOPE.md`/`CONTEXT_INDEX.md` per §7.5.
