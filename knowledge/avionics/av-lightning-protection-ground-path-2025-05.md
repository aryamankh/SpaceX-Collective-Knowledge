---
id: av-lightning-protection-ground-path-2025-05
domain: avionics
system: flight-computer-b2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2025-05-29
tags: [avionics, cryo, termination]
---

# Lightning protection ground path

## Context

A cryo proof on flight-computer-b2, while the CAN termination was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the CAN termination moved outside the expected band within 16 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The can termination had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the CAN termination instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
