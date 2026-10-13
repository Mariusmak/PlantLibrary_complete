<!-- Adapted from trailofbits/skills @ 82fe822, plugins/fp-check/skills/fp-check/references/deep-verification.md (CC-BY-SA-4.0; see NOTICE). Modified 2026-10-04 by the Conductor (Orchestrator_System, OP-SK-A, D-2026-10-04-11) and 2026-10-13 for PlantLibrary (master rework B1-3, Q-A1-02 (a)). -->
# Deep Verification

Full task-based verification for complex bugs. Use when routing from fp-check.md selects the deep path, or when standard verification escalates.

## If Escalated from Standard

When a bug escalates from standard verification:

1. Review all evidence gathered during the standard pass — do not repeat completed work
2. Identify which phases below are already satisfied by existing evidence
3. Track only the remaining phases, starting from where standard left off
4. Preserve and reference all prior findings in the remaining phases' notes

## Verification Task List

For each bug (Bug #N), track one item per phase with the dependency structure below - in the session's task list when the runtime offers one, otherwise as a checklist in the report. No phase starts until every item it depends on is complete.

```
── Phase 1: Data Flow Analysis ──────────────────────────────────
"BUG #N - Phase 1.1: Map trust boundaries and trace data flow"
  Then in parallel (each blocked by 1.1):
  "BUG #N - Phase 1.2: Research API contracts and safety guarantees"
  "BUG #N - Phase 1.3: Environment protection analysis"
  "BUG #N - Phase 1.4: Cross-reference analysis"

── Phase 2: Exploitability Verification (blocked by Phase 1) ───
  In parallel:
  "BUG #N - Phase 2.1: Confirm attacker controls input data"
  "BUG #N - Phase 2.2: Mathematical bounds verification"
  "BUG #N - Phase 2.3: Race condition feasibility proof"
  Then (blocked by 2.1, 2.2, 2.3):
  "BUG #N - Phase 2.4: Adversarial analysis"

── Phase 3: Impact Assessment (blocked by Phase 2) ─────────────
  In parallel:
  "BUG #N - Phase 3.1: Demonstrate real security impact"
  "BUG #N - Phase 3.2: Primary control vs defense-in-depth"

── Phase 4: PoC Creation (blocked by Phase 3) ──────────────────
  "BUG #N - Phase 4.1: Create pseudocode PoC with data flow diagrams"
  Then in parallel (each blocked by 4.1):
  "BUG #N - Phase 4.2: Executable PoC, only under the PoC rule"
  "BUG #N - Phase 4.3: Unit test PoC, only under the PoC rule"
  "BUG #N - Phase 4.4: Negative PoC — show exploit preconditions"
  Then (blocked by 4.2, 4.3, 4.4):
  "BUG #N - Phase 4.5: Verify PoC demonstrates the vulnerability"

── Phase 5: Devil's Advocate (blocked by Phase 4) ──────────────
  "BUG #N - Phase 5.1: Devil's advocate review"

── Gate Review (blocked by Phase 5) ────────────────────────────
  "BUG #N - GATE REVIEW: Evaluate all six gates before verdict"
```

## Execution Rules

- Mark each item in progress when starting, completed only with concrete evidence
- **Independent sub-phases**: run them one after another, inline (no agent is installed). Collect all results before proceeding to the next dependency gate.
- **Dependency gates**: Never start a phase until all tasks it depends on are completed.
- Apply all 13 checklist items from [fp-check-false-positive-patterns.md](fp-check-false-positive-patterns.md) to each bug

## Phases run inline

No agent is installed. Run every phase yourself, inline, in the order of the task list above, and carry each phase's results into the next in your notes. Phases 3, 5 and the Gate Review synthesize results across phases, as before.

## Phase Requirements

The task list above names every phase. Below are the key pitfalls and decision criteria for each — focus on what you might get wrong.

### Phase 1: Data Flow Analysis

**1.1**: Map trust boundaries (internal/trusted vs external/untrusted) and trace data from source to alleged vulnerability. Apply class-specific verification from [fp-check-bug-class-verification.md](fp-check-bug-class-verification.md). **Key pitfall**: Analyzing code in isolation without tracing the full validation chain. Conditional logic upstream may make the vulnerable code mathematically unreachable (see [fp-check-false-positive-patterns.md](fp-check-false-positive-patterns.md) items 1 and 1a).

**1.2**: Check API contracts before claiming overflows — many APIs have built-in bounds protection that prevents the alleged issue regardless of inputs.

**1.3**: Before concluding vulnerability, verify that no compiler, runtime, OS, or framework protections prevent exploitation. Note: mitigations like ASLR and stack canaries raise the exploitation bar but do not eliminate the vulnerability itself. Distinguish "prevents exploitation entirely" (e.g., Rust's safe type system) from "makes exploitation harder" (e.g., ASLR).

**1.4**: Check if similar code patterns exist elsewhere and are handled safely. Review test coverage, code review history, and design documentation for this area.

### Phase 2: Exploitability Verification

**2.1**: Prove attacker controls the data reaching the vulnerability. **Key pitfall**: Assuming network/external data reaches the operation without tracing the actual path — internal storage set by trusted components is not attacker-controlled.

**2.2**: Create explicit algebraic proofs for bounds-related issues. Use the template in [fp-check-evidence-templates.md](fp-check-evidence-templates.md). Verify: IF validation_check_passes THEN bounds_guarantee_holds.

**2.3**: For race conditions, prove concurrent access is actually possible. **Key pitfall**: Assuming race conditions in single-threaded initialization or synchronized contexts.

**2.4**: Assess full attack surface: input control, validation bypass paths, timing dependencies, and state manipulation.

### Phase 3: Impact Assessment

**3.1**: Distinguish real security impact (RCE, privesc, info disclosure) from operational robustness issues.

**3.2**: Distinguish primary security controls from defense-in-depth. Failure of a defense-in-depth measure is not a vulnerability if primary protections remain intact.

### Phase 4: PoC Creation

**Always create a pseudocode PoC (4.1) and a negative PoC (4.4), in the report.** An executable PoC (4.2) or a
unit-test PoC (4.3) is written only when the invoking batch row's `validation` cell names it; then it lives only under
the session's scratchpad directory, is never committed, follows `real-stack-testing`'s offline rules and never
reaches a real external service (a botanical provider API, a deployed server or Keycloak). Otherwise record 4.2 and 4.3 as `not run: no validation cell names a PoC`.

1. **Pseudocode with data flow diagrams** showing the attack path (always)
2. **Executable PoC** in the target language - only under the rule above
3. **Unit test PoC** exercising the vulnerable code path - only under the rule above

See [fp-check-evidence-templates.md](fp-check-evidence-templates.md) for PoC templates.

**Negative PoC (Phase 4.4)**: Demonstrate the gap between normal operation and the exploit path — what preconditions must hold for the vulnerability to trigger, and why they don't hold under normal conditions.

### Phase 5: Devil's Advocate Review

Before final verdict, systematically challenge the vulnerability claim. Assume you are biased toward finding bugs and rating them as critical — actively work against that bias.

**Challenges arguing AGAINST the vulnerability:**

1. What non-vulnerability explanations exist for this code pattern?
2. How would the original developers justify this implementation?
3. What crucial system architecture context might be missing?
4. Am I seeing a vulnerability because the pattern "looks dangerous" rather than because it actually is?
5. Even if validation looks insufficient, does it actually prevent the claimed condition?
6. Am I incorrectly assuming attacker control over trusted data?
7. Have I rigorously proven the mathematical condition for vulnerability can occur?
8. Beyond theoretical possibility, is this practically exploitable?
9. Am I confusing defense-in-depth failure with a primary security vulnerability?
10. What compiler/runtime/OS protections might prevent exploitation?
11. Am I hallucinating this vulnerability? LLMs are biased toward seeing bugs everywhere and rating every finding as critical — is this actually a real, exploitable issue or am I pattern-matching on scary-looking code?

**Challenges arguing FOR the vulnerability (false-negative protection):**

12. Am I dismissing a real vulnerability because the exploit seems complex or unlikely?
13. Am I inventing mitigations or validation logic that I haven't verified in the actual source code? Re-read the code after reaching a conclusion.

See [fp-check-evidence-templates.md](fp-check-evidence-templates.md) for the devil's advocate documentation template.

## Gate Review

Apply the six gates from [fp-check-gate-reviews.md](fp-check-gate-reviews.md) to reach a verdict.
