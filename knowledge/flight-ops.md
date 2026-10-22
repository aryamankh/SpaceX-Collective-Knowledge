---
id: ops-anomaly-triage-during-ascent-2024-07
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2024-07-28
tags: [flight, reflight, set]
---

# Anomaly triage during ascent

## Context

A reflight turnaround on launch-complex-39a, while the weather rule set was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the weather rule set moved outside the expected band within 28 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The weather rule set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The acceptance band was revised and a leak check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the weather rule set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-chase-plane-comms-loss-2024-10
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2024-10-04
tags: [flight, set, turnaround]
---

# Chase plane comms loss

## Context

A reflight turnaround on launch-complex-39a, while the weather rule set was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the weather rule set moved outside the expected band within 9 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The weather rule set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The purge dwell was revised and a pre-run visual was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the weather rule set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-countdown-poll-drift-2024-10
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: low
created: 2024-10-12
tags: [cryo, flight, set]
---

# Countdown poll drift

## Context

A wet dress rehearsal on launch-complex-39a, while the weather rule set was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the weather rule set moved outside the expected band within 10 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The weather rule set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The chilldown ramp was revised and a functional test was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the weather rule set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-crew-rest-versus-window-trade-2025-03
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2025-03-08
tags: [flight, pad, set]
---

# Crew rest versus window trade

## Context

The first integrated flight on launch-complex-39a, while the weather rule set was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the weather rule set moved outside the expected band within 6 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The weather rule set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The inspection interval was revised and a leak check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the weather rule set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-observer-exclusion-zones-2025-09
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2025-09-07
tags: [checklist, flight, hotfire]
---

# Observer exclusion zones

## Context

The first integrated flight on launch-complex-39a, while the handover checklist was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the handover checklist moved outside the expected band within 25 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The handover checklist had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The chilldown ramp was revised and a leak check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the handover checklist instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-pad-crew-handover-checklist-2026-02
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2026-02-10
tags: [flight, reflight, rota]
---

# Pad crew handover checklist

## Context

A night tanking on launch-complex-39a, while the triage rota was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the triage rota moved outside the expected band within 13 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The triage rota had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the triage rota instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-post-flight-downlink-priority-2026-09
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: low
created: 2026-09-19
tags: [flight, hotfire, rota]
---

# Post-flight downlink priority

## Context

The first integrated flight on launch-complex-39a, while the triage rota was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the triage rota moved outside the expected band within 24 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The triage rota had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The purge dwell was revised and a dimensional check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the triage rota instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-range-asset-conflict-resolution-2025-01
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2025-01-06
tags: [flight, hotfire, poll]
---

# Range asset conflict resolution

## Context

A wet dress rehearsal on launch-complex-39a, while the countdown poll was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the countdown poll moved outside the expected band within 37 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The countdown poll had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and a leak check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the countdown poll instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-range-call-timing-on-hold-2026-03
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2026-03-29
tags: [flight, rota, turnaround]
---

# Range call timing on hold

## Context

A wet dress rehearsal on launch-complex-39a, while the triage rota was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the triage rota moved outside the expected band within 15 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The triage rota had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the triage rota instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-recovery-fleet-positioning-2024-08
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2024-08-10
tags: [cryo, flight, set]
---

# Recovery fleet positioning

## Context

A night tanking on launch-complex-39a, while the weather rule set was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the weather rule set moved outside the expected band within 20 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The weather rule set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The chilldown ramp was revised and a torque re-verification was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the weather rule set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-tanking-sequence-conflict-2026-10
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2026-10-06
tags: [checklist, flight, hotfire]
---

# Tanking sequence conflict

## Context

A reflight turnaround on launch-complex-39a, while the handover checklist was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the handover checklist moved outside the expected band within 17 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The handover checklist had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The sampling rate was revised and a dimensional check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the handover checklist instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: ops-weather-scrub-decision-tree-2024-07
domain: flight-ops
system: launch-complex-39a
author: VineethSendilraj
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2024-07-27
tags: [call, flight, hotfire]
---

# Weather scrub decision tree

## Context

A reflight turnaround on launch-complex-39a, while the range call was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the range call moved outside the expected band within 4 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The range call had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The inspection interval was revised and a pre-run visual was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the range call instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


