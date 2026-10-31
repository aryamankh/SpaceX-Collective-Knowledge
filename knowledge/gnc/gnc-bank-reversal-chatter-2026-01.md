---
id: gnc-bank-reversal-chatter-2026-01
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-01-12
tags: [cryo, gnc, schedule]
---

# Bank reversal chatter

## Context

A night tanking on booster-b19, while the grid fin schedule was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the grid fin schedule moved outside the expected band within 20 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The grid fin schedule had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The sampling rate was revised and a functional test was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the grid fin schedule instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
