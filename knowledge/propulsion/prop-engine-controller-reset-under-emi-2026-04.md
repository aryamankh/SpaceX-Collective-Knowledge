---
id: prop-engine-controller-reset-under-emi-2026-04
domain: propulsion
system: raptor-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-04-07
tags: [hotfire, propulsion, turbopump]
---

# Engine controller reset under EMI

## Context

A wet dress rehearsal on raptor-3, while the turbopump was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the turbopump moved outside the expected band within 6 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The turbopump had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The torque spec was revised and a pre-run visual was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the turbopump instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
