---
id: mat-fastener-hydrogen-embrittlement-2024-07
domain: materials
system: inconel-718
author: AlbericTrancart
reviewed_by: CAM-Gerlach
status: reviewed
severity: high
created: 2024-07-14
tags: [cryo, lot, materials]
---

# Fastener hydrogen embrittlement

## Context

A cryo proof on inconel-718, while the fastener lot was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the fastener lot moved outside the expected band within 37 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The fastener lot had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The chilldown ramp was revised and a functional test was added to the task list before the next run. Owner: AlbericTrancart.

## What we would do differently

Stop on the first excursion of the fastener lot instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
