"""Check the harness mirrors and the Codex freeze of the superproject and its submodules.

PlantLibrary variant, trimmed from the Orchestrator_System original and
extended for the multi-root layout (RC-A2-08, RC-A1-21, Q-A2-04 (a);
AUDIT_skills-and-agents §7.6 items 1-5, §7.7 items 1-5, 8). Six checks:

1. Codex freeze (B7-2; Q-G-09 (a), Q-A3-01 (a); the Conductor's
   ``D-2026-10-02-23`` made block-aware): in every repository whose
   ``FROZEN_AT`` row is set, ``.codex/**`` and ``AGENTS.md`` outside its
   installer-owned marker blocks are frozen at that commit -- kept, never
   deleted, not edited, not mirrored. Every file under ``.codex/`` must equal,
   by SHA-256 of its CRLF->LF-normalized bytes, its pinned content at the
   freeze commit; an added, removed or changed file is a diagnostic. Exempt:
   the four Kit-installed skill folders under ``.codex/skills/``
   (``KIT_INSTALLED_SKILLS``; the Design Template Kit installs and re-pins
   them, absent or not), ``settings.local.json`` and ``__pycache__/``.
   ``AGENTS.md`` must carry its repository's one-line banner exactly once, as
   line 1 or directly under the file's first heading line, and with the banner
   removed it must equal its pinned digest after ``frozen_agents_text``: each
   ``<!-- repo-hygiene:begin/end -->`` and ``<!-- design-kit:begin/end -->``
   region is removed, markers included, and blank-line runs collapse, so an
   installer that inserts, updates or moves its block is not drift (the
   hygiene checker owns the block's parity with ``CLAUDE.md``). The pins are
   written once from ``git show <freeze commit>:<path>`` by
   ``--print-freeze-table``, never from working-tree bytes. The freeze commit
   of a repository is the commit immediately preceding the commit of its
   freeze decision entry (its tree holds the pre-banner ``AGENTS.md``). A
   repository whose row is ``None`` is listed as pending, not failed.
2. Bridge coverage: every ``.claude/skills/*`` folder of the superproject is
   either a frozen bridge row (a table row naming ``.claude/skills/<name>``
   whose status cell says ``frozen``, ``runtime-adapted`` or
   ``Kit-installed``) or a row of the ``## Claude-only skills`` table in
   ``.agents/README.md``. Until that README carries the ``## Claude-only
   skills`` heading (its rewrite is B1-1) the check prints "README pending"
   and does not fail.
3. Suite mirrors: in each present submodule folder named by ``.gitmodules``,
   the shared skill folders (``SHARED_SKILLS`` plus the suite's row of
   ``SUITE_EXTRA_SKILLS``) and every superproject ``.claude/agents/*.md`` must
   equal the superproject's copy. A suite skill folder of the same name that is
   not in that set is listed, not compared (RC-A1-22 moves it in at B1).
4. Run-batch commit contract: every ``run-batch/SKILL.md`` copy under any
   ``.claude/skills`` or ``.codex/skills`` of a present repository holds the
   four commit-proposal strings and neither retired string.
5. Codex compare (``--with-codex-compare``, off by default since the freeze):
   the superproject's ``.claude/skills`` against ``.codex/skills`` file by
   file, ``validate-real-stack/SKILL.md`` allowed to differ, and the agent stem
   pairing ``.claude/agents/*.md`` <-> ``.codex/agents/*.toml``. Kept defined
   for the unfreeze.
6. Roots: a submodule folder that is absent or not checked out is skipped with
   a printed line, so a standalone suite clone does not fail.

To unfreeze codex in a repository: a later decision entry there; re-mirror
``.claude/**`` (and ``CLAUDE.md``'s text outside the blocks into ``AGENTS.md``)
for every change since its freeze commit; remove the banner; flip the
``frozen`` bridge statuses in ``.agents/README.md`` back to ``mirrored``; set
its ``FROZEN_AT`` row to ``None`` and drop its pins; for the superproject, make
``--with-codex-compare`` the default again.

Every content compare normalizes CRLF to LF first (the ``run-batch/SKILL.md``
mirrors are mixed in every repository; working-tree endings follow checkout).
``__pycache__/`` is ignored. ``--self-test`` is a static mode over temporary
copies: it plants one drift per check, proves each is reported, proves that a
CRLF<->LF flip and the exempt edits are not reported, restores the copy, then
checks the real tree.

Read-only, stdlib only, dependency-free so it runs in either coding harness on
Windows; only ``--print-freeze-table`` calls git. Exit 0 pass, 1 drift, 2 could
not run.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import hashlib  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import tempfile  # noqa: E402
from dataclasses import dataclass, field  # noqa: E402
from pathlib import Path  # noqa: E402


ALLOWED_SKILL_DIFFERENCES = frozenset({"validate-real-stack/SKILL.md"})
SHARED_SKILLS = (
    "plan-batch",
    "real-stack-testing",
    "run-batch",
    "test-driven-development",
    "validate-real-stack",
)
# RC-A1-22 (B1, after Q-A1-04 / Q-G-07): PlantLibrary-only skills mirrored into a
# suite join its row here in the same commit that mirrors them.
SUITE_EXTRA_SKILLS: dict[str, tuple[str, ...]] = {}
RUN_BATCH_REQUIRED = (
    "Propose the commit — never mutate Git",
    "Do not run `git add`, `git commit`, `git push`, `git reset`",
    "Commit: proposed for orchestrator",
    "CONDUCTOR_BATCH_COMMIT_PROPOSAL: <canonical-json>",
)
RUN_BATCH_FORBIDDEN = (
    "Commit: skipped: sandbox-protected Git metadata",
    "Commit command:",
)
IGNORED_PARTS = frozenset({"__pycache__"})
VERDICT = "harness parity"

# --- The Codex freeze (B7-2; see the module docstring) -----------------------
SUPERPROJECT = "."
KIT_INSTALLED_SKILLS = ("design-gate", "design-audit", "gallery-governance", "impeccable")
INSTALLER_BLOCKS = (
    ("<!-- repo-hygiene:begin -->", "<!-- repo-hygiene:end -->"),
    ("<!-- design-kit:begin -->", "<!-- design-kit:end -->"),
)
BANNER_FORM = "> Frozen {date} (`{decision}`): codex disabled; `CLAUDE.md` is the live text."
BRIDGE_README = Path(".agents") / "README.md"
CLAUDE_ONLY_HEADING = re.compile(r"^##\s+Claude-only skills\b")
BRIDGE_STATUSES = ("frozen", "runtime-adapted", "kit-installed")

# The freeze commit per repository ("." is the superproject; a suite is its
# folder name from .gitmodules) and the decision entry in that repository's
# hygiene/HYGIENE_DECISIONS.md that records it. None: not frozen yet (pending).
FROZEN_AT: dict[str, str | None] = {
    ".": "1cd675d",
    "PlantLibrary_AndroidApp": "f7b4e75",
    "PlantLibrary_Dashboard": "47ce96b",
    "PlantLibrary_PyApp": "5f91cdc",
    "PlantLibrary_Server": "590825d",
    "PlantLibrary_SharedContracts": "a3f863d",
    "PlantLibrary_Workspace": "8f7dad5",
}
FREEZE_DECISIONS: dict[str, str] = {
    ".": "D-2026-10-13-03",
    "PlantLibrary_AndroidApp": "D-2026-10-13-02",
    "PlantLibrary_Dashboard": "D-2026-10-13-02",
    "PlantLibrary_PyApp": "D-2026-10-13-02",
    "PlantLibrary_Server": "D-2026-10-13-02",
    "PlantLibrary_SharedContracts": "D-2026-10-13-03",
    "PlantLibrary_Workspace": "D-2026-10-13-03",
}
# Written by --print-freeze-table <repo>=<FROZEN_AT>; never edited by hand.
FROZEN_AGENTS_DIGESTS: dict[str, str] = {
    ".": "85c5e4ad5c9264aee144698670d710ab35bccc9ea4b507ee6041db089dd19de1",
    "PlantLibrary_AndroidApp": "8671e2be433ad05db6c2e4b61f22060c42fd17d79f59fed3898510fa2ea711bc",
    "PlantLibrary_Dashboard": "20ac862c1f5eccc9796953f38ae4b195d92c244a3187edd8259c2fd689728064",
    "PlantLibrary_PyApp": "30d83875e303c59055c3ff2b678599ce6001f4578669bb53866dc8a47138d418",
    "PlantLibrary_Server": "80c1477ba1454eea03f4d2bd04c4f4231b098a899e5358367e1a04dd2656a8f9",
    "PlantLibrary_SharedContracts": "21cab64829f1769c066eacca5ac8abe6c7882d143bcefca6171ccb74e3cd3570",
    "PlantLibrary_Workspace": "9923efccbaa0388871a1a7b8039b4bf78c37a15497caa6f4879f57defb287cee",
}
FROZEN_CODEX_DIGESTS: dict[str, dict[str, str]] = {
    ".": {
        "agents/batch-closeout-reviewer.toml": "e804e72dd81ed2606904b619fca197c22e398d01245a94a999dd3c223d89ff93",
        "agents/batch-plan-auditor.toml": "8b0731dc238029da99b2e7dc5952d325a1e0762abc4c02b1a46845c3c0a2855e",
        "agents/real-stack-validator.toml": "0b34280ee1f6f2350119bd2ae5e8e342d7dd76784dfc73a2b9ba1be66d942dd0",
        "hooks.json": "8b3e3c593986d6b0e32a4ceab950d6771e6dee44122f6cb9668b7741739345dd",
        "hooks/deny_git_commands.mjs": "9bbe26879081f1f7a03f77aa7fe177003383459fa40d2c0da71d0ae70e06c236",
        "skills/android-validation/SKILL.md": "2e79a54ae4ae398e14abafd4adfc9eab0df5d4407182dd3af83d7052d3ca7ceb",
        "skills/design-adoption/SKILL.md": "8859a6f3331b8ce483faf4647bd80c54b6379ed8980137b48c2140b89bb1212a",
        "skills/gui-validation/SKILL.md": "380cb38bc2d7a5db014638a7099c7320a89572e40f34ddbf00ff31880db2dd8f",
        "skills/plan-batch/SKILL.md": "b9a6de6474e8ee97808073683d85086579ac425773945397ab9f3b986e42559c",
        "skills/real-stack-testing/SKILL.md": "e21039f153889b1eb1df3a5d7f1a539cd74abd69e3227432fcea923c0d5a08bd",
        "skills/real-stack-testing/references/gui-testing.md": "2aa0cef011cb6cf669c35990c34f7f3ff12d8580ed097830dca8eba7b1479054",
        "skills/real-stack-testing/references/metered-validation.md": "52cfc0c068a439424759fcbc1c87c9cd918b221c9b2c8504aa6effa1682a1c6f",
        "skills/run-batch/SKILL.md": "c861dce96121c4e7cca097c372a0451e94ec9264a243300890fa30ba5e355dc7",
        "skills/sync-contracts/SKILL.md": "72f04fd925f148a81500541d484d0f41a321749c7253dc9802bb15e5b3764752",
        "skills/systematic-debugging/SKILL.md": "008cbf6b2a6098f24a4388c39c1b239f32125043d38d97896e4542e660e75e0b",
        "skills/systematic-debugging/condition-based-waiting-example.ts": "40ae5ebe497fdf310200e43fe986552546d0a22837c0d39e855db1cfd33eb88e",
        "skills/systematic-debugging/condition-based-waiting.md": "e89fec8400d6cd50f43407cec9fab50976ba4d55d0ec2eb51c0bd68036b54c26",
        "skills/systematic-debugging/defense-in-depth.md": "1e175fb86fc357e58c6aebf5441e481e1b7868b4380c0456b63a17eefbd18ba7",
        "skills/systematic-debugging/find-polluter.sh": "6462747eae9b175ac145b78bcfaeab755654a75e32637f08eb633f065a9e1d7c",
        "skills/systematic-debugging/root-cause-tracing.md": "6b0622269e098ca1399e123e553fd385f0b6412d88ef0e9c4f5a8ea9cf1cec7b",
        "skills/test-driven-development/SKILL.md": "7655284ceae6b2b5ade21dd6a7b17bee52e3aeca6e973244a629fa1a57834250",
        "skills/test-driven-development/testing-anti-patterns.md": "bde453bc258f06543987477c837939afaa774ea2acbd9f308d702fc452bc4283",
        "skills/ui-ux-pro-max/SKILL.md": "07b87b8998b51b9c234df031e31aa2a85cf86abeaa05efd984c2f66ca7f06d68",
        "skills/ui-ux-pro-max/data/charts.csv": "77d32cf4d9e78f80795baf391e1cc8f9ee137351aab29ca682938ec9d8ebe7e4",
        "skills/ui-ux-pro-max/data/colors.csv": "19a74a1fe858f92dc9213553bb6b8326b7f32dc6bfc0857668e2b4da32322f8a",
        "skills/ui-ux-pro-max/data/icons.csv": "351fe61ba45b8146c66de6ea7d67297654639d79a94f537b4d0bad570058c28f",
        "skills/ui-ux-pro-max/data/landing.csv": "51021dbadc40b0305c42f80c270eb515420440afe9f3482dfd048dc2475dbfbd",
        "skills/ui-ux-pro-max/data/products.csv": "6f9c9be6fdb53a415af273dac6221e87a418d1600da2ee39f974b997e880050e",
        "skills/ui-ux-pro-max/data/react-performance.csv": "904c8afcda229629545912dde0e8ac37503757131f0169f80b016f1f58c4fd3f",
        "skills/ui-ux-pro-max/data/stacks/astro.csv": "ad18dae3ab6d148d37d144592df80dc1825b6c9e86d9d2d68fdda77434206a37",
        "skills/ui-ux-pro-max/data/stacks/flutter.csv": "fe36d404c799781e8ba6e9a8179b45799ed5126a545528550cd2eb0f2346e8c5",
        "skills/ui-ux-pro-max/data/stacks/html-tailwind.csv": "7aef38e75c53559470afcfa91580a9917ca8b7dbf8b92110389e23e93703ac52",
        "skills/ui-ux-pro-max/data/stacks/jetpack-compose.csv": "6c8fd4b0391c342c12b0af15610cd5becbeccaef0bbe8dcfc01d928c3195d93e",
        "skills/ui-ux-pro-max/data/stacks/nextjs.csv": "e828ccc04843742f52f545a068e8a9ab0d2b97c0e771f7e93bf0cef74da05554",
        "skills/ui-ux-pro-max/data/stacks/nuxt-ui.csv": "05d6e74501b2b6a636faed32450622759f49a5bcafad971f5f4e7eba0eb7be71",
        "skills/ui-ux-pro-max/data/stacks/nuxtjs.csv": "f7a3f2d9542856d00199f85c6c023b7c284cc698e2e6e12d61afce2edacb24d6",
        "skills/ui-ux-pro-max/data/stacks/react-native.csv": "077aefc81d194895ecf7936b3ed298b978e36961f183e3a275f8acda19b5f621",
        "skills/ui-ux-pro-max/data/stacks/react.csv": "e5624ab41d33427d88e41d07581ce4eca59b37b36ab72a6ad43a9c8e2d0a1c72",
        "skills/ui-ux-pro-max/data/stacks/shadcn.csv": "395c2e415ef6f48a474acccdc8eb2c7258a6ed751a5037ba171a2d8823e02ded",
        "skills/ui-ux-pro-max/data/stacks/svelte.csv": "71af52d64f266c88070b91dbbaa900c2f8074b6baae9f35eaea6ba9cec6fd803",
        "skills/ui-ux-pro-max/data/stacks/swiftui.csv": "c9c2d2510f8e66281a2514e8dd0125a6b653b9ef53a71281b5e7dfe003d5b569",
        "skills/ui-ux-pro-max/data/stacks/vue.csv": "c2724915d3c11cd67263f25896cff721f787a0fdd8326002d31e9f5806dfd8f8",
        "skills/ui-ux-pro-max/data/styles.csv": "663ac9775e6f5b874b32d930fa0951591c45e39cde8ac7033278f42a0881c037",
        "skills/ui-ux-pro-max/data/typography.csv": "64695e05ac335ba534aff396c4ba9241c642f80ea53b424251d2669b71c4772b",
        "skills/ui-ux-pro-max/data/ui-reasoning.csv": "58fc52fff69f62709f8c7dd460de6f6693699ea820f24287f3301a427c2b554e",
        "skills/ui-ux-pro-max/data/ux-guidelines.csv": "e01943c433b2cad3040f19389b3b0455673758a569b7a927b5bedf65c989cb96",
        "skills/ui-ux-pro-max/data/web-interface.csv": "10bfc24e09a6a15db8309e6ef9b6881e1d4af97dffb7c99418aefb8e30df7d54",
        "skills/ui-ux-pro-max/scripts/core.py": "5459d1f04eea03dfb913742d0c03edc5065ac67f6227e4807fa87699662588cb",
        "skills/ui-ux-pro-max/scripts/design_system.py": "4da1d341f3c7749df51b51db4a543a48a427c3c746eb0e9882a1ab86acf3bb54",
        "skills/ui-ux-pro-max/scripts/search.py": "e924de555714fe612398d36f30c1d2514339a881d68a018fdbdc0b5589330de3",
        "skills/validate-real-stack/SKILL.md": "a57993ba64f2c7d3fff3c86cb223798a30a2fe56b7b84a346ba9845a39bef7d9",
        "skills/validate-real-stack/scripts/run_validation.ps1": "20bcc557b6f60bfe956768220a681a620647e54df86c9dcf8314a9f69edc15de",
        "skills/verify-stack/SKILL.md": "a4f0efd9c0188a40ba81ef9ba09af450ec5fd30d8753dd7b52382408c4a3c6da",
        "skills/webapp-testing/LICENSE.txt": "bc6b3af2f331cbc7fb0da1344efb2cbe5877a31498b4d70dbc7000f3405a1362",
        "skills/webapp-testing/SKILL.md": "61aeae7d032bd474ba0878ed417f967742c87cb755b70058f49c7d34da6eca70",
        "skills/webapp-testing/examples/console_logging.py": "ea46877289acb82da7e7ce59d0bc37c8977cd57e2a006d0c88d7a1c625bf95da",
        "skills/webapp-testing/examples/element_discovery.py": "d63c89604a22f8845d724e95dda45db49b1bf57c25ce0a83afbb7b8da3d402f0",
        "skills/webapp-testing/examples/static_html_automation.py": "9d533aafb875ee3ab8b8ebf8f5b9003ac8d999da3d09b285cce252e623140064",
        "skills/webapp-testing/scripts/with_server.py": "b0dcf4918935b795f4eda9821579b9902119235ff4447f687a30286e7d0925fd",
    },
    "PlantLibrary_AndroidApp": {
        "agents/batch-closeout-reviewer.toml": "e804e72dd81ed2606904b619fca197c22e398d01245a94a999dd3c223d89ff93",
        "agents/batch-plan-auditor.toml": "8b0731dc238029da99b2e7dc5952d325a1e0762abc4c02b1a46845c3c0a2855e",
        "agents/real-stack-validator.toml": "0b34280ee1f6f2350119bd2ae5e8e342d7dd76784dfc73a2b9ba1be66d942dd0",
        "skills/plan-batch/SKILL.md": "b9a6de6474e8ee97808073683d85086579ac425773945397ab9f3b986e42559c",
        "skills/real-stack-testing/SKILL.md": "e21039f153889b1eb1df3a5d7f1a539cd74abd69e3227432fcea923c0d5a08bd",
        "skills/real-stack-testing/references/gui-testing.md": "2aa0cef011cb6cf669c35990c34f7f3ff12d8580ed097830dca8eba7b1479054",
        "skills/real-stack-testing/references/metered-validation.md": "52cfc0c068a439424759fcbc1c87c9cd918b221c9b2c8504aa6effa1682a1c6f",
        "skills/run-batch/SKILL.md": "c861dce96121c4e7cca097c372a0451e94ec9264a243300890fa30ba5e355dc7",
        "skills/test-driven-development/SKILL.md": "7655284ceae6b2b5ade21dd6a7b17bee52e3aeca6e973244a629fa1a57834250",
        "skills/test-driven-development/testing-anti-patterns.md": "bde453bc258f06543987477c837939afaa774ea2acbd9f308d702fc452bc4283",
        "skills/validate-real-stack/SKILL.md": "a57993ba64f2c7d3fff3c86cb223798a30a2fe56b7b84a346ba9845a39bef7d9",
        "skills/validate-real-stack/scripts/run_validation.ps1": "20bcc557b6f60bfe956768220a681a620647e54df86c9dcf8314a9f69edc15de",
    },
    "PlantLibrary_Dashboard": {
        "agents/batch-closeout-reviewer.toml": "e804e72dd81ed2606904b619fca197c22e398d01245a94a999dd3c223d89ff93",
        "agents/batch-plan-auditor.toml": "8b0731dc238029da99b2e7dc5952d325a1e0762abc4c02b1a46845c3c0a2855e",
        "agents/real-stack-validator.toml": "0b34280ee1f6f2350119bd2ae5e8e342d7dd76784dfc73a2b9ba1be66d942dd0",
        "skills/plan-batch/SKILL.md": "b9a6de6474e8ee97808073683d85086579ac425773945397ab9f3b986e42559c",
        "skills/real-stack-testing/SKILL.md": "e21039f153889b1eb1df3a5d7f1a539cd74abd69e3227432fcea923c0d5a08bd",
        "skills/real-stack-testing/references/gui-testing.md": "2aa0cef011cb6cf669c35990c34f7f3ff12d8580ed097830dca8eba7b1479054",
        "skills/real-stack-testing/references/metered-validation.md": "52cfc0c068a439424759fcbc1c87c9cd918b221c9b2c8504aa6effa1682a1c6f",
        "skills/run-batch/SKILL.md": "c861dce96121c4e7cca097c372a0451e94ec9264a243300890fa30ba5e355dc7",
        "skills/test-driven-development/SKILL.md": "7655284ceae6b2b5ade21dd6a7b17bee52e3aeca6e973244a629fa1a57834250",
        "skills/test-driven-development/testing-anti-patterns.md": "bde453bc258f06543987477c837939afaa774ea2acbd9f308d702fc452bc4283",
        "skills/validate-real-stack/SKILL.md": "a57993ba64f2c7d3fff3c86cb223798a30a2fe56b7b84a346ba9845a39bef7d9",
        "skills/validate-real-stack/scripts/run_validation.ps1": "20bcc557b6f60bfe956768220a681a620647e54df86c9dcf8314a9f69edc15de",
    },
    "PlantLibrary_PyApp": {
        "agents/batch-closeout-reviewer.toml": "e804e72dd81ed2606904b619fca197c22e398d01245a94a999dd3c223d89ff93",
        "agents/batch-plan-auditor.toml": "8b0731dc238029da99b2e7dc5952d325a1e0762abc4c02b1a46845c3c0a2855e",
        "agents/real-stack-validator.toml": "0b34280ee1f6f2350119bd2ae5e8e342d7dd76784dfc73a2b9ba1be66d942dd0",
        "hooks.json": "18deea971a77aac7f54ac3756654975120fa7e8097f78a51a814acbf515db88d",
        "skills/plan-batch/SKILL.md": "b9a6de6474e8ee97808073683d85086579ac425773945397ab9f3b986e42559c",
        "skills/real-stack-testing/SKILL.md": "e21039f153889b1eb1df3a5d7f1a539cd74abd69e3227432fcea923c0d5a08bd",
        "skills/real-stack-testing/references/gui-testing.md": "2aa0cef011cb6cf669c35990c34f7f3ff12d8580ed097830dca8eba7b1479054",
        "skills/real-stack-testing/references/metered-validation.md": "52cfc0c068a439424759fcbc1c87c9cd918b221c9b2c8504aa6effa1682a1c6f",
        "skills/run-batch/SKILL.md": "c861dce96121c4e7cca097c372a0451e94ec9264a243300890fa30ba5e355dc7",
        "skills/test-driven-development/SKILL.md": "7655284ceae6b2b5ade21dd6a7b17bee52e3aeca6e973244a629fa1a57834250",
        "skills/test-driven-development/testing-anti-patterns.md": "bde453bc258f06543987477c837939afaa774ea2acbd9f308d702fc452bc4283",
        "skills/validate-real-stack/SKILL.md": "a57993ba64f2c7d3fff3c86cb223798a30a2fe56b7b84a346ba9845a39bef7d9",
        "skills/validate-real-stack/scripts/run_validation.ps1": "20bcc557b6f60bfe956768220a681a620647e54df86c9dcf8314a9f69edc15de",
    },
    "PlantLibrary_Server": {
        "agents/batch-closeout-reviewer.toml": "e804e72dd81ed2606904b619fca197c22e398d01245a94a999dd3c223d89ff93",
        "agents/batch-plan-auditor.toml": "8b0731dc238029da99b2e7dc5952d325a1e0762abc4c02b1a46845c3c0a2855e",
        "agents/real-stack-validator.toml": "0b34280ee1f6f2350119bd2ae5e8e342d7dd76784dfc73a2b9ba1be66d942dd0",
        "skills/plan-batch/SKILL.md": "b9a6de6474e8ee97808073683d85086579ac425773945397ab9f3b986e42559c",
        "skills/real-stack-testing/SKILL.md": "e21039f153889b1eb1df3a5d7f1a539cd74abd69e3227432fcea923c0d5a08bd",
        "skills/real-stack-testing/references/gui-testing.md": "2aa0cef011cb6cf669c35990c34f7f3ff12d8580ed097830dca8eba7b1479054",
        "skills/real-stack-testing/references/metered-validation.md": "52cfc0c068a439424759fcbc1c87c9cd918b221c9b2c8504aa6effa1682a1c6f",
        "skills/run-batch/SKILL.md": "c861dce96121c4e7cca097c372a0451e94ec9264a243300890fa30ba5e355dc7",
        "skills/test-driven-development/SKILL.md": "7655284ceae6b2b5ade21dd6a7b17bee52e3aeca6e973244a629fa1a57834250",
        "skills/test-driven-development/testing-anti-patterns.md": "bde453bc258f06543987477c837939afaa774ea2acbd9f308d702fc452bc4283",
        "skills/validate-real-stack/SKILL.md": "a57993ba64f2c7d3fff3c86cb223798a30a2fe56b7b84a346ba9845a39bef7d9",
        "skills/validate-real-stack/scripts/run_validation.ps1": "20bcc557b6f60bfe956768220a681a620647e54df86c9dcf8314a9f69edc15de",
    },
    "PlantLibrary_SharedContracts": {
        "agents/batch-closeout-reviewer.toml": "e804e72dd81ed2606904b619fca197c22e398d01245a94a999dd3c223d89ff93",
        "agents/batch-plan-auditor.toml": "8b0731dc238029da99b2e7dc5952d325a1e0762abc4c02b1a46845c3c0a2855e",
        "agents/real-stack-validator.toml": "0b34280ee1f6f2350119bd2ae5e8e342d7dd76784dfc73a2b9ba1be66d942dd0",
        "skills/plan-batch/SKILL.md": "b9a6de6474e8ee97808073683d85086579ac425773945397ab9f3b986e42559c",
        "skills/real-stack-testing/SKILL.md": "e21039f153889b1eb1df3a5d7f1a539cd74abd69e3227432fcea923c0d5a08bd",
        "skills/real-stack-testing/references/gui-testing.md": "2aa0cef011cb6cf669c35990c34f7f3ff12d8580ed097830dca8eba7b1479054",
        "skills/real-stack-testing/references/metered-validation.md": "52cfc0c068a439424759fcbc1c87c9cd918b221c9b2c8504aa6effa1682a1c6f",
        "skills/run-batch/SKILL.md": "c861dce96121c4e7cca097c372a0451e94ec9264a243300890fa30ba5e355dc7",
        "skills/test-driven-development/SKILL.md": "7655284ceae6b2b5ade21dd6a7b17bee52e3aeca6e973244a629fa1a57834250",
        "skills/test-driven-development/testing-anti-patterns.md": "bde453bc258f06543987477c837939afaa774ea2acbd9f308d702fc452bc4283",
        "skills/validate-real-stack/SKILL.md": "a57993ba64f2c7d3fff3c86cb223798a30a2fe56b7b84a346ba9845a39bef7d9",
        "skills/validate-real-stack/scripts/run_validation.ps1": "20bcc557b6f60bfe956768220a681a620647e54df86c9dcf8314a9f69edc15de",
    },
    "PlantLibrary_Workspace": {
        "agents/batch-closeout-reviewer.toml": "e804e72dd81ed2606904b619fca197c22e398d01245a94a999dd3c223d89ff93",
        "agents/batch-plan-auditor.toml": "8b0731dc238029da99b2e7dc5952d325a1e0762abc4c02b1a46845c3c0a2855e",
        "agents/real-stack-validator.toml": "0b34280ee1f6f2350119bd2ae5e8e342d7dd76784dfc73a2b9ba1be66d942dd0",
        "skills/plan-batch/SKILL.md": "b9a6de6474e8ee97808073683d85086579ac425773945397ab9f3b986e42559c",
        "skills/real-stack-testing/SKILL.md": "e21039f153889b1eb1df3a5d7f1a539cd74abd69e3227432fcea923c0d5a08bd",
        "skills/real-stack-testing/references/gui-testing.md": "2aa0cef011cb6cf669c35990c34f7f3ff12d8580ed097830dca8eba7b1479054",
        "skills/real-stack-testing/references/metered-validation.md": "52cfc0c068a439424759fcbc1c87c9cd918b221c9b2c8504aa6effa1682a1c6f",
        "skills/run-batch/SKILL.md": "c861dce96121c4e7cca097c372a0451e94ec9264a243300890fa30ba5e355dc7",
        "skills/test-driven-development/SKILL.md": "7655284ceae6b2b5ade21dd6a7b17bee52e3aeca6e973244a629fa1a57834250",
        "skills/test-driven-development/testing-anti-patterns.md": "bde453bc258f06543987477c837939afaa774ea2acbd9f308d702fc452bc4283",
        "skills/validate-real-stack/SKILL.md": "a57993ba64f2c7d3fff3c86cb223798a30a2fe56b7b84a346ba9845a39bef7d9",
        "skills/validate-real-stack/scripts/run_validation.ps1": "20bcc557b6f60bfe956768220a681a620647e54df86c9dcf8314a9f69edc15de",
    },
}


@dataclass(frozen=True)
class ParityResult:
    """The deterministic diagnostics produced by one parity comparison."""

    diagnostics: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.diagnostics


@dataclass
class Report:
    diagnostics: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    suites: list[str] = field(default_factory=list)
    frozen: list[str] = field(default_factory=list)
    pending: list[str] = field(default_factory=list)
    bridge: str = "not run"

    @property
    def ok(self) -> bool:
        return not self.diagnostics


def repository_root() -> Path:
    """Return the superproject root independently of the current directory."""

    return Path(__file__).resolve().parents[2]


def _lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def _lf_digest(data: bytes) -> str:
    return hashlib.sha256(_lf(data)).hexdigest()


def _file_inventory(root: Path) -> dict[str, bytes]:
    if not root.is_dir():
        raise FileNotFoundError(f"missing directory: {root}")
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file() and not IGNORED_PARTS.intersection(path.relative_to(root).parts)
    }


def _agent_stems(root: Path, suffix: str) -> set[str]:
    if not root.is_dir():
        raise FileNotFoundError(f"missing directory: {root}")
    return {path.stem for path in root.glob(f"*{suffix}") if path.is_file()}


def compare_trees(root: Path) -> ParityResult:
    """The superproject's ``.claude``/``.codex`` compare: skills by LF content, agents by stem."""

    claude_skills = _file_inventory(root / ".claude" / "skills")
    codex_skills = _file_inventory(root / ".codex" / "skills")
    diagnostics: list[str] = []

    for relative_path in sorted(set(claude_skills) | set(codex_skills)):
        in_claude = relative_path in claude_skills
        in_codex = relative_path in codex_skills
        if not in_claude:
            diagnostics.append(f"skill missing from Claude: {relative_path}")
        elif not in_codex:
            diagnostics.append(f"skill missing from Codex: {relative_path}")
        elif (
            _lf(claude_skills[relative_path]) != _lf(codex_skills[relative_path])
            and relative_path not in ALLOWED_SKILL_DIFFERENCES
        ):
            diagnostics.append(f"skill byte-different: {relative_path}")

    claude_agents = _agent_stems(root / ".claude" / "agents", ".md")
    codex_agents = _agent_stems(root / ".codex" / "agents", ".toml")
    for stem in sorted(claude_agents - codex_agents):
        diagnostics.append(f"agent missing from Codex: {stem}")
    for stem in sorted(codex_agents - claude_agents):
        diagnostics.append(f"agent missing from Claude: {stem}")

    return ParityResult(tuple(diagnostics))


# --- Codex freeze ------------------------------------------------------------


def freeze_banner(repository: str) -> str:
    """The one-line ``AGENTS.md`` banner of a repository, naming its freeze entry."""

    decision = FREEZE_DECISIONS[repository]
    return BANNER_FORM.format(date=decision[2:12], decision=decision)


def is_frozen_codex_path(relative: str) -> bool:
    """Whether a path relative to ``.codex/`` is under the freeze."""

    parts = relative.split("/")
    if IGNORED_PARTS.intersection(parts) or relative == "settings.local.json":
        return False
    return not (len(parts) >= 2 and parts[0] == "skills" and parts[1] in KIT_INSTALLED_SKILLS)


def _without_installer_blocks(lines: list[str]) -> list[str]:
    """The lines outside every installer-owned marker block, markers removed too."""

    kept: list[str] = []
    closing: str | None = None
    opened_at = 0
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if closing is None:
            closer = next((end for begin, end in INSTALLER_BLOCKS if stripped == begin), None)
            if closer is None:
                kept.append(line)
            else:
                closing, opened_at = closer, number
        elif stripped == closing:
            closing = None
    if closing is not None:
        raise ValueError(f"marker block opened at line {opened_at} is never closed ({closing} missing)")
    return kept


def frozen_agents_text(data: bytes) -> bytes:
    """``AGENTS.md`` as the freeze digests it: LF, installer blocks removed, blank runs collapsed."""

    lines = _lf(data).decode("utf-8", "surrogateescape").split("\n")
    collapsed: list[str] = []
    for line in _without_installer_blocks(lines):
        if not line.strip():
            if collapsed and collapsed[-1] == "":
                continue
            line = ""
        collapsed.append(line)
    while collapsed and collapsed[0] == "":
        collapsed.pop(0)
    while collapsed and collapsed[-1] == "":
        collapsed.pop()
    return ("\n".join(collapsed) + "\n").encode("utf-8", "surrogateescape")


def _first_heading_index(lines: list[str]) -> int | None:
    """Index of the first ATX heading line outside code fences and installer blocks."""

    in_fence = False
    closing: str | None = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if closing is not None:
            if stripped == closing:
                closing = None
            continue
        closer = next((end for begin, end in INSTALLER_BLOCKS if stripped == begin), None)
        if closer is not None:
            closing = closer
            continue
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if not in_fence and re.match(r"^#{1,6}\s", line):
            return index
    return None


def check_codex_frozen(repository: Path, label: str, pins: dict[str, str]) -> list[str]:
    """Every frozen file under ``.codex/`` is unchanged since the freeze commit."""

    codex = repository / ".codex"
    if not codex.is_dir():
        return [f"{label}.codex: missing since the freeze"]
    actual = {
        relative: _lf_digest(data)
        for relative, data in _file_inventory(codex).items()
        if is_frozen_codex_path(relative)
    }
    diagnostics: list[str] = []
    for relative in sorted(set(actual) | set(pins)):
        if relative not in actual:
            change = "removed"
        elif relative not in pins:
            change = "added"
        elif actual[relative] != pins[relative]:
            change = "changed"
        else:
            continue
        diagnostics.append(f"{label}.codex/{relative}: {change} since the freeze")
    return diagnostics


def check_agents_frozen(repository: Path, label: str, key: str, pin: str) -> list[str]:
    """``AGENTS.md`` carries its banner once, in place, and is unchanged outside its blocks."""

    path = repository / "AGENTS.md"
    if not path.is_file():
        return [f"{label}AGENTS.md: missing since the freeze"]
    lines = _lf(path.read_bytes()).decode("utf-8", "surrogateescape").split("\n")
    banner = freeze_banner(key)
    hits = [index for index, line in enumerate(lines) if line == banner]
    diagnostics: list[str] = []
    if not hits:
        diagnostics.append(f"{label}AGENTS.md: freeze banner missing ({banner!r})")
    elif len(hits) > 1:
        diagnostics.append(f"{label}AGENTS.md: freeze banner present {len(hits)} times")
    else:
        index = hits[0]
        rest = lines[:index] + lines[index + 1 :]
        heading = _first_heading_index(rest)
        allowed = {0} | ({heading + 1} if heading is not None else set())
        if index not in allowed:
            diagnostics.append(
                f"{label}AGENTS.md: freeze banner at line {index + 1}, not line 1 or directly under"
                " the first heading line"
            )
        lines = rest
    try:
        digest = hashlib.sha256(frozen_agents_text("\n".join(lines).encode("utf-8", "surrogateescape"))).hexdigest()
    except ValueError as error:
        return diagnostics + [f"{label}AGENTS.md: {error}"]
    if digest != pin:
        diagnostics.append(
            f"{label}AGENTS.md: changed since the freeze outside its installer blocks"
            " (edit CLAUDE.md, the live text, instead)"
        )
    return diagnostics


def check_freeze(repository: Path, label: str, key: str, report: Report) -> None:
    if FROZEN_AT.get(key) is None:
        report.pending.append(key)
        return
    if key not in FROZEN_AGENTS_DIGESTS or key not in FROZEN_CODEX_DIGESTS or key not in FREEZE_DECISIONS:
        report.diagnostics.append(f"{label or './'}: freeze table incomplete for {key} (FROZEN_AT set, pins missing)")
        return
    found = check_codex_frozen(repository, label, FROZEN_CODEX_DIGESTS[key])
    found += check_agents_frozen(repository, label, key, FROZEN_AGENTS_DIGESTS[key])
    report.diagnostics.extend(found)
    if not found:
        report.frozen.append(key)


def freeze_table(root: Path, key: str, commit: str) -> str:
    """The pins of one repository, read from ``git show <commit>:<path>`` (never the working tree)."""

    repository = root if key == SUPERPROJECT else root / key

    def git(*arguments: str) -> bytes:
        return subprocess.run(
            ["git", "-C", str(repository), *arguments], check=True, capture_output=True
        ).stdout

    listed = git("ls-tree", "-r", "--name-only", "-z", commit, "--", ".codex").decode("utf-8").split("\0")
    codex = {}
    for path in sorted(p for p in listed if p):
        relative = path[len(".codex/") :]
        if is_frozen_codex_path(relative):
            codex[relative] = _lf_digest(git("show", f"{commit}:{path}"))
    agents = hashlib.sha256(frozen_agents_text(git("show", f"{commit}:AGENTS.md"))).hexdigest()
    out = [f"# {key} @ {commit}", "FROZEN_AGENTS_DIGESTS:", f'    "{key}": "{agents}",', "FROZEN_CODEX_DIGESTS:"]
    out.append(f'    "{key}": {{')
    out.extend(f'        "{relative}": "{digest}",' for relative, digest in codex.items())
    out.append("    },")
    return "\n".join(out)


# --- Bridge coverage ---------------------------------------------------------


def check_bridge_coverage(root: Path) -> tuple[list[str], str]:
    """Every superproject ``.claude/skills/*`` folder is a frozen bridge row or a Claude-only row."""

    readme = root / BRIDGE_README
    if not readme.is_file():
        return [], "README pending (no .agents/README.md; B1-1 writes it)"
    lines = _lf(readme.read_bytes()).decode("utf-8", "replace").split("\n")
    if not any(CLAUDE_ONLY_HEADING.match(line) for line in lines):
        return [], "README pending (no '## Claude-only skills' table until B1-1 rewrites .agents/README.md)"
    bridged: set[str] = set()
    claude_only: set[str] = set()
    section = ""
    for line in lines:
        if line.startswith("## "):
            section = line
            continue
        match = re.match(r"^\|\s*`([^`]+)`\s*\|(.*)\|\s*$", line)
        if not match:
            continue
        cells = [cell.strip() for cell in match.group(2).split("|")]
        if not cells or ".claude/skills/" not in cells[0].lower():
            continue
        if CLAUDE_ONLY_HEADING.match(section):
            claude_only.add(match.group(1))
        elif any(status in cells[-1].lower() for status in BRIDGE_STATUSES):
            bridged.add(match.group(1))
    folders = sorted(
        p.name for p in (root / ".claude" / "skills").iterdir() if p.is_dir() and p.name not in IGNORED_PARTS
    )
    diagnostics = [
        f"bridge coverage: .claude/skills/{name} has neither a frozen bridge row nor a Claude-only row"
        f" in {BRIDGE_README.as_posix()}"
        for name in folders
        if name not in bridged and name not in claude_only
    ]
    return diagnostics, f"checked ({len(folders)} skill folders)"


# --- Suites ------------------------------------------------------------------


def submodule_folders(root: Path) -> list[str]:
    gitmodules = root / ".gitmodules"
    if not gitmodules.is_file():
        return []
    names = []
    for line in gitmodules.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*path\s*=\s*(.+?)\s*$", line)
        if match:
            names.append(match.group(1))
    return sorted(names)


def compare_suite(
    root: Path, suite: str, extra_skills: dict[str, tuple[str, ...]]
) -> tuple[list[str], list[str]]:
    """One suite's shared skill folders and agents against the superproject's (LF content)."""

    diagnostics: list[str] = []
    notes: list[str] = []
    super_skills = root / ".claude" / "skills"
    suite_skills = root / suite / ".claude" / "skills"
    compared = tuple(SHARED_SKILLS) + tuple(extra_skills.get(suite, ()))
    for skill in compared:
        source = super_skills / skill
        mirror = suite_skills / skill
        if not source.is_dir():
            diagnostics.append(f"{suite}: superproject has no skill folder {skill}")
            continue
        if not mirror.is_dir():
            diagnostics.append(f"{suite}: missing shared skill folder {skill}")
            continue
        expected = _file_inventory(source)
        actual = _file_inventory(mirror)
        for relative in sorted(set(expected) | set(actual)):
            if relative not in actual:
                diagnostics.append(f"{suite}: skill file missing: {skill}/{relative}")
            elif relative not in expected:
                diagnostics.append(f"{suite}: skill file not in the superproject: {skill}/{relative}")
            elif _lf(expected[relative]) != _lf(actual[relative]):
                diagnostics.append(f"{suite}: skill differs from the superproject's: {skill}/{relative}")
    if suite_skills.is_dir():
        uncompared = sorted(
            p.name
            for p in suite_skills.iterdir()
            if p.is_dir() and p.name not in compared and (super_skills / p.name).is_dir()
        )
        if uncompared:
            notes.append(f"{suite}: same-name skill folders listed, not compared: {', '.join(uncompared)}")

    super_agents = root / ".claude" / "agents"
    suite_agents = root / suite / ".claude" / "agents"
    for agent in sorted(super_agents.glob("*.md")):
        mirror = suite_agents / agent.name
        if not mirror.is_file():
            diagnostics.append(f"{suite}: agent missing: {agent.name}")
        elif _lf(mirror.read_bytes()) != _lf(agent.read_bytes()):
            diagnostics.append(f"{suite}: agent differs from the superproject's: {agent.name}")
    if suite_agents.is_dir():
        extra = sorted(
            p.name for p in suite_agents.glob("*.md") if not (super_agents / p.name).is_file()
        )
        if extra:
            notes.append(f"{suite}: suite-only agents listed, not compared: {', '.join(extra)}")
    return diagnostics, notes


def check_run_batch_contract(repository: Path, label: str) -> list[str]:
    """The commit-proposal strings in every run-batch copy of one repository (RC-A1-21)."""

    diagnostics: list[str] = []
    for harness in (".claude", ".codex"):
        path = repository / harness / "skills" / "run-batch" / "SKILL.md"
        if not path.is_file():
            continue
        text = _lf(path.read_bytes()).decode("utf-8", "replace")
        where = f"{label}{harness}/skills/run-batch/SKILL.md"
        for needle in RUN_BATCH_REQUIRED:
            if needle not in text:
                diagnostics.append(f"run-batch commit contract: {where} lacks {needle!r}")
        for needle in RUN_BATCH_FORBIDDEN:
            if needle in text:
                diagnostics.append(f"run-batch commit contract: {where} carries retired {needle!r}")
    return diagnostics


def check_all(
    root: Path,
    with_codex_compare: bool = False,
    extra_skills: dict[str, tuple[str, ...]] | None = None,
) -> Report:
    extras = SUITE_EXTRA_SKILLS if extra_skills is None else extra_skills
    report = Report()
    if with_codex_compare:
        report.diagnostics.extend(compare_trees(root).diagnostics)
    check_freeze(root, "", SUPERPROJECT, report)
    bridge_diagnostics, report.bridge = check_bridge_coverage(root)
    report.diagnostics.extend(bridge_diagnostics)
    report.diagnostics.extend(check_run_batch_contract(root, ""))
    for suite in submodule_folders(root):
        folder = root / suite
        if not (folder.is_dir() and (folder / ".git").exists()):
            report.skipped.append(suite)
            continue
        report.suites.append(suite)
        diagnostics, notes = compare_suite(root, suite, extras)
        report.diagnostics.extend(diagnostics)
        report.notes.extend(notes)
        check_freeze(folder, f"{suite}/", suite, report)
        report.diagnostics.extend(check_run_batch_contract(folder, f"{suite}/"))
    return report


def _print_report(report: Report, with_codex_compare: bool) -> int:
    for suite in report.skipped:
        print(f"{VERDICT}: skipped {suite} (submodule folder not present)")
    for key in report.pending:
        print(f"{VERDICT}: note: codex freeze pending for {key} (no FROZEN_AT row yet)")
    print(f"{VERDICT}: note: bridge coverage: {report.bridge}")
    for note in report.notes:
        print(f"{VERDICT}: note: {note}")
    for diagnostic in report.diagnostics:
        print(f"{VERDICT}: FAIL: {diagnostic}")
    checked = 1 + len(report.suites)
    scope = (
        f"{1 + len(report.suites)} repositories (superproject + {len(report.suites)} suites,"
        f" {len(report.skipped)} skipped); codex freeze green in {len(report.frozen)} of {checked}"
        f" ({len(report.pending)} pending); codex compare {'on' if with_codex_compare else 'off'};"
        f" bridge coverage {report.bridge.split(' (')[0]}; {len(SHARED_SKILLS)} shared skills + agents"
        " per suite; run-batch commit contract"
    )
    if report.ok:
        print(f"{VERDICT}: pass — {scope}")
        return 0
    print(f"{VERDICT}: fail — {len(report.diagnostics)} diagnostics; {scope}")
    return 1


# --- Self-test ---------------------------------------------------------------


def _copy_repository(source: Path, target: Path) -> None:
    ignore = shutil.ignore_patterns("__pycache__")
    for harness in (".claude",):
        for part in ("skills", "agents"):
            if (source / harness / part).is_dir():
                shutil.copytree(source / harness / part, target / harness / part, ignore=ignore)
    if (source / ".codex").is_dir():
        shutil.copytree(source / ".codex", target / ".codex", ignore=ignore)
    for name in ("AGENTS.md", BRIDGE_README.as_posix()):
        if (source / name).is_file():
            (target / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source / name, target / name)


def _copy_mirrors(source_root: Path, target_root: Path) -> None:
    target_root.mkdir(parents=True)
    shutil.copy2(source_root / ".gitmodules", target_root / ".gitmodules")
    _copy_repository(source_root, target_root)
    for suite in submodule_folders(source_root):
        folder = source_root / suite
        if not (folder.is_dir() and (folder / ".git").exists()):
            continue
        (target_root / suite).mkdir()
        (target_root / suite / ".git").write_text("gitdir: self-test copy\n", encoding="utf-8")
        _copy_repository(folder, target_root / suite)


def _flip_line_endings(data: bytes) -> bytes:
    if b"\r\n" in data:
        return data.replace(b"\r\n", b"\n")
    return data.replace(b"\n", b"\r\n")


def _replace_lines(path: Path, edit) -> None:
    """Rewrite a text file through ``edit(lines) -> lines``, keeping its line endings."""

    data = path.read_bytes()
    eol = "\r\n" if b"\r\n" in data else "\n"
    lines = _lf(data).decode("utf-8", "surrogateescape").split("\n")
    path.write_bytes(eol.join(edit(lines)).encode("utf-8", "surrogateescape"))


def run_self_test(source_root: Path, with_codex_compare: bool) -> int:
    """Plant one drift per check in a temporary copy, prove each is caught, restore, pass."""

    suites = [
        s
        for s in submodule_folders(source_root)
        if (source_root / s).is_dir() and (source_root / s / ".git").exists()
    ]
    if not suites:
        print(f"{VERDICT} self-test: error — no submodule folder present to plant suite drifts in")
        return 2
    suite = suites[0]
    frozen_suites = [s for s in suites if FROZEN_AT.get(s)]
    failures: list[str] = []
    detected: list[str] = []
    with tempfile.TemporaryDirectory(prefix="harness-parity-") as temporary:
        copy = Path(temporary) / "repository"
        _copy_mirrors(source_root, copy)
        baseline = check_all(copy, with_codex_compare)
        base_set = set(baseline.diagnostics)

        def plant(name: str, path: Path, mutate, expected: str, *, extras=None, absent=False, silent=False) -> None:
            backup = Path(temporary) / "backup"
            was_dir = path.is_dir()
            original = b""
            if was_dir:
                shutil.copytree(path, backup)
            else:
                original = path.read_bytes()
            mutate(path)
            result = check_all(copy, with_codex_compare, extras)
            new = [d for d in result.diagnostics if d not in base_set]
            if absent:
                ok = not new and expected in result.skipped
                label = f"{name}: skipped {expected}, no diagnostic"
            elif silent:
                ok = not new
                label = f"{name}: {expected}, no diagnostic"
            else:
                ok = any(expected in d for d in new)
                label = f"{name}: {expected}"
            (detected if ok else failures).append(label if ok else f"{label} (new: {new})")
            if was_dir:
                if path.exists():
                    shutil.rmtree(path)
                shutil.copytree(backup, path)
                shutil.rmtree(backup)
            else:
                path.write_bytes(original)
            restored = check_all(copy, with_codex_compare)
            if set(restored.diagnostics) != base_set:
                failures.append(f"{name}: restored copy differs from the baseline")

        skills = copy / suite / ".claude" / "skills"
        agents = copy / suite / ".claude" / "agents"
        append = lambda p: p.write_bytes(p.read_bytes() + b"\n<!-- temporary one-sided drift -->\n")  # noqa: E731

        if with_codex_compare:
            plant("codex compare", copy / ".claude" / "skills" / "run-batch" / "SKILL.md", append,
                  "skill byte-different: run-batch/SKILL.md")
        plant("suite skill", skills / "plan-batch" / "SKILL.md", append,
              f"{suite}: skill differs from the superproject's: plan-batch/SKILL.md")
        plant("suite skill folder", skills / "test-driven-development", shutil.rmtree,
              f"{suite}: missing shared skill folder test-driven-development")
        first_agent = sorted((copy / ".claude" / "agents").glob("*.md"))[0].name
        plant("suite agent", agents / first_agent, append,
              f"{suite}: agent differs from the superproject's: {first_agent}")
        plant("suite agent missing", agents / first_agent, lambda p: p.unlink(),
              f"{suite}: agent missing: {first_agent}")
        plant("extra-skill table", skills / "plan-batch" / "SKILL.md", lambda p: None,
              f"{suite}: missing shared skill folder systematic-debugging",
              extras={suite: ("systematic-debugging",)})
        plant("run-batch required string", skills / "run-batch" / "SKILL.md",
              lambda p: p.write_bytes(p.read_bytes().replace(b"Commit: proposed for orchestrator", b"Commit: x")),
              f"{suite}/.claude/skills/run-batch/SKILL.md lacks 'Commit: proposed for orchestrator'")
        plant("run-batch retired string", copy / ".codex" / "skills" / "run-batch" / "SKILL.md",
              lambda p: p.write_bytes(p.read_bytes() + b"\nCommit command:\n"),
              ".codex/skills/run-batch/SKILL.md carries retired 'Commit command:'")

        # The Codex freeze: one frozen suite's .codex, the superproject's AGENTS.md.
        if FROZEN_AT.get(SUPERPROJECT) and frozen_suites:
            fsuite = frozen_suites[0]
            fcodex = copy / fsuite / ".codex"
            ftoml = sorted((fcodex / "agents").glob("*.toml"))[0]
            frelative = ftoml.relative_to(fcodex).as_posix()
            plant("freeze: .codex file changed", ftoml, append,
                  f"{fsuite}/.codex/{frelative}: changed since the freeze")
            plant("freeze: .codex file removed", ftoml, lambda p: p.unlink(),
                  f"{fsuite}/.codex/{frelative}: removed since the freeze")
            plant("freeze: .codex file added", fcodex / "skills" / "run-batch",
                  lambda p: (p / "EXTRA.md").write_bytes(b"one-sided\n"),
                  f"{fsuite}/.codex/skills/run-batch/EXTRA.md: added since the freeze")
            plant("freeze: Kit folder exempt", fcodex / "skills",
                  lambda p: ((p / "design-gate").mkdir(), (p / "design-gate" / "SKILL.md").write_bytes(b"kit\n")),
                  "a Kit-installed .codex/skills/design-gate/SKILL.md", silent=True)
            plant("freeze: settings.local.json exempt", fcodex,
                  lambda p: (p / "settings.local.json").write_bytes(b"{}\n"),
                  ".codex/settings.local.json", silent=True)
            plant("freeze: .codex CRLF<->LF flip", ftoml,
                  lambda p: p.write_bytes(_flip_line_endings(p.read_bytes())),
                  f"a line-ending flip of .codex/{frelative}", silent=True)

            agents_md = copy / "AGENTS.md"
            banner = freeze_banner(SUPERPROJECT)
            plant("freeze: AGENTS.md edited outside a block", agents_md,
                  lambda p: _replace_lines(p, lambda ls: ls[:-1] + ["temporary drift", ls[-1]]),
                  "AGENTS.md: changed since the freeze outside its installer blocks")
            plant("freeze: AGENTS.md edited inside the hygiene block", agents_md,
                  lambda p: _replace_lines(p, lambda ls: [
                      x for line in ls for x in (["installer re-sync line", line] if line.strip() == INSTALLER_BLOCKS[0][1] else [line])
                  ]),
                  "an edit inside <!-- repo-hygiene:begin/end -->", silent=True)
            design_block = [INSTALLER_BLOCKS[1][0], "## Design rules", "body", INSTALLER_BLOCKS[1][1]]
            plant("freeze: design-kit block appended (installer shape)", agents_md,
                  lambda p: _replace_lines(p, lambda ls: ls[:-1] + ["", *design_block, ""]),
                  "a design-kit block appended at the end", silent=True)

            def insert_before_first_heading(ls: list[str]) -> list[str]:
                at = next(i for i, line in enumerate(ls) if line.startswith("#"))
                before = ls[:at]
                while before and not before[-1].strip():
                    before.pop()
                return [*before, *([""] if before else []), *design_block, "", *ls[at:]]

            plant("freeze: design-kit block inserted before a heading (installer shape)", agents_md,
                  lambda p: _replace_lines(p, insert_before_first_heading),
                  "a design-kit block inserted before the first heading", silent=True)
            plant("freeze: AGENTS.md CRLF<->LF flip", agents_md,
                  lambda p: p.write_bytes(_flip_line_endings(p.read_bytes())),
                  "a line-ending flip of AGENTS.md", silent=True)
            plant("freeze: banner removed", agents_md,
                  lambda p: _replace_lines(p, lambda ls: [line for line in ls if line != banner]),
                  "AGENTS.md: freeze banner missing")
            plant("freeze: banner moved", agents_md,
                  lambda p: _replace_lines(p, lambda ls: [line for line in ls if line != banner] + [banner]),
                  "AGENTS.md: freeze banner at line")
            plant("freeze: unterminated marker block", agents_md,
                  lambda p: _replace_lines(p, lambda ls: [line for line in ls if line.strip() != INSTALLER_BLOCKS[0][1]]),
                  "AGENTS.md: marker block opened at line")
        else:
            failures.append("freeze plants: no FROZEN_AT row for the superproject and a suite")

        # Bridge coverage: a rewritten README that misses one skill folder fails.
        readme = copy / BRIDGE_README
        names = sorted(p.name for p in (copy / ".claude" / "skills").iterdir() if p.is_dir())
        rows = "\n".join(f"| `{n}` | `../.claude/skills/{n}` | original | B1-1 |" for n in names[1:])
        plant("bridge coverage", readme,
              lambda p: p.write_bytes(
                  b"# Agent Skill Bridge\n\n## Claude-only skills\n\n| Skill | Claude source | Source | Added at |\n"
                  b"| --- | --- | --- | --- |\n" + rows.encode("utf-8") + b"\n"),
              f"bridge coverage: .claude/skills/{names[0]} has neither")
        plant("bridge coverage, frozen row", readme,
              lambda p: p.write_bytes(
                  b"# Agent Skill Bridge\n\n## Codex-enabled skills\n\n| Skill | Claude source | Codex | Status |\n"
                  b"| --- | --- | --- | --- |\n"
                  + f"| `{names[0]}` | `../.claude/skills/{names[0]}` | `../.codex/skills/{names[0]}` | frozen |\n".encode()
                  + b"\n## Claude-only skills\n\n| Skill | Claude source | Source | Added at |\n| --- | --- | --- | --- |\n"
                  + rows.encode("utf-8") + b"\n"),
              "a README covering every folder", silent=True)

        plant("multi-root skip", copy / suite / ".git", lambda p: p.unlink(), suite, absent=True)

        # A CRLF<->LF flip of a mirrored file is not drift.
        target = skills / "run-batch" / "SKILL.md"
        original = target.read_bytes()
        target.write_bytes(_flip_line_endings(original))
        flipped = check_all(copy, with_codex_compare)
        if set(flipped.diagnostics) != base_set:
            failures.append("LF normalization: a CRLF<->LF flip was reported as drift")
        else:
            detected.append("LF normalization: a CRLF<->LF flip of run-batch/SKILL.md is not drift")
        target.write_bytes(original)

    for line in detected:
        print(f"{VERDICT} self-test: ok: {line}")
    for line in failures:
        print(f"{VERDICT} self-test: FAILED: {line}")
    if failures:
        print(f"{VERDICT} self-test: fail — {len(failures)} of {len(failures) + len(detected)} plants")
        return 1
    print(
        f"{VERDICT} self-test: pass — {len(detected)} plants proven (suite {suite});"
        " restored copy equals the baseline"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="plant one drift per check in a temporary copy, then check the real tree",
    )
    parser.add_argument(
        "--with-codex-compare",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="compare the superproject's .claude with .codex (off since the freeze; on again at an unfreeze)",
    )
    parser.add_argument(
        "--print-freeze-table",
        metavar="REPO=COMMIT",
        help="print the freeze pins of one repository ('.' or a suite folder) from git show COMMIT:<path>",
    )
    arguments = parser.parse_args()
    root = repository_root()
    if arguments.print_freeze_table:
        key, _, commit = arguments.print_freeze_table.partition("=")
        if not commit:
            print(f"{VERDICT}: error — --print-freeze-table takes REPO=COMMIT")
            return 2
        try:
            print(freeze_table(root, key, commit))
        except (subprocess.CalledProcessError, ValueError) as error:
            print(f"{VERDICT}: error — could not read the freeze commit: {error}")
            return 2
        return 0
    if not (root / ".claude" / "skills").is_dir():
        print(f"{VERDICT}: error — could not run: no .claude/skills under {root}")
        return 2
    try:
        if arguments.self_test:
            self_code = run_self_test(root, arguments.with_codex_compare)
            real_code = _print_report(check_all(root, arguments.with_codex_compare), arguments.with_codex_compare)
            return max(self_code, real_code)
        return _print_report(check_all(root, arguments.with_codex_compare), arguments.with_codex_compare)
    except FileNotFoundError as error:
        print(f"{VERDICT}: error — could not run: {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
