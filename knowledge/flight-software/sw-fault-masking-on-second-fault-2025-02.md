---
id: sw-fault-masking-on-second-fault-2025-02
domain: flight-software
system: flight-software-v7
author: aryamankha
reviewed_by: shahar603
status: reviewed
severity: high
created: 2025-02-08
tags: [flight, pad, table]
---

# Fault masking on second fault

## Context

The first integrated flight on flight-software-v7, while the parameter table was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the parameter table moved outside the expected band within 8 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The parameter table had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The purge dwell was revised and a pre-run visual was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the parameter table instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
