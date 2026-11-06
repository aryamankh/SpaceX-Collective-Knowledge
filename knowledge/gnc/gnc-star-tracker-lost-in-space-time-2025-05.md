---
id: gnc-star-tracker-lost-in-space-time-2025-05
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-05-09
tags: [gnc, hotfire, scheduler]
---

# Star tracker lost-in-space time

## Context

A static fire on booster-b19, while the flap scheduler was under watch by the console. The run was configured to the current published limits.

## What happened

Pressure on the flap scheduler moved outside the expected band within 40 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The flap scheduler had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The torque spec was revised and a leak check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the flap scheduler instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
