---
id: prop-regen-channel-pressure-drop-drift-2026-07
domain: propulsion
system: raptor-3
author: jakewmeyer
reviewed_by: mattythorne
status: reviewed
severity: medium
created: 2026-07-16
tags: [bearing, hotfire, propulsion]
---

# Regen channel pressure drop drift

## Context

A static fire on raptor-3, while the gimbal bearing was under watch by the console. The run was configured to the current published limits.

## What happened

Vibration on the gimbal bearing moved outside the expected band within 19 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The gimbal bearing had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the NCR records it with photos.

## What we changed

The purge dwell was revised and a functional test was added to the task list before the next run. Owner: jakewmeyer.

## What we would do differently

Stop on the first excursion of the gimbal bearing instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The telemetry slice, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
