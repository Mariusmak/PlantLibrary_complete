# rework/ — index

Artifacts of the PlantLibrary master rework program: the transfer of the standards, skills, kits, harnesses and
conventions the Conductor program developed since 2026-09 into this superproject and its six submodules, in three
phases (A read-only analysis, B transfer lanes, C hand-back to validated batch work). File names follow
`<TYPE>_<topic>_<YYYY-MM-DD>.md`, `TYPE ∈ {PROMPT, PROMPTS, REGISTER, AUDIT, MATRIX, FINDING, EVIDENCE, HANDOVER,
PLAN}`; every new file gets a line here in the same commit. Declared as a general root by `D-2026-10-13-01`.

| File | What |
|---|---|
| `PROMPT_master-rework-kickoff_2026-10-13.md` | The kickoff prompt, verbatim: roots and measured facts (§1), the ten rules that bind every session (§2), the orchestrator's own steps `R-0`…`R-5` and the nine analysis lanes `A1`…`A9` and the transfer lanes `B1`…`B8`, `C1` (§3), the nine seed questions `Q-G-01`…`Q-G-09` (§4). The only copy; the runbook cites it |
| `PROMPTS_master-rework-runbook_2026-10-13.md` | The program runbook and ledger of record: §0 what it is and is not, §1 where things stand (re-measured at `R-0`), §2 rules by reference, §3 lanes and step map with one paste-ready block per step (filled at `R-3`), §3a what may run beside what, §Q operator questions with recorded answers, §O the operator-session prompt, §L the ledger |
| `REGISTER_operator-questions_2026-10-13.md` | Every operator question of the program, one row per `Q-<lane>-<nn>`: options, the recommended (a), the steps that wait on it, the answer verbatim with its date. Seeded with `Q-G-01`…`Q-G-09` at `R-0`; the operator session (§O) flips rows |
| `REGISTER_deferred-validations_2026-10-13.md` | Every validation a Phase B step would have run and did not (rule 1): what would be run, by which skill, for which change, after which lane. Becomes the first batches of Phase C (`C1`) |
| `REGISTER_conductor-reuse-candidates_2026-10-13.md` | One row per reusable thing found in the Conductor, kit and reconciliation sources: source path and pin, verdict, target repository and path, lane, question id. Header rows at `R-0`; merged from `A1`…`A9` at `R-2` |
