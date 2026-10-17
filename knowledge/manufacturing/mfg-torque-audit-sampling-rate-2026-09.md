---
id: mfg-torque-audit-sampling-rate-2026-09
domain: manufacturing
system: high-bay-3
author: AstralZebulon
reviewed_by: CAM-Gerlach
status: reviewed
severity: low
created: 2026-09-24
tags: [cryo, manufacturing, set]
---

# Torque audit sampling rate

## Context

The first integrated flight on high-bay-3, while the weld parameter set was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the weld parameter set moved outside the expected band within 17 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The weld parameter set had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The purge dwell was revised and a pre-run visual was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the weld parameter set instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
