# Skills and agents — lane A1 (read-only analysis, 2026-10-13)

*Lane A1 of the PlantLibrary master rework, Phase A (`PROMPT_master-rework-kickoff_2026-10-13.md` §3 `R-1`). Read-only:
nothing was edited outside this file; no test, build or install ran. Pins read: SOURCE-C `Orchestrator_System` `main`
`2e7adb3` (its working tree carries uncommitted edits to `CLAUDE.md` and two package files, none under `.claude/`,
`.codex/`, `.agents/` or `scripts/harness/`); Design_Template_Kit `f08e588` (Kit 1.7.0); Repo_Hygiene_Template_Kit
0.2.1; TARGET superproject `8702e0a`, Workspace `6b4b88b`, PyApp `35ddc63`, AndroidApp `5d6410f`, Dashboard `7795fc8`,
Server `f1a31b9`, SharedContracts `d43f7a2`. Source paths are absolute; TARGET paths are prefixed with the repository
name (`SW_Development/` for the superproject). The one command run beyond reads: `python
scripts/harness/check_harness_parity.py` from `C:\Programmierung\SW_Development` → `harness parity: pass`, exit 0.*

## §0 Summary

1. **run-batch: adapt, not adopt.** §1–§5 and §8 are byte-identical in both copies; §7 differs by one paragraph (newline rule, adopt). §6 is the whole delta: the Conductor collapsed PlantLibrary's 171-line validation algorithm into one command, `scripts/harness/closeout.py` (3,402 lines, reads the Conductor instance config and imports `conductor.batch_package`). No TARGET suite has `closeout.py`; only PyApp has the older harness the 408-line text needs. Verbatim adoption breaks every closeout in all six suites (Q-A1-01).
2. **plan-batch 1.4.0 → 1.5.1: adapt.** Take two of the three new §7 items verbatim. The third (`closeout.py --predict`) waits on the same harness decision.
3. **Agents: adopt the three shared Conductor agents.** Their edits are project-neutral: Opus for the closeout reviewer, the "before you report" and judge-against-contract paragraphs, and the foreground rule. `real-stack-validator` also needs `BASH_MAX_TIMEOUT_MS`. `v5-section-reader` does not transfer.
4. **New Conductor skills.** The three Kit skills come only through the Kit installer (B5). `impeccable` is already identical (3.8.0, auto-mode fixed). `instance-sync` is retired as Conductor-only. `harness-upkeep` and `scratch-gate` are adapted at B7. The four third-party-derived skills (`code-quality-review`, `security-audit`, `pathfinder`, `dependency-audit`) carry Conductor paths and need a licence and installation decision (Q-A1-02).
5. **Skill discovery gap (critical).** Discovery does not cross from a suite to the superproject (onboarding audit). Yet suite rows name skills their suite does not carry: `android-validation`, `verify-stack`, `sync-contracts`, `design-adoption` and `webapp-testing` (Q-A1-04). PyApp's `gui-validation` pointer does not resolve.
6. **The parity checker does not do what the instructions claim.** It compares only the superproject's `.claude` and `.codex` trees. The suites' CLAUDE.md say it checks their mirrors. The superproject's `.agents/README.md` is a stale Conductor text describing checks this checker lacks.
7. **The Codex freeze collides with the kits.** The Conductor freezes `AGENTS.md` whole-file, so its design-kit block is stuck at Kit 0.8.0 while CLAUDE.md is at 1.3.1. In TARGET the hygiene checker enforces CLAUDE.md↔AGENTS.md block parity. A whole-file freeze here therefore fails at the first kit re-pin, so the TARGET shape must freeze AGENTS.md *outside* the marked blocks. This is evidence for Q-G-09.
8. **Settings.** TARGET's protective deny list is in untracked `settings.local.json` files, with no PowerShell twins. The superproject's local file even allows `cat .env`. The Conductor tracks the deny list (Bash + PowerShell) and `BASH_MAX_TIMEOUT_MS` in `settings.json` (Q-A1-03).
9. **ui-ux-pro-max must stay in the superproject.** The Kit wizard's fallback path is `c:/Programmierung/SW_Development/.claude/skills/ui-ux-pro-max`.
10. **Questions raised:** Q-A1-01 (run-batch §6 shape), Q-A1-02 (third-party skills), Q-A1-03 (tracked settings), Q-A1-04 (mirror the PlantLibrary-only skills into the suites whose rows name them).

## §1 Coverage

| Item | Status | Reason / what was skipped |
|---|---|---|
| SOURCE-C `.claude/skills/code-quality-review/` (SKILL.md 12, references/python-anti-patterns.md 292, LICENSE) | partly read | SKILL.md whole; the reference listed, not read (MIT, Python-only by name) |
| SOURCE-C `.claude/skills/dependency-audit/` (SKILL.md 168, NOTICE, scripts/collect.py 1568, model.py 402, render.py 809, sources.py 683) | partly read | SKILL.md :1-50 and NOTICE whole; scripts listed, not read (unmodified Trail of Bits) |
| SOURCE-C `.claude/skills/design-audit/SKILL.md` (203) | partly read | head :1-40 and headings; byte-identical to the Kit's `anchoring-kit/skills/design-audit/SKILL.md` apart from CRLF (diff 0 lines) |
| SOURCE-C `.claude/skills/design-gate/SKILL.md` (202) | partly read | head :1-40 and headings; identical to the Kit copy apart from CRLF |
| SOURCE-C `.claude/skills/gallery-governance/SKILL.md` (210) | partly read | head :1-40 and headings; identical to the Kit copy apart from CRLF |
| SOURCE-C `.claude/skills/harness-upkeep/SKILL.md` (52) | read | — |
| SOURCE-C `.claude/skills/impeccable/` (SKILL.md 167, reference/ 30 files, scripts/ ~65 files) | partly read | trees diffed against PyApp/AndroidApp (`diff -rq --strip-trailing-cr`: identical); version line and the bypass-flag grep read; references and scripts not read |
| SOURCE-C `.claude/skills/instance-sync/SKILL.md` (77) | read | — |
| SOURCE-C `.claude/skills/pathfinder/` (SKILL.md 119, LICENSE, NOTICE) | partly read | SKILL.md :1-60; LICENSE/NOTICE not read |
| SOURCE-C `.claude/skills/plan-batch/SKILL.md` (260) | read | headings, :1-20 and :185-260 read; diffed whole against TARGET |
| SOURCE-C `.claude/skills/real-stack-testing/` (SKILL.md 93, references/gui-testing.md 17, metered-validation.md 12) | read | SKILL.md :1-60 read and diffed whole; references are byte-identical to TARGET (md5) |
| SOURCE-C `.claude/skills/run-batch/SKILL.md` (282) | read | whole |
| SOURCE-C `.claude/skills/scratch-gate/SKILL.md` (68) | read | — |
| SOURCE-C `.claude/skills/security-audit/` (SKILL.md 24, NOTICE, 13 references) | partly read | SKILL.md whole; references listed, not read |
| SOURCE-C `.claude/skills/systematic-debugging/` (SKILL.md 282, 3 references, LICENSE) | read | diffed whole against TARGET with CR stripped |
| SOURCE-C `.claude/skills/test-driven-development/` (SKILL.md 311, writing-good-tests.md 203, LICENSE) | partly read | SKILL.md diffed whole; writing-good-tests.md :1-12 only |
| SOURCE-C `.claude/skills/validate-real-stack/` (SKILL.md 39, scripts/run_validation.ps1 50) | read | byte-identical to TARGET (md5) |
| SOURCE-C `.claude/agents/` (4) | read | all four whole |
| SOURCE-C `.agents/README.md` (119) | read | whole |
| SOURCE-C `.agents/skills/` (4 Kit folders), `.codex/**` (4 toml, hooks.json, hooks/deny_git_commands.mjs, 9 skill folders) | partly read | listed; shared mirrors hash-compared against TARGET; impeccable not re-read |
| SOURCE-C `.claude/settings.json`, `.claude/settings.local.json` | read | both whole; local file untracked (global ignore) |
| SOURCE-C `scripts/harness/check_harness_parity.py` (824) | partly read | :1-300 and :560-660; the proposal-fact and section-map checks (:342-560) and the self-test bodies were not read |
| SOURCE-C decision `D-2026-10-02-23` (`implementation/Conductor_V2/STATE.md:44146-44230`) | read | whole entry (a)–(l); freeze commit `10177e3` confirmed |
| TARGET superproject `.claude/skills` (13 folders) | partly read | run-batch, plan-batch, design-adoption whole. real-stack-testing, TDD and systematic-debugging diffed. verify-stack's delta read. gui-validation (375), android-validation (255), sync-contracts (96), ui-ux-pro-max (377 + scripts + data) and webapp-testing (113) read by description and checklist usage only |
| TARGET superproject `.claude/agents` (3) | read | diffed whole against the Conductor |
| TARGET superproject `.claude/settings.json`, `settings.local.json` | read | — |
| TARGET superproject `.codex/**` (59 tracked files) and `.agents/README.md` (86) | read | `.codex` hash-compared; README read whole |
| TARGET superproject `scripts/harness/check_harness_parity.py` (133) | read | whole; ran it (pass) |
| PlantLibrary_Workspace `.claude/`, `.codex/` (55 / 12 tracked) | read | hash-compared; verify-stack's delta read |
| PlantLibrary_PyApp `.claude/` (111), `.codex/` (13), `.agents/` (100), `.github/skills` (97) | partly read | hash-compared; gui-validation pointer, settings.local.json and `.codex/hooks.json` read; impeccable compared by tree diff |
| PlantLibrary_AndroidApp `.claude/` (108), `.codex/` (12), `.agents/` (99), `.github/skills` (96) | partly read | hash-compared; CLAUDE.md :58-90 read |
| PlantLibrary_Dashboard, PlantLibrary_Server, PlantLibrary_SharedContracts `.claude/`, `.codex/` (12 / 12 each) | read | hash-compared; no `.agents/` |
| Added: Kit `anchoring-kit/INSTALL.md` :12-61, :87-132 | partly read | the impeccable and rule-block sections only |
| Added: Kit `anchoring-kit/skills/{design-migration,design-wizard}` | not read | listed only (218 / 268 lines); A4's lane |
| Added: Kit `wizard/lib/axes-to-tokens.mjs:62`, Kit `README.md:65-80` | partly read | the ui-ux-pro-max fallback chain |
| Added: Hygiene Kit `checker/repo_hygiene_check.py` :54, :715-732 (same lines in `SW_Development/scripts/hygiene/repo_hygiene_check.py`) | partly read | block-parity check only |
| Added: `SW_Development/onboarding/AUDIT_skill-assumptions_2026-09-15.md` :86-171 | partly read | the discovery measurement |
| Added: SOURCE-C `scripts/harness/closeout.py` (3402), `src/conductor/execution_table.py` :525-560, :755-775, `tests/test_run_batch_skill_contract.py` (19), `docs/harness/closeout.md` (grep) | partly read | dependency and contract lines only |
| Added: the six suite TASK_CHECKLIST.md files (skill-column grep), suite CLAUDE.md harness lines | partly read | grep only |
| Added: `PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md:17-19, :42` | partly read | ui-ux-pro-max verdict F3 |

Counts: 18 read, 20 partly read, 1 not read (39 rows).

## §2 Findings

**F-A1-01 — run-batch differs only in §6 and one §7 paragraph.** Lines 1–155 of both files are identical. §8 is identical (Conductor :241-282 = TARGET :367-408). §7 gains one paragraph in the Conductor (`C:\Programmierung\Orchestrator_System\.claude\skills\run-batch\SKILL.md:199-202`, commit `ab49005`, CD2-B412). §6 shrank from `SW_Development/.claude/skills/run-batch/SKILL.md:156-326` (171 lines) to `C:\Programmierung\Orchestrator_System\.claude\skills\run-batch\SKILL.md:156-195` (40 lines). The 408/282 delta is entirely §6 minus the new paragraph. Detail in §7.2.

**F-A1-02 — The Conductor's §6 depends on a harness no PlantLibrary suite has.** The Conductor's §6 item 2 makes `python scripts/harness/closeout.py --package … --batch …` the only closeout (`…\run-batch\SKILL.md:174-190`). Its real-stack-testing item 7 says the same (`…\real-stack-testing\SKILL.md:40-45`). Its plan-batch §7 calls `closeout.py --predict` (`…\plan-batch\SKILL.md:208-215`).

`closeout.py` is Conductor-bound:
- 3,402 lines;
- reads `C:\Programs\AI_Orchestrator\config.yaml` (`C:\Programmierung\Orchestrator_System\scripts\harness\closeout.py:67`);
- uses `conductor.batch_package.parse_package` (`:114`).

TARGET has no `closeout.py` anywhere. Only `PlantLibrary_PyApp/scripts/harness/` holds the older harness (`regression_scope.py`, `run_validation.py`, `run_chunks.py`, `reclaim_scratch.py`, `scope_cap.py`; `PlantLibrary_PyApp/CLAUDE.md:344-349`). The other five suites have no `scripts/harness/`. So the current 408-line text is executable only in PyApp, and the Conductor text would be executable nowhere.

**F-A1-03 — The Conductor coordinator has a closeout route that runs `closeout.py` in the project.** `closeout_handoff_clause` tells a worker to run `python scripts/harness/closeout.py handoff …` and append its `CONDUCTOR_CLOSEOUT_HANDOFF:` line. The coordinator re-runs the same command and refuses on disagreement (`C:\Programmierung\Orchestrator_System\src\conductor\execution_table.py:762-775`; shape check `:531-560`). Whether instance 2 uses that route for PlantLibrary decides whether every suite needs a `closeout.py`. That belongs to A7/A8/B8; it gates Q-A1-01.

**F-A1-04 — plan-batch 1.4.0 → 1.5.1 is a three-item §7 change.**
- The version comment changed: `SW_Development/.claude/skills/plan-batch/SKILL.md:8` → `C:\…\plan-batch\SKILL.md:8-11`.
- The `cites:` premise item gained "no `cites:` target under `implementation/*/validation/`" (`C:\…\plan-batch\SKILL.md:204-207`, D-2026-10-04-04 (g)).
- The 1.4.0 cap item (`SW_Development/.claude/skills/plan-batch/SKILL.md:202-205`) became the `closeout.py --predict` budget item (`C:\…\plan-batch\SKILL.md:208-215`).
- A proof-surface item was added (`C:\…\plan-batch\SKILL.md:216-218`; 1.5.0, F-7).

Nothing else differs (`diff` exit 1 on exactly these hunks).

**F-A1-05 — The three shared agents gained project-neutral hardening in the Conductor.**
- `batch-closeout-reviewer`: `model: opus`, `maxTurns: 30`, and a "Before you report" paragraph (`C:\…\.claude\agents\batch-closeout-reviewer.md:4,7,30-39`). TARGET has `sonnet` and 20 (`SW_Development/.claude/agents/batch-closeout-reviewer.md:4,7`).
- `batch-plan-auditor`: `effort: high`, `maxTurns: 24`, and a "Judge each artifact against its contract" paragraph (`C:\…\batch-plan-auditor.md:5-7,39-47`). TARGET has `medium` and 12.
- `real-stack-validator`: NotebookEdit disallowed, `maxTurns: 16`, and a foreground paragraph capped at 3,600,000 ms (`C:\…\real-stack-validator.md:6-7,18-21`).

The Opus choice is operator answer e.7 (`C:\Programmierung\Orchestrator_System\implementation\Conductor_V2\STATE.md:44152-44156`).

**F-A1-06 — `real-stack-validator`'s 3,600,000 ms timeout needs an env setting TARGET lacks.** The Conductor sets `BASH_MAX_TIMEOUT_MS: 3600000` in tracked `settings.json` (`C:\Programmierung\Orchestrator_System\.claude\settings.json:2-4`, commit `e21e7f0`). No TARGET repository has it: `SW_Development/.claude/settings.json:1` is `{}`, and the suites have no `settings.json`. Adopting the agent text without the env promises a timeout the Bash tool refuses.

**F-A1-07 — Discovery does not cross from a suite to the superproject.** Measured at onboarding: from `PlantLibrary_PyApp` and `PlantLibrary_Server`, none of the superproject's 13 skills appear (`SW_Development/onboarding/AUDIT_skill-assumptions_2026-09-15.md:125-128, 169-171`). Yet suite rows name skills the suite does not carry:
- `android-validation:capture` (`PlantLibrary_AndroidApp/implementation/System_V1_Implementation/TASK_CHECKLIST.md:27`);
- `design-adoption:android` (`:48`);
- `verify-stack` (`:58`);
- Dashboard: `verify-stack`, `design-adoption` and `webapp-testing` (`PlantLibrary_Dashboard/implementation/System_V1_Implementation/TASK_CHECKLIST.md:26, 36, 42`);
- PyApp: `verify-stack`, `sync-contracts` and `design-adoption` (`PlantLibrary_PyApp/implementation/System_V1_Implementation/TASK_CHECKLIST.md:26, 35, 37`);
- `sync-contracts` (`PlantLibrary_Server/implementation/System_V1_Implementation/TASK_CHECKLIST.md:27`; `PlantLibrary_SharedContracts/implementation/System_V1_Implementation/TASK_CHECKLIST.md:18-19`).

run-batch §4 item 4 says such a row is never done unless the command ran (`SW_Development/.claude/skills/run-batch/SKILL.md:77-81`). Every one of these rows is therefore unexecutable by a worker whose cwd is the suite. The opposite direction does work in this session's Claude Code: the session listing offered `PlantLibrary_AndroidApp:plan-batch` and the other suite skills as scoped skills when working from the superproject. A superproject session therefore sees duplicate names. This is an observation from the session's skill listing, not a measurement.

**F-A1-08 — PyApp's `gui-validation` pointer does not resolve.** It cites `../../.claude/skills/gui-validation/SKILL.md` (`PlantLibrary_PyApp/.claude/skills/gui-validation/SKILL.md:14-19`). From the file's folder that resolves to `PlantLibrary_PyApp/.claude/.claude/…`, which is absent. The correct relative path is `../../../../.claude/skills/gui-validation/SKILL.md` (verified with `ls`). A standalone PyApp clone has no target at all. The same 38-line pointer is in `.agents/` and `.github/` (`PlantLibrary_PyApp/.agents/skills/gui-validation/SKILL.md`, `PlantLibrary_PyApp/.github/skills/gui-validation/SKILL.md`).

**F-A1-09 — The superproject parity checker checks one repository only, yet five suite CLAUDE.md files say it checks theirs.** `compare_trees` reads `root/.claude/skills` and `root/.codex/skills` of the superproject only (`SW_Development/scripts/harness/check_harness_parity.py:58-85`, root at `:36-39`). The suite CLAUDE.md say their mirrors are "checked by its `scripts/harness/check_harness_parity.py`" (`PlantLibrary_AndroidApp/CLAUDE.md:59-63`; the same at `PlantLibrary_Dashboard/CLAUDE.md:55` and `PlantLibrary_PyApp/CLAUDE.md:329`).

The cross-repository identity was a one-time byte compare at onboarding step 3 (`SW_Development/onboarding/PROMPTS_conductor-onboarding-runbook_2026-09-15.md:471-472`). It holds today: all 24 mirrored files and 3 agents hash-equal across the seven repositories, and the aggregate `.codex` mirror hash `f68a2f0c` is equal in all seven. Nothing re-checks it.

**F-A1-10 — The superproject's `.agents/README.md` is a stale copy of the Conductor's.**
- It describes checks the local checker lacks: the shared-block diff and the v5 facts (`SW_Development/.agents/README.md:10-20`).
- It lists `v5-section-reader`, which TARGET does not carry (`:36`).
- It lists only 4 bridged skills (`:24-29`) while `.codex/skills` mirrors 13.
- It writes `../.Claude` (`:3, :26-29`).
- It speaks as the Conductor about "relocating" skills to the PlantLibrary workspace (`:62-68`).
- It names `CLAUDE.md`/`AGENTS.md` markers this repository does not use (`:84-86`).

**F-A1-11 — The Conductor's Codex freeze, as built.**
- Decision: `D-2026-10-02-23` (c) (`C:\Programmierung\Orchestrator_System\implementation\Conductor_V2\STATE.md:44166-44175`).
- Operator rule (b) 1: "no step edits `.codex/**`, `AGENTS.md`'s runtime section or a Codex agent definition, and no act mirrors a `.claude` edit" (`:44159-44161`).
- Freeze commit: `10177e3`, the decision commit itself.
- Checker: `FROZEN_AT = "10177e3"`, 15 LF-normalized SHA-256 digests for every non-Kit `.codex` file, and `FROZEN_AGENTS_DIGEST` for `AGENTS.md` (`C:\Programmierung\Orchestrator_System\scripts\harness\check_harness_parity.py:54-77`).
- Exemptions: the four Kit folders, `settings.local.json` and `__pycache__` (`:204-210`).
- AGENTS.md may differ only by the inserted F-01 notice line (`:238-272`, notice text `:56-58`).
- `check_all` runs the two frozen checks in place of the tree and shared-block compares (`:629-642`).
- The unfreeze recipe is in the docstring (`:21-26`) and in `.agents/README.md` (`C:\Programmierung\Orchestrator_System\.agents\README.md:9-11`).
- Bridge rows were flipped to `frozen` (`:28-32`), and a "Claude-only skills" table records every post-freeze skill (`:47-60`).

**F-A1-12 — A whole-file AGENTS.md freeze has already let rule blocks drift in the Conductor and would fail TARGET's hygiene checker.** The Conductor's frozen `AGENTS.md` carries its design-kit block at `Kit … @ 0.8.0` (`C:\Programmierung\Orchestrator_System\AGENTS.md:187`). Its live `CLAUDE.md` carries `@ 1.3.1` (`C:\Programmierung\Orchestrator_System\CLAUDE.md:231`).

TARGET's `AGENTS.md` files all carry the hygiene block (`SW_Development/AGENTS.md:16`, each suite's `AGENTS.md` at `:30`, PyApp `:494`, Server `:45`). TARGET's hygiene checker requires that block to equal CLAUDE.md's (`SW_Development/scripts/hygiene/repo_hygiene_check.py:54, 725-732`). The Design Kit installer also writes a `design-kit` block into `AGENTS.md` (`C:\Programmierung\Design_Template_Kit\anchoring-kit\INSTALL.md:42`), which B5 will do in three suites.

A Conductor-shaped freeze in TARGET therefore either:
- blocks every hygiene-kit and design-kit re-pin, or
- turns the hygiene checker red at the first re-pin.

**F-A1-13 — The Kit skills are identical everywhere they exist and are Kit-owned.**
- The Conductor's `design-gate`, `design-audit` and `gallery-governance` equal `C:\Programmierung\Design_Template_Kit\anchoring-kit\skills\*\SKILL.md` apart from CRLF.
- The Kit installs them byte-for-byte into `.claude`, `.codex`, `.agents` and `.github` (`…\anchoring-kit\INSTALL.md:36-38`).
- The Conductor edits them "only through the Kit" (`C:\Programmierung\Orchestrator_System\.agents\README.md:88-94`).
- None exists in TARGET today.
- `design-gate` refuses to run without a Configuration (`…\design-gate\SKILL.md:33-40`), so installing it before B5's Configuration is BINDING produces a gate that only says "no Configuration".

**F-A1-14 — impeccable is the same 3.8.0 tree in the Conductor, PyApp and AndroidApp.**
- `diff -rq --strip-trailing-cr` is clean between `PlantLibrary_PyApp/.claude/skills/impeccable` and `C:\Programmierung\Orchestrator_System\.claude\skills\impeccable`.
- The bypass flags are gone in all six TARGET copies (PyApp `35ddc63`, D-2026-10-02-20 mirrored).
- PyApp/AndroidApp `.agents/skills/impeccable` carry 3 extra Codex agent files (99 files vs 96) and a 173-line SKILL.md.
- `.github/skills/impeccable/SKILL.md` is 165 lines. The Conductor has the 167-line SKILL.md in all four mirrors.
- PyApp wires the Claude hook in a tracked `settings.local.json` (`PlantLibrary_PyApp/.claude/settings.local.json:9-24`) and the Copilot hook in `PlantLibrary_PyApp/.github/hooks/impeccable.json`.
- AndroidApp has the skill but no hook configuration at all.
- Dashboard, which is the first GUI client in Q-G-08 (a), has no impeccable.

**F-A1-15 — design-adoption is the unparameterized predecessor of design-gate.** `design-gate` says it was "Authored … as the parameterised form of the house design-adoption gate" and that "if a value ever appears in this file, that is the defect" (`C:\…\design-gate\SKILL.md:8-16`). `design-adoption` states values: `#22C55E`, `#16A34A`, `#4ADE80`, `PRIMARY.600 #2A7A30`, `PRIMARY.400 #74BC85` (`SW_Development/.claude/skills/design-adoption/SKILL.md:71-74`). It also hard-codes its adoption rows (`:55-61`). It lives only in the superproject and the Workspace, while the client rows that name it are in Dashboard, AndroidApp and PyApp (F-A1-07). This is the evidence for Q-G-07.

**F-A1-16 — ui-ux-pro-max is load-bearing for the Kit wizard.** The Kit's third fallback root for the wizard's style/typography/chart CSVs is `c:/Programmierung/SW_Development/.claude/skills/ui-ux-pro-max` (`C:\Programmierung\Design_Template_Kit\wizard\lib\axes-to-tokens.mjs:62`; chain at `C:\Programmierung\Design_Template_Kit\README.md:65-80`). PlantLibrary decided it is "not adopted" for V1 product audits and reserved for non-product surfaces (`PlantLibrary_Workspace/implementation/System_V1_Implementation/proposal/02_VALIDATION_METHODOLOGY_DECISIONS_2026-07-10.md:17-19, 42`). No checklist row names it.

**F-A1-17 — TDD and systematic-debugging: the Conductor made them headless-safe but Python/PowerShell-specific.**
- TDD (`C:\…\test-driven-development\SKILL.md`, OP-SK-A, D-2026-10-04-11):
  - "Delete it" becomes "set aside, uncommitted; never delete committed product or package files" (:39, :238).
  - Exceptions are recorded, never asked (:25), since a headless session cannot ask.
  - Real code means substitution at a process boundary (:105).
  - "Why Order Matters" is folded into the rationalization table, and `testing-anti-patterns.md` is replaced by `writing-good-tests.md`.
  - A LICENSE is added.
  - The examples are now pytest/PowerShell (:111-112, :245-262), while PlantLibrary's TDD rows are in Server (Python, 13 references) and the skill is mirrored into Kotlin and TypeScript suites.
- systematic-debugging:
  - "ask your human partner" and "attempt fix #4 after discussion" become "mark the row blocked; never attempt fix #4".
  - A secrets-presence-only PowerShell example is added.
  - The upstream marketing section is removed; a LICENSE is added.
  - PlantLibrary's copy keeps two upstream assets the Conductor dropped (`condition-based-waiting-example.ts`, `find-polluter.sh`).
  - The PlantLibrary copy's "Related skills" names a "verify" skill this repository does not have (`SW_Development/.claude/skills/systematic-debugging/SKILL.md`, the hunk `285,296d282` of the CR-stripped diff).

**F-A1-18 — Codex hooks: superproject identical, PyApp a different hook, other suites none.** `SW_Development/.codex/hooks.json` and `.codex/hooks/deny_git_commands.mjs` are byte-identical to the Conductor's frozen pair (md5 equal). Its description claims to mirror `.claude/settings.local.json`'s deny list (`SW_Development/.codex/hooks.json:2`), which is an untracked file. PyApp's `.codex/hooks.json` is an impeccable hook pointing at `.agents/skills/impeccable/scripts/hook.mjs` (`PlantLibrary_PyApp/.codex/hooks.json:2-10`). The other five suites have no `.codex/hooks.json`.

**F-A1-19 — Protective settings are untracked in TARGET.**
- Superproject: the 14-entry Bash deny list lives in `SW_Development/.claude/settings.local.json:7-22`, which is ignored by the user's global gitignore (`**/.claude/settings.local.json`). The same file allows `Bash(cat .env)` (`:5`). The tracked `settings.json` is `{}`.
- The Conductor tracks 28 deny entries, Bash plus PowerShell twins (`C:\Programmierung\Orchestrator_System\.claude\settings.json:5-35`; D-2026-10-03-21, `5ac4e13`).
- No suite has a deny list.
- PyApp's tracked `settings.local.json` (force-added) allows a script that no longer exists: `Improvements/GUI_Improvements_V3/select_v3_batch.py` is absent (`PlantLibrary_PyApp/.claude/settings.local.json:6`).
- Onboarding measured that an untrusted suite folder ignores `settings.local.json` allows (`SW_Development/onboarding/AUDIT_skill-assumptions_2026-09-15.md:130-132`).

**F-A1-20 — The Workspace carries a stale `verify-stack`.** `PlantLibrary_Workspace/.claude/skills/verify-stack/SKILL.md` has 149 lines against the superproject's 188. It lacks the "Client environments" section (`SW_Development/.claude/skills/verify-stack/SKILL.md:49-86`). The other five Workspace-only skills are byte-identical to the superproject's.

**F-A1-21 — The Conductor pins its run-batch commit contract by a test.** `C:\Programmierung\Orchestrator_System\tests\test_run_batch_skill_contract.py:7-19` asserts the "Propose the commit — never mutate Git" strings in both mirrors. That text is identical in TARGET (`SW_Development/.claude/skills/run-batch/SKILL.md:346-365`), so it transfers safely. TARGET has no such guard: a B7 candidate, recorded here and A2's to place.

## §3 Candidates

| ID | Source path @ pin | What | Verdict | Target repo and path | Lane | Q |
|---|---|---|---|---|---|---|
| RC-A1-01 | `Orchestrator_System/.claude/skills/run-batch/SKILL.md` @ 2e7adb3 | run-batch 282 lines: §6 closeout-one-command, §7 newline paragraph | adapt: take §7:199-202 (newline rule) verbatim now. Take §6 only as Q-A1-01 decides; until then keep TARGET §6 :156-326. Replaces `SW_Development/.claude/skills/run-batch/SKILL.md` and its six suite mirrors and seven `.codex` copies (frozen per Q-G-09). If §6 is copied verbatim, every suite closeout calls an absent `scripts/harness/closeout.py` and every batch fails at close | SW_Development + 6 suites `.claude/skills/run-batch/SKILL.md` | B1 (text), B7 (harness) | Q-A1-01 |
| RC-A1-02 | `Orchestrator_System/.claude/skills/plan-batch/SKILL.md` @ 2e7adb3 (1.5.1) | plan-batch §7 items: no `cites:` under `validation/`; proof-surface item; `--predict` budget item | adapt: adopt :204-207 and :216-218 verbatim. Keep the 1.4.0 cap item (TARGET :202-205) in place of :208-215 until a suite has `closeout.py --predict`. Version comment "1.5.1-pl". Replaces TARGET plan-batch 1.4.0 in seven `.claude` copies. If wrong, the auditor's §7 line demands a `--predict` command that does not exist | SW_Development + 6 suites `.claude/skills/plan-batch/SKILL.md` | B1 | Q-A1-01 |
| RC-A1-03 | `Orchestrator_System/.claude/skills/real-stack-testing/SKILL.md` @ 2e7adb3 | item 7: closeout via `closeout.py`; "a test never reads a file the harness writes" | adapt: adopt the second sentence (:43-45) now; the `closeout.py` sentence only with RC-A1-01's §6. Replaces TARGET item 7 (`SW_Development/.claude/skills/real-stack-testing/SKILL.md:40-43`) in seven copies | SW_Development + 6 suites `.claude/skills/real-stack-testing/SKILL.md` | B1 | Q-A1-01 |
| RC-A1-04 | `Orchestrator_System/.claude/agents/batch-closeout-reviewer.md` @ 2e7adb3 | Opus · high, maxTurns 30, "before you report" paragraph | adopt verbatim (no Conductor-specific term). Replaces seven TARGET copies. If wrong (e.g. Opus unavailable to the worker account), the reviewer fails to start and run-batch §7 falls back to inline review | SW_Development + 6 suites `.claude/agents/batch-closeout-reviewer.md` | B1 | — |
| RC-A1-05 | `Orchestrator_System/.claude/agents/batch-plan-auditor.md` @ 2e7adb3 | effort high, maxTurns 24, judge-against-contract paragraph | adopt verbatim. Replaces seven TARGET copies. If wrong, it only costs more tokens per audit | SW_Development + 6 suites `.claude/agents/batch-plan-auditor.md` | B1 | — |
| RC-A1-06 | `Orchestrator_System/.claude/agents/real-stack-validator.md` @ 2e7adb3 | foreground rule, 3,600,000 ms cap, maxTurns 16 | adopt verbatim together with RC-A1-17's env. Replaces seven TARGET copies. Without the env a Bash call above 600 s is refused and long validations cannot finish | SW_Development + 6 suites `.claude/agents/real-stack-validator.md` | B1 | Q-A1-03 |
| RC-A1-07 | `Orchestrator_System/.claude/agents/v5-section-reader.md` @ 2e7adb3 | quoted windows from the Conductor v5 proposal via its Section Map | retire for TARGET (do not transfer): hard-codes the v5 proposal path (:10-12). PlantLibrary has no Section-Mapped authority document. run-batch §5 already says "where one exists" | — | B1 | — |
| RC-A1-08 | `Orchestrator_System/.claude/skills/test-driven-development/` @ 2e7adb3 | headless-safe TDD (never delete committed files; exceptions recorded), `writing-good-tests.md`, LICENSE | adapt: take the headless and process-boundary edits, `writing-good-tests.md` and the LICENSE. Replace the pytest/PowerShell examples with stack-neutral ones, or one per stack (Python, Kotlin, TS). Replaces TARGET TDD + `testing-anti-patterns.md` in seven copies. A verbatim copy teaches a pytest command inside Gradle and npm suites | SW_Development + 6 suites `.claude/skills/test-driven-development/` | B1 | — |
| RC-A1-09 | `Orchestrator_System/.claude/skills/systematic-debugging/` @ 2e7adb3 | headless edits (fix #4 → blocked, no "ask the human"), secrets-presence example, LICENSE | adapt: adopt verbatim except the PowerShell-only example; keep PlantLibrary's two extra assets. Replaces `SW_Development/.claude/skills/systematic-debugging/`. If wrong, a headless worker waits for an answer it never gets | SW_Development `.claude/skills/systematic-debugging/` | B1 | — |
| RC-A1-10 | `Orchestrator_System/.claude/skills/{design-gate,design-audit,gallery-governance}` @ 2e7adb3 (= `Design_Template_Kit/anchoring-kit/skills/*` @ f08e588) | the Kit's three governance skills | adopt verbatim through the Kit installer only (never a hand copy), after the Configuration exists. New in Dashboard, AndroidApp, PyApp (`.claude`, `.codex` exempt from the freeze, `.agents`, `.github`). A hand copy drifts from the Kit and fails the Kit's `check-parity.mjs` | PlantLibrary_Dashboard, _AndroidApp, _PyApp `.claude/skills/…` (+ SharedContracts if Q-G-01 (a)) | B5 | Q-G-01, Q-G-07 |
| RC-A1-11 | `Orchestrator_System/.claude/skills/impeccable` @ 2e7adb3 (3.8.0) | impeccable | keep PlantLibrary's (identical modulo CRLF; auto-mode already applied at PyApp `35ddc63`). Install into Dashboard with the Kit's `--with-impeccable` from the PyApp checkout. If sourced from an unpatched copy, the bypass flags return (Kit `INSTALL.md:107-116`) | PlantLibrary_Dashboard `.claude/skills/impeccable` (new); PyApp/AndroidApp unchanged | B5 | Q-G-08 |
| RC-A1-12 | `Orchestrator_System/.claude/skills/harness-upkeep/SKILL.md` @ 2e7adb3 (0.1.0) | which check follows which edit | adapt: rewrite the table for TARGET: parity checker, hygiene checker, batch-package checker, Kit parity. Drop the v5, Section Map and duration-history rows. Operator-session only. New in the superproject. A verbatim copy names `regenerate_section_map.py` and a v5 proposal that do not exist | SW_Development `.claude/skills/harness-upkeep/` | B7 | — |
| RC-A1-13 | `Orchestrator_System/.claude/skills/scratch-gate/SKILL.md` @ 2e7adb3 (0.1.0) | operator scratch gate over `reclaim_scratch.py` | adapt for PyApp only (the only suite with `reclaim_scratch.py`); replace the CLAUDE.md-paragraph and runbook §11 references. Elsewhere it would call an absent script | PlantLibrary_PyApp `.claude/skills/scratch-gate/` | B7 | Q-A1-01 |
| RC-A1-14 | `Orchestrator_System/.claude/skills/instance-sync/SKILL.md` @ 2e7adb3 | sync of a deployed Conductor instance | retire for TARGET (Conductor-instance procedure: `SYNC_INSTANCE.md`, `run-conductor-supervised.bat`) | — | — | — |
| RC-A1-15 | `Orchestrator_System/.claude/skills/{code-quality-review,security-audit,pathfinder}` @ 2e7adb3 | third-party-derived review skills (MIT, CC-BY-SA-4.0, Apache-2.0) | adapt: replace the deliverable path `implementation/Conductor_V2/planning/AUDIT_*` with a TARGET root. Drop "v5 §14", "single asyncio loop" and the Conductor read-exclusions (`code-quality-review/SKILL.md:10`, `pathfinder/SKILL.md:36,44`). Keep LICENSE/NOTICE. Superproject only. A verbatim copy writes into a path that does not exist | SW_Development `.claude/skills/…` | B1 | Q-A1-02 |
| RC-A1-16 | `Orchestrator_System/.claude/skills/dependency-audit` @ 2e7adb3 | Trail of Bits supply-chain collector (npm/PyPI/Go) | adapt: the repository-rules section (:16-38) is Conductor's (one `pyproject.toml`, five hosts, deliverable path). PlantLibrary has npm (Dashboard), PyPI (PyApp, Server) and Gradle (unsupported). Operator session, network | SW_Development `.claude/skills/dependency-audit/` | B1 | Q-A1-02 |
| RC-A1-17 | `Orchestrator_System/.claude/settings.json` @ 2e7adb3 | tracked deny list (Bash + PowerShell twins) and `BASH_MAX_TIMEOUT_MS` | adapt: track the deny list in each of the seven `settings.json` files. Add the env where a suite runs long validations. Replaces the untracked `SW_Development/.claude/settings.local.json` deny list. If wrong, a fresh clone or a suite worker runs without the git-safety denies | 7 × `.claude/settings.json` | B1 | Q-A1-03 |
| RC-A1-18 | `Orchestrator_System/.claude/settings.local.json` (untracked) @ 2e7adb3 | operator allows: Conductor REST, `notify_telegram`, instance bats, `conductor.db` | retire for TARGET (Conductor-specific; the generic `python scripts/harness/*` allow is the one transferable line) | — | — | — |
| RC-A1-19 | `Orchestrator_System/scripts/harness/check_harness_parity.py` @ 2e7adb3 :54-77, :204-272, :629-642 | the Codex freeze checks (`check_codex_frozen`, `check_agents_frozen`) | adapt: port the two frozen checks into `SW_Development/scripts/harness/check_harness_parity.py`, stdlib only, without `src/conductor/tree_parity.py` (:156-158). Pins per repository. AGENTS.md hashed *outside* the marked blocks (F-A1-12). Add the cross-repository mirror compare. A verbatim port imports a module that does not exist here | SW_Development `scripts/harness/check_harness_parity.py` | B7 | Q-G-09 |
| RC-A1-20 | `Orchestrator_System/.agents/README.md` @ 2e7adb3 | bridge file: frozen statuses, unfreeze recipe, "Claude-only skills" table with licence and pin | adapt: rewrite `SW_Development/.agents/README.md` as PlantLibrary's own bridge file (F-A1-10). A copy keeps the Conductor voice and the wrong rows | SW_Development `.agents/README.md` | B1 | Q-G-09 |
| RC-A1-21 | `Orchestrator_System/tests/test_run_batch_skill_contract.py` @ 2e7adb3 | static guard on run-batch's commit-proposal strings | adapt as a checker function (no test runner in this program): the parity checker asserts the four strings in every run-batch copy | SW_Development `scripts/harness/check_harness_parity.py` | B7 | — |
| RC-A1-22 | `SW_Development/.claude/skills/{android-validation,verify-stack,sync-contracts,webapp-testing,design-adoption}` @ 8702e0a | PlantLibrary-only skills named by suite rows | keep PlantLibrary's; mirror into each suite whose rows name it: android-validation → AndroidApp; verify-stack → PyApp, AndroidApp, Dashboard; sync-contracts → Server, SharedContracts, PyApp; webapp-testing → Dashboard; design-adoption → the three clients per Q-G-07. Then add them to the parity checker. Without this the rows stay unexecutable from a suite cwd | suite `.claude/skills/…` | B1 | Q-A1-04, Q-G-07 |
| RC-A1-23 | `SW_Development/.claude/skills/gui-validation/SKILL.md` @ 8702e0a | 375-line GUI-driving protocol | keep PlantLibrary's. Replace PyApp's broken 38-line pointer (`.claude`, `.agents`, `.github`) with the full mirror. A pointer that does not resolve gives the worker no protocol | PlantLibrary_PyApp `.claude/skills/gui-validation/SKILL.md` | B1 | Q-A1-04 |
| RC-A1-24 | `SW_Development/.claude/skills/ui-ux-pro-max` @ 8702e0a | style, font and chart dataset + scripts | keep in the superproject (Kit wizard fallback, `Design_Template_Kit/wizard/lib/axes-to-tokens.mjs:62`); never mirror into suites (VAL F3). Retiring it breaks the wizard's third fallback unless `KIT_UXPM_ROOT` or `<kit>/vendor` is set | SW_Development `.claude/skills/ui-ux-pro-max` | B5 | — |
| RC-A1-25 | `PlantLibrary_Workspace/.claude/skills/*` @ 6b4b88b | six Workspace-only skill copies (verify-stack stale) | adapt: refresh verify-stack from the superproject, or retire the Workspace copies in favour of the superproject's. The Workspace has no rows naming them except `android-validation` and `verify-stack` (2 each) | PlantLibrary_Workspace `.claude/skills/` | B1 | Q-A1-04 |
| RC-A1-26 | `PlantLibrary_PyApp/.claude/settings.local.json` @ 35ddc63 | tracked local settings: impeccable hook + stale allows | adapt: move the hook into a tracked `settings.json` and drop the allows for absent files. AndroidApp gets the same hook when B5 re-installs impeccable | PlantLibrary_PyApp `.claude/settings.json` | B5 | Q-A1-03 |
| RC-A1-27 | `Orchestrator_System/.claude/skills/real-stack-testing` + `validate-real-stack` @ 2e7adb3 | shared references and runner | adopt verbatim = no-op (already byte-identical: `gui-testing.md`, `metered-validation.md`, `validate-real-stack/SKILL.md`, `run_validation.ps1`) | — | B1 | — |
| RC-A1-28 | `Design_Template_Kit/anchoring-kit/skills/{design-wizard,design-migration}` @ f08e588 | the Kit's two creation/migration skills (not installed in the Conductor) | record only here; A4 decides where they run (Kit checkout or installed) | — | B5/B6 | — |

## §4 Questions for the operator

| Q-A1-nn | Question | Options ((a) recommended first) | Why (a) | Which steps wait |
|---|---|---|---|---|
| Q-A1-01 | How should PlantLibrary's run-batch §6 (closeout) relate to the Conductor's `closeout.py`? | (a) Keep PlantLibrary §6 for now and adopt everything else in run-batch. B7 ports `closeout.py` per suite only after A7/A8 confirm instance 2's closeout route; §6 and the plan-batch `--predict` item follow in the same step. (b) Write a stack-neutral PlantLibrary §6: named row validation, then the suite's `SCOPE.md` standing closeout, with no chunk harness outside PyApp. (c) Adopt the Conductor §6 verbatim now. | (a) breaks nothing today: PyApp keeps a working closeout and the five other suites keep their row validations. (c) fails every closeout in all six suites (F-A1-02). (b) diverges permanently from the Conductor and its coordinator handoff (F-A1-03) | B1's run-batch/plan-batch/real-stack-testing §6–§7 text; B7's closeout port; C1's resume prompt |
| Q-A1-02 | Install the four third-party-derived Conductor skills (`code-quality-review` MIT, `security-audit` CC-BY-SA-4.0, `pathfinder` Apache-2.0, `dependency-audit` CC-BY-SA-4.0 + network)? | (a) Install the first three in the superproject only, adapted per RC-A1-15 with LICENSE/NOTICE carried, operator-session only. Defer `dependency-audit` until Gradle coverage is decided. (b) Install all four in the superproject. (c) Install none. | The Conductor installed them only after a safety check and operator approval (`D-2026-10-02-23` (h), `STATE.md:44198-44207`). The licences travel with them. `dependency-audit` cannot see AndroidApp's Gradle dependencies, and it sends the `gh` token to `api.github.com` (`dependency-audit/SKILL.md:33-37`) | B1's new-skill step |
| Q-A1-03 | Move protective settings into tracked `.claude/settings.json` in all seven repositories? | (a) Yes: the Conductor's 28-entry deny list (Bash + PowerShell twins) tracked in each. `BASH_MAX_TIMEOUT_MS` 3600000 is added only where a suite runs long validations (PyApp now; others with Q-A1-01). PyApp's impeccable hook moves to its tracked `settings.json`. The superproject's local `Bash(cat .env)` allow is left to the operator's own file. (b) Keep everything local. | Today a fresh clone or a suite worker runs without any git-safety deny (F-A1-19). `real-stack-validator`'s promised timeout needs the env (F-A1-06) | B1 settings step; RC-A1-06's agent text |
| Q-A1-04 | Should the PlantLibrary-only skills that suite rows name be mirrored into those suites? | (a) Yes: mirror each into exactly the suites whose rows name it (RC-A1-22) as whole folders, extend the parity checker to them, and replace PyApp's gui-validation pointer with a full copy. The Workspace copies are refreshed or retired with them. (b) Keep them superproject-only; such rows run only from a superproject session, recorded in each suite's `SCOPE.md`. | Discovery does not cross upward (F-A1-07), so those rows are unexecutable by an instance-2 worker today. (b) contradicts run-batch §4.4 ("never mark such a row done unless the command ran") | B1 mirror step; B4's row edits (none if (a)); B7 parity extension |

## §5 Reusable things this brief did not name

- **The Kit's `scripts/design/check-parity.mjs`.** The four-mirror parity check for the Kit folders (`C:\Programmierung\Orchestrator_System\scripts\design\check-parity.mjs`). The Conductor's parity checker defers to it for the four Kit folders. B5 gets it from the Kit installer, never by hand.
- **The Conductor's `tests/test_skill_mirror_parity.py` (221 lines).** It treats a `frozen` bridge status as unenforced (`D-2026-10-02-23` (c)). Its logic belongs in the extended parity checker (RC-A1-19), not as a test. Not read beyond its name and the decision text.
- **The F-01 notice convention.** One line inserted after line 2 of a frozen `AGENTS.md` (`C:\…\check_harness_parity.py:56-58, 238-247`). It is the clean way to mark TARGET's frozen `AGENTS.md` files.
- **The "Claude-only skills" table with source, pin and licence** (`C:\Programmierung\Orchestrator_System\.agents\README.md:47-60`). This is the provenance record TARGET lacks for `webapp-testing` (Apache LICENSE.txt present), `systematic-debugging` and `test-driven-development` (obra/superpowers, no LICENSE file in TARGET).
- **impeccable's two environment off-switches** (`IMPECCABLE_LIVE_COPY_AGENT=off`, `IMPECCABLE_NO_UPDATE_CHECK=1`; `C:\Programmierung\Design_Template_Kit\anchoring-kit\INSTALL.md:118-128`). They are per-user and already set on this machine per operator answer B7, so this is a check for B5, not a file.
- **`closeout.py handoff`.** The coordinator-side contract (`execution_table.py:762-775`) for A7/A8/B8.

## §6 Claims to verify

1. **The superproject parity checker checks only the superproject's own `.claude` vs `.codex`, never a suite.**
   Check: `grep -n "root /\|PlantLibrary_\|submodule" C:\Programmierung\SW_Development\scripts\harness\check_harness_parity.py`. Expected: only `.claude`/`.codex` lines under the one repository root (:61-62, :78-79, and the self-test copies :102-105), no suite path.
2. **No TARGET repository has `scripts/harness/closeout.py`, so the Conductor's run-batch §6 cannot run in any suite.**
   Check, from `C:\Programmierung\SW_Development`: `for r in . PlantLibrary_*; do git -C $r ls-files scripts/harness/closeout.py; done`. Expected: no output. Then compare with `grep -n "closeout.py" C:\Programmierung\Orchestrator_System\.claude\skills\run-batch\SKILL.md`, which shows :175 and :190.
3. **A whole-file AGENTS.md freeze conflicts with the hygiene checker's block parity.** Check both halves:
   - `grep -n "Kit:" C:\Programmierung\Orchestrator_System\AGENTS.md C:\Programmierung\Orchestrator_System\CLAUDE.md`: 0.8.0 vs 1.3.1, so the frozen block already drifted.
   - `sed -n 725,732p C:\Programmierung\SW_Development\scripts\hygiene\repo_hygiene_check.py`: TARGET fails on any CLAUDE.md/AGENTS.md block difference.

## §7 Detail

### §7.1 Per-skill matrix

Line counts are SKILL.md lines (companion files in brackets). "=" means byte-identical, CR-insensitive where stated.

| Skill | Conductor @ 2e7adb3 | TARGET superproject @ 8702e0a (per suite where it differs) | Verdict | What breaks if wrong |
|---|---|---|---|---|
| code-quality-review | 12 [+ref 292, LICENSE] | absent | adapt, superproject only (RC-A1-15). Paths and Conductor terms in :10-12; Python reference fits PyApp/Server/SharedContracts only | writes to `implementation/Conductor_V2/planning/`, which does not exist |
| dependency-audit | 168 [+4 scripts 3,462, NOTICE] | absent | adapt (RC-A1-16), Q-A1-02 | rules name one `pyproject.toml` and five hosts; Gradle invisible; the token goes to GitHub |
| design-audit | 203 (= Kit 1.1.0) | absent | adopt verbatim via the Kit installer, B5 (RC-A1-10) | a hand copy drifts from the Kit; reports red "no Configuration" before B5 |
| design-gate | 202 (= Kit 1.0.0) | absent | adopt verbatim via the Kit installer, B5 | as above; it is the designated successor of design-adoption (Q-G-07) |
| gallery-governance | 210 (= Kit 1.0.0) | absent | adopt verbatim via the Kit installer, B5 | as above |
| harness-upkeep | 52 (0.1.0) | absent | adapt (RC-A1-12), superproject | names v5/Section-Map scripts that do not exist |
| impeccable | 167 [+~95 files] 3.8.0 | absent in the superproject. PyApp, AndroidApp: 167 = Conductor (CRLF-insensitive), plus `.agents` 173-line and `.github` 165-line runtime variants. Dashboard, Server, SharedContracts, Workspace: absent | keep PlantLibrary's. Add to Dashboard via `--with-impeccable` (RC-A1-11) | a re-install from an unpatched source brings back `bypassPermissions` |
| instance-sync | 77 (0.1.0) | absent | retire for TARGET (RC-A1-14) | — |
| pathfinder | 119 [+LICENSE, NOTICE] | absent | adapt, superproject only (RC-A1-15) | read-exclusions and deliverable path are Conductor paths (:36, :44) |
| plan-batch | 260 (1.5.1) | 247 (1.4.0); seven copies = | adapt (RC-A1-02; §7.3) | the `--predict` item fails every audit without `closeout.py` |
| real-stack-testing | 93 [+2 refs =] | 91 [+2 refs =]; seven copies = | adapt item 7 (RC-A1-03) | names `closeout.py` |
| run-batch | 282 | 408; seven copies = | adapt (RC-A1-01; §7.2), Q-A1-01 | verbatim: every suite closeout fails |
| scratch-gate | 68 (0.1.0) | absent | adapt for PyApp only (RC-A1-13) | calls an absent `reclaim_scratch.py` elsewhere |
| security-audit | 24 [+13 refs, NOTICE] | absent | adapt, superproject only (RC-A1-15), Q-A1-02 | Python-only sharp-edges; Kotlin/TS unreviewed; deliverable path |
| systematic-debugging | 282 [+3 refs, LICENSE] | 296 [+3 refs, +.ts example, +find-polluter.sh]; superproject only | adapt (RC-A1-09) | a headless worker "asks the human" and stalls |
| test-driven-development | 311 [+writing-good-tests 203, LICENSE] | 371 [+testing-anti-patterns 299]; seven copies = (= Conductor's frozen `.codex` copy) | adapt (RC-A1-08) | verbatim teaches pytest in Kotlin/TS suites; the old text says "delete" committed code |
| validate-real-stack | 39 [+runner 50] | = (Claude and Codex variants both equal the Conductor's) | adopt = no-op | — |
| android-validation (PL-only) | — (relocated out in 2026-08) | 255; superproject + `.codex` only | keep; mirror into AndroidApp (RC-A1-22) | AndroidApp rows (:27 and others) stay unexecutable |
| design-adoption (PL-only) | — | 90; superproject, `.codex`, Workspace | evidence for Q-G-07 (F-A1-15): states hex values (:71-74) and hard-codes adoption rows (:55-61), against design-gate's no-values rule (`design-gate/SKILL.md:15-16`). Its client-suite rows cannot load it (F-A1-07). design-gate is its parameterized successor (`:8-11`). The canon it points to (`SharedContracts/design-tokens`, `04_APPROVED_DESIGN_REVISION_2026-07-10.md`) is what A4's import turns into a Configuration. Decision: not taken here | keeping both without a rule: two gates with different sources of truth; retiring before B5 anchors: no gate at all |
| gui-validation (PL-only) | — | 375; superproject, `.codex`, Workspace. PyApp: 38-line pointer that does not resolve (F-A1-08) | keep; full mirror into PyApp (RC-A1-23) | PyApp GUI rows (`TASK_CHECKLIST.md:11`) run without the protocol |
| sync-contracts (PL-only) | — | 96; superproject, `.codex`, Workspace | keep; mirror into Server, SharedContracts, PyApp | contract-wave rows unexecutable from the suite |
| ui-ux-pro-max (PL-only) | — | 377 [+3 scripts, data; 28 files]; superproject, `.codex`, Workspace | keep in the superproject only (RC-A1-24) | retiring breaks the Kit wizard's fallback root |
| verify-stack (PL-only) | — | 188; Workspace 149 (stale, F-A1-20) | keep; mirror into PyApp, AndroidApp, Dashboard; refresh or retire the Workspace copy | walkthrough rows unexecutable; a Workspace session reads the stale copy |
| webapp-testing (PL-only) | — | 113 [+scripts, examples, Apache LICENSE.txt]; superproject, `.codex`, Workspace | keep; mirror into Dashboard | Dashboard row :42 unexecutable |

### §7.2 run-batch delta (TARGET 408 → Conductor 282)

Diff of `SW_Development/.claude/skills/run-batch/SKILL.md` against `C:\Programmierung\Orchestrator_System\.claude\skills\run-batch\SKILL.md`:

| Section | TARGET lines | Conductor lines | What changed | Where it went | Verdict for PlantLibrary |
|---|---|---|---|---|---|
| front matter, §1 Locate, §2 Authority, §3 Select, §4 Preflight, §5 Implement | 1-155 | 1-155 | identical | — | keep (= adopt) |
| §6.0 foreground rule | 158-170 | 158-165 | Shortened. "regression" dropped from the command list. "Validation commands are run in the foreground… long validations are the orchestrator's job (item 1)" removed. Resumability now points at item 2 (the closeout) instead of item 6 | — | adopt the Conductor wording only with Q-A1-01 (its "item 2" reference needs the closeout); else keep |
| §6.1 long-validation rule | 171-180 | 166-169 (merged) | The `run_validation.py` launch rule survives as one sentence. Shell-timeout, yield and no-polling detail and the 540 s split rule are gone | `docs/harness/runners.md`, `run_validation.py` itself | keep TARGET's (only PyApp has the runner; its CLAUDE.md :344-349 relies on it) |
| §6.2 validate-real-stack delegation | 181-187 | 170-172 (merged into 6.1) | condensed; same contract | — | either; identical meaning |
| §6.3 run each validation cell literally | 188-191 | 166-167, 172-173 | condensed | — | either |
| §6.4 lint touched files, no repository-wide widening | 192-195 | removed | lint moved into the closeout's preflight (`closeout.py:831-832, 1028-1036`, refusal `lint_red`) | `closeout.py` | keep TARGET's (no closeout exists) |
| §6.5 touched-path accounting / `direct-validation-only` | 196-205 | removed | moved into the closeout's scope planning (`regression_scope` refusals passed through, `docs/harness/closeout.md:155`) | `closeout.py`, `regression_scope.py` | keep (PyApp's ported `regression_scope.py` implements it) |
| §6.5a standing legs: history merge, ruff, acceptance registry, probe | 206-227 | removed | moved into the closeout: acceptance as a standing inclusion (`closeout.py:15, 598`), history merge on pass (`:3109`) | `closeout.py`; `docs/harness/closeout.md:77-83` | keep for PyApp; inapplicable to the Gradle and npm suites as written (pytest-specific) |
| §6.6 scoped matrix, chunk plan, `run_chunks.py`, envelope, classification, digests | 228-309 | removed | The whole algorithm, including the `CD2-B140`/`CD2-B230` cap history and the AM-44 envelope arithmetic, moved into one command | `closeout.py` (3,402 lines); `docs/harness/closeout.md`, `run-chunks.md`, `regression-scope.md` | keep for PyApp until Q-A1-01; these 82 lines are why TARGET is 126 lines longer |
| §6.7 no speculative variants | 310-312 | 188-190 (as "never widen the run") | condensed into item 2 | — | either |
| §6.8 standing invariants (offline smoke; no repository-wide run under the ceiling) | 313-318 | removed (§8 `Invariants:` line stays) | moved into the package `SCOPE.md` standing checks run by the closeout | `closeout.py` + `SCOPE.md` | keep (PlantLibrary's `SCOPE.md` files name the invariants; nothing runs them for the worker) |
| §6.9 long output | 319 | 191 | same | — | either |
| §6.10 evidence file and deliverable naming | 320-326 | 191-195 | condensed; evidence prose goes "below the fact block" the closeout writes | — | keep TARGET wording until a closeout writes a fact block |
| new §6.2 the closeout is one command (exit 0/1/2/3, `--stop`, handoff line) | — | 174-190 | new | — | adopt only with Q-A1-01 (b)/(c) or after B7's port |
| §7 newline rule (read bytes, keep CRLF/LF) | — | 199-202 | new (CD2-B412, `ab49005`) | — | adopt verbatim now; matches the kickoff's rule 8 |
| §7 diff review, closeout-reviewer delegation, row status, commit proposal JSON | 328-365 | 204-239 | identical | — | keep (the Conductor's `test_run_batch_skill_contract.py:7-19` pins these strings) |
| §8 report, `CONDUCTOR_BATCH_COMMIT_PROPOSAL`, Telegram enqueue | 367-408 | 241-282 | identical | — | keep. The enqueue fails in every suite (no `scripts/notify_telegram.py`), already documented as expected (`PlantLibrary_AndroidApp/CLAUDE.md:74-76`) |

What PlantLibrary's 408 lines contain that the Conductor's 282 do not: §6.1's runner timing rules, §6.4 lint, §6.5 path accounting, §6.5a standing legs, §6.6's chunk algorithm, §6.7 and §6.8 as separate items. Together that is TARGET :171-318 minus the condensed overlap, which is the 126-line difference plus the 4-line §7 paragraph the Conductor added. Nothing in TARGET's version is PlantLibrary-specific. It is the Conductor's own pre-2026-09-18 text (the closeout act `e21e7f0`, D-2026-09-18-01), so "keep" means "keep the Conductor's older version", not "keep a PlantLibrary invention".

### §7.3 plan-batch delta 1.4.0 → 1.5.1

| Section | TARGET (1.4.0) | Conductor (1.5.1) | Change | Verdict |
|---|---|---|---|---|
| version comment | :8-12 | :8-14 | adds the 1.5.0 and 1.5.1 history lines | adapt: own line "1.5.1-pl (2026-10-xx), from Conductor 1.5.1 minus the `--predict` item" |
| §1–§6, §8 | 1-191, 207-247 | 1-191, 219-260 | identical | keep |
| §7 premise item | :201-202 | :204-207 | adds "no `cites:` target under `implementation/*/validation/`, which no test may read" (D-2026-10-04-04 (g)) | adopt verbatim. PlantLibrary packages keep evidence under `validation/` too |
| §7 cap item → budget item | :202-205 ("touched-path set scopes under the active cap") | :208-215 (`closeout.py --predict … fits validation.closeout_budget_s`) | replaced | keep 1.4.0's item until Q-A1-01; `closeout_budget_s` and `--predict` do not exist in TARGET |
| §7 proof-surface item | — | :216-218 | new (1.5.0, F-7): no runbook or row note names a proof surface beyond the row's validation cell | adopt verbatim. It matches this program's own rule (kickoff §2 rule 3: "never a proof surface") |

The `batch-plan-auditor` runs "plan-batch's §7 self-review checklist" item by item (`C:\…\batch-plan-auditor.md:16`). Whatever §7 says is what the auditor fails rows on, so the `--predict` item must not be adopted without the command.

### §7.4 Agents

| Agent | Conductor | TARGET (7 identical copies) | Verdict |
|---|---|---|---|
| batch-closeout-reviewer | opus · high, maxTurns 30; "Before you report" adds: weakened-bar findings, `Inspected:` / `Not inspected:` lines, `not judged` (:30-39) | sonnet · high, maxTurns 20 | adopt verbatim (RC-A1-04). No Conductor-specific term ("the project CLAUDE.md" :19) |
| batch-plan-auditor | sonnet · high, maxTurns 24, no Bash/PowerShell; "Judge each artifact against its contract": scope reduction, broken contract, mis-cut (:39-47) | sonnet · medium, maxTurns 12 | adopt verbatim (RC-A1-05). AM-52/AC142 wording is already in TARGET |
| real-stack-validator | sonnet · low, maxTurns 16; foreground rule, ≤ 3,600,000 ms, no elevation, basetemp inside the repo, verbatim command only (:18-21) | maxTurns 10 | adopt verbatim with the env (RC-A1-06, Q-A1-03) |
| v5-section-reader | sonnet · low; reads only `implementation/Conductor_V2/proposal/conductor-v5-system-proposal.md` via its `## Section Map` (:10-17) | absent (deliberately, `SW_Development/.agents/README.md:56-57`) | does not transfer (RC-A1-07). Purpose: keep a multi-thousand-line normative proposal out of the parent context by returning quoted windows. TARGET's largest Markdown files are `PlantLibrary_Workspace/prompts/reference/TASK_CONTEXT_V3.md` (8,012 lines) and two `PlantLibrary_PyApp/Documentation/*_plan_*.md` (3,362; 3,042). None is a live package's normative input and none has a Section Map. A generic `section-reader` taking the document path as input is a later option if a package adopts a large normative proposal |

All three shared agents preload skills (`skills: real-stack-testing`, plus `plan-batch` for the auditor). They therefore read whatever plan-batch §7 and real-stack-testing item 7 say in that repository, which is why RC-A1-02 and RC-A1-03 must land in the same commit as the agents.

### §7.5 Settings

| Entry | Conductor | TARGET | Conductor-specific? |
|---|---|---|---|
| `env.BASH_MAX_TIMEOUT_MS: 3600000` | tracked `settings.json:2-4` (e21e7f0, with `foreground_ceiling_s 3600`) | none | generic mechanism; the value is tied to the closeout ceiling. Needed wherever a Claude session runs a validation over 600 s |
| `permissions.deny` git-safety list | tracked `settings.json:5-35`, 28 entries: 14 Bash + 14 PowerShell twins (D-2026-10-03-21) | superproject untracked `settings.local.json:7-22`, 14 Bash, no PowerShell; suites none | generic; adopt (Q-A1-03) |
| `permissions.allow` | untracked `settings.local.json:3-41`: `notify_telegram --enqueue`; awk/sort one-liners; Conductor REST (`127.0.0.1:8787` pause/resume/cancel/answer); `python scripts/harness/*`; `regenerate_section_map.py --check`; `check_plan_contract_stable.py`; `plan_readiness.py`; `SYNC_INSTANCE.md`; `C:\Programs\AI_Orchestrator\*.bat`; keeper logs; `sqlite3 conductor.db` | superproject: `Bash(ls -la .env)`, `Bash(cat .env)`. PyApp (tracked local): `python -`, one `rg`, a script that no longer exists | all Conductor-specific except `python scripts/harness/*`; operator-personal files, never tracked |
| hooks | none in either Conductor settings file. Conductor hooks: `.codex/hooks.json` (deny-git, frozen) and `.github/hooks/impeccable.json` | superproject `.codex/hooks.json` (= Conductor's); PyApp: Claude impeccable hook in tracked `settings.local.json:9-24`, Codex hook `.codex/hooks.json`, Copilot hook `.github/hooks/impeccable.json`; AndroidApp none | impeccable hooks are Kit-managed (`.github/hooks/impeccable.json` per Kit `INSTALL.md:38-39`) |
| `model` | none in either | none | — |

TARGET's `{}` (`SW_Development/.claude/settings.json:1`) therefore lacks exactly two transferable things: the tracked deny list with twins, and the timeout env.

### §7.6 The Codex freeze pattern applied to TARGET (evidence for Q-G-09; not decided here)

**What D-2026-10-02-23 froze** (`C:\Programmierung\Orchestrator_System\implementation\Conductor_V2\STATE.md:44166-44175`):
- `.codex/**`, `AGENTS.md`'s runtime section and `.codex/agents/*.toml`, at `main` `10177e3`;
- "kept, never deleted (AC51), not edited, not mirrored";
- Codex stays a registered but disabled vendor (`D-2026-09-30-16`);
- re-enabling starts with an unfreeze act that re-mirrors `.claude/**` since the freeze commit.

The four Kit folders were exempted later (`D-2026-10-03-07`, `CD2-B461`; `.agents/README.md:91-94`).

**How `.agents/README.md` explains it:**
- the freeze notice and unfreeze recipe (:6-11);
- the parity checker's new meaning (:13-22);
- bridge rows flipped to `frozen` (:28-32), with `validate-real-stack` kept as "runtime-adapted" and the Kit rows "Kit-installed";
- the agent roster with Codex models marked `(frozen)` (:40-45);
- the "Claude-only skills" table for everything added or changed after the freeze, with source, pin and licence (:47-60).

**How the checker compares against the freeze commit:**
- Digests are SHA-256 of CRLF→LF-normalized bytes, written once from `git show 10177e3:<path>`, never from the working tree (`check_harness_parity.py:49-53`).
- Every non-exempt `.codex` file must be present and equal; any added, removed or changed file is a diagnostic (`:213-235`).
- `AGENTS.md` must equal its frozen digest, or that digest plus the F-01 notice line after line 2 (`:250-272`).
- The two old compares stay defined but out of `check_all` (`:629-642`, docstring :21-26).

**TARGET today** (all measured):

| Repository | `.codex/**` (tracked) | `.agents/**` | `AGENTS.md` | Mirrors what |
|---|---|---|---|---|
| SW_Development | 59: 13 skill folders = `.claude/skills` (validate-real-stack Codex variant), 3 agent `.toml`, `hooks.json` + `hooks/deny_git_commands.mjs` (= Conductor's) | `README.md` only (stale, F-A1-10) | 33 lines, hygiene block at :16 | `.claude/**` byte-identically; the parity checker enforces it |
| Workspace | 12: the 5 shared skill folders + 3 agents | none | 47 lines, hygiene block :30 | the superproject's shared 5 + 3 (not its 6 Workspace-only skills) |
| PyApp | 13: the 12 shared + `hooks.json` (impeccable via `.agents`) | 100: `skills/impeccable` (Codex variant, 99 files) + `skills/gui-validation` pointer | 511 lines, hygiene block :494 | shared 5 + 3; impeccable lives in `.agents` |
| AndroidApp | 12 | 99: `skills/impeccable` | 47 lines, :30 | shared 5 + 3 |
| Dashboard, Server, SharedContracts | 12 each | none | 47 / 62 / 47 lines | shared 5 + 3 |

**The shape the freeze would take here** (if Q-G-09 (a)):
1. **Freeze commit.** One superproject commit plus one per suite, recorded as a `D-2026-10-xx-nn` in each repository's `hygiene/HYGIENE_DECISIONS.md` (the hold vocabulary) and pointing at the Conductor precedent. Digests come from `git show <freeze>:<path>` with LF normalization, never from working bytes. Line endings in TARGET are mixed, which is why normalization is required.
2. **`.codex/**` per repository.** Frozen and kept, with these exemptions:
   - the four Kit folders under `.codex/skills/`, once B5 installs them;
   - `settings.local.json`;
   - `__pycache__`.

   The superproject's `.codex/skills` also holds the 8 PlantLibrary-only mirrors; they freeze with the rest. A skill added later, such as RC-A1-22's mirrors, goes into `.claude/` only and gets a "Claude-only skills" row.
3. **`AGENTS.md` per repository.** Frozen *outside* the marked blocks `<!-- repo-hygiene:begin/end -->` and `<!-- design-kit:begin/end -->`:
   - Hash the file with each marked block's interior removed.
   - Let the hygiene checker keep enforcing the block parity it already enforces (`repo_hygiene_check.py:725-732`).
   - Insert an F-01-style notice after line 2, e.g. "> Frozen <date> (`D-…`): codex disabled; `CLAUDE.md` is the live text."
   - This deviates from the Conductor, whose whole-file freeze let its design-kit block drift (F-A1-12). A3's CLAUDE.md/AGENTS.md reconciliation (B2) must land **before** the freeze commit, or the frozen AGENTS.md preserves pre-reconciliation text forever.
4. **`.agents/**`.**
   - The superproject `.agents/README.md` is rewritten as PlantLibrary's bridge file (RC-A1-20): freeze notice, unfreeze recipe, bridge table with `frozen` statuses, agent roster, Claude-only table with licences.
   - It is live, not frozen: it is the Claude-side record.
   - Suite `.agents/skills/impeccable` (PyApp, AndroidApp) and PyApp's `gui-validation` pointer are Kit or local runtime mirrors, not Codex. The Kit's `check-parity.mjs` covers the Kit folders. PyApp's pointer is replaced per RC-A1-23 or, if Codex mirrors must not move, left frozen as is (it lives under `.agents`, which the Conductor's checker does not freeze).
   - Suites get no README of their own; the superproject file covers all seven.
5. **What stops being enforced.** Option (a) stops the `.claude`↔`.codex` byte compare. Without a replacement, B1's new `.claude` copies would have no mirror check at all, hence §7.7's cross-repository compare.

### §7.7 The parity checker

**TARGET today** (`SW_Development/scripts/harness/check_harness_parity.py`, 133 lines):
- one function, `compare_trees`, over the superproject only (:58-85);
- a byte compare of `.claude/skills` vs `.codex/skills`, except `validate-real-stack/SKILL.md` (:22, :65-76);
- agent stem pairing `.md` ↔ `.toml` (:78-83);
- a self-test that plants one-sided drift in run-batch (:97-121);
- no CLAUDE.md/AGENTS.md compare, no suite, no freeze, no Kit exemption;
- result: `harness parity: pass`.

**The Conductor's** (824 lines):
- the two frozen checks (:213-272);
- proposal-fact checks: line count and Section Map range cited by CLAUDE.md and CONTEXT_INDEX.md (:342-421);
- Section Map row contents (:456-563);
- chunk-argv determinism-flag parity against `regression_scope.py` (:576-598);
- no mirrored ceiling constants in `scripts/harness/*.py` (:601-626);
- self-tests for the freeze and the argv parity (:654-760).

It depends on `src/conductor/tree_parity.py` (:156-158), which TARGET does not have. The closeout runs it as a preflight (`.agents/README.md:20-22`).

**What the extension needs** (B7, after Q-G-09):
1. **Multi-root.** Iterate the superproject and the six submodule folders when present. Skip with a printed line when a submodule is not checked out, so a standalone suite clone does not fail.
2. **Cross-repository mirror compare.** Each suite's `.claude/skills/{plan-batch,real-stack-testing,run-batch,test-driven-development,validate-real-stack}` and `.claude/agents/*.md`, plus the RC-A1-22 set per suite, must equal the superproject's, LF-normalized. This is the check the suite CLAUDE.md files already claim exists (F-A1-09).
3. **Freeze.** `FROZEN_AT` per repository; a digest table per repository for `.codex/**`; the AGENTS.md digest computed with marked-block interiors removed (§7.6 item 3); the Kit-folder exemption under `.codex/skills/`.
4. **Bridge coverage.** Every `.claude/skills/*` folder is either a frozen bridge row or a "Claude-only skills" row in `SW_Development/.agents/README.md`. This takes the place of the Conductor's `test_skill_mirror_parity.py` frozen-status rule.
5. **Run-batch commit contract strings** in every copy (RC-A1-21).
6. **PyApp only, optional (A2's call).** `check_no_mirrored_ceiling` and the chunk-argv parity over `PlantLibrary_PyApp/scripts/harness/`, since PyApp carries a ported `regression_scope.py`.
7. **Dropped as Conductor-specific.** The proposal-fact and Section Map checks.
8. **Kept from TARGET's current checker.** Dependency-free and stdlib only, with a `--self-test` extended to plant one drift per new check on temporary copies.

The B1 commit that edits `.claude/**` and the B7 commit that extends the checker must be ordered: freeze and checker first, then the `.claude` edits. Otherwise today's `.claude`↔`.codex` compare goes red on the first B1 edit. That ordering is how the Conductor sequenced it: "until it lands, no `.claude`-only edit is made" (`STATE.md:44170-44172`).
