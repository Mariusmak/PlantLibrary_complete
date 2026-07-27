---
name: real-stack-testing
description: Architecture rules for tests that must exercise the real product across module boundaries. Use when writing or reviewing integration, end-to-end, GUI/browser, acceptance, or batch-row tests; when changing their harnesses or fixtures; or when a green suite may not cover shipped behavior.
---

# Real-Stack Testing

## Invariant

Substitute only at a process boundary. Never substitute the product layer under
test.

Allowed doubles return canned external data or record calls:

- worker subprocesses and external CLIs
- third-party HTTP, chat, webhook, and LLM APIs
- clock, randomness, and ID generation
- filesystem behavior outside the workspace under test

Run these for real:

- composition root and production startup path
- domain services, schedulers, state machines, and policy engines
- persistence on a temporary real database
- routes, controllers, handlers, and rendering

Reject any fixture that re-implements a rule also present in product source. A
real object that cannot be constructed in a test is a product-design finding,
not permission to replace it with a stand-in.

## Harness contract

1. Boot the production entrypoint on an ephemeral port with temporary data.
2. Seed through public APIs where practical and cover relevant domain states.
3. Inject deterministic external events; never synchronize with fixed sleeps.
4. Fail on unhandled server errors and unexpected client or browser errors.
5. Capture full failure evidence to files; keep model-visible output compact.
6. Treat a skipped required validation as failure through the repository's
   strict flag.

For a rendered UI, assert the triad: visible DOM, outbound request, and
persisted state. Read [references/gui-testing.md](references/gui-testing.md)
only when the selected work exercises a rendered surface.

Read [references/metered-validation.md](references/metered-validation.md) only
when validation would use paid APIs, real workers, or another metered resource.

## Validation handoff

After implementation, invoke the `validate-real-stack` action with the row or
task ID, exact command, acceptance criteria, touched paths, and artifact path.
The cheaper validation worker runs the command in isolated context and returns
compact evidence.

The parent implementation agent owns fixes, checklist state, evidence
decisions, and completion. A validator must not change product code, tests, or
batch metadata. If the worker is unavailable, validate inline and report the
fallback.

## Review checklist

- [ ] No fixture duplicates product rules
- [ ] Production composition and real temporary persistence run
- [ ] Doubles exist only at process boundaries
- [ ] Errors and missing expected requests fail loudly
- [ ] UI coverage proves DOM + request + persisted state
- [ ] Required skips fail and evidence is written to files
