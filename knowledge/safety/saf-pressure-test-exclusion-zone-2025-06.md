---
id: saf-pressure-test-exclusion-zone-2025-06
domain: safety
system: pad-operations
author: shahar603
reviewed_by: kknox
status: reviewed
severity: high
created: 2025-06-29
tags: [analysis, safety, turnaround]
---

# Pressure test exclusion zone

## Context

The first integrated flight on pad-operations, while the hazard analysis was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the hazard analysis moved outside the expected band within 32 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The hazard analysis had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The acceptance band was revised and a torque re-verification was added to the task list before the next run. Owner: shahar603.

## What we would do differently

Stop on the first excursion of the hazard analysis instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
