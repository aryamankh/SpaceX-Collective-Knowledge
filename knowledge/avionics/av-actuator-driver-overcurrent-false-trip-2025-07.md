---
id: av-actuator-driver-overcurrent-false-trip-2025-07
domain: avionics
system: flight-computer-b2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-07-21
tags: [avionics, reflight, termination]
---

# Actuator driver overcurrent false trip

## Context

A static fire on flight-computer-b2, while the CAN termination was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the CAN termination moved outside the expected band within 15 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The can termination had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The chilldown ramp was revised and a torque re-verification was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the CAN termination instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
