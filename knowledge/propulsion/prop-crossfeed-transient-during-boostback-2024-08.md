---
id: prop-crossfeed-transient-during-boostback-2024-08
domain: propulsion
system: raptor-3
author: jakewmeyer
reviewed_by: CAM-Gerlach
status: reviewed
severity: high
created: 2024-08-22
tags: [cryo, propulsion, puck]
---

# Crossfeed transient during boostback

## Context

A reflight turnaround on raptor-3, while the thrust puck was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the thrust puck moved outside the expected band within 31 s. The run was cut short. No hardware was lost beyond the item already suspect.

## Root cause

The thrust puck had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the telemetry slice records it with photos.

## What we changed

The torque spec was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the thrust puck instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
