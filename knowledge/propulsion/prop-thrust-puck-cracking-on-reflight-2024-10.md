---
id: prop-thrust-puck-cracking-on-reflight-2024-10
domain: propulsion
system: raptor-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-10-25
tags: [hotfire, propulsion, turbopump]
---

# Thrust puck cracking on reflight

## Context

A static fire on raptor-3, while the turbopump was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the turbopump moved outside the expected band within 26 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The turbopump had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The purge dwell was revised and an endoscope pass was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the turbopump instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
