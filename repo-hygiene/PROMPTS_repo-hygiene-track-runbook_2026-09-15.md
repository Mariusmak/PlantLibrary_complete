# Repo Hygiene Template Kit — track runbook (steps `K-1` … `M-9`)

*Written 2026-09-15 (evening) by the bootstrap session of `PROMPT_kit-bootstrap-session_2026-09-15.md`, after the two
registers were measured and gate `G0` was answered. One track, one sequence: this file is the authority for **what to
paste, in which order, with which model and reasoning**. It was written from the registers, never from memory of the
source repository; where a step needs a fact, it cites the register that holds it.*

## 0. What this is, and what it is not

| | |
|---|---|
| Scope | Derive a reusable **Repo Hygiene Template Kit** from the harness `C:\Programmierung\Orchestrator_System` enforces (deliverable naming, folder roots, per-root `INDEX.md`, prompt proof-surface rule, `CLAUDE.md`/`AGENTS.md` rule-block parity, decision-recorded exemptions), shaped like `C:\Programmierung\Design_Template_Kit`; anchor it in `C:\Programmierung\SW_Development` and its six `PlantLibrary_*` submodules; migrate the existing corpus; carry three generic runbooks so the kit can be re-derived, re-anchored and re-applied elsewhere |
| Three roots, fixed | **SOURCE** `C:\Programmierung\Orchestrator_System` on `main` at `fc5a14c` — read, never written; a stray file there is swept into an instance commit. **KIT** `C:\Programmierung\Repo_Hygiene_Template_Kit` — created by step `K-1` as its own git repository. **TARGET** `C:\Programmierung\SW_Development` — the superproject and its six submodules (`.gitmodules`: AndroidApp, Dashboard, PyApp, Server, SharedContracts, Workspace; GitHub remotes; gitlinks in the index) |
| Working directories | `KIT` for every `K-*` step (`K-1` starts in `C:\Programmierung` to create it). `TARGET` for `A-1`, `M-0`, `M-1`, `M-8`. **The submodule folder** for `A-2`…`A-7`, `M-2`…`M-7` and `M-9`, followed by `TARGET` for the gitlink bump — the submodule is the git root of everything those steps change |
| Normative sources | `repo-hygiene\REGISTER_hygiene-harness-inventory_2026-09-15.md` (what the kit is derived from; the `K-3` baseline) · `repo-hygiene\REGISTER_target-corpus-census_2026-09-15.md` (what the target holds; the `M-8` baseline; the hold register) · the `G0` record in §1d · after `K-1`: `KIT\KIT_SPEC.md`; after `K-2b`: `KIT\CONTRIBUTING.md` §1 (the verification order) and `KIT\installer\INSTALL.md` (what an anchoring writes, and how it is verified) |
| Ledger of record | §L at the end of this file. Flip a step there in the same commit as the step's output; for a `K-*` step, whose output commits in KIT, the flip is its own one-line superproject commit (§2 item 8). Gate answers are recorded in §4 |
| Where the track's artifacts live | `TARGET\repo-hygiene\`, indexed in `repo-hygiene\INDEX.md` in the same commit — with one exception the track itself creates: the `M-8` HANDOVER routes to the superproject's `handovers\` root, because that is the rule the kit installs (`HANDOVER`/`FINDING` → `handovers\`); `repo-hygiene\INDEX.md` carries a pointer line |
| Deviations from the commissioning prompt's step list | Two, both because a step must complete in one session: `K-2` is three steps (`K-2a` checker and fixtures, `K-2b` installer and templates, `K-2c` documents); `M-9` is a rolling release step after `M-8`, because 21 of the 34 census holds outlive the migration (§1b) |
| What this file never does | Name a proof surface. A paste block states scope, read-first, constraints, done-when and the commit line; what counts as proof is the verification order the kit's `CONTRIBUTING.md` §1 and `INSTALL.md` own — a done-when cites that document's verdict, it never spells a test invocation. Touch Conductor instance 2, the onboarding track's ledger, or SOURCE |

## 1. Where things stand (from the two registers — never re-measured here)

### 1a. SOURCE — the harness at `fc5a14c` (`REGISTER_hygiene-harness-inventory_2026-09-15.md`)

Eleven components in two layers: the 2026-08-10 repo-hygiene layer (`DECISION_FILE_AND_DOCS_POLICY.md`, `DECISION_TEMP_STRUCTURE.md`,
`tests/test_repo_hygiene.py`) and the 2026-08-18/19 deliverable-naming layer (the normative block, the 113-file census, the
Chapter-8 retrofit executed as `d8dad58`/`ea87e5a`/`3cf3540`, the three `INDEX.md` files, `tests/test_docs_naming_hygiene.py`,
the `CLAUDE.md`/`AGENTS.md` section), plus the 2026-08-27 proof-surface guard (`tests/test_prompt_proof_surface_hygiene.py`,
`D-2026-08-26-08`) and the parity checker (`scripts/harness/check_harness_parity.py`). Verdicts: **generic** the pattern and
enum, the proof-surface detectors, the marked-block parity idea, the census shape, the `INDEX.md` line and mapping table, the
retrofit procedure and its commit split, principles A.0.1/A.0.3/A.0.5/A.0.6, the decision-record shape, the self-test pattern;
**parameterised** the deliverable roots, exempt/held sets, exempt subfolders, block markers, sanctioned launcher, root allowlist,
retired names, scratch root, editable/never-edit lists; **Conductor-specific, out** skill mirrors and the bridge table, the batch
package schema, the validation harness and `.tmp/` interior, the v5-proposal and chunk/envelope parity checks, graphify, the
Telegram rule, `STATE.md` as the decision home. The A.0.2-versus-Chapter-8 conflict is recorded as superseded: **Chapter 8
governs** (inventory §2). One thing SOURCE keeps by hand: nothing asserts `INDEX.md` coverage; the kit will (G0 Q3a).

**Baseline the kit must reproduce (`K-3`):** at `fc5a14c` the three hygiene modules are 11 green nodes (re-verified 0.87 s,
nothing written), the parity checker exits 0, the held names are `FULL_AUTONOMY_PROPOSAL_2026-08-13.md` and
`GAP_REGISTER_FULL_AUTONOMY_2026-08-13.md`, the exempt names `INDEX.md`, `README.md`, `conductor-v5-system-proposal.md`,
`META_WORK_PLAN_2026-08-18.md`, the exempt subfolder `planning/gap/`, the sanctioned launcher `run_validation.py`.

### 1b. TARGET — the corpus (`REGISTER_target-corpus-census_2026-09-15.md`)

| repo | HEAD | md files | candidates | to rename | holds | frozen | pinned | generated |
|---|---|---|---|---|---|---|---|---|
| SW_Development | `6ecc155` | 11 | 6 | 1 | 4 | 0 | 0 | 0 |
| PlantLibrary_PyApp | `5cefe62` | 192 | 31 | 31 | 4 | 64 | 0 | 5 |
| PlantLibrary_Server | `5c312d3` | 47 | 5 | 5 | 4 | 10 | 0 | 0 |
| PlantLibrary_SharedContracts | `75846a9` | 187 | 1 | 1 | 1 | 9 | 0 | 134 |
| PlantLibrary_Dashboard | `472e7d2` | 75 | 5 | 5 | 5 | 51 | 0 | 0 |
| PlantLibrary_AndroidApp | `b75265a` | 56 | 2 | 2 | 1 | 22 | 0 | 0 |
| PlantLibrary_Workspace | `5147569` | 399 | 53 | 53 | 15 | 205 | 107 | 1 |
| total | | 967 | 103 | 98 | 34 | 361 | 107 | 140 |

What the census settled beyond the pre-session facts: PyApp `Documentation\` is 27 pre-MVP session documents (June 2026) plus
four product specs; Server/Dashboard/AndroidApp `docs\` hold nine dated deliverables among living notes; every live package's
`proposal\` file except AndroidApp's is cited by its own `STATE.md` (in Workspace also by anchors); five Workspace documents
are numbered chapter sets (four outside live packages, 29 files; two inside live `proposal\` roots, 8 files); 28 candidates carry
a header date one day before their git-created date (one, ten days); 11 candidates are cited by nothing. Enforcement surfaces:
Python 3.12 and pytest on every session's `PATH`; a pytest home in PyApp and Server only; CI in PyApp, Server, SharedContracts;
`CLAUDE.md`/`AGENTS.md` in the superproject (mixed line endings inside each file), PyApp (CRLF) and Server (LF) only; `.tmp\`
ignored in PyApp only. Never renamed: every `implementation\MVP\`, PyApp `Archive_PreMVP\`, Dashboard `references\`,
SharedContracts `generated\`, Workspace `System_Integration_MVP`, `System_Tooling`, `strategy\Cross_Platform_Strategy`,
`system_description\`, and the two pinned methodology trees (`GUI_Improvement_Methodology`, pinned by absolute path, version
4.0.0 and per-file name from the Design kit; `Design_Template_Initiative`, its live initiative). Pinned by name across repos:
`CONTRACT_VERSION.md`, `generated\CLIENT_MANIFEST.md`, `VERSION.md` and the 28 `*_TEMPLATE.md`.

**How the 34 holds release** (census §3, grouped by the citer that must change; a name with citers in two groups belongs to
the later group):

| group | names | released by |
|---|---|---|
| onboarding runbook (4) | superproject `HANDOVER_batch-package-schema-drift_2026-09-15.md`, `IMPLEMENTATION_PLAN.md`, `onboarding\AUDIT_skill-assumptions_2026-09-15.md`, `onboarding\REGISTER_package-census_2026-09-15.md` | the onboarding track, when it retires or edits its runbook; three of the four are already compliant, so only `IMPLEMENTATION_PLAN.md` is at stake (`M-0` proposal 1) |
| live package `STATE.md`/anchor only (10) | the `proposal\` file of PyApp, Server, SharedContracts, Dashboard; Workspace `System_V1_Implementation\proposal\00`, `01`, `02`; Workspace `MVP_Reconciliation\02`, `04`, `05` | the onboarding track's steps `2a`/`2b` migrating that package (`M-9`); AndroidApp's `proposal\` file joins this group as a **policy hold** (Q5c), no citer — 11 names |
| terminal package `STATE.md` only (5) | Server `docs\SV-B07_runtime_verification_report.md`, `SV-B08_deployment_hardening_report.md`; Dashboard `docs\WD-A11Y-01_validation_report.md`, `WD-PARITY-01_parity_report.md`; Workspace `prompts\PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` (after its live citer migrates) | a decision: the MVP packages' and `System_Tooling`'s `STATE.md` are frozen history that is never edited — `M-0` proposal 6 asks whether the mapping table covers them, as Chapter 8's own rule did |
| pinned tree or Design kit, no code (8) | PyApp `Documentation\Design_Implementation_Claude.md`, `GUI\screen_structures\improvements.md`; Dashboard `docs\WD-MOCKUP-UPGRADE_PROPOSAL.md`, `WD-UX-10_mockup_parity_report.md`; Workspace `System_Design_Architecture\proposal\00`, `01`, `02`, `03` | the Design initiative's owner or a Design-kit re-pin — not this track |
| code or config file (7) | PyApp `Documentation\plant_information_system_implementation_plan_v1.md`; Server `docs\SV-B07_dashboard_endpoint_coverage_report.md`; AndroidApp `docs\security_token_storage_acceptance.md`; Workspace `docs\proposals\PlantLibrary_Full_Implementation_Update.md`, `System_Design_Architecture\MODEL_RECOMMENDATION.md`, `System_Design_Architecture\proposal\04_APPROVED_DESIGN_REVISION_2026-07-10.md`, `prompts\reference\SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | a code edit in a batch (policy A.0.5: code-anchored files do not move) — not this track |

### 1c. The kit shape to mirror

`C:\Programmierung\Design_Template_Kit` at `8e708f8` (Kit 0.8.0): `README.md` with a folder map and a "contains / never
contains" table; `KIT_VERSION.md` (semver rule: patch = wording, minor = additive, major = breaking, bump in the same change;
changelog); `CONTRIBUTING.md` §1 "Verify like this, in this order" with a "what green means" table; `METHODOLOGY_SOURCE.md` (a
pin — version and path, no generator reads it); `anchoring-kit\INSTALL.md` + `install.mjs` whose header lists what it writes, in
order, idempotently, refusing to overwrite the pin without `--force`; `rule-block\DESIGN_RULES_BLOCK.md` between
`<!-- design-kit:begin -->`/`<!-- design-kit:end -->` ending "A prompt never overrides this block"; `skills\README.md` and
`CODEX_ADAPTATION.md` (byte-identical mirrors, the only permitted differences enumerated); `examples\anchored-target\` (a
reference anchored repo with `CLAUDE.md`, `AGENTS.md`, `design\conformance\CONSUMED_DESIGN.md` as the pin, the CI template). The
Design kit is Node for Playwright and ajv; this kit needs neither (G0 Q2).

### 1d. Gate `G0` — recorded 2026-09-15

The eleven questions and the five census sub-questions were presented with one recommendation each. **The operator's answer,
verbatim: "all recommendations accepted".** What that resolves to, per question, is the recommendation exactly as presented:

| Q | Decided |
|---|---|
| Q1 | `C:\Programmierung\Repo_Hygiene_Template_Kit`, its own git repository, `KIT_VERSION.md` starting at 0.1.0, no `node_modules`, no build step |
| Q2 | one stdlib-only Python 3 script (the `check_harness_parity.py` precedent) plus a thin pytest wrapper module in the repos that have a pytest suite (PyApp, Server); not Node |
| Q3 | in: the dated-deliverable naming rule and TYPE enum; the folder taxonomy as configurable deliverable roots with `INDEX.md`/`README.md` exempt and package-schema files exempt by name; per-root `INDEX.md` with the same-commit rule and the rename mapping table; the prompt proof-surface rule for `PROMPT`/`PROMPTS` files; the `CLAUDE.md`/`AGENTS.md` rule block between begin/end markers with line-ending-insensitive byte parity of the block; a per-repo decision record for exemptions and holds; optional modules for the root allowlist and the `.tmp\` scratch policy. Out, to the onboarding track: skill mirrors and the bridge table, the batch package schema, the validation harness, graphify. **Q3a:** the checker also verifies `INDEX.md` coverage (every file in a root has an index line) |
| Q4 | deliverable roots declared per repo; default `implementation\<Package>\{planning,proposal,handovers}` where a package exists; the superproject declares `repo-hygiene\`, `onboarding\` and a new `handovers\` that receives the root HANDOVER by `git mv`; product documentation folders (`docs\`, `Documentation\adr`, `GUI\`, `openapi\`) catalogued, not renamed — where "product documentation" is decided per repo by content: the suites' `docs\` are product notes with a few dated deliverables inside, while Workspace `docs\` and `docs\proposals\` hold nothing but deliverables (census §2.7) and are declared roots at `M-7`. **Q4b:** PyApp `Documentation\` is catalogued and left, listed as an exempt legacy corpus in PyApp's decision record; the nine `docs\` candidates (Server 4, Dashboard 4, AndroidApp 1) are moved by `git mv` into their package's `planning\` root, keeping the row id inside the topic |
| Q5 | the Chapter-8 procedure verbatim: `git mv` only, TYPE from the census classification, already-compliant names untouched, no case churn, holds for every live citation, an old→new table in the root's `INDEX.md`; the frozen and pinned sets of §1b listed as exempt in each repo's decision record and never renamed. **Q5a:** the git-created date wins, the header-date divergence noted in the mapping table. **Q5b:** a numbered chapter set becomes a dated folder `<TYPE>_<topic>_<YYYY-MM-DD>\` whose chapter names are left as they are. **Q5c:** a live package's `proposal\` files stay held until the onboarding track's steps `2a`/`2b` have migrated that package, then are renamed with the sweep; the M steps declare the dependency |
| Q6 | the kit's enum is fixed; a repo extends it only by a decision record entry; nothing enters the enum now: DECISION-shaped files are `PROPOSAL` with their status in the index line, REPORT-shaped desk research is `EVIDENCE` (an audit of the repo's own work would be `AUDIT`), GUIDE-shaped setup runbooks are product documentation, exempt by name |
| Q7 | each submodule commits on its own `main` in the step that changes it; the superproject bumps the gitlinks in one commit per step; nothing is pushed by a track session — pushing is the operator's, out of band |
| Q8 | the checker everywhere; the pytest wrapper where a suite exists; a `.github\workflows\repo-hygiene.yml` template; an optional pre-commit hook (not installed by default); the rule block for agents; the installer idempotent and re-runnable on a kit upgrade, refusing to overwrite a pin without `--force` |
| Q9 | `hygiene\CONSUMED_HYGIENE.md` for the pin (kit version and SOURCE commit) and `hygiene\HYGIENE_DECISIONS.md`, append-only, for exemptions, holds and enum extensions, entries `D-YYYY-MM-DD-nn`; parallel to `design\conformance\CONSUMED_DESIGN.md` |
| Q10 | three generic runbooks in `KIT\runbooks\` with `<PLACEHOLDERS>` — derive the kit from a source, anchor a repository, migrate an existing repository — and this instantiated runbook in `TARGET\repo-hygiene\`; a prompt exists in one place only |
| Q11 | every edit preserves the file's existing line endings; no `.gitattributes` introduced by this track; the checker normalises line endings before comparing the rule block |

Two consequences the runbook draws from the answers, stated once: `hygiene\` is the kit's anchoring folder in every repo,
the superproject included (`repo-hygiene\` stays the track's deliverable root — two different things); and the `.tmp\` scratch
module is **deferred** in every repo to the onboarding track's step `3`, which owns the per-suite scratch policy — each decision
record says so, and nothing in phase A edits a `.gitignore`.

### 1e. The fresh-context review of this runbook (2026-09-15)

A general-purpose reviewer with no prior context read the first draft against the commissioning prompt's checklist. Result:
items 1, 2, 3, 6 passed; item 7 passed with one hole (this section was an unfilled placeholder); items 4, 5, 8, 9 failed.
Findings and what changed: (4) `M-9` did not name `GM` as a precondition — added. (5) `A-6`'s and `A-7`'s done-when "zero
violations" was unreachable, because non-compliant, unheld names sat in their declared roots — AndroidApp's `proposal\` file is
now a Q5c policy hold, and `A-7` declares only the two package roots; Workspace's four loose roots are declared at `M-7` by a
decision entry `M-0` proposes (proposal 5). (8a) the `GM` row cited a section that does not exist — fixed. (8b) two hold sets
disagreed with the census: `GUI\screen_structures\improvements.md` was held in the draft but not in the register — the reviewer
was right about the disagreement and the register was wrong: the pinned Design initiative names the file four times in lines
that call its folder `screen_requirements/`, which the census's collision rule filtered out; the register was corrected by
hand (its method note says so), PyApp's holds are 4, the total 34. (8c) `A-7` labelled every Workspace hold "per Q5c" although
most are pinned, code or Design-kit citers that onboarding never releases — the holds are now grouped by what releases them
(§1b), and "seven of 33" became the exact groups. (9) `A-n`/`M-n` placeholders were not told to be filled — fixed; `K-3`'s
Watch quoted SOURCE counts no register carries — dropped; `K-2` was too large for one session — split into `K-2a`/`K-2b`/`K-2c`.
Of five observations, three were applied: Q4's per-repo reading of "product documentation" is stated in §1d; `GK`'s
recommendation reads "the same verdict at the recorded HEAD"; `K-2a`'s read-first names the Design kit's `CONTRIBUTING.md`
explicitly. The two others were confirmations (the `onboarding\INDEX.md` link fix in `M-1` is correct; the shared paste block
for `A-2`…`A-7` and `M-2`…`M-7` is the right shape, and the fill table is what `GA` confirms). The draft was also scanned with
SOURCE's two proof-surface detectors: zero hits, before and after the fixes.

## 2. How to use this runbook

1. **One fresh session per step.** No step is resumed inside another session's context.
2. Set the model and reasoning from the step's own line **before** pasting.
3. `cwd` is stated per step; it is one of the three roots or a submodule folder (§0).
4. Paste the fenced block **exactly as it stands**, after filling the placeholders the step names (`<SUITE>`, the step id). It is
   the whole prompt.
5. The **Watch** paragraph under a block is for you, not for the paste.
6. Every session here can spawn agents (VS Code entry point). A session takes the inline fallback only after a real refused
   or dead Agent call and says so in its report.
7. Commit discipline is G0 Q7: a submodule commits on its own `main` in the step that changes it; the superproject bumps the
   gitlink in one commit per step; no track session pushes.
8. Flip the step in §L in the same commit as its output. For a `K-*` step the output commit is in KIT, so the flip is a
   separate one-line superproject commit `repo-hygiene: ledger <step>` — the only thing that commit carries.
9. SOURCE is read at `fc5a14c` and never written; a `K-3` checker run over it writes nothing there (no cache, no bytecode).
10. The onboarding track shares this repository and its `onboarding\` folder is already compliant. The two tracks do not share
    steps, but they touch the same files twice: the rule block (phase A) and the per-suite `CLAUDE.md`/`AGENTS.md` (onboarding
    step `3`) — either order works because the block is marked and the checker reports its loss; and the eleven live-package
    holds (§1b) wait for onboarding `2a`/`2b` (`M-9`).

## 3. Step map — the sequence and its state

| Step | What it does | Model · reasoning | cwd | State |
|---|---|---|---|---|
| `G0` | the eleven questions + five census sub-questions | operator | — | **answered** 2026-09-15 (§1d) |
| `K-1` | create KIT; `KIT_SPEC.md` from the inventory and G0 — what the kit contains and never contains | **Fable 5.1 · xhigh** | `C:\Programmierung` → KIT | done 2026-09-16 |
| `K-2a` | the checker (check / census / self-test), the pytest wrapper, the rule block, the negative fixtures | **Fable 5.1 · high** | KIT | done 2026-09-16 |
| `K-2b` | the installer, the templates, `examples\anchored-target`, `CONTRIBUTING.md` with the verification order | **Fable 5.1 · high** | KIT | done 2026-09-16 |
| `K-2c` | `README.md`, `SOURCE_HARNESS.md` (the SOURCE pin), the three generic runbooks, `KIT_VERSION.md` | **Fable 5.1 · high** | KIT | done 2026-09-16 |
| `K-3` | the self-test: the checker reproduces SOURCE's baseline and fails a non-compliant scratch tree; the record | **Sonnet 5 · thinking** | KIT | done 2026-09-16 |
| `K-4` | version 0.1.0, changelog, commit, tag | **Sonnet 5 · thinking** | KIT | done 2026-09-16 |
| `GK` | operator gate: the kit at `v0.1.0` is accepted for anchoring | operator | — | **answered** 2026-09-16 (§4) |
| `A-1` | anchor the superproject (roots `repo-hygiene\`, `onboarding\`, `handovers\`; root-allowlist module on) | **Opus 5 · high** | TARGET | done 2026-09-16 |
| `A-2` | anchor PyApp | **Opus 5 · high** | `PlantLibrary_PyApp` → TARGET | todo |
| `A-3` | anchor Server | **Opus 5 · high** | `PlantLibrary_Server` → TARGET | todo |
| `A-4` | anchor SharedContracts | **Opus 5 · high** | `PlantLibrary_SharedContracts` → TARGET | todo |
| `A-5` | anchor Dashboard | **Opus 5 · high** | `PlantLibrary_Dashboard` → TARGET | todo |
| `A-6` | anchor AndroidApp | **Opus 5 · high** | `PlantLibrary_AndroidApp` → TARGET | todo |
| `A-7` | anchor Workspace (the largest decision record: four frozen trees, two pinned, 15 holds) | **Opus 5 · high** | `PlantLibrary_Workspace` → TARGET | todo |
| `GA` | operator gate: the seven decision records (exempt, frozen, pinned, held sets) are confirmed — `M-0` derives from them | operator | — | open |
| `M-0` | the rename map per repo, re-verified against the tree, six proposals, presented at `GM` | **Fable 5.1 · high** | TARGET | todo |
| `GM` | operator gate: the map is confirmed before the first `git mv` | operator | — | open |
| `M-1` | migrate the superproject | **Opus 5 · high** | TARGET | todo |
| `M-2` | migrate PyApp | **Opus 5 · high** | `PlantLibrary_PyApp` → TARGET | todo |
| `M-3` | migrate Server | **Opus 5 · high** | `PlantLibrary_Server` → TARGET | todo |
| `M-4` | migrate SharedContracts | **Opus 5 · high** | `PlantLibrary_SharedContracts` → TARGET | todo |
| `M-5` | migrate Dashboard | **Opus 5 · high** | `PlantLibrary_Dashboard` → TARGET | todo |
| `M-6` | migrate AndroidApp | **Opus 5 · high** | `PlantLibrary_AndroidApp` → TARGET | todo |
| `M-7` | migrate Workspace (declares its four loose roots first) | **Opus 5 · high** | `PlantLibrary_Workspace` → TARGET | todo |
| `M-8` | the closing pass: checker green over the whole tree, census re-run and diffed against the register, the HANDOVER, the kit's changelog | **Sonnet 5 · thinking** | TARGET, then KIT | todo |
| `M-9` | rolling: release held names as their citers change (onboarding `2a`/`2b`) or the operator releases them | **Opus 5 · high** | the repo that holds the name → TARGET | rolling |

Dependencies: `K-1` → `K-2a` → `K-2b` → `K-2c` → `K-3` → `K-4` → `GK` → `A-1` → `A-2` … `A-7` → `GA` → `M-0` → `GM` → `M-1` …
`M-7` → `M-8`; `M-9` any time after `M-8` for a name whose hold is released. `A-2`…`A-7` are independent of each other and may
run in any order once `A-1` is done; `M-2`…`M-7` likewise once `GM` is answered.

## 4. Gates the operator owns — record the answer here, in the step's commit

| Gate | Question | Recommendation | decided |
|---|---|---|---|
| `GK` | Is the kit at `v0.1.0` accepted for anchoring into TARGET? Its self-test record (`K-3`) and `CONTRIBUTING.md` §1's "what green means" are the evidence | yes, if `K-3` reproduced the SOURCE baseline — the same verdict at the SOURCE HEAD the record names — and the negative tree failed with every planted defect named | **yes** — 2026-09-16, recorded in the `A-1` commit. The operator's answer, verbatim: "Yes, accept (Recommended)", given to the question that quoted the `K-3`/`K-4` evidence: `fail — 3 violations, 2 held, 1 skipped` over SOURCE, the 3 being the kit's `INDEX.md`-coverage addition that `K-4` wrote into `KIT_SPEC.md` §14 as the baseline; exactly the two held names; zero name/proof lines over 42 prompt files; the negative tree naming all six planted defects, the line-endings-only pair passing |
| `GA` | Are the seven decision records (`hygiene\HYGIENE_DECISIONS.md`, entry `-01` in each repo) confirmed as the exempt, frozen, pinned and held sets `M-0` maps against? | yes, if each record lists exactly the §12 row for that repo (which is the census §2/§3 sets) and nothing else | |
| `GM` | Is the rename map (`repo-hygiene\MATRIX_rename-map_<date>.md`) confirmed, old → new per file, holds with target-on-release, date divergences, set folders, and the six proposals of §13? | yes, after reading the holds and the six proposals (§13, `M-0`) | |

## 5. Step `K-1` — create the kit and write its specification

**Fable 5.1 · xhigh.** The open-ended shape: it decides what the kit is, in writing, once. Depends on G0 Q1, Q2, Q3/Q3a, Q6,
Q9, Q10, Q11. `cwd`: `C:\Programmierung` to create the repository, then inside it.

```text
Step K-1 of repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md (TARGET = C:\Programmierung\SW_Development).
cwd C:\Programmierung. Create C:\Programmierung\Repo_Hygiene_Template_Kit as a new git repository on main and write its
specification. No tooling is built in this step; nothing under SOURCE (C:\Programmierung\Orchestrator_System) or TARGET is
changed except the ledger flip named at the end.

Read first: TARGET\repo-hygiene\REGISTER_hygiene-harness-inventory_2026-09-15.md in full (sections 1, 3, 4 are the input);
the runbook's section 1d (the G0 record), section 1b (the hold groups) and section 1c (the Design kit shape); TARGET\
repo-hygiene\REGISTER_target-corpus-census_2026-09-15.md sections 4, 5 and 6 (what the targets look like, so the spec
parameterises the right things); C:\Programmierung\Design_Template_Kit at 8e708f8: README.md, KIT_VERSION.md,
CONTRIBUTING.md section 1, METHODOLOGY_SOURCE.md, anchoring-kit\INSTALL.md, the header comment of anchoring-kit\install.mjs,
anchoring-kit\rule-block\DESIGN_RULES_BLOCK.md. Do not open SOURCE for anything the inventory already states; open a SOURCE
file only to quote a regex or a set literally, and read only.

Write KIT_SPEC.md with these sections, each self-contained: 0 what the kit contains and never contains (a two-column table,
the Design kit's shape); 1 the rule - the pattern and TYPE enum verbatim from inventory section 4, topic rules, no case churn,
the date rule (git-created), exempt names, exempt subfolders, held names, catalogued conventions (validation evidence
<BATCH>_<slug>, evidence packs, id-prefixed and row-anchored product notes, ADRs, page contracts, generated docs, version
pins by name), and the dated set folder <TYPE>_<topic>_<YYYY-MM-DD>\ whose members are exempt from the file rule and which
takes one index line (G0 Q5b); 2 deliverable roots - declared per repo in the pin, the default implementation\<Package>\
{planning,proposal,handovers} with the type routing, a root checks its direct files and its set folders, a subfolder is a
root only when declared, a root change is a decision entry; 3 INDEX.md - the line shape, the same-commit rule, the coverage
check (a file's basename occurs in its root's INDEX.md; no line format is enforced, so an existing table-shaped index
passes), the "Renamed <date>" mapping table and held rows with target-on-release; 4 the prompt proof-surface rule - the argv
and prose detectors and the negation guard verbatim, the sanctioned-launcher parameter (empty by default), the per-repo file
floor, handovers never scanned; 5 the rule block - markers <!-- repo-hygiene:begin --> / <!-- repo-hygiene:end -->, the block
text (which ends "A prompt never overrides this block"), parity of the marked block between CLAUDE.md and AGENTS.md after
line-ending normalisation, AGENTS.md created when absent; 6 the decision record - hygiene\HYGIENE_DECISIONS.md, append-only,
entries D-YYYY-MM-DD-nn with the operator's verbatim words where a gate answered, what needs an entry (an exemption, a hold,
a release, an enum extension, a root change, an allowlist change); 7 the checker contract - one stdlib-only Python 3 script,
modes check (exit 0/1, one line per violation naming the file and the rule, held names reported as held not as violations),
census (the register's columns per root: file, class, git-created, compliance) and --self-test (mutate a temporary copy,
prove a failure, restore, pass); configuration read from hygiene\CONSUMED_HYGIENE.md and hygiene\HYGIENE_DECISIONS.md, never
from literals in the script; runs from any cwd inside the repo; writes nothing; Windows paths; 8 the pytest wrapper - one
module that imports the checker and asserts its verdict, installed only where the pin says a suite exists; 9 the installer -
stdlib Python, what it writes in order (scripts\hygiene\ checker copy, the wrapper where applicable, .github\workflows\
repo-hygiene.yml, the rule block into CLAUDE.md and AGENTS.md preserving each file's line endings, INDEX.md seeded where a
declared root has none, hygiene\HYGIENE_DECISIONS.md seeded if absent, hygiene\CONSUMED_HYGIENE.md last and never
overwritten without --force), idempotent, --roots and --modules flags, the optional pre-commit hook behind a flag, exit codes;
10 the optional modules - root allowlist (the allowlist and retired names live in the decision record) and scratch policy
(one gitignored .tmp\ root, retired names fail loud); 11 versioning and the SOURCE pin - KIT_VERSION.md semver rule copied
from the Design kit, SOURCE_HARNESS.md pinning C:\Programmierung\Orchestrator_System at fc5a14c with the inventory's
row-to-kit-file map; 12 the three runbooks the kit carries (derive, anchor, migrate) - their section shapes, mirroring this
runbook's; 13 out of scope, named: skill mirrors and the bridge table, the batch package schema, the validation harness and
.tmp\ interior, the v5-proposal, chunk and envelope parity checks, graphify, the Telegram rule, STATE.md as the decision
home; 14 the K-3 reproduction target verbatim from inventory section 4.

Also write a two-paragraph README.md that says what the kit is and points at KIT_SPEC.md, and .gitignore with .tmp/ and
__pycache__/. Nothing else - no checker, no templates, no runbooks yet.

Constraints: no node_modules, no build step, no package.json; nothing copied from SOURCE except quoted regexes and set
literals with their origin cited; every G0 answer maps to a spec clause and every inventory row 1-11 is either in a section
or in section 13; the spec names no test invocation - the verification order is CONTRIBUTING.md's, written in K-2b.

Done when: the repository exists on main with one commit carrying KIT_SPEC.md, README.md and .gitignore; a table at the end
of KIT_SPEC.md maps inventory rows 1a-11b and G0 Q1-Q11 (with Q3a, Q4b, Q5a-c) to spec sections, with no row unmapped; git
status clean in KIT; SOURCE untouched (git -C SOURCE status shows nothing new); TARGET touched only by the ledger flip.

Commit line (KIT): kit: K-1 - specification from the SOURCE harness inventory and the G0 record
Ledger (TARGET, separate commit): repo-hygiene: ledger K-1
```

**Watch:** the session will want to start writing the checker. It must not — `K-2a` is the next session and the spec is what it
builds against. If the spec grows past ~400 lines, it is re-deriving the inventory instead of citing it; send it back to the
register. The set-folder clause (§1 of the spec) is new relative to SOURCE; make sure it says a set folder needs an index
line and its members need none.

## 6. Step `K-2a` — the checker, the wrapper, the rule block, the negative fixtures

**Fable 5.1 · high.** Building against a written specification. Depends on G0 Q2, Q3/Q3a, Q11. `cwd`: KIT.

```text
Step K-2a of TARGET\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md. cwd C:\Programmierung\
Repo_Hygiene_Template_Kit on main, tree clean at K-1's commit. Build the checker and what proves it; the installer, templates,
example and CONTRIBUTING are K-2b, the documents K-2c.

Read first: KIT_SPEC.md in full (sections 1-5, 7, 8 are built here); for each regex or set literal the spec quotes, the
SOURCE file it cites, read only, to copy it exactly; C:\Programmierung\Design_Template_Kit\CONTRIBUTING.md section 1 for the
shape of a "what green means" table (the kit's own CONTRIBUTING is written in K-2b, so this step records its verdict lines
in a short VERIFICATION_NOTES.md that K-2b folds in).

Build, in this order: checker\repo_hygiene_check.py (stdlib only; modes check, census, --self-test; configuration from
hygiene\CONSUMED_HYGIENE.md and hygiene\HYGIENE_DECISIONS.md; every rule of spec sections 1-5 including the INDEX.md coverage
check, set folders, held names, the proof-surface detectors with their negation guard and the sanctioned-launcher exemption,
the marked-block parity after line-ending normalisation; one output line per violation naming file and rule; exit codes per
spec section 7); checker\test_repo_hygiene_kit.py (the pytest wrapper template: one module, imports the checker by path,
asserts the check verdict, no fixtures); rule-block\HYGIENE_RULES_BLOCK.md between the markers, ending "A prompt never
overrides this block", with {{KIT_ROOT}} and {{KIT_VERSION}} placeholders; tests\ (the kit's own negative fixtures, each a
small committed tree with a hygiene\ configuration: an undated file in a root; a PROMPT_ file naming a bare-root argv; a
PROMPTS_ file asking in prose for a whole-suite run; a CLAUDE.md/AGENTS.md pair whose marked blocks differ by one byte; a
pair that differs only in line endings, which must pass; a root file missing from its INDEX.md; a set folder without an
index line; a held name, which must be reported as held and not fail); checker\VERIFICATION_NOTES.md listing, for the
checker over each fixture and for --self-test, the exact verdict line expected.

Constraints: Python 3.12 syntax, stdlib only, no third-party import; no absolute path from this machine inside any kit
file; the checker never writes; every project fact comes from the two hygiene\ files at run time, never from the script;
nothing under SOURCE or TARGET changed except the ledger flip.

Done when: over every fixture the checker prints the verdict VERIFICATION_NOTES.md names (each planted defect named, the
line-endings-only pair and the held name passing) and --self-test passes; one commit on KIT main; SOURCE untouched.

Commit line (KIT): kit: K-2a - checker, pytest wrapper, rule block, negative fixtures, verification notes
Ledger (TARGET, separate commit): repo-hygiene: ledger K-2a
```

**Watch:** if the session proposes a YAML or JSON configuration instead of reading the two `hygiene\` markdown files, that
is a spec change; it stops and raises it rather than building around it. A fixture that "passes" without a quoted verdict
line in the notes is not a fixture yet.

## 7. Step `K-2b` — the installer, the templates, the example, `CONTRIBUTING.md`

**Fable 5.1 · high.** Depends on G0 Q8, Q9, Q11. `cwd`: KIT.

```text
Step K-2b of TARGET\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md. cwd C:\Programmierung\
Repo_Hygiene_Template_Kit on main, tree clean at K-2a's commit. Build the installer and everything an anchoring writes into a
target; then write CONTRIBUTING.md, the document every later done-when cites.

Read first: KIT_SPEC.md sections 3, 5, 6, 9, 10; checker\VERIFICATION_NOTES.md; C:\Programmierung\Design_Template_Kit\
anchoring-kit\install.mjs (header and the order of writes; read only), anchoring-kit\INSTALL.md, and the Design kit's
CONTRIBUTING.md section 1 (the shape of a verification order and a "what green means" table).

Build: installer\install.py and installer\INSTALL.md (what it writes, in order, idempotent; --target, --roots, --modules,
--with-pytest-wrapper, --with-pre-commit, --force; refuses to overwrite an existing pin without --force and exits 0 with a
notice on a plain re-run; preserves each edited file's line endings; creates AGENTS.md when absent; INSTALL.md ends with a
"Verify" section stating the command that checks an anchored repository and the verdict line it prints on pass, on
pass-with-holds, and on failure); templates\ (INDEX_TEMPLATE.md, CONSUMED_HYGIENE_TEMPLATE.md, HYGIENE_DECISIONS_TEMPLATE.md,
RUNBOOK_TEMPLATE.md with the section shape of this runbook, HANDOVER_CONTINUATION_TEMPLATE.md - scope, constraints, done-when,
commit line, never a proof surface -, AUDIT_migration-record_TEMPLATE.md with the Chapter-8 disposition table,
workflows\repo-hygiene.yml, hooks\pre-commit); examples\anchored-target\ (a minimal repository the installer has actually
been run on: CLAUDE.md and AGENTS.md with the block, hygiene\ with a pin and a decision record, one package with planning\,
proposal\, handovers\ each holding an INDEX.md and one compliant file, one PROMPTS_ file, one dated set folder; committed as
files, not generated at verify time); CONTRIBUTING.md section 1 "Verify like this, in this order" listing every verification
the kit owns with a "what green means" table carrying the exact verdict lines (the example passes; every negative fixture of
K-2a fails naming its planted defect; --self-test passes; the installer re-run exits 0 with the pin notice; the installer
with --force re-pins), folding checker\VERIFICATION_NOTES.md in and deleting it; section 2 the invariants (stdlib only; no
project fact in any kit file; the example is the only anchored tree; a copy the installer writes is byte-identical to the
kit's copy; a mirror difference is drift).

Constraints: stdlib only; the installer never edits anything outside the paths it lists; every kit file the installer copies
into a target is byte-identical to the kit's copy; no absolute path from this machine inside any kit file; nothing under
SOURCE or TARGET changed except the ledger flip.

Done when: CONTRIBUTING.md section 1 exists and its verification order, run exactly as written, reports what its "what green
means" table says for every row; the example tree is committed and passes; INSTALL.md's Verify section names the verdict
lines; one commit on KIT main; SOURCE untouched.

Commit line (KIT): kit: K-2b - installer, templates, example anchored target, CONTRIBUTING with the verification order
Ledger (TARGET, separate commit): repo-hygiene: ledger K-2b
```

**Watch:** the "what green means" table is the contract every later done-when cites; if a row says "pass" without the
literal verdict line the tool prints, send it back. The installer's pin refusal must be a notice with exit 0 on a plain
re-run and a refusal with a non-zero exit only when the pin would change without `--force` — the Design kit's 0.6.0 lesson.

## 8. Step `K-2c` — the documents

**Fable 5.1 · high.** Depends on G0 Q1, Q10, Q11. `cwd`: KIT.

```text
Step K-2c of TARGET\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md. cwd C:\Programmierung\
Repo_Hygiene_Template_Kit on main, tree clean at K-2b's commit. Write the kit's documents; change no tooling.

Read first: KIT_SPEC.md sections 0, 11, 12, 13; CONTRIBUTING.md; installer\INSTALL.md; TARGET\repo-hygiene\
PROMPTS_repo-hygiene-track-runbook_2026-09-15.md sections 0, 2, 3 and one K, one A and one M step, as the shape the three
generic runbooks mirror; TARGET\repo-hygiene\REGISTER_hygiene-harness-inventory_2026-09-15.md section 1 (the row-to-kit-file
map goes into the pin); Design_Template_Kit\README.md, KIT_VERSION.md, METHODOLOGY_SOURCE.md (shape only).

Write: README.md (what the kit is, the "contains / never contains" table, the folder map, prerequisites - Python 3 on PATH,
nothing else -, how an install is verified by pointing at INSTALL.md and CONTRIBUTING.md); SOURCE_HARNESS.md (the pin:
C:\Programmierung\Orchestrator_System, main, fc5a14c, pinned on 2026-09-15; a table mapping inventory rows 1a-11b to the kit
file that carries each, with "out" rows named; the upgrade rule: re-derive when SOURCE's harness moves, by the derive
runbook); runbooks\RUNBOOK_derive-the-kit.md, runbooks\RUNBOOK_anchor-a-repository.md, runbooks\
RUNBOOK_migrate-an-existing-repository.md - each with the section shape of the track runbook (0 what it is, 1 where things
stand, 2 how to use, 3 step map, one section per step with model and reasoning, cwd, a paste block, a Watch paragraph, the
gates, the ladder, the ledger), every project fact replaced by a <PLACEHOLDER> named in a table at the top, every paste block
stating scope, read-first, constraints, done-when and the commit line and citing CONTRIBUTING.md section 1 or INSTALL.md for
its verdict; the migrate runbook carries the Chapter-8 procedure as its steps: census, rename map with holds and date
divergences, the operator gate before the first git mv, git mv, the reference sweep with editable and never-edit lists, INDEX
regeneration with the mapping table, the closing record; KIT_VERSION.md with the semver rule and an empty "0.1.0 - <date>"
changelog entry that K-4 completes.

Constraints: a prompt exists in one place only - the generic runbooks carry placeholders, never a copy of a TARGET step; no
project name, path, decision id or row id from TARGET inside a runbook (the pin is the one file that names SOURCE); no
document names a test invocation; line endings LF throughout the kit.

Done when: the four documents and three runbooks exist; a grep for "PlantLibrary", "SW_Development" and "Conductor" across
runbooks\ returns nothing; the placeholder tables list every <PLACEHOLDER> used; CONTRIBUTING.md section 1 still reports
green for every row; one commit on KIT main.

Commit line (KIT): kit: K-2c - README, SOURCE pin, the three generic runbooks, KIT_VERSION
Ledger (TARGET, separate commit): repo-hygiene: ledger K-2c
```

**Watch:** the derive runbook is the one that makes the kit re-derivable; if it reads like a summary of the track runbook
rather than a procedure a future session can follow against a moved SOURCE, send it back. The grep in done-when is the
placeholder discipline; a hit is a defect, not a note.

## 9. Step `K-3` — the self-test against SOURCE's baseline

**Sonnet 5 · thinking.** Mechanical verification of a written contract. Depends on G0 Q2, Q11. `cwd`: KIT.

```text
Step K-3 of TARGET\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md. cwd C:\Programmierung\
Repo_Hygiene_Template_Kit on main, tree clean at K-2c's commit. Prove the kit reproduces the source harness before it touches
any target, and prove it fails what it should. SOURCE = C:\Programmierung\Orchestrator_System at fc5a14c or later, read only;
its working tree may be dirty with instance work - that is not yours and not a stop.

Read first: KIT_SPEC.md section 14 (the reproduction target) and section 7 (the checker contract); CONTRIBUTING.md section 1;
TARGET\repo-hygiene\REGISTER_hygiene-harness-inventory_2026-09-15.md sections 1 (rows 5, 6, 9a) and 4 (the baseline facts);
installer\INSTALL.md for how a configuration is expressed.

Do: (1) under KIT\.tmp\k3\ write a throwaway configuration equivalent to SOURCE's sets - roots implementation/Conductor_V2/
{planning,proposal,handovers} with handovers using the date-anywhere variant, exempt names INDEX.md, README.md,
conductor-v5-system-proposal.md, META_WORK_PLAN_2026-08-18.md, exempt subfolder planning/gap, held names
FULL_AUTONOMY_PROPOSAL_2026-08-13.md and GAP_REGISTER_FULL_AUTONOMY_2026-08-13.md, sanctioned launcher run_validation.py,
block markers absent (SOURCE has none; that check is skipped, and the skip is reported) - and run the checker's check and
census modes over SOURCE with that configuration from KIT's cwd, with bytecode writing and every cache disabled, verifying
before and after with git -C SOURCE status that nothing new appeared under SOURCE; (2) run the verification order of
CONTRIBUTING.md section 1 in full; (3) build under KIT\.tmp\k3\bad\ a deliberately non-compliant tree - an undated file in a
root, a PROMPT_ file with a bare-root argv, a PROMPTS_ file asking in prose for a whole suite, a CLAUDE.md/AGENTS.md pair
differing by one byte inside the block and a pair differing only in line endings (must pass), a root file absent from its
INDEX.md, a set folder without an index line - and run check over it; (4) record everything in KIT_VERSION.md's 0.1.0 entry
under "Self-test record" (date, SOURCE HEAD at run time, the configuration used, the verdict lines quoted, the census counts
per root, the negative tree's verdict lines) and in CONTRIBUTING.md section 1's table where a row was missing an expected
verdict; (5) delete KIT\.tmp\k3\.

Constraints: nothing under SOURCE written (the two git status listings are quoted in the record and must be identical);
nothing under TARGET changed except the ledger flip; no kit tooling changed in this step - a defect found here is written
into the record as a finding for K-4 to decide (fix now in K-4 or defer to 0.1.1), never patched silently.

Done when: over SOURCE, check reports zero violations and exactly the two held names as held, and the proof-surface scan
reports zero violations over at least 20 PROMPT_/PROMPTS_ files; the negative tree fails with every planted defect named and
the line-endings-only pair passes; CONTRIBUTING.md section 1 reports green for every row; the record is in KIT_VERSION.md;
one commit on KIT main.

Commit line (KIT): kit: K-3 - self-test: SOURCE baseline reproduced, negative tree fails as planted
Ledger (TARGET, separate commit): repo-hygiene: ledger K-3
```

**Watch:** "zero violations" over SOURCE is the whole point; if the checker reports even one, the kit's rule is wider than
SOURCE's and `K-4` must decide. The two `git status` listings must match line for line — SOURCE's tree is live and dirty, and
a new entry means the checker wrote something. The census counts per root are the numbers a re-derivation compares against;
they belong in the record even though no register carries them yet.

## 10. Step `K-4` — version, commit, the first tag

**Sonnet 5 · thinking.** Depends on G0 Q1. `cwd`: KIT.

```text
Step K-4 of TARGET\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md. cwd C:\Programmierung\
Repo_Hygiene_Template_Kit on main, tree clean at K-3's commit.

Read first: KIT_VERSION.md (the 0.1.0 entry and K-3's self-test record, including any finding it left for this step);
CONTRIBUTING.md section 1.

Do: decide each K-3 finding - fix it in this step if it is a defect in the kit's own contract, or record it as deferred to
0.1.1 with the reason; if anything was fixed, run CONTRIBUTING.md section 1's order again and update the record; set the
current version in KIT_VERSION.md to 0.1.0 and complete the changelog entry (what the kit contains, the SOURCE pin, the
self-test summary, the deferred findings); make sure README.md and the rule block's {{KIT_VERSION}} default agree with it;
commit; tag v0.1.0 on that commit.

Constraints: no new feature; no change to the spec beyond the findings decided here; nothing pushed.

Done when: git tag lists v0.1.0 on the head of main, the tree is clean, CONTRIBUTING.md section 1 reports green for every row
at that commit, and KIT_VERSION.md's current version reads 0.1.0.

Commit line (KIT): kit: K-4 - version 0.1.0; tag v0.1.0
Ledger (TARGET, separate commit): repo-hygiene: ledger K-4; GK opened
```

**Watch:** after this step answer `GK` in §4 (a yes on the `K-3` record is enough) and record it in the `A-1` commit. Nothing
in phase A starts before that line exists.

## 11. Step `A-1` — anchor the superproject

**Opus 5 · high.** Structured execution of `INSTALL.md`. Depends on G0 Q4, Q8, Q9, Q11, and `GK`. `cwd`: TARGET.

```text
Step A-1 of repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md. cwd C:\Programmierung\SW_Development on main,
tree clean. Anchor the superproject to the kit at v0.1.0 (C:\Programmierung\Repo_Hygiene_Template_Kit). No submodule is
touched; nothing is renamed or moved; the root HANDOVER stays where it is until M-1.

Read first: the runbook's sections 1b, 1d and 4 (GK must be answered - stop if it is not); KIT\installer\INSTALL.md in full;
KIT\KIT_SPEC.md sections 2, 3, 5, 6, 10; repo-hygiene\REGISTER_target-corpus-census_2026-09-15.md sections 2.1, 3 (the
superproject's four holds) and 4 (its row); CLAUDE.md and AGENTS.md here (both carry mixed CRLF/LF inside one file - the
installer must preserve that, and the parity check must pass across it).

Do: run the installer per INSTALL.md with roots repo-hygiene, onboarding, handovers; modules root-allowlist on, scratch off;
no pytest wrapper (no suite here); no pre-commit hook. Then complete what the installer seeds: handovers\INDEX.md (new,
empty index with the header); hygiene\HYGIENE_DECISIONS.md entry D-<today>-01 recording, with the G0 words quoted: the three
roots and their routing (HANDOVER/FINDING to handovers\, every other type to the track folder that owns it); the held names
from census section 3 with their citer (the four names cited by the onboarding runbook - held against renaming, not against
a move, since a move keeps the basename) and, for IMPLEMENTATION_PLAN.md, the note that its disposition is M-0's proposal 1;
the root allowlist (the exact root listing today, Todo.md included as an ignored-but-present entry) and the retired names
(none); the scratch module deferred to onboarding step 3. Check CLAUDE.md and AGENTS.md carry the marked block and nothing
else changed in them. Record the GK answer in the runbook's section 4. Commit.

Constraints: edits preserve each file's line endings; no .gitattributes; no edit under onboarding\ (its INDEX.md already
lists every file); no change to any submodule or gitlink; the graphify and Testing sections of CLAUDE.md/AGENTS.md are the
onboarding track's and stay as they are.

Done when: INSTALL.md's Verify section reports its pass-with-holds verdict for this repository with exactly the four held
names listed as held and zero violations; hygiene\CONSUMED_HYGIENE.md pins kit 0.1.0 and SOURCE fc5a14c; the decision
record's -01 entry exists; the GK answer is in the runbook's section 4; one commit on main carrying hygiene\, scripts\
hygiene\, .github\workflows\repo-hygiene.yml, handovers\INDEX.md, CLAUDE.md, AGENTS.md and the runbook (ledger flip + GK).

Commit line: repo-hygiene: A-1 - superproject anchored to kit 0.1.0; GK recorded
```

**Watch:** the root-allowlist module is on here and nowhere else — the superproject root is exactly where new markdown must
not be born. If the installer reports the block inserted but the parity check fails, the cause is the mixed line endings in
these two files; the checker normalises, the installer must not "fix" the file's endings. `Todo.md` is git-ignored but
present; the allowlist polices the listing, as SOURCE's does. `IMPLEMENTATION_PLAN.md` at the root is a non-compliant name
outside every declared root, so it is not a violation here; it is the allowlist's business and `M-0`'s.

## 12. Steps `A-2` … `A-7` — anchor one submodule each

**Opus 5 · high, one session per submodule**, in the onboarding runbook's suite order: `A-2` PyApp, `A-3` Server, `A-4`
SharedContracts, `A-5` Dashboard, `A-6` AndroidApp, `A-7` Workspace. Depends on G0 Q4/Q4b, Q5/Q5c, Q6, Q8, Q9, Q11. `cwd`: the
submodule folder, then TARGET for the gitlink bump. One paste block; before pasting, replace `A-n` with the step id and
`<SUITE>` with the folder name, and read the row below — it is what the decision record must say and what `GA` confirms.

| `<SUITE>` | declared roots | pytest wrapper | decision record seeds (census §2.n and §3; hold groups per §1b) |
|---|---|---|---|
| `PlantLibrary_PyApp` | `implementation\System_V1_Implementation\{planning,proposal,handovers}` | yes | frozen `implementation\MVP\`, `implementation\Archive_PreMVP\`; exempt legacy corpus `Documentation\` (Q4b, 31 files never renamed, listed by name); exempt by name `PRODUCT.md`, `DESIGN.md`; generated `.docpipeline\`, `app\**\*.md`; held — live-package group: `proposal\PYAPP_V1_PROPOSAL.md` (`STATE.md`, Q5c); pinned group: `Documentation\Design_Implementation_Claude.md`, `GUI\screen_structures\improvements.md`; code group: `Documentation\plant_information_system_implementation_plan_v1.md`; scratch deferred |
| `PlantLibrary_Server` | the same three | yes | frozen `implementation\MVP\`; exempt by name `docs\local_android_test_environment.md`; held — live-package group: `proposal\SERVER_V1_PROPOSAL.md` (Q5c); terminal-`STATE.md` group: `docs\SV-B07_runtime_verification_report.md`, `docs\SV-B08_deployment_hardening_report.md`; code group: `docs\SV-B07_dashboard_endpoint_coverage_report.md`; `docs\SV-CONTRACT-01_contract_validation_report.md` is free; scratch deferred |
| `PlantLibrary_SharedContracts` | the same three | no (one test module, no pytest configuration — recorded) | frozen `implementation\MVP\`, `generated\**`; exempt by name `CONTRACT_VERSION.md`, `generated\CLIENT_MANIFEST.md`, `openapi\changelog.md`; held — live-package group: `proposal\SHAREDCONTRACTS_V1_PROPOSAL.md` (Q5c); scratch deferred |
| `PlantLibrary_Dashboard` | the same three | no | frozen `implementation\MVP\`, `references\PlantLibrary_pythonApp_old\`; held — live-package group: `proposal\DASHBOARD_V1_PROPOSAL.md` (Q5c); terminal-`STATE.md` group: `docs\WD-A11Y-01_validation_report.md`, `docs\WD-PARITY-01_parity_report.md`; pinned group: `docs\WD-MOCKUP-UPGRADE_PROPOSAL.md`, `docs\WD-UX-10_mockup_parity_report.md`; scratch deferred |
| `PlantLibrary_AndroidApp` | the same three | no | frozen `implementation\MVP\`; held — live-package group: `proposal\ANDROIDAPP_V1_PROPOSAL.md` (a **policy hold** per Q5c, no citer — the record says so); code group: `docs\security_token_storage_acceptance.md`; the three git-tracked skill mirrors are the onboarding track's, untouched; scratch deferred |
| `PlantLibrary_Workspace` | `implementation\System_V1_Implementation\{planning,proposal,handovers}`, `implementation\System_Design_Architecture\{planning,proposal,handovers}` — **only these six here**; the four loose roots (`docs\`, `docs\proposals\`, `prompts\`, `implementation\Server_VM_Setup\`) and `MVP_Reconciliation\` are declared at `M-7` after `GM` (`M-0` proposal 5), so phase A's verdict is reachable | no | frozen `implementation\System_Integration_MVP\`, `implementation\System_Tooling\`, `strategy\Cross_Platform_Strategy\`, `system_description\`; pinned `methodology\GUI_Improvement_Methodology\`, `methodology\Design_Template_Initiative\`; exempt by name `WORKSPACE_STATE.md`, `REPOSITORY_MAP.md`, `methodology\VALIDATION_METHODOLOGY.md`, `docs\local_development.md`, `implementation\Server_VM_Setup\ServerSetUp_MVP.md` (GUIDE → product, Q6), `System_V1_Implementation\{SKILLS,SUITE_HANDOFFS,V1_IMPLEMENTATION_SEQUENCE}.md`, the four `prompts\reference\*_V3.md`; generated `docs\proposals\Repo_Restructure_MVP_V1_Split\manifests\REVIEW_LIST.md`; held — live-package group: `System_V1_Implementation\proposal\00`, `01`, `02` and `MVP_Reconciliation\02`, `04`, `05`; terminal-`STATE.md` group: `prompts\PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md`; pinned group: `System_Design_Architecture\proposal\00`, `01`, `02`, `03`; code group: `System_Design_Architecture\proposal\04_APPROVED_DESIGN_REVISION_2026-07-10.md`, `System_Design_Architecture\MODEL_RECOMMENDATION.md`, `docs\proposals\PlantLibrary_Full_Implementation_Update.md`, `prompts\reference\SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md`; scratch deferred |

```text
Step A-n of C:\Programmierung\SW_Development\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md for <SUITE>.
cwd C:\Programmierung\SW_Development\<SUITE> on main, tree clean; A-1 is done and the superproject is clean. Anchor this
submodule to the kit at v0.1.0. Nothing is renamed or moved in this step; no other submodule is touched.

Read first: the runbook's section 12 row for <SUITE> (roots, wrapper, decision seeds), section 1b (the hold groups) and
section 1d; KIT\installer\INSTALL.md; KIT\KIT_SPEC.md sections 2, 3, 6; repo-hygiene\REGISTER_target-corpus-census_
2026-09-15.md section 2.<n> for this suite, section 3 (its holds) and section 4 (its row: pytest surface, line endings,
existing CLAUDE.md/AGENTS.md); this suite's CLAUDE.md and AGENTS.md if they exist (PyApp: CRLF, rich; Server: LF,
runtime-only; the other four: absent).

Do: run the installer per INSTALL.md with this suite's roots; the pytest wrapper per the row; modules off (root allowlist
off, scratch deferred); no pre-commit hook. Then complete what it seeds: an INDEX.md in every declared root that has none
(proposal\ gets one line for its existing file, marked held with its group; planning\ and handovers\ are created with an
empty index so new deliverables have a home); hygiene\HYGIENE_DECISIONS.md entry D-<today>-01 with, quoting the G0 words:
the roots and routing, the frozen trees, the pinned trees, the exempt names, the generated trees, the held names each with
its hold group, its citing file class and its target-on-release (TYPE and topic from census section 2, date from the
git-created column), the scratch module deferred to onboarding step 3, and for Workspace the sentence that the loose roots
are declared at M-7; the rule block present in CLAUDE.md and AGENTS.md (both created by the installer where absent, with the
block only). Commit here; then in the superproject add the gitlink and commit with the ledger flip.

Constraints: edits preserve each file's line endings; no .gitattributes; no .gitignore change; nothing under implementation\
MVP\, Archive_PreMVP\, references\, generated\, the frozen Workspace trees or the pinned methodology trees is touched; no
batch package file (BATCH_PLAN.md, TASK_CHECKLIST.md, TASK_CONTEXT.md, STATE.md) is edited; the existing CLAUDE.md content
(PyApp, Server) is untouched apart from the inserted block; nothing pushed.

Done when: INSTALL.md's Verify section reports its pass-with-holds verdict for this submodule with exactly the row's held
names that sit inside a declared root listed as held and zero violations; the pin and the -01 decision entry exist; every
declared root has an INDEX.md that names every file in it; one commit on the submodule's main and one superproject commit
carrying the gitlink and the ledger flip.

Commit line (submodule): hygiene: A-n - <SUITE> anchored to kit 0.1.0
Commit line (superproject): repo-hygiene: A-n - bump <SUITE> gitlink; ledger A-n
```

**Watch:** the decision record is the whole value of this step — `M-0` maps against it, and `GA` confirms it. A record that
says "see the census" instead of listing names is incomplete; the names must be there, hold group included. Held names
outside a declared root (the `docs\` and `Documentation\` ones, Workspace's loose folders) are in the record but not in the
verdict yet — the checker only sees declared roots. For `A-7`, the Workspace record will be long; that is correct. If the
installer wants to write `.gitignore` for `.tmp\`, that is the scratch module and it is off here. PyApp's `CLAUDE.md` is
CRLF: the inserted block must be CRLF too, and `AGENTS.md` (also CRLF) gets the same bytes; the parity check normalises, so a
mismatch reported here is a real text difference. After `A-7`, answer `GA` in §4 and record it in the `M-0` commit.

## 13. Step `M-0` — the rename map, presented at `GM`

**Fable 5.1 · high.** A map derived from known facts, with six judgment calls the operator decides. Depends on G0 Q4/Q4b,
Q5/Q5a/Q5b/Q5c, Q6, and `GA`. `cwd`: TARGET.

```text
Step M-0 of repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md. cwd C:\Programmierung\SW_Development on main,
tree clean, GA answered (stop if not). Produce the rename map for all seven repositories and present it at gate GM. Nothing
is renamed or moved in this step; no git mv.

Read first: the runbook's sections 1b, 1d and 4; repo-hygiene\REGISTER_target-corpus-census_2026-09-15.md sections 2, 3, 6
and 7; each repo's hygiene\HYGIENE_DECISIONS.md entry -01 (the confirmed sets); KIT\KIT_SPEC.md sections 1-3; KIT\runbooks\
RUNBOOK_migrate-an-existing-repository.md (the procedure; this step is its census + map stage).

First re-measure: run the checker's census mode in every repo (per INSTALL.md) and diff its per-root counts against the
register's section 1; a file created, deleted or moved since 2026-09-15 is listed in the map's preamble with its git date,
and every new file is dispositioned like the rest. Then derive the map, one section per repo, one row per candidate of
census section 2: old name -> new name (TYPE from the census proposal as adjusted by Q6: DECISION-shaped -> PROPOSAL with
its status in the index line, REPORT-shaped -> EVIDENCE, GUIDE-shaped -> exempt product doc; topic from the census; date =
git-created, with the header date and the divergence noted where they differ, per Q5a), or held with its group, the citing
file and class, and the target-on-release, or exempt by decision with the entry cited, or set folder with the folder's new
name and the member names unchanged (Q5b). Include the moves (Q4): the superproject's root HANDOVER into handovers\; the
nine docs\ candidates of Server, Dashboard and AndroidApp into their package's planning\ with the row id kept in the topic
(where held, the move waits with the rename). Then the six proposals GM decides, each with a recommendation: (1)
IMPLEMENTATION_PLAN.md at the superproject root - recommend exempt by decision as the living program plan, entered in the
root allowlist, since the onboarding runbook cites it eight times and it is a "how to continue" document; (2) the three
PyApp GUI\ candidates (FUTURE_GUI_DEVELOPMENT_PROPOSAL.md, source_derived\Source_GUI_Integration_Report.md,
screen_structures\improvements.md) - recommend the docs\ treatment: git mv into planning\, the last one held (pinned group);
(3) the two numbered sets inside live proposal\ roots (Workspace SDA 00-04, V1 00-02) - recommend, on release, a dated set
subfolder inside proposal\ so the root keeps its name; (4) MVP_Reconciliation\ - recommend, on release, docs\
SNAPSHOT_mvp-reconciliation_2026-07-10\ as a set folder; (5) Workspace's loose roots - recommend that M-7 declares docs\,
docs\proposals\, prompts\ and implementation\Server_VM_Setup\ as roots by a decision entry before its first git mv, with
docs\fable5_* and docs\proposals\Repo_Restructure_MVP_V1_Split\ as dated set folders; (6) the terminal-STATE.md hold group of
section 1b (five names) - recommend that a citation from a frozen package's STATE.md is served by the mapping table, as
Chapter 8's own rule served STATE.md citations, which releases those five for M-3, M-5 and M-7; the live-package group
stays held per Q5c. Write the map as repo-hygiene\MATRIX_rename-map_<today>.md with a preamble (re-measurement diff), the
seven sections, a holds summary per repo by group, a date-divergence table, and the six proposals with their
recommendation. Present the map in full and wait for the operator's explicit answer; record it verbatim in the runbook's
section 4 (GM) and in the map's preamble. Do not auto-resolve a gate question. Record the GA answer in section 4 as well.
Add the map's line to repo-hygiene\INDEX.md. Commit.

Constraints: no git mv, no edit outside repo-hygiene\ and the runbook; the re-measurement writes nothing (census mode is
read-only); the frozen, pinned and exempt names of every decision record appear in the map only as "never renamed" rows,
with the record entry cited; no name that any live package anchor, STATE.md, the onboarding runbook, a pinned tree, the
Design kit or a code file cites is mapped as a plain rename - it is held with its group and target, unless proposal 6 is
accepted for the terminal-STATE.md group.

Done when: every candidate of the census (plus every file the re-measurement found) is dispositioned exactly once - renamed,
moved, held, exempt-by-decision, set-folder - and the counts per repo reconcile with the register's section 1 plus the diff;
the GM and GA answers are recorded verbatim; the map is indexed; one commit on main.

Commit line: repo-hygiene: M-0 - rename map for seven repositories; GA and GM recorded
```

**Watch:** the two things a reviewer would otherwise miss are here by construction — the pinned methodology trees are
"never renamed" rows, and every live citation is a hold — check that the map says so for `GUI_Improvement_Methodology`,
`Design_Template_Initiative` and for all 34 census holds (fewer only if a citer has already changed, with the commit named).
The session must stop at the gate; a map "confirmed" without your words in §4 is not confirmed.

## 14. Step `M-1` — migrate the superproject

**Opus 5 · high.** The Chapter-8 procedure on the smallest repo. Depends on G0 Q4, Q5, Q7, Q11, and `GM`. `cwd`: TARGET.

```text
Step M-1 of repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md. cwd C:\Programmierung\SW_Development on main,
tree clean, GM answered (stop if not). Execute the superproject's section of repo-hygiene\MATRIX_rename-map_<date>.md.

Read first: the map's preamble and superproject section; KIT\runbooks\RUNBOOK_migrate-an-existing-repository.md (the
execute stage: git mv, sweep, INDEX regeneration, verify); hygiene\HYGIENE_DECISIONS.md; repo-hygiene\
REGISTER_target-corpus-census_2026-09-15.md section 3 (the superproject's four hold rows).

Do, in the map's order: git mv the root HANDOVER into handovers\ (a move, name unchanged); apply every confirmed rename by
git mv; the reference sweep over the editable list - repo-hygiene\**, handovers\**, the relative link in onboarding\INDEX.md
that points at the moved HANDOVER (a path fix, one line), CLAUDE.md/AGENTS.md if they cite a renamed name - and never the
onboarding runbook, the onboarding register or audit, any submodule; regenerate repo-hygiene\INDEX.md and handovers\INDEX.md
with a "Renamed <date>" old -> new table that carries every held row with its group and target-on-release and every
exempt-by-decision row with its entry; add a decision entry D-<today>-nn recording what was renamed, moved, held and
exempted, with the GM words quoted; verify per INSTALL.md; commit with the ledger flip.

Constraints: git mv only, never delete-and-add; no case-only churn; edits preserve line endings; IMPLEMENTATION_PLAN.md is
handled exactly as GM decided for proposal 1; nothing under any submodule or gitlink changes; a git grep for each old name
after the sweep must hit only the mapping table, the decision record, the census register, this runbook, the map and the
onboarding track's own files.

Done when: INSTALL.md's Verify section reports its verdict with the held names listed as held and zero violations; the
old-name grep residue is accounted for by category in the commit message body; one commit on main.

Commit line: repo-hygiene: M-1 - superproject migrated per the confirmed map; INDEX mapping tables
```

**Watch:** this is the one M step that edits a file of the onboarding track (`onboarding\INDEX.md`, one relative link; the
onboarding runbook cites the HANDOVER by basename only, so the move breaks nothing there). If the session proposes touching
the onboarding runbook instead, that is the hold rule being broken — send it back.

## 15. Steps `M-2` … `M-7` — migrate one submodule each

**Opus 5 · high, one session per submodule**, suite order as in §12. Depends on G0 Q4b, Q5/Q5a/Q5b/Q5c, Q6, Q7, Q11, and
`GM`. `cwd`: the submodule folder, then TARGET. Before pasting, replace `M-n` with the step id and `<SUITE>` with the folder
name.

```text
Step M-n of C:\Programmierung\SW_Development\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md for <SUITE>.
cwd C:\Programmierung\SW_Development\<SUITE> on main, tree clean; GM answered (stop if not); the superproject clean.
Execute this submodule's section of ..\repo-hygiene\MATRIX_rename-map_<date>.md.

Read first: the map's preamble, this suite's section and the GM decisions on proposals 2-6; KIT\runbooks\
RUNBOOK_migrate-an-existing-repository.md (the execute stage); this repo's hygiene\HYGIENE_DECISIONS.md; ..\repo-hygiene\
REGISTER_target-corpus-census_2026-09-15.md sections 2.<n> and 3 for this suite; the runbook's section 1b (the hold groups).

Do, in the map's order: for Workspace first, the decision entry that declares the loose roots the map adds (proposal 5) and
seeds their INDEX.md files; every confirmed move by git mv (the docs\ candidates into planning\ where the map says so; a set
folder renamed as a folder, its members untouched); every confirmed rename by git mv; a held name is released in this step
only when git grep at HEAD across the whole superproject (every submodule included) shows no remaining hold-class citer of
its old name, or GM's answer to proposal 6 covers it - the grep result or the proposal is quoted in the decision entry; every
other held name stays held for M-9; the reference sweep over the editable list - the declared roots' files, README.md files,
product documentation under docs\, Documentation\, GUI\ and similar, hygiene\, CLAUDE.md/AGENTS.md, this repo's own
candidates - and never BATCH_PLAN.md, TASK_CHECKLIST.md, TASK_CONTEXT.md, STATE.md of any package, any frozen or pinned
tree, any generated tree, any code or config file, anything outside this repo; regenerate every declared root's INDEX.md,
the roots that received files gaining their lines and a "Renamed <date>" old -> new table carrying held rows with group
and target-on-release and exempt-by-decision rows with their entry; a decision entry D-<today>-nn recording the renames,
moves, holds kept, holds released (with the grep result or proposal that released each) and exemptions; verify per
INSTALL.md; commit here; then in the superproject add the gitlink and commit with the ledger flip.

Constraints: git mv only; no case-only churn; edits preserve line endings; a citation from a never-edit file is served by
the mapping table, never by an edit; a code citation (a test docstring, a route comment) is a hold, not a sweep target;
nothing pushed; a git grep for each old name after the sweep must hit only the mapping tables, the decision record, the
register, the map, never-edit files, frozen trees and the onboarding track's files.

Done when: INSTALL.md's Verify section reports its verdict for this submodule with exactly the remaining held names listed
as held and zero violations; every declared root's INDEX.md names every file in it; the residue is accounted for by
category in the commit message body; one commit on the submodule's main and one superproject commit with the gitlink and
the ledger flip.

Commit line (submodule): hygiene: M-n - <SUITE> migrated per the confirmed map; INDEX mapping tables
Commit line (superproject): repo-hygiene: M-n - bump <SUITE> gitlink; ledger M-n
```

**Watch:** PyApp's `Documentation\` is exempt by decision — if the session renames anything in it, `GM`'s map was not read.
Workspace's four dated set folders (three `fable5_*`, `Repo_Restructure_MVP_V1_Split`) are folder renames: the chapter files
keep their names, and a session that starts renaming `00_EXECUTIVE_SUMMARY.md` has misread Q5b. A hold released because the
grep came back empty must quote that grep; "it looked migrated" is not a release.

## 16. Step `M-8` — the closing pass

**Sonnet 5 · thinking.** Verification and record. Depends on G0 Q7, Q10. `cwd`: TARGET, then KIT.

```text
Step M-8 of repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md. cwd C:\Programmierung\SW_Development on main,
tree clean, M-1 to M-7 done and every gitlink bumped. Close the pilot.

Read first: the runbook's sections 1b, 3 and L; repo-hygiene\REGISTER_target-corpus-census_2026-09-15.md sections 1 and 7
(the baseline and its rules); repo-hygiene\MATRIX_rename-map_<date>.md; every repo's hygiene\HYGIENE_DECISIONS.md; KIT\
templates\HANDOVER_CONTINUATION_TEMPLATE.md and AUDIT_migration-record_TEMPLATE.md; KIT\KIT_VERSION.md.

Do: (1) verify per INSTALL.md in all seven repositories and quote each verdict line; (2) run the checker's census mode in
all seven and write repo-hygiene\REGISTER_target-corpus-census_<today>.md in the register's shape with a diff section
against the 2026-09-15 register's section 1 - per repo: files, candidates, renamed, moved, held (with the group each hold
remains in), exempt-by-decision, set folders; every difference explained by a map row, a decision entry or a file the
re-measurement found; (3) write the migration record repo-hygiene\AUDIT_migration-record_<today>.md from the kit's
template: the disposition table per repo (renamed, moved, held, exempt, set-folder, already-compliant, frozen, pinned,
generated), the sweep residue by category, the enforcement installed per repo, deviations; (4) write the handover for
whoever continues into handovers\HANDOVER_repo-hygiene-pilot-closeout_<today>.md from the continuation template: the state
of every repo, the remaining holds by group and what releases each (M-9), what the pilot taught the kit, the next action;
index it in handovers\INDEX.md and add a pointer line in repo-hygiene\INDEX.md; (5) in KIT: add to KIT_VERSION.md a
changelog entry for what the pilot taught - every rule the seven decision records needed that the spec did not foresee,
every installer behaviour that had to be worked around, with a version bump per the semver rule (patch for wording, minor
for an additive rule) - commit in KIT, tag if the version moved; (6) if the kit version moved, do not re-pin the seven repos
here - record the re-pin as owed in the handover; (7) commit in TARGET with the ledger flip.

Constraints: nothing renamed or moved in this step; no decision record edited except to append a closing entry; the kit's
changelog entry names what changed and why, never patches the checker silently - a checker change is a K-style step
recorded in the derive runbook, not part of M-8.

Done when: seven verdict lines quoted; the new register's diff section reconciles every number against the baseline; the
migration record and the handover exist and are indexed; the kit's changelog entry exists; one commit on TARGET main and,
if the kit changed, one commit on KIT main.

Commit line (TARGET): repo-hygiene: M-8 - closing pass: seven repos verified, census diffed, migration record, handover
Commit line (KIT, if any): kit: pilot lessons from SW_Development; version <x.y.z>
```

**Watch:** the diff is the deliverable; a register that repeats the numbers without explaining each difference is not a
diff. The handover goes to `handovers\` per the rule the kit installed (§0); if the session puts it in `repo-hygiene\`, the
checker will tell it. Expect the remaining holds to be the live-package group (unless onboarding released some), the pinned
group and the code group of §1b, and the terminal-`STATE.md` group only if `GM` rejected proposal 6.

## 17. Step `M-9` — rolling: release held names

**Opus 5 · high, one session per release batch.** Depends on G0 Q5c, Q7, `GM`, and on the onboarding track's `2a`/`2b`
commits or an explicit operator release recorded in the repo's decision record. `cwd`: the repo that holds the name, then
TARGET. Before pasting, replace `<REPO>` with the folder name.

```text
Step M-9 of C:\Programmierung\SW_Development\repo-hygiene\PROMPTS_repo-hygiene-track-runbook_2026-09-15.md, release batch
for <REPO>. cwd C:\Programmierung\SW_Development\<REPO> on main, tree clean; M-8 done; GM answered - the confirmed map's
target-on-release column is the only target. Release the held names whose citer has changed.

Read first: this repo's hygiene\HYGIENE_DECISIONS.md (the held names, their group and their citers); the "Renamed" mapping
table of each declared root's INDEX.md (target-on-release per held name); the runbook's section 1b (what releases each
group); the onboarding runbook's ledger and the commit that migrated this package's STATE.md and anchors, or the operator's
release words; the map ..\repo-hygiene\MATRIX_rename-map_<date>.md for the set-subfolder targets of the live proposal\ sets.

Do: for each held name whose hold-class citer no longer cites the old name (verified by git grep at HEAD across the whole
superproject, every submodule included, quoting the result) or whose release the operator has recorded: git mv to the
target-on-release (a live proposal\ set becomes its dated subfolder); the sweep over the editable list as in M-n; flip the
INDEX.md mapping row from held to renamed; a decision entry D-<today>-nn naming the releasing commit or the operator's
words; verify per INSTALL.md; commit; gitlink bump with the ledger line "M-9: <REPO> <names> released <date>" appended in
section L.

Constraints: a name whose citer still cites it stays held - no edit to STATE.md, an anchor, the onboarding runbook, a
pinned tree, the Design kit or a code file to force a release; git mv only; line endings preserved; nothing pushed.

Done when: INSTALL.md's Verify section reports its verdict with the remaining held names listed as held; the released
names have index lines and mapping rows; one submodule commit and one superproject commit.

Commit line (repo): hygiene: M-9 - released <names>
Commit line (superproject): repo-hygiene: M-9 - bump <REPO> gitlink; ledger
```

**Watch:** the eleven live-package holds are released by the onboarding track's package migration, not by this track editing
a package file; the pinned and code groups are released by other owners, or never. If a session argues the `STATE.md` line is
"just a citation", that is the never-edit list being tested.

## 18. Model · reasoning ladder for this track

| Shape | Model · reasoning |
|---|---|
| Open-ended design and gates (the bootstrap, `K-1`) | Fable 5.1 · xhigh |
| Building against a written specification, and rename maps (`K-2a`, `K-2b`, `K-2c`, `M-0`) | Fable 5.1 · high |
| Structured execution of an existing procedure (`A-1`…`A-7`, `M-1`…`M-7`, `M-9`) | Opus 5 · high |
| Mechanical verification and closing passes (`K-3`, `K-4`, `M-8`) | Sonnet 5 · thinking |

**Substitution when Fable 5.1 is unavailable** (the `D-2026-09-12-05` rule of the Meta V2 track): a Fable · high slot becomes
Opus 5 · high plus a mandatory fresh-context review of the draft before it is written (`K-1`, `K-2a`, `K-2b`, `K-2c`: a
general-purpose reviewer against the step's done-when; `M-0`: the reviewer checks every hold and every never-renamed set is
present), never `xhigh` on Opus and never Sonnet for a Fable slot. The compensating control is review, not effort.

## L. Track ledger — flip as you go

| Step | What | Model · reasoning | Status |
|---|---|---|---|
| `G0` | the gate | operator | done 2026-09-15 — "all recommendations accepted" |
| `K-1` | KIT created; `KIT_SPEC.md` | Fable 5.1 · xhigh | done 2026-09-16 — KIT `7475e13` on `main`: `KIT_SPEC.md` (sections 0–14 plus the section-15 mapping: inventory rows 1a–11b and G0 Q1–Q11 with Q3a, Q4b, Q5a–c, none unmapped), two-paragraph `README.md`, `.gitignore`; no tooling built; SOURCE untouched |
| `K-2a` | checker, wrapper, rule block, negative fixtures | Fable 5.1 · high | done 2026-09-16 — KIT `f414e6f` on `main`: `checker\repo_hygiene_check.py` (check / census / `--self-test`, stdlib only, configuration from the two `hygiene\` files), `checker\test_repo_hygiene_kit.py`, `rule-block\HYGIENE_RULES_BLOCK.md`, eight fixtures under `tests\` each with an `expected.txt` and `tests\run_fixtures.py` (8/8 fixtures, 2/2 self-tests), `checker\VERIFICATION_NOTES.md`; a read-only smoke over SOURCE showed the two holds and the skip plus three `index` coverage lines (the kit's addition, a `K-3`/`K-4` finding per spec §14); SOURCE untouched |
| `K-2b` | installer, templates, example, `CONTRIBUTING.md` §1 | Fable 5.1 · high | done 2026-09-16 — KIT `47a6628` on `main`: `installer\install.py` (eight writes in spec order; `pin unchanged` / kit-upgrade notice with exit 0; exit 3 on a declaration conflict without `--force`, nothing written; line endings preserved per file; `AGENTS.md` created when absent) and `installer\INSTALL.md` with its Verify section; eight templates under `templates\` (index, pin, decision record, runbook, handover continuation, migration record, `workflows\repo-hygiene.yml`, `hooks\pre-commit`); `examples\anchored-target` (the installer run on it, seeds completed by hand, committed as files); `tests\run_installer.py` (8/8 cases); `CONTRIBUTING.md` §1 with the verification order and the "what green means" table (every row green at that commit), §2 invariants; `checker\VERIFICATION_NOTES.md` folded in and deleted; SOURCE untouched |
| `K-2c` | README, SOURCE pin, three generic runbooks, `KIT_VERSION.md` | Fable 5.1 · high | done 2026-09-16 — KIT `f07c111` on `main`: `README.md` (contains / never contains table, folder map, prerequisites, verification by pointer to `INSTALL.md` and `CONTRIBUTING.md`), `SOURCE_HARNESS.md` (the pin: Orchestrator harness, `main`, `fc5a14c`, pinned 2026-09-15; inventory rows 1a–11b mapped to kit files, 9b/9c out; the upgrade rule), `runbooks\RUNBOOK_derive-the-kit.md` (`D-1`…`D-9`, `GD`, `GK`, with the re-derivation delta form), `runbooks\RUNBOOK_anchor-a-repository.md` (`A-0`…`A-<N>`, `GA`), `runbooks\RUNBOOK_migrate-an-existing-repository.md` (`M-0`, `GM`, `M-1`…`M-<N>`, `M-C`, `M-R`) — each with a placeholder table that matches every placeholder used; `KIT_VERSION.md` (current version `0.1.0` as the installer stamps it, the semver rule, the empty `0.1.0` entry for `K-3`/`K-4`); grep for PlantLibrary / SW_Development / Conductor across `runbooks\` empty; `CONTRIBUTING.md` §1 green on every row (installer now reads version and SOURCE commit from the documents, no `notice:` lines); LF throughout; SOURCE untouched |
| `K-3` | self-test against the SOURCE baseline; negative tree | Sonnet 5 · thinking | done 2026-09-16 — KIT `5eecfaa` on `main`: `KIT_VERSION.md`'s `0.1.0` entry completed with the self-test record — `check`/`census` over SOURCE (HEAD `55bcc21`, working tree dirty with unrelated instance work) under a throwaway `.tmp/k3/` configuration expressing spec §14 verbatim: `repo-hygiene: fail — 3 violations, 2 held, 1 skipped` (exactly the two held names held, the skip reported, zero `name`/`proof-argv`/`proof-prose`/`proof-floor` lines over 42 `PROMPT_*`/`PROMPTS_*` files; the 3 violations are the kit's own `INDEX.md`-coverage addition, §14's own named exception, carried to Findings, not patched); census totals 229 files, 222 compliant, 5 exempt, 2 held, 0 set folders; `git -C SOURCE status` identical before/after both runs; `CONTRIBUTING.md` §1's full verification order reproduced every row's exact line; a fresh negative tree failed naming all six planted defects (`name`, `proof-argv`, `proof-prose`, `block-parity`, `index` ×2) and its line-endings-only companion passed; both scratch trees deleted, `.tmp/k3/` gone; one Finding recorded for `K-4` (the three `index` lines), nothing else; SOURCE untouched |
| `K-4` | 0.1.0, changelog, tag `v0.1.0` | Sonnet 5 · thinking | done 2026-09-16 — KIT `1360c0c` on `main`, tag `v0.1.0` on that commit: the one `K-3` finding decided (not a defect — `KIT_SPEC.md` §14's reproduction-target paragraph amended to state the expected three `index` lines and the literal `repo-hygiene: fail — 3 violations, 2 held, 1 skipped` verdict, so a re-run compares against the true baseline); `KIT_VERSION.md`'s `0.1.0` changelog entry completed (what the kit contains, the SOURCE pin, the self-test summary, the decided finding, nothing deferred); `README.md` and the rule block's `{{KIT_VERSION}}` default already agreed (`0.1.0`), no edit needed; `CONTRIBUTING.md` §1's full verification order re-run and green on every row at the tagged commit; no checker or installer behaviour changed; nothing pushed |
| `GK` | kit accepted for anchoring | operator | done 2026-09-16 — "Yes, accept (Recommended)" (§4) |
| `A-1` | superproject anchored | Opus 5 · high | done 2026-09-16 — superproject `master` (this commit): installer run with roots `repo-hygiene`, `onboarding`, `handovers`, module `root-allowlist`, no wrapper, no hook — `install: done — pin written`; `hygiene\CONSUMED_HYGIENE.md` pins kit `0.1.0` @ `C:/Programmierung/Repo_Hygiene_Template_Kit`, SOURCE `fc5a14c`; `handovers\INDEX.md` seeded empty; `hygiene\HYGIENE_DECISIONS.md` entry `D-2026-09-16-01` (G0 and GK words, roots and routing, the four onboarding-runbook holds with citing lines and targets, `IMPLEMENTATION_PLAN.md` → `M-0` proposal 1, 24 allowlist entries = today's root listing plus `.github`/`handovers`/`hygiene`, no retired names, scratch deferred to onboarding step `3`); rule block appended to `CLAUDE.md`/`AGENTS.md` in CRLF (each file's first-line ending), prior bytes unchanged, both still mixed; checker verdict `repo-hygiene: pass with holds — 0 violations, 2 held`, `--self-test` `pass — 6 defects detected, original unchanged`; census 10 files, 5 compliant, 0 candidates, 3 exempt, 2 held. **Finding for `GA`/`M-0`:** the checker lists a held name only inside a declared root, so the two root-level holds (`HANDOVER_…`, `IMPLEMENTATION_PLAN.md`) are in the record but not in the verdict — 2 held, not the 4 the done-when expected; kit unchanged |
| `A-2` | PyApp anchored | Opus 5 · high | todo |
| `A-3` | Server anchored | Opus 5 · high | todo |
| `A-4` | SharedContracts anchored | Opus 5 · high | todo |
| `A-5` | Dashboard anchored | Opus 5 · high | todo |
| `A-6` | AndroidApp anchored | Opus 5 · high | todo |
| `A-7` | Workspace anchored (six package roots) | Opus 5 · high | todo |
| `GA` | decision records confirmed | operator | open |
| `M-0` | rename map, six proposals | Fable 5.1 · high | todo |
| `GM` | map confirmed | operator | open |
| `M-1` | superproject migrated | Opus 5 · high | todo |
| `M-2` | PyApp migrated | Opus 5 · high | todo |
| `M-3` | Server migrated | Opus 5 · high | todo |
| `M-4` | SharedContracts migrated | Opus 5 · high | todo |
| `M-5` | Dashboard migrated | Opus 5 · high | todo |
| `M-6` | AndroidApp migrated | Opus 5 · high | todo |
| `M-7` | Workspace migrated (loose roots declared first) | Opus 5 · high | todo |
| `M-8` | closing pass: seven verdicts, census diff, migration record, handover, kit changelog | Sonnet 5 · thinking | todo |
| `M-9` | rolling: held names released | Opus 5 · high | rolling — `<REPO> <names> released <date>` appended here |
