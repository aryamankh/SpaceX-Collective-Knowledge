---
id: ops-post-flight-downlink-priority-2026-09
domain: flight-ops
system: launch-complex-39a
author: CAM-Gerlach
reviewed_by: mattythorne
status: reviewed
severity: low
created: 2026-09-19
tags: [flight, hotfire, rota]
---

# Post-flight downlink priority

## Context

The first integrated flight on launch-complex-39a, while the triage rota was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the triage rota moved outside the expected band within 24 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The triage rota had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The purge dwell was revised and a dimensional check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the triage rota instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
