# STK_CM Portal — Configuration Management

**AoR:** STK_CM (Configuration Management)  
**ATA Scope:** 00 — GENERAL (Program Governance Control Plane)  
**Entry Point:** Configuration Management & Baseline Control

---

## Overview

The STK_CM Portal serves as the **ATA 00 governance entry point** for Configuration Management, providing
baseline control, cross-ATA integration clearance, SSOT register governance, and evidence packaging for
release snapshots across the AMPEL360 ecosystem.

### Primary Responsibilities

1. **Authority Model (K01)** — decision rights, certification-basis authority alignment where applicable
2. **Integration Contracts (K04)** — cross-ATA coupling control (interfaces/ICDs/clearances)
3. **Data Governance SSOT (K06)** — v6.0 nomenclature, schemas, identifiers, uniqueness and validation rules
4. **Evidence Packaging & Release Snapshots (K08)** — audit-ready evidence closure, release/export bundles
5. **Cross-AoR Coordination** — interface with PMO, SE, SAF, CERT, DATA

---

## Navigation

- [PROGRAM_SPACET/](./PROGRAM_SPACET/)
- [LINKS/](./LINKS/) *(optional)*
- [REGISTRIES/](./REGISTRIES/) *(optional: legacy/shortcut; prefer program subtree SSOT)*

---

## Portal Contract (SSOT)

This portal uses a **Portal Contract** as SSOT configuration (views, tools, outputs, validation rules).

> If you keep the contract as a registry-config artifact, treat it as:
> - **CATEGORY:** REGISTRY
> - **TYPE:** REGISTER
> - **KNOT:** K06 (SSOT governance)

**File (example pattern):**  
`00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Portal_Contract_REGISTRY_REGISTER_I01-R01_ACTIVE.yaml`

### Contract Sections

1. **Metadata & Context** — AoR identity, program scope, pathway definition
2. **Portal Views** — baseline status, change queue, SSOT registers, CI/CD, cross-ATA interfaces
3. **Communication Matrix** — Cross-AoR dependencies (PMO, SE, SAF, CERT, DATA)
4. **Outputs** — what CM produces (release snapshots, registers, evidence packs)
5. **Tools** — tool launchpad configuration
6. **Validation** — enforcement rules and gate mapping (**K01/K04/K06/K08**)
7. **Publishing** — export destinations and notification channels
8. **Features** — MoSCoW backlog
9. **AI Assistants** — portal-aware assistants (constraints: cannot bypass gates; must link to SSOT)
10. **Backend Services** — service integrations
11. **Knot Mapping** — operational workflow (**K01 → K04 → K06 → K08**)

---

## Feature Register (SSOT)

Feature register is a structured SSOT register.

> Recommended classification:
> - **CATEGORY:** REGISTRY
> - **TYPE:** REGISTER
> - **KNOT:** K06 (SSOT)

**File (example pattern):**  
`00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Portal_Feature_Register_REGISTRY_REGISTER_I01-R01_ACTIVE.csv`

### Feature Summary by MoSCoW
- MUST / SHOULD / COULD / WON’T (counts and IDs as per register)

---

## Knot Workflow (K01 → K04 → K06 → K08)

### K01 — Authority Model / Certification-Basis Authority
- **Purpose:** establish authority model, decision rights, and certification-basis authority alignment (where applicable)
- **Outputs:** authority statements, approval minutes, clearance statements (as authority artifacts)
- **Gate concept:** authority approval required where mandated by governance

### K04 — Interfaces / ICDs / Integration Contracts (Cross-ATA Coupling)
- **Purpose:** approve integration impacts across systems (interfaces, ICD coherence, coupling clearance)
- **Outputs:** impact analysis, cross-ATA clearance, integration approval records
- **Gates:** impact analysis complete, approvals obtained, cross-ATA clearance recorded

### K06 — Data Governance / SSOT / Schemas / Identifiers
- **Purpose:** enforce v6.0 nomenclature, schemas, identifiers, uniqueness; maintain SSOT registers
- **Outputs:** schema registry, vocabularies, rulesets, validation profiles
- **Gates:** nomenclature validation, schema validation, SSOT consistency, uniqueness checks

### K08 — DPP / Provenance / Evidence Packaging & Release Snapshots
- **Purpose:** package evidence, freeze snapshots, and produce audit-ready export bundles
- **Outputs:** release snapshots, evidence index, traceability matrices, audit/export bundles
- **Gates:** traceability complete, evidence closure, signoff obtained, CERT clearance included (when required)

---

## Tool Launchpad (example)

1. **Change Control Console** — cross-ATA impact & clearance workflow (**K04**)
2. **Standards & SSOT Manager** — nomenclature/schemas/identifiers (**K06**)
3. **CI Gate Monitor** — validation tracking (**K06/K08**)
4. **Release Snapshot Builder** — freeze & manifest (**K08**)
5. **Audit Evidence Assembler** — evidence index & closure (**K08**)
6. **Git Portal** — version control interface
7. **CCB / Integration Board Portal** — integration decision workflow (**K04**)

---

## Portal-aware AI Assistants

### CM Assistant (Primary)
**AoR:** STK_CM  
**Constraints:**
- cannot bypass gates
- cannot invent AoRs
- must link to SSOT
- must leave an auditable trail (what/why)

**Capabilities:**
- triage changes (K04)
- suggest routing and required clearances (K04)
- validate nomenclature/schema/uniqueness (K06)
- prepare release snapshot and evidence closure summaries (K08)

### Cross-AoR Assistants (interfaces only)
- **PMO Assistant** — prioritization, lead time, blockers
- **SE Assistant** — interface impact, ICD coherence
- **SAF Assistant** — safety/security implications
- **CERT Assistant** — compliance checklist, evidence expectations
- **DATA Assistant (STK_DATA)** — lineage, schema consistency, retention

---

## Cross-AoR Dependencies

- **STK_PMO** — planning, milestones, reporting, prioritization  
- **STK_SE** — requirements coherence, architecture, ICDs  
- **STK_SAF** — safety/security gating inputs  
- **STK_CERT** — evidence expectations, clearance rules, audit posture  
- **STK_DATA** — data governance, lineage, quality, schemas, retention  

---

## Backend Services (conceptual)

1. **Register Service** — SSOT registers (baseline, change, decisions, exceptions)
2. **Workflow Service** — approvals, clearances, escalations (K04)
3. **Evidence Service** — storage, hash verification, artifact linking (K08)
4. **Policy/Rules Service** — nomenclature, uniqueness, gate criteria (K06)
5. **Audit Log Service** — append-only log, export API (K08)

---

## Publishing Destinations

1. **Repository Baseline** — git tags/releases (immutable references)
2. **Registry Read-only** — append-only registry exports (when required)
3. **Evidence Packs** — signed bundles (K08)
4. **Notification Feed** — portal/email/webhook events

**Export Formats:** JSON, CSV, YAML, PDF (audit packs)  
**Integrity:** sha256 hashes (and signing where mandated by security policy)

---

## Governance Rules (minimum)

- No integration clearance without **K04** evidence/approval where cross-ATA coupling exists.
- No SSOT acceptance without **K06** validation (nomenclature + schema + uniqueness where applicable).
- No release snapshot/export without **K08** evidence closure and required signoffs/CERT clearance.

---

## Files in this Directory (example)


