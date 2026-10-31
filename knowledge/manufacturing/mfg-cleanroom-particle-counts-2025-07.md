---
id: mfg-cleanroom-particle-counts-2025-07
domain: manufacturing
system: high-bay-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2025-07-09
tags: [manufacturing, set, turnaround]
---

# Cleanroom particle counts

## Context

A wet dress rehearsal on high-bay-3, while the weld parameter set was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the weld parameter set moved outside the expected band within 8 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The weld parameter set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The inspection interval was revised and a pre-run visual was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the weld parameter set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
