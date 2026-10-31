---
id: gse-ship-qd-plate-alignment-2025-03
domain: ground-systems
system: ols-tower-2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2025-03-07
tags: [cryo, ground, line]
---

# Ship QD plate alignment

## Context

The first integrated flight on ols-tower-2, while the detank line was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the detank line moved outside the expected band within 21 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The detank line had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The purge dwell was revised and an endoscope pass was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the detank line instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
