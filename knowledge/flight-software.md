---
id: sw-abort-rule-false-positive-2025-08
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: low
created: 2025-08-09
tags: [cryo, flight, tree]
---

# Abort rule false positive

## Context

The first integrated flight on flight-software-v7, while the fault tree was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the fault tree moved outside the expected band within 20 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The fault tree had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The sampling rate was revised and a functional test was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the fault tree instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-boot-image-rollback-failure-2026-07
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2026-07-14
tags: [encoder, flight, pad]
---

# Boot image rollback failure

## Context

A cryo proof on flight-software-v7, while the telemetry encoder was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the telemetry encoder moved outside the expected band within 40 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The telemetry encoder had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The chilldown ramp was revised and a leak check was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the telemetry encoder instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-config-hash-mismatch-at-load-2026-06
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: low
created: 2026-06-08
tags: [cryo, flight, table]
---

# Config hash mismatch at load

## Context

The first integrated flight on flight-software-v7, while the parameter table was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the parameter table moved outside the expected band within 18 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The parameter table had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The purge dwell was revised and a pre-run visual was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the parameter table instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-control-loop-timing-jitter-2026-02
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2026-02-26
tags: [flight, sequencer, turnaround]
---

# Control loop timing jitter

## Context

A cryo proof on flight-software-v7, while the mode sequencer was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the mode sequencer moved outside the expected band within 13 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The mode sequencer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The sampling rate was revised and an endoscope pass was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the mode sequencer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-fault-masking-on-second-fault-2025-02
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2025-02-08
tags: [flight, pad, table]
---

# Fault masking on second fault

## Context

The first integrated flight on flight-software-v7, while the parameter table was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the parameter table moved outside the expected band within 8 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The parameter table had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The purge dwell was revised and a pre-run visual was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the parameter table instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-logging-backpressure-2026-01
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2026-01-15
tags: [cryo, flight, tree]
---

# Logging backpressure

## Context

A reflight turnaround on flight-software-v7, while the fault tree was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the fault tree moved outside the expected band within 27 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The fault tree had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The chilldown ramp was revised and a torque re-verification was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the fault tree instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-mode-transition-race-in-sequencer-2026-07
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2026-07-08
tags: [flight, pad, sequencer]
---

# Mode transition race in sequencer

## Context

A wet dress rehearsal on flight-software-v7, while the mode sequencer was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the mode sequencer moved outside the expected band within 21 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The mode sequencer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the mode sequencer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-parameter-table-version-skew-2026-06
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2026-06-11
tags: [flight, tree, turnaround]
---

# Parameter table version skew

## Context

A wet dress rehearsal on flight-software-v7, while the fault tree was under watch by the console. The run was configured to the current published limits.

## What happened

Pressure on the fault tree moved outside the expected band within 25 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The fault tree had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The torque spec was revised and an endoscope pass was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the fault tree instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-patch-rollback-after-hotfire-2026-05
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2026-05-23
tags: [flight, hotfire, rule]
---

# Patch rollback after hotfire

## Context

A night tanking on flight-software-v7, while the abort rule was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the abort rule moved outside the expected band within 4 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The abort rule had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The purge dwell was revised and a leak check was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the abort rule instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-sim-in-the-loop-coverage-gap-2026-06
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2026-06-22
tags: [encoder, flight, reflight]
---

# Sim-in-the-loop coverage gap

## Context

A night tanking on flight-software-v7, while the telemetry encoder was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the telemetry encoder moved outside the expected band within 3 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The telemetry encoder had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the telemetry encoder instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-telemetry-encoder-buffer-overrun-2026-06
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2026-06-29
tags: [cryo, encoder, flight]
---

# Telemetry encoder buffer overrun

## Context

A static fire on flight-software-v7, while the telemetry encoder was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the telemetry encoder moved outside the expected band within 38 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The telemetry encoder had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The inspection interval was revised and a torque re-verification was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the telemetry encoder instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: sw-watchdog-timeout-during-engine-start-2024-08
domain: flight-software
system: flight-software-v7
author: SivilTaram
reviewed_by: marsoperator
status: reviewed
severity: low
created: 2024-08-10
tags: [flight, hotfire, timer]
---

# Watchdog timeout during engine start

## Context

The first integrated flight on flight-software-v7, while the watchdog timer was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the watchdog timer moved outside the expected band within 21 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The watchdog timer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the watchdog timer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


