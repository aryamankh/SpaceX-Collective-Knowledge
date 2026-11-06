---
id: tps-emissivity-change-from-soot-2025-05
domain: thermal-protection
system: starship-heat-shield
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-05-02
tags: [manifold, reflight, thermal]
---

# Emissivity change from soot

## Context

A cryo proof on starship-heat-shield, while the purge manifold was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the purge manifold moved outside the expected band within 4 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The purge manifold had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The chilldown ramp was revised and a torque re-verification was added to the task list before the next run. Owner: emmedve1.

## What we would do differently

Stop on the first excursion of the purge manifold instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
