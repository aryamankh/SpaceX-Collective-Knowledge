---
id: ops-countdown-poll-drift-2024-10
domain: flight-ops
system: launch-complex-39a
author: aryamankh
reviewed_by: aryamankh
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
