---
id: saf-lox-spill-response-drill-2024-09
domain: safety
system: pad-operations
author: shahar603
reviewed_by: jhpratt
status: reviewed
severity: medium
created: 2024-09-11
tags: [cryo, lighting, safety]
---

# LOX spill response drill

## Context

A static fire on pad-operations, while the egress lighting was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the egress lighting moved outside the expected band within 18 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The egress lighting had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: shahar603.

## What we would do differently

Stop on the first excursion of the egress lighting instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
