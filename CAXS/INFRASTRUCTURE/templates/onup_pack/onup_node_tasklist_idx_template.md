---
title: "ONUP Node Tasklist (SSOT) — {{AXIS}} / ATA {{ATA}} / BLOCK {{BLOCK}} / {{PHASE}}"
project: "AMPEL360"
program: "{{PROGRAM}}"
family: "{{FAMILY}}"
variant: "{{VARIANT}}"
version: "{{VERSION}}"
model: "{{MODEL}}"
block: "{{BLOCK}}"
phase: "{{PHASE}}"
knot: "{{KNOT}}"
primary_aor: "{{PRIMARY_AOR}}"
issue_rev: "{{ISSUE_REV}}"
status: "{{STATUS}}"
node_subject: "{{NODE_SUBJECT}}"
---

# ONUP Node Tasklist (SSOT) — {{AXIS}} / ATA {{ATA}} / BLOCK {{BLOCK}} / {{PHASE}}

## Intent
SSOT navigation and control plane for this node's uncertainty resolution:
DELIVERABLE ↔ EVIDENCE ↔ SIGNOFF (where required), with deterministic routing and gates.

## Node identity (PGK)
ATA={{ATA}}, PROJECT=AMPEL360, PROGRAM={{PROGRAM}}, FAMILY={{FAMILY}}, VARIANT={{VARIANT}},
VERSION={{VERSION}}, MODEL={{MODEL}}, BLOCK={{BLOCK}}, PHASE={{PHASE}}

## Mandatory backlinks
- Portal entrypoints SSOT: `{{PORTAL_ENTRYPOINTS_LINK}}`
- AoR entrypoint (Primary): `{{AOR_ENTRYPOINT_LINK}}`
- Axis/ATA domain index: `{{DOMAIN_INDEX_LINK}}`

## ONUP artifacts (must exist)
- Problem statement: `{{PROBLEM_STATEMENT_LINK}}`
- ATA impact matrix (CSV): `{{ATA_IMPACT_MATRIX_LINK}}`
- AoR RACI (CSV): `{{AOR_RACI_LINK}}`
- Roadmap registry (CSV): `{{ROADMAP_REGISTRY_LINK}}`
- Task registry (CSV): `{{TASK_REGISTRY_LINK}}`
- Evidence index: `{{EVIDENCE_INDEX_LINK}}`
- Signoff index: `{{SIGNOFF_INDEX_LINK}}`

## Execution folders (optional, if you materialize per-node subfolders)
- `TASKS/`
- `EVIDENCE/`
- `DECISIONS/`
- `REGISTRIES/`
- `EXPORTS/`
- `MONITORING/`
- `LINKS/`

## Node status summary
- Current node state: {{NODE_STATE}} (SUPERPOSITION | PARTIAL_COLLAPSE | COLLAPSED | REOPENED)
- Hard blockers (from impact matrix): {{HARD_BLOCKERS}}
- Next milestone (from roadmap): {{NEXT_MILESTONE}}

## Gate compliance notes
- v6.0 naming enforced in-scope
- One Official Chain uniqueness enforced
- Category↔AoR constraints enforced (SIGNOFF/EXPORT_CONTROL → STK_CM or STK_CERT)
- Link integrity required for critical SSOT references
