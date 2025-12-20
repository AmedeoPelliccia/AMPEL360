# STK_CM Portal — Configuration Management

**AoR:** STK_CM (Configuration Management)  
**ATA Scope:** 00 — GENERAL  
**Entry Point:** Configuration Management & Baseline Control

---

## Overview

The STK_CM Portal serves as the **ATA 00 entry point** for Configuration Management, providing comprehensive baseline control, change management, and audit readiness capabilities across the AMPEL360 ecosystem.

### Primary Responsibilities

1. **Baseline Management** — Version control, freeze points, release packages
2. **Change Control** — CR/ECR/ECO workflow with cross-ATA impact analysis
3. **Standards Enforcement** — v6.0 nomenclature, uniqueness validation
4. **Audit Readiness** — Immutable audit trails, evidence packaging
5. **Cross-AoR Coordination** — Interface with PMO, SE, SAF, CERT, DAB

---

## Portal Contract

**File:** `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__portal-contract_REGISTRY_REG_I01-R01_ACTIVE.yaml`

**Version:** 2.0.0  
**Status:** ACTIVE  
**Last Updated:** 2025-12-20

### Contract Sections

1. **Metadata & Context** — AoR identity, program scope, pathway definition
2. **Portal Views** — What CM users see (baseline status, change queue, registers, CI/CD, cross-ATA interfaces)
3. **Communication Matrix** — Cross-AoR dependencies (PMO, SE, SAF, CERT, DAB)
4. **Outputs** — What CM produces (BRP, CM Plans, Program Registers, Audit Packs)
5. **Tools** — Tool Launchpad configuration (7 tools)
6. **Validation** — Sign-off rules and gate enforcement (K04/K06/K10)
7. **Publishing** — Export destinations and notification channels
8. **Features** — MoSCoW backlog (39 features total)
9. **AI Assistants** — Portal-aware assistants (6 cross-AoR assistants)
10. **Backend Services** — Service integrations (5 core services)
11. **Knot Mapping** — Operational workflow (K01/K04/K06/K10)

---

## Feature Register

**File:** `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__portal-feature-register_REGISTRY_REG_I01-R01_ACTIVE.csv`

### Feature Summary by MoSCoW

| Category | Count | Features |
|----------|-------|----------|
| **MUST** | 19 | Core portal features (F01-F09) + CM-specific (F_CM01-F_CM10) |
| **SHOULD** | 10 | Enhanced capabilities (F12, F14, F_CM11-F_CM18) |
| **COULD** | 6 | Future enhancements (F15, F_CM19-F_CM23) |
| **WON'T** | 4 | Explicitly excluded (F19, F20, F_CM24, F_CM25) |

### Key Features (MUST)

1. **F_CM01** — Baseline Registry & Manifest
2. **F_CM02** — Change Request Workflow (CR/ECR/ECO)
3. **F_CM03** — Impact Analysis Cross-ATA
4. **F_CM04** — Gate Enforcement (K04/K06/K10)
5. **F_CM05** — CI Gate Monitor
6. **F_CM06** — Nomenclature & Standards Enforcement
7. **F_CM07** — Audit Trail (Immutable Log)
8. **F_CM08** — Release Builder (BRP)
9. **F_CM09** — Registers Hub
10. **F_CM10** — Role-based Access Control (RBAC)

---

## Knot Workflow (K01 → K04 → K06 → K10)

### K01 — Standards
- **Purpose:** Define nomenclature, policies, templates
- **Output:** Standard release + enforcement rules
- **Gates:** Nomenclature validation, schema validation

### K04 — Change Control Gate
- **Purpose:** Approve changes for integration
- **Output:** CR "Approved for integration"
- **Gates:** Impact analysis complete, approval obtained, cross-ATA clearance

### K06 — Baseline Release Gate
- **Purpose:** Validate and freeze release candidate
- **Output:** BRP "Releaseable"
- **Gates:** Nomenclature compliance, uniqueness check, baseline integrity, CI validation pass

### K10 — Audit Gate
- **Purpose:** Prepare audit-ready baseline
- **Output:** "Audit-ready baseline" + export
- **Gates:** Traceability complete, evidence closure, signoff obtained, CERT clearance

---

## Tool Launchpad (7 Tools)

1. **Change Control Console** — CR/ECR/ECO workflow, impact analysis
2. **Baseline Builder** — Compose/lock/export baseline
3. **Standards & Nomenclature Manager** — v6.0 enforcement
4. **CI Gate Monitor** — Pipeline validation tracking
5. **Audit Evidence Assembler** — Evidence pack generation
6. **Git Portal** — Version control interface
7. **Change Control Board Portal** — CCB governance

All tools configured with TALF (Tool Access & Licensing Fabric) integration for entitlement checking, license management, and audit logging.

---

## Portal-aware AI Assistants (6 Assistants)

### CM Assistant (Primary)
**AoR:** STK_CM  
**Capabilities:**
- Triage changes
- Suggest approval routing
- Prepare BRP
- Check nomenclature
- Explain policies
- Identify cross-ATA impact
- Generate audit trail summary
- Suggest evidence requirements

### Cross-AoR Assistants
- **PMO Assistant** — Prioritization, lead time estimation, blocker alerts
- **SE Assistant** — Interface impact, ICD coherence, requirements assessment
- **SAF Assistant** — Safety/security implications, evidence suggestions
- **CERT Assistant** — Compliance checklist, evidence pack structure
- **DAB Assistant** — Data lineage, quality, schema consistency

**All assistants:**
- Operate with baseline context
- Leave auditable trail (what recommended and why)
- Cannot bypass gates
- Cannot invent AoRs
- Must cite sources
- Must link to SSOT

---

## Cross-AoR Dependencies

### STK_PMO
- Planificación, hitos, reporting, priorización

### STK_SE
- Coherencia de requisitos, arquitectura, ICDs

### STK_SAF
- Impactos safety/security, hazard/risk gating

### STK_CERT
- Evidencias, compliance packs, sign-offs formales

### STK_DAB
- Gobierno del dato, linaje, calidad, esquemas, retention

---

## Backend Services

1. **Register Service** — Baseline, change, decision, exception, config item registries
2. **Workflow Service** — Change, approval, gate, escalation workflows
3. **Evidence Service** — Storage, hash verification, artifact linking
4. **Policy/Rules Service** — Nomenclature, uniqueness, gate criteria, blocking rules
5. **Audit Log Service** — Event sourcing, append-only log, query/export API

---

## Publishing Destinations

1. **Repository Baseline** — Git tags/releases (immutable)
2. **Registry Read-only** — Audit registry (append-only)
3. **Evidence Packs** — Evidence store (signed bundles)
4. **Notification Feed** — Portal/email/webhook events

**Export Formats:** JSON, CSV, YAML, PDF (audit packs)

**Signing:** SHA256-RSA, key owner STK_CM, verification required

---

## Governance

**Regla base:** Ningún baseline "releaseable" sin pasar K04 → K06 → K10 (según aplicabilidad del cambio)

**Sign-off hierarchy:**
- **Primary:** STK_CM
- **Conditional:** SE (interfaces/requisitos), SAF (safety/security), CERT (compliance), PMO (plan/hitos), DAB (calidad/linaje)

**Audit retention:** 7 years (evidence), permanent (audit logs)

---

## References

- **Portal Feature Catalog (SSOT):** `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__portal-feature-catalog_REGISTRY_CAT_I01-R01_ACTIVE.md`
- **AoR Portal Contract Schema:** `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__aor-portal-contract-schema_DELIVERABLE_SCHEMA_I01-R01_ACTIVE.md`
- **Tool Launchpad Specification:** `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__tool-launchpad-specification_DELIVERABLE_SPEC_I01-R01_ACTIVE.md`
- **v6.0 Nomenclature:** `README.md` Section 10
- **KNOTS Framework:** `README.md` Section 7

---

## Files in this Directory

```
STK_CM/PORTAL/
├── 00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__portal-contract_REGISTRY_REG_I01-R01_ACTIVE.yaml
│   └── Portal contract (v2.0.0) — Complete portal configuration for ATA 00
├── 00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__portal-feature-register_REGISTRY_REG_I01-R01_ACTIVE.csv
│   └── Feature register — Tabular view of 39 features with MoSCoW, owners, dependencies, knots
├── README.md
│   └── This file — Overview and navigation guide
├── LINKS/
│   └── External references and integrations
└── REGISTRIES/
    └── CM-specific registries and catalogs
```

---

**Maintained by:** cm-team@ampel360.org  
**Last Updated:** 2025-12-20  
**Status:** ACTIVE
