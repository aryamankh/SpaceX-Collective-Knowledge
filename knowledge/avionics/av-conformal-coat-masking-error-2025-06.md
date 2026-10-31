---
id: av-conformal-coat-masking-error-2025-06
domain: avionics
system: flight-computer-b2
author: collierrgbsitisfise
reviewed_by: kknox
status: reviewed
severity: low
created: 2025-06-10
tags: [avionics, bundle, hotfire]
---

# Conformal coat masking error

## Context

The first integrated flight on flight-computer-b2, while the harness bundle was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the harness bundle moved outside the expected band within 6 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The harness bundle had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The sampling rate was revised and a pre-run visual was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the harness bundle instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
