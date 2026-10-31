---
id: av-redundant-lane-desync-at-boot-2026-06
domain: avionics
system: flight-computer-b2
author: collierrgbsitisfise
reviewed_by: CAM-Gerlach
status: reviewed
severity: medium
created: 2026-06-30
tags: [avionics, limiter, pad]
---

# Redundant lane desync at boot

## Context

A static fire on flight-computer-b2, while the inrush limiter was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the inrush limiter moved outside the expected band within 6 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The inrush limiter had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The purge dwell was revised and a leak check was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the inrush limiter instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
