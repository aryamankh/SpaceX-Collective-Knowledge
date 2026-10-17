---
id: gse-methane-detector-false-positive-2025-01
domain: ground-systems
system: ols-tower-2
author: kknox
reviewed_by: mattythorne
status: reviewed
severity: low
created: 2025-01-11
tags: [ground, pad, valve]
---

# Methane detector false positive

## Context

A static fire on ols-tower-2, while the deluge valve was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the deluge valve moved outside the expected band within 23 s. The run was aborted by the operator. No hardware was lost beyond the item already suspect.

## Root cause

The deluge valve had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The inspection interval was revised and an endoscope pass was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the deluge valve instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The teardown report, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
