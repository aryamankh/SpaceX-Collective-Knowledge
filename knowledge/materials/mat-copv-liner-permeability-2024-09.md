---
id: mat-copv-liner-permeability-2024-09
domain: materials
system: inconel-718
author: AlbericTrancart
reviewed_by: kknox
status: reviewed
severity: critical
created: 2024-09-27
tags: [lot, materials, pad]
---

# COPV liner permeability

## Context

A static fire on inconel-718, while the incoming plate lot was under watch by the console. The run was configured to the current published limits.

## What happened

Pressure on the incoming plate lot moved outside the expected band within 12 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The incoming plate lot had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: AlbericTrancart.

## What we would do differently

Stop on the first excursion of the incoming plate lot instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
