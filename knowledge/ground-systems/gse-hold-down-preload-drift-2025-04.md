---
id: gse-hold-down-preload-drift-2025-04
domain: ground-systems
system: ols-tower-2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2025-04-21
tags: [clamp, ground, pad]
---

# Hold-down preload drift

## Context

A wet dress rehearsal on ols-tower-2, while the hold-down clamp was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the hold-down clamp moved outside the expected band within 21 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The hold-down clamp had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The sampling rate was revised and a leak check was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the hold-down clamp instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
