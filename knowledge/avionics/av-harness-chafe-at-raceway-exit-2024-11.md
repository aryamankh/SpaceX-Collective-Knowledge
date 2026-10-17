---
id: av-harness-chafe-at-raceway-exit-2024-11
domain: avionics
system: flight-computer-b2
author: collierrgbsitisfise
reviewed_by: kknox
status: reviewed
severity: high
created: 2024-11-28
tags: [avionics, cryo, watchdog]
---

# Harness chafe at raceway exit

## Context

A night tanking on flight-computer-b2, while the watchdog was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the watchdog moved outside the expected band within 36 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The watchdog had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the watchdog instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
