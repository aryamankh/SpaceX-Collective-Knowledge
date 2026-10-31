---
id: mat-cryogenic-seal-leak-rate-scatter-2025-01
domain: materials
system: inconel-718
author: AlbericTrancart
reviewed_by: jhpratt
status: reviewed
severity: medium
created: 2025-01-25
tags: [batch, hotfire, materials]
---

# Cryogenic seal leak rate scatter

## Context

A static fire on inconel-718, while the adhesive batch was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the adhesive batch moved outside the expected band within 13 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The adhesive batch had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: AlbericTrancart.

## What we would do differently

Stop on the first excursion of the adhesive batch instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
