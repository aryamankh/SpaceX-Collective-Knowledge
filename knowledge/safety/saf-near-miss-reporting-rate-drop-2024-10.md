---
id: saf-near-miss-reporting-rate-drop-2024-10
domain: safety
system: pad-operations
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2024-10-25
tags: [kit, pad, safety]
---

# Near-miss reporting rate drop

## Context

A reflight turnaround on pad-operations, while the lockout tagout kit was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the lockout tagout kit moved outside the expected band within 22 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The lockout tagout kit had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The inspection interval was revised and a torque re-verification was added to the task list before the next run. Owner: shahar603.

## What we would do differently

Stop on the first excursion of the lockout tagout kit instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
