---
id: saf-forklift-pedestrian-separation-2026-08
domain: safety
system: pad-operations
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2026-08-01
tags: [pad, safety, zone]
---

# Forklift pedestrian separation

## Context

A night tanking on pad-operations, while the exclusion zone was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the exclusion zone moved outside the expected band within 17 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The exclusion zone had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The purge dwell was revised and a leak check was added to the task list before the next run. Owner: shahar603.

## What we would do differently

Stop on the first excursion of the exclusion zone instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
