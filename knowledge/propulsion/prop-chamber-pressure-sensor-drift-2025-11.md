---
id: prop-chamber-pressure-sensor-drift-2025-11
domain: propulsion
system: raptor-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2025-11-14
tags: [propulsion, reflight, transducer]
---

# Chamber pressure sensor drift

## Context

A night tanking on raptor-3, while the chamber pressure transducer was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the chamber pressure transducer moved outside the expected band within 5 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The chamber pressure transducer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The inspection interval was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the chamber pressure transducer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
