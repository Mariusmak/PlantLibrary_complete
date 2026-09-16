# Consumed hygiene — SW_Development

The pin (`KIT_SPEC.md` §7.2): which kit this repository is anchored to and what it declares. Written by
the kit's installer, last, and re-written only by `--force` — a re-pin is its own task and a decision
entry in `HYGIENE_DECISIONS.md`. A root, module, wrapper, launcher or floor change is a decision entry
with the table below edited in the same commit; the checker reads roots from this table only.

| Field | Value |
|---|---|
| Kit version | `0.1.0` |
| Kit path | `C:/Programmierung/Repo_Hygiene_Template_Kit` |
| SOURCE harness | `fc5a14c` |
| Pinned on | 2026-09-16 |
| Modules | root-allowlist |
| Pytest wrapper | no |
| Rule block | on |
| Sanctioned launcher |  |
| Prompt file floor | 1 |

## Deliverable roots

| Root | Kind | Pattern |
|---|---|---|
| `repo-hygiene` | general | standard |
| `onboarding` | general | standard |
| `handovers` | handovers | date-anywhere |
