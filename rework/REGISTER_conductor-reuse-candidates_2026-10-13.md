# Conductor reuse candidates — PlantLibrary master rework (register of record)

*Opened 2026-10-13 at `R-0` (`PROMPT_master-rework-kickoff_2026-10-13.md` §2 rule 2, §3 `R-2`). One row per
reusable thing found in the sources — the Conductor (`C:\Programmierung\Orchestrator_System` at `2e7adb3` and its
worktrees), the Design Template Kit (`f08e588`, Kit 1.7.0), the Repo Hygiene Template Kit (`0.2.1`), the round-6
reconciliation folder and the Working_Folder — with its verdict and its target in this repository set. Sources are
read-only: a finding about a source is a row here, never an edit there. Header rows at `R-0`; merged from the nine
analysis lanes `A1`…`A9` at `R-2`; the transfer lanes `B1`…`B8` cite rows by ID.*

## How to read a row

| Column | Meaning |
|---|---|
| ID | `RC-<lane>-<nn>`, lane = the analysis lane that found it (`A1`…`A9`) |
| Source | Repository-relative path in the source, with the pin (commit or version) it was read at |
| What | One line: what it is and what it does |
| Verdict | `adopt verbatim` · `adapt` (what and why) · `keep PlantLibrary's` · `retire` · `record only` (a kit or Conductor defect, never patched from here) |
| Target | Repository and path in TARGET, or `—` |
| Lane | The transfer lane (`B1`…`B8`, `C1`) that acts on it |
| Q | The operator question that gates it, or `—` |
| Verified | `R-1` for a claim the orchestrator re-checked on the critical path; blank for a lane's claim taken as reported |

## Rows

| ID | Source | What | Verdict | Target | Lane | Q | Verified |
|---|---|---|---|---|---|---|---|
