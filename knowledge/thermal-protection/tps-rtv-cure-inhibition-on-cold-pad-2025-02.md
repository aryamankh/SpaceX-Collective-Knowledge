---
id: tps-rtv-cure-inhibition-on-cold-pad-2025-02
domain: thermal-protection
system: starship-heat-shield
author: emmedve1
reviewed_by: shahar603
status: reviewed
severity: high
created: 2025-02-03
tags: [sample, thermal, turnaround]
---

# RTV cure inhibition on cold pad

## Context

A night tanking on starship-heat-shield, while the shear sample was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the shear sample moved outside the expected band within 2 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The shear sample had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The purge dwell was revised and a pre-run visual was added to the task list before the next run. Owner: emmedve1.

## What we would do differently

Stop on the first excursion of the shear sample instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
