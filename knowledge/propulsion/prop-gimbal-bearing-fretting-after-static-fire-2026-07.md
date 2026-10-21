---
id: prop-gimbal-bearing-fretting-after-static-fire-2026-07
domain: propulsion
system: raptor-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2026-07-28
tags: [hotfire, propulsion, turbopump]
---

# Gimbal bearing fretting after static fire

## Context

A night tanking on raptor-3, while the turbopump was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the turbopump moved outside the expected band within 39 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The turbopump had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The chilldown ramp was revised and a pre-run visual was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the turbopump instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
