---
name: code-quality-review
description: Review Python code in the PlantLibrary suites (PlantLibrary_PyApp, PlantLibrary_Server, PlantLibrary_SharedContracts) for anti-patterns and AI-generated debt - swallowed exceptions, blocking calls in async code, mock-heavy tests, invented imports. Operator session only - use when the operator asks for a code-quality review; no batch row names this skill. Read-only; it reports findings, it never fixes them.
---

<!-- references/python-anti-patterns.md is adapted from wshobson/agents @ 156b7a5 (MIT; see LICENSE),
     by the Conductor (Orchestrator_System @ 2e7adb3, OP-SK-A) and for PlantLibrary at master rework
     B1-3 (2026-10-13, Q-A1-02 (a)). -->

Read `references/python-anti-patterns.md`, then the paths you were given.
The reference is Python only: Kotlin (PlantLibrary_AndroidApp) and
TypeScript (PlantLibrary_Dashboard) paths are listed as not covered, never
reviewed from memory.
Report each finding with file:line, the pattern, and why it matters here
(the suite's `CLAUDE.md` architecture rules, e.g. PlantLibrary_PyApp's
offline-first layering; `real-stack-testing`). Pre-existing code outside
the given paths is reported, never changed. No edit anywhere except the
one deliverable,
`<root>/AUDIT_code-quality-review-<topic>_<YYYY-MM-DD>.md` in this repository (the
PlantLibrary superproject) with its line in `<root>/INDEX.md`, where `<root>`
is the deliverable root the operator names from the `general` roots of
`hygiene/CONSUMED_HYGIENE.md`. No root named: no file is written and the
report is the final message.
Scratch notes stay in the session's scratchpad directory, never in the
repository tree. No network; no token or credential is read or configured.
