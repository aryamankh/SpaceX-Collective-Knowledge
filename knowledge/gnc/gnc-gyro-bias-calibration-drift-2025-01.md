---
id: gnc-gyro-bias-calibration-drift-2025-01
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2025-01-28
tags: [cryo, estimator, gnc]
---

# Gyro bias calibration drift

## Context

A wet dress rehearsal on booster-b19, while the attitude estimator was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the attitude estimator moved outside the expected band within 20 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The attitude estimator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The inspection interval was revised and a functional test was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the attitude estimator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
