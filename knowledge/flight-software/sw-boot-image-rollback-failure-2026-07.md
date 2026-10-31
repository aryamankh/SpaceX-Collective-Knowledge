---
id: sw-boot-image-rollback-failure-2026-07
domain: flight-software
system: flight-software-v7
author: aryamankha
reviewed_by: kknox
status: reviewed
severity: critical
created: 2026-07-14
tags: [encoder, flight, pad]
---

# Boot image rollback failure

## Context

A cryo proof on flight-software-v7, while the telemetry encoder was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the telemetry encoder moved outside the expected band within 40 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The telemetry encoder had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The chilldown ramp was revised and a leak check was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the telemetry encoder instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
