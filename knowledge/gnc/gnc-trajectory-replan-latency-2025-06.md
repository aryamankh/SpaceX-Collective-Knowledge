---
id: gnc-trajectory-replan-latency-2025-06
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2025-06-02
tags: [estimator, gnc, turnaround]
---

# Trajectory replan latency

## Context

A cryo proof on booster-b19, while the attitude estimator was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the attitude estimator moved outside the expected band within 39 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The attitude estimator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the attitude estimator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
