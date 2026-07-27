## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## Testing

- **Never fake the layer under test.** Tests substitute only *process
  boundaries* — subprocesses, third-party HTTP, the clock, randomness. The
  composition root, domain services, persistence, and routes/rendering always
  run for real. A fixture class that re-implements logic living in `src/` is a
  defect, not a fixture: it makes the suite green while the product is broken.
- Any test spanning more than one module (integration, e2e, browser,
  acceptance, batch-row validation) must follow the `real-stack-testing` skill.
- After implementation, invoke `validate-real-stack` with the exact named
  validation. Its Sonnet/Terra worker runs in isolated context and returns
  compact evidence; the parent implementation agent owns fixes and completion.
- UI tests fail on uncaught console exceptions, unasserted 4xx/5xx, and
  server-side exceptions — not only on missing selectors.
