---
id: str-cryo-shock-crack-at-doubler-edge-2025-10
domain: structures
system: starship-s38
author: mattythorne
reviewed_by: kknox
status: reviewed
severity: medium
created: 2025-10-04
tags: [cryo, lug, structures]
---

# Cryo-shock crack at doubler edge

## Context

A static fire on starship-s38, while the hinge lug was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the hinge lug moved outside the expected band within 36 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The hinge lug had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The chilldown ramp was revised and an endoscope pass was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the hinge lug instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The inspection photo set, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
