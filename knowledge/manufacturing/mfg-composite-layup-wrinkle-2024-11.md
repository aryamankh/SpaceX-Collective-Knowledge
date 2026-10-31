---
id: mfg-composite-layup-wrinkle-2024-11
domain: manufacturing
system: high-bay-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-11-23
tags: [cryo, manufacturing, table]
---

# Composite layup wrinkle

## Context

A static fire on high-bay-3, while the layup table was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the layup table moved outside the expected band within 12 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The layup table had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the layup table instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
