---
id: av-can-bus-termination-fault-2026-10
domain: avionics
system: flight-computer-b2
author: collierrgbsitisfise
reviewed_by: CAM-Gerlach
status: reviewed
severity: critical
created: 2026-10-08
tags: [avionics, limiter, pad]
---

# CAN bus termination fault

## Context

A static fire on flight-computer-b2, while the inrush limiter was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the inrush limiter moved outside the expected band within 13 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The inrush limiter had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The purge dwell was revised and an endoscope pass was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the inrush limiter instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
