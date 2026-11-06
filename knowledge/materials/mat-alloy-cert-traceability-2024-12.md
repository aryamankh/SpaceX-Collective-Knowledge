---
id: mat-alloy-cert-traceability-2024-12
domain: materials
system: inconel-718
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2024-12-03
tags: [batch, materials, reflight]
---

# Alloy cert traceability

## Context

A cryo proof on inconel-718, while the adhesive batch was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the adhesive batch moved outside the expected band within 32 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The adhesive batch had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The torque spec was revised and a leak check was added to the task list before the next run. Owner: AlbericTrancart.

## What we would do differently

Stop on the first excursion of the adhesive batch instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
