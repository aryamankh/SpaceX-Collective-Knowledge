---
id: ops-tanking-sequence-conflict-2026-10
domain: flight-ops
system: launch-complex-39a
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-10-06
tags: [checklist, flight, hotfire]
---

# Tanking sequence conflict

## Context

A reflight turnaround on launch-complex-39a, while the handover checklist was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the handover checklist moved outside the expected band within 17 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The handover checklist had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The sampling rate was revised and a dimensional check was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the handover checklist instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
