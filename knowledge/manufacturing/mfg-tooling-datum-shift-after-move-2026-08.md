---
id: mfg-tooling-datum-shift-after-move-2026-08
domain: manufacturing
system: high-bay-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-08-14
tags: [manufacturing, pad, tracker]
---

# Tooling datum shift after move

## Context

A static fire on high-bay-3, while the laser tracker was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the laser tracker moved outside the expected band within 31 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The laser tracker had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The torque spec was revised and a leak check was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the laser tracker instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The torque audit sheet, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
