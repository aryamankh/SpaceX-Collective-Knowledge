---
id: tps-thermal-soak-through-raceway-penetration-2025-03
domain: thermal-protection
system: starship-heat-shield
author: emmedve1
reviewed_by: mattythorne
status: reviewed
severity: high
created: 2025-03-07
tags: [hotfire, manifold, thermal]
---

# Thermal soak through raceway penetration

## Context

A reflight turnaround on starship-heat-shield, while the purge manifold was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the purge manifold moved outside the expected band within 8 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The purge manifold had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The inspection interval was revised and a functional test was added to the task list before the next run. Owner: emmedve1.

## What we would do differently

Stop on the first excursion of the purge manifold instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
