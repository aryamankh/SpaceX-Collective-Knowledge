---
id: sw-mode-transition-race-in-sequencer-2026-07
domain: flight-software
system: flight-software-v7
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-07-08
tags: [flight, pad, sequencer]
---

# Mode transition race in sequencer

## Context

A wet dress rehearsal on flight-software-v7, while the mode sequencer was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the mode sequencer moved outside the expected band within 21 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The mode sequencer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the mode sequencer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
