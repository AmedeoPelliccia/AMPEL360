# AoR — Areas of Responsibility (Stakeholder Entry Points)

## Overview

The **AoR (Areas of Responsibility)** directory contains **14 stakeholder entry points**, each representing a primary governance domain with specific ownership boundaries, accountabilities, and portal views.

Each subdirectory serves as a **role-routed entry point** into the CAXS Portal (CA360º).

---

## Stakeholder Directory Structure

### STK_CM — Configuration Management
**Path:** `STK_CM/`

**Ownership:** Naming standard, change control, baselines, registers, release governance

**Primary Responsibilities:**
- v6.0 nomenclature enforcement
- Configuration baselines management
- Change control processes
- Release gate governance
- Master registers maintenance
- Version control and branching strategies

**Primary ATA Chapters:** 00, 11, 99

---

### STK_PMO — Program Management Office
**Path:** `STK_PMO/`

**Ownership:** Planning, schedule, cost, risk, gates, stakeholder/program governance

**Primary Responsibilities:**
- Program planning and scheduling
- Cost management and budgeting
- Risk assessment and mitigation
- Gate reviews and milestone tracking
- Stakeholder coordination
- Resource allocation

**Primary ATA Chapters:** 00, 01-05

---

### STK_SE — Systems Engineering
**Path:** `STK_SE/`

**Ownership:** Architecture, SysML/MBSE governance, ICD governance, requirements structure

**Primary Responsibilities:**
- System architecture definition
- SysML/MBSE model governance
- Interface Control Document (ICD) management
- Requirements allocation and traceability
- System integration planning
- Verification and validation planning

**Primary ATA Chapters:** 00, 20, 40, 51

---

### STK_DAB — Digital Applications & Blockchains
**Path:** `STK_DAB/`

**Ownership:** Software, prompting/agent specs, automation, data engineering, schemas/SSOT, traceability, DPP/SBOM, manifests/signing, ledger/blockchain

**Primary Responsibilities:**
- Software architecture and development
- Agentic task automation and prompting engineering
- Data schemas and SSOT (Single Source of Truth)
- Traceability graph maintenance
- Digital Product Passport (DPP) implementation
- SBOM/BOM generation
- Release manifest signing
- Knowledge ledger operations
- Portal automation and CI/CD

**Primary ATA Chapters:** 42, 46, 90-99

---

### STK_PHM — Physical & Mechanical Engineering
**Path:** `STK_PHM/`

**Ownership:** Aerostructures, mechanisms, hydraulics, pneumatics, actuation, landing gear

**Primary Responsibilities:**
- Structural design and analysis
- Mechanical systems engineering
- Hydraulic and pneumatic systems
- Actuation systems
- Landing gear design
- Physical integration

**Primary ATA Chapters:** 20, 29, 32, 51-57

---

### STK_SAF — Safety
**Path:** `STK_SAF/`

**Ownership:** FHA/PSSA/SSA logic, hazard controls, safety constraints, operational limits

**Primary Responsibilities:**
- Functional Hazard Assessment (FHA)
- Preliminary System Safety Assessment (PSSA)
- System Safety Assessment (SSA)
- Hazard identification and control
- Safety requirements definition
- Safety case development
- Operational limits definition

**Primary ATA Chapters:** 04, 26, all safety aspects

---

### STK_CERT — Certification / Compliance
**Path:** `STK_CERT/`

**Ownership:** Compliance evidence, certification packs, authority-facing deliverables

**Primary Responsibilities:**
- Certification planning and execution
- Compliance evidence collection
- Authority liaison and submissions
- Certification packs preparation
- Type Certificate support
- Continued airworthiness
- TEKNIA credential issuance

**Primary ATA Chapters:** All (certification oversight)

---

### STK_TEST — Test / V&V
**Path:** `STK_TEST/`

**Ownership:** Test planning/execution, benches, results, anomalies, VV evidence

**Primary Responsibilities:**
- Test planning and strategy
- Test procedure development
- SIL/HIL/PIL bench operation
- Test execution and reporting
- Anomaly management
- V&V evidence generation
- Test data management

**Primary ATA Chapters:** 100-116 (SIM/TEST axis)

---

### STK_OPS — Operations
**Path:** `STK_OPS/`

**Ownership:** ConOps, procedures, readiness, operational baselines and evidence

**Primary Responsibilities:**
- Concept of Operations (ConOps) development
- Operational procedures
- Flight operations support
- Mission operations
- Operational readiness assessment
- Operational baselines maintenance

**Primary ATA Chapters:** 01-05, 11

---

### STK_MRO — Maintenance, Repair & Overhaul
**Path:** `STK_MRO/`

**Ownership:** Maintenance plans, servicing, facilities/tooling, maintainability

**Primary Responsibilities:**
- Maintenance program development
- Maintenance manual authoring (AMM, IPC, etc.)
- Servicing procedures
- MRO facility requirements
- Tooling specifications
- Maintainability engineering
- Reliability engineering

**Primary ATA Chapters:** 05, 12, all (MRO perspective)

---

### STK_AI — AI / ML Engineering & Assurance
**Path:** `STK_AI/`

**Ownership:** Model registry, AI validation, monitoring, AI governance and assurance

**Primary Responsibilities:**
- AI/ML model lifecycle management
- Model registry maintenance
- AI validation and verification
- Model monitoring and drift detection
- AI governance framework
- AI risk assessment
- Bias detection and mitigation

**Primary ATA Chapters:** 90, 96, 114

---

### STK_CY — Cybersecurity
**Path:** `STK_CY/`

**Ownership:** IAM, ZTA, secure networks, hardening, cyber evidence and controls

**Primary Responsibilities:**
- Identity and Access Management (IAM)
- Zero Trust Architecture (ZTA) implementation
- Network security design
- System hardening
- Cyber threat analysis
- Security evidence generation
- Compliance with cyber standards

**Primary ATA Chapters:** 20, 42, 87

---

### STK_SPACEPORT — Spaceport / Ground Segment
**Path:** `STK_SPACEPORT/`

**Ownership:** Spaceport interfaces, off-board infrastructure, range constraints

**Primary Responsibilities:**
- Spaceport interface requirements
- Ground segment design
- Range safety coordination
- Launch/landing infrastructure
- Ground support equipment (GSE)
- Emergency response planning

**Primary ATA Chapters:** 80-89 (Infrastructure axis)

---

### STK_CEGT — Circular Economy and Green Tech
**Path:** `STK_CEGT/`

**Ownership:** Circular systems, ESG reporting, alternative technologies, sustainability governance, social responsibility

**Primary Responsibilities:**
- Circular economy strategy and implementation
- ESG (Environmental, Social, Governance) reporting
- Alternative and green technology assessment
- Sustainability governance framework
- Social responsibility programs
- Green tech integration and validation
- Circularity metrics and KPIs

**Primary ATA Chapters:** 85 (Circularity Infrastructure), LC09 integration

---

## Usage Guidelines

### For Stakeholder Representatives

1. **Navigate to your AoR directory**
2. **Review your governance scope** (listed above)
3. **Access your active roadmaps** (link to ROADMAPS/)
4. **Check uncertainty nodes** assigned to your AoR
5. **Use appropriate templates** from INFRASTRUCTURE/templates/
6. **Execute tasks** following KNOTS aligned to your domain
7. **Generate artifacts** with your AoR code in filenames
8. **Produce evidence** and update relevant ledgers

### For Cross-Functional Work

When work spans multiple AoRs:
- **Primary AoR** leads and is named in artifact filename
- **Supporting AoRs** are documented in artifact metadata
- **Handoff points** are defined in roadmap dependencies
- **Evidence** must satisfy all involved AoRs' gates

---

## AoR Constraints (v6.0 Nomenclature)

### Category-AoR Restrictions

The following constraints are enforced by PLC validators:

1. **CATEGORY=SIGNOFF** → AoR must be `STK_CM` or `STK_CERT` only
2. **CATEGORY=EXPORT_CONTROL** → AoR must be `STK_CM` or `STK_CERT` only
3. **TYPE in {BADGE, CERT, LIC}** → AoR must be `STK_CM` or `STK_CERT` only

### AoR Code Registry (Fixed)

The following AoR codes are **configuration-controlled and fixed**:

```
STK_CM, STK_PMO, STK_SE, STK_DAB, STK_PHM, STK_SAF, STK_CERT, 
STK_TEST, STK_OPS, STK_MRO, STK_AI, STK_CY, STK_SPACEPORT, STK_CEGT
```

**No custom or ad-hoc AoR codes are permitted.**

---

## Deprecated Codes

The following AoR codes have been deprecated and unified:

| Deprecated | Replacement | Reason |
|------------|-------------|--------|
| `STK_DATA` | **STK_DAB** | Unified digital AoR |
| `STK_SPE` | **STK_DAB** | Unified digital AoR (Software + Prompting Engineering) |

---

## AoR Interaction Matrix

Common interaction patterns:

- **STK_CM ↔ STK_CERT** — Release governance and compliance evidence
- **STK_SE ↔ STK_DAB** — Architecture definition and digital implementation
- **STK_SE ↔ STK_PHM** — System architecture and physical design
- **STK_SAF ↔ STK_CERT** — Safety case and certification evidence
- **STK_TEST ↔ STK_SE** — V&V planning and execution
- **STK_DAB ↔ STK_AI** — Digital implementation and AI model integration
- **STK_CY ↔ STK_DAB** — Security architecture and digital security
- **STK_OPS ↔ STK_MRO** — Operations and maintenance interfaces
- **STK_SPACEPORT ↔ STK_OPS** — Ground segment and operations coordination
- **STK_CEGT ↔ STK_PMO** — Sustainability strategy and ESG reporting
- **STK_CEGT ↔ STK_DAB** — Green tech integration and circularity ledgers

---

## Portal Navigation

Each AoR entry point provides:

1. **Scope summary** — What this AoR owns and governs
2. **Active roadmaps** — Current work items and deliverables
3. **Uncertainty nodes** — Open questions requiring resolution
4. **Template library** — Artifact templates for this AoR
5. **Validator configs** — PLC validators relevant to this AoR
6. **Evidence requirements** — Mandatory outputs for this domain
7. **Ledger views** — Filtered views of knowledge ledger
8. **Release gates** — Gate criteria this AoR enforces

---

## Governance

- **AoR ownership is binding** — Each artifact must have exactly one primary AoR
- **AoR codes are immutable** — Cannot be changed or extended without CM upgrade
- **AoR accountability is traceable** — All artifacts link back to responsible AoR
- **AoR gates are enforceable** — CI/PR blocks enforce AoR-specific validators

---

## Version

**AoR Structure Version:** 1.0  
**Last Updated:** 2025-12-19

---

## References

- [CAXS Main README](../README.md)
- [v6.0 Nomenclature](../../README.md#92-controlled-vocabulary--nomenclature-v60)
- [AoR Allowlist](../../README.md#929-aor-allowlist-portal-entry-points)
