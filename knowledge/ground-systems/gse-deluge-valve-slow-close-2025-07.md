---
id: gse-deluge-valve-slow-close-2025-07
domain: ground-systems
system: ols-tower-2
author: kknox
reviewed_by: jhpratt
status: reviewed
severity: medium
created: 2025-07-26
tags: [ground, pump, turnaround]
---

# Deluge valve slow close

## Context

The first integrated flight on ols-tower-2, while the cryo pump was under watch by the console. The run was configured to the current published limits.

## What happened

Pressure on the cryo pump moved outside the expected band within 5 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The cryo pump had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and a torque re-verification was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the cryo pump instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
