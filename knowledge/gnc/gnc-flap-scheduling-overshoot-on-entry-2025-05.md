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
