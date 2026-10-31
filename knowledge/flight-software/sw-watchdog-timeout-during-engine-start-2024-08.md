---
id: sw-watchdog-timeout-during-engine-start-2024-08
domain: flight-software
system: flight-software-v7
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2024-08-10
tags: [flight, hotfire, timer]
---

# Watchdog timeout during engine start

## Context

The first integrated flight on flight-software-v7, while the watchdog timer was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the watchdog timer moved outside the expected band within 21 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The watchdog timer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the watchdog timer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
