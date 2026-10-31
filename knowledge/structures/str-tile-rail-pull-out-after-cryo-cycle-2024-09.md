---
id: str-tile-rail-pull-out-after-cryo-cycle-2024-09
domain: structures
system: starship-s38
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-09-08
tags: [pad, seam, structures]
---

# Tile rail pull-out after cryo cycle

## Context

A night tanking on starship-s38, while the gore seam was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the gore seam moved outside the expected band within 37 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The gore seam had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The torque spec was revised and a pre-run visual was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the gore seam instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
