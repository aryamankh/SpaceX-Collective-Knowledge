---
id: mat-primer-adhesion-on-pickled-steel-2024-06
domain: materials
system: inconel-718
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2024-06-23
tags: [lot, materials, pad]
---

# Primer adhesion on pickled steel

## Context

A night tanking on inconel-718, while the fastener lot was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the fastener lot moved outside the expected band within 18 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The fastener lot had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The inspection interval was revised and a torque re-verification was added to the task list before the next run. Owner: AlbericTrancart.

## What we would do differently

Stop on the first excursion of the fastener lot instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
