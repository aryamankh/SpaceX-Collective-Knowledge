---
id: sw-telemetry-encoder-buffer-overrun-2026-06
domain: flight-software
system: flight-software-v7
author: aryamankha
reviewed_by: mattythorne
status: reviewed
severity: high
created: 2026-06-29
tags: [cryo, encoder, flight]
---

# Telemetry encoder buffer overrun

## Context

A static fire on flight-software-v7, while the telemetry encoder was under watch by the console. The run was configured to the current published limits.

## What happened

Frame timing on the telemetry encoder moved outside the expected band within 38 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The telemetry encoder had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the teardown report records it with photos.

## What we changed

The inspection interval was revised and a torque re-verification was added to the task list before the next run. Owner: aryamankha.

## What we would do differently

Stop on the first excursion of the telemetry encoder instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
