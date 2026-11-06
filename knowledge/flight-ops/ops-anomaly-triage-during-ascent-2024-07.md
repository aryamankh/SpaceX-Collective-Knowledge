---
id: ops-anomaly-triage-during-ascent-2024-07
domain: flight-ops
system: launch-complex-39a
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2024-07-28
tags: [flight, reflight, set]
---

# Anomaly triage during ascent

## Context

A reflight turnaround on launch-complex-39a, while the weather rule set was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the weather rule set moved outside the expected band within 28 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The weather rule set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The acceptance band was revised and a leak check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the weather rule set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
