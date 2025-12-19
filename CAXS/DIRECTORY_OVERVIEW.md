# CAXS (CA360º) Directory Structure Overview

## Quick Reference

This document provides a high-level overview of the complete CAXS Portal (CA360º) directory structure.

---

## Directory Tree (Top Level)

```
CAXS/
├── AoR/                    # Areas of Responsibility (13 stakeholder entry points)
├── OPT-INS/                # Six canonical axes (O-P-T-I-N-S)
├── KNOTS/                  # Knowledge Nets (K01-K14 controlled process nodes)
├── LIFECYCLE/              # 14 lifecycle phases (LC01-LC14)
├── PROGRAMS/               # AIRT and SPACET program work
├── MODELS/                 # Four model categories (BB, HW, SW, PR)
├── BLOCKS/                 # Ten domain/subsystem segments (00-90)
├── CATEGORIES/             # Six governance categories
├── ATA/                    # ATA chapters 00-116 (organized by OPT-INS axes)
├── INFRASTRUCTURE/         # Supporting tools and systems
├── LEDGERS/                # Evidence and trust fabric
├── VARIANTS/               # Six operating contexts
├── ROADMAPS/               # Structured delivery plans
├── UNCERTAINTY_NODES/      # Pre-defined uncertainty nodes
└── TASK_EXECUTION_SPINE/   # Task-to-artifact lifecycle
```

---

## 1. AoR (Areas of Responsibility)

**14 Stakeholder Entry Points:**

```
AoR/
├── STK_CM/          # Configuration Management
├── STK_PMO/         # Program Management Office
├── STK_SE/          # Systems Engineering
├── STK_DAB/         # Digital Applications & Blockchains
├── STK_PHM/         # Physical & Mechanical Engineering
├── STK_SAF/         # Safety
├── STK_CERT/        # Certification / Compliance
├── STK_TEST/        # Test / V&V
├── STK_OPS/         # Operations
├── STK_MRO/         # Maintenance, Repair & Overhaul
├── STK_AI/          # AI / ML Engineering & Assurance
├── STK_CY/          # Cybersecurity
├── STK_SPACEPORT/   # Spaceport / Ground Segment
└── STK_CEGT/        # Circular Economy and Green Tech
```

**Purpose:** Role-routed portal entry points for stakeholder-specific views

**See:** [AoR/README.md](AoR/README.md)

---

## 2. OPT-INS Framework

**Six Canonical Axes:**

```
OPT-INS/
├── O-OPS-ORG/           # Operations/Organization (ATA 01-05, 18)
├── P-PROGRAM/           # Program governance (ATA 00, 11)
├── T-TECHNOLOGY/        # On-board systems (ATA 20-79)
├── I-INFRASTRUCTURES/   # Off-board/ground (ATA 06-12, 80-89)
├── N-NEURAL_NETWORKS/   # AI/ML/Ledgers (ATA 90-99)
└── S-SIM_TEST/          # Simulation/Test (ATA 100-116)
```

**Purpose:** Information topology organization aligned with ATA chapters

**See:** [OPT-INS/README.md](OPT-INS/README.md)

---

## 3. KNOTS (Knowledge Nets and Ontology as Tasking Strategy)

**14 Controlled Process Nodes:**

```
KNOTS/
├── K01/    # Initial Concept and Problem Definition
├── K02/    # Requirements Capture and Allocation
├── K03/    # Architecture Definition
├── K04/    # Engineering Analysis
├── K05/    # Integration and Testing
├── K06/    # Quality Assurance
├── K07/    # Safety and Security Assurance
├── K08/    # Certification Planning and Execution
├── K09/    # Sustainability and Green Initiatives
├── K10/    # Production and Configuration Management
├── K11/    # Operations Planning and Execution
├── K12/    # Support and Services Delivery
├── K13/    # Maintenance and Sustainment
└── K14/    # Retirement and Circularity
```

**Purpose:** Bridge design thinking to certifiable agentic work

**See:** [KNOTS/README.md](KNOTS/README.md)

---

## 4. LIFECYCLE

**14 Controlled Lifecycle Phases:**

```
LIFECYCLE/
├── LC01-Problem-Statement-Generation-Prompting/
├── LC02-System-Requirements/
├── LC03-Design-Models/
├── LC04-Engineering-Analysis-Calculation/
├── LC05-Integration-Testing-Prototyping/
├── LC06-Quality/
├── LC07-Safety-Security/
├── LC08-Certification-First-Flight/
├── LC09-Green-Aircraft-Baselines/
├── LC10-Industrialization-Serialization-Production/
├── LC11-Operations/
├── LC12-Support-Services/
├── LC13-MRO-Sustainment/
└── LC14-Retirement-Circularity/
```

**Purpose:** Temporal progression from concept to retirement

**See:** [LIFECYCLE/README.md](LIFECYCLE/README.md)

---

## 5. PROGRAMS

**Two Programs, Four Families:**

```
PROGRAMS/
├── AIRT/
│   ├── Q100-PLUS/         # BWB H₂-Electric Aircraft (INTEGRA)
│   └── Q200LR-PLUSULTRA/  # Long-Range Advanced Variant
└── SPACET/
    ├── Q10-PLUS/          # Space Transport Baseline
    └── QHABITAT-PLUSULTRA/ # Habitat-Class Space Vehicle
```

**Purpose:** Program-specific work organization

**See:** [PROGRAMS/README.md](PROGRAMS/README.md)

---

## 6. MODELS

**Four Representational Categories:**

```
MODELS/
├── BB-Body-Brain/    # Physical structure + intelligence integration
├── HW-Hardware/      # Physical components and systems
├── SW-Software/      # Software components and applications
└── PR-Process/       # Process definitions and workflows
```

**Purpose:** Organize work by model type

---

## 7. BLOCKS

**Ten Domain/Subsystem Segments:**

```
BLOCKS/
├── BLOCK-00-GENERAL/
├── BLOCK-10-OPERATIONAL-SYSTEMS/
├── BLOCK-20-CYBERSECURITY/
├── BLOCK-30-DATA-COMMS-REGISTRY/
├── BLOCK-40-PHYSICS/
├── BLOCK-50-PHYSICAL/
├── BLOCK-60-DYNAMICS/
├── BLOCK-70-RECIPROCITY-ALT-ENGINES/
├── BLOCK-80-RENEWABLE-ENERGY-CIRCULARITY/
└── BLOCK-90-CONNECTIONS-MAPPING/
```

**Purpose:** Domain/subsystem segmentation within ATA chapters

---

## 8. CATEGORIES

**Six Governance Intent Classifications:**

```
CATEGORIES/
├── DELIVERABLE/         # Official publishable artifacts
├── EVIDENCE/            # Change note NKUs + proofs
├── REGISTRY/            # SSOT registers, indexes, schemas
├── SIGNOFF/             # Formal approvals (restricted)
├── EXPORT_CONTROL/      # Controlled export packages (restricted)
└── INTERNAL_PRODUCTION/ # Working/internal artifacts
```

**Purpose:** Classify artifacts by governance intent

---

## 9. ATA

**ATA Chapters 00-116 (Organized by OPT-INS Axes):**

```
ATA/
├── O-AXIS/     # ATA 00-05, 18 (Operations/Organization)
│   ├── ATA-00-GENERAL/
│   ├── ATA-01-OPS-ORG-POLICY/
│   ├── ATA-02-OPS-ORG/
│   ├── ATA-03-SUPPORT-INFO/
│   ├── ATA-04-AIRWORTHINESS-LIMITS/
│   ├── ATA-05-TIME-LIMITS-CHECKS/
│   └── ATA-18-NOISE-VIBRATION/
├── I-AXIS/     # ATA 06-12, 80-89 (Infrastructures)
│   ├── ATA-06/ through ATA-12/
│   └── ATA-80/ through ATA-89/
├── T-AXIS/     # ATA 20-79 (Technology/On-board)
│   └── ATA-20/ through ATA-79/
├── N-AXIS/     # ATA 90-99 (Neural Networks/Ledgers)
│   └── ATA-90/ through ATA-99/
└── S-AXIS/     # ATA 100-116 (Simulation/Test)
    └── ATA-100/ through ATA-116/
```

**Purpose:** Standardized aerospace documentation structure

**See:** [ATA/README.md](ATA/README.md)

---

## 10. INFRASTRUCTURE

**Supporting Tools and Systems:**

```
INFRASTRUCTURE/
├── templates/     # Artifact templates aligned to v6.0
├── validators/    # PLC validators (nomenclature, schema, etc.)
├── schemas/       # SSOT schemas and ontologies
├── automation/    # CI/PR automation scripts
├── portals/       # Portal UI components
└── roadmaps/      # Roadmap templates and orchestration
```

**Purpose:** Enable deterministic, validated, auditable execution

**See:** [INFRASTRUCTURE/README.md](INFRASTRUCTURE/README.md)

---

## 11. LEDGERS

**Evidence and Trust Fabric:**

```
LEDGERS/
├── knowledge-ledger/           # Immutable artifact addressing
├── traceability-graph/         # REQ↔DESIGN↔VV↔OPS linkage
├── digital-product-passport/   # Provenance and lifecycle identity
├── sbom-bom/                   # SW/HW/Model BOM exports
├── release-packs/              # Signed manifests and exports
└── master-registers/           # Golden records and vocab
```

**Purpose:** Audit-grade continuity and evidence management

**See:** [LEDGERS/README.md](LEDGERS/README.md)

---

## 12. VARIANTS

**Six Operating Contexts:**

```
VARIANTS/
├── GEN-General/           # General/generic configurations
├── BASELINE/              # Baseline configurations
├── FLIGHT_TEST/           # Flight test configurations
├── CERT-Certification/    # Certification-specific
├── MSN-Mission/           # Mission-specific (numbered)
└── CUST-Customer/         # Customer-specific
```

**Purpose:** Differentiate artifacts by operating context

---

## 13. ROADMAPS

**Structured Delivery Plans:**

```
ROADMAPS/
├── active/       # Currently active roadmaps
├── completed/    # Completed roadmap archives
└── templates/    # Roadmap templates
```

**Purpose:** Organize and track structured delivery plans

---

## 14. UNCERTAINTY_NODES

**Pre-defined Uncertainty Management:**

```
UNCERTAINTY_NODES/
└── (Organized by reduction targets and KNOT alignment)
```

**Purpose:** Track and reduce known unknowns systematically

---

## 15. TASK_EXECUTION_SPINE

**Task-to-Artifact Lifecycle:**

```
TASK_EXECUTION_SPINE/
└── (Execution workflow definitions and tracking)
```

**Purpose:** Enforce deterministic task-to-artifact-to-evidence flow

---

## Navigation Patterns

### By Role (AoR-based)
```
Start → AoR/<your-STK>/ → Review scope → Access roadmaps → Execute tasks
```

### By Technical Domain (ATA-based)
```
Start → OPT-INS/<axis>/ → ATA/<chapter>/ → BLOCK/<segment>/ → Work
```

### By Lifecycle Phase
```
Start → LIFECYCLE/<phase>/ → Align KNOT → Execute → Generate evidence
```

### By Program/Product
```
Start → PROGRAMS/<program>/<family>/ → Select VARIANT → Work
```

---

## v6.0 Nomenclature Integration

All artifacts follow the canonical format:

```
[ATA]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__[SUBJECT]_[CATEGORY]_[TYPE]_[ISSUE-REV]_[STATUS].[EXT]
```

**Key mappings:**
- **ATA** → ATA/ directory
- **PROGRAM/FAMILY** → PROGRAMS/ directory
- **VARIANT** → VARIANTS/ context
- **MODEL** → MODELS/ category
- **BLOCK** → BLOCKS/ segmentation
- **PHASE** → LIFECYCLE/ phase
- **KNOT** → KNOTS/ process node
- **AoR** → AoR/ stakeholder
- **CATEGORY** → CATEGORIES/ intent

---

## Governance Summary

- **Configuration-controlled elements:**
  - AoR codes (13 fixed)
  - KNOT IDs (K01-K14 only)
  - Lifecycle phases (LC01-LC14 only)
  - OPT-INS axes (6 fixed)
  - ATA chapters (00-116 range)
  - PROGRAM/FAMILY matrix
  
- **Validator-enforced:**
  - v6.0 nomenclature compliance
  - Category-AoR constraints
  - KNOT allowlist
  - ATA range
  - Phase codes
  
- **Ledger-tracked:**
  - All artifacts registered
  - All trace links recorded
  - All evidence bundled
  - All releases signed

---

## Quick Start

1. **Identify your entry point:**
   - By role → `AoR/<your-STK>/`
   - By domain → `OPT-INS/<axis>/` → `ATA/<chapter>/`
   - By program → `PROGRAMS/<program>/<family>/`
   - By phase → `LIFECYCLE/<phase>/`

2. **Review documentation:**
   - Read relevant README files
   - Check templates in `INFRASTRUCTURE/templates/`
   - Review active roadmaps in `ROADMAPS/active/`

3. **Execute work:**
   - Use appropriate KNOT process
   - Follow v6.0 nomenclature
   - Generate required evidence
   - Update ledgers

4. **Validate and release:**
   - Run validators from `INFRASTRUCTURE/validators/`
   - Bundle evidence
   - Create release pack
   - Obtain approvals

---

## Total Directory Count

- **15 top-level directories**
- **13 AoR directories**
- **6 OPT-INS axis directories**
- **14 KNOT directories**
- **14 LIFECYCLE directories**
- **117 ATA directories** (00-116)
- **10 BLOCK directories**
- **6 CATEGORY directories**
- **4 MODEL directories**
- **6 VARIANT directories**
- **6 INFRASTRUCTURE subdirectories**
- **6 LEDGER subdirectories**
- **Plus program-specific and support directories**

**Total: 200+ directories** providing comprehensive structure

---

## Version

**Directory Structure Version:** 1.0  
**Last Updated:** 2025-12-19

---

## References

- [CAXS Main README](README.md) — Detailed CAXS overview
- [AMPEL360 Main README](../README.md) — Overall framework
- Individual directory READMEs for detailed information
