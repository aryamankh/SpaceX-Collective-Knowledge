---
id: mfg-rework-traceability-gap-2024-08
domain: manufacturing
system: high-bay-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-08-06
tags: [audit, manufacturing, turnaround]
---

# Rework traceability gap

## Context

The first integrated flight on high-bay-3, while the torque audit was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the torque audit moved outside the expected band within 38 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The torque audit had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The chilldown ramp was revised and a leak check was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the torque audit instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
