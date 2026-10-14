---
name: code-quality-review
description: Review Python code in the PlantLibrary suites (PlantLibrary_PyApp, PlantLibrary_Server, PlantLibrary_SharedContracts) for anti-patterns and AI-generated debt - swallowed exceptions, blocking calls in async code, mock-heavy tests, invented imports. Operator session only - use when the operator asks for a code-quality review; no batch row names this skill. Read-only; it reports findings, it never fixes them; writes to reviews/ by default.
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
PlantLibrary superproject) with its line in `<root>/INDEX.md` in the same
commit, where `<root>` is `reviews/` unless the operator names another of
the `general` roots of `hygiene/CONSUMED_HYGIENE.md` (the default since
master rework B3-6.1, 2026-10-14, Q-B3-11 (a)).
Scratch notes stay in the session's scratchpad directory, never in the
repository tree. No network; no token or credential is read or configured.
