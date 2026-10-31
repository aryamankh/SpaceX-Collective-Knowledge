---
id: str-copv-overwrap-delamination-2026-03
domain: structures
system: starship-s38
author: mattythorne
reviewed_by: CAM-Gerlach
status: reviewed
severity: high
created: 2026-03-23
tags: [frame, structures, turnaround]
---

# COPV overwrap delamination

## Context

A cryo proof on starship-s38, while the ring frame was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the ring frame moved outside the expected band within 18 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The ring frame had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The inspection interval was revised and a functional test was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the ring frame instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
