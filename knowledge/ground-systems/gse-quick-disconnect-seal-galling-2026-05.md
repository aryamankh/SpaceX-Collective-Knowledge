---
id: gse-quick-disconnect-seal-galling-2026-05
domain: ground-systems
system: ols-tower-2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2026-05-09
tags: [disconnect, ground, turnaround]
---

# Quick disconnect seal galling

## Context

A reflight turnaround on ols-tower-2, while the quick disconnect was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the quick disconnect moved outside the expected band within 22 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The quick disconnect had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The purge dwell was revised and a leak check was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the quick disconnect instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
