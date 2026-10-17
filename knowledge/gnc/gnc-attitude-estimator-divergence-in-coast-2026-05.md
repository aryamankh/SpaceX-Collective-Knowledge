---
id: gnc-attitude-estimator-divergence-in-coast-2026-05
domain: gnc
system: booster-b19
author: richiksc
reviewed_by: shahar603
status: reviewed
severity: medium
created: 2026-05-04
tags: [allocator, gnc, pad]
---

# Attitude estimator divergence in coast

## Context

A static fire on booster-b19, while the control allocator was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the control allocator moved outside the expected band within 15 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The control allocator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The inspection interval was revised and a dimensional check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the control allocator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
