---
id: ops-chase-plane-comms-loss-2024-10
domain: flight-ops
system: launch-complex-39a
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-10-04
tags: [flight, set, turnaround]
---

# Chase plane comms loss

## Context

A reflight turnaround on launch-complex-39a, while the weather rule set was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the weather rule set moved outside the expected band within 9 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The weather rule set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The purge dwell was revised and a pre-run visual was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the weather rule set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
