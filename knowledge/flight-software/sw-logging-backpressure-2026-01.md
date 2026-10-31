---
id: sw-logging-backpressure-2026-01
domain: flight-software
system: flight-software-v7
author: aryamankha
reviewed_by: mattythorne
status: reviewed
severity: medium
created: 2026-01-15
tags: [cryo, flight, tree]
---

# Logging backpressure

## Context

A reflight turnaround on flight-software-v7, while the fault tree was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the fault tree moved outside the expected band within 27 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The fault tree had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The chilldown ramp was revised and a torque re-verification was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the fault tree instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
