---
name: gui-validation
description: Operational protocol for validating a real GUI application (desktop or browser) by direct mouse/keyboard control. Makes every action state-aware, evidence-based, and recoverable — never assumes the target window has focus, is in the foreground, is at a remembered position, or that a click/keypress landed where intended. Use before and during any session that drives a real application UI (PySide6/Qt desktop apps, Electron, browser-based flows opened from a desktop app, etc.) via simulated mouse/keyboard rather than in-process test APIs. Derived from a real PlantLibrary_PyApp validation session that lost clicks to an unfocused window, including one click that landed on an unrelated browser tab.
user-invocable: true
argument-hint: "[application/window-title]"
---

# GUI Validation Protocol

## 1. Purpose

This skill governs validation of a real running application through **direct
mouse and keyboard control** — not an in-process test harness, not a browser
automation framework with built-in auto-waiting, but raw OS-level input
(`SetCursorPos`/`mouse_event`, `SendKeys`, UI Automation `Invoke`/`SetValue`,
or equivalent). At this level, nothing is guaranteed: the operating system
delivers your click to whatever window is actually in focus, not whatever
window your last screenshot showed. This skill exists to make every action
**state-aware** (based on what is true right now, not what was true when you
last looked), **evidence-based** (verified by a specific observable signal,
not inferred), and **recoverable** (a wrong assumption is caught in one step,
not compounded across ten).

You must never assume: the application is in the foreground; the intended
window has focus; a window is still at its previous position; screen
coordinates remain valid; a click was accepted; a keypress went to the
intended control; the GUI finished updating; a dialog did not appear; a
window was not minimized, covered, moved, resized, or closed; the
application state matches your memory of it; or that a screenshot taken
earlier still represents the current screen. Every one of these was
violated at least once in the session this skill is built from (§16).

## 2. Non-negotiable rules

1. **Verify the target window is actually foreground before every click or keypress.** A successful screenshot of a window proves nothing about whether it currently has OS focus — some screenshot methods render window content regardless of focus or occlusion.
2. **One action, one verification.** Never chain a second click, keypress, or navigation step before confirming the visible/logged effect of the first.
3. **Never reuse coordinates or element references from an earlier observation.** Re-locate the target from the current screen state immediately before acting on it.
4. **Treat every click and keypress as unconfirmed until its specific expected effect is verified** — not a related-but-weaker signal (a status banner, a toast, an API call returning success) standing in for the actual expected behavior.
5. **Never retry a click or shortcut just because nothing visibly happened.** Diagnose first — the first attempt may already have landed on the wrong window.
6. **A negative/"not found" result from a lookup API is not proof the target doesn't exist.** Cross-check with an independent signal before concluding an action failed.
7. **Reacquire full state after any window move, resize, dialog, external tool call, or unexpected result** — assume nothing about focus or layout survives a context switch.
8. **Never target a shared resource (process, window) by a non-unique identifier.** Kill/close by exact PID or window handle, never by image name or title substring on a machine other automation or a human might also be using.
9. **Stop and classify before continuing when observed state differs from expected state.** Do not proceed on the assumption that it will "probably resolve itself."
10. **Capture evidence for passes and failures alike**, and explicitly separate "the application did something wrong" from "my input went to the wrong place."

## 3. Core operating principles

- **Observe before every meaningful action.** Inspect the current screen or accessibility tree immediately before acting — not the screen from your last screenshot.
- **Never rely on coordinates remembered from an earlier screenshot.** Screens move, windows resize, DPI changes; a coordinate is valid for one action only.
- **Bring the target window to the foreground and verify it before interacting.** Don't assume `SetForegroundWindow`-equivalent calls succeeded — OS foreground-lock protections routinely refuse them silently.
- **Prefer locating controls from the current screen** (by name, label, role, or accessibility tree) **over fixed coordinates.**
- **Treat every click and keypress as unconfirmed** until its visible effect is verified against a specific expectation, not a proxy.
- **Use one action followed by one verification.** Never batch multiple GUI-changing actions before checking any of them.
- **Reacquire the current GUI state** after any movement, resize, dialog, navigation, external tool call, or unexpected result.
- **Stop and diagnose** when observed state differs from expected state — do not continue a scripted sequence from an invalid state.
- **Capture evidence for both passes and failures.**
- **Separate automation errors from application defects** — rule out "my input went to the wrong window" before reporting "the app is broken."

## 4. Preflight procedure

Run this before any test action:

1. **Confirm the expected application process is running** (process list, not assumption).
2. **Identify the application by stable attributes**: exact or matching window title, process name, distinctive on-screen text, or layout — never by "it's probably the one I just launched."
3. **Bring the application to the foreground** and **verify** it actually became foreground (see §5) — do not trust the API call's return value alone.
4. **Confirm it is neither minimized nor obscured** by another window.
5. **Record current window position and size as a temporary observation only** — re-derive it before every subsequent action, never treat it as durable.
6. **Check screen resolution and display scaling** if available; a coordinate system mismatch between your input APIs and the accessibility APIs is a real, hard-to-diagnose failure mode (see §16, DPI investigation).
7. **Identify unrelated windows that could steal focus** (browsers, IDEs, other app instances) — you do not need to close them, but you must know they exist and re-check foreground after any action that could plausibly hand them focus.
8. **Detect startup dialogs, error dialogs, splash screens, or modal windows** before proceeding.
9. **Navigate to a known initial state** and confirm you're in it.
10. **Capture a baseline screenshot** scoped to the target window only (see §9 — never capture the full desktop).
11. **Define the expected result and required evidence for each test** before starting it.
12. **Determine the reset method** for this test before starting it — how will you get back to a known state if it fails midway?

If the target application cannot be brought to the foreground after
reasonable retries: **stop, do not click blind, and report a blocked
precondition** rather than guessing at coordinates on an unconfirmed window.

## 5. Observe → Act → Verify loop

Mandatory for every meaningful interaction. Do not skip or reorder steps.
Do not batch multiple loop iterations before verifying any of them —
intermediate states matter.

1. Capture or inspect the current screen/accessibility tree.
2. Confirm the target application and intended control are visible in it.
3. Confirm no modal dialog or overlay blocks the action.
4. **Re-identify the control from the current state** — never reuse a reference or coordinate from a prior loop iteration.
5. Bring the target window to foreground and **verify** (§5.1) before any input.
6. Move the pointer to the newly determined target.
7. Where possible, confirm the pointer is over the intended control before clicking.
8. Perform **exactly one** click, keypress, or text-entry action.
9. Wait for a **state-dependent completion condition**, not a fixed delay assumed to be "long enough" (§8).
10. Capture or inspect the resulting screen.
11. Verify the **specific** expected change — not a proxy signal.
12. If confirmed: continue. If not: **stop**, classify the discrepancy (§11), and recover (§12) before any further input.

### 5.1 Foreground verification, concretely

"Verified" means checking an independent signal after attempting to focus
the window — for example, comparing the current foreground window's handle
or title against the target, or a UI Automation focus indicator on the
specific control. It does not mean assuming a focus API call succeeded
because it returned without an error, and it does not mean assuming a
window has focus because a screenshot of it looks correct — some capture
methods render window content regardless of whether that window is actually
focused or even visible on top.

## 6. Window focus and foreground protocol

- **Explicitly activate the application before any keyboard input.** Never type immediately after a terminal command, file operation, or screenshot — assume focus may have changed.
- **Verify activation with current evidence**: foreground window handle/title match, a focus-indicator/caret in the target control, a selected-state change, or another available signal. A successful window-content screenshot is *not* sufficient evidence of focus.
- **If focus is uncertain, click a safe, non-destructive region of the intended window first** (e.g., a neutral label or empty panel area) before typing or invoking shortcuts.
- **Do not send shortcuts** (including Ctrl+W, Escape, Alt+Tab, Enter) **until the active window is confirmed** — an unconfirmed shortcut can act on an entirely unintended application.
- **Reconfirm focus after**: opening or closing any dialog, switching applications, running a terminal command, taking a screenshot, any filesystem operation, or any wait longer than a few hundred milliseconds. Treat every one of these as a potential focus-stealing event.
- **If a foreground-activation call appears to succeed but the observed foreground window doesn't match the target, do not proceed.** This is a known, common failure mode (OS foreground-lock timeout protections silently refuse activation requests from background processes) — retry activation a bounded number of times with a short backoff; if it still fails, stop and report the environment as unable to grant focus rather than clicking blind.
- **Never use a destructive or state-changing shortcut as a way to test whether focus landed correctly.** Use a reversible probe (reading current focus/foreground state) instead.
- **If the intended application cannot be brought to the foreground after retries**: stop, capture the current foreground window's identity, and report a blocked precondition. Do not fall back to coordinate-only clicking on an unconfirmed window.

## 7. Coordinate and target-selection protocol

- Determine target locations from the **newest** available screenshot or live accessibility-tree query — never from an observation more than one action old.
- **Recalculate targets after** any window movement, resize, maximize/restore, scroll, layout change, or dialog appearance.
- **Prefer controls identified by label/name, role, or stable layout position** over raw pixel coordinates. When the accessibility tree exposes no stable identifier (common for custom-styled controls), match by exact visible text or accessible name — and verify that name against the live tree rather than assuming it matches the visible label (accessible names and visible text can differ, including punctuation).
- **Verify your element-lookup mechanism against a known, simple control before relying on it broadly.** A lookup helper that silently returns nothing for the wrong reason (e.g., a bad type/role mapping) is indistinguishable from "the control isn't there yet" unless you've proven the mechanism itself works.
- Use coordinates **only as a short-lived execution detail for the immediately following action** — never store and reuse them across a multi-step sequence.
- **Reject a coordinate outright** when the current screen no longer matches the screen it was derived from.
- Click near the **center** of a control, away from borders and neighboring controls.
- **Do not click while the interface is animating, loading, or otherwise visibly changing.**
- **Scroll in small increments and reacquire the target after each scroll** — do not scroll a large, unverified distance and assume the target is now visible at a computed offset.

## 8. Keyboard and text-entry protocol

- **Verify the intended input field has focus** (caret visible, field highlighted, or equivalent signal) before typing anything.
- **Clear existing text only through a deliberate, verified operation** (select-all + delete, or a field-clear API) — never assume a field was empty.
- **Avoid typing secrets or destructive commands** unless the test explicitly requires them; when it does, use disposable/local test credentials only, never real ones.
- **Enter text in controlled chunks when field behavior is uncertain**, verifying after each chunk.
- **Verify the rendered value after entry** — read it back from the control rather than assuming the typed string landed correctly.
- **Account for keyboard layout, modifier keys, autocomplete, and default-button behavior.**
- **Do not press Enter or Escape unless you know what it will do in the current control** — confirm first whether Enter submits a form, inserts a newline, activates a default (possibly destructive) button, or does nothing.

## 9. Waiting and synchronization

**Never rely on a fixed sleep as your only completion signal for a
consequential action.** A fixed delay that "usually works" is a latent
flake — prefer an explicit, observable completion condition:

- A button becomes enabled/disabled.
- A progress indicator appears then disappears.
- A new window or dialog appears (verified by title/handle, not just "some time passed").
- A status label or banner text changes to the expected value.
- A table row, list item, or field value appears/updates.
- A file is created or a log line appears.
- The interface is visually/structurally stable across two or more consecutive observations a short interval apart.

Define a **bounded** retry/poll strategy for every wait — never wait
indefinitely, and never repeatedly click while waiting for a condition (a
repeated click during a wait is itself an unverified action and risks
double-submission). If the condition isn't met within the bound, treat it
as a failed verification (§5 step 12) and go to recovery (§12), not as
license to keep clicking.

## 10. Dialog, overlay, and unexpected-window handling

Before every action, check for: modal confirmation dialogs, error dialogs,
file pickers, permission prompts, tooltips covering the target control,
context menus, dropdown menus, secondary application windows, crash
dialogs, and OS notifications obscuring the application.

To determine whether a new window belongs to the application under test:
check its owning process, its title against known application window
titles, or a parent/child relationship in the accessibility tree — do not
assume based on timing alone ("it appeared right after my click, so it
must be mine"). If a window's ownership is ambiguous, capture evidence of
it (title, screenshot) before touching it, then close it via its own
explicit close control (not a blind keyboard shortcut) so you don't
accidentally act on a window you don't actually control.

If an unrelated window unexpectedly has focus (e.g., a browser tab
belonging to something else entirely), do not interact with it beyond what
is needed to safely restore focus to the target application — record what
happened as evidence, then follow the recovery procedure (§12).

## 11. Evidence collection

For every test, record: a test identifier; a concise description of the
intended behavior; preconditions; the exact actions performed; a screenshot
**before** the critical action; a screenshot **after** the result; relevant
logs or file output; the expected result; the observed result; a status of
`pass | fail | blocked | inconclusive`; and a classification of application
defect vs. validation-agent error.

**A screenshot is not valid evidence unless you confirm it actually shows
the target application, the relevant control, and the result** — check this
before filing it as evidence, not after. Scope screenshots to the target
window, not the full desktop: a full-desktop capture routinely includes
unrelated windows (other applications, browser tabs, editors, chat
sessions) that were never part of the test and should not appear in
evidence artifacts. Prefer a capture method that renders a specific
window's content directly (e.g., window-content capture) over a
full-screen-region capture, both for evidence hygiene and because
full-screen capture can be unreliable on remote/virtual sessions.

## 12. Failure classification

Classify every unexpected result into one category before deciding what to
do next:

- **Application defect** — the application behaved incorrectly given confirmed-correct input delivery.
- **Automation targeting error** — the input went to the wrong window/control.
- **Focus error** — the target window was not actually foreground when input was sent.
- **Synchronization error** — the action was taken before the UI finished updating from a prior action.
- **Invalid precondition** — the test started from a state other than the one it assumed.
- **Environment issue** — display/DPI mismatch, unrelated process interference, resource unavailable.
- **Ambiguous result** — the effect can't be distinguished between two or more of the above from available evidence.
- **Test-design issue** — the test itself specifies an unreachable or ill-defined state.
- **Evidence-capture failure** — the action may have succeeded or failed, but the evidence captured doesn't show which.

**Do not report an application defect until focus, targeting,
synchronization, and environment errors have been explicitly ruled out or
the evidence clearly isolates the application as the cause.** When in
doubt, classify as ambiguous/inconclusive rather than asserting a defect.

## 13. Recovery procedure

On any unexpected result:

1. **Stop issuing input immediately.**
2. Capture the current screen (window-scoped).
3. Record the last confirmed state and the last action taken.
4. Check the active/foreground window and any visible dialogs.
5. Determine whether the action landed on the intended target at all.
6. Determine whether the application is still responsive.
7. Classify the failure (§12).
8. Restore a known state using the **least destructive** method available (e.g., navigate back, close an unintended dialog via its own control — not force-kill unless nothing else works).
9. **Reacquire all target positions/references** — nothing carries over from before the failure.
10. Retry only if the original action is confirmed safe and idempotent, or after the application has been reset to a known state. **Never blindly repeat a click or shortcut as a first response.**
11. If reliable recovery isn't possible, **mark the result inconclusive** and move on rather than continuing to guess.

## 14. Destructive-action safeguards

For any action that deletes, overwrites, submits, closes-without-saving, or
otherwise alters persistent state:

- Perform a **second verification immediately before** the action (target window, target control, both reconfirmed fresh).
- Confirm the data being affected is disposable test data, not real user data.
- Capture evidence of the **pre-action state**.
- Have a defined rollback/reset method **before** performing the action, not improvised after.
- Verify the **resulting persistent state** afterward (not just the UI acknowledgment of the action).
- **Never target a shared process/window by a non-unique identifier** (e.g., kill-by-image-name) when other processes with the same name could exist on the machine — resolve to the exact PID/handle for the process you actually launched or are actually driving, and kill only that.

## 15. Test execution template

```text
Test ID:
Objective:
Preconditions:
Known initial state:
Target window identity:
Expected result:
Required evidence:
Reset method:

Step:
Current observed state:
Target control:
Focus verification:
Action:
Completion condition:
Observed result:
Evidence:
Decision:
```

## 16. Lessons derived from the reviewed session

Source: a `PlantLibrary_PyApp` (`PlantLibrary_Workspace/implementation/System_Integration_MVP`) `SYS-VAL-PYAPP-01` GUI validation session, 2026-07-13. Full narrative and screenshots: `PlantLibrary_Workspace/implementation/System_Integration_MVP/validation/evidence/MVP-VALIDATION-20260708-01/EV-011_pyapp_gui_walkthrough_20260713.md` and `.../pyapp_gui/*.png`.

| Observed mistake | Evidence | Consequence | Root cause | Preventive rule | Detection or recovery rule |
|---|---|---|---|---|---|
| First screenshot captured the entire desktop, not the target window | `pyapp_gui/01_startup.png` (superseded) — captured the full 3440x1440 desktop including unrelated IDE/browser/chat windows | Evidence artifact contained content unrelated to (and outside the scope of) the test | Screenshot helper used a full-virtual-screen capture (`CopyFromScreen` over `SystemInformation.VirtualScreen`) instead of scoping to the target window | §11: scope every screenshot to the target window; verify before filing as evidence | §9: prefer a window-content capture method over full-screen-region capture |
| Full-screen capture method (`CopyFromScreen`) intermittently threw "invalid handle" on later attempts | Repeated `Ausnahme … CopyFromScreen … Das Handle ist ungültig` errors mid-session | Lost screenshots at points where evidence was needed; had to retry | Screen-region capture is sensitive to session/display state on the remote session in use | §9: prefer window-content capture over screen-region capture for reliability, not just scope | — |
| Clicking a nav item via UI-Automation `Select`/`Invoke` patterns reported success but did not navigate | `02_settings.png`/`02b_settings_invoke.png` still showed the Dashboard page after `Select-Elem`/`Invoke-Elem` calls returned without error | Two full loop iterations spent before the real cause (custom-styled control ignores these patterns) was found | Assumed a UI-Automation pattern call succeeding was equivalent to the control's real click behavior, without verifying against the visible result first | §5 step 11: verify the *specific* expected change, not just that an API call didn't error | §5.1 / §7: verify your interaction mechanism against a known control before relying on it broadly |
| Element lookup for "Account & Sync" repeatedly returned nothing | Multiple `Find-Elem`/`Find-ElemContains` calls with `ControlType "Text"` found nothing; the control was actually a `ListItem` (confirmed via a full tree dump) | Wasted attempts searching for the wrong control type before falling back to a full tree listing | Assumed a control's type without checking the live accessibility tree first | §7: verify the element-lookup mechanism/assumptions against the live tree, don't assume a role | §12 step 5: when a lookup keeps failing, check whether the *lookup itself* is wrong before assuming the control is absent |
| A confirmed-correct click on a confirmed-correct element still didn't navigate the app | `12_account_sync_fixed.png` unchanged after clicking a correctly-located "Account & Sync" `ListItem` | Time spent investigating a DPI-scaling hypothesis (added `SetProcessDpiAwarenessContext`) that turned out not to be the cause | Root cause (foreground/focus, see next row) was not yet suspected; a plausible but wrong hypothesis was pursued first | §12 step 5: before elaborating a hypothesis, test the cheapest alternative explanation first (verify foreground) | §6: foreground verification is the *first* thing to check when a confirmed-correct click has no effect |
| Clicking on **any** nav item, not just one specific control, silently had no effect | `13_sanity_plants.png` unchanged after clicking "Plants" — a simple, unambiguous, always-visible control | Confirmed the fault was systemic (focus/delivery), not control-specific — this was the actual breakthrough | The application window was not the OS foreground window; clicks were being delivered elsewhere. Window-content screenshots (`PrintWindow`-style capture) kept showing the "expected" app state regardless, masking the real cause | §1/§5.1: a correct-looking screenshot does not prove focus; verify foreground independently on every click | §6: reconfirm foreground before every click, not just once at session start |
| A click intended for the app's "Sign in" button instead landed on an unrelated browser tab and opened a Google Lens image-search dialog | `28b_browser.png` shows a "Mit Lens in einem Bild suchen" dialog on a Chrome "New Tab" page, immediately after a `Click-ElemReal` call targeting the PyApp window | An input was delivered to a completely unintended, unrelated application — low-consequence here (opened a search dialog) but the same class of failure could hit a destructive control in a different app | `SetForegroundWindow`-equivalent call was silently refused by the OS foreground-lock-timeout protection; the click proceeded anyway without verifying the target actually became foreground | §6: never click without verifying the target window actually became foreground first; treat a failed activation as a stop condition, not a proceed condition | §5.1/§12: check the foreground window's identity immediately after any unexpected result, before doing anything else |
| Same foreground-activation call kept failing intermittently even after a first fix was added | Repeated `Could not bring 'Plant Library' to foreground … (currently '')` failures across several consecutive attempts, succeeding only after a delay and an unrelated diagnostic check | Several retries consumed before the action succeeded; environment turned out to be a real, actively-used desktop where window/focus state could change for reasons outside the agent's control | The session ran on the operator's real, live desktop (confirmed by other real windows — IDE, browser, emulator — visible throughout), not an isolated test environment; external focus changes are a real, ongoing risk, not a one-time setup problem | §6: reconfirm foreground after *every* action, including ones after which focus "should" be stable — an interactive desktop can be used by something/someone else at any time | §12 step 4: always re-check the active window as the first recovery step, don't assume the last-known focus owner is still correct |
| A dialog-lookup helper reported "not found" for a dialog that (per a foreground-window check moments later) was actually open | `Get-TopWindow`'s window-enumeration helper returned no match for "First Sync Assistant" immediately after a click that opened it; a separate check of the OS foreground window's title showed `First Sync Assistant` was in fact frontmost | Led to re-clicking the same trigger control believing the first click had failed, risking a duplicate dialog/action | The enumeration API used for the lookup was itself unreliable for freshly-opened windows; its negative result was trusted without cross-checking | §7: verify a lookup mechanism's reliability, especially for freshly-created windows; a negative result is not proof of absence | §10/§12: cross-check an unexpected "not found" against an independent signal (e.g., foreground window identity) before retrying the triggering action |
| Reconfiguring a connection setting and reconnecting appeared to succeed (status banner and persisted DB values were correct) but the actual downstream behavior (browser navigation target) kept using the old, stale value | Banner read "Connected to … (OIDC issuer: …)" and a direct database read confirmed the correct value, yet the subsequent browser-driven flow repeatedly navigated to the old host across three separate attempts | Multiple reconnect/retry cycles spent chasing the wrong layer (config value, cache-busting the input text) before finding the actual fix (restarting the running process) | A proxy signal (UI status text, persisted config value) was treated as confirmation of the actual expected behavior (correct navigation target), which depended on additional in-process state that the proxy didn't reflect | §5 step 11/§12 step 5: verify the *specific* expected outcome of an action, not a related-but-insufficient proxy signal; when a proxy keeps confirming success but the real behavior doesn't change, suspect a different layer of state entirely | §12: when the same fix is verified "successful" by a proxy multiple times but the real symptom persists, stop repeating the same verification and check a different layer (e.g., restart the process under test) |
| An attempt to close a stray, unintended browser tab via a keyboard shortcut failed | `SendKeys.SendWait` calls raised "Zugriff verweigert" (access denied) when targeting a window that may not have actually had focus | A recovery action itself silently failed without an immediately obvious downstream effect | Same root cause as the foreground failures above — the shortcut was sent without independently confirmed focus | §6: never send a shortcut, including a recovery shortcut, without confirmed focus | §12 step 2/4: capture current state and check the active window before assuming a recovery shortcut worked |
| A broad process-kill was attempted by image name rather than a specific process ID | An attempted `taskkill /F /IM python.exe` (intended to restart one specific PyApp instance) was blocked before execution because it would have terminated *every* `python.exe` process on the shared machine | Would have terminated unrelated Python processes on a machine known to be in active use by other work, had it not been intercepted | The process to restart was identified by image name instead of resolving to its specific PID first | §14: never target a shared resource by a non-unique identifier; resolve to the exact PID/handle first | §12 step 8: use the least destructive, most specific method available for any restore/reset action |

## 17. Anti-patterns

Explicitly prohibited. Every example below is a paraphrase of a real
mistake made or narrowly avoided in the reviewed session (§16):

- "The button was at this coordinate before, so click there again." — Always re-locate from the current state (§7).
- "The click / API call probably worked; continue to the next step." — Verify the specific expected change before continuing (§5).
- "Type immediately after switching from the terminal / after a screenshot." — Reconfirm focus after any context switch first (§6).
- "Repeat the click because nothing happened." — Diagnose before retrying; nothing happening is itself informative (§5, §12).
- "Take a screenshot and assume it captured the correct window." — A window-content screenshot can be correct even when the window isn't focused; screenshot success ≠ focus (§1, §6).
- "The lookup said 'not found', so retry the action that created it." — A negative lookup result can itself be wrong; cross-check before retrying (§10, §12).
- "The status banner/toast says it worked, so the underlying behavior must be correct now." — Verify the actual expected behavior, not a proxy for it (§5).
- "Continue even though the screen differs from the expected state." — Stop and classify the discrepancy; never proceed from an unconfirmed state (§5, §12).
- "Use a long prerecorded coordinate sequence." — Coordinates are single-use, derived fresh each time (§7).
- "Kill the process by image name, it's probably just mine." — Resolve to the exact PID/handle on a shared machine (§14).
- "Report a product bug before checking whether the input went to the wrong window." — Rule out focus/targeting/timing/environment errors first (§12).

---

## Appendix A — Preflight checklist

- [ ] Confirmed the expected application process is running.
- [ ] Identified the application by a stable attribute (title/process/text/layout).
- [ ] Brought it to the foreground and **verified** foreground independently.
- [ ] Confirmed not minimized/obscured.
- [ ] Noted current window position/size as a temporary observation only.
- [ ] Checked display resolution/scaling if relevant.
- [ ] Identified unrelated windows that could steal focus.
- [ ] Checked for startup/error/splash/modal windows.
- [ ] Navigated to and confirmed a known initial state.
- [ ] Captured a window-scoped baseline screenshot.
- [ ] Defined expected result and required evidence for the test.
- [ ] Defined the reset method if the test fails midway.

## Appendix B — Per-action checklist

Before the action:
- [ ] Observed current screen/tree state (not a stale one).
- [ ] Confirmed foreground window matches target — independently verified, not assumed.
- [ ] Re-identified the target control from the current state.
- [ ] Checked for blocking dialogs/overlays.
- [ ] Defined the expected state change and how it will be verified.

After the action:
- [ ] Waited for an observable completion condition (not a blind fixed delay for anything consequential).
- [ ] Captured the resulting window-scoped state.
- [ ] Verified the exact expected change (not a proxy signal).
- [ ] Stopped and classified on any mismatch — did not continue regardless.

## Appendix C — Failure-recovery checklist

- [ ] Stopped issuing input.
- [ ] Captured current window-scoped screen.
- [ ] Recorded last confirmed state and last action.
- [ ] Checked active/foreground window and visible dialogs.
- [ ] Determined whether the action landed on the intended target.
- [ ] Determined whether the application is still responsive.
- [ ] Classified the failure (§12).
- [ ] Restored a known state via the least destructive method.
- [ ] Reacquired all target positions/references — none carried over.
- [ ] Retried only if safe/idempotent or after a confirmed reset; never blindly repeated the same input.
- [ ] Marked inconclusive if reliable recovery wasn't possible.

## Appendix D — Test-result reporting template

```text
Test ID:
Description:
Preconditions:
Actions performed:
Screenshot before:
Screenshot after:
Logs/output:
Expected result:
Observed result:
Status: pass | fail | blocked | inconclusive
Classification: application defect | automation error | focus error |
  synchronization error | invalid precondition | environment issue |
  ambiguous | test-design issue | evidence-capture failure
Notes:
```
