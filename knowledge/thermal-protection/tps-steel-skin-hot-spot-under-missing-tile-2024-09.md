---
id: tps-steel-skin-hot-spot-under-missing-tile-2024-09
domain: thermal-protection
system: starship-heat-shield
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2024-09-13
tags: [inspection, reflight, thermal]
---

# Steel skin hot spot under missing tile

## Context

A static fire on starship-heat-shield, while the closeout inspection was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the closeout inspection moved outside the expected band within 10 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The closeout inspection had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The chilldown ramp was revised and a functional test was added to the task list before the next run. Owner: emmedve1.

## What we would do differently

Stop on the first excursion of the closeout inspection instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
