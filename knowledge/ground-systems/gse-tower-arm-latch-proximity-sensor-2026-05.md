---
id: gse-tower-arm-latch-proximity-sensor-2026-05
domain: ground-systems
system: ols-tower-2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2026-05-24
tags: [clamp, ground, pad]
---

# Tower arm latch proximity sensor

## Context

A wet dress rehearsal on ols-tower-2, while the hold-down clamp was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the hold-down clamp moved outside the expected band within 25 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The hold-down clamp had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The purge dwell was revised and a torque re-verification was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the hold-down clamp instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
