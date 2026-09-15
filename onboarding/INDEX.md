# onboarding/ — index

Artifacts of the track that brings the `PlantLibrary_*` suites under Conductor instance 2.
File names follow `<TYPE>_<topic>_<YYYY-MM-DD>.md`, `TYPE ∈ {PROMPTS, AUDIT, REGISTER, FINDING,
EVIDENCE, HANDOVER}`; every new file gets a line here in the same commit.

| File | What |
|---|---|
| `PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | The runbook: findings F-1…F-11, the step map `0`…`9`, gates `G1`/`G2`, the exact prompts with model and reasoning, the migration recipe (Appendix B), the REST calls (Appendix C), the Workspace verdicts (Appendix D), the ledger §L |
| `../HANDOVER_batch-package-schema-drift_2026-09-15.md` | The handover this track starts from (schema drift, Requires lint, instance-2 state) |
| `REGISTER_package-census_2026-09-15.md` | Running record of `scripts\harness\check_batch_packages.py` output; step 0 captured pre-migration error counts for the seven live packages |
| `AUDIT_skill-assumptions_2026-09-15.md` | Step `1`: every path, script, config key and convention the four batch skills assume, checked against all six suite trees; the three measurements behind `F-6`/`F-7` (parent-folder skill discovery from PyApp and Server; the dev-repo harness refusals on a scratch PyApp copy); the per-suite `CLAUDE.md`/`AGENTS.md` input for step `3`; the `G1` recommendations on `D1`–`D8` |
