# reviews — index

Deliverables of the operator-run review skills (`code-quality-review`, `security-audit`, `pathfinder`): one
`AUDIT_<skill>-<topic>_<YYYY-MM-DD>.md` per invocation that names this root. Declared a general root (pattern
standard) by `D-2026-10-14-01` (master rework `Q-B1-04` (a)).

Newest first. Line shape: `- YYYY-MM-DD · <file> · <TYPE> · <status> · <summary>`; a dated set folder
(`<TYPE>_<topic>_<YYYY-MM-DD>/`) takes one line naming the folder with its trailing `/`, and its members take
none. A file born in or moved into this root gets its line in the commit that adds it. A rename adds a row
to a closing section `## Renamed <YYYY-MM-DD>` holding `| old name | new name |`; a held name stays listed
under its current name, its row reading `**held** — cited by <citer>. Target on release: <new name>`; an
exempt-by-decision row cites its `D-YYYY-MM-DD-nn` entry. Seeded from the Repo Hygiene Template Kit's
`templates/INDEX_TEMPLATE.md` (0.2.1) at master rework step `B3-6`; no lines yet.
