---
id: tps-purge-flow-loss-in-tile-cavity-2025-01
domain: thermal-protection
system: starship-heat-shield
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2025-01-07
tags: [sample, thermal, turnaround]
---

# Purge flow loss in tile cavity

## Context

A reflight turnaround on starship-heat-shield, while the shear sample was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the shear sample moved outside the expected band within 35 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The shear sample had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The acceptance band was revised and a pre-run visual was added to the task list before the next run. Owner: emmedve1.

## What we would do differently

Stop on the first excursion of the shear sample instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
