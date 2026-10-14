# Unplanned backlog — PlantLibrary master rework (register of record)

*Opened 2026-10-13 at step `B3-2` of `PROMPTS_master-rework-runbook_2026-10-13.md` (§3.5), on the answers `Q-G-05`
(a) and `Q-A6S-04` (a). It holds what the two stale sequencers carry and no batch package does: the backlog of
`IMPLEMENTATION_PLAN.md` §7 (`:358-376`), its operator decisions of §5 (`:271-314`), and the live ideas of the
git-ignored `Todo.md`. `Todo.md` is not edited (decision P3 of 2026-07-15, `Q-A6S-04` (a)); its ideas are cited by
line and reduced to one line each, and no body text is copied. `IMPLEMENTATION_PLAN.md` stays in place until `B3-6`
archives it after the hand-back. Line numbers are those of `IMPLEMENTATION_PLAN.md` at `4b2027d` and of `Todo.md` as
read on 2026-10-13 (280 lines). `C1-2` points the hand-back section here (§H.3 for §3 of this file, §H.4 for §1 and
§2), and `C1` turns each row that needs it into `plan-batch` work in its suite. This file is a register, not a plan:
it schedules nothing.*

## How to read a row

| Column | Meaning |
|---|---|
| ID | `UB-<nn>`, in order of recording |
| Source | `file:line` of the item; a second citation marks the same idea in the other source |
| Item | The idea in one line |
| Target · nearest home | The suite that would carry it, and the nearest existing batch or row |
| State at `4b2027d` | What exists today, measured by grep in the suite packages |
| Needs | `needs plan-batch in <suite>`, an operator decision, or nothing, and what `C1` does with it |

## 1. Backlog without batch rows (`IMPLEMENTATION_PLAN.md` §7)

| ID | Source | Item | Target · nearest home | State at `4b2027d` | Needs |
|---|---|---|---|---|---|
| `UB-01` | `IMPLEMENTATION_PLAN.md:366`; `Todo.md:123` | No cleartext-HTTP exception on Android; plan HTTPS | AndroidApp · `AN1-B09`, beside `AN-V1-SEC-01` | Unhomed: `git -C PlantLibrary_AndroidApp grep -i cleartext -- implementation/System_V1_Implementation` prints nothing | needs plan-batch in AndroidApp (release-path security); check the server-side TLS counterpart when the row is planned |
| `UB-02` | `IMPLEMENTATION_PLAN.md:367`; `Todo.md:110` | Detailed setup guide for the server | Server · `SV-OPS-INSTALL-01` (`SV1-B06`) | Half-homed: the row names `deploy/SETUP_GUIDE.md` among its outputs (`TASK_CHECKLIST.md:52`); `Q-A6V-06` (a) leaves the authoring to that row | needs plan-batch in Server only to widen `SV-OPS-INSTALL-01` from "single setup guide" to a full operator guide; otherwise the row is its home |
| `UB-03` | `IMPLEMENTATION_PLAN.md:368`; `Todo.md:30-32` | Remove the Gradle features that break Gradle 9 | AndroidApp · `AN1-B09` | Unhomed: no row names Gradle 9; the build works today (forward-compatibility debt) | needs plan-batch in AndroidApp |
| `UB-04` | `IMPLEMENTATION_PLAN.md:369`; `Todo.md:91` | Server-side data enrichment inside the plant-creation flow | Server · near `SV-V1-SEARCH-01`, `SV-V1-PROVIDER-01`, `SV-V1-JOBS-01`, `SV-V1-REVIEW-01` | Partly homed by those rows; a proposal exists and is unapproved: `PlantLibrary_Workspace/docs/proposals/PROPOSAL_enrichment-v2_2026-07-10.md` (`RC-A6W-11`) | operator decision on the proposal, then needs plan-batch in Server (and in the clients that show the creation flow) |
| `UB-05` | `IMPLEMENTATION_PLAN.md:370` | Follow-through of the Fable 5 business/GTM proposal (`BDEV-01`…`06`) | Workspace · `docs/PROPOSAL_fable5-business-gtm_2026-07-11/` (the plan names it by its old folder `fable5_business_proposal/`) | Nothing approved; independent of V1 | operator decision first; needs plan-batch in Workspace only for approved items |
| `UB-06` | `IMPLEMENTATION_PLAN.md:371`; `Todo.md:76` | Old MVP folders: keep them read-only, do not delete | Workspace and every suite's frozen MVP tree | Settled in practice: the MVP/V1 split (restructure D1-D10, 2026-07-16) and the suites' frozen `exempt-tree` declarations keep them; deleting would break the evidence chain the V1 registers cite | no plan-batch: a standing rule; `C1` states it once in §H.5 and closes the row unless the operator reopens it |

`IMPLEMENTATION_PLAN.md:373-374` also recommends running `fewer-permission-prompts` once (also `Todo.md:185-190`). That
is a tooling act on the superproject's `.claude/` settings, not product backlog; it is listed under §4.

## 2. Live ideas of `Todo.md` not already in §1

`Q-A6S-04` (a) admits the live ideas the census estimated (`AUDIT_corpus-census-superproject_2026-10-13.md`,
F-A6S-03, start lines 34, 76, 91, 94, 123, 195, 201). Lines 76, 91 and 123 are the same ideas as `UB-06`, `UB-04` and
`UB-01`, and lines 30-32 and 110 the same as `UB-03` and `UB-02`; the rest follow.

| ID | Source | Item | Target · nearest home | State at `4b2027d` | Needs |
|---|---|---|---|---|---|
| `UB-07` | `Todo.md:34` | Build parts that sit under SharedContracts are excluded from git (noted under the Android build) | SharedContracts and AndroidApp | Unhomed; which files are meant is not recorded | operator names the files, then needs plan-batch in SharedContracts (and AndroidApp if its build reads them) |
| `UB-08` | `Todo.md:94` (again `:102`) | A prioritised audit of what would make the app more valuable to users | Workspace (system level) | Answered once, unapproved: `PlantLibrary_Workspace/docs/PROPOSAL_fable5-product-strategy-v1_2026-07-11/` and `…-v2_2026-07-11/` (function catalogue and its reconciliation) | operator decision on the proposal; then needs plan-batch per suite for each approved item |
| `UB-09` | `Todo.md:195` | A security-assessment proposal before the final release | Workspace · `SY1-B07` (`SY1-SEC-01`), with Server `SV-V1-SEC-01` (`SV1-B06`) | Partly homed: the `/security-review` triage row and the security gate row exist; anything wider than that triage has no row | operator decides whether the two rows suffice; if not, a proposal first, then needs plan-batch in Workspace |
| `UB-10` | `Todo.md:201` | Backup scripts for whole folders under `C:\Backups` | Outside the seven repositories (`C:\Backups`); the in-repo row Server `SV-OPS-BACKUP-01` covers only the server's data backup | The note says the scripts were built; one interactive run (UAC) by the operator is outstanding | no plan-batch (an operator act outside TARGET); see the proposed `Q-B3-01` in the `B3-2` report |

## 3. Operator decisions (`IMPLEMENTATION_PLAN.md` §5), for `C1`'s `Q-` entries

| ID | Source | Item | Target · nearest home | State at `4b2027d` | Needs |
|---|---|---|---|---|---|
| `UB-11` | `IMPLEMENTATION_PLAN.md:276-292` | `SDA-DEC-01`…`05`: SharedContracts folder layout, PyApp token inversion, parity capture, icon set, Android font policy | Workspace · `implementation/System_Design_Architecture/` | Overtaken: accepted as recommended at onboarding G1/D5 (2026-09-15), then overtaken by `Q-G-01` (a) in the form of `Q-A4-01` (a) and by `Q-A7-06` (a); the package's `STATE.md` decisions table reads "overtaken 2026-10-13" for all five (Workspace `764c11f`, `B4-3`); the design choices now sit in the Configuration (`B5`, gate `G-DS`) | no `Q-` entry; `C1` lists it in §H.3 as closed |
| `UB-12` | `IMPLEMENTATION_PLAN.md:294-301` | `AN-V1-SEC-01`: a named sign-off: keep the DataStore token storage as an accepted deviation, or implement Keystore | AndroidApp · `AN1-B09`; gates `AN1-B10` → `SY1-B04` → release | Open: the row is `gated`; `Q-A6A-03` (a) keeps `docs/security_token_storage_acceptance.md` held until it resolves | `C1`: a `Q-` entry for the operator (release-blocking, rule `SYS-QUAL-GAP-004`) |
| `UB-13` | `IMPLEMENTATION_PLAN.md:302-304` | `SV-V1-SEC-01` → `SY1-B07`: a named sign-off on every accepted or deferred `/security-review` finding | Server · `SV1-B06`; Workspace · `SY1-SEC-01` | Open: `SV-V1-SEC-01` is `todo`, `SY1-SEC-01` `gated`; the sign-off is owed once the triage exists | `C1`: a `Q-` entry, asked when the triage file exists (release-blocking) |
| `UB-14` | `IMPLEMENTATION_PLAN.md:306-314` | Confirm `VGAP-020`/`SD-GAP-008` (PyApp `data_source`/tags first sync) as V1 scope before `SV1-B00` | Server `SV-SYNC-REFDATA-01`, SharedContracts `SC1-B00`, PyApp `PY-V1-REFDATA-01` | Deferred out of MVP into V1 by the operator on 2026-07-15; no confirmation recorded since | `C1`: a `Q-` entry before `SV1-B00` runs (it sizes that batch) |

## 4. `Todo.md` lines read and not admitted

Cited by line only. "Done" means the work the block asks for exists in the repositories today.

| Lines | Reading | Why not a row |
|---|---|---|
| `1-28` | MVP-era prompts (Android and Workspace batches, MVP validation) | Done: MVP closed 2026-07-15 |
| `37-50` | Design architecture first, MVP gap reconciliation, V1 proposal rewrite, skills | Done: V1 packages and skills exist |
| `53-73` | Fable 5 notes and the V1-proposal prompt | Done: the V1 proposals exist |
| `78` | Retrieve skills from earlier chats | Done: skills authored |
| `80` | A link about having Fable write skills | Ambiguous; proposed `Q-B3-01` |
| `84-88` | Fold old Android proposal content into the V1 proposal | Ambiguous; proposed `Q-B3-01` |
| `92` | An instruction to improve a prompt | Not an idea |
| `95`, `98-102` | Restructure (MVP/V1 split), design system improvement | Done: restructure D1-D10; design system approved; `:102` is `UB-08` |
| `105` | Enable skills for Codex | Superseded: Codex frozen (`Q-G-09`) |
| `114-117` | The "no constraints" recommendations (two surfaces, auth, provider roster, scaffolding) | Ambiguous; Keycloak and the 20 providers stay (operator, 2026-07-10); proposed `Q-B3-01` |
| `119-120` | Re-check the MVP integration checklist for open tasks | Ambiguous; proposed `Q-B3-01` |
| `127-152` | Validation proposal; the V1 wave order and model roles | Done or superseded: validation methodology approved; the order lives in the packages and §H.2 |
| `156-181` | Skill assessment | Done: the skills it recommends are installed |
| `185-190` | Run `fewer-permission-prompts` (also `IMPLEMENTATION_PLAN.md:373-374`) | A tooling act on `.claude/` settings, not product backlog; whether it ran is not recorded |
| `196` | Follow `IMPLEMENTATION_PLAN.md` | Instruction; superseded by this program |
| `236-253` | Design analysis and template creation | Done: the Design Template Initiative and the rework's `B5` |
| `257-280` | The origin prompt of this program | In progress as the master rework itself |

## 5. Findings recorded by the lanes (wave 3 onward)

Rows the lane sessions surfaced that are product backlog for a package owner, not program work; each is also a
`Q-` row's answer. The `State` cell names the commit the finding was measured at.

| ID | Source | Item | Target · nearest home | State | Needs |
|---|---|---|---|---|---|
| `UB-15` | `B6b-2` census (`Q-B6b-07`), AndroidApp `e9ac4a8` `implementation/Design_Migration_V1/current_state/Function_UI_Census.md` | Three dead repository operations with no caller: `AuthRepository.isLoggedIn`, `MediaRepository.getPendingUploads`, `GardenRepository.observeMembershipsForUser` | AndroidApp · the V1 package (`implementation/System_V1_Implementation`), nearest a cleanup row of `AN1-B09` | Unhomed; "leave what you did not make" — reported, never deleted in passing | needs plan-batch in AndroidApp |
| `UB-16` | `B6b-3` contracts, AndroidApp `c02f9bb` (`implementation/Design_Migration_V1/screen_requirements/`) | Four code findings left unedited: `Routes.kt:34-41` `bottomNavDestinations` unused (a second copy of the tab order); `Routes.kt:4-6` cites a Cross_Platform_Strategy proposal that no longer exists; `describeRecency` duplicated three times (`HomeViewModel.kt:118`, `PlantsScreen.kt:73`, `MoreScreen.kt:106`); capture errors silently discarded at `CameraCaptureScreen.kt:102-105` | AndroidApp · the V1 package; the tab-order copy and the route citation nearest `B6b-6`'s IA (Q-A9A-05), the other two a cleanup row of `AN1-B09` | Unhomed; reported, never edited in passing | needs plan-batch in AndroidApp (the IA step may claim the first two) |
| `UB-17` | `B6b-4` gap map (`Q-B6b-10`), AndroidApp `e6247a7`, F-A9A-13 remainder | 98 user-facing `Text("…")` literals in the Compose screens; `strings.xml` holds only `app_name` (no string resources, no localisation) | AndroidApp · the V1 package; nearest a quality row of `AN1-B09` | Unhomed; no Configuration rule and no V1 row asks for string resources | needs plan-batch in AndroidApp |
| `UB-18` | `B6c-3` contracts, PyApp `de5551d` (`implementation/Design_Migration_V1/screen_requirements/`) | Dead GUI code found by the contract writers, recorded not removed: `_ImagesTab`, `_ImportExportTab`, `_LocationTreeWidget`, `LocationActionRow`, unused `domain_colors` groups, `_toggle_sidebar`, `_navigate_to_settings`, `_placeholder_action_messages`, the `filtersVisible` QSS rule; added at B6c-4: `PlaceholderView` (`app/gui/views/placeholder_view.py:9`) | PyApp · the V1 package; nearest a cleanup row of its last batch | Unhomed; reported, never deleted in passing | needs plan-batch in PyApp (the re-skin batches may claim the QSS rule) |
| `UB-19` | `B6b-5` information model (`Q-B6b-12`), AndroidApp `762bc1e` (`Forward_Surface.md` FS-C5, `Information_Model.md` IM-Q1, `Settings_Inventory.md` §3) | (1) list queries not scoped to the active garden (`FieldActionsDao.kt:22`, `PlantInstanceDao.kt:22`), no Room cache clear on garden switch or logout (`AuthRepository.kt:102-105`); (2) Tasks groups on the UTC day and marks overdue once the due instant passes (`TasksViewModel.kt:54-63`); (3) `base_url` has two editors (`LoginViewModel.kt:124`, `SettingsViewModel.kt:106`) and a duplicated default literal (`ApiServerConfig.kt:9`, `LoginViewModel.kt:165`) | AndroidApp · the V1 package rows `AN-V1-CARE-01`, `-HOME-01`, `-SETTINGS-01` (anchor notes at `B6b-7`); runtime check DV-B6b-04 | Unhomed; static reads, reported not edited | needs plan-batch in AndroidApp |
| `UB-20` | `B6a-5` information model (`Q-B6a-12`), Dashboard `6eca8eb` (`Information_Model.md` §5–§6) | Server / SharedContracts findings: the SharedContracts OpenAPI snapshot lacks `GardenLocationOut.parent_location_id`, which the Server already returns (`PlantLibrary_Server/app/api/schemas.py:73`; the pending export SV-OPENAPI-01 is behind); no client creates a garden (seed script only); `client_device.last_seen_at` is never written; the sign-in callback answers failures with raw JSON on the API origin; the location parent is not settable, no photo listing operation, no snooze or planting date in REST, no change timestamps or actor exposed (P-1…P-8); added at B6a-7a: D-2 `delete_location` leaves its plants and sub-locations pointing at it (`locations.py:121-139`), D-3 `delete_plant_instance` leaves the plant's open tasks listed (`plants.py:234-252`, `tasks.py:99-107`) — each with an assertion in the Dashboard's `PROPOSAL_web-v1-scope-amendment_2026-10-14.md` §5 | Server · `SV-OPENAPI-01` and the V1 package; SharedContracts · the next export | Unhomed beyond SV-OPENAPI-01; the GUI lane writes no Server row | needs plan-batch in Server and SharedContracts (B6a-7 adds the per-item rows) |
| `UB-21` | `B6c-5` forward surface (`Q-G-c-1-03/05/08`), PyApp `cac2e5f` (`Forward_Surface.md` §6–§10) | The unowned PyApp forward behaviours: the seven Settings controls disabled with a reason (Units, auto-fetch on add, image download policy, startup reminder, due-date horizon, automatic backups and their scheduler, backup frequency); per-plant sync markers from the outbox; 16 contract features plus 5 controls with no operation or owner (Statistics export and time range, bulk assignment, task edit, …); added at B6c-6a: PDF export (LP-15), update checks (LP-16), a user guide (Q-B6c-17), "Clear cache" (V-10 §8 #7) and "Open folder" after a backup (D-06), tag merge and the count on deletes (D-07, D-19), a server auto-merge section (D-11) and per-type structured editors (D-12), visible lightbox zoom controls (D-18), a "due soon" Dashboard band (V-02 §8 #7, S-19); G-c-1 answered (a) 2026-10-14 | PyApp · the V1 package; nearest its last planned batch | Unhomed; no row and no Configuration rule asks for them | needs plan-batch in PyApp |
| `UB-22` | `B9-3` proposal (`Q-B9-29`, `Q-B9-24`, `Q-B9-28`), Workspace `8125384` (`02_PROPOSAL.md` findings) | The sync-identity defect S-18: a synced location create drops the client's `sync_id` and its parent (`PlantLibrary_Server/app/api/routes/sync.py:237-238`); the PyApp pushes local integer ids in reference fields (`sync_hooks.py:116-128`, `sync_service.py:510-520`) which the Server cannot parse — locations and plants created on the desktop would not keep their identity on the Server | Server + PyApp V1 sync rows (`SV1`/`PY1` sync batches) | read at Server `0e491d3`, PyApp `47d2ffc`; not run | a plan-batch amendment naming the rows; a real-stack test of a desktop-created location round trip |
| `UB-23` | `B9-3` proposal (`Q-B9-29`, `Q-B9-24`, `Q-B9-28`), Workspace `8125384` (`02_PROPOSAL.md` findings) | The web's REST writes are last-write-wins: read models carry no `server_version` and PATCH has no base check (`schemas.py:68-104`, `locations.py:96-118`, `plants.py:205-231`) | Server V1 / the planner's SCGP1-B01 (Q-B9-24) | read at Server `0e491d3` | a contract decision (Q-B9-24 at G-gp-1) |
| `UB-24` | `B9-3` proposal (`Q-B9-29`, `Q-B9-24`, `Q-B9-28`), Workspace `8125384` (`02_PROPOSAL.md` findings) | Contract wording vs. Server: `operations.yaml:25` and `:64-71` specify a Server-assigned create id and a field-level auto-merge the Server does not implement | SharedContracts + Server (`sync-contracts` conformance) | read at SharedContracts `bc37a0e` | the V1 sync rows or SVGP1-B03 (Q-B9-28) |
| `UB-25` | `B6b-7a` classification (`Q-B6b-24`), AndroidApp `c11052d` (`Change_Classification.md`) | The server's conflict values the phone shows are not the contract's (a successor to UB-20's SharedContracts gap: the conflict record's value shapes) | Server / SharedContracts (`sync-contracts` conformance) | read at AndroidApp `28101da`, Server `0e491d3` | a contract reading at the next contract wave |
