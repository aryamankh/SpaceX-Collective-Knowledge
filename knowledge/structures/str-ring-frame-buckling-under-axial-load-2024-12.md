---
id: str-ring-frame-buckling-under-axial-load-2024-12
domain: structures
system: starship-s38
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-12-08
tags: [frame, reflight, structures]
---

# Ring frame buckling under axial load

## Context

The first integrated flight on starship-s38, while the ring frame was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the ring frame moved outside the expected band within 16 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The ring frame had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The inspection interval was revised and a torque re-verification was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the ring frame instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
