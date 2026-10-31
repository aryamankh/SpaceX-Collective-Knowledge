---
id: mat-seal-swell-in-methalox-2025-10
domain: materials
system: inconel-718
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-10-03
tags: [hotfire, lot, materials]
---

# Seal swell in methalox

## Context

A reflight turnaround on inconel-718, while the incoming plate lot was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the incoming plate lot moved outside the expected band within 12 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The incoming plate lot had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and a functional test was added to the task list before the next run. Owner: AlbericTrancart.

## What we would do differently

Stop on the first excursion of the incoming plate lot instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
