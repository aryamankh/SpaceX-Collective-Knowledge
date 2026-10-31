---
id: ops-crew-rest-versus-window-trade-2025-03
domain: flight-ops
system: launch-complex-39a
author: CAM-Gerlach
reviewed_by: jhpratt
status: reviewed
severity: high
created: 2025-03-08
tags: [flight, pad, set]
---

# Crew rest versus window trade

## Context

The first integrated flight on launch-complex-39a, while the weather rule set was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the weather rule set moved outside the expected band within 6 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The weather rule set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The inspection interval was revised and a leak check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the weather rule set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
