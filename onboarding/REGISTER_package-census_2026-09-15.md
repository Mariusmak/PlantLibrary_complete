# onboarding/ — package census register

Running record of `scripts\harness\check_batch_packages.py` output, one section per capture.
Interpreter used is named at each heading.

## Census at step 0

Run with `C:\Programs\AI_Orchestrator_2\.venv\Scripts\python.exe scripts\harness\check_batch_packages.py`
from `C:\Programmierung\SW_Development`, 2026-09-15. Exit code `1` (errors present, expected pre-migration).

Seven live packages match runbook §1b exactly: PyApp 24, Server 35, AndroidApp 44, Dashboard 26,
SharedContracts 11, Workspace V1 18, SDA 8.

```text
PlantLibrary_AndroidApp\implementation\System_V1_Implementation: 44 errors -> {'no 15-column': 1, 'declares missing primary row': 40, 'outside the first sentence': 3}
    batch AN1-B08 has requires token AN1-B09 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
    batch AN1-B08 has requires token AN1-B10 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
    batch AN1-B11 has requires token AN1-B09 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
PlantLibrary_Dashboard\implementation\System_V1_Implementation: 26 errors -> {'no 15-column': 1, 'declares missing primary row': 22, 'has no goal': 1, 'outside the first sentence': 2}
    batch WD1-B03 has no goal
    batch WD1-B04 has requires token WD1-B05 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
    batch WD1-B06 has requires token WD1-B05 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
PlantLibrary_PyApp\implementation\System_V1_Implementation: 24 errors -> {'no 15-column': 1, 'declares missing primary row': 22, 'outside the first sentence': 1}
    batch PY1-B04 has requires token PY1-B05 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
PlantLibrary_Server\implementation\System_V1_Implementation: 35 errors -> {'no 15-column': 1, 'declares missing primary row': 33, 'has no goal': 1}
    batch SV1-B05 has no goal
PlantLibrary_SharedContracts\implementation\System_V1_Implementation: 11 errors -> {'no 15-column': 1, 'declares missing primary row': 10}
PlantLibrary_Workspace\implementation\System_Design_Architecture: 8 errors -> {'no 15-column': 1, 'declares missing primary row': 7}
PlantLibrary_Workspace\implementation\System_Integration_MVP: 25 errors -> {'no 15-column': 1, 'declares missing primary row': 24}
PlantLibrary_Workspace\implementation\System_Tooling: 6 errors -> {'no 15-column': 1, 'declares missing primary row': 5}
PlantLibrary_Workspace\implementation\System_V1_Implementation: 18 errors -> {'no 15-column': 1, 'declares missing primary row': 16, 'outside the first sentence': 1}
    batch SY1-B05 has requires token SY1-B07 outside the first sentence; fold the prerequisite into the first sentence or move the commentary to **Notes:**
PlantLibrary_Workspace\strategy\Cross_Platform_Strategy: 30 errors -> {'no 15-column': 1, 'declares missing primary row': 29}
PlantLibrary_Workspace\system_description\PlantLibrary_System_Description: 62 errors -> {'no 15-column': 1, 'duplicate': 46, 'declares missing primary row': 15}
    duplicate context anchor Intent
    duplicate context anchor Output
    duplicate context anchor Validation
    duplicate context anchor Intent
    duplicate context anchor Output
    duplicate context anchor Validation
    duplicate context anchor Intent
    duplicate context anchor Output
    … 38 more
```
