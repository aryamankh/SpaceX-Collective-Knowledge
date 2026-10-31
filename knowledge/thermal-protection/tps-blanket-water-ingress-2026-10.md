---
id: tps-blanket-water-ingress-2026-10
domain: thermal-protection
system: starship-heat-shield
author: emmedve1
reviewed_by: kknox
status: reviewed
severity: high
created: 2026-10-05
tags: [reflight, seal, thermal]
---

# Blanket water ingress

## Context

A cryo proof on starship-heat-shield, while the flap seal was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the flap seal moved outside the expected band within 28 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The flap seal had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: emmedve1.

## What we would do differently

Stop on the first excursion of the flap seal instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
