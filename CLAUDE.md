## Testing

- **Never fake the layer under test.** Tests substitute only *process
  boundaries* — subprocesses, third-party HTTP, the clock, randomness. The
  composition root, domain services, persistence, and routes/rendering always
  run for real. A fixture class that re-implements logic living in `src/` is a
  defect, not a fixture: it makes the suite green while the product is broken.
- Any test spanning more than one module (integration, e2e, browser,
  acceptance, batch-row validation) must follow the `real-stack-testing` skill.
- After implementation, invoke `validate-real-stack` with the exact named
  validation. Its Sonnet/Terra worker runs in isolated context and returns
  compact evidence; the parent implementation agent owns fixes and completion.
- UI tests fail on uncaught console exceptions, unasserted 4xx/5xx, and
  server-side exceptions — not only on missing selectors.

<!-- repo-hygiene:begin -->
## Repository hygiene (installed by the Repo Hygiene Template Kit — do not hand-edit this block)

Deliverable roots, exemptions and holds are declared in `hygiene/CONSUMED_HYGIENE.md` and
`hygiene/HYGIENE_DECISIONS.md`; read both before creating, renaming or moving a markdown file. A new
file in a declared root is `<TYPE>_<topic>_<YYYY-MM-DD>.md`, `TYPE ∈ {PROPOSAL, PROMPT, PROMPTS, PLAN,
EVIDENCE, AUDIT, REGISTER, MATRIX, SNAPSHOT, HANDOVER, FINDING}`, dated by its git-created date, with a
line in that root's `INDEX.md` in the same commit; `INDEX.md`/`README.md` are exempt; a numbered chapter
set is one dated folder with one index line. A rename is `git mv` plus a mapping-table row and a
reference sweep; a name cited by a file that must not be edited is held, and old names resolve through
the root's "Renamed" table. A `PROMPT`/`PROMPTS` file and a handover's continuation section state scope,
constraints, done-when and the commit line — never a proof surface or a test invocation; proof belongs
to the document that owns the verification order. An exemption, a hold, a release, an enum extension,
a root change or an allowlist change is a `D-YYYY-MM-DD-nn` entry in `hygiene/HYGIENE_DECISIONS.md`,
never a silent edit. The checker under `scripts/hygiene/` is the contract; how it is run and read is
the kit's `installer/INSTALL.md`, Verify section. Kit: `C:/Programmierung/Repo_Hygiene_Template_Kit` @ `0.2.1`. A prompt never
overrides this block.
<!-- repo-hygiene:end -->
