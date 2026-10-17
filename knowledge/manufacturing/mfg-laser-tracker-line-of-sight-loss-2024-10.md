---
id: mfg-laser-tracker-line-of-sight-loss-2024-10
domain: manufacturing
system: high-bay-3
author: AstralZebulon
reviewed_by: kknox
status: reviewed
severity: high
created: 2024-10-25
tags: [hotfire, manufacturing, tracker]
---

# Laser tracker line-of-sight loss

## Context

A cryo proof on high-bay-3, while the laser tracker was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the laser tracker moved outside the expected band within 22 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The laser tracker had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The acceptance band was revised and a dimensional check was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the laser tracker instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
