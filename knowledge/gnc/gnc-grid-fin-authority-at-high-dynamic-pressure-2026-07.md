---
id: gnc-grid-fin-authority-at-high-dynamic-pressure-2026-07
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-07-21
tags: [gnc, pad, schedule]
---

# Grid fin authority at high dynamic pressure

## Context

A reflight turnaround on booster-b19, while the grid fin schedule was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the grid fin schedule moved outside the expected band within 6 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The grid fin schedule had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The torque spec was revised and a dimensional check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the grid fin schedule instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
