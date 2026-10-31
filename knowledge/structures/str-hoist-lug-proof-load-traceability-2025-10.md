---
id: str-hoist-lug-proof-load-traceability-2025-10
domain: structures
system: starship-s38
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2025-10-22
tags: [reflight, row, structures]
---

# Hoist lug proof load traceability

## Context

The first integrated flight on starship-s38, while the aft skirt fastener row was under watch by the console. The run was configured to the current published limits.

## What happened

Pressure on the aft skirt fastener row moved outside the expected band within 8 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The aft skirt fastener row had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The acceptance band was revised and an endoscope pass was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the aft skirt fastener row instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
