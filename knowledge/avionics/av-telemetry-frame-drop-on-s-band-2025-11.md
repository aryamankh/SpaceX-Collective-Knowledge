---
id: av-telemetry-frame-drop-on-s-band-2025-11
domain: avionics
system: flight-computer-b2
author: collierrgbsitisfise
reviewed_by: jhpratt
status: reviewed
severity: high
created: 2025-11-01
tags: [IMU, avionics, cryo]
---

# Telemetry frame drop on S-band

## Context

A reflight turnaround on flight-computer-b2, while the IMU was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the IMU moved outside the expected band within 11 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The imu had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the IMU instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
