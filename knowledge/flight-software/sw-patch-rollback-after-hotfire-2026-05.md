---
id: sw-patch-rollback-after-hotfire-2026-05
domain: flight-software
system: flight-software-v7
author: aryamankha
reviewed_by: jhpratt
status: reviewed
severity: high
created: 2026-05-23
tags: [flight, hotfire, rule]
---

# Patch rollback after hotfire

## Context

A night tanking on flight-software-v7, while the abort rule was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the abort rule moved outside the expected band within 4 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The abort rule had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The purge dwell was revised and a leak check was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the abort rule instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
