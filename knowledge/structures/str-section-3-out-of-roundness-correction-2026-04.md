---
id: str-section-3-out-of-roundness-correction-2026-04
domain: structures
system: starship-s38
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2026-04-24
tags: [reflight, row, structures]
---

# Section 3 out-of-roundness correction

## Context

The first integrated flight on starship-s38, while the aft skirt fastener row was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the aft skirt fastener row moved outside the expected band within 24 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The aft skirt fastener row had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The acceptance band was revised and a pre-run visual was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the aft skirt fastener row instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
