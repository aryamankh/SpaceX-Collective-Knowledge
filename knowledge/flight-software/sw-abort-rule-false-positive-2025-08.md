---
id: sw-abort-rule-false-positive-2025-08
domain: flight-software
system: flight-software-v7
author: aryamankha
reviewed_by: kknox
status: reviewed
severity: low
created: 2025-08-09
tags: [cryo, flight, tree]
---

# Abort rule false positive

## Context

The first integrated flight on flight-software-v7, while the fault tree was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the fault tree moved outside the expected band within 20 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The fault tree had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The sampling rate was revised and a functional test was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the fault tree instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
