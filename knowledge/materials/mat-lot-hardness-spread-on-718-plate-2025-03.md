---
id: mat-lot-hardness-spread-on-718-plate-2025-03
domain: materials
system: inconel-718
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-03-27
tags: [materials, reflight, seal]
---

# Lot hardness spread on 718 plate

## Context

A night tanking on inconel-718, while the face seal was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the face seal moved outside the expected band within 40 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The face seal had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: AlbericTrancart.

## What we would do differently

Stop on the first excursion of the face seal instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
