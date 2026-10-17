---
id: str-peel-ply-residue-before-primer-2026-08
domain: structures
system: starship-s38
author: mattythorne
reviewed_by: CAM-Gerlach
status: reviewed
severity: high
created: 2026-08-11
tags: [lug, reflight, structures]
---

# Peel ply residue before primer

## Context

A wet dress rehearsal on starship-s38, while the hinge lug was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the hinge lug moved outside the expected band within 16 s. The run was held at T-4 s. No hardware was lost beyond the item already suspect.

## Root cause

The hinge lug had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The sampling rate was revised and a torque re-verification was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the hinge lug instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
