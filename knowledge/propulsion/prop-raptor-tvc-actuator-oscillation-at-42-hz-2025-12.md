---
id: prop-raptor-tvc-actuator-oscillation-at-42-hz-2025-12
domain: propulsion
system: raptor-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2025-12-07
tags: [propulsion, puck, turnaround]
---

# Raptor TVC actuator oscillation at 42 Hz

## Context

A night tanking on raptor-3, while the thrust puck was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the thrust puck moved outside the expected band within 25 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The thrust puck had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The acceptance band was revised and a leak check was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the thrust puck instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
