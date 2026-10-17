---
id: av-connector-keying-mismatch-on-test-rack-2025-02
domain: avionics
system: flight-computer-b2
author: collierrgbsitisfise
reviewed_by: shahar603
status: reviewed
severity: medium
created: 2025-02-01
tags: [avionics, bundle, hotfire]
---

# Connector keying mismatch on test rack

## Context

The first integrated flight on flight-computer-b2, while the harness bundle was under watch by the console. The run was configured to the current published limits.

## What happened

Strain on the harness bundle moved outside the expected band within 23 s. The run was paused for inspection. No hardware was lost beyond the item already suspect.

## Root cause

The harness bundle had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the run log records it with photos.

## What we changed

The chilldown ramp was revised and a dimensional check was added to the task list before the next run. Owner: collierrgbsitisfise.

## What we would do differently

Stop on the first excursion of the harness bundle instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
