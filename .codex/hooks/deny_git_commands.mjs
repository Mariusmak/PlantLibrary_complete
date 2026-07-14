#!/usr/bin/env node
// PreToolUse hook: deny risky/destructive git commands before they run.
// Mirrors the deny rules in .claude/settings.local.json's permissions.deny.
// Reads the hook-input JSON on stdin; if tool_input.command matches a
// denied pattern, emits a "deny" permission decision instead of running it.

const DENY_RULES = [
  { name: "git stash", test: (c) => /\bgit\s+stash\b/.test(c) },
  { name: "git reset --hard", test: (c) => /\bgit\s+reset\s+--hard\b/.test(c) },
  { name: "git clean -f", test: (c) => /\bgit\s+clean\s+-f/.test(c) },
  { name: "git checkout -- (discard)", test: (c) => /\bgit\s+checkout\s+--\s/.test(c) },
  { name: "git restore", test: (c) => /\bgit\s+restore\b/.test(c) },
  { name: "git branch -D/--delete", test: (c) => /\bgit\s+branch\s+(-D\b|--delete\b)/.test(c) },
  {
    name: "git push --force/-f/--force-with-lease/--delete",
    test: (c) =>
      /\bgit\s+push\b/.test(c) &&
      /(--force(-with-lease)?\b|(^|\s)-f\b|--delete\b)/.test(c),
  },
  { name: "git rebase", test: (c) => /\bgit\s+rebase\b/.test(c) },
  { name: "git filter-branch", test: (c) => /\bgit\s+filter-branch\b/.test(c) },
  {
    name: "git gc --prune",
    test: (c) => /\bgit\s+gc\b/.test(c) && /--prune/.test(c),
  },
];

let raw = "";
process.stdin.on("data", (chunk) => {
  raw += chunk;
});
process.stdin.on("end", () => {
  let input;
  try {
    input = JSON.parse(raw || "{}");
  } catch {
    process.exit(0); // fail open on unparseable input
  }

  const command = input?.tool_input?.command;
  if (typeof command !== "string" || command.length === 0) {
    process.exit(0);
  }

  const hit = DENY_RULES.find((rule) => rule.test(command));
  if (!hit) {
    process.exit(0);
  }

  process.stdout.write(
    JSON.stringify({
      hookSpecificOutput: {
        hookEventName: "PreToolUse",
        permissionDecision: "deny",
        permissionDecisionReason:
          `Blocked by project policy: "${hit.name}" is a destructive/history-` +
          `rewriting git command. This class of command is denied outright ` +
          `(see .claude/settings.local.json's permissions.deny for the ` +
          `equivalent Claude Code rule) rather than left to per-call judgment.`,
      },
    })
  );
  process.exit(0);
});
