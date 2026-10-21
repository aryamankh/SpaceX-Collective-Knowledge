---
id: mat-brazing-flux-residue-corrosion-2024-12
domain: materials
system: inconel-718
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-12-01
tags: [materials, turnaround, wall]
---

# Brazing flux residue corrosion

## Context

A reflight turnaround on inconel-718, while the liner wall was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the liner wall moved outside the expected band within 14 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The liner wall had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The purge dwell was revised and a functional test was added to the task list before the next run. Owner: AlbericTrancart.

## What we would do differently

Stop on the first excursion of the liner wall instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
