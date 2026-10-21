---
id: prop-lox-dome-priming-waterhammer-2025-08
domain: propulsion
system: raptor-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2025-08-12
tags: [actuator, hotfire, propulsion]
---

# LOX dome priming waterhammer

## Context

A cryo proof on raptor-3, while the TVC actuator was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the TVC actuator moved outside the expected band within 38 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The tvc actuator had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the TVC actuator instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
