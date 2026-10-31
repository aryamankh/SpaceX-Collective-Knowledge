---
id: str-flap-hinge-lug-fatigue-2024-08
domain: structures
system: starship-s38
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2024-08-21
tags: [frame, hotfire, structures]
---

# Flap hinge lug fatigue

## Context

A wet dress rehearsal on starship-s38, while the ring frame was under watch by the console. The run was configured to the current published limits.

## What happened

Pressure on the ring frame moved outside the expected band within 28 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The ring frame had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The torque spec was revised and a dimensional check was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the ring frame instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
