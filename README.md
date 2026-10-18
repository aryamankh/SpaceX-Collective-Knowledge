<p align="center"><img src="https://live.staticflickr.com/65535/49185149122_37f5c52e43_k.jpg" alt="Starship on the pad"></p>

<h1 align="center">SpaceX Collective Knowledge Base</h1>

<h3 align="center">
One repository, every team, everything we had to learn the hard way.
</h3>

<p align="center">
<a href="https://github.com/marsoperator/SpaceX-Collective-Knowledge-Base2/actions/workflows/knowledge.yml"><img src="https://img.shields.io/github/actions/workflow/status/marsoperator/SpaceX-Collective-Knowledge-Base2/knowledge.yml?style=flat-square&label=corpus"></a>
<a href="https://github.com/marsoperator/SpaceX-Collective-Knowledge-Base2/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue.svg?style=flat-square"></a>
<a href="https://go.dev"><img src="https://img.shields.io/badge/go-1.18+-00ADD8.svg?style=flat-square&logo=go&logoColor=white"></a>
<a href="knowledge/SCHEMA.md"><img src="https://img.shields.io/badge/notes-132-blueviolet.svg?style=flat-square"></a>
</p>

<h4 align="center">
  <i>
    The company-wide engineering corpus. Personal notes, failure write-ups, process tips, design gotchas and ops tricks — written by the person who lived it, reviewed by the owning team, ingested by Grokbot.
  </i>
</h4>

<h3 align="center">
<a href="knowledge/SCHEMA.md">Schema</a> - <a href="knowledge/index.json">Corpus Index</a> - <a href=".github/CODEOWNERS">Owners</a> - <a href="CONTRIBUTING.md">Contributing</a>
<br/>
</h3>

## Overview

The expensive lessons were already being learned. They just were not being kept. A note that lives in a chat thread is gone in a week; a note that lives here is read by the next engineer, by the reviewer, and by Grokbot when someone asks a question at 02:00 before a tanking operation.

The rule is simple: if you had to figure it out, write it down.

## What belongs here

| ✅ Belongs | ❌ Does not |
|---|---|
| Failure write-ups with a root cause and an owner | Drawings (link the document id) |
| Design gotchas that cost you a day | Meeting minutes |
| Ops tricks that are not in any runbook | Org charts |
| Inspection and acceptance findings worth generalizing | Anything that belongs in a ticket |
| Process notes: what the checklist should have said | Vendor marketing |
| Corrections to a note that turned out to be wrong | Duplicates of the same lesson |

## Structure

~~~
knowledge/
├── propulsion/           engines, turbomachinery, ignition, TVC
├── structures/           tanks, barrels, frames, joints, COPVs
├── avionics/             harness, computers, buses, sensors, power
├── gnc/                  guidance, navigation, control, aero surfaces
├── thermal-protection/   tiles, seals, blankets, purge, closeout
├── ground-systems/       pad, GSE, tanking, quick disconnects
├── manufacturing/        tooling, welding, fit-up, traceability
├── materials/            alloys, seals, coatings, lots, certs
├── flight-software/      sequencers, timing, faults, config
├── flight-ops/           countdown, range, recovery, triage
├── safety/               hazard analysis, LOTO, exclusion zones
├── SCHEMA.md             format contract
└── index.json            generated, never hand-edited
~~~

## Anatomy of a note

Front-matter, then the story, then the evidence. Every field is machine-checked.

~~~yaml
---
id: prop-raptor-tvc-oscillation-2026-04
domain: propulsion
system: raptor-3
author: jakewmeyer
reviewed_by: CAM-Gerlach
status: reviewed
severity: high
created: 2026-04-18
tags: [tvc, oscillation, damping]
---
~~~

Then `## Context`, `## What happened`, `## Root cause`, `## What we changed`, `## What we would do differently`, `## Evidence`. Numbers over adjectives: frequencies, pressures, torques, durations.

## Workflow

~~~mermaid
flowchart LR
    A[draft note] --> B[owning team review]
    B --> C[independent reviewer]
    C --> D[reviewed on main]
    D --> E[Grokbot corpus]
~~~

`CODEOWNERS` routes every domain to its owning team. A note lands as `draft`, gets reviewed by someone from another team, and merges as `reviewed`. The reviewer stays in the front-matter — if the note is wrong later, we know who to ask. Leadership signs off on the ones that change how we build.

## Ingestion

~~~bash
./manage.sh ingest-kb
~~~

Validates every note, then writes `dist/corpus.jsonl` — one record per note, stable field order, content hash — and regenerates `knowledge/index.json`. CI fails on any schema violation, so `main` is always ingestible and Grokbot never reads a broken corpus.

## Running locally

~~~bash
./manage.sh serve-backend     # API on :3041
./manage.sh serve-frontend    # UI on :3040
./manage.sh build-all         # full build, docs included
~~~

Requires Go 1.18+, Node 16+, and Hugo for the docs build.

## Provenance

The application shell — HTTP session handling, storage abstraction, Gist integration, routing and the cookie UI — is derived from [Prestige](https://github.com/sharat87/prestige) by Shrikant Sharat Kandula, Apache-2.0. The corpus, its schema, the ingestion pipeline, the domain layout and the knowledge-base framing are ours. Attribution is kept in [NOTICE](NOTICE).

## Ownership

Domain owners are in `CODEOWNERS`. The corpus is maintained by everyone who writes into it; the format is maintained by the ingestion owners. If a note is wrong, fix it in place and say what changed — do not open a ticket about it.

## License

Apache-2.0. Notes are internal by default; no controlled drawings inline.

<p align="center">
  <i>An independent project, not affiliated with or endorsed by Space Exploration Technologies Corp.</i>
</p>
