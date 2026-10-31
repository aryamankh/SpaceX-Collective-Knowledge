---
id: ops-recovery-fleet-positioning-2024-08
domain: flight-ops
system: launch-complex-39a
author: CAM-Gerlach
reviewed_by: mattythorne
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
