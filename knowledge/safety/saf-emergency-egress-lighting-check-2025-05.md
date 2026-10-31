---
id: saf-emergency-egress-lighting-check-2025-05
domain: safety
system: pad-operations
author: shahar603
reviewed_by: jhpratt
status: reviewed
severity: low
created: 2025-05-11
tags: [analysis, hotfire, safety]
---

# Emergency egress lighting check

## Context

A cryo proof on pad-operations, while the hazard analysis was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the hazard analysis moved outside the expected band within 8 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The hazard analysis had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The sampling rate was revised and a leak check was added to the task list before the next run. Owner: shahar603.

## What we would do differently

Stop on the first excursion of the hazard analysis instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
