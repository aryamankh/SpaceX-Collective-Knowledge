---
id: gse-flame-trench-pressure-transient-2024-12
domain: ground-systems
system: ols-tower-2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-12-22
tags: [ground, reflight, valve]
---

# Flame trench pressure transient

## Context

A wet dress rehearsal on ols-tower-2, while the deluge valve was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the deluge valve moved outside the expected band within 15 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The deluge valve had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the deluge valve instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
