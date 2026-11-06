---
id: saf-confined-space-entry-on-tank-2024-11
domain: safety
system: pad-operations
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2024-11-13
tags: [drill, hotfire, safety]
---

# Confined space entry on tank

## Context

A night tanking on pad-operations, while the spill drill was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the spill drill moved outside the expected band within 40 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The spill drill had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The purge dwell was revised and a torque re-verification was added to the task list before the next run. Owner: shahar603.

## What we would do differently

Stop on the first excursion of the spill drill instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
