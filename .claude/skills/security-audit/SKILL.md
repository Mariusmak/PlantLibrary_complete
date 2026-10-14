---
name: security-audit
description: Security review of a change or a module in the PlantLibrary repositories - triage a suspected finding, check an API or configuration for footguns, verify whether a finding is a true positive. Operator session only - use when the operator asks for a security review or triage; no batch row names this skill. Read-only; it reports findings, it never fixes them; writes to reviews/ by default.
---

<!-- References under references/ are adapted from Trail of Bits skills
     (github.com/trailofbits/skills @ 82fe822), CC-BY-SA-4.0; see NOTICE. -->

One mode per invocation; read only what the mode needs.

| Mode | Reference | Output |
|---|---|---|
| triage a reported finding | `references/brocards.md` (detail: `references/brocards-detail.md`) | accept / dismiss / needs-information, with the rule applied |
| footgun review of an API or config | `references/sharp-edges.md` (with `sharp-edges-lang-python.md`, `sharp-edges-config-patterns.md`, `sharp-edges-auth-patterns.md`) | findings with file:line and the misuse that triggers them |
| true-or-false-positive check | `references/fp-check.md` (with the six `fp-check-*.md`) | TRUE POSITIVE / FALSE POSITIVE with the evidence chain |

Rules: operator session only (Q-A1-02 (a)); no network; no token or
credential is read or configured; no edit anywhere except the one
deliverable,
`<root>/AUDIT_security-audit-<topic>_<YYYY-MM-DD>.md` in this repository (the
PlantLibrary superproject) - for a single triage result
`<root>/FINDING_security-audit-<topic>_<YYYY-MM-DD>.md` - with its line in
`<root>/INDEX.md` in the same commit, where `<root>` is `reviews/` unless
the operator names another of the `general` roots of
`hygiene/CONSUMED_HYGIENE.md` (the default since master rework B3-6.1,
2026-10-14, Q-B3-11 (a)).
Scratch notes stay in the session's scratchpad directory, never in the
repository tree.
A proof of concept is pseudocode or a negative PoC in the report. No batch
row invokes this skill, so no `validation` cell admits an executable or
unit-test PoC: record 4.2 and 4.3 as `not run`.
The language reference is Python only (`sharp-edges-lang-python.md`); for
Kotlin (PlantLibrary_AndroidApp) and TypeScript (PlantLibrary_Dashboard)
use `sharp-edges.md` with the config and auth patterns, and say in the
report that no language reference applied. A question you cannot
answer is recorded in the report (a headless session cannot ask). Findings go to the register or a
plan act, never straight into code.
