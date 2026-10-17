---
id: gse-ground-purge-dew-point-excursion-2024-08
domain: ground-systems
system: ols-tower-2
author: kknox
reviewed_by: shahar603
status: reviewed
severity: critical
created: 2024-08-10
tags: [ground, hotfire, line]
---

# Ground purge dew point excursion

## Context

The first integrated flight on ols-tower-2, while the detank line was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the detank line moved outside the expected band within 13 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The detank line had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The acceptance band was revised and a dimensional check was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the detank line instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
