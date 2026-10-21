---
id: sw-parameter-table-version-skew-2026-06
domain: flight-software
system: flight-software-v7
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2026-06-11
tags: [flight, tree, turnaround]
---

# Parameter table version skew

## Context

A wet dress rehearsal on flight-software-v7, while the fault tree was under watch by the console. The run was configured to the current published limits.

## What happened

Pressure on the fault tree moved outside the expected band within 25 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The fault tree had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The torque spec was revised and an endoscope pass was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the fault tree instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
