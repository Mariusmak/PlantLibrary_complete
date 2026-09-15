"""Census of every PlantLibrary batch package through Conductor's real parser.

Run with the interpreter of a Conductor instance (its venv has the ``conductor``
package installed) or with the dev repo's venv; ``CONDUCTOR_SRC`` may point at
a ``src`` folder as a fallback.
"""

from __future__ import annotations

import collections
import glob
import os
import sys

_FALLBACK_SRC = os.environ.get("CONDUCTOR_SRC", r"C:\Programs\AI_Orchestrator_2\src")
try:
    from conductor.batch_package import parse_package
except ImportError:
    sys.path.insert(0, _FALLBACK_SRC)
    from conductor.batch_package import parse_package

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PATTERNS = (
    r"PlantLibrary_*\implementation\*",
    r"PlantLibrary_Workspace\strategy\*",
    r"PlantLibrary_Workspace\system_description\*",
)
KINDS = (
    "no 15-column",
    "declares missing primary row",
    "outside the first sentence",
    "missing required file",
    "has no goal",
    "no context anchor",
    "does not match checklist",
    "invalid status",
    "cells, expected",
    "duplicate",
    "unsafe output path",
)


def main() -> int:
    folders = sorted(
        path
        for pattern in PATTERNS
        for path in glob.glob(os.path.join(ROOT, pattern))
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, "TASK_CHECKLIST.md"))
    )
    worst = 0
    for folder in folders:
        short = os.path.relpath(folder, ROOT)
        result = parse_package(folder)
        if isinstance(result, list):
            kinds: collections.Counter[str] = collections.Counter()
            for error in result:
                kinds[next((k for k in KINDS if k in error.message), error.message[:60])] += 1
            worst = max(worst, len(result))
            print(f"{short}: {len(result)} errors -> {dict(kinds)}")
            details = [
                e.message
                for e in result
                if not any(k in e.message for k in ("no 15-column", "declares missing"))
            ]
            for message in details[:8]:
                print(f"    {message[:160]}")
            if len(details) > 8:
                print(f"    … {len(details) - 8} more")
        else:
            classes = ", ".join(f"{b.key}={b.classification}" for b in result.batches)
            print(f"{short}: OK {len(result.batches)} batches {len(result.rows)} rows :: {classes}")
    return 1 if worst else 0


if __name__ == "__main__":
    raise SystemExit(main())
