---
id: tps-aft-flap-seal-char-through-2025-01
domain: thermal-protection
system: starship-heat-shield
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2025-01-21
tags: [seal, thermal, turnaround]
---

# Aft flap seal char-through

## Context

A cryo proof on starship-heat-shield, while the flap seal was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the flap seal moved outside the expected band within 35 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The flap seal had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The purge dwell was revised and a torque re-verification was added to the task list before the next run. Owner: emmedve1.

## What we would do differently

Stop on the first excursion of the flap seal instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
