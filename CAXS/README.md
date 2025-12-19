# CAXS Portal (CA360º) Directory Structure

## Overview

**CAXS Portal (CA360º)** is the **unified digital lifecycle architecture portal** for AMPEL360 that organizes all navigation and work execution around **AoR entry points (STKs)** and **stakeholder roles**.

**CA360º** = **C**onfiguration **A**rchitecture **360°** - providing full-circle lifecycle closure from design through operations and back.

---

## Purpose

The CAXS Portal provides:

- **Role-correct navigation** (stakeholder-specific, AoR-accountable)
- **Enforceable governance** (validators, CI gates, controlled KNOTS)
- **Traceable delivery** (task → artifact → evidence → release)
- **Accelerated integration** of new technology through reusable, validated knowledge capsules

---

## Directory Structure

### 1. AoR (Areas of Responsibility)
**Path:** `AoR/`

Contains **14 stakeholder entry points**, each representing a primary Area of Responsibility (AoR) with specific ownership boundaries:

- **STK_CM** — Configuration Management
- **STK_PMO** — Program Management Office
- **STK_SE** — Systems Engineering
- **STK_DAB** — Digital Applications & Blockchains
- **STK_PHM** — Physical & Mechanical Engineering
- **STK_SAF** — Safety
- **STK_CERT** — Certification / Compliance
- **STK_TEST** — Test / V&V
- **STK_OPS** — Operations
- **STK_MRO** — Maintenance, Repair & Overhaul
- **STK_AI** — AI / ML Engineering & Assurance
- **STK_CY** — Cybersecurity
- **STK_SPACEPORT** — Spaceport / Ground Segment
- **STK_CEGT** — Circular Economy and Green Tech

Each AoR directory serves as a **portal entry point** exposing:
- Scope (what this AoR owns)
- Canonical ATA roots / domains it governs
- Active roadmaps and open uncertainty nodes
- Mandatory artifacts, evidence, and release gates

---

### 2. OPT-INS Framework
**Path:** `OPT-INS/`

Six canonical axes for information topology:

- **O-OPS-ORG** — Operations / Organization policy and governance (ATA 01-05, 18)
- **P-PROGRAM** — Program governance, baselines, registers (ATA 00, 11)
- **T-TECHNOLOGY** — On-board vehicle systems and subsystems (ATA 20-79)
- **I-INFRASTRUCTURES** — Off-board / ground infrastructure (ATA 06-12, 80-89)
- **N-NEURAL_NETWORKS** — AI/ML, schemas, traceability, DPP, ledgers (ATA 90-99)
- **S-SIM_TEST** — Simulation, test, V&V evidence (ATA 100-116)

---

### 3. KNOTS (Knowledge Nets and Ontology as Tasking Strategy)
**Path:** `KNOTS/`

Contains **14 controlled process nodes (K01-K14)** that bridge:
- MBSE/SysML architecture (requirements, behavior, structure, interfaces)
- Agentic execution (task decomposition, automation, prompting/tooling)
- Configuration control (traceability, naming standard, release packs)
- Certification evidence (VV packs, audit queries, signed manifests)

Each KNOT defines:
- What knowledge must exist (ontology commitments)
- How it must connect (knowledge net interfaces)
- What tasks agents may execute (tasking strategy)
- What evidence must be produced (compliance-ready outputs)

**KNOT IDs are configuration-controlled:** K01..K14 only (with optional `-T###` suffix)

---

### 4. LIFECYCLE
**Path:** `LIFECYCLE/`

Contains **14 controlled lifecycle phases (LC01-LC14)**:

- **LC01** — Problem Statement / Generation / Prompting Engineering
- **LC02** — System Requirements
- **LC03** — Design Models
- **LC04** — Engineering Analysis & Calculation Models
- **LC05** — Integration Testing & Prototyping (V&V / V6V)
- **LC06** — Quality
- **LC07** — Safety and Security
- **LC08** — Certification and First Flight
- **LC09** — Green Aircraft / Baselines
- **LC10** — Industrialization / Serialization / Production Plan / CM
- **LC11** — Operations
- **LC12** — Support and Services
- **LC13** — MRO and Sustainment
- **LC14** — Retirement Management and Circularity

---

### 5. PROGRAMS
**Path:** `PROGRAMS/`

Program-specific work organized by:

**AIRT** (Advanced Air Transport):
- Q100-PLUS — BWB H₂-Electric Aircraft (INTEGRA)
- Q200LR-PLUSULTRA — Long-Range Advanced Variant

**SPACET** (Space Transport):
- Q10-PLUS — Space Transport Baseline
- QHABITAT-PLUSULTRA — Habitat-Class Space Vehicle

---

### 6. MODELS
**Path:** `MODELS/`

Four representational categories:

- **BB-Body-Brain** — Physical structure + intelligence integration
- **HW-Hardware** — Physical components and systems
- **SW-Software** — Software components and applications
- **PR-Process** — Process definitions and workflows

---

### 7. BLOCKS
**Path:** `BLOCKS/`

Ten domain/subsystem segmentation categories:

- **BLOCK-00** — GENERAL (Implicit/Universal)
- **BLOCK-10** — OPERATIONAL SYSTEMS
- **BLOCK-20** — CYBERSECURITY
- **BLOCK-30** — DATA, COMMS AND REGISTRY
- **BLOCK-40** — PHYSICS (pressure/thermal/cryo/…)
- **BLOCK-50** — PHYSICAL (aerostructures + information HW)
- **BLOCK-60** — DYNAMICS (thrust, drag-lift, balancing, attitude, inerting)
- **BLOCK-70** — RECIPROCITY & ALTERNATIVE ENGINES
- **BLOCK-80** — RENEWABLE ENERGY & CIRCULARITY
- **BLOCK-90** — CONNECTIONS & MAPPING

---

### 8. CATEGORIES
**Path:** `CATEGORIES/`

Governance intent classification:

- **DELIVERABLE** — Official publishable artifact (one official chain)
- **EVIDENCE** — Change note NKUs + proofs (many allowed)
- **REGISTRY** — SSOT registers, indexes, catalogs, schemas, ontologies
- **SIGNOFF** — Formal approvals / signature records (restricted)
- **EXPORT_CONTROL** — Controlled export/disclosure packages (restricted)
- **INTERNAL_PRODUCTION** — Working/internal production artifacts (hidden by default)

---

### 9. ATA Chapters
**Path:** `ATA/`

Organized by OPT-INS axes, covering **ATA 00-116**:

- **O-AXIS** — ATA 00-05, 18 (Operations/Organization)
- **I-AXIS** — ATA 06-12, 80-89 (Infrastructures)
- **T-AXIS** — ATA 20-79 (Technology/On-board systems)
- **N-AXIS** — ATA 90-99 (Neural Networks/AI/ML/Ledgers)
- **S-AXIS** — ATA 100-116 (Simulation/Test)

---

### 10. INFRASTRUCTURE
**Path:** `INFRASTRUCTURE/`

Supporting tools and systems:

- **templates** — Artifact templates aligned to v6.0 nomenclature
- **validators** — PLC validators (nomenclature, identifiers, schema integrity)
- **schemas** — SSOT schemas and ontologies
- **automation** — CI/PR automation scripts
- **portals** — Portal UI components and configurations
- **roadmaps** — Roadmap templates and orchestration configs

---

### 11. LEDGERS
**Path:** `LEDGERS/`

Evidence and trust fabric (audit-grade continuity):

- **knowledge-ledger** — Immutable artifact addressing (repo path + sha256)
- **traceability-graph** — REQ ↔ DESIGN ↔ V&V ↔ OPS linkage
- **digital-product-passport** — Provenance, materials, lifecycle identity
- **sbom-bom** — Dependency integrity for SW/HW/Model compositions
- **release-packs** — Manifests, exports, PR-blocking compliance evidence
- **master-registers** — Golden records and controlled vocabulary datasets

---

### 12. VARIANTS
**Path:** `VARIANTS/`

Operating context variants:

- **GEN-General** — General/generic configurations
- **BASELINE** — Baseline configurations
- **FLIGHT_TEST** — Flight test configurations
- **CERT-Certification** — Certification-specific configurations
- **MSN-Mission** — Mission-specific configurations
- **CUST-Customer** — Customer-specific configurations

---

### 13. ROADMAPS
**Path:** `ROADMAPS/`

Structured delivery plans:

- **active** — Currently active roadmaps
- **completed** — Completed roadmap archives
- **templates** — Roadmap templates

Each roadmap:
- Is **identified** (ID + scope + owner AoR)
- Decomposes into **tasks** aligned to KNOTS (K01..K14)
- Produces **controlled artifacts** using v6.0 naming standard
- Requires **evidence outputs** (validator logs, link-check logs, test results)
- Aggregates results into **knowledge ledger** for audit and reuse

---

### 14. UNCERTAINTY_NODES
**Path:** `UNCERTAINTY_NODES/`

Pre-defined uncertainty nodes that are actively reduced by work:
- Each node has a measurable "unknown → known" target
- Each task must produce artifacts that **reduce uncertainty**
- Successful closure is recorded as **evidence-backed ledger entries**

---

### 15. TASK_EXECUTION_SPINE
**Path:** `TASK_EXECUTION_SPINE/`

Task-to-artifact lifecycle execution spine:

1. **Select entry point (AoR)** → determines authority, templates, and gates
2. **Bind to an uncertainty node + KNOT (K01..K14)** → defines permitted actions
3. **Generate/modify artifacts** under v6.0 nomenclature → NKU implicit
4. **Run PLC validators and link-check** → PR-blocking evidence
5. **Register exceptions (if any)** → CM-controlled register diff
6. **Update ledger** (paths + hashes + relations) → audit-ready trace graph
7. **Package release** (signed manifests / export packs) → certification/ops readiness

---

## v6.0 Nomenclature

All artifacts in CAXS follow the **v6.0 nomenclature standard**:

```
[ATA]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__[SUBJECT]_[CATEGORY]_[TYPE]_[ISSUE-REV]_[STATUS].[EXT]
```

**Key rules:**
- Double-underscore `__` is mandatory before SUBJECT
- No KNOT outside K01..K14 may appear anywhere in filename
- AoR must be one allowlisted STK token
- BLOCK is domain segmentation, not lifecycle (LC stays in PHASE)

---

## Navigation Guidelines

### For Stakeholders (Role-based Entry)
1. Start at your **AoR entry point** (`AoR/STK_*/`)
2. Review your **active roadmaps** and **uncertainty nodes**
3. Access **templates** and **validators** from `INFRASTRUCTURE/`
4. Execute tasks using the **TASK_EXECUTION_SPINE**
5. Generate artifacts following **v6.0 nomenclature**
6. Produce evidence and update **ledgers**

### For Technical Domains (ATA-based Entry)
1. Navigate to appropriate **OPT-INS axis** (`OPT-INS/`)
2. Locate specific **ATA chapter** (`ATA/`)
3. Access **BLOCK** segmentation for domain-specific work
4. Follow **lifecycle phase** progression (`LIFECYCLE/`)
5. Align with **KNOTS** for task execution

### For Program/Product Work
1. Start at **PROGRAMS/** (AIRT or SPACET)
2. Select **FAMILY** (Q100, Q200LR, Q10, QHABITAT)
3. Choose **VARIANT** context (GEN, BASELINE, FLIGHT_TEST, etc.)
4. Execute work through appropriate **AoR** and **KNOT**

---

## Integration with AMPEL360

CAXS Portal (CA360º) is the **execution platform** pillar of AMPEL360, binding:

- **A (Aerospace)** — Domain scope via ATA/OPT-INS
- **M (Models)** — Representational layer via MODELS/
- **P (Platforms)** — Execution infrastructure (this portal)
- **E (Evolution)** — Temporal governance via LIFECYCLE/ and UNCERTAINTY_NODES/
- **L (Ledgers)** — Evidence fabric via LEDGERS/

Together, these provide **360° integration** — full-circle lifecycle closure where every artifact produced feeds the ledger, reduces uncertainty, and is reusable across cycles.

---

## Getting Started

1. **Identify your role** → Find your AoR entry point
2. **Review README in your AoR directory** → Understand your scope
3. **Check active roadmaps** → See what work is planned
4. **Access templates** → Use standardized artifact templates
5. **Execute tasks** → Follow TASK_EXECUTION_SPINE
6. **Generate evidence** → Document and validate your work
7. **Update ledgers** → Contribute to the knowledge graph

---

## Governance

- **All KNOT IDs (K01-K14) are configuration-controlled** — No new KNOTs without CM approval
- **All AoR codes are fixed** — No custom stakeholder codes
- **All lifecycle phases (LC01-LC14) are normative** — Meanings must not be repurposed
- **All filenames must follow v6.0 nomenclature** — Enforced by PLC validators
- **All evidence must be trace-linked** — Recorded in knowledge ledger
- **All releases must be signed and manifested** — PR-blocking requirement

---

## Version

**CAXS Directory Structure Version:** 1.0  
**AMPEL360 Framework Version:** As per main README.md  
**Nomenclature Version:** v6.0  
**Last Updated:** 2025-12-19

---

## References

- [AMPEL360 Main README](../README.md)
- [ATA Partition Matrix](../ATA_PARTITION_MATRIX.yaml)
- [v6.0 Nomenclature Standard](../README.md#92-controlled-vocabulary--nomenclature-v60)
- [KNOTS Definition](../README.md#6-knots--knowledge-nets-and-ontology-as-tasking-strategy)
- [OPT-INS Framework](../README.md#7-opt-ins-framework)

---

## Support

For questions about:
- **Directory structure** → Contact STK_CM
- **Portal navigation** → Contact STK_DAB
- **Roadmaps and planning** → Contact STK_PMO
- **Technical content** → Contact relevant STK owner
