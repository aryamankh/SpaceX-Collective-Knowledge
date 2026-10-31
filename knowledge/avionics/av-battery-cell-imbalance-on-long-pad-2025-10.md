---
id: av-battery-cell-imbalance-on-long-pad-2025-10
domain: avionics
system: flight-computer-b2
author: collierrgbsitisfise
reviewed_by: kknox
status: reviewed
severity: medium
created: 2025-10-02
tags: [avionics, pad, transmitter]
---

# Battery cell imbalance on long pad

## Context

A cryo proof on flight-computer-b2, while the S-band transmitter was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the S-band transmitter moved outside the expected band within 15 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The s-band transmitter had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The sampling rate was revised and a functional test was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the S-band transmitter instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The run log, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
