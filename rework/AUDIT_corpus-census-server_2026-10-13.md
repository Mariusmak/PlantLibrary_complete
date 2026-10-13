# Corpus census — PlantLibrary_Server — lane A6 (read-only analysis, 2026-10-13)

Pin read: `PlantLibrary_Server` main @ `f1a31b9`, tree clean. Kit 0.2.1 (`PlantLibrary_Server/hygiene/CONSUMED_HYGIENE.md:11`). Static reading only; no test, build, container or install was run. The checker's `check` and `census` were run (read-only).

## §0 Summary

- 72 tracked `.md` files, classified in 28 rows (§7.1): 19 byte-mirrored skill/agent files, 10 frozen MVP files, 11 `docs/` notes, 5 package validation notes, 3 dated evidence files, the rest live package, root, index and hygiene files.
- Checker verdict `repo-hygiene: pass with holds — 0 violations, 1 held`; repository totals 7 files in roots, 3 compliant, 0 candidates, 3 exempt (the three INDEX.md), 1 held, 0 set folders (§7.4).
- Four directive lines are active in the record (one `exempt-tree`, one `exempt-name`, two `held-name`) and two `held-name` lines were released at M-3 (§7.2). The checker prints only one `held:` line although two holds are active, because the dashboard hold sits in `docs/`, outside every root (F-A6V-02).
- K-7 bites Server in exactly one place: `exempt-tree: implementation/MVP` (`PlantLibrary_Server/hygiene/HYGIENE_DECISIONS.md:109`). The MVP tree cannot move into an `archive/` until K-7 lands; nothing else in Server is exposed (F-A6V-01). Q-G-06 (a) costs Server nothing.
- Server holds almost nothing worth archiving: no `_ACT_STATE.md`, no `Todo.md`, no tracked handover, no OpenAPI export markdown, no setup guide. The one real archive candidate is the V1 `DRIVER_SCRIPT.md`; GC-7053's lines 7, 21, 42, 61 are confirmed, and `README.md:46-47` is a further instructing site the note did not list (F-A6V-05).
- The "server setup guide" does not exist. Row `SV-OPS-INSTALL-01` (todo) names `deploy/SETUP_GUIDE.md` as its output; the file is absent and no batch has run (F-A6V-06).
- Defects found: `app/core/metrics.py:4` cites a doc name that never existed (F-A6V-04); `scripts/run_next_batch.py` reads two root files that moved in July (F-A6V-07); two validation names are cited from other repositories but do not exist yet (F-A6V-08).
- Recommended (a) everywhere: no speculative `archive/`; create it only if the operator approves retiring DRIVER_SCRIPT.md (Q-A6V-01); release the SERVER_V1_PROPOSAL hold in B3 (Q-A6V-02); keep the dashboard-report hold until a batch edits the three docstrings (Q-A6V-03).
- 6 questions (§4), 3 claims to verify (§6).

## §1 Coverage

| Item | Status (read / partly read / not read) | Reason |
|---|---|---|
| Kickoff prompt §1, §2 | read | in full |
| `PlantLibrary_Server/CLAUDE.md` (149 lines) | read | in full; two lines hold runnable test commands, not reproduced here |
| `PlantLibrary_Server/AGENTS.md` | read | in full |
| `hygiene/CONSUMED_HYGIENE.md`, `hygiene/HYGIENE_DECISIONS.md` | read | in full, every directive line extracted |
| `repo-hygiene/MATRIX_rename-map_2026-09-16.md` Server section (§5), §10, §13 | read | Server rows, holds summary, reconciliation row; other repositories' sections not read |
| `handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md` | read | in full |
| `Repo_Hygiene_Template_Kit/KIT_SPEC.md` | partly read | §1.4-1.9, §6 directive table, census paragraph; other sections not read |
| Kit checker as installed in Server (`scripts/hygiene/repo_hygiene_check.py`) | partly read | `_apply_directive` (lines 426-470) only |
| `onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md` | partly read | §N (918-934), lines 294-299, 356-362, ledger rows 5/7/8; rest not read |
| V1 package `DRIVER_SCRIPT.md`, `README.md`, `SCOPE.md`, `CONTEXT_INDEX.md`, three INDEX.md, `validation/README.md` | read | in full |
| V1 package `STATE.md` (237 lines) | partly read | lines 1-40, 99-140, 200-237; the 2026-07-15..17 entries skimmed by heading |
| V1 package `BATCH_PLAN.md`, `TASK_CHECKLIST.md` | partly read | headings, status counts, rows 24, 52, 55; no other row bodies |
| V1 package `TASK_CONTEXT.md` (549 lines) | not read | only grepped for citations; out of census scope |
| `proposal/SERVER_V1_PROPOSAL.md` (111 lines) | partly read | lines 1-12 and grep hits |
| `planning/` three dated files (106/82/144 lines) | partly read | headings and citation lines only |
| `validation/SV1-*.md` (5 files) | partly read | first lines and citers; bodies not read |
| `docs/SV-*.md` (10) and `docs/local_android_test_environment.md` | partly read | first 7 lines each plus citation greps |
| `implementation/MVP/**` (10 files) | partly read | headings of four files, grep for citers; frozen, bodies not read |
| `README.md`, `implementation/README.md`, `docs/README.md`, `openapi/README.md`, `app/README.md`, `tests/README.md` | read | in full; `deploy/README.md` first 30 of 72 lines |
| `.claude/**`, `.codex/**` mirrors (19 md + 5 non-md) | partly read | compared by git blob hash against the superproject (24 of 24 identical); content not read (lane A1 owns it) |
| Citer sweep | read | `git grep` over the superproject (root, onboarding, repo-hygiene, handovers, skills), Server, Workspace, SharedContracts, Dashboard, AndroidApp, PyApp at HEAD; citing files read only as the hit line |
| `repo_hygiene_check.py check` and `census` | read | run once each, output in §7.4 |

## §2 Findings

**F-A6V-01 — K-7 exposure in Server is one directive.** The only `exempt-tree` or `exempt-subfolder` line in the record is `PlantLibrary_Server/hygiene/HYGIENE_DECISIONS.md:109` (`exempt-tree: implementation/MVP — frozen`). The checker tests `target.exists()` on every `exempt-tree` at fold time with no release path: `PlantLibrary_Server/scripts/hygiene/repo_hygiene_check.py:446-451`. A `git mv` of `implementation/MVP` into an archive would fail `record` for ever on kit 0.2.1 — the shape described at `handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md:24-30`, which names "every frozen `implementation/MVP/` tree if archived" at lines 39-41. The `exempt-name` for `docs/local_android_test_environment.md` (`HYGIENE_DECISIONS.md:131`) has no existence test in its path form (`repo_hygiene_check.py:439-440`), and that file never moves.

**F-A6V-02 — Two holds are active; the checker reports one.** `HYGIENE_DECISIONS.md:139` (SERVER_V1_PROPOSAL) and `:142` (SV-B07 dashboard report) are both unreleased. The `check` output prints a single `held:` line and `census` counts `1 held`, because `docs/` is not a declared root. The second hold is carried only by this record, by `implementation/System_V1_Implementation/planning/INDEX.md:24` and by `HYGIENE_DECISIONS.md:279-282`. B3 must track it by hand; the checker will not fail if it is forgotten.

**F-A6V-03 — The SERVER_V1_PROPOSAL hold's stated precondition is met.** The hold waited on onboarding steps 2a/2b (`HYGIENE_DECISIONS.md:60-61`, `:279-280`); the onboarding ledger records 2b done (`onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:908`). The remaining blocker is textual: the `held-name` note cites `implementation/System_V1_Implementation/STATE.md:15` (`HYGIENE_DECISIONS.md:139`). In-repo citing lines to sweep on release: `PlantLibrary_Server/implementation/System_V1_Implementation/STATE.md:15`, `README.md:6`, `README.md:60`, `CONTEXT_INDEX.md:10`, plus the index lines `proposal/INDEX.md:11` and `:20`. Outside the repo, `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/00_V1_SYSTEM_PROPOSAL.md:222` and `PlantLibrary_Workspace/docs/proposals/Repo_Restructure_MVP_V1_Split/VERIFICATION_REPORT.md:57` cite it by path; both are held or frozen files and are served by the root's "Renamed" table (`HYGIENE_DECISIONS.md:149-152`). A release needs no kit change (K-6 covers a release by `git mv`).

**F-A6V-04 — A code docstring cites a doc name that never existed.** `PlantLibrary_Server/app/core/metrics.py:4` cites `docs/SV-DEPLOY-HARDEN-01_deployment_hardening_report.md`. No such file is in the index, and no commit ever added one (`git log --all --diff-filter=A --name-only -- 'docs/SV-DEPLOY*'` is empty); the report was always `SV-B08_deployment_hardening_report.md`, now `implementation/System_V1_Implementation/planning/EVIDENCE_sv-b08-deployment-hardening_2026-07-05.md`. M-3's hold analysis did not see it because the name differs. It is a third code citer of the same class as the dashboard report's two (`app/api/routes/dashboard_support.py:2`, `app/workers/tasks.py:9`). A docstring edit needs no validation, but policy A.0.5 routes code-cited names through a batch (Q-A6V-03).

**F-A6V-05 — DRIVER_SCRIPT.md: GC-7053 confirmed for Server, plus one more instructing site.** `PlantLibrary_Server/implementation/System_V1_Implementation/DRIVER_SCRIPT.md:7` (deprecation note), `:21` ("State cache: `_ACT_STATE.md` (create on first run…)"), `:42` (read it), `:61` (append to it): the onboarding runbook's "7,21,42,61" is exact (`onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:934`). Not listed there: `PlantLibrary_Server/implementation/System_V1_Implementation/README.md:43` ("Execute …/DRIVER_SCRIPT.md") and `:46-47` ("The driver creates/maintains `_ACT_STATE.md`"), plus the README's file-index row `:59`. `SCOPE.md:3` carries the legacy marker D7 chose, and `SCOPE.md` lines 5-30 reproduce the Hard scope and Standing invariants. In-repo mentions a move would leave stale: `README.md:12,43,59`, `SCOPE.md:3,16`, `CONTEXT_INDEX.md:38`, `STATE.md:125,233-234`, `openapi/README.md:10`, `scripts/export_openapi.py:9`, `scripts/run_next_batch.py:5,77`, `planning/AUDIT_sv-contract-01-contract-validation_2026-07-04.md:11` — all prose by basename, none a link. `STATE.md:233-234` records "kept, superseded, not deleted"; kit §1.9 says "archive and hide, never delete". The file is not in a declared root, so the checker never looks at it.

**F-A6V-06 — No server setup guide, no OpenAPI export markdown, no sequencer files other than DRIVER_SCRIPT.** `git ls-files` finds no `*SETUP*` or `*GUIDE*` file. `PlantLibrary_Server/implementation/System_V1_Implementation/TASK_CHECKLIST.md:52` (`SV-OPS-INSTALL-01`, status `todo`, batch `SV1-B06`) lists `deploy/SETUP_GUIDE.md` among its files; it does not exist. The superproject backlog `IMPLEMENTATION_PLAN.md:367` names the guide ("Server setup guide … next to `SV-OPS-INSTALL-01`"); the row already covers it, nothing is un-homed. The only deploy prose is `deploy/README.md`. `openapi/` holds `plantlibrary.openapi.yaml` (generated, not markdown) and `openapi/README.md` (13 lines). Absent from the tree: `_ACT_STATE.md`, `Todo.md`, tracked HANDOVER files (`implementation/System_V1_Implementation/handovers/INDEX.md` has no lines), a root `IMPLEMENTATION_PLAN.md` or `WORKSPACE_STATE.md`. The Server's only `IMPLEMENTATION_PLAN.md` is the frozen MVP one (`implementation/MVP/package/IMPLEMENTATION_PLAN.md`), not the superproject sequencer Q-G-05 names.

**F-A6V-07 — `scripts/run_next_batch.py` does not work against the current layout.** It reads `BATCH_PLAN.md` and `TASK_CHECKLIST.md` at the repository root (`PlantLibrary_Server/scripts/run_next_batch.py:14-16`); both moved to `implementation/MVP/package/` on 2026-07-15 (`implementation/README.md:12-15`), and it parses the 9-cell MVP row shape (`:28`), not the 15-column schema. Its docstring and last print line point at DRIVER_SCRIPT (`:5`, `:77`); `README.md:10` still advertises it. Run-batch and the Conductor select the next batch; nothing else in Server replaces it.

**F-A6V-08 — Forward citations of validation names that do not exist yet.** `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/TASK_CONTEXT.md:67` cites `PlantLibrary_Server/implementation/System_V1_Implementation/validation/SV1-B00_contract_decisions.md` (owner row `SV-SYNC-PUSH-02`, `todo`, `TASK_CHECKLIST.md:24`); `PlantLibrary_Workspace/implementation/System_V1_Implementation/BATCH_PLAN.md:160` and `TASK_CONTEXT.md:310` cite `…/validation/SV1-B06_security_review_triage.md` (owner row `SV-V1-SEC-01`, `todo`, `TASK_CHECKLIST.md:55`). Neither file exists. `validation/README.md:5-11` lists six expected files, only `SV1-B00_profile_sync_record.md` exists, and the README omits the four files that do exist (`SV1-B00_VGAP-005_sync_push.md`, `SV1-B00_partial_validation.md`, `SV1-B00_refdata_decision.md`, `SV1-B06_oidc_local.md`) and the triage file. Written validation files are cited by path from Workspace (`MVP_VALIDATION_GAP_LOG.md:114,134,140,155`, `SYSTEM_ACCEPTANCE_REPORT.md:21,52`) and AndroidApp (`AN-B13_VGAP-005_offline_sync_validation_2026-07-13.md:28`, `AN1-B14_oidc_local.md:21`): the `validation/` names must never be renamed.

**F-A6V-09 — `implementation/README.md:27` cites the Workspace set that K-7 holds.** The path `PlantLibrary_Workspace/docs/proposals/Repo_Restructure_MVP_V1_Split/manifests/MANIFEST_Server.csv` is the one the finding says every suite's `implementation/README.md` needs fixed by one line when the set is released (`handovers/FINDING_kit-exempt-tree-cannot-retire-on-rename_2026-09-17.md:91-93`). A Workspace release (M-9) therefore owes Server one sweep edit.

**F-A6V-10 — Broken relative links in eight `docs/` notes.** `docs/SV-AUTH-01_auth_design.md:4,6`, `SV-BOOT-02_local_services_plan.md:5,7`, `SV-CONFLICT-01_conflict_protocol_notes.md:4`, `SV-CRUD-01_core_api_notes.md:6`, `SV-DOMAIN-01_domain_port_notes.md:5`, `SV-GARDEN-01_garden_model_plan.md:4`, `SV-MEDIA-01_media_flow_notes.md:4`, `SV-SYNC-01_sync_protocol_notes.md:4` use `../PlantLibrary_Workspace/strategy/Cross_Platform_Strategy/…`, which resolves to `PlantLibrary_Server/PlantLibrary_Workspace/…` from `docs/` (correct only from the repository root, as in `README.md:34-39`). The target tree exists at `PlantLibrary_Workspace/strategy/Cross_Platform_Strategy`. Product documentation is editable; `../../PlantLibrary_Workspace/…` fixes all ten lines.

**F-A6V-11 — Stale stubs.** `PlantLibrary_Server/app/README.md:3` and `tests/README.md:3` still say "empty scaffold until then" (SV-B01 landed in July). `README.md:7-15` does not list `hygiene/`, `openapi/`, `scripts/hygiene/` or `.claude`/`.codex`. `implementation/System_V1_Implementation/STATE.md:3-10` ("Durable status") describes 2026-08-04 while entries run to 2026-09-15 (`STATE.md:204`). `STATE.md:105` has a double-encoded dash (`â€”`); STATE is an append-only continuation log, so the fix belongs to B4's package pass, not a silent edit.

**F-A6V-12 — Mirrors are byte-identical and undeclared.** All 24 tracked files under `.claude/` and `.codex/` (19 md, 5 non-md) have the same git blob as the superproject's copy (compared with `git rev-parse HEAD:<path>` in both). `CLAUDE.md:89-93` and `AGENTS.md:34-37` forbid edits. The record declares no exemption for them; the checker ignores them (outside every root). Server has no `scripts/harness/`, only `scripts/hygiene/` (`git ls-files scripts`), consistent with onboarding step 7 `todo` (`onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:195,914`) — lane A2/B7's concern, noted because `CLAUDE.md:91-92` names a parity checker that lives in the superproject.

**F-A6V-13 — Line endings are mixed.** `git ls-files --eol`: `AGENTS.md`, `CLAUDE.md`, `README.md` are `i/lf w/crlf`; `STATE.md`, `DRIVER_SCRIPT.md`, `HYGIENE_DECISIONS.md` are `i/lf w/lf`. Any B3 edit to a markdown file must preserve the working-tree form (kickoff rule 8). Lane A8 owns the policy.

## §3 Candidates

| Id | Source path @ pin | What | Verdict | Target repo and path | Lane (B3) | Q id or — |
|---|---|---|---|---|---|---|
| RC-A6V-01 | `PlantLibrary_Server/implementation/System_V1_Implementation/DRIVER_SCRIPT.md` @ `f1a31b9` | Legacy driver with four `_ACT_STATE.md` instructions; Hard scope already lives in `SCOPE.md` | archive (after B4 sweeps the README and A7/B8 confirm instance 2 needs `SCOPE.md` only) | `PlantLibrary_Server/archive/System_V1_Implementation/DRIVER_SCRIPT.md` | B3 (move) after B4 (sweep) | Q-A6V-01 |
| RC-A6V-02 | `PlantLibrary_Server/implementation/System_V1_Implementation/proposal/SERVER_V1_PROPOSAL.md` @ `f1a31b9` | Held proposal whose precondition (2a/2b) is met | release the hold, `git mv` to `PROPOSAL_server-v1_2026-07-10.md`, sweep four citing lines | `PlantLibrary_Server/implementation/System_V1_Implementation/proposal/PROPOSAL_server-v1_2026-07-10.md` | B3 (M-9 for Server) | Q-A6V-02 |
| RC-A6V-03 | `PlantLibrary_Server/docs/SV-B07_dashboard_endpoint_coverage_report.md` @ `f1a31b9` | Held (code citers) coverage snapshot of 2026-07-05 | hold; release in the first resumed Server batch that edits the three docstrings | on release `PlantLibrary_Server/implementation/System_V1_Implementation/planning/AUDIT_sv-b07-dashboard-endpoint-coverage_2026-07-05.md` | B3 records a deferred row; Phase C executes | Q-A6V-03 |
| RC-A6V-04 | `PlantLibrary_Server/scripts/run_next_batch.py` @ `f1a31b9` | Helper reading moved root files | retire (archive with the driver) or repoint or leave | `PlantLibrary_Server/archive/scripts/run_next_batch.py` | B4 / B3 | Q-A6V-04 |
| RC-A6V-05 | `PlantLibrary_Server/implementation/System_V1_Implementation/validation/README.md` @ `f1a31b9` | Manifest lists six expected files, omits five existing ones | refresh in place (add rows; never rename any file) | same path | B4 | — |
| RC-A6V-06 | `PlantLibrary_Server/docs/SV-*.md` (8 files, F-A6V-10) and the two stub READMEs | Broken `../PlantLibrary_Workspace` links; "empty scaffold" text | fix in place (one text sweep) | same paths | B3 or B2 | Q-A6V-05 |
| RC-A6V-07 | `PlantLibrary_Server/hygiene/CONSUMED_HYGIENE.md` @ `f1a31b9` | Pin at kit 0.2.1; re-pin only after K-7 ships | hold the pin; re-pin as its own D-entry if K-7 ships | same path | B3 | Q-G-06 |
| RC-A6V-08 | `PlantLibrary_Server/.claude/**`, `.codex/**` @ `f1a31b9` | 24 byte mirrors of the superproject | refreshed by B1 as mirrors; never hand-edited here | same paths (`.codex/**` per Q-G-09) | B1 | Q-G-09 |
| RC-A6V-09 | `PlantLibrary_Server/implementation/README.md` @ `f1a31b9` | Line 27 cites the held Workspace manifest path | one-line path edit when Workspace releases its set | same path | B3 (with Workspace M-9) | Q-G-06 |

## §4 Questions for the operator

| Id | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A6V-01 | What happens to the V1 `DRIVER_SCRIPT.md` (legacy; `_ACT_STATE.md` instructions at 21, 42, 61; `README.md:43,46-47`)? | (a) After B4 rewrites the README "How to run" and A7/B8 confirm instance 2 binds on `SCOPE.md` alone, `git mv` it to `archive/System_V1_Implementation/DRIVER_SCRIPT.md` and declare `archive` as `exempt-tree: legacy`. (b) Keep in place and add a one-line banner (GC-7053's smallest change). (c) Leave untouched. | Kit §1.9 says archive, never delete; D7 already made `SCOPE.md` the procedure; the file has no link citers (all prose by basename); the new path is declared once, so K-7 never applies. | B3 Server archive step; B4 README rewrite; B8 re-verification of the binding |
| Q-A6V-02 | Release the SERVER_V1_PROPOSAL hold in B3? | (a) Yes: `release` + `git mv` to `PROPOSAL_server-v1_2026-07-10.md`; sweep `README.md:6,60`, `CONTEXT_INDEX.md:10`, `STATE.md:15` (the STATE edit recorded by B4 as a package decision), the index line and a "Renamed" row. (b) Keep held until the GUI rework finishes. | The 2a/2b precondition is met; the only blockers are four in-repo lines B3/B4 own anyway; Workspace's citers are served by the Renamed table; no kit change is needed. | B3 hold-release step for Server (the same-repo writer follows B4's STATE.md pass) |
| Q-A6V-03 | The dashboard report's hold (code citers `app/api/routes/dashboard_support.py:2`, `app/workers/tasks.py:9`) and the dangling `app/core/metrics.py:4`: edit the docstrings in this program? | (a) No code edits in the rework; keep the hold; record one deferred row so the first resumed Server batch fixes the three docstrings and then releases. (b) Docstring-only edit in B3 (three comment lines), then release and move. | Policy A.0.5 routes code-cited names through a batch; a code edit would arrive without the standing-invariant evidence the package asks for. | `rework/REGISTER_deferred-validations_2026-10-13.md` row; Phase C |
| Q-A6V-04 | `scripts/run_next_batch.py` (reads moved root files, 9-cell parse): retire, repoint or leave? | (a) Retire with the driver: archive to `archive/scripts/`, drop the `README.md:10` row, once B4's hand-back replaces it. (b) Repoint to the V1 package and the 15-column schema. (c) Leave. | Run-batch and the Conductor already select the next batch; repointing re-implements a skill; (a) ends a script that cannot work today. | B4 hand-back step; B3 move |
| Q-A6V-05 | The `docs/SV-*.md` relative links (eight files) and the two "empty scaffold" READMEs: fix in the rework? | (a) Yes, one text sweep by B3 or B2 (`../../PlantLibrary_Workspace/…`; refresh the two stubs); product docs, no rename. (b) Leave. | Pure text; no citer changes; removes dead links before the corpus is cited by the new runbook. | B3 Server sweep |
| Q-A6V-06 | The setup guide: author it in the rework? | (a) No: leave `deploy/SETUP_GUIDE.md` to row `SV-OPS-INSTALL-01` (its verification needs the live stack); add a deferred-validation row; no D-entry is needed because `deploy/` is outside every root. (b) Draft now and verify later. | The row already homes it (`TASK_CHECKLIST.md:52`); an unverified install guide is worse than none; the no-test rule applies. | `rework/REGISTER_deferred-validations_2026-10-13.md`; B4 hand-back text |

Q-G-05 and Q-G-06 evidence for Server is in §7.3; neither needs a further question here.

## §5 Reusable things this brief did not name

- `PlantLibrary_Server/hygiene/HYGIENE_DECISIONS.md:203-313` (D-2026-09-17-01 and -02): a worked example of a re-pin plus a rename-with-hold-release entry, with preconditions measured, numbered dispositions and a "Verify after" line; B3 can use the shape for every repository's release entry.
- `PlantLibrary_Server/implementation/System_V1_Implementation/planning/INDEX.md:21-25` and `proposal/INDEX.md:20`: the "Renamed <date>" table with a **held** row is the proven way to serve frozen citers; reuse it for every release.
- `PlantLibrary_Server/tests/test_repo_hygiene_kit.py` and `.github/workflows/repo-hygiene.yml` carry the checker as one test node and in CI (wrapper declared `yes`, `CONSUMED_HYGIENE.md:16`); the rework never invokes them.
- The checker is silent on files outside declared roots; §7.1 is the only classification of `docs/` (11), the mirrors (19) and the package folder (8). B3 may copy the row set into `rework/REGISTER_conductor-reuse-candidates_2026-10-13.md` as pointers.
- `docs/local_android_test_environment.md` is cited by superproject skills (`.claude/skills/android-validation/SKILL.md:34,47`, `.claude/skills/verify-stack/SKILL.md:21,30`), AndroidApp (`OidcConfig.kt:31`, `network_security_config.xml:3`) and Dashboard (`implementation/System_V1_Implementation/TASK_CONTEXT.md:291`): any lane that rewrites those skills (A1/B1/B5) must keep the path.
- `implementation/README.md:39-45` (the Conductor paragraph) is the onboarding step 3 note; B8 should check its Server copy against the live binding (`onboarding/REGISTER_package-census_2026-09-15.md:92`).

## §6 Claims to verify

1. **K-7 touches Server in exactly one directive.** Check (under one minute): `git -C C:\Programmierung\SW_Development\PlantLibrary_Server grep -n -E "^- (exempt-tree|exempt-subfolder):" -- hygiene/HYGIENE_DECISIONS.md` must print one line (109, `implementation/MVP`); then `sed -n 446,451p C:\Programmierung\SW_Development\PlantLibrary_Server\scripts\hygiene\repo_hygiene_check.py` must show the `target.exists()` test with no `release` branch for trees.
2. **`README.md` is a further `_ACT_STATE.md` instruction site beside DRIVER_SCRIPT 7/21/42/61.** Check: `git -C C:\Programmierung\SW_Development\PlantLibrary_Server grep -n "_ACT_STATE" -- implementation/System_V1_Implementation/README.md implementation/System_V1_Implementation/DRIVER_SCRIPT.md` must print line 47 for README.md and lines 7, 21, 42, 61 for DRIVER_SCRIPT.md.
3. **`app/core/metrics.py:4` cites a document that exists nowhere.** Check: `git -C C:\Programmierung\SW_Development\PlantLibrary_Server ls-files -- "*SV-DEPLOY-HARDEN*"` prints nothing, while `git -C C:\Programmierung\SW_Development\PlantLibrary_Server grep -n "SV-DEPLOY-HARDEN-01" -- app` prints `app/core/metrics.py:4`.

## §7 Deliverables

### §7.1 Disposition table

Class legend: live; superseded (by what); archive; frozen / pinned / generated (which). "Citers" lists the references that bear on a move; mirror and README rows are summarised. Line numbers are at `f1a31b9`.

| File or folder (n) | Class | Citers | Hold / exemption (D-id) and release | Disposition (keep / archive to <path> / retire / hold) | Reason |
|---|---|---|---|---|---|
| `PlantLibrary_Server/.claude/agents/*.md` (3) | pinned (byte mirror of the superproject; parity-checked) | `CLAUDE.md:89-93`; superproject `scripts/harness/check_harness_parity.py` | none declared; checker ignores (outside roots) | keep; B1 refreshes as mirror | never edited here; 24 of 24 blobs equal the superproject's |
| `PlantLibrary_Server/.claude/skills/**/*.md` (8: plan-batch, real-stack-testing + 2 refs, run-batch, test-driven-development + 1 ref, validate-real-stack) | pinned (mirror) | same | none | keep; B1 | as above |
| `PlantLibrary_Server/.codex/skills/**/*.md` (8) | pinned (mirror; fate per Q-G-09) | `AGENTS.md:34-43` | none | keep; B1 per Q-G-09 | frozen-not-mirrored under Q-G-09 (a) |
| `PlantLibrary_Server/AGENTS.md` (1) | live | `.codex` runtime; `hygiene/HYGIENE_DECISIONS.md:75` | rule block parity (`AGENTS.md:45-62`) | keep; B2 reconciles | Codex section interacts with Q-G-09 |
| `PlantLibrary_Server/CLAUDE.md` (1) | live | superproject `IMPLEMENTATION_PLAN.md:156,349`; `repo-hygiene/PROMPT_kit-bootstrap-session_2026-09-15.md:125` | rule block `:133-149`; "Deliverable naming" pointer (`D-2026-09-16-02`, no directive) | keep; B2 reconciles | `_ACT_STATE` mention at `:81` is the deprecation, correct |
| `PlantLibrary_Server/README.md` (1) | live (partly stale) | none outside the repo | exempt by name (kit) | keep; B2/B3 refresh rows `:7-15` | lists `scripts/run_next_batch.py` (F-A6V-07), omits hygiene/openapi |
| `PlantLibrary_Server/app/README.md`, `tests/README.md` (2) | live (stale stub) | none | exempt by name | keep; refresh (Q-A6V-05) | "empty scaffold" (F-A6V-11) |
| `PlantLibrary_Server/deploy/README.md` (1) | live | none | exempt by name | keep | the only deploy prose; guide row `SV-OPS-INSTALL-01` pending |
| `PlantLibrary_Server/docs/README.md` (1) | live | `hygiene/HYGIENE_DECISIONS.md:289-290` (mapping note) | exempt by name | keep | already points at the moved write-ups |
| `PlantLibrary_Server/openapi/README.md` (1) | live | none | exempt by name | keep | `:12` already swept to the AUDIT path |
| `PlantLibrary_Server/docs/SV-AUTH-01_auth_design.md` (1) | live (code-cited design note) | `app/api/routes/auth.py:2`, `app/core/config.py:38`, `app/core/security.py:3`; `docs/SV-PROFILE-01_profile_plan.md`; Dashboard `docs/WD-AUTH-01_session_strategy.md`; Workspace `prompts/reference/SETUP_ANDROID_TEST_ENVIRONMENT_PROMPT.md` | catalogued, not declared (`HYGIENE_DECISIONS.md:111-115`) | keep in place; fix links (F-A6V-10) | code citers: must not move |
| `PlantLibrary_Server/docs/SV-SYNC-01_sync_protocol_notes.md` (1) | live (code-cited) | `app/api/routes/sync.py:2`; `repo-hygiene/REGISTER_target-corpus-census_2026-09-15.md`; the AUDIT file | catalogued | keep in place; fix links | code citer |
| `PlantLibrary_Server/docs/SV-{BOOT-02,CONFLICT-01,CRUD-01,DOMAIN-01,GARDEN-01,MEDIA-01,PROFILE-01}_*.md` (7) | live (MVP-era design notes, id-prefixed) | frozen `implementation/MVP/package/TASK_CONTEXT.md` only; CONFLICT and CRUD also the AUDIT file | catalogued (kit §1.7) | keep in place; fix links where F-A6V-10 applies | descriptive, row-anchored; no live citer forces a move |
| `PlantLibrary_Server/docs/SV-B07_dashboard_endpoint_coverage_report.md` (1) | live-held (MVP-era report snapshot) | code `app/api/routes/dashboard_support.py:2`, `app/workers/tasks.py:9`; frozen `implementation/MVP/package/STATE.md:49,182`; Workspace `MVP_Reconciliation/00_SOURCE_INVENTORY.md:59` | `held-name` `D-2026-09-16-01` (`HYGIENE_DECISIONS.md:142`), kept at M-3 (`:279-282`); release: a code edit in a batch (A.0.5) | hold; on release `git mv` to `planning/AUDIT_sv-b07-dashboard-endpoint-coverage_2026-07-05.md` | Q-A6V-03; invisible to the checker's `held:` count |
| `PlantLibrary_Server/docs/local_android_test_environment.md` (1) | live runbook | `scripts/seed_android_test_environment.py:3`; AndroidApp `OidcConfig.kt:31`, `network_security_config.xml:3`; superproject skills `android-validation`, `verify-stack`; Workspace skill; Dashboard `TASK_CONTEXT.md:291` | `exempt-name` `D-2026-09-16-01` (`HYGIENE_DECISIONS.md:131`), never released | keep; never rename | code, config and skill citers |
| `PlantLibrary_Server/hygiene/CONSUMED_HYGIENE.md`, `HYGIENE_DECISIONS.md` (2) | live (kit-owned; decisions append-only) | rule block in `CLAUDE.md`/`AGENTS.md`; superproject track runbook | pin kit 0.2.1 | keep; B3 appends | never edited retroactively |
| `PlantLibrary_Server/implementation/README.md` (1) | live | none outside; cites the Workspace manifest at `:27` | exempt by name | keep; one-line fix owed at Workspace release (F-A6V-09) | |
| `PlantLibrary_Server/implementation/MVP/**` (10: `package/` 8, `evidence/` 1, `handoffs/` 1) | frozen | `CLAUDE.md:76`; V1 `CONTEXT_INDEX.md:38`, `SCOPE.md:16`, `README.md:12-17`; AndroidApp frozen `STATE.md:482`; Workspace `MANIFEST_Server.csv:10,11` | `exempt-tree` frozen `D-2026-09-16-01` (`HYGIENE_DECISIONS.md:109`); no release possible; a move is K-7-blocked | keep in place | terminal evidence; never bound, never edited |
| `…/System_V1_Implementation/{BATCH_PLAN,TASK_CHECKLIST,TASK_CONTEXT}.md` (3) | live (package schema files) | Conductor instance 2 binding (`onboarding/REGISTER_package-census_2026-09-15.md:92`); superproject `IMPLEMENTATION_PLAN.md:37`; Workspace `SUITE_HANDOFFS.md:26,43,56` | none; not in a root | keep; B4 edits | one writer: B4 |
| `…/System_V1_Implementation/STATE.md` (1) | live (append-only log; header stale) | the hold note in `proposal/INDEX.md:20`; Workspace V1 `SUITE_HANDOFFS.md`; Workspace `00_V1_SYSTEM_PROPOSAL.md` | `STATE.md:15` is the hold citer (`HYGIENE_DECISIONS.md:139`) | keep; B4 appends; the line-15 edit only with Q-A6V-02 (a) | |
| `…/System_V1_Implementation/SCOPE.md`, `CONTEXT_INDEX.md` (2) | live | Conductor intake; `CLAUDE.md:78-88`; `AGENTS.md:26` | none | keep; B4 | SCOPE replaces DRIVER_SCRIPT for the hard scope |
| `…/System_V1_Implementation/README.md` (1) | live, superseded in part ("How to run") | `implementation/README.md:35-37` | exempt by name | keep; B4 rewrites "How to run" and drops the `_ACT_STATE` lines | F-A6V-05 |
| `…/System_V1_Implementation/DRIVER_SCRIPT.md` (1) | superseded (by `SCOPE.md` + run-batch); legacy | prose mentions only (F-A6V-05); `onboarding/…runbook:934` | none; outside every root | archive to `PlantLibrary_Server/archive/System_V1_Implementation/DRIVER_SCRIPT.md` after B4 (Q-A6V-01); hold until then | "kept, superseded, not deleted" (`STATE.md:233-234`); onboarding forbids deleting it (`…runbook:361`) |
| `…/handovers/INDEX.md`, `planning/INDEX.md`, `proposal/INDEX.md` (3) | live (index) | checker | INDEX exempt | keep; B3 appends lines | `handovers/` has no deliverable yet |
| `…/planning/{AUDIT_sv-contract-01-contract-validation_2026-07-04, EVIDENCE_sv-b07-runtime-verification_2026-07-05, EVIDENCE_sv-b08-deployment-hardening_2026-07-05}.md` (3) | archive-grade, final (MVP-era evidence in a live root) | frozen MVP `STATE.md:181,183`, `TASK_CONTEXT.md:190,201,225`; SharedContracts frozen MVP `BATCH_PLAN.md:83`, `TASK_CHECKLIST.md:19`, `TASK_CONTEXT.md:130`; `openapi/README.md:12`; Workspace frozen trees | none (released at M-3, `HYGIENE_DECISIONS.md:307-308`); old names served by `planning/INDEX.md:21-25` | keep | compliant names; in a declared root |
| `…/proposal/SERVER_V1_PROPOSAL.md` (1) | live (binding scope; the package's authority) | in-repo `STATE.md:15`, `README.md:6,60`, `CONTEXT_INDEX.md:10`; Workspace `00_V1_SYSTEM_PROPOSAL.md:222`, `VERIFICATION_REPORT.md:57` | `held-name` `D-2026-09-16-01` (`HYGIENE_DECISIONS.md:139`); release: 2a/2b done, then M-9 (`:279-280`) | hold now; release in B3 to `PROPOSAL_server-v1_2026-07-10.md` (Q-A6V-02) | the checker's one `held:` line |
| `…/validation/README.md` (1) | live (manifest, stale) | none | catalogued (kit §1.7) | keep; B4 refreshes (RC-A6V-05) | F-A6V-08 |
| `…/validation/{SV1-B00_VGAP-005_sync_push, SV1-B00_partial_validation, SV1-B00_profile_sync_record, SV1-B00_refdata_decision, SV1-B06_oidc_local}.md` (5) | live evidence (batch-keyed; cited from other repositories) | Workspace `MVP_VALIDATION_GAP_LOG.md:114,134,140,155`, `SYSTEM_ACCEPTANCE_REPORT.md:21,52`; AndroidApp `AN-B13…:28`, `AN1-B14_oidc_local.md:21` | catalogued, not a root | keep; never rename | outside citers use the path |

Count check: 3+8+8+1+1+1+2+1+1+1+1+1+7+1+1+2+1+10+3+1+2+1+1+3+3+1+1+5 = 72 (28 rows).

Nothing in Server is tracked as generated markdown. The OpenAPI file is generated YAML (`openapi/plantlibrary.openapi.yaml`, produced by `scripts/export_openapi.py`, per `openapi/README.md:3-5`) and is not a census item.

### §7.2 Holds and exemptions (every directive line)

| Line | Directive | Value | State | Release condition |
|---|---|---|---|---|
| `PlantLibrary_Server/hygiene/HYGIENE_DECISIONS.md:109` | `exempt-tree` (class `frozen`) | `implementation/MVP` | active, permanent | none by design; the path cannot move until K-7 (F-A6V-01) |
| `:131` | `exempt-name` | `docs/local_android_test_environment.md` | active, permanent | none (live runbook, cited by code and skills) |
| `:139` | `held-name` | `implementation/System_V1_Implementation/proposal/SERVER_V1_PROPOSAL.md` | **active**; the checker's only `held:` line | onboarding 2a/2b migrated Server (done), then M-9; in practice `STATE.md:15` and three further lines are swept in the commit of the `git mv`; target `PROPOSAL_server-v1_2026-07-10.md` |
| `:140` | `held-name` | `docs/SV-B07_runtime_verification_report.md` | released at `:307` (`D-2026-09-17-02`), file moved | none left |
| `:141` | `held-name` | `docs/SV-B08_deployment_hardening_report.md` | released at `:308` (`D-2026-09-17-02`), file moved | none left |
| `:142` | `held-name` | `docs/SV-B07_dashboard_endpoint_coverage_report.md` | **active**; not reported by the checker (outside roots) | a code edit in a batch changing `app/api/routes/dashboard_support.py:2` and `app/workers/tasks.py:9` (A.0.5), then `release`; target `planning/AUDIT_sv-b07-dashboard-endpoint-coverage_2026-07-05.md` |
| `:307` | `release` | `docs/SV-B07_runtime_verification_report.md` | done at M-3 | — |
| `:308` | `release` | `docs/SV-B08_deployment_hardening_report.md` | done at M-3 | — |

Entries with no directive line: `D-2026-09-16-02` (`:170-201`, says so at `:196`) and `D-2026-09-17-01` (`:205-230`, says so at `:227-228`). Pin facts (`hygiene/CONSUMED_HYGIENE.md:11-19`): kit `0.2.1`, modules none (root-allowlist off, scratch off), test-wrapper yes, rule block on, no launcher, prompt-file floor 0. Roots (`:25-27`): `planning` (standard), `proposal` (standard), `handovers` (date-anywhere), all under `implementation/System_V1_Implementation/`.

Active directives: 4 (`:109`, `:131`, `:139`, `:142`); released: 2 (`:140`, `:141` by `:307`, `:308`).

### §7.3 Archive layout proposal

**Options for Server.**
1. Top-level `archive/` declared `exempt-tree: legacy` (the kickoff's A6 default). The checker ignores files outside roots, so the declaration only gives the census a "legacy" table; no root-allowlist entry is needed because the module is off (`CONSUMED_HYGIENE.md:15`).
2. In-place exempt-tree lines for each legacy file. For Server this adds nothing (DRIVER_SCRIPT.md, the other candidate, is outside every root), and each such line would be a new K-7 exposure if the file later moves.
3. Nothing: keep every file where it is.

**Recommendation.** Option 3 for everything except Q-A6V-01 (a): when and only when the operator approves retiring DRIVER_SCRIPT.md (and, per Q-A6V-04, the run_next_batch script), create `archive/` with exactly those files and one directive on the folder. Do not move `implementation/MVP` (frozen, already declared in place, K-7-blocked, and cited by live prose: `CLAUDE.md:76`, `AGENTS.md:24`, `README.md:15-21`, `implementation/README.md`, `CONTEXT_INDEX.md:38`, `SCOPE.md:16`). Declare the new tree once, at its final path, so a later move never arises.

**What K-7 limits (two sentences).** A path already named by an `exempt-tree` or `exempt-subfolder` line can never be moved or renamed on kit 0.2.1, because the checker re-tests its existence and no `release` ends the declaration; in Server that is only `implementation/MVP`. Every other Server file can move today, a held name releases by `git mv` under K-6, and a set folder held as a whole (K-7's second gap) does not arise in Server.

**D-entry B3 would write** (id: next free `D-2026-10-<dd>-nn` by grep; the next free today would be `D-2026-10-13-01`, to be re-verified at execution):

```text
## 2026-10-13 — rework: archive and release (Server)

### D-2026-10-13-01 — PlantLibrary_Server: SERVER_V1_PROPOSAL released; legacy driver archived

Authority: step B3 of rework/PROMPTS_master-rework-runbook_2026-10-13.md; the operator's answers to
Q-A6V-01 and Q-A6V-02 (verbatim, with date). Preconditions measured: checker verdict before; the citing
lines of SERVER_V1_PROPOSAL.md swept (STATE.md:15, README.md:6,60, CONTEXT_INDEX.md:10); DRIVER_SCRIPT.md
prose mentions listed. Dispositions: git mv proposal/SERVER_V1_PROPOSAL.md -> proposal/PROPOSAL_server-v1_2026-07-10.md;
git mv implementation/System_V1_Implementation/DRIVER_SCRIPT.md -> archive/System_V1_Implementation/DRIVER_SCRIPT.md.
Commit line: rework: B3 - PlantLibrary_Server hold released; legacy driver archived

- release: implementation/System_V1_Implementation/proposal/SERVER_V1_PROPOSAL.md — Q-A6V-02 (a); moved by git mv to proposal/PROPOSAL_server-v1_2026-07-10.md in this commit
- exempt-tree: archive — legacy; retired files kept for the record (DRIVER_SCRIPT.md, Q-A6V-01 (a)); never edited, never renamed
```

**INDEX lines B3 would write.**
- `implementation/System_V1_Implementation/proposal/INDEX.md`: replace the held line (`:11`) by `- 2026-07-10 · PROPOSAL_server-v1_2026-07-10.md · PROPOSAL · final · the Server MVP→V1 suite proposal (binding scope, gap dispositions); released from hold 2026-10-13 (D-2026-10-13-01)`; add a `## Renamed 2026-10-13` section with row `| SERVER_V1_PROPOSAL.md | PROPOSAL_server-v1_2026-07-10.md — hold released (D-2026-09-16-01, D-2026-10-13-01) |`, keeping the existing 2026-09-17 table.
- `archive/` is not a declared root, so no INDEX line is required; add `archive/README.md` (exempt by name) with one row per file, its origin path and the D-id.

**Q-G-06 evidence for Server.** (i) One exposed directive: `HYGIENE_DECISIONS.md:109`, tested at `repo_hygiene_check.py:446-451`. (ii) Verdict today is `pass with holds — 0 violations, 1 held`; an `implementation/MVP` move would turn it into a `record` violation that no later entry can clear. (iii) Everything the rework wants to move in Server (the proposal, the driver, one script) avoids that path. (iv) Hence Q-G-06 (a) — record the need, hold the affected set, queue the kit session — has no cost in Server; (b) "work around inside TARGET" would need an edit of line 109 (the record is append-only, `HYGIENE_DECISIONS.md:3-5`) or a stub left at the old path, and neither is available. (v) The MVP tree has a second reason to stay: live files cite it (`CLAUDE.md:76`, `AGENTS.md:24`, `README.md:15-21`, `implementation/README.md:6-28`). If K-7 ships and the operator later wants it archived, the entry is a `release` of the old tree path plus a new `exempt-tree: archive/MVP — frozen` in the same entry, after re-pinning to the new kit.

### §7.4 Checker

Verdict line of `check`, run from `PlantLibrary_Server` on `f1a31b9`:

`repo-hygiene: pass with holds — 0 violations, 1 held` (preceded by the one `held:` line for `implementation/System_V1_Implementation/proposal/SERVER_V1_PROPOSAL.md`, date-divergence note included).

Per-root totals of `census`:

| Root | Totals line |
|---|---|
| `implementation/System_V1_Implementation/planning` (planning, standard) | totals: 4 files, 3 compliant, 0 candidates, 1 exempt, 0 held, 0 set folders |
| `implementation/System_V1_Implementation/proposal` (proposal, standard) | totals: 2 files, 0 compliant, 0 candidates, 1 exempt, 1 held, 0 set folders |
| `implementation/System_V1_Implementation/handovers` (handovers, date-anywhere) | totals: 1 files, 0 compliant, 0 candidates, 1 exempt, 0 held, 0 set folders |
| repository | totals: 7 files, 3 compliant, 0 candidates, 3 exempt, 1 held, 0 set folders |

Exempt-tree table: the 10 files of `implementation/MVP` (8 in `package/`, 1 in `evidence/`, 1 in `handoffs/`), all class `frozen`. The census sees 7 + 10 = 17 of the 72 tracked `.md` files; the other 55 are classified here only (package schema files, product notes, hygiene records, mirrors).
