# handovers — index

Newest first. Line shape: `- YYYY-MM-DD · <file> · <TYPE> · <status> · <summary>`; a dated set folder
(`<TYPE>_<topic>_<YYYY-MM-DD>/`) takes one line naming the folder with its trailing `/`, and its members take
none. A file born in or moved into this root gets its line in the commit that adds it. A rename adds a row
to a closing section `## Renamed <YYYY-MM-DD>` holding `| old name | new name |`; a held name stays listed
under its current name, its row reading `**held** — cited by <citer>. Target on release: <new name>`; an
exempt-by-decision row cites its `D-YYYY-MM-DD-nn` entry. Seeded by the Repo Hygiene Template Kit's installer;
the lines are the anchoring session's.

- 2026-09-16 · FINDING_kit-release-after-move-fails-record_2026-09-16.md · FINDING · resolved by K-6 (kit 0.2.1) · kit 0.1.0/0.2.0 checks held-name existence before a later release folds, so a hold ended by a git mv always fails record; M-1 stopped uncommitted, kit patch K-6 (0.2.1) proposed before M-1 resumes
- 2026-09-16 · FINDING_kit-proof-floor-blocks-suite-anchoring_2026-09-16.md · FINDING · resolved by K-5 (kit 0.2.0) · kit 0.1.0's prompt file floor (≥ 1) makes A-2…A-7 unreachable (empty planning roots); kit patch proposed before A-2 resumes

