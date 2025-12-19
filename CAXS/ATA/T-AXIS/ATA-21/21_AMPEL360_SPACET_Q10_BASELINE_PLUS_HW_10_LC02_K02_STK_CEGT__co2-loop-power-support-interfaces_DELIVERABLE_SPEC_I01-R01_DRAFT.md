---
document_id: "21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC02_K02_STK_CEGT__co2-loop-power-support-interfaces_DELIVERABLE_SPEC_I01-R01_DRAFT"
title: "CO₂ Loop Power Support Interface Specification — SPACET Q10 BASELINE PLUS"
project: "AMPEL360"
program: "SPACET"
family: "Q10"
variant: "BASELINE"
version: "PLUS"
ata: "21"
ata_description: "Air Conditioning/Environmental Control"
model: "HW"
block: "10"
block_description: "Operational Systems"
phase: "LC02"
phase_description: "System Requirements"
knot: "K02"
scope: "Interface requirements for CO₂ capture system integrated with CO₂-battery energy storage module (power support only, closed loop)"
owner_aor: "STK_CEGT"
interfaces:
  required: ["STK_SE", "STK_PHM", "STK_CERT", "STK_CM"]
  optional: ["STK_SAF", "STK_TEST"]
category: "DELIVERABLE"
type: "SPEC"
status: "DRAFT"
issue_rev: "I01-R01"
---

# CO₂ Loop Power Support Interface Specification — SPACET Q10 BASELINE PLUS

## 1. Purpose and Scope

This specification defines the **interface requirements and operating boundaries** for the integrated CO₂ capture and CO₂-battery energy storage system for **SPACET Q10 BASELINE PLUS**.

**Key architectural principle**: The system operates in two **closed loops** with **power support only** (bidirectional electrical interface), with **no propulsive thrust** and **no net mass ejection**.

### 1.1 Document Authority

This specification is the **Single Source of Truth (SSOT)** for:
- CO₂ loop claim boundary ("power support only, no thrust")
- Bidirectional power interface envelope (ATA-21 ↔ ATA-24)
- Thermal interface envelope and heat rejection requirements
- Operational modes and control authority
- Safety and isolation requirements

**Interface Control Authority**: Requirements defined in this specification shall not be relaxed or modified without formal change control through **STK_CM** and compliance acceptance by **STK_CERT**.

---

## 2. Applicable Documents

### 2.1 Parent Requirements
- `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC02_K02_STK_SE__env-control-system-requirements_DELIVERABLE_REQ_I01-R01_ACTIVE.md`
  - REQ-ECS-ATM-005 (CO₂ partial pressure limits)
  - REQ-ECS-PWR-BIDIR-001, REQ-ECS-PWR-RT-001, REQ-ECS-PWR-MODE-001, REQ-ECS-PWR-CLAIM-001
  - REQ-ECS-SAF-CO2-001, REQ-ECS-SAF-CO2-002

### 2.2 Supporting Analysis
- `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_10_LC04_K04-T010_STK_CEGT__co2-loop-energy-balance_DELIVERABLE_RPT_I01-R01_DRAFT.md` (Energy Balance Report)
- `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC04_K04-T011_STK_PHM__co2-loop-thermal-envelope_DELIVERABLE_RPT_I01-R01_DRAFT.md` (Thermal Envelope Report)

### 2.3 Standards
- ECSS-E-ST-50C: Space Engineering - Thermal Control
- NASA-STD-3001: NASA Space Flight Human-System Standard
- IEC 62040: Uninterruptible Power Systems (UPS) standards (for bidirectional power interface design patterns)

---

## 3. System Architecture and Claim Boundary

### 3.1 Two-Loop Architecture (Normative)

The CO₂ capture and energy storage system operates as **two independent closed loops**:

#### 3.1.1 Air Loop (ECS — Habitability)
```
Cabin Atmosphere → CO₂ Capture → CO₂ Buffer Storage → 
Regeneration/Desorption → Return to Cabin (closed)
```
**Purpose**: Maintain cabin CO₂ partial pressure within limits per REQ-ECS-ATM-005.

**Mass flow**: Closed loop — no CO₂ ejected to space.

#### 3.1.2 Energy Loop (CO₂-Battery — Power Support)
```
ATA-24 Electrical Bus ↔ CO₂-Battery Module (charge/discharge) ↔ 
Internal CO₂ State Change (energy storage) ↔ ATA-24 Electrical Bus (closed)
```
**Purpose**: Energy storage and management for peak shaving, load leveling, and resilience.

**Energy flow**: Bidirectional electrical interface with ATA-24. Internal CO₂ used as storage medium but remains within module (closed loop).

### 3.2 Claim Boundary (Compliance-Critical)

**CLAIM**: The CO₂-battery module is an **energy storage and management device** providing **power support** to the vehicle electrical system (ATA-24). It is **NOT** an energy source and does **NOT** provide propulsive thrust.

**Characteristics**:
1. **Bidirectional electrical interface**: Can charge from ATA-24 and discharge to ATA-24
2. **Energy storage**: Stores energy using internal CO₂ state changes (e.g., phase change, pressure/temperature variation)
3. **Closed system**: All CO₂ remains within the module; no mass ejection
4. **Thermal management**: Heat rejection required for charge/discharge cycles
5. **Finite capacity**: Cannot produce more energy than stored; round-trip efficiency <100%

**Verification basis**: Energy balance analysis (see Section 5) demonstrates net energy consumption over full operational cycle, confirming storage/management function only.

---

## 4. Interface Requirements

### 4.1 Electrical Power Interface (ATA-21 ↔ ATA-24)

#### 4.1.1 Power Envelope

**IF-PWR-001**: The CO₂-battery module shall interface with ATA-24 vehicle electrical power system with the following bidirectional power envelope:

| Parameter | Charge Mode | Discharge Mode |
|-----------|-------------|----------------|
| Continuous Power | 2.0 kW max | 1.5 kW max |
| Peak Power | — | 2.5 kW (≤60s) |
| Voltage Range | Per ATA-24 bus spec | Per ATA-24 bus spec |
| Current Limit | 10 A continuous | 12 A continuous, 20 A peak |
| Power Factor | ≥0.95 | ≥0.95 |

**IF-PWR-002**: Power ramp rate shall not exceed 0.5 kW/s during mode transitions to prevent bus transients.

**IF-PWR-003**: Inrush current during connection shall not exceed 20 A for duration ≤100 ms.

#### 4.1.2 Bus Interface Characteristics

**IF-PWR-011**: The module shall comply with ATA-24 bus voltage and frequency specifications (TBD: specify DC bus voltage range or AC characteristics).

**IF-PWR-012**: Total Harmonic Distortion (THD) shall not exceed 5% during discharge mode operation.

**IF-PWR-013**: Power quality ripple shall remain within ±2% of nominal voltage under all operating modes.

#### 4.1.3 Protection and Control

**IF-PWR-021**: The module shall implement overcurrent protection (OCP), overvoltage protection (OVP), and short-circuit protection with isolation capability within 10 ms of fault detection.

**IF-PWR-022**: The module shall respond to discrete load shedding commands from ATA-24 Electrical Power System (EPS) with:
- Command acknowledgment: ≤100 ms
- Load reduction complete: ≤500 ms
- Shedding priority levels: Normal operation (lowest priority), Essential ECS functions (higher priority)

**IF-PWR-023**: The module shall provide electrical isolation capability (disconnect/contactor) commandable by EPS or autonomously upon internal fault detection.

### 4.2 Thermal Interface

#### 4.2.1 Heat Rejection Envelope

**IF-THM-001**: The CO₂-battery module shall reject heat to the vehicle thermal management system (ATA-21 thermal bus) with the following envelope:

| Operating Mode | Thermal Load (kW) | Temperature Range |
|----------------|-------------------|-------------------|
| Charge (2.0 kW) | 0.6 kW avg | 15-35°C inlet |
| Discharge (1.5 kW) | 0.4 kW avg | 15-35°C inlet |
| Peak Discharge (2.5 kW) | 0.8 kW peak (≤60s) | 15-35°C inlet |
| Standby | 0.05 kW | 15-35°C inlet |

**IF-THM-002**: Heat rejection interface shall use vehicle thermal control fluid loop or cold plate mounting per mechanical interface specification (TBD: ICD reference).

**IF-THM-003**: Module internal temperature shall remain within operational limits (TBD: specify based on CO₂-battery technology) with thermal management system active. Overtemperature protection shall initiate load reduction or shutdown as required for safety.

#### 4.2.2 Thermal Transients

**IF-THM-011**: Thermal transient response during mode changes shall not exceed thermal interface capacity. Thermal mass and control algorithms shall limit thermal shock to vehicle thermal system.

### 4.3 CO₂ Fluidic Interface (Air Loop ↔ CO₂ Capture)

#### 4.3.1 CO₂ Flow Characteristics

**IF-CO2-001**: The CO₂ capture subsystem shall interface with cabin atmosphere with the following characteristics:

| Parameter | Value |
|-----------|-------|
| CO₂ Capture Rate (nominal) | ≥1.0 kg/day/person |
| Inlet Air Flow Rate | TBD (based on capture technology) |
| CO₂ Concentration (inlet) | 0.3-0.6 kPa partial pressure |
| CO₂ Concentration (outlet) | <0.05 kPa partial pressure |
| Operating Pressure | 70-101 kPa cabin pressure |

**IF-CO2-002**: CO₂ buffer storage capacity shall accommodate minimum 2 hours of peak CO₂ generation with margin per REQ-ECS-CO2-BUF-001.

**IF-CO2-003**: Regeneration/desorption cycle shall return captured CO₂ to buffer storage (closed loop). No CO₂ venting to space permitted during nominal operations.

#### 4.3.2 Isolation and Safety

**IF-CO2-011**: The CO₂ capture and buffer subsystems shall include isolation valving with automatic closure capability upon:
- Overpressure detection (>150% nominal operating pressure)
- Leak detection (cabin CO₂ rate of change exceeds threshold)
- Loss of control power or communication
- Manual command from crew or ground control

**IF-CO2-012**: All pressure vessels and CO₂ storage components shall be designed and certified per applicable pressure vessel standards with safety factors per space systems requirements.

### 4.4 Control and Data Interface

#### 4.4.1 Command Interface

**IF-CTRL-001**: The CO₂-battery module shall accept discrete commands from vehicle control system (ATA-42) and EPS (ATA-24):
- Mode selection: Charge, Discharge, Standby, Isolation
- Shedding commands: Normal, Reduced, Emergency Shutdown
- Manual override: Crew-commanded isolation

**IF-CTRL-002**: Command response time shall be ≤100 ms for acknowledgment, with commanded state achieved within specified transition times per operating mode.

#### 4.4.2 Telemetry Interface

**IF-CTRL-011**: The module shall provide real-time telemetry to vehicle data network (ATA-46):
- State of Charge (SOC): 0-100%, ±2% accuracy, 1 Hz update rate
- Power flow: Charge/discharge power (kW), ±5% accuracy, 1 Hz update rate
- Thermal status: Module temperature, coolant flow/temperature, 1 Hz update rate
- Health status: Fault flags, warning flags, operational mode, 1 Hz update rate
- CO₂ subsystem status: Pressure, flow rate, capture efficiency (if instrumented), 0.1 Hz update rate

**IF-CTRL-012**: Caution and warning (C&W) signals shall be provided for:
- High/low state of charge
- Overtemperature
- Overpressure
- Electrical fault conditions
- Loss of thermal management

#### 4.4.3 Health Monitoring

**IF-CTRL-021**: The module shall implement Built-In Test (BIT) capability for autonomous fault detection and isolation (FDI) with maintenance reporting to Central Maintenance System (ATA-45).

---

## 5. Operational Modes

### 5.1 Normal Mode

**MODE-NORMAL-001**: In Normal mode, the CO₂-battery module charges from ATA-24 when excess power is available and discharges on demand to support peak power events or load leveling.

**MODE-NORMAL-002**: State of Charge (SOC) management:
- Charge when SOC <80% and ATA-24 capacity available
- Discharge when ATA-24 requests load support or SOC >20%
- Maintain SOC in 40-80% range for optimal cycle life when possible

### 5.2 Peak Shaving Mode

**MODE-PEAK-001**: Module automatically discharges during vehicle peak power events to reduce instantaneous EPS loading, per ATA-24 load management strategy.

**MODE-PEAK-002**: Peak shaving activation triggered by EPS power demand exceeding threshold (TBD: specify threshold or reference EPS specification).

### 5.3 Degraded Mode

**MODE-DEG-001**: In Degraded mode, module operates with reduced capacity due to:
- Reduced State of Health (SOH <80% of nominal capacity)
- Thermal management capacity reduction
- Partial failure of redundant components (if applicable)

**MODE-DEG-002**: Performance limits in Degraded mode:
- Charge/discharge power reduced by proportional factor
- State of charge operating range may be restricted
- Thermal limits may be reduced

**MODE-DEG-003**: Transition to Degraded mode requires crew notification and ground review for continued operations or maintenance action.

### 5.4 Shedding Mode

**MODE-SHED-001**: Upon receipt of load shedding command from EPS, module shall:
1. Acknowledge command (≤100 ms)
2. Cease discharge if active
3. Reduce charge power to minimum or zero per command level
4. Achieve commanded state within 500 ms

**MODE-SHED-002**: Shedding priority levels:
- Level 1 (Normal operations): Reduce charge power by 50%
- Level 2 (Essential loads only): Cease charge, standby mode
- Level 3 (Emergency): Electrical isolation

### 5.5 Isolation Mode

**MODE-ISO-001**: Isolation mode electrically and fluidically isolates the module from vehicle systems. Entered by:
- Manual crew/ground command
- Automatic fault response per safety requirements
- EPS emergency shedding command (Level 3)

**MODE-ISO-002**: In Isolation mode:
- All electrical contactors open
- CO₂ isolation valves close
- Internal monitoring remains active if safe to do so
- Module enters safe state with thermal management as required

---

## 6. Energy Balance and Verification Basis

### 6.1 Energy Storage Function (Normative Claim Support)

**ENERGY-001**: The CO₂-battery module functions as an energy storage device. Energy balance over full operational cycle demonstrates:
- Energy input (charge from ATA-24) > Energy output (discharge to ATA-24)
- Round-trip efficiency = (Energy out) / (Energy in) <100%
- No external energy source; all discharged energy previously charged from ATA-24

**ENERGY-002**: Detailed energy balance analysis documented in:
`21_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_10_LC04_K04-T010_STK_CEGT__co2-loop-energy-balance_DELIVERABLE_RPT_I01-R01_DRAFT.md`

### 6.2 Closed Loop Verification

**CLOSED-001**: CO₂ mass balance over operational cycle:
- All CO₂ captured from cabin returns to cabin (via regeneration or buffer release)
- CO₂-battery module internal inventory may vary but no net loss to space
- CO₂ leak rate from both Air Loop and Energy Loop subsystems shall be <0.1 kg/day total system

**CLOSED-002**: Verification methods:
- Mass balance calculation: CO₂ captured = CO₂ returned (±measurement uncertainty)
- Pressure vessel leak testing per applicable standards
- Long-duration functional testing with CO₂ inventory tracking

---

## 7. Safety and Fault Response

### 7.1 Hazard Controls (Implements REQ-ECS-SAF-CO2-001)

**SAFETY-001**: Overpressure protection:
- Pressure relief valves sized per ASME standards (or equivalent for space systems)
- Automatic isolation valving on high-pressure detection
- Pressure sensors with redundancy and voting logic (if applicable)

**SAFETY-002**: Leak detection and isolation:
- Cabin atmosphere CO₂ monitoring with rate-of-change alarming
- Automatic closure of CO₂ isolation valves on leak detection
- Manual isolation capability from crew station and ground control

**SAFETY-003**: Thermal runaway prevention:
- Temperature monitoring at critical locations in CO₂-battery module
- Automatic load reduction or shutdown on overtemperature
- Thermal management system interlocks ensuring cooling availability before high-power operation

**SAFETY-004**: Electrical fault isolation:
- Overcurrent, overvoltage, and short-circuit protection per IF-PWR-021
- Galvanic isolation or isolation contactor for fault containment
- Ground fault detection (if required by electrical system architecture)

### 7.2 Fail-Safe Design

**SAFETY-011**: Upon loss of control power or communication, the system shall default to safe state:
- CO₂ isolation valves close (fail-closed design)
- Electrical contactors open (fail-open design)
- Pressure relief valves remain functional (passive safety)

**SAFETY-012**: Single-fault tolerance for crew-safety-critical functions:
- CO₂ capture system failure shall not prevent cabin CO₂ from being managed by alternate means (if applicable)
- CO₂-battery module failure shall not compromise vehicle electrical system integrity (isolation and protection required)

### 7.3 Hazard Analysis Traceability

**SAFETY-021**: Hazard analysis (FMEA/FMECA) per REQ-ECS-SAF-CO2-002 shall identify all credible failure modes and define mitigations. Hazard analysis results shall be traceable to:
- Design features implementing mitigations
- Verification test cases demonstrating mitigation effectiveness
- LC06 compliance matrix entries for safety evidence closure

---

## 8. Verification and Compliance

### 8.1 Verification Methods

Requirements in this specification shall be verified by:

| Requirement Category | Verification Method(s) |
|---------------------|------------------------|
| Electrical Power Interface | Test (bench, vehicle integration) |
| Thermal Interface | Analysis + Test (thermal vacuum chamber if required) |
| CO₂ Fluidic Interface | Test (flow, pressure, leak) |
| Control and Data Interface | Test (command/telemetry validation) |
| Operational Modes | Demonstration + Test (mode transition validation) |
| Energy Balance | Analysis (energy balance calculation) |
| Closed Loop | Analysis + Test (mass balance, leak rate) |
| Safety and Fault Response | FMEA + Analysis + Test (fault injection where applicable) |

### 8.2 Interface Control Document (ICD) Requirements

**VER-ICD-001**: Detailed interface specifications (connector types, pinouts, bus protocols, mechanical mounting, fluid fittings) shall be documented in Interface Control Documents (ICDs) referenced from ICD Index.

**VER-ICD-002**: ICD baseline approval required per LC03 gate (STK_CM signoff) before hardware fabrication or integration planning.

### 8.3 LC06 Compliance Evidence

**VER-LC06-001**: Verification matrix entries shall map each interface requirement to Method of Compliance (MoC) and required evidence artifacts.

**VER-LC06-002**: Evidence acceptability for claim boundary ("power support only") requires:
- Energy balance analysis report (demonstrates storage function, not energy source)
- Closed-loop verification results (demonstrates no mass ejection)
- Safety analysis (FMEA) showing hazard mitigations

**VER-LC06-003**: STK_CERT shall review and accept verification evidence per LC06 gate signoff process.

---

## 9. Traceability and Governance

### 9.1 Requirements Traceability

This specification implements and refines parent requirements from ECS Requirements document:
- REQ-ECS-ATM-005 → IF-CO2-001, IF-CO2-002, IF-CO2-003
- REQ-ECS-PWR-BIDIR-001 → IF-PWR-001, IF-PWR-002, IF-PWR-003
- REQ-ECS-PWR-RT-001 → ENERGY-001 (verified in Energy Balance Report)
- REQ-ECS-PWR-MODE-001 → Section 5 (Operational Modes)
- REQ-ECS-PWR-CLAIM-001 → Section 3.2 (Claim Boundary), Section 6 (Energy Balance)
- REQ-ECS-SAF-CO2-001 → Section 7 (Safety and Fault Response)

### 9.2 Change Control

**GOV-001**: Changes to this specification require:
1. Change Request (CR) submitted to STK_CM configuration management
2. Impact assessment by STK_CEGT (technical) and STK_SE (system-level impacts)
3. Safety review by STK_SAF if safety-related changes
4. Compliance review by STK_CERT if verification/evidence impacts exist
5. Change Board approval per AMPEL360 change control process
6. Document revision with updated issue_rev and changelog entry

**GOV-002**: Interface relaxation (less stringent requirements) prohibited without explicit STK_CM and STK_CERT signoff demonstrating no impact to safety, performance, or certification.

### 9.3 Linked Artifacts

**Supporting Analysis**:
- Energy Balance Report: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_10_LC04_K04-T010_STK_CEGT__co2-loop-energy-balance_DELIVERABLE_RPT_I01-R01_DRAFT.md`
- Thermal Envelope Report: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC04_K04-T011_STK_PHM__co2-loop-thermal-envelope_DELIVERABLE_RPT_I01-R01_DRAFT.md`

**Parent Requirements**:
- ECS Requirements: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC02_K02_STK_SE__env-control-system-requirements_DELIVERABLE_REQ_I01-R01_ACTIVE.md`

**Governance**:
- ATA Impact Matrix: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC02_K02_STK_SE__ata-impact-matrix_REGISTRY_TAB_I01-R01_ACTIVE.csv`
- Task Registry (STK_CEGT): `CAXS/AoR/STK_CEGT/task_registry.md`
- Signoff Index: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_10_LC03_K03_STK_CM__ecs-signoff-index_REGISTRY_IDX_I01-R01_ACTIVE.md`

---

## 10. Approvals and Signoffs

**Specification Owner**: STK_CEGT (Circular Economy and Green Tech)

**Technical Interfaces**:
- STK_SE (Systems Engineering) — system-level interface consistency, ICD coordination
- STK_PHM (Physical & Mechanical Engineering) — thermal analysis and heat rejection validation

**Governance**:
- STK_CM (Configuration Management) — LC03 baseline approval, change control authority
- STK_CERT (Certification) — LC06 verification matrix acceptance, evidence acceptability

**Safety Review**:
- STK_SAF (Safety) — hazard analysis review (supporting, with CERT signoff per constraints)

---

## 11. Revision History

| Issue-Rev | Date | Author | Description |
|-----------|------|--------|-------------|
| I01-R01 | 2025-12-19 | STK_CEGT | Initial draft specification for CO₂ loop power support interfaces |

---

## 12. References

### 12.1 AMPEL360 Framework
- `README.md` — AMPEL360 framework overview and nomenclature v6.0
- `ATA_PARTITION_MATRIX.yaml` — ATA-21/ATA-24 applicability
- CAXS Portal Main Workflow SSOT

### 12.2 Standards
- ECSS-E-ST-50C: Space Engineering - Thermal Control
- NASA-STD-3001: NASA Space Flight Human-System Standard
- IEC 62040: Uninterruptible Power Systems (UPS)
- ASME Boiler and Pressure Vessel Code (or equivalent for space systems pressure vessels)

### 12.3 Related ATA Systems
- ATA-21: Air Conditioning / Environmental Control
- ATA-24: Electrical Power
- ATA-42: IMA / Compute Platform
- ATA-45: Central Maintenance System
- ATA-46: Information Systems / Data Networks

---

**END OF DOCUMENT**
