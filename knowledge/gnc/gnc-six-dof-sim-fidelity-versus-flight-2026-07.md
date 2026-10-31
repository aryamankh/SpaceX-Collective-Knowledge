---
id: gnc-six-dof-sim-fidelity-versus-flight-2026-07
domain: gnc
system: booster-b19
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: medium
created: 2026-07-02
tags: [gnc, pad, quantizer]
---

# Six-DOF sim fidelity versus flight

## Context

A night tanking on booster-b19, while the throttle quantizer was under watch by the console. The run was configured to the current published limits.

## What happened

Temperature on the throttle quantizer moved outside the expected band within 14 s. The run was run to completion with a note. No hardware was lost beyond the item already suspect.

## Root cause

The throttle quantizer had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the the torque audit sheet records it with photos.

## What we changed

The sampling rate was revised and a leak check was added to the task list before the next run. Owner: richiksc.

## What we would do differently

Stop on the first excursion of the throttle quantizer instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

The ncr, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
