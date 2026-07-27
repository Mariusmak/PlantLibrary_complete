---
name: validate-real-stack
description: Run one already-defined real-stack validation through the cheaper project validation agent after implementation. Use only when the exact command, acceptance criteria, touched paths, and output artifact are known.
argument-hint: "<task-id> | <exact-command> | <criteria> | <touched-paths> | <artifact-path>"
context: fork
agent: real-stack-validator
background: false
---

# Validate Real Stack

Validate `$ARGUMENTS` and wait for completion.

The input must supply:

- task or row ID
- exact validation command
- acceptance criteria
- touched paths
- full-output artifact path inside the workspace

Run `${CLAUDE_SKILL_DIR}\scripts\run_validation.ps1` with
`powershell.exe -NoProfile -ExecutionPolicy Bypass -File`, passing the exact
command and artifact path. The script writes full output to the artifact and
prints compact JSON containing the exit code, duration, path, and at most 20
tail lines.

Return:

- command and exit code
- pass/fail for each acceptance criterion
- artifact paths
- no more than 20 relevant output lines
- suspected cause when failed

Do not edit source, tests, checklist state, batch metadata, or evidence prose.
The parent implementation agent owns all fixes and completion decisions.
