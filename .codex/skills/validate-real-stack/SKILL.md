---
name: validate-real-stack
description: Run one already-defined real-stack validation through the cheaper project validation agent after implementation. Use only when the exact command, acceptance criteria, touched paths, and output artifact are known.
---

# Validate Real Stack

Delegate this workflow to the project agent named `real_stack_validator` in a
fresh, minimal-context subagent. If already executing as that agent, continue
directly. Wait for its result before the parent closes the task.

Pass only:

- task or row ID
- exact validation command
- acceptance criteria
- touched paths
- full-output artifact path inside the workspace

Resolve `scripts/run_validation.ps1` relative to this skill directory and run
it with `powershell.exe -NoProfile -ExecutionPolicy Bypass -File`. Pass the
exact command and artifact path. The script writes full output to the artifact
and prints compact JSON containing the exit code, duration, path, and at most
20 tail lines.

Return:

- command and exit code
- pass/fail for each acceptance criterion
- artifact paths
- no more than 20 relevant output lines
- suspected cause when failed

Do not edit source, tests, checklist state, batch metadata, or evidence prose.
The parent implementation agent owns all fixes and completion decisions. If the
named validation agent is unavailable, tell the parent to run the same workflow
inline and record the fallback.
