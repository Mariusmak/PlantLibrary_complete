# Operator questions — PlantLibrary master rework (register of record)

*Opened 2026-10-13 at `R-0` by the orchestrating session (`PROMPT_master-rework-kickoff_2026-10-13.md` §2 rule 7).
A question never blocks the program: a step that depends on one is marked `waits Q-…` in the runbook's §3 and
skipped until the answer is recorded here verbatim with its date; every other step proceeds. The operator session
(runbook §O) walks the open rows in dependency order, records the answers verbatim, flips the state and commits.
The runbook's §Q mirrors this table; this file is the register of record.*

## How to read a row

| Column | Meaning |
|---|---|
| ID | `Q-<lane>-<nn>`; `G` is the program lane (seeded by the kickoff prompt §4), `A1`…`A9`, `B1`…`B8`, `C1` the lanes that raise one |
| Question | What the operator decides, in plain words |
| Options | `(a)` is always the recommendation; others follow |
| Why (a) | The reasoning for the recommendation, short |
| Waits | The runbook steps marked `waits Q-…` on this row |
| State | `open` · `answered` · `withdrawn` |
| Answer (verbatim, date) | The operator's words, unedited, with the date; `(a)` alone means "as recommended" |

## Questions

| ID | Question | Options | Why (a) | Waits | State | Answer (verbatim, date) |
|---|---|---|---|---|---|---|
| `Q-G-01` | Where the Design Configuration lives | (a) `SharedContracts/design/` as the one Configuration, each client pinned to it through its own `design/conformance/CONSUMED_DESIGN.md` and consuming generated stack artifacts; (b) one `design/` per client | One canon (tokens 1.2.0 "field-ledger", `P-DS-01..10`) already lives in SharedContracts; three copies would drift, and the Kit's anchoring is built for a consumer pinned to one Configuration | `B5` (import, gate, anchoring); `B6` reads it | open | |
| `Q-G-02` | Repository structure | (a) keep the superproject with six submodules; (b) consolidate into fewer repositories | Instance 2's bindings, the six GitHub remotes and the hygiene pins are all per repository; a consolidation is a program of its own and nothing in the transfer needs it | `A8` recommends; `B3` and `B4` assume (a) | open | |
| `Q-G-03` | Pushing | (a) no session pushes; the operator pushes at the end of each wave from the operator session; (b) each lane pushes its branch fast-forward after every commit | Four parallel writers and gitlink bumps are safest with one pair of hands at the remote; nothing downstream reads the remotes during the program | every write lane (standing rule) | open | |
| `Q-G-04` | Mechanical checks allowed in Phase B | (a) linters, formatters, type checks and the Kit's static checks only; (b) also compile steps (web build, Gradle compile) when the machine is idle | The one test slot is the Conductor's; a compile is not a test but holds CPU and disk, and the Kit's static checks already prove token conformance | `B5`, `B6`, `B7` | open | |
| `Q-G-05` | Stale sequencers | (a) `IMPLEMENTATION_PLAN.md` and `WORKSPACE_STATE.md` archived once `B4`'s hand-back section replaces them, `Todo.md`'s live ideas moved into a REGISTER under `rework/` and the file emptied; (b) keep and refresh them | Two sequencers dated July and August contradict the packages' own `STATE.md`; one hand-back section with the packages as truth removes the contradiction instead of maintaining it | `B3` (archive), `B4` (hand-back section) | open | |
| `Q-G-06` | Hygiene kit finding K-7 (an exempt tree cannot retire on rename) | (a) record the need, hold the affected set, and queue a separate Kit session for the operator; (b) work around it inside TARGET | The pilot's rule G-08 and the kit's own contract: a kit defect is patched in the kit, never papered over in a consumer; the hold costs nothing until M-9 | `B3` (M-9 release of the Workspace restructure set) | open | |
| `Q-G-07` | The design-adoption skill | (a) retire it in favour of the Kit's design-gate once `B5` anchors the three clients, leaving a pointer; (b) keep both | Two gates over the same canon with different wording will disagree; design-gate reads the Configuration the clients are pinned to | `B5` (last step), `B1` (skill set) | open | |
| `Q-G-08` | GUI rework order | (a) all three clients planned, Dashboard implemented first, Android and PyApp as soon as their stacks are proven emittable; (b) all three implemented in parallel from the start | The Kit's only proven stack is web-css; Compose and Qt emission is `A4`'s open item, so implementing them first would build on an unproven emitter | `B6` (implementation order) | open | |
| `Q-G-09` | Codex | (a) freeze as the Conductor did: `.codex/**` and `AGENTS.md` kept, never deleted, not mirrored, the parity checker comparing them against the freeze commit; (b) remove the Codex mirrors | The Conductor's `D-2026-10-02-23` is the proven pattern; deleting mirrors breaks nothing today but loses the option of a Codex session, and the freeze is reversible | `B1` (mirrors), `B2` (`AGENTS.md`), `B7` (parity checker) | open | |
