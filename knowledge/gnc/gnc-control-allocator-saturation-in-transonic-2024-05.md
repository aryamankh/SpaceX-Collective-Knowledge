---
id: gnc-control-allocator-saturation-in-transonic-2024-05
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-05-26
tags: [gnc, hotfire, scheduler]
---

# Control allocator saturation in transonic

## Context

A cryo proof on booster-b19, while the flap scheduler was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the flap scheduler moved outside the expected band within 39 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The flap scheduler had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The chilldown ramp was revised and a leak check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the flap scheduler instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
