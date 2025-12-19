# OPT-INS Framework — Six Canonical Axes

## Overview

The **OPT-INS framework** defines six canonical axes for information topology, organizing all AMPEL360 work into coherent domains aligned with ATA chapters and stakeholder responsibilities.

---

## OPT-INS Axes

### O — O-OPS-ORG (Operations / Organization)
**Path:** `O-OPS-ORG/`

**ATA Range:** 01–05, 18  
**Applicability:** AIRT+SPACET

**Description:** Operations / Organization policy and governance

**Key Topics:**
- Organizational policies
- Operational procedures
- Support information
- Airworthiness limitations
- Time limits and maintenance checks
- Noise and vibration management

**Primary AoRs:** STK_PMO, STK_OPS, STK_CM

---

### P — P-PROGRAM (Program Governance)
**Path:** `P-PROGRAM/`

**ATA Range:** 00, 11  
**Applicability:** AIRT+SPACET

**Description:** Program governance, baselines, registers

**Key Topics:**
- General program information
- Placards and markings
- Configuration baselines
- Program registers
- Master planning

**Primary AoRs:** STK_PMO, STK_CM

---

### T — T-TECHNOLOGY (On-board Systems)
**Path:** `T-TECHNOLOGY/`

**ATA Range:** 20–79  
**Applicability:** AIRT+SPACET

**Description:** On-board vehicle systems and subsystems

**Key Topics:**
- Airframe systems
- Avionics and electrical
- Propulsion systems
- Structures
- Flight controls
- Environmental control
- All on-board technology

**Primary AoRs:** STK_PHM, STK_SE, STK_DAB

---

### I — I-INFRASTRUCTURES (Off-board / Ground)
**Path:** `I-INFRASTRUCTURES/`

**ATA Range:** 06–12, 80–89  
**Applicability:** AIRT+SPACET

**Description:** Off-board / ground infrastructure

**Key Topics:**
- Dimensions and areas
- Lifting and shoring
- Servicing
- Spaceport infrastructure
- Ground support equipment
- Off-board energy and cryo services
- MRO facilities
- Digital services platforms
- Test rigs and instrumentation

**Primary AoRs:** STK_SPACEPORT, STK_MRO, STK_DAB

---

### N — N-NEURAL_NETWORKS (AI/ML and Digital Ledgers)
**Path:** `N-NEURAL_NETWORKS/`

**ATA Range:** 90–99  
**Applicability:** AIRT+SPACET

**Description:** AI/ML, schemas, traceability, DPP, ledgers

**Key Topics:**
- AI/ML model registry (ATA 90)
- Data schemas and ontologies (ATA 91)
- Wiring/connectivity graphs (ATA 92)
- Traceability graph (ATA 93)
- Digital Product Passport (ATA 94)
- SBOM/BOM exports (ATA 95)
- AI governance (ATA 96)
- Change impact analytics (ATA 97)
- Signed release packs (ATA 98)
- Master registers (ATA 99)

**Primary AoRs:** STK_DAB, STK_AI, STK_CM

---

### S — S-SIM_TEST (Simulation and Testing)
**Path:** `S-SIM_TEST/`

**ATA Range:** 100–116  
**Applicability:** AIRT+SPACET

**Description:** Simulation, test, V&V evidence

**Key Topics:**
- SIM/TEST governance (ATA 100)
- Digital twin catalog (ATA 101)
- Scenario libraries (ATA 102)
- SIL automation (ATA 103)
- HIL benches (ATA 104)
- PIL execution (ATA 105)
- Test procedures (ATA 106)
- Test data (ATA 107)
- Test results (ATA 108)
- VV evidence packs (ATA 109)
- Qualification testing (ATA 110)
- System integration testing (ATA 111)
- Mission/flight testing (ATA 112)
- Uncertainty quantification (ATA 113)
- AI/ML validation (ATA 114)
- Certification tests (ATA 115)
- Archives and baselines (ATA 116)

**Primary AoRs:** STK_TEST, STK_SE, STK_DAB

---

## OPT-INS Usage

### For Domain Navigation

1. **Identify your domain** — Which axis (O-P-T-I-N-S)?
2. **Navigate to axis directory** — OPT-INS/<axis>/
3. **Locate specific ATA chapter** — Within axis scope
4. **Review domain requirements** — Templates and validators
5. **Execute work** — Following axis-specific patterns

### For Cross-Domain Work

When work spans multiple axes:
- **Identify primary axis** for the work
- **Document dependencies** on other axes
- **Coordinate with relevant AoRs** for each axis
- **Generate evidence** satisfying all axes involved

---

## OPT-INS and ATA Integration

The OPT-INS framework organizes ATA chapters into coherent groupings:

```
O-AXIS: ATA 01-05, 18
P-AXIS: ATA 00, 11
T-AXIS: ATA 20-79
I-AXIS: ATA 06-12, 80-89
N-AXIS: ATA 90-99
S-AXIS: ATA 100-116
```

This organization:
- **Reduces complexity** by grouping related chapters
- **Clarifies ownership** by aligning with AoRs
- **Enables navigation** through logical domains
- **Supports governance** with axis-specific rules

---

## OPT-INS and Blocks

The OPT-INS axes cross-cut with BLOCK segmentation:

- **Blocks** provide domain/subsystem segmentation within chapters
- **Axes** provide high-level topological organization
- **Together** they create a matrix for precise artifact placement

Example:
- **ATA 42** (IMA/Compute Platform) is in **T-AXIS** (on-board)
- Within ATA 42, **BLOCK-20** focuses on **CYBERSECURITY** aspects
- Within ATA 42, **BLOCK-30** focuses on **DATA/COMMS** aspects

---

## Governance

- **OPT-INS axes are fixed** — O-P-T-I-N-S only
- **ATA assignments to axes are controlled** — Per ATA_PARTITION_MATRIX.yaml
- **Axis scope is normative** — Cannot be changed without CM approval

---

## Version

**OPT-INS Structure Version:** 1.0  
**Last Updated:** 2025-12-19

---

## References

- [CAXS Main README](../README.md)
- [OPT-INS Framework (Main README)](../../README.md#7-opt-ins-framework)
- [ATA Partition Matrix](../../ATA_PARTITION_MATRIX.yaml)
- [ATA Directory](../ATA/README.md)
