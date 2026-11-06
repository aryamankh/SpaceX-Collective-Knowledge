---
id: mfg-fastener-hole-positional-tolerance-2026-02
domain: manufacturing
system: high-bay-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2026-02-06
tags: [cryo, fixture, manufacturing]
---

# Fastener hole positional tolerance

## Context

A reflight turnaround on high-bay-3, while the fit-up fixture was under watch by the console. The run was configured to the current published limits.

## What happened

Current draw on the fit-up fixture moved outside the expected band within 34 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The fit-up fixture had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The chilldown ramp was revised and a pre-run visual was added to the task list before the next run. Owner: AstralZebulon.

## What we would do differently

Stop on the first excursion of the fit-up fixture instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
