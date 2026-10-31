---
id: av-flight-computer-watchdog-reset-2025-10
domain: avionics
system: flight-computer-b2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-10-28
tags: [IMU, avionics, turnaround]
---

# Flight computer watchdog reset

## Context

A wet dress rehearsal on flight-computer-b2, while the IMU was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the IMU moved outside the expected band within 17 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The imu had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the IMU instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
