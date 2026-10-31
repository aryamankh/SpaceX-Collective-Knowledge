<div align="center">

<img src="https://i.imgur.com/yULmKup.png" alt="SpaceX Collective Knowledge Base" width="100%">

# SpaceX Collective Knowledge Base

[![corpus](https://img.shields.io/badge/corpus-132%20notes-000000?style=flat-square)](knowledge/)
[![domains](https://img.shields.io/badge/domains-11-000000?style=flat-square)](#domains)
[![schema](https://img.shields.io/badge/schema-v2-000000?style=flat-square)](knowledge/SCHEMA.md)
[![ingest](https://img.shields.io/github/actions/workflow/status/aryamankh/SpaceX-Collective-Knowledge-Database/knowledge.yml?style=flat-square&label=corpus)](.github/workflows/knowledge.yml)
[![license](https://img.shields.io/badge/license-Apache--2.0-000000?style=flat-square)](LICENSE)

</div>

## Purpose

Versioned engineering corpus, maintained per domain, exported as a machine-readable dataset for Grokbot. The corpus is the single source of engineering knowledge for retrieval; the export is the only supported machine interface.

Scope:

- one markdown note per event, dated, with fixed front-matter
- one directory per domain, one owning team per directory
- schema validation and corpus reproducibility enforced in CI
- no runtime service, no database, no external dependency for reading the corpus

## Domains

| Directory | Scope | Notes |
| --- | --- | :---: |
| `knowledge/propulsion/` | engines, turbopumps, feed system, igniters, TVC | 12 |
| `knowledge/structures/` | tanks, barrels, skirts, lugs, welds, load paths | 12 |
| `knowledge/avionics/` | power, harnesses, buses, computers, telemetry | 12 |
| `knowledge/gnc/` | guidance, navigation, control allocation, sensors | 12 |
| `knowledge/thermal-protection/` | tiles, blankets, seals, purge, reentry heating | 12 |
| `knowledge/ground-systems/` | GSE, quick disconnects, deluge, transport, hold-down | 12 |
| `knowledge/manufacturing/` | layup, weld parameters, tooling, tolerances, rework | 12 |
| `knowledge/materials/` | alloys, seals, adhesives, coatings, certifications | 12 |
| `knowledge/flight-software/` | sequencer, fault handling, aborts, parameter tables | 12 |
| `knowledge/flight-ops/` | countdown, range, recovery, weather, crew flow | 12 |
| `knowledge/safety/` | LOTO, confined space, exclusion zones, mishap closeout | 12 |

## Note format

Path: `knowledge/<domain>/<prefix>-<slug>-<YYYY-MM>.md`.

~~~yaml
---
id: prop-raptor-tvc-actuator-oscillation-at-42-hz-2025-12
domain: propulsion
system: raptor-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
date: 2025-12-04
tags: [tvc, oscillation, hotfire, damping]
---
~~~

Required fields: `id`, `domain`, `system`, `author`, `reviewed_by`, `status`, `severity`, `date`, `tags`.

`status` ∈ `draft`, `reviewed`, `superseded`. `severity` ∈ `low`, `medium`, `high`, `critical`.

Body sections, in order:

~~~text
## What happened
## What we changed
## What we would do differently
## Evidence
~~~

`## Evidence` holds the trace, plot, part number or procedure reference. Notes are never deleted; superseded notes set `status: superseded` and reference the replacement.

Full specification: [`knowledge/SCHEMA.md`](knowledge/SCHEMA.md).

## Validation

~~~bash
./manage.sh ingest-kb
~~~

Runs the validator over the tree and emits `dist/corpus.jsonl` and `knowledge/index.json`.

Validator rules:

| Rule | Result |
| --- | --- |
| missing or malformed front-matter | fail |
| `domain` differs from parent directory | fail |
| duplicate `id` | fail |
| invalid `status` or `severity` value | fail |
| malformed `date` | fail |
| body sections missing or out of order | fail |
| `reviewed_by` equals `author` on `status: reviewed` | warning |

Output format: one JSON object per line, keys sorted, `id` ascending, body verbatim, `sha256` over `id` and body, no build timestamps. Byte-identical across machines.

## Local development

Requirements: Go 1.22+, Node 20+.

~~~bash
git clone https://github.com/aryamankh/SpaceX-Collective-Knowledge-Database.git
cd SpaceX-Collective-Knowledge-Database
./manage.sh ingest-kb
cd backend/tools/ingest && go vet ./... && go test ./...
cd ../.. && ./manage.sh dev
~~~

`manage.sh` targets: `build`, `ingest-kb`, `lint`, `test`, `dev`, `new-note`.

## Contribution procedure

1. `./manage.sh new-note <domain> "<title>"` scaffolds path, slug and front-matter.
2. Fill body sections and attach evidence.
3. Open a pull request; CODEOWNERS assigns the owning team as reviewer.
4. Owner reviews the technical claim and evidence, not the prose.
5. CI validates the note and rebuilds the corpus; merge requires a green build and an owner approval.

## Review and ownership

Ownership is declared per directory in `.github/CODEOWNERS`. Each domain has one owning team and one required reviewer. The maintainer account holds review on `knowledge/SCHEMA.md`, `backend/tools/ingest/` and any change to the corpus format.

## CI

`.github/workflows/knowledge.yml` runs on `push` and `pull_request`:

- schema validation of changed notes
- corpus rebuild and reproducibility diff
- `go vet` and unit tests on the ingest tool
- CODEOWNERS coverage check per domain
- staleness flag for notes older than 18 months with `status: reviewed`

Failures block merge.

## Layout

~~~text
knowledge/                 corpus, one directory per domain
  SCHEMA.md                format specification
  index.json               generated index
backend/tools/ingest/      validator and exporter (Go)
.github/workflows/         validation and reproducibility CI
.github/CODEOWNERS         directory ownership
assets/                    banner and documentation images
manage.sh                  build, ingest, lint, test, dev, new-note
dist/corpus.jsonl          generated export
~~~

## Versioning

Corpus format is versioned in `knowledge/SCHEMA.md`. A format change requires a schema version bump and a migration note; consumers pin the version they read. Content changes do not bump the version.

## Prior art

The workspace layer — gist-backed persistence, proxy, OAuth exchange and request editor — builds on [Prestige](https://github.com/sharat87/prestige) by Shrikant Sharat Kandula, Apache-2.0. The corpus, schema, ingestion pipeline and domain layout are original to this repository. See [NOTICE](NOTICE).

## License

Apache-2.0. See [LICENSE](LICENSE).
