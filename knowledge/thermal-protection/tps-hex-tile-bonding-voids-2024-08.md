---
id: tps-hex-tile-bonding-voids-2024-08
domain: thermal-protection
system: starship-heat-shield
author: emmedve1
reviewed_by: shahar603
status: reviewed
severity: medium
created: 2024-08-30
tags: [hotfire, manifold, thermal]
---

# Hex tile bonding voids

## Context

A static fire on starship-heat-shield, while the purge manifold was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the purge manifold moved outside the expected band within 11 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The purge manifold had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The purge dwell was revised and a functional test was added to the task list before the next run. Owner: emmedve1.

## What we would do differently

Stop on the first excursion of the purge manifold instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
