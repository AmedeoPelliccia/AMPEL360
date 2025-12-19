# ATA — ATA Chapter Organization

## Overview

The **ATA** directory organizes work by **ATA chapters (00-116)**, structured according to the **OPT-INS framework** axes.

ATA (Air Transport Association) chapters provide a standardized numbering system for aerospace documentation, extended by AMPEL360 to cover both AIRT and SPACET systems.

---

## OPT-INS Axis Organization

ATA chapters are organized into five axes:

### O-AXIS — Operations/Organization
**Path:** `O-AXIS/`  
**ATA Range:** 00-05, 18

- ATA-00 — General
- ATA-01 — Operations/Organization Policy (Reserved)
- ATA-02 — Operations/Organization (Reserved)
- ATA-03 — Support Information (Reserved)
- ATA-04 — Airworthiness Limitations/Operational Limits (Reserved)
- ATA-05 — Time Limits/Maintenance Checks
- ATA-18 — Noise & Vibration Management

---

### I-AXIS — Infrastructures
**Path:** `I-AXIS/`  
**ATA Range:** 06-12, 80-89

**Support Operations (06-12):**
- ATA-06 — Dimensions and Areas
- ATA-07 — Lifting and Shoring
- ATA-08 — Leveling and Weighing
- ATA-09 — Towing and Taxiing
- ATA-10 — Parking/Mooring/Storage/Return to Service
- ATA-11 — Placards and Markings
- ATA-12 — Servicing

**Off-board Infrastructure (80-89):**
- ATA-80 — Off-board/Airport/Spaceport Infrastructures (Master)
- ATA-81 — Off-board Energy/Cryo Services
- ATA-82 — Off-board MRO Facilities/Tooling/Logistics
- ATA-83 — Ground Comms/Data Exchange Infra
- ATA-84 — Spaceport Safety/Emergency Response Infra
- ATA-85 — Circularity Infra (Return Flows, Recycling)
- ATA-86 — Off-board Digital Services Platform
- ATA-87 — Identity/Access/Cybersecurity Infra
- ATA-88 — GSE Configuration/Asset Management
- ATA-89 — Test Rigs/Instrumentation Infra (Ground)

---

### T-AXIS — Technology (On-board Systems)
**Path:** `T-AXIS/`  
**ATA Range:** 20-79

**Airframe Systems (20-19):**
- ATA-20 — Standard Practices - Airframe
- ATA-21 — Air Conditioning/Environmental Control
- ATA-22 — Auto Flight/Guidance-Navigation-Control
- ATA-23 — Communications
- ATA-24 — Electrical Power
- ATA-25 — Equipment/Furnishings
- ATA-26 — Fire Protection
- ATA-27 — Flight Controls
- ATA-28 — Fuel/Propellant Systems
- ATA-29 — Hydraulic Power
- ATA-30 — Ice and Rain Protection/Atmospheric Protection
- ATA-31 — Indicating/Recording Systems
- ATA-32 — Landing Gear
- ATA-33 — Lights
- ATA-34 — Navigation
- ATA-35 — Oxygen/Life Support Gas
- ATA-36 — Pneumatic/Gas Distribution
- ATA-37 — Vacuum (if applicable)
- ATA-38 — Water/Waste (Life Support)
- ATA-39 — Electrical/Electronic Panels & Multipurpose Components
- ATA-40 — Multi-System/Integration Services
- ATA-41 — Water Ballast/Mass Trim (if applicable)
- ATA-42 — Integrated Modular Avionics/Compute Platform
- ATA-43 — Reserved/Platform Integration
- ATA-44 — Cabin Systems
- ATA-45 — Central Maintenance System/Health Monitoring
- ATA-46 — Information Systems/Data Networks
- ATA-47 — Inert Gas System/Tank Inerting
- ATA-48 — In-Flight Fuel Dispensing (Reserved)
- ATA-49 — Airborne Auxiliary Power/APU/Aux Power Modules

**Structures (50-59):**
- ATA-50 — Cargo and Accessory Compartments
- ATA-51 — Standard Practices & Structures - General
- ATA-52 — Doors/Hatches
- ATA-53 — Fuselage/Pressure Vessel
- ATA-54 — Nacelles/Pylons (if applicable)
- ATA-55 — Stabilizers/Control Surfaces
- ATA-56 — Windows/Viewports
- ATA-57 — Wings/Lifting Surfaces
- ATA-58 — Reserved/Extension
- ATA-59 — Reserved/Extension

**Propeller/Rotor (60-69):**
- ATA-60 — Standard Practices - Propeller/Rotor
- ATA-61 — Propellers/Propulsors (if applicable)
- ATA-62 — Rotors (if applicable)
- ATA-63 — Rotor Drives (if applicable)
- ATA-64 — Tail Rotor (if applicable)
- ATA-65 — Tail Rotor Drive (if applicable)
- ATA-66 — Folding Blades/Tail Pylon (if applicable)
- ATA-67 — Rotors Flight Control (if applicable)
- ATA-68 — Reserved/Extension
- ATA-69 — Reserved/Extension

**Propulsion (70-79):**
- ATA-70 — Standard Practices - Engine
- ATA-71 — Power Plant/Propulsion Integration
- ATA-72 — Engine (Turbine/Rocket/Hybrid as applicable)
- ATA-73 — Engine Fuel and Control
- ATA-74 — Ignition
- ATA-75 — Air (Bleed/Inlet/APU Air)/Intake
- ATA-76 — Engine Controls
- ATA-77 — Engine Indicating
- ATA-78 — Exhaust/Plume Management
- ATA-79 — Oil/Lubrication

---

### N-AXIS — Neural Networks (AI/ML and Ledgers)
**Path:** `N-AXIS/`  
**ATA Range:** 90-99

- ATA-90 — AI/ML Model Registry & Model Lifecycle
- ATA-91 — Data Schemas/Ontologies/Semantic Model (SSOT)
- ATA-92 — Wiring/Connectivity Graphs & Harness Data Packages
- ATA-93 — Traceability Graph (REQ↔DESIGN↔VV↔OPS) & Evidence Ledgers
- ATA-94 — DPP Core (Digital Product Passport) & Provenance
- ATA-95 — SBOM/SWHW BOM/Model BOM Exports
- ATA-96 — AI Governance (Risk, Assurance, Monitoring, Drift/Bias)
- ATA-97 — Change Impact Analytics (Wiring/Config/Trace)
- ATA-98 — Signed Release Packs/Manifests/Exports
- ATA-99 — Master Registers (Golden Records) & Reference Datasets

---

### S-AXIS — Simulation/Test
**Path:** `S-AXIS/`  
**ATA Range:** 100-116

- ATA-100 — SIM/TEST Governance (Plans, Environments, Quality)
- ATA-101 — Digital Twin Configuration & SIM Model Catalog
- ATA-102 — Scenario Libraries (Mission, Off-nominal, Emergency)
- ATA-103 — SIL (Software-In-The-Loop) Automation
- ATA-104 — HIL (Hardware-In-The-Loop) Benches
- ATA-105 — PIL/Target Execution (Processor/Platform-In-The-Loop)
- ATA-106 — Test Procedures/Test Cases/Acceptance Criteria
- ATA-107 — Test Data/Input Decks/Stimuli
- ATA-108 — Test Results/Reporting/Anomaly Management
- ATA-109 — VV Evidence Packs (Linked to Traceability)
- ATA-110 — Qualification/Environmental Testing (Space-T)
- ATA-111 — System Integration Testing (End-to-End)
- ATA-112 — Mission/Flight Testing (Operational Demos)
- ATA-113 — Uncertainty Quantification (UQ)/Monte Carlo/Sensitivity
- ATA-114 — AI/ML Validation Suites & Monitoring Tests
- ATA-115 — Certification Tests (SW/HW/ECSS-DO) & Compliance Reports
- ATA-116 — SIM/TEST Archives & Baselines (Frozen Campaigns)

---

## Usage Guidelines

### For ATA-based Navigation

1. **Identify your ATA chapter** from the list above
2. **Determine the OPT-INS axis** (O, I, T, N, or S)
3. **Navigate to the axis directory** (e.g., `T-AXIS/`)
4. **Locate the ATA chapter directory** (e.g., `ATA-42/`)
5. **Follow v6.0 nomenclature** with ATA in filename
6. **Align with BLOCK segmentation** within ATA chapter

### For Multi-ATA Work

When work spans multiple ATA chapters:
- **Identify primary ATA** for artifact
- **Document dependencies** on other ATAs
- **Create cross-references** in related ATAs
- **Use traceability graph** to link ATAs

---

## ATA Applicability Matrix

Not all ATAs apply equally to AIRT and SPACET:

- **AIRT+SPACET (common)** — Most ATAs
- **AIRT primary** — ATA 09 (Taxiing), ATA 27 (Flight Controls)
- **SPACET primary** — ATA 84 (Spaceport Safety), ATA 110 (Qualification)
- **Conditional** — Some ATAs depend on configuration

**See ATA_PARTITION_MATRIX.yaml for detailed applicability rules.**

---

## ATA and BLOCK Integration

Within each ATA chapter, work is further segmented by BLOCK:

- **BLOCK-00** — General (applicable to all ATAs)
- **BLOCK-10** — Operational Systems
- **BLOCK-20** — Cybersecurity
- **BLOCK-30** — Data, Comms and Registry
- **BLOCK-40** — Physics
- **BLOCK-50** — Physical
- **BLOCK-60** — Dynamics
- **BLOCK-70** — Reciprocity & Alternative Engines
- **BLOCK-80** — Renewable Energy & Circularity
- **BLOCK-90** — Connections & Mapping

**Example:** ATA-42 (IMA/Compute) might have subdirectories for BLOCK-20 (cyber aspects) and BLOCK-30 (data aspects).

---

## Governance

- **ATA chapters are fixed** — 00-116 range is controlled
- **ATA descriptions are normative** — From main README
- **ATA-to-axis mapping is controlled** — Per OPT-INS framework
- **ATA applicability is CM-controlled** — Per ATA_PARTITION_MATRIX.yaml
- **ATA field in filename is mandatory** — Enforced by validators

---

## Version

**ATA Structure Version:** 1.0  
**Last Updated:** 2025-12-19

---

## References

- [CAXS Main README](../README.md)
- [ATA Allowlist (Main README)](../../README.md#9212-ata-allowlist-00116--canonical-descriptions)
- [OPT-INS Framework](../OPT-INS/README.md)
- [ATA Partition Matrix](../../ATA_PARTITION_MATRIX.yaml)
