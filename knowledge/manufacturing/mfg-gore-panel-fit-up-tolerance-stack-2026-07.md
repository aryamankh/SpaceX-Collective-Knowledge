---
id: mfg-gore-panel-fit-up-tolerance-stack-2026-07
domain: manufacturing
system: high-bay-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-07-02
tags: [manufacturing, set, turnaround]
---

# Gore panel fit-up tolerance stack

## Context

A static fire on high-bay-3, while the weld parameter set was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the weld parameter set moved outside the expected band within 30 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The weld parameter set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The acceptance band was revised and a dimensional check was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the weld parameter set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
