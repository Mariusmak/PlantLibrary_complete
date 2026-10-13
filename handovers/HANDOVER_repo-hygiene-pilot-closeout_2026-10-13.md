# HANDOVER — repo-hygiene pilot close-out (2026-10-13)

*File name `HANDOVER_<topic>_<YYYY-MM-DD>.md` in the `handovers` root, listed in that root's `INDEX.md` in the same
commit. Written from the Repo Hygiene Template Kit's `templates/HANDOVER_CONTINUATION_TEMPLATE.md` (kit `0.2.1`) by step
`M-8` of `repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md` (§16, item 4), run as step `B3-1` of the master
rework program. The continuation section, like a prompt, names no proof surface and no invocation; what counts as proof
is the kit's `installer/INSTALL.md`, Verify section.*

## 1. What was done

| | |
|---|---|
| Session | `M-8` closing pass, as master-rework step `B3-1`; Opus 5.5 · high (the track's ladder names Sonnet 5 · thinking for `M-8`; the master runbook's row governs); 2026-10-13 |
| Repositories touched | SW_Development only, one commit on `master`: `repo-hygiene: M-8 - closing pass - 7 repositories measured; M-9 set listed`. The six submodules, the Repo Hygiene Template Kit and the Design Template Kit were read (git reads, the kit checker in `check` and `census` mode), never written |
| Delivered | `repo-hygiene/REGISTER_target-corpus-census_2026-10-13.md` (post-migration census, diff against the 2026-09-15 baseline, hold register with citers re-verified); `repo-hygiene/AUDIT_migration-record_2026-10-13.md` (migration record for seven repositories); this handover; one line each in `repo-hygiene/INDEX.md` and `handovers/INDEX.md`; the runbook's §L row `M-8` |
| Not delivered (owed) | runbook §16 item 5, the kit's changelog entry and its version decision: SOURCE-K is read-only in the master rework program, so it is the master runbook's owed item 17 (§3b), for the operator's Kit session together with `K-7` (owed item 9) |
| Verified | the seven verdict lines quoted in the migration record §7 — every repository `pass with holds — 0 violations`, held 3 / 10 / 1 / 1 / 1 / 1 / 1 |

## 2. State at handover

- **Trees.** The superproject is clean after the `M-8` commit except the six gitlinks, which the orchestrator bumps (the
  suites moved to step `B4-2`'s commits during this session; the census's measurements are identical at the pinned and
  the new heads). Every submodule is clean on `main`.
- **Kit.** All seven pin kit `0.2.1` (SOURCE harness `fc5a14c`), carry the rule block stamped `0.2.1`, a checker
  byte-identical to the kit's at `810733e` (`v0.2.1`, the kit's HEAD) and the CI workflow; wrappers in PyApp and Server;
  the superproject alone runs the root-allowlist module and a prompt floor of 1, the suites floor 0. No hook anywhere.
  No re-pin is owed while the kit stays at `0.2.1`.
- **Corpus.** 1072 markdown files by the baseline's walk (967 at the baseline, 1024 at `M-0`); of the 103 baseline
  candidates 4 were compliant, 15 files were renamed or moved, 3 set folders renamed (22 members), 29 exempted by
  decision, 30 names and 1 set folder remain held, 5 holds were released during migration.
- **Holds by group, and what releases each** (citers in the census register §3):

| group | held | releases it |
|---|---|---|
| onboarding runbook | SW `handovers/HANDOVER_batch-package-schema-drift…`, `onboarding/AUDIT_skill-assumptions…`, `onboarding/REGISTER_package-census…` | the onboarding runbook retiring (Q-A6S-02 (a)); the audit is also cited by PyApp `scripts/harness/regression_scope.py:33` and `scope_cap.py:5`, which the record does not name |
| live package | the five suites' `<SUITE>_V1_PROPOSAL.md`; Workspace SV1 `proposal/00`–`02`, `MVP_Reconciliation/02`, `04`, `05` | the five suite proposals: **`M-9` now**, on the operator's recorded words (Q-A6P-03, Q-A6V-02, Q-A6C-04, Q-A6D-02, Q-A6A-02); the six Workspace names: their anchors stop citing them (Q-A6W-03 (a) keeps them) |
| terminal `STATE.md` + live | Workspace `prompts/PROCESS_IMPROVEMENTS_HANDOFF_2026-07-10.md` | the PyApp, Dashboard and AndroidApp anchors migrating |
| pinned | Dashboard `docs/WD-MOCKUP-UPGRADE_PROPOSAL.md`, `docs/WD-UX-10_mockup_parity_report.md`; PyApp `improvements.md`, `Design_Implementation_Claude.md`; Workspace SDA `proposal/00`–`03` | the two Dashboard names: **`M-9` now** (Q-A6D-03 (a)); `improvements.md` never (Q-A6P-05 (a)); the rest: the Design kit's owner or a re-pin |
| code | PyApp `plant_information_system_implementation_plan_v1.md`; Server `SV-B07_dashboard_endpoint_coverage_report.md`; AndroidApp `security_token_storage_acceptance.md`; Workspace SDA `proposal/04`, `MODEL_RECOMMENDATION.md`, `PlantLibrary_Full_Implementation_Update.md`, `SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | a code edit in a batch (policy A.0.5) |
| record | Workspace `docs/proposals/Repo_Restructure_MVP_V1_Split/` (set folder) | kit patch `K-7` (Q-G-06 open; owed item 9), then a Workspace `M-9` batch with the five suites' one-line `implementation/README.md` path fixes |

- **The M-9 set: seven names**, all on the operator's words of 2026-10-13 18:05 UTC — PyApp `PYAPP_V1_PROPOSAL.md`, Server
  `SERVER_V1_PROPOSAL.md`, SharedContracts `SHAREDCONTRACTS_V1_PROPOSAL.md`, Dashboard `DASHBOARD_V1_PROPOSAL.md`,
  `WD-MOCKUP-UPGRADE_PROPOSAL.md`, `WD-UX-10_mockup_parity_report.md`, AndroidApp `ANDROIDAPP_V1_PROPOSAL.md`. Only the
  AndroidApp name has no hold-class citer left; the other four live-package names are still cited by their own
  `STATE.md` and the two Dashboard names by the closed Design initiative, so their release entries quote the words.
- **Two directives name stale targets.** Dashboard `D-2026-09-16-01`:137 (`WD-MOCKUP…`) and AndroidApp
  `D-2026-09-16-01`:144 (`security_token…`) say `planning/`; `MC-1` moved both targets to `proposal/`
  (`D-2026-09-17-02` item 2 and item 1). A release entry must restate the `proposal/` target.
- **The three FINDINGs.** `FINDING_kit-proof-floor-blocks-suite-anchoring_2026-09-16.md` — resolved by `K-5` (kit
  `0.2.0`); `FINDING_kit-release-after-move-fails-record_2026-09-16.md` — resolved by `K-6` (kit `0.2.1`);
  `FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md` — open, kit patch `K-7` proposed, undecided (Q-G-06).
- **What the pilot taught the kit** — the content owed to the kit's changelog (item 17), each with its evidence:
  1. A prompt floor of at least 1 made empty planning roots unanchorable — fixed in `0.2.0` (`K-5`).
  2. A hold ended by a `git mv` failed `record` — fixed in `0.2.1` (`K-6`).
  3. An `exempt-tree`/`exempt-subfolder` path cannot be retired when it moves, and `held-name` cannot name a folder — the
     `M-7` deviation; `K-7` proposed (additive directive: a minor version).
  4. `check` and `census` do not see held names outside declared roots: 12 of the 30 held names (and the set folder) live
     only in the records, so `M-0` and `M-8` counted them by hand (the `A-1` observation, map §1a). A census section
     listing the record's out-of-root holds would make the closing pass mechanical.
  5. No directive retargets a held name: `MC-1` changed two targets in a later entry's prose while the directive lines
     kept the old ones (above). A later `held-name` line for the same path superseding the earlier one, or a stated
     rule, would keep the record machine-true.
  6. `exempt-name` has no existence check and nothing ends it: a dead line stays harmless but would exempt a same-named
     file in any root (`rework/AUDIT_corpus-census-superproject_2026-10-13.md` F-A6S-07).
  7. A re-pin to a newer kit is two runs — `--target` alone (the upgrade notice, checker re-synced) then `--force` with a
     decision entry; all six suites did both at `M-2`…`M-7`. `installer/INSTALL.md` "The pin" could state the recipe.
  8. The census's "candidates" (non-compliant, unheld names inside roots) is not the register's "candidates" (dated
     deliverables anywhere); the closing diff needed the register's walk reproduced outside the kit.
  9. Releases against never-edit citers (live `STATE.md`, pinned trees) happen by the operator's recorded words, which the
     migrate runbook allows (`RUNBOOK_migrate-an-existing-repository.md:51-52`); its `M-R` step could require the words
     and their date to be quoted in the release entry.
  10. The migration-record template's per-repository name and three-commit split did not fit a superproject-plus-
      submodules pilot migrated as one commit per repository plus a gitlink bump; a superproject variant could be noted.
  Items 4–10 are wording or additive; with `K-7` the kit session decides the version (Q-B3-02 proposed). If the version
  moves, the seven repositories re-pin (`--target`, then `--force` and a decision entry each), recorded here as owed.

## 3. Open items

| Item | Owner | Blocked on |
|---|---|---|
| `M-9` for the seven names above (five suites, serial) | master-rework step `B3-4` | nothing (`B3-1` committed; the six Q answers recorded) |
| Kit changelog entry for the pilot lessons, version decision, tag | operator's Kit session (master runbook owed item 17) | the operator scheduling it, with item 9 |
| `K-7` kit patch, then the Workspace restructure set's `M-9` | operator's Kit session, then a Workspace `M-9` batch | Q-G-06 |
| Re-pin of seven repositories | the session after a kit version move | the kit session |
| The three onboarding-runbook holds | the onboarding track's retirement | the Conductor's S-2 gate (onboarding runbook step 6) |
| Track runbook §3 step map row `M-8` still reads `todo` (this step wrote §L only, as its Write line allows) | orchestrator | Q-B3-01 proposed |
| Archiving the spent track files (`PROMPT_kit-bootstrap-session`, `REGISTER_hygiene-harness-inventory`, `REGISTER_target-corpus-census_2026-09-15`) | the archive step of lane B3 | Q-A6S-05 (a): after `M-8` — now possible |

## 4. Continuation — paste this into the next session

```text
Scope: step M-9 of repo-hygiene/PROMPTS_repo-hygiene-track-runbook_2026-09-15.md (§17) for the seven names this
handover lists as the M-9 set, one release batch per repository (PyApp, Server, SharedContracts, Dashboard, AndroidApp),
serially, as master-rework step B3-4 frames it. Not here: any other held name, the Workspace restructure set (waits for
K-7), the kit, any rename the confirmed map's target-on-release column does not name.

Read first: this handover §2; repo-hygiene/REGISTER_target-corpus-census_2026-10-13.md §3 rows #4, #8, #10-#14 (citers at
HEAD on 2026-10-13); each repository's hygiene/HYGIENE_DECISIONS.md (the held-name lines and, for Dashboard and
AndroidApp, the MC-1 target restatements in D-2026-09-17-02); the operator's answers to Q-A6P-03, Q-A6V-02, Q-A6C-04,
Q-A6D-02, Q-A6D-03, Q-A6A-02 in rework/REGISTER_operator-questions_2026-10-13.md; the track runbook §17.

Constraints: re-verify every citer at HEAD across all seven repositories before each release (the grep result quoted in
the entry); git mv only; a release line in the same decision entry as the move, the entry quoting the operator's words
and their date; a citing STATE.md line changes only as a package decision recorded in that package's STATE.md; pinned
trees, the Design kit and code are never edited; line endings as found; one commit per repository; no push.

Done when: each of the five repositories' verdict, per the kit's installer/INSTALL.md Verify section, is pass or pass
with holds with the released names gone from its held lines; the released names have index lines and flipped "Renamed"
rows; the track runbook §L carries one M-9 line per repository.

Commit line (each repository): hygiene: M-9 - released <names>
```
