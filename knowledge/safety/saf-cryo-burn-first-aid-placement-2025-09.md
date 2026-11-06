---
id: saf-cryo-burn-first-aid-placement-2025-09
domain: safety
system: pad-operations
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-09-14
tags: [reflight, review, safety]
---

# Cryo burn first aid placement

## Context

A cryo proof on pad-operations, while the closeout review was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the closeout review moved outside the expected band within 4 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The closeout review had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The sampling rate was revised and a functional test was added to the task list before the next run. Owner: shahar603.

## What we would do differently

Stop on the first excursion of the closeout review instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
