---
id: mfg-springback-compensation-2025-07
domain: manufacturing
system: high-bay-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2025-07-05
tags: [fixture, manufacturing, turnaround]
---

# Springback compensation

## Context

A night tanking on high-bay-3, while the fit-up fixture was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the fit-up fixture moved outside the expected band within 39 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The fit-up fixture had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The sampling rate was revised and a torque re-verification was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the fit-up fixture instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
