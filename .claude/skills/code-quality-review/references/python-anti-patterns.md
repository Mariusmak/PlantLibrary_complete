<!-- Adapted from wshobson/agents @ 156b7a5, plugins/python-development/skills/python-anti-patterns/SKILL.md (MIT; see LICENSE). Modified 2026-10-04 by the Conductor (Orchestrator_System, OP-SK-A, D-2026-10-04-11) and 2026-10-13 for PlantLibrary (master rework B1-3, Q-A1-02 (a)). -->

# Python Anti-Patterns Checklist

A reference checklist of common mistakes and anti-patterns in Python code. Review this before finalizing implementations to catch issues early.

## When to Use This Skill

- Reviewing code before merge
- Debugging mysterious issues
- Teaching or learning Python best practices
- Establishing team coding standards
- Refactoring legacy code

**Note:** This reference focuses on what to avoid.

## Infrastructure Anti-Patterns

### Scattered Timeout/Retry Logic

```python
# BAD: Timeout logic duplicated everywhere
def fetch_user(user_id):
    try:
        return httpx.get(url, timeout=30)
    except httpx.TimeoutException:
        logger.warning("Timeout fetching user")
        return None

def fetch_orders(user_id):
    try:
        return httpx.get(url, timeout=30)
    except httpx.TimeoutException:
        logger.warning("Timeout fetching orders")
        return None
```

**Fix:** Centralize in one client wrapper.

```python
# GOOD: one client owns timeout and retry
_client = httpx.Client(timeout=30.0, transport=httpx.HTTPTransport(retries=3))

def http_get(url: str) -> httpx.Response:
    return _client.get(url)
```

### Double Retry

```python
# BAD: Retrying at multiple layers
@retry(max_attempts=3)  # Application retry
def call_service():
    return client.request()  # Client also has retry configured!
```

**Fix:** Retry at one layer only. Know your infrastructure's retry behavior.

### Hard-Coded Configuration

```python
# BAD: Secrets and config in code
DATA_DIR = r"C:\Users\me\AppData\Local\PlantLibrary"
API_KEY = "sk-12345"
```

**Fix:** Settings come from the suite's validated settings model (PlantLibrary_Server:
`app/core/config.py`, pydantic-settings read from the environment); on the desktop client
a secret lives only in the OS credential store, reached through `keyring`
(PlantLibrary_PyApp: `app/services/auth_service.py`). No secret in code, config examples,
fixtures or logs.

```python
# GOOD
settings = Settings()      # pydantic-settings: read from the environment, validated
token = keyring.get_password(SERVICE_NAME, username)  # desktop client: OS credential store
```

## Error Handling Anti-Patterns

### Bare Exception Handling

```python
# BAD: Swallowing all exceptions
try:
    process()
except Exception:
    pass  # Silent failure - bugs hidden forever
```

**Fix:** Catch specific exceptions. Log or handle appropriately.

```python
# GOOD
try:
    process()
except ConnectionError as e:
    logger.warning("Connection failed, will retry: %s", e)
    raise
except ValueError as e:
    logger.error("Invalid input: %s", e)
    raise BadRequestError(str(e))
```

### Ignored Partial Failures

```python
# BAD: Stops on first error
def process_batch(items):
    results = []
    for item in items:
        result = process(item)  # Raises on error - batch aborted
        results.append(result)
    return results
```

**Fix:** Capture both successes and failures.

```python
# GOOD
def process_batch(items) -> BatchResult:
    succeeded = {}
    failed = {}
    for idx, item in enumerate(items):
        try:
            succeeded[idx] = process(item)
        except Exception as e:
            failed[idx] = e
    return BatchResult(succeeded, failed)
```

### Missing Input Validation

```python
# BAD: No validation
def create_user(data: dict):
    return User(**data)  # Crashes deep in code on bad input
```

**Fix:** Validate early at API boundaries.

```python
# GOOD
def create_user(data: dict) -> User:
    validated = CreateUserInput.model_validate(data)
    return User.from_input(validated)
```

## Resource Anti-Patterns

### Unclosed Resources

```python
# BAD: File never closed
def read_file(path):
    f = open(path)
    return f.read()  # What if this raises?
```

**Fix:** Use context managers.

```python
# GOOD
def read_file(path):
    with open(path) as f:
        return f.read()
```

### Blocking in Async

```python
# BAD: Blocks the entire event loop
async def fetch_data():
    time.sleep(1)  # Blocks everything!
    response = httpx.get(url)  # Also blocks!
```

**Fix:** Use async-native libraries.

```python
# GOOD
async def fetch_data():
    await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
```

## Type Safety Anti-Patterns

### Missing Type Hints

```python
# BAD: No types
def process(data):
    return data["value"] * 2
```

**Fix:** Annotate all public functions.

```python
# GOOD
def process(data: dict[str, int]) -> int:
    return data["value"] * 2
```

### Untyped Collections

```python
# BAD: Generic list without type parameter
def get_users() -> list:
    ...
```

**Fix:** Use type parameters.

```python
# GOOD
def get_users() -> list[User]:
    ...
```

## Testing Anti-Patterns

### Only Testing Happy Paths

```python
# BAD: Only tests success case
def test_create_user():
    user = service.create_user(valid_data)
    assert user.id is not None
```

**Fix:** Test error conditions and edge cases.

```python
# GOOD
def test_create_user_success():
    user = service.create_user(valid_data)
    assert user.id is not None

def test_create_user_invalid_email():
    with pytest.raises(ValueError, match="Invalid email"):
        service.create_user(invalid_email_data)

def test_create_user_duplicate_email():
    service.create_user(valid_data)
    with pytest.raises(ConflictError):
        service.create_user(valid_data)
```

### Over-Mocking

```python
# BAD: Mocking everything
def test_user_service():
    mock_repo = Mock()
    mock_cache = Mock()
    mock_logger = Mock()
    mock_metrics = Mock()
    # Test doesn't verify real behavior
```

**Fix:** Substitute only at a process boundary (`real-stack-testing`).

## Quick Review Checklist

Before finalizing code, verify:

- [ ] No scattered timeout/retry logic (centralized)
- [ ] No double retry (app + infrastructure)
- [ ] No hard-coded configuration or secrets
- [ ] No bare `except Exception: pass`
- [ ] No ignored partial failures in batches
- [ ] No missing input validation
- [ ] No unclosed resources (using context managers)
- [ ] No blocking calls in async code
- [ ] All public functions have type hints
- [ ] Collections have type parameters
- [ ] Error paths are tested
- [ ] Edge cases are covered

## Common Fixes Summary

| Anti-Pattern | Fix |
|-------------|-----|
| Scattered retry logic | One client wrapper |
| Hard-coded config | A validated settings model; the environment or `keyring` for secrets |
| Bare except | Catch specific exceptions |
| Batch stops on error | Return BatchResult with successes/failures |
| No validation | Validate at boundaries with Pydantic |
| Unclosed resources | Context managers |
| Blocking in async | Async-native libraries |
| Missing types | Type annotations on all public APIs |
| Only happy path tests | Test errors and edge cases |
