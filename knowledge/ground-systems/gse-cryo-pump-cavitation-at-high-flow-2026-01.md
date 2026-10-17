---
id: gse-cryo-pump-cavitation-at-high-flow-2026-01
domain: ground-systems
system: ols-tower-2
author: kknox
reviewed_by: shahar603
status: reviewed
severity: medium
created: 2026-01-03
tags: [clamp, ground, pad]
---

# Cryo pump cavitation at high flow

## Context

A night tanking on ols-tower-2, while the hold-down clamp was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the hold-down clamp moved outside the expected band within 4 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The hold-down clamp had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The inspection interval was revised and a pre-run visual was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the hold-down clamp instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
