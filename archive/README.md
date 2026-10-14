# archive/ — retired material of SW_Development

This folder holds documents and files of the superproject that are retired: no longer living, kept for the record
and for the citers that still name them ("archive and hide, never delete", `KIT_SPEC.md` §1.9). It is allowlisted at
the repository root and declared `exempt-tree: archive — legacy` by `D-2026-10-14-01` in
`hygiene/HYGIENE_DECISIONS.md` (master rework `Q-A6S-01` (a)).

Rules:

1. A retired file arrives by `git mv` with its basename unchanged, under the subfolder named for where it came from:
   `archive/root/` for the repository root, `archive/<root>/` for a declared deliverable root (`repo-hygiene/`,
   `onboarding/`, `handovers/`, …). The commit that moves it adds its row to the table below and repoints its live
   citers; a citer that must not be edited (a frozen or held file, another track's live runbook) is served by this
   table, and where the file left a declared root, also by that root's "Renamed" table.
2. Nothing here is edited after it arrives, except this README's table.
3. Only the top-level `archive` is declared; no sub-path is ever declared, and `archive/` itself never moves or is
   renamed (a moved exempt path fails `record` on kit `0.2.1`, finding K-7). Files move freely below it.
4. `archive/` is not a deliverable root: it takes no `INDEX.md`, and its members keep their names.

Not archived here by `B3-6`: the spent hygiene-track files of `repo-hygiene/` (`Q-A6S-05` (a): they leave after
`M-8`/`M-9`, by `B3-8` and the Workspace release), the onboarding holds (`Q-A6S-02` (a)), `Todo.md` (`Q-A6S-04` (a)).

## Mapping

| old path | new path | date | entry |
|---|---|---|---|
| `IMPLEMENTATION_PLAN.md` | `archive/root/IMPLEMENTATION_PLAN.md` | 2026-10-14 | `D-2026-10-14-01` — the 2026-08-04 program sequencer, replaced by §H of `rework/PROMPTS_master-rework-runbook_2026-10-13.md` (H.7); cited by name on ten lines of `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md`, which stay as they are |
