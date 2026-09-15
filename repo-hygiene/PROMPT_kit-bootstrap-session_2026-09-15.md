# PROMPT — Repo Hygiene Template Kit: the bootstrap session (2026-09-15)

*Written 2026-09-15 (evening) by a Fable 5.1 session rooted in the Orchestrator repo, from
measurements taken the same evening. Nothing in this track has run. This file holds **one** paste
block — the bootstrap session that writes the track runbook. Every later session is paced by the
runbook that session writes, never by this file.*

## 0. What this is, and what it is not

| | |
|---|---|
| Goal of the track | Derive a reusable **Repo Hygiene Template Kit** from the harness the Orchestrator repo already enforces (deliverable naming, folder taxonomy, per-folder `INDEX.md`, prompt proof-surface rule, `CLAUDE.md`/`AGENTS.md` rule-block parity, decision-recorded exemptions), shaped like `C:\Programmierung\Design_Template_Kit`; anchor it in `C:\Programmierung\SW_Development` and its six `PlantLibrary_*` submodules; migrate the existing corpus so every repo is compliant afterwards; carry a derivation runbook so the kit can be re-derived when the source harness moves |
| Goal of **this** session | Measure, decide at one gate, and write the runbook the whole track follows — with the exact prompts, `cwd`, model · reasoning per step, and a ledger. **It builds no kit, renames no file, anchors nothing.** |
| Three roots, fixed | **SOURCE** `C:\Programmierung\Orchestrator_System` (`main`, `fc5a14c` or later) — read, never written. **KIT** `C:\Programmierung\Repo_Hygiene_Template_Kit` — does not exist yet; a later step creates it as its own git repository. **TARGET** `C:\Programmierung\SW_Development` — the superproject and its six submodules; every track artifact lives under `SW_Development\repo-hygiene\` |
| Working directory | `C:\Programmierung\SW_Development` on `main`, for this session and for every track step that is not inside a submodule |
| What this file never does | Name a proof surface. A paste block states scope, read-first, constraints, done-when and the commit line. What counts as proof is the verification order the kit's own `CONTRIBUTING.md`/`INSTALL.md` will own — a step's done-when cites that document's verdict, it never spells a test invocation |

## 1. Measured 2026-09-15 — cite, do not re-derive

### 1a. SOURCE — the harness, as it exists at `fc5a14c`

Two layers, written nine days apart, and one conflict between them that the kit must resolve the
way the source did:

| # | Component | Path (relative to SOURCE) | Mechanism |
|---|---|---|---|
| 1 | The authoring rule: `<TYPE>_<topic>_<YYYY-MM-DD>.md`, `TYPE ∈ {PROPOSAL, PROMPT, PROMPTS, PLAN, EVIDENCE, AUDIT, REGISTER, MATRIX, SNAPSHOT, HANDOVER, FINDING}`; where each type lives; `INDEX.md` same-commit rule; the "a prompt never names a proof surface" rule | `CLAUDE.md` § "Deliverable naming" and § "Authority"; the identical block in `AGENTS.md` | prose, byte-parity-checked (row 9) |
| 2 | The normative naming block and the 113-file census with git-authoritative dates and a `type` column | `implementation/Conductor_V2/planning/REGISTER_document-index_2026-08-18.md` (181 lines; the block is its last section, lines 172–181) | prose |
| 3 | The retrofit procedure — rename-map policy, hold-back check, operator review gate, `git mv`, the reference sweep with its editable / never-edit lists, `INDEX.md` regeneration with a "Renamed" old→new table; executed as three commits `d8dad58`, `ea87e5a`, `3cf3540` | `implementation/Conductor_V2/planning/PROMPT_CH8_docs-retrofit_2026-08-19.md` (308 lines) and `META_WORK_PLAN_2026-08-18.md` Chapters 1 and 8 | prose, executed once |
| 4 | The three folder indexes: one line per file (`date · name · type · disposition · summary`) plus the mapping table | `implementation/Conductor_V2/{planning,proposal,handovers}/INDEX.md` | prose, kept by hand |
| 5 | Filename enforcement per folder, a frozen exemption set, a held set, a gap-folder exemption | `tests/test_docs_naming_hygiene.py` (109 lines) | pytest, fixture-free |
| 6 | Prompt proof-surface enforcement: two regex detectors with a negation guard, empty held set | `tests/test_prompt_proof_surface_hygiene.py` (155 lines) | pytest, fixture-free |
| 7 | Repo-root allowlist, retired scratch names, the `C:\pt` ban, a dev-repo marker | `tests/test_repo_hygiene.py` (174 lines) | pytest, fixture-free |
| 8 | The first layer's policy: born-in-package, archive+hide never delete, the `.tmp/` interior, the root allowlist | `implementation/Repo_Hygiene/DECISION_FILE_AND_DOCS_POLICY.md` (482 lines, Part A), `DECISION_TEMP_STRUCTURE.md`, `PROMPTS_REPO_CLEANUP_2026-08-10.md` | prose + row 7 |
| 9 | `CLAUDE.md`/`AGENTS.md` shared-block byte parity and skill-mirror parity, dependency-free by design | `scripts/harness/check_harness_parity.py`; `.agents/README.md` (the bridge table); `tests/test_skill_mirror_parity.py` | stdlib script + pytest |
| 10 | Decision records `D-YYYY-MM-DD-nn` — exemption and held sets "grow only by an explicit STATE.md decision, never silently" | `implementation/Conductor_V2/STATE.md` (example `D-2026-09-15-13` at line 34916) | prose |
| 11 | Two further conventions the kit catalogues but does not fold into the dated rule: batch-keyed evidence `<BATCH>_<slug>.md|.log` (490 files) and numbered handbook chapters `NN-topic.md` | `implementation/Conductor_V2/validation/`; `docs/handbook/` | prose |

- **The conflict.** Row 8's principle A.0.2 says *filenames are immutable on move — never rename to
  fix a naming convention retroactively*. Row 3, nine days later, renamed 45 files via `git mv`
  with mapping tables and held two. **Row 3 governs**: it is later, executed, and it is what this
  track needs. The kit records the supersession; it does not carry the conflict forward.
- **The harness covers three folders only** — Conductor_V2's `planning/`, `proposal/`,
  `handovers/`. The Orchestrator's own `implementation/Repo_Hygiene/` and `Conductor_V1/` are
  outside it and non-compliant. The kit generalises "three folders" to **configurable deliverable
  roots per repo**; nothing else in the rule changes.
- Rows 5–7 together: **11 nodes, green in 1.11 s** at `fc5a14c`. Row 9 exits 0. That is the
  baseline the kit's self-test reproduces (§3, step K-3).
- Instance 1 sweeps stray files under SOURCE into `conductor: handover checkpoint` commits — one
  more reason SOURCE is never written by this track.

### 1b. TARGET — the corpus, as it stands

| surface | observed |
|---|---|
| Superproject | `main` at `3bb2320`, tree clean; six submodules (`.gitmodules`, GitHub remotes) all clean on their own `main`; `.gitattributes` absent everywhere; `CLAUDE.md` carries mixed CRLF/LF, the 2026-09-15 documents are LF |
| Instruction files | `CLAUDE.md`/`AGENTS.md` in the superproject (graphify + testing sections), in `PlantLibrary_PyApp` and `PlantLibrary_Server` only; the other four submodules have none |
| Already compliant | `onboarding\` — `INDEX.md` + `PROMPTS_conductor-onboarding-runbook_2026-09-15.md` + `REGISTER_package-census_2026-09-15.md` (the onboarding track, step `0` done) |
| Non-compliant at the root | `HANDOVER_batch-package-schema-drift_2026-09-15.md` (compliant name, no `handovers/` home), `IMPLEMENTATION_PLAN.md` (2026-08-04 program plan), `Todo.md` (git-ignored, personal) |
| Markdown census, excluding `node_modules`, `.git`, `.venv`, `build`, the four runtime mirrors | AndroidApp 143 · Dashboard 75 · PyApp 284 (of which **192 under `.tmp\audit-harness-probe` are scratch**) · Server 48 · SharedContracts 187 (of which **130 under `generated\`**) · Workspace 405 |
| Where the dated deliverables would live | each submodule's `implementation\<Package>\` (package files `BATCH_PLAN.md`, `TASK_CHECKLIST.md`, `TASK_CONTEXT.md`, `STATE.md`, `CONTEXT_INDEX.md`, `DRIVER_SCRIPT.md`, `README.md` are schema-named and exempt by construction); `<Package>\proposal\`, `\validation\` exist in places; `docs\` folders carry id-prefixed notes (`SV-SYNC-01_sync_protocol_notes.md`, `WD-UX-10_mockup_parity_report.md`); Workspace carries `docs\proposals\`, `prompts\`, `methodology\`, `strategy\`, `system_description\` |
| **Frozen — never renamed** (onboarding runbook Appendix D and `IMPLEMENTATION_PLAN.md` §7) | every `<Suite>\implementation\MVP\`, `PyApp\implementation\Archive_PreMVP\`, `Workspace\implementation\System_Integration_MVP\`, `\System_Tooling\`, `Workspace\strategy\Cross_Platform_Strategy\`, `Workspace\system_description\PlantLibrary_System_Description\` (137 files), `Dashboard\references\PlantLibrary_pythonApp_old\` (42), `SharedContracts\generated\**` |
| **Pinned by another kit — a rename breaks it** | `Workspace\methodology\GUI_Improvement_Methodology\` (62 files) is pinned **by absolute path, version 4.0.0 and per-file name** from `Design_Template_Kit\METHODOLOGY_SOURCE.md` (its "inherited templates" table names `SCOPE_TEMPLATE.md`, `TASK_CHECKLIST_TEMPLATE.md`, …) and resolved at run time by the `design-migration` skill's `<meth>` root. `Workspace\methodology\Design_Template_Initiative\` (45 files) is that kit's live initiative (Phase 6, `STATE.md`). Both are **held** unless the Design kit is re-pinned in the same change — which is not this track's call |
| Cross-references | the batch packages' anchors, `STATE.md` files and the onboarding runbook cite file names; a rename without a reference sweep breaks a live package. The hold rule of SOURCE row 3 applies verbatim |

### 1c. The kit shape to mirror

`C:\Programmierung\Design_Template_Kit` at `8e708f8` (Kit 0.8.0): `README.md` (folder map, "what the
Kit contains / never contains" table), `KIT_VERSION.md` (semver rule + changelog), `CONTRIBUTING.md`
§1 (the verification order and what "green" means), `METHODOLOGY_SOURCE.md` (a pin, not a runtime
path), `anchoring-kit/INSTALL.md` + `install.mjs` (idempotent installer; the header comment lists
what it writes in order), `rule-block/DESIGN_RULES_BLOCK.md` (the `<!-- design-kit:begin/end -->`
block), `skills/README.md` + `CODEX_ADAPTATION.md` (byte-identical mirrors, documented
differences only), `examples/anchored-target/` (a reference anchored repo), `checks/` +
`check-parity.mjs`. The Design kit is Node because it needs Playwright and ajv; this kit needs
neither.

## 2. Model · reasoning for the paste below

**Fable 5.1 · xhigh.** This is the "open-ended design and gates" shape of the track ladder
(`PROMPTS_meta-v2-track-runbook_2026-09-06.md` §16): it decides the kit's boundary, the folder
taxonomy for repos that have no Conductor package, the migration policy over six heterogeneous
repos with frozen sets and cross-kit pins, and it writes the runbook every later session obeys — an
error here is copied into every step. **If Fable is unavailable:** Opus 5 · high, **plus** a
mandatory fresh-context review of the drafted runbook before it is written (the `D-2026-09-12-05`
substitution rule: the compensating control is review, not effort). Never Sonnet for this step.

The runbook the session writes sets the ladder for everything after it; the expected shape is
Fable 5.1 · high for the kit build and each rename map, Opus 5 · high for each per-repo anchoring
and migration execution, Sonnet 5 · thinking for the verification passes.

## 3. The paste block

```text
Bootstrap session for the Repo Hygiene Template Kit track. cwd C:\Programmierung\SW_Development on main.
Measurement, one decision gate, and authoring only: this session writes the track runbook and its two
registers under SW_Development\repo-hygiene\. It builds no kit, creates no folder under C:\Programmierung,
renames or moves no file, anchors nothing, commits nothing inside a submodule.

Three roots, fixed. SOURCE = C:\Programmierung\Orchestrator_System on main (fc5a14c or later): read only,
never written - a stray file there is swept into an instance commit. KIT = C:\Programmierung\
Repo_Hygiene_Template_Kit: does not exist yet; a later step of the runbook creates it as its own git
repository, shaped like C:\Programmierung\Design_Template_Kit. TARGET = C:\Programmierung\SW_Development:
the superproject and its six PlantLibrary_* submodules; every artifact of this track lives under
SW_Development\repo-hygiene\ and is indexed in repo-hygiene\INDEX.md in the same commit.

Read first, in SOURCE, in this order: CLAUDE.md sections "Authority" and "Deliverable naming" and the same
block in AGENTS.md; implementation/Conductor_V2/planning/REGISTER_document-index_2026-08-18.md (the census
shape and its last section, the normative naming block); planning/PROMPT_CH8_docs-retrofit_2026-08-19.md
(the retrofit procedure: rename-map policy, hold-back check, operator review gate, git mv, the reference
sweep's editable and never-edit lists, INDEX regeneration with the old-to-new table) and the three commits it
produced, d8dad58, ea87e5a, 3cf3540; planning/META_WORK_PLAN_2026-08-18.md Chapters 1 and 8; the three
INDEX.md files under implementation/Conductor_V2/{planning,proposal,handovers} including the "Renamed
2026-08-19" tables; tests/test_docs_naming_hygiene.py, tests/test_prompt_proof_surface_hygiene.py,
tests/test_repo_hygiene.py; scripts/harness/check_harness_parity.py with .agents/README.md and
tests/test_skill_mirror_parity.py; implementation/Repo_Hygiene/DECISION_FILE_AND_DOCS_POLICY.md Part A and
DECISION_TEMP_STRUCTURE.md; one decision record in implementation/Conductor_V2/STATE.md (D-2026-09-15-13,
line 34916) for the D-id shape; the validation/ naming (<BATCH>_<slug>.md) and docs/handbook/ naming
(NN-topic.md) as conventions to catalogue, not to fold in. Do not open proposal/conductor-v5-system-proposal.md
- nothing in this track cites it.

Read next, in TARGET: CLAUDE.md, AGENTS.md, .gitignore, .gitmodules; onboarding\INDEX.md and
onboarding\PROMPTS_conductor-onboarding-runbook_2026-09-15.md sections 0-3, Appendix D and section L;
HANDOVER_batch-package-schema-drift_2026-09-15.md; IMPLEMENTATION_PLAN.md section 7; PlantLibrary_PyApp\
CLAUDE.md and AGENTS.md; PlantLibrary_Server\CLAUDE.md and AGENTS.md; repo-hygiene\PROMPT_kit-bootstrap-
session_2026-09-15.md section 1 (the facts measured before you; re-verify only HEAD, cleanliness and the
counts).

Read for shape: C:\Programmierung\Design_Template_Kit at 8e708f8 - README.md, KIT_VERSION.md,
CONTRIBUTING.md section 1, METHODOLOGY_SOURCE.md, anchoring-kit\INSTALL.md, the header comment of
anchoring-kit\install.mjs, anchoring-kit\rule-block\DESIGN_RULES_BLOCK.md, anchoring-kit\skills\README.md,
anchoring-kit\CODEX_ADAPTATION.md, and the tree of examples\anchored-target. For the runbook shape:
SOURCE's implementation/Conductor_V2/planning/PROMPTS_meta-v2-track-runbook_2026-09-06.md sections 0, 2, 3,
7.11u (a gate step), 7.11v (an authoring step), 16 and 18, and TARGET's onboarding runbook sections 0-3,
section 5 (a step block) and section L.

Measure before designing - read only, no scratch outside SW_Development\.tmp\, deleted afterwards. Write
the results as two registers, REGISTER_hygiene-harness-inventory_<today>.md and
REGISTER_target-corpus-census_<today>.md, under repo-hygiene\:
(a) the harness inventory: every component of section 1a with its path, the rule it enforces, its
    mechanism (test, script, prose, kept-by-hand), the decision or commit that created it, and a
    portability verdict - generic (goes into the kit as is), parameterised (goes in with a placeholder:
    the three folders, the exemption sets, the shared-block end markers, the root allowlist), or
    Conductor-specific (stays out, named); the supersession of DECISION_FILE_AND_DOCS_POLICY.md A.0.2 by
    the Chapter-8 retrofit recorded as such;
(b) the corpus census: for the superproject and each submodule, markdown files by folder excluding
    node_modules, .git, .venv, build, .tmp, generated trees and the four runtime mirrors, each folder
    classified as package-schema (exempt by construction), dated deliverable (candidate), product
    documentation (outside the naming rule), frozen or terminal (section 1b's list - never renamed),
    pinned by the Design kit (held), generated, or scratch; for every candidate file its git-created date
    (git log --follow --diff-filter=A), its proposed TYPE and topic, and every reference to its current
    name across the whole superproject including all submodules (git grep per repo) with the citing
    file's class - a citation from a live batch package's anchor, a STATE.md or the onboarding runbook is
    a hold; totals per repo: candidates, holds, frozen, exempt;
(c) the enforcement surfaces available per repo: whether a pytest suite exists, whether python is on
    PATH for that repo's sessions, whether CLAUDE.md/AGENTS.md exist, the line-ending mix, and which
    folders would become that repo's deliverable roots.
The census over roughly 1,100 files is agent work: delegate it if this invocation can spawn agents
(Explore for the sweep, one agent per submodule), otherwise do it inline and say so in the report.

Then design, and present at gate G0 - each question with the options, one recommendation and its
reason; wait for the operator's explicit answer and record it verbatim in the runbook; do not auto-resolve
a gate question:
Q1 kit name and location (recommendation: C:\Programmierung\Repo_Hygiene_Template_Kit, its own git
   repository, KIT_VERSION.md starting at 0.1.0, no node_modules, no build step);
Q2 the checker's language (recommendation: one stdlib-only Python 3 script, the check_harness_parity.py
   precedent - runs in either coding harness on Windows with nothing installed - plus a thin pytest
   wrapper module for repos that have a pytest suite; not Node: the Design kit is Node for Playwright and
   ajv, which this kit does not need);
Q3 the kit's boundary (recommendation, in: the dated-deliverable naming rule and TYPE enum; the folder
   taxonomy as configurable deliverable roots with INDEX.md/README.md exempt and package-schema files
   exempt by name; per-root INDEX.md with the same-commit rule and the rename mapping table; the prompt
   proof-surface rule for PROMPT/PROMPTS files; the CLAUDE.md/AGENTS.md rule block between begin/end
   markers with line-ending-insensitive byte parity of the block; a per-repo decision record for
   exemptions and holds; optional modules for the root allowlist and the .tmp\ scratch policy. Out, to
   the onboarding track: skill mirrors and the bridge table, the batch package schema, the validation
   harness, graphify);
Q4 the folder taxonomy for a repo without a Conductor package (recommendation: deliverable roots are
   declared per repo; default implementation\<Package>\{planning,proposal,handovers} where a package
   exists; the superproject declares repo-hygiene\, onboarding\ and a new handovers\ that receives the
   root HANDOVER by git mv; product documentation folders - docs\, Documentation\adr, GUI\, openapi\ -
   are catalogued, not renamed);
Q5 the migration policy (recommendation: the Chapter-8 procedure verbatim - git mv only, date from the
   git-created date even where the name embeds another and the divergence noted, TYPE from the census
   classification, already-compliant names untouched, no case churn, holds for every live citation, an
   old-to-new table in the root's INDEX.md; the frozen and pinned sets of section 1b listed as exempt
   in each repo's decision record and never renamed);
Q6 the TYPE enum's extension policy (recommendation: the kit's enum is fixed; a repo extends it only by
   a decision record entry; the census proposes candidates - DECISION, REPORT, SPEC, GUIDE - and the
   gate decides whether any enters the kit's enum now);
Q7 commit and push discipline (recommendation: each submodule commits on its own main in the step that
   changes it; the superproject bumps the gitlinks in one commit per step; nothing is pushed by a track
   session - pushing is the operator's, out of band);
Q8 enforcement surfaces per repo (recommendation: the checker everywhere; the pytest wrapper where a
   suite exists; a .github\workflows\repo-hygiene.yml template; an optional pre-commit hook; the rule
   block for agents; the installer idempotent and re-runnable on a kit upgrade, refusing to overwrite a
   pin without --force, as the Design kit's does);
Q9 where a repo records its pin and its decisions (recommendation: hygiene\CONSUMED_HYGIENE.md for the
   pin - kit version and SOURCE commit - and hygiene\HYGIENE_DECISIONS.md, append-only, for exemptions,
   holds and enum extensions; parallel to design\conformance\CONSUMED_DESIGN.md);
Q10 runbook placement (recommendation: three generic runbooks in KIT\runbooks\ with <PLACEHOLDERS> -
   derive the kit from a source, anchor a repository, migrate an existing repository - and the
   instantiated track runbook in TARGET\repo-hygiene\; a prompt exists in one place only);
Q11 line endings (recommendation: every edit preserves the file's existing line endings; no
   .gitattributes introduced by this track; the checker normalises line endings before comparing the
   rule block).

Then write the runbook, repo-hygiene\PROMPTS_repo-hygiene-track-runbook_<today>.md, in the exact shape of
the two reference runbooks: section 0 what this is and is not with the three roots; section 1 where
things stand, from the two registers, never re-measured in prose; section 2 how to use (one fresh
session per step; model and reasoning set before pasting; cwd stated per step; paste the block exactly;
the Watch paragraph is for the operator; agents may be spawned, inline fallback only after a real
refused call and said so; flip the ledger in the step's own commit); section 3 the step map with three
phases - K derive the kit, A anchor, M migrate - and the gates between them; then one section per step
with its model and reasoning line, its cwd, its fenced paste block, its Watch paragraph, and the G0
answers it depends on. Phase K: K-1 the kit specification from the inventory (KIT_SPEC.md, what the kit
contains and never contains); K-2 build the kit - the checker, the pytest wrapper, the rule block, the
installer, the templates for INDEX.md, the decision record, the runbook shape and the handover
continuation section, the three generic runbooks, examples\anchored-target, README, CONTRIBUTING with
the verification order, KIT_VERSION, the SOURCE pin; K-3 the self-test - the kit's checker run over
SOURCE's implementation/Conductor_V2 must reproduce the baseline of section 1a (eleven green nodes, zero
violations, the same held names) before the kit touches any target, and a deliberately non-compliant
scratch tree must fail it; K-4 version, commit, the kit's first tag. Phase A: A-1 the superproject; A-2
to A-7 one submodule each in the onboarding runbook's suite order (PyApp, Server, SharedContracts,
Dashboard, AndroidApp, Workspace); each writes the rule block, the checker, the wrapper where applicable,
seeds the INDEX.md files and the decision record with that repo's frozen and held sets, commits in the
submodule and bumps the gitlink. Phase M: M-0 the rename map per repo from the census with holds and
date divergences, presented at gate GM and confirmed by the operator before the first git mv; M-1 to
M-7 one repo each - git mv, the reference sweep within the editable list, INDEX.md regeneration with the
mapping table, the checker green, commit and gitlink bump; M-8 the closing pass - the checker green over
the whole tree, the census re-run and diffed against the pre-migration register, a HANDOVER for whoever
continues, the kit's changelog updated with anything the pilot taught it. Every step completes in one
session; split before writing where a step cannot. Every paste block states scope, read-first,
constraints, done-when and the commit line; none spells a test invocation - it names the kit document
that owns the verification order and cites its verdict. Close the runbook with the model and reasoning
ladder (section 16's shape, four rows by shape) and the ledger, every step todo.

Before writing the runbook to disk, have it reviewed in a fresh context if this invocation can spawn
agents - a general-purpose reviewer with this checklist: every step has cwd, model and reasoning, paste
block, Watch, done-when, commit line; no paste block spells a test invocation; no step renames a frozen
or pinned file; every rename step has the gate before its first git mv; every done-when is verifiable
from the step's own output; the G0 answers it relies on are recorded. Fix what the review finds; record
the review and its findings in the runbook's section 1. Inline fallback only after a real refused call.

Constraints: nothing under SOURCE written; nothing under TARGET renamed, moved or deleted; no folder
created under C:\Programmierung; no commit in any submodule; the superproject's one commit carries only
repo-hygiene\; no push; no secrets, tokens or chat ids anywhere; scratch under SW_Development\.tmp\ only;
edits preserve each file's line endings; Conductor instance 2 is not touched - this track does not
involve it.

Done when: repo-hygiene\ holds the two registers, the runbook and an updated INDEX.md; the G0 answers
are recorded verbatim in the runbook with the operator's exact words per question; the runbook's ledger
lists every step todo with its model and reasoning; the fresh-context review is recorded; the pre-
migration census totals per repo are in the register the M-8 diff will read; one commit on main.

Commit line: repo-hygiene: bootstrap - harness inventory, corpus census, track runbook; G0 recorded
```

## 4. Watch (for you, not for the paste)

- The session **will want to start building the kit**. It must not. Its output is three documents
  and a commit; K-1 is the next session.
- Expect the gate after the two registers exist. Answer every question explicitly; "all
  recommendations accepted" is a valid answer and is recorded verbatim.
- The census is the expensive part (~1,100 markdown files across seven repositories). If the
  session runs it inline instead of through agents it should say why; that is allowed, not preferred.
- Two things a reviewer will otherwise miss: the methodology folder pinned by the Design kit (§1b,
  "held"), and the hold rule for names cited by live batch packages. If the runbook's M-0 does not
  carry both, send it back.
- Nothing here touches Conductor instance 2 or the onboarding track's ledger. The two tracks share the
  repository and the `onboarding\` folder is already compliant; they do not share steps.
