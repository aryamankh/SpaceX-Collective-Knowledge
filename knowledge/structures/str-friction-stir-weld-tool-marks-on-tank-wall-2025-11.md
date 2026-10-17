---
id: str-friction-stir-weld-tool-marks-on-tank-wall-2025-11
domain: structures
system: starship-s38
author: mattythorne
reviewed_by: jhpratt
status: reviewed
severity: medium
created: 2025-11-24
tags: [pad, row, structures]
---

# Friction stir weld tool marks on tank wall

## Context

A night tanking on starship-s38, while the aft skirt fastener row was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the aft skirt fastener row moved outside the expected band within 24 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The aft skirt fastener row had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The torque spec was revised and an endoscope pass was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the aft skirt fastener row instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
