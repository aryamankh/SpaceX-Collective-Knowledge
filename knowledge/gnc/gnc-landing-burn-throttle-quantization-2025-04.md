---
id: gnc-landing-burn-throttle-quantization-2025-04
domain: gnc
system: booster-b19
author: richiksc
reviewed_by: CAM-Gerlach
status: reviewed
severity: high
created: 2025-04-14
tags: [estimator, gnc, reflight]
---

# Landing burn throttle quantization

## Context

A cryo proof on booster-b19, while the attitude estimator was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the attitude estimator moved outside the expected band within 37 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The attitude estimator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The torque spec was revised and a dimensional check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the attitude estimator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
