---
id: prop-turbopump-chilldown-cavitation-on-restart-2025-03
domain: propulsion
system: raptor-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2025-03-30
tags: [propulsion, transducer, turnaround]
---

# Turbopump chilldown cavitation on restart

## Context

A cryo proof on raptor-3, while the chamber pressure transducer was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the chamber pressure transducer moved outside the expected band within 39 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The chamber pressure transducer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The inspection interval was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the chamber pressure transducer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
