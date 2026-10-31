---
id: ops-range-asset-conflict-resolution-2025-01
domain: flight-ops
system: launch-complex-39a
author: CAM-Gerlach
reviewed_by: shahar603
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
