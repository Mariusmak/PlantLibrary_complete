---
name: pathfinder
description: Map the PlantLibrary codebase (the superproject and its six suites) into feature-grouped flowcharts with file:line evidence and report duplicated concerns. Operator session only - use when the operator asks for an architecture or duplication map; no batch row names this skill. Read-only; it proposes, plan-batch plans; writes to reviews/ by default.
---
<!-- Adapted from thedotmack/claude-mem @ 039c616, plugin/skills/pathfinder/SKILL.md (Apache-2.0; see LICENSE and NOTICE). Modified 2026-10-04 by the Conductor (Orchestrator_System, OP-SK-A, D-2026-10-04-11) and 2026-10-13 for PlantLibrary (master rework B1-3, Q-A1-02 (a)); local edit 2026-10-14: default root reviews/ (B3-6.1, Q-B3-11 (a)). -->

# Pathfinder

You are an ORCHESTRATOR. Map the codebase into feature-grouped flowcharts, identify duplicated concerns, propose the simplest unified architecture, and hand the findings to `plan-batch`.

You do not write implementation code. You produce diagrams, a duplication report, a proposed unified flowchart, and candidate rows for `plan-batch`. Read only; never edit a file outside the session's scratchpad directory and the one audit file with its `INDEX.md` line. No network; no token or credential is read or configured.

## Delegation Model

If this invocation can spawn agents, delegate discovery as below; otherwise run each phase inline in the same order, keeping the same reporting contract.

Use subagents for *discovery and extraction* (file reading, flow tracing, grep, diagramming). Keep *synthesis* (deciding feature boundaries, picking unification strategies, final flowchart) with the orchestrator. Reject subagent reports that lack source citations and redeploy.

### Subagent Reporting Contract (MANDATORY)

Each subagent response must include:
1. Sources consulted — exact file paths and line ranges read
2. Concrete findings — exact function names, call sites, data flow
3. Mermaid diagram(s) with nodes labeled by `file:line`
4. Confidence note + known gaps

## Output Artifacts

Working files go in `pathfinder/<YYYY-MM-DD>/` under the session's scratchpad directory (else the OS temp directory), never in the repository tree:
- `00-features.md` — feature inventory with boundaries
- `01-flowcharts/<feature>.md` — one Mermaid flowchart per feature
- `02-duplication-report.md` — cross-cutting duplicated concerns with evidence
- `03-unified-proposal.md` — proposed unified architecture + Mermaid
- `04-findings-for-plan-batch.md` — one candidate row per unified system

The one deliverable, assembled from those files, is
`<root>/AUDIT_pathfinder-<topic>_<YYYY-MM-DD>.md` in this repository (the
PlantLibrary superproject) with its line in `<root>/INDEX.md` in the same
commit, where `<root>` is `reviews/` unless the operator names another of
the `general` roots of `hygiene/CONSUMED_HYGIENE.md` (the default since
master rework B3-6.1, 2026-10-14, Q-B3-11 (a)).

## Phases

### Phase 0: Feature Discovery (ALWAYS FIRST)

Deploy ONE "Feature Discovery" subagent to:
1. Walk the source tree (not built artifacts) of the superproject and the suites in scope, and read each one's top-level README / CLAUDE.md. Never read `.codex/**` or `.agents/**` (frozen runtime copies), `graphify-out/**`, `PlantLibrary_Workspace/archive/**` (history), `PlantLibrary_SharedContracts/generated/**` (generated clients; read the OpenAPI source under `PlantLibrary_SharedContracts/openapi/` instead) or build and dependency output (`node_modules/`, `build/`, `.gradle/`, `dist/`, `__pycache__/`).
2. Propose feature boundaries based on directory structure, import graph, and naming
3. Return a flat list of features with: name, entry points (file:line), core files, brief purpose

Orchestrator reviews the proposal, adjusts boundaries if needed, writes `00-features.md`. Do NOT fan out until feature boundaries are approved.

### Phase 1: Per-Feature Flowcharts (FAN OUT)

Deploy ONE "Flowchart" subagent per feature in parallel. Each receives only its feature's scope. Each must:
1. Trace the feature's primary happy path from entry point to terminal state
2. Identify side effects (DB writes, HTTP calls, file I/O, process spawns)
3. Note error and fallback branches but do not let them dominate the diagram
4. Produce a Mermaid `flowchart TD` with every node labeled `Name<br/>file:line`
5. List external dependencies (other features it calls into) at the bottom

Orchestrator writes each flowchart to `01-flowcharts/<feature>.md`. Reject any diagram missing `file:line` labels.

### Phase 2: Duplication Hunt

Deploy TWO subagents in parallel:

**"Within-Feature Duplication"** subagent:
- For each feature, find repeated code/logic patterns inside the feature only
- Report only duplications worth consolidating (ignore trivial repetition)

**"Cross-Feature Duplication"** subagent:
- Compare flowcharts across features for concerns that appear in multiple places
- Examples of what to look for: multiple capture paths, parallel queue implementations, duplicated storage/migration code, repeated agent scaffolding, parallel parsing layers
- For each duplication, report: (a) the concern, (b) every location with `file:line`, (c) why they diverged, (d) whether the divergence is legitimate specialization or accidental

Orchestrator synthesizes both into `02-duplication-report.md`. Every duplication claim must cite ≥2 `file:line` locations.

### Phase 3: Unified Proposal (ORCHESTRATOR)

The orchestrator writes `03-unified-proposal.md` itself — do not delegate synthesis.

For each duplicated concern from Phase 2 that is NOT legitimate specialization:
1. Propose the simplest unified design (one path, one store, one handler — whatever applies)
2. Name the consolidated component and its single entry point
3. Show what each old call site becomes
4. Call out any loss of capability and whether it's acceptable

End the document with ONE combined Mermaid flowchart showing the proposed unified system. Nodes still labeled with target `file:line` (new or existing) where knowable.

**Anti-patterns to reject in your own proposal:**
- Adding a new abstraction layer "for flexibility"
- Keeping both old paths behind a feature flag
- Introducing a registry/factory when a switch statement suffices
- Preserving divergent behavior "just in case"

Never propose unifying a boundary PlantLibrary keeps on purpose (the three clients PlantLibrary_PyApp, PlantLibrary_AndroidApp and PlantLibrary_Dashboard each consuming the SharedContracts API; PlantLibrary_PyApp's per-source adapters for its external botanical APIs; a suite's `CLAUDE.md` layer rules) or deleting a normative record (a recorded decision, a contract); those are legitimate specialization.

### Phase 4: Findings for `plan-batch`

For each unified system in the proposal, write one candidate row to `04-findings-for-plan-batch.md`. Each must:
1. State the target unified component and its single entry point
2. List the exact call sites to rewrite (from Phase 2 evidence)
3. Cite the relevant flowchart file from `01-flowcharts/`
4. Propose an observable done-when and the baseline it traces to (a contract, a requirement, a GAP or VGAP id, or a recorded decision)

No `/make-plan` prompt is written; `plan-batch` turns an accepted candidate into a row.

## Key Principles

- **Evidence over intuition** — every diagram node and duplication claim cites `file:line`
- **Current state before ideal state** — Phases 0–2 describe what IS; Phase 3 describes what SHOULD BE
- **Simplest unification wins** — prefer one path over configurable paths; deletion only through a row
- **Specialization is not duplication** — two components serving different trust models or data sources are legitimate even if their code looks similar
- **Handoff, don't implement** — Pathfinder ends at candidate rows; `plan-batch` takes it from there

## Failure Modes to Prevent

- Drawing flowcharts from memory instead of source — redeploy subagent with grep evidence requirement
- Proposing unification of legitimately specialized components — re-examine trust/data-source divergence
- Candidate rows that lack concrete call sites — rewrite with Phase 2 evidence
- Skipping Phase 0 boundary review — fanning out on bad feature boundaries wastes all of Phase 1
