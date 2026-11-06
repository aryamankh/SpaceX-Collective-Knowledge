---
id: str-weld-porosity-in-barrel-gore-seam-2026-09
domain: structures
system: starship-s38
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2026-09-18
tags: [frame, pad, structures]
---

# Weld porosity in barrel gore seam

## Context

A night tanking on starship-s38, while the ring frame was under watch by the console. The run was configured to the current published limits.

## What happened

Leak rate on the ring frame moved outside the expected band within 6 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The ring frame had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The inspection interval was revised and a functional test was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the ring frame instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
