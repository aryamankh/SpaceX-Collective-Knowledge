---
id: mfg-station-takt-time-creep-2024-10
domain: manufacturing
system: high-bay-3
author: AstralZebulon
reviewed_by: jhpratt
status: reviewed
severity: low
created: 2024-10-22
tags: [hotfire, manufacturing, tracker]
---

# Station takt time creep

## Context

A night tanking on high-bay-3, while the laser tracker was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the laser tracker moved outside the expected band within 23 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The laser tracker had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The purge dwell was revised and a functional test was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the laser tracker instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
