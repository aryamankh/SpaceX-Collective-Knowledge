---
id: tps-tile-density-lot-variation-2026-01
domain: thermal-protection
system: starship-heat-shield
author: emmedve1
reviewed_by: shahar603
status: reviewed
severity: medium
created: 2026-01-07
tags: [pad, seal, thermal]
---

# Tile density lot variation

## Context

A wet dress rehearsal on starship-heat-shield, while the flap seal was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the flap seal moved outside the expected band within 28 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The flap seal had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The chilldown ramp was revised and a torque re-verification was added to the task list before the next run. Owner: emmedve1.

## What we would do differently

Stop on the first excursion of the flap seal instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
