---
id: sw-control-loop-timing-jitter-2026-02
domain: flight-software
system: flight-software-v7
author: aryamankha
reviewed_by: kknox
status: reviewed
severity: critical
created: 2026-02-26
tags: [flight, sequencer, turnaround]
---

# Control loop timing jitter

## Context

A cryo proof on flight-software-v7, while the mode sequencer was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the mode sequencer moved outside the expected band within 13 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The mode sequencer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The sampling rate was revised and an endoscope pass was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the mode sequencer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
