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
