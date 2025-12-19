# LIFECYCLE — 14 Controlled Lifecycle Phases

## Overview

The **LIFECYCLE** directory contains **14 controlled lifecycle phases (LC01-LC14)** that represent the temporal progression of work from initial concept through retirement and circularity.

---

## Lifecycle Phase Definitions

### LC01 — Problem Statement / Generation / Prompting Engineering
**Path:** `LC01-Problem-Statement-Generation-Prompting/`

**Scope:** Problem framing, ideation, NKU generation pathways, prompting engineering baselines, initial scope statements

**Primary AoR(s):** STK_DAB, STK_SE, STK_CM  
**Primary KNOT:** K01

---

### LC02 — System Requirements
**Path:** `LC02-System-Requirements/`

**Scope:** Requirement capture, allocation, traceability seeding, acceptance criteria definition

**Primary AoR(s):** STK_SE, STK_CM  
**Primary KNOT:** K02

---

### LC03 — Design Models
**Path:** `LC03-Design-Models/`

**Scope:** Architecture + design models (SysML, design baselines, interface modeling)

**Primary AoR(s):** STK_SE, STK_PHM, STK_DAB  
**Primary KNOT:** K03

---

### LC04 — Engineering Analysis & Calculation Models
**Path:** `LC04-Engineering-Analysis-Calculation/`

**Scope:** Analyses, calculation models, trade studies, margins, model validation artifacts

**Primary AoR(s):** STK_PHM, STK_SE, STK_DAB  
**Primary KNOT:** K04

---

### LC05 — Integration Testing & Prototyping (V&V / V6V)
**Path:** `LC05-Integration-Testing-Prototyping/`

**Scope:** Prototyping, integration campaigns, SIL/HIL/PIL, closure evidence production

**Primary AoR(s):** STK_TEST, STK_SE, STK_DAB  
**Primary KNOT:** K05

**Note:** "V6V" naming is treated as part of the LC05 scope.

---

### LC06 — Quality
**Path:** `LC06-Quality/`

**Scope:** QMS artifacts, process quality, audits, nonconformance management, quality gates

**Primary AoR(s):** STK_CM, STK_PMO, STK_TEST  
**Primary KNOT:** K06

---

### LC07 — Safety and Security
**Path:** `LC07-Safety-Security/`

**Scope:** Safety case, hazard controls, cybersecurity assurance objectives and evidence

**Primary AoR(s):** STK_SAF, STK_CY, STK_SE  
**Primary KNOT:** K07

---

### LC08 — Certification and First Flight
**Path:** `LC08-Certification-First-Flight/`

**Scope:** Certification planning/execution, authority-facing packs, first-flight/mission readiness evidence

**Primary AoR(s):** STK_CERT, STK_TEST, STK_OPS  
**Primary KNOT:** K08

---

### LC09 — Green Aircraft / Baselines
**Path:** `LC09-Green-Aircraft-Baselines/`

**Scope:** Sustainability baselines, circularity KPIs, green tech evidence, ESG reporting baselines

**Primary AoR(s):** STK_PMO, STK_DAB, STK_CM  
**Primary KNOT:** K09

---

### LC10 — Industrialization / Serialization / Production Plan / CM
**Path:** `LC10-Industrialization-Serialization-Production/`

**Scope:** Industrial planning, production readiness, configuration baselines, manufacturing interfaces

**Primary AoR(s):** STK_CM, STK_PMO, STK_PHM  
**Primary KNOT:** K10

---

### LC11 — Operations
**Path:** `LC11-Operations/`

**Scope:** ConOps, procedures, readiness, operational baselines, mission operations control

**Primary AoR(s):** STK_OPS, STK_SPACEPORT, STK_CM  
**Primary KNOT:** K11

---

### LC12 — Support and Services
**Path:** `LC12-Support-Services/`

**Scope:** Customer support, service processes, service tooling, support documentation

**Primary AoR(s):** STK_OPS, STK_MRO, STK_DAB  
**Primary KNOT:** K12

---

### LC13 — MRO and Sustainment
**Path:** `LC13-MRO-Sustainment/`

**Scope:** Maintenance programs, manuals, sustainment evidence, reliability/PHM integration

**Primary AoR(s):** STK_MRO, STK_PHM, STK_DAB  
**Primary KNOT:** K13

---

### LC14 — Retirement Management and Circularity
**Path:** `LC14-Retirement-Circularity/`

**Scope:** End-of-life, retirement procedures, recycling/return flows, circularity closure

**Primary AoR(s):** STK_PMO, STK_CM, STK_DAB  
**Primary KNOT:** K14

---

## Key Principles

1. **PHASE is lifecycle only** — It must not encode domain segmentation (that is BLOCK)
2. **PHASE is always exactly one of LC01..LC14** — Appears once in the filename
3. **PHASE meanings are fixed** — Must not be repurposed
4. **PHASE progression is governed** — CM controls phase transitions

---

## 360° Integration

The lifecycle phases form a continuous circle:

```
DESIGN → BUILD → VERIFY → CERTIFY → OPERATE → SUSTAIN → EVOLVE → (return)
   ↑                                                              ↓
   └──────────────── Knowledge Ledger Continuity ─────────────────┘
```

Every artifact produced at any phase:
- Feeds the knowledge ledger
- Reduces uncertainty
- Is reusable across cycles
- Links to traceability graph

---

## Usage Guidelines

### For Artifact Creation

When creating artifacts:
1. **Identify current lifecycle phase** (LC01-LC14)
2. **Include phase in filename** as per v6.0 nomenclature
3. **Align with primary KNOT** for that phase
4. **Generate phase-appropriate evidence**
5. **Update phase-specific ledgers**

### For Phase Transitions

When transitioning between phases:
1. **Review phase exit criteria** (gates)
2. **Ensure evidence is complete**
3. **Run phase-specific validators**
4. **Update configuration baseline**
5. **Record transition in ledger**

---

## Phase-KNOT-AoR Mapping

| Phase | KNOT | Primary AoR(s) |
|-------|------|----------------|
| LC01 | K01 | STK_DAB, STK_SE, STK_CM |
| LC02 | K02 | STK_SE, STK_CM |
| LC03 | K03 | STK_SE, STK_DAB |
| LC04 | K04 | STK_PHM, STK_SE, STK_DAB |
| LC05 | K05 | STK_TEST, STK_SE, STK_DAB |
| LC06 | K06 | STK_CM, STK_PMO, STK_TEST |
| LC07 | K07 | STK_SAF, STK_CY, STK_SE |
| LC08 | K08 | STK_CERT, STK_TEST, STK_OPS |
| LC09 | K09 | STK_PMO, STK_DAB, STK_CM |
| LC10 | K10 | STK_CM, STK_PMO, STK_PHM |
| LC11 | K11 | STK_OPS, STK_SPACEPORT, STK_CM |
| LC12 | K12 | STK_OPS, STK_MRO, STK_DAB |
| LC13 | K13 | STK_MRO, STK_PHM, STK_DAB |
| LC14 | K14 | STK_PMO, STK_CM, STK_DAB |

---

## Governance

- **Phase codes are configuration-controlled** — LC01..LC14 only
- **Phase meanings are normative** — Cannot be changed or repurposed
- **Phase transitions are gated** — Must satisfy exit criteria
- **Phase evidence is mandatory** — Required for phase closure

---

## Version

**Lifecycle Structure Version:** 1.0  
**Controlled Phase Range:** LC01-LC14  
**Last Updated:** 2025-12-19

---

## References

- [CAXS Main README](../README.md)
- [Phase Definitions (Main README)](../../README.md#928-phase-allowlist-lc01lc14--controlled-lifecycle-definitions-normative)
- [KNOTS Directory](../KNOTS/README.md)
