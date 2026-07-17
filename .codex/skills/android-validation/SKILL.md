---
name: android-validation
description: Repeatable validation harness for the PlantLibrary Android app on this machine's emulator. Brings up a headless AVD, applies the adb reverse rules, builds/installs/launches the debug APK, drives the app state-aware through adb + uiautomator (never assuming focus or that a tap landed), captures screenshot/UI-dump/logcat evidence in the house evidence-pack format, and tears down by exact serial. Use for "start the Android emulator", "install the app on the emulator", "run the Android walkthrough for AN-V1-ACC-01", "is the emulator healthy", or any row whose skill column says android-validation:<command>.
user-invocable: true
argument-hint: "[up|install|status|capture|walkthrough|down] [row-id|label]"
---

Evidence-driven device validation: a step passes only with captured proof
(screenshot, UI dump, logcat line, API response) — never because the build
succeeded or an adb command exited 0. This skill owns the **device
procedure, environment recipe, and evidence format** for
`PlantLibrary_AndroidApp`; the **scenario list** for a walkthrough always
comes from the invoking row's `TASK_CONTEXT.md` anchor or named runbook —
never duplicated here. The server stack belongs to verify-stack: this skill
never brings up, seeds, or tears down the Docker stack itself — server-backed
flows call `verify-stack up/seed/status/snapshot` for that.

## Operating rules

- Never edit product code during a validation run. Failures become gap/row
  proposals routed to the owning suite (run-batch §5 route-don't-duplicate).
- gui-validation's protocol governs all app driving; the Interaction
  protocol below maps it to adb. Its non-negotiables (one action one
  verification, no stale coordinates, no proxy signals, classify before
  retry) apply verbatim.
- Emulator only by default. A physical device only on explicit user request,
  and never force-stop, clear data, or wipe a device holding real personal
  data — clients under test use disposable validation identities
  (`testgrower`) and a disposable validation database, never a real one.
- The headless AVD is the default; the visible GUI emulator runs only on
  explicit user request.
- Never paste secrets, tokens, or real personal data into evidence files;
  redact and note the redaction. The disposable local credential source is
  `PlantLibrary_Server/docs/local_android_test_environment.md`.
- Kill the emulator only by its exact serial (`adb -s <serial> emu kill`) —
  never by image name; emulator/qemu processes on this machine may belong to
  other work.
- Step statuses: `pass | fail | blocked | gated | skipped | pass-with-gap |
  pending`. Record honestly; a partial run is a partial run.
- A successful Gradle build is necessary but never sufficient — no row or
  scenario is marked from `gradlew` output alone (this suite's founding
  rule, `STATE.md` `AN-B07`).

## Canonical environment

Authority for connection values, seeding, and quirks:
`PlantLibrary_Server/docs/local_android_test_environment.md` — if anything
here has drifted, fix it there and here together.

| Item | Value |
|---|---|
| SDK root | `$env:ANDROID_SDK_ROOT`, else `$env:ANDROID_HOME`, else `$env:LOCALAPPDATA\Android\Sdk` |
| adb | `<SDK>\platform-tools\adb.exe` — not on PATH; always use the full path |
| emulator | `<SDK>\emulator\emulator.exe`; set `$env:ANDROID_AVD_HOME = "$env:USERPROFILE\.android\avd"` |
| JDK for Gradle | `$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio\jbr'` (JBR 21 — the only JDK proven against this build) |
| Build | `.\gradlew.bat` from `PlantLibrary_AndroidApp\`; debug APK at `app\build\outputs\apk\debug\app-debug.apk` |
| AVDs | `plantlibrary_test_noGUI` (headless default) · `plantlibrary_test_GUI` (visible, explicit request only, via `scripts/start_gui_emulator.ps1`) · `plantlibrary_test` (legacy; produced the MVP evidence) |
| App | `com.plantlibrary.android` / `.MainActivity` |
| Server (through adb reverse) | issuer `http://localhost:8080/realms/plantlibrary` · client `plantlibrary-android` · API `http://localhost:8000` · test identity `testgrower`, garden `Test Backyard Garden` |

Reverse rules — required after **every** emulator boot (they do not survive
restarts), per `VGAP-033`/`AN-V1-LOCAL-OIDC-01` (all clients use
`localhost`; never switch Keycloak hostnames between clients):

```powershell
& $ADB reverse tcp:8000 tcp:8000   # API
& $ADB reverse tcp:8080 tcp:8080   # Keycloak
& $ADB reverse tcp:9000 tcp:9000   # MinIO presigned uploads
```

Known quirks (reference, don't re-diagnose): cold boot under this machine's
nested virtualization can take tens of minutes (~90 min observed 2026-07-13
— CPU-bound ART verification, not a hang); the MinIO presigned-URL host gap
is recorded in the environment doc; instrumented-test runs go through
`scripts/run_headless_tests.ps1` once `AN-V1-TEST-02` creates it.

## Commands

### `up [avd]`

1. If the target AVD is already running (`adb devices` + `adb -s <serial>
   emu avd name`), reuse it — record its serial, never start a second copy.
2. Start headless: `emulator.exe -avd plantlibrary_test_noGUI -no-window
   -no-audio -no-boot-anim -no-snapshot -gpu swiftshader_indirect`,
   detached. The GUI AVD only on explicit request via
   `scripts/start_gui_emulator.ps1`.
3. Wait: `adb wait-for-device`, then poll `adb shell getprop
   sys.boot_completed` until `1`. Patient bounded wait — report progress
   every few minutes and consult the cold-boot quirk above before declaring
   a hang.
4. Apply the three reverse rules; verify with `adb reverse --list`.
5. Print serial, AVD name, boot duration, reverse rules — and, if the run
   is server-backed, the `verify-stack status` result.

### `install`

1. From `PlantLibrary_AndroidApp\` with `JAVA_HOME` set to the JBR:
   `.\gradlew.bat :app:assembleDebug :app:lintDebug` — both must pass; lint
   findings are not warnings to skip.
2. `adb -s <serial> install -r app\build\outputs\apk\debug\app-debug.apk`.
3. Launch: `adb shell am start -n com.plantlibrary.android/.MainActivity`.
4. Verify launched, not merely started: poll the foreground activity
   (`dumpsys activity activities` → `topResumedActivity` is
   `MainActivity`), check logcat since launch for `FATAL EXCEPTION`/ANR for
   the package, and capture a baseline screenshot. The install exit code
   alone proves nothing.

### `status`

One compact table: serial + AVD, boot state, reverse rules
(`adb reverse --list`), installed `versionName` (`dumpsys package
com.plantlibrary.android`), app process running, foreground activity,
crash-buffer check (`adb logcat -d -b crash`). No log dumps unless
something is wrong.

### `capture <label>`

The evidence primitive; every walkthrough step uses it.

- Screenshot: `adb shell screencap -p /sdcard/cap.png` + `adb pull` →
  `<run>/NN_<label>.png` (NN = next sequence number; shell-then-pull avoids
  Windows pipe corruption of `exec-out` binary output).
- UI dump: `adb shell uiautomator dump /sdcard/window_dump.xml` + pull →
  `<run>/window_<label>.xml`.
- Logcat slice: `adb logcat -d` filtered to the app package + crash buffer
  → `<run>/<label>_logcat.txt`.

Before filing, confirm the screenshot actually shows the intended screen
and state (gui-validation §11) — a capture that doesn't show the claimed
result is not evidence.

### `walkthrough <row-id>`

1. **Resolve the scenario source**: the row's checklist line +
   `TASK_CONTEXT.md` anchor in the invoking package define the scenario
   list, required clients, and the evidence-pack path (the row's `file(s)`
   column). Requirements unmet → report and stop (do not bring up half a
   run).
2. **Prepare**: `up` + `install` (fresh build unless the row says
   otherwise). Server-backed rows additionally require `verify-stack up`
   (+ `seed` if the run needs a fresh dataset) and a `verify-stack
   snapshot` `before`. Create `validation/evidence/<RUN-ID>/` in the
   invoking package, `RUN-ID = <ROW-ID>-<yyyymmdd>-NN`; capture a baseline.
3. **Execute scenarios in order** using the Interaction protocol — every
   step is observe → act → verify with a `capture` at each decision point.
   OIDC login runs through a Chrome Custom Tab (a different foreground
   package); that is an expected state, driven under the same rules.
4. **On failure**: classify first (gui-validation §12 — app defect vs
   automation targeting / synchronization / invalid precondition /
   environment error), record the exact step + evidence, log a gap to the
   invoking package's register (next `VGAP-NNN` or the V1 register's
   scheme), mark the scenario `fail` or `pass-with-gap`, and continue with
   the remaining scenarios where independent — never inline-fix.
5. Force-stop/restart-recovery scenarios use
   `adb shell am force-stop com.plantlibrary.android` (package-scoped) —
   never process kills by name.
6. **Write the evidence pack** (path from the row) and run the
   completeness check. Take the `verify-stack snapshot` `after` following
   each mutating server-backed scenario. Update the package's evidence
   index if it has one.

### `down`

If this run started the emulator: final `capture` if a walkthrough is
open, then `adb -s <serial> emu kill`. If the emulator was already running
before `up`, leave it running and say so. Reverse rules die with the
emulator. Stack teardown is `verify-stack down`, not this skill's.

## Interaction protocol

gui-validation governs; this section maps its loop to adb driving, where
the same trap class exists — a tap is delivered to whatever is on screen
*now*, not what the last screenshot showed.

1. **Observe fresh.** Before every tap or keypress, take a new
   `uiautomator dump`; locate the target by text/resource-id/content-desc
   in *that* dump; compute the tap point from its bounds. Coordinates are
   single-use — never carried across steps, scrolls, or recompositions.
2. **Confirm the foreground package/activity before input**
   (`dumpsys activity activities`). Permission prompts, system dialogs,
   the IME, and Custom Tabs are other packages — interact with them
   knowingly or dismiss them deliberately, never accidentally.
3. **One action, one verification.** After each input, verify the specific
   expected change (expected node present/changed in a fresh dump, expected
   screen in a fresh screenshot, expected logcat line) — never a proxy (a
   toast, an API `200`) standing in for the actual expected behavior.
4. **Wait on state, not time.** Poll dump/logcat for the expected condition
   with a bound; never re-tap while waiting (double-submission risk); a
   fixed sleep is never the only completion signal for a consequential
   step.
5. **Text entry**: confirm the field is focused in the dump
   (`focused="true"`) before `adb shell input text` (escape spaces as
   `%s`); read the rendered value back from the next dump — don't assume
   the string landed.
6. **Keyboard**: check `dumpsys input_method` before using Back to dismiss
   it — if the keyboard isn't actually shown, Back navigates instead.
7. **A negative lookup is not absence.** `uiautomator dump` can fail or
   serve a stale tree; re-dump and cross-check with a screenshot before
   concluding a control is missing or an action failed.
8. **Classify before any retry** (gui-validation §12): rule out targeting,
   synchronization, precondition, and environment errors before reporting
   an app defect; blind re-taps are prohibited.

## Evidence conventions

- Run folder in the invoking package: `validation/evidence/<RUN-ID>/`,
  `RUN-ID = <ROW-ID>-<yyyymmdd>-NN` (the folder name carries row + date
  identity, so files inside don't repeat it).
- Screenshots: `NN_<snake_case_description>.png`, numbered in action order
  (`01_...`, `02_...`); a retaken/superseded shot keeps its number with a
  letter suffix (`02b_...`).
- UI dumps: `window_<description>.xml`.
- Logcat: `<flow>_logcat.txt`, filtered to the app package + crash buffer;
  save a full log only when diagnosing.
- Server-side proof (SQL/API responses) follows verify-stack's snapshot
  format and lives in the same run folder.

## Evidence pack format

```markdown
# <ROW-ID> — <title>
Run: <RUN-ID> · Date · AVD + serial · APK: <git rev + build command> · Stack: <verify-stack state or "not required">

## Environment
<emulator, reverse rules, seed state if server-backed, login identity>
## Scenario results
| # | Scenario | Steps ref | Status | Evidence |
## Convergence (server-backed runs)
| Entity | id | server_version before | after | Verdict |
## Gaps raised
| Gap ID | Scenario | One-line description | Routed to |
## Artifact manifest
<one line per evidence file: name — what it shows>
## Verdict
<overall + what remains pending, honestly>
```

Completeness check before closing: every scenario has a status and at
least one evidence file; every mutating server-backed scenario has
before/after `server_version`s (via verify-stack snapshots); every
`fail`/`pass-with-gap` has a gap row with an owner; the artifact manifest
lists every file in the run folder; no unexplained crash lines in any
saved logcat; secrets redacted.

## Integration with batch rows

Rows opt in via their `skill` column (`android-validation:walkthrough`,
`android-validation:install`, ...); run-batch loads this skill only for
such rows, after selection and requirements pass. Division of labor with
verify-stack: cross-platform rows keep `verify-stack:walkthrough`
(verify-stack orchestrates the run and owns the stack; its Android client
steps execute through this skill), while Android-only device rows name
`android-validation:walkthrough` directly. A walkthrough row is `done`
only when its evidence pack passes the completeness check — matching
run-batch's rule that unexecuted validation means not done.
