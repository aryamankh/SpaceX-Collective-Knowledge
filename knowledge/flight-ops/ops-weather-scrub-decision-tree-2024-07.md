---
id: ops-weather-scrub-decision-tree-2024-07
domain: flight-ops
system: launch-complex-39a
author: CAM-Gerlach
reviewed_by: kknox
status: reviewed
severity: critical
created: 2024-07-27
tags: [call, flight, hotfire]
---

# Weather scrub decision tree

## Context

A reflight turnaround on launch-complex-39a, while the range call was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the range call moved outside the expected band within 4 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The range call had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The inspection interval was revised and a pre-run visual was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the range call instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
