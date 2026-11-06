---
id: av-power-bus-inrush-trip-2026-06
domain: avionics
system: flight-computer-b2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2026-06-20
tags: [avionics, cryo, limiter]
---

# Power bus inrush trip

## Context

A reflight turnaround on flight-computer-b2, while the inrush limiter was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the inrush limiter moved outside the expected band within 25 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The inrush limiter had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The purge dwell was revised and a dimensional check was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the inrush limiter instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
