---
id: mfg-paint-booth-humidity-control-2026-03
domain: manufacturing
system: high-bay-3
author: AstralZebulon
reviewed_by: kknox
status: reviewed
severity: high
created: 2026-03-13
tags: [datum, hotfire, manufacturing]
---

# Paint booth humidity control

## Context

A wet dress rehearsal on high-bay-3, while the tooling datum was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the tooling datum moved outside the expected band within 31 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The tooling datum had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The acceptance band was revised and a functional test was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the tooling datum instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
