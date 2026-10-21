---
id: av-imu-thermal-drift-after-pad-soak-2026-07
domain: avionics
system: flight-computer-b2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2026-07-04
tags: [avionics, bundle, pad]
---

# IMU thermal drift after pad soak

## Context

A wet dress rehearsal on flight-computer-b2, while the harness bundle was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the harness bundle moved outside the expected band within 25 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The harness bundle had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and a functional test was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the harness bundle instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
