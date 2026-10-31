---
id: gse-booster-transport-saddle-load-2025-06
domain: ground-systems
system: ols-tower-2
author: kknox
reviewed_by: mattythorne
status: reviewed
severity: high
created: 2025-06-03
tags: [clamp, cryo, ground]
---

# Booster transport saddle load

## Context

The first integrated flight on ols-tower-2, while the hold-down clamp was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the hold-down clamp moved outside the expected band within 36 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The hold-down clamp had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The purge dwell was revised and a dimensional check was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the hold-down clamp instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
