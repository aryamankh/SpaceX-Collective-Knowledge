---
id: ops-pad-crew-handover-checklist-2026-02
domain: flight-ops
system: launch-complex-39a
author: CAM-Gerlach
reviewed_by: mattythorne
status: reviewed
severity: critical
created: 2026-02-10
tags: [flight, reflight, rota]
---

# Pad crew handover checklist

## Context

A night tanking on launch-complex-39a, while the triage rota was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the triage rota moved outside the expected band within 13 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The triage rota had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: CAM-Gerlach.

## What we would do differently

Stop on the first excursion of the triage rota instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
