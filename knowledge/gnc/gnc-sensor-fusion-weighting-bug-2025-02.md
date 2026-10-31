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
