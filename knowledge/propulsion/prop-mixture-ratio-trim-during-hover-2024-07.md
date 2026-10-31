---
id: prop-mixture-ratio-trim-during-hover-2024-07
domain: propulsion
system: raptor-3
author: jakewmeyer
reviewed_by: shahar603
status: reviewed
severity: critical
created: 2024-07-30
tags: [propulsion, turbopump, turnaround]
---

# Mixture ratio trim during hover

## Context

A static fire on raptor-3, while the turbopump was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the turbopump moved outside the expected band within 38 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The turbopump had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The inspection interval was revised and a pre-run visual was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the turbopump instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
