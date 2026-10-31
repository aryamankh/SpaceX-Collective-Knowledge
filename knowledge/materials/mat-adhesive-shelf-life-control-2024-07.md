---
id: mat-adhesive-shelf-life-control-2024-07
domain: materials
system: inconel-718
author: AlbericTrancart
reviewed_by: mattythorne
status: reviewed
severity: high
created: 2024-07-07
tags: [layer, materials, turnaround]
---

# Adhesive shelf life control

## Context

The first integrated flight on inconel-718, while the primer layer was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the primer layer moved outside the expected band within 4 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The primer layer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The sampling rate was revised and a leak check was added to the task list before the next run. Owner: AlbericTrancart.

## What we would do differently

Stop on the first excursion of the primer layer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
