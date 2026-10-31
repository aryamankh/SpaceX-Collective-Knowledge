---
id: prop-hot-gas-manifold-leak-after-30-s-run-2024-11
domain: propulsion
system: raptor-3
author: jakewmeyer
reviewed_by: mattythorne
status: reviewed
severity: critical
created: 2024-11-07
tags: [pad, propulsion, transducer]
---

# Hot gas manifold leak after 30 s run

## Context

A cryo proof on raptor-3, while the chamber pressure transducer was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the chamber pressure transducer moved outside the expected band within 12 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The chamber pressure transducer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the chamber pressure transducer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
