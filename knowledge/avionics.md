---
id: av-actuator-driver-overcurrent-false-trip-2025-07
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2025-07-21
tags: [avionics, reflight, termination]
---

# Actuator driver overcurrent false trip

## Context

A static fire on flight-computer-b2, while the CAN termination was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the CAN termination moved outside the expected band within 15 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The can termination had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The chilldown ramp was revised and a torque re-verification was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the CAN termination instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-battery-cell-imbalance-on-long-pad-2025-10
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2025-10-02
tags: [avionics, pad, transmitter]
---

# Battery cell imbalance on long pad

## Context

A cryo proof on flight-computer-b2, while the S-band transmitter was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the S-band transmitter moved outside the expected band within 15 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The s-band transmitter had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The sampling rate was revised and a functional test was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the S-band transmitter instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-can-bus-termination-fault-2026-10
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2026-10-08
tags: [avionics, limiter, pad]
---

# CAN bus termination fault

## Context

A static fire on flight-computer-b2, while the inrush limiter was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the inrush limiter moved outside the expected band within 13 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The inrush limiter had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The purge dwell was revised and an endoscope pass was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the inrush limiter instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-conformal-coat-masking-error-2025-06
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: low
created: 2025-06-10
tags: [avionics, bundle, hotfire]
---

# Conformal coat masking error

## Context

The first integrated flight on flight-computer-b2, while the harness bundle was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the harness bundle moved outside the expected band within 6 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The harness bundle had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the harness bundle instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-connector-keying-mismatch-on-test-rack-2025-02
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2025-02-01
tags: [avionics, bundle, hotfire]
---

# Connector keying mismatch on test rack

## Context

The first integrated flight on flight-computer-b2, while the harness bundle was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the harness bundle moved outside the expected band within 23 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The harness bundle had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The chilldown ramp was revised and a dimensional check was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the harness bundle instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-flight-computer-watchdog-reset-2025-10
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2025-10-28
tags: [IMU, avionics, turnaround]
---

# Flight computer watchdog reset

## Context

A wet dress rehearsal on flight-computer-b2, while the IMU was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the IMU moved outside the expected band within 17 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The imu had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the IMU instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-harness-chafe-at-raceway-exit-2024-11
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2024-11-28
tags: [avionics, cryo, watchdog]
---

# Harness chafe at raceway exit

## Context

A night tanking on flight-computer-b2, while the watchdog was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the watchdog moved outside the expected band within 36 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The watchdog had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the watchdog instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-imu-thermal-drift-after-pad-soak-2026-07
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: low
created: 2026-07-04
tags: [avionics, bundle, pad]
---

# IMU thermal drift after pad soak

## Context

A wet dress rehearsal on flight-computer-b2, while the harness bundle was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the harness bundle moved outside the expected band within 25 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The harness bundle had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and a functional test was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the harness bundle instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-lightning-protection-ground-path-2025-05
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2025-05-29
tags: [avionics, cryo, termination]
---

# Lightning protection ground path

## Context

A cryo proof on flight-computer-b2, while the CAN termination was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the CAN termination moved outside the expected band within 16 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The can termination had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the CAN termination instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-power-bus-inrush-trip-2026-06
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2026-06-20
tags: [avionics, cryo, limiter]
---

# Power bus inrush trip

## Context

A reflight turnaround on flight-computer-b2, while the inrush limiter was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the inrush limiter moved outside the expected band within 25 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The inrush limiter had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The purge dwell was revised and a dimensional check was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the inrush limiter instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-redundant-lane-desync-at-boot-2026-06
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2026-06-30
tags: [avionics, limiter, pad]
---

# Redundant lane desync at boot

## Context

A static fire on flight-computer-b2, while the inrush limiter was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the inrush limiter moved outside the expected band within 6 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The inrush limiter had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The purge dwell was revised and a leak check was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the inrush limiter instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: av-telemetry-frame-drop-on-s-band-2025-11
domain: avionics
system: flight-computer-b2
author: anonrig
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2025-11-01
tags: [IMU, avionics, cryo]
---

# Telemetry frame drop on S-band

## Context

A reflight turnaround on flight-computer-b2, while the IMU was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the IMU moved outside the expected band within 11 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The imu had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the IMU instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


