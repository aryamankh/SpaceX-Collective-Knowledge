# Corpus schema

Every note here is one hard-won lesson, written by the person who lived it and
reviewed by the owning team before merge. Grokbot ingests the whole corpus, so the
format is strict and machine-checked.

## Layout

```
knowledge/<domain>/<slug>-<yyyy>-<mm>.md
```

Domain is the owning discipline. Slug is lowercase, hyphenated, and names the
finding, not just the subsystem. `index.json` is generated, never hand-edited.

## Front-matter

```yaml
---
id: prop-raptor-tvc-oscillation-2026-04
domain: propulsion
system: raptor-3
author: aryamankh
reviewed_by: aryamankh
status: reviewed
severity: high
created: 2026-04-18
tags: [tvc, oscillation, damping]
---
```

| field | required | values |
|---|---|---|
| `id` | yes | `<domain-abbrev>-<slug>-<yyyy>-<mm>`, unique |
| `domain` | yes | directory name |
| `system` | yes | vehicle, engine, pad asset or process area |
| `author` | yes | GitHub login from `people.yaml` |
| `reviewed_by` | yes | login from a different team; `pending` while in draft |
| `status` | yes | `draft`, `reviewed`, `superseded` |
| `severity` | yes | `low`, `medium`, `high`, `critical` |
| `created` | yes | ISO date |
| `tags` | yes | 2-6 lowercase tags |

## Body

All required, in this order: `## Context`, `## What happened`, `## Root cause`,
`## What we changed`, `## What we would do differently`, `## Evidence`.

## Rules

- Write for a reader who has never seen your subsystem.
- One lesson per note. If it needs two, split it.
- Numbers over adjectives: frequencies, pressures, torques, durations.
- Name the change owner. A lesson with no owner is folklore.
- Never paste controlled drawings inline; link the document id.
- `status: reviewed` requires a `reviewed_by` login from a different team.

## Ingestion

`./manage.sh ingest-kb` validates every note, then emits `dist/corpus.jsonl` and
`knowledge/index.json`. CI fails on any schema violation, so `main` is always
ingestible.
