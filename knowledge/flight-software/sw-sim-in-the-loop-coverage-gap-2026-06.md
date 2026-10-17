---
id: sw-sim-in-the-loop-coverage-gap-2026-06
domain: flight-software
system: flight-software-v7
author: aryamankha
reviewed_by: shahar603
status: reviewed
severity: medium
created: 2026-06-22
tags: [encoder, flight, reflight]
---

# Sim-in-the-loop coverage gap

## Context

A night tanking on flight-software-v7, while the telemetry encoder was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the telemetry encoder moved outside the expected band within 3 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The telemetry encoder had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the telemetry encoder instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
