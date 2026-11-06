---
id: gse-gse-hose-whip-on-disconnect-2026-08
domain: ground-systems
system: ols-tower-2
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: low
created: 2026-08-25
tags: [disconnect, ground, pad]
---

# GSE hose whip on disconnect

## Context

The first integrated flight on ols-tower-2, while the quick disconnect was under watch by the console. The run was configured to the current published limits.

## What happened

Valve position on the quick disconnect moved outside the expected band within 35 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The quick disconnect had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the inspection photo set records it with photos.

## What we changed

The acceptance band was revised and a torque re-verification was added to the task list before the next run. Owner: kknox.

## What we would do differently

Stop on the first excursion of the quick disconnect instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
