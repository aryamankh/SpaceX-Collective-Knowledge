---
id: prop-chamber-pressure-sensor-drift-2025-11
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2025-11-14
tags: [propulsion, reflight, transducer]
---

# Chamber pressure sensor drift

## Context

A night tanking on raptor-3, while the chamber pressure transducer was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the chamber pressure transducer moved outside the expected band within 5 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The chamber pressure transducer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The inspection interval was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the chamber pressure transducer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-crossfeed-transient-during-boostback-2024-08
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2024-08-22
tags: [cryo, propulsion, puck]
---

# Crossfeed transient during boostback

## Context

A reflight turnaround on raptor-3, while the thrust puck was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the thrust puck moved outside the expected band within 31 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The thrust puck had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the thrust puck instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-engine-controller-reset-under-emi-2026-04
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2026-04-07
tags: [hotfire, propulsion, turbopump]
---

# Engine controller reset under EMI

## Context

A wet dress rehearsal on raptor-3, while the turbopump was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the turbopump moved outside the expected band within 6 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The turbopump had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The torque spec was revised and a pre-run visual was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the turbopump instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-gimbal-bearing-fretting-after-static-fire-2026-07
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: low
created: 2026-07-28
tags: [hotfire, propulsion, turbopump]
---

# Gimbal bearing fretting after static fire

## Context

A night tanking on raptor-3, while the turbopump was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the turbopump moved outside the expected band within 39 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The turbopump had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The chilldown ramp was revised and a pre-run visual was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the turbopump instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-hot-gas-manifold-leak-after-30-s-run-2024-11
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2024-11-07
tags: [pad, propulsion, transducer]
---

# Hot gas manifold leak after 30 s run

## Context

A cryo proof on raptor-3, while the chamber pressure transducer was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the chamber pressure transducer moved outside the expected band within 12 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The chamber pressure transducer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the chamber pressure transducer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-igniter-torch-fouling-on-long-coast-2026-08
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2026-08-18
tags: [actuator, pad, propulsion]
---

# Igniter torch fouling on long coast

## Context

A wet dress rehearsal on raptor-3, while the TVC actuator was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the TVC actuator moved outside the expected band within 17 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The tvc actuator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The torque spec was revised and a torque re-verification was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the TVC actuator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-lox-dome-priming-waterhammer-2025-08
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: low
created: 2025-08-12
tags: [actuator, hotfire, propulsion]
---

# LOX dome priming waterhammer

## Context

A cryo proof on raptor-3, while the TVC actuator was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the TVC actuator moved outside the expected band within 38 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The tvc actuator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the TVC actuator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-mixture-ratio-trim-during-hover-2024-07
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2024-07-30
tags: [propulsion, turbopump, turnaround]
---

# Mixture ratio trim during hover

## Context

A static fire on raptor-3, while the turbopump was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the turbopump moved outside the expected band within 38 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The turbopump had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The inspection interval was revised and a pre-run visual was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the turbopump instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-raptor-tvc-actuator-oscillation-at-42-hz-2025-12
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2025-12-07
tags: [propulsion, puck, turnaround]
---

# Raptor TVC actuator oscillation at 42 Hz

## Context

A night tanking on raptor-3, while the thrust puck was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the thrust puck moved outside the expected band within 25 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The thrust puck had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The acceptance band was revised and a leak check was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the thrust puck instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-regen-channel-pressure-drop-drift-2026-07
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: medium
created: 2026-07-16
tags: [bearing, hotfire, propulsion]
---

# Regen channel pressure drop drift

## Context

A static fire on raptor-3, while the gimbal bearing was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the gimbal bearing moved outside the expected band within 19 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The gimbal bearing had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The purge dwell was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the gimbal bearing instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-thrust-puck-cracking-on-reflight-2024-10
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: high
created: 2024-10-25
tags: [hotfire, propulsion, turbopump]
---

# Thrust puck cracking on reflight

## Context

A static fire on raptor-3, while the turbopump was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the turbopump moved outside the expected band within 26 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The turbopump had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The purge dwell was revised and an endoscope pass was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the turbopump instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


---
id: prop-turbopump-chilldown-cavitation-on-restart-2025-03
domain: propulsion
system: raptor-3
author: bliutech
reviewed_by: marsoperator
status: reviewed
severity: critical
created: 2025-03-30
tags: [propulsion, transducer, turnaround]
---

# Turbopump chilldown cavitation on restart

## Context

A cryo proof on raptor-3, while the chamber pressure transducer was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the chamber pressure transducer moved outside the expected band within 39 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The chamber pressure transducer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The inspection interval was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the chamber pressure transducer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.


