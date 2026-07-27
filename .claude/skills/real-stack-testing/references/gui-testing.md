# GUI and browser real-stack tests

Use the repository's mandated browser stack and existing shared harness. Do not
introduce a second browser path.

- Boot the real application entrypoint on an ephemeral port.
- Use real routes and a temporary real store; do not call client handlers
  directly or drive state through fixture-only flags.
- Register shared failure hooks for uncaught page errors, error-level console
  messages, unexpected 4xx/5xx responses, and server-side exceptions.
- Assert the expected request was sent and the resulting persisted state, not
  only selectors or screenshots.
- Synchronize on observable state or events. Fixed timeout sleeps are defects.
- Capture screenshots, DOM, console, network, and server logs on failure, but
  prove behavior with executable assertions.
- When browser availability is required evidence, use the repository's strict
  option so an unavailable browser fails rather than skips.
