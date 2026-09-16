# repo-hygiene/ — index

Artifacts of the track that derives the Repo Hygiene Template Kit from the Orchestrator repo's
hygiene harness, anchors it in this repository and its six submodules, and migrates the existing
corpus. File names follow `<TYPE>_<topic>_<YYYY-MM-DD>.md`, `TYPE ∈ {PROMPT, PROMPTS, REGISTER,
AUDIT, MATRIX, FINDING, EVIDENCE, HANDOVER}`; every new file gets a line here in the same commit.

| File | What |
|---|---|
| `PROMPT_kit-bootstrap-session_2026-09-15.md` | The one paste block that opens the track: the three roots, the harness inventory and corpus facts measured 2026-09-15, the model · reasoning line (Fable 5.1 · xhigh), gate `G0`'s eleven questions with recommendations, and the shape of the runbook the bootstrap session writes |
| `REGISTER_hygiene-harness-inventory_2026-09-15.md` | Bootstrap item (a): every component of SOURCE's hygiene harness at `fc5a14c` — path, rule, mechanism, creating commit or decision, portability verdict (generic / parameterised / Conductor-specific) with its placeholders; the A.0.2-versus-Chapter-8 supersession recorded; the baseline K-3 must reproduce (11 green nodes, parity pass, the two held names); the facts K-1 copies verbatim |
| `REGISTER_target-corpus-census_2026-09-15.md` | Bootstrap item (b)/(c): the pre-migration census of 967 markdown files over the superproject and six submodules — folder classes, 103 candidates with git-created / header dates, proposed TYPE and topic, every citation and the 33 holds with their citing lines, per-repo totals (the M-8 baseline), enforcement surfaces per repo, the conventions catalogued and the rules used |
| `PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` | The track runbook: the three roots, where things stand from the two registers, the `G0` record ("all recommendations accepted", resolved per question), the fresh-context review record, the step map `K-1`…`K-4` / `GK` / `A-1`…`A-7` / `GA` / `M-0` / `GM` / `M-1`…`M-9` with one paste block per step, model · reasoning and cwd, the gates table, the ladder and the ledger (every step todo) |
| `MATRIX_rename-map_2026-09-16.md` | Step `M-0`, presented at gate `GM`: the rename map for the superproject and six submodules — the 2026-09-16 re-measurement against the census (967 → 1024 files, no candidate changed), one row per candidate (103) with old → new, TYPE, git-created date, hold group, citer and target on release; the moves, the set folders, the never-renamed rows per decision record; the 35 holds by group; the 28 date divergences; the six proposals and two map calls with recommendations; the `GA` record and the `GM` words |
