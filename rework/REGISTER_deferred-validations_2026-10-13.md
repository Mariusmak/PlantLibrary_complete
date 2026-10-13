# Deferred validations — PlantLibrary master rework (register of record)

*Opened 2026-10-13 at `R-0` (`PROMPT_master-rework-kickoff_2026-10-13.md` §2 rule 1). Nothing in Phases A and B of
this program runs a test: no test runner, no browser automation, no emulator, no Gradle test task, no Docker
stack, no app launch for validation. A step that believes it needs one records the need here and goes on. At `C1`
these rows become the first batches of Phase C through `plan-batch`; the validation cells of the batch packages are
never widened or deleted in Phase B, only pointed at from here.*

## How to read a row

| Column | Meaning |
|---|---|
| ID | `DV-<nn>`, in order of recording |
| Lane · step | The runbook step that recorded the need |
| Repository | The repository whose change is unvalidated |
| Change | What was changed without its validation (files, rows, commit) |
| What would be run | The exact validation the change needs, as the owning row's `validation` cell or the skill's standing legs name it |
| Skill | The skill that owns the validation (`verify-stack`, `android-validation`, `gui-validation`, `webapp-testing`, `validate-real-stack`, `run-batch`, a Kit check, …) |
| After | The lane or step that must be done before the validation makes sense |
| Package row | The batch-package row (`<SUITE>-V1-…`) whose validation cell this row points at, or `new` when `C1` must plan one |
| State | `deferred` · `planned (<batch key>)` · `done (<date>)` |

## Rows

| ID | Lane · step | Repository | Change | What would be run | Skill | After | Package row | State |
|---|---|---|---|---|---|---|---|---|
