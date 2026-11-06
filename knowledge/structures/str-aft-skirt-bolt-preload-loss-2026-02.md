---
id: str-aft-skirt-bolt-preload-loss-2026-02
domain: structures
system: starship-s38
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: critical
created: 2026-02-06
tags: [reflight, row, structures]
---

# Aft skirt bolt preload loss

## Context

A cryo proof on starship-s38, while the aft skirt fastener row was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the aft skirt fastener row moved outside the expected band within 40 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The aft skirt fastener row had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The inspection interval was revised and a leak check was added to the task list before the next run. Owner: mattythorne.

## What we would do differently

Stop on the first excursion of the aft skirt fastener row instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
