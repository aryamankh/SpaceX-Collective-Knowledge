---
id: ops-observer-exclusion-zones-2025-09
domain: flight-ops
system: launch-complex-39a
author: aryamankh
reviewed_by: aryamankh
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
