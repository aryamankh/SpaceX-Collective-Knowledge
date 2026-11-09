---
id: gnc-attitude-estimator-divergence-in-coast-2026-05
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2026-05-04
tags: [allocator, gnc, pad]
---

# Attitude estimator divergence in coast

## Context

A static fire on booster-b19, while the control allocator was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the control allocator moved outside the expected band within 15 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The control allocator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The inspection interval was revised and a dimensional check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the control allocator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-bank-reversal-chatter-2026-01
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-01-12
tags: [cryo, gnc, schedule]
---

# Bank reversal chatter

## Context

A night tanking on booster-b19, while the grid fin schedule was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the grid fin schedule moved outside the expected band within 20 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The grid fin schedule had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The sampling rate was revised and a functional test was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the grid fin schedule instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-control-allocator-saturation-in-transonic-2024-05
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-05-26
tags: [gnc, hotfire, scheduler]
---

# Control allocator saturation in transonic

## Context

A cryo proof on booster-b19, while the flap scheduler was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the flap scheduler moved outside the expected band within 39 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The flap scheduler had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The chilldown ramp was revised and a leak check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the flap scheduler instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-flap-scheduling-overshoot-on-entry-2025-05
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2025-05-19
tags: [allocator, cryo, gnc]
---

# Flap scheduling overshoot on entry

## Context

A wet dress rehearsal on booster-b19, while the control allocator was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the control allocator moved outside the expected band within 40 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The control allocator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The chilldown ramp was revised and a dimensional check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the control allocator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-grid-fin-authority-at-high-dynamic-pressure-2026-07
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-07-21
tags: [gnc, pad, schedule]
---

# Grid fin authority at high dynamic pressure

## Context

A reflight turnaround on booster-b19, while the grid fin schedule was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the grid fin schedule moved outside the expected band within 6 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The grid fin schedule had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The torque spec was revised and a dimensional check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the grid fin schedule instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-gyro-bias-calibration-drift-2025-01
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2025-01-28
tags: [cryo, estimator, gnc]
---

# Gyro bias calibration drift

## Context

A wet dress rehearsal on booster-b19, while the attitude estimator was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the attitude estimator moved outside the expected band within 20 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The attitude estimator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The inspection interval was revised and a functional test was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the attitude estimator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-landing-burn-throttle-quantization-2025-04
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-04-14
tags: [estimator, gnc, reflight]
---

# Landing burn throttle quantization

## Context

A cryo proof on booster-b19, while the attitude estimator was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the attitude estimator moved outside the expected band within 37 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The attitude estimator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The torque spec was revised and a dimensional check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the attitude estimator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-roll-coupling-in-high-wind-2025-01
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-01-25
tags: [allocator, gnc, turnaround]
---

# Roll coupling in high wind

## Context

A night tanking on booster-b19, while the control allocator was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the control allocator moved outside the expected band within 21 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The control allocator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The chilldown ramp was revised and a functional test was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the control allocator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-sensor-fusion-weighting-bug-2025-02
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-02-17
tags: [gnc, pad, schedule]
---

# Sensor fusion weighting bug

## Context

A static fire on booster-b19, while the grid fin schedule was under watch by the console. The run was configured to the current published limits.

## What happened

Pressure on the grid fin schedule moved outside the expected band within 23 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The grid fin schedule had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The acceptance band was revised and an endoscope pass was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the grid fin schedule instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-six-dof-sim-fidelity-versus-flight-2026-07
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2026-07-02
tags: [gnc, pad, quantizer]
---

# Six-DOF sim fidelity versus flight

## Context

A night tanking on booster-b19, while the throttle quantizer was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the throttle quantizer moved outside the expected band within 14 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The throttle quantizer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The sampling rate was revised and a leak check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the throttle quantizer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-star-tracker-lost-in-space-time-2025-05
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-05-09
tags: [gnc, hotfire, scheduler]
---

# Star tracker lost-in-space time

## Context

A static fire on booster-b19, while the flap scheduler was under watch by the console. The run was configured to the current published limits.

## What happened

Pressure on the flap scheduler moved outside the expected band within 40 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The flap scheduler had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The torque spec was revised and a leak check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the flap scheduler instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: gnc-trajectory-replan-latency-2025-06
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2025-06-02
tags: [estimator, gnc, turnaround]
---

# Trajectory replan latency

## Context

A cryo proof on booster-b19, while the attitude estimator was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the attitude estimator moved outside the expected band within 39 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The attitude estimator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the attitude estimator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


