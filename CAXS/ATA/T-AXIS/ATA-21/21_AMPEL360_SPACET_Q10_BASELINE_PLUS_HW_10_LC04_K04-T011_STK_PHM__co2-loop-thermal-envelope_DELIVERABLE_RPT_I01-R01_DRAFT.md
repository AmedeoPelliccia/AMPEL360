---
document_id: "21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC04_K04-T011_STK_PHM__co2-loop-thermal-envelope_DELIVERABLE_RPT_I01-R01_DRAFT"
title: "CO₂ Loop Thermal Envelope Analysis Report — SPACET Q10 BASELINE PLUS"
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
phase: "LC04"
phase_description: "Analysis and Simulation"
knot: "K04"
task_id: "K04-T011"
scope: "Thermal envelope analysis for CO₂ capture and CO₂-battery energy storage system heat rejection"
owner_aor: "STK_PHM"
interfaces:
  required: ["STK_CEGT", "STK_SE"]
  optional: []
category: "DELIVERABLE"
type: "RPT"
status: "DRAFT"
issue_rev: "I01-R01"
---

# CO₂ Loop Thermal Envelope Analysis Report — SPACET Q10 BASELINE PLUS

## Executive Summary

This report provides **thermal envelope analysis** for the CO₂ capture subsystem and CO₂-battery energy storage module integrated with the Environmental Control System (ECS) for SPACET Q10 BASELINE PLUS.

**Key Findings**:
- **Total heat rejection requirement**: 0.6-0.8 kW peak during charge/discharge operations
- **Baseline ECS thermal capacity**: 5 kW continuous (REQ-ECS-THM-002) — sufficient margin available
- **Thermal interface**: Cold plate or fluid loop connection to vehicle thermal management system
- **Critical constraint**: Module performance and safety depend on thermal management system availability

**Recommendation**: Proceed with thermal integration design; verify thermal capacity allocation with vehicle-level thermal budget.

---

## 1. Purpose and Scope

### 1.1 Objective

Quantify thermal loads and heat rejection requirements for:
1. **CO₂ capture subsystem** (atmospheric CO₂ removal and regeneration)
2. **CO₂-battery energy storage module** (charge/discharge thermal losses)
3. **Combined thermal envelope** impact on vehicle thermal management system

### 1.2 Analysis Basis

Thermal analysis based on:
- Interface requirements: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC02_K02_STK_CEGT__co2-loop-power-support-interfaces_DELIVERABLE_SPEC_I01-R01_DRAFT.md`
- Energy balance: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_10_LC04_K04-T010_STK_CEGT__co2-loop-energy-balance_DELIVERABLE_RPT_I01-R01_DRAFT.md`
- Operating envelope: Charge 2.0 kW / Discharge 1.5-2.5 kW
- ECS baseline capacity: 5 kW continuous heat rejection (REQ-ECS-THM-002)

### 1.3 Methodology

Thermal loads calculated from:
- **First Law energy balance**: Electrical power in/out + stored energy change = thermal losses
- **Component efficiency models**: Power electronics, CO₂ storage process, mechanical/pumping losses
- **Capture process thermal load**: Regeneration/desorption energy requirements
- **Steady-state and transient thermal response** (preliminary)

---

## 2. System Thermal Description

### 2.1 CO₂ Capture Subsystem Thermal Loads

#### 2.1.1 Capture Process (Adsorption/Absorption)

**Process**: Atmospheric CO₂ removal from cabin air using sorbent material (solid amine, liquid amine, or other capture technology)

**Thermal characteristic**: Capture phase is typically **exothermic** (heat released as CO₂ binds to sorbent)

**Heat release estimate** (for representative amine-based capture):
- Heat of adsorption: ~50-80 kJ/mol CO₂
- CO₂ capture rate: 1.0 kg/person/day = 22.7 mol/day per person
- For 4-person crew: 90.8 mol/day = 0.00105 mol/s
- Heat release: 0.00105 mol/s × 65 kJ/mol (midpoint) = **0.068 kW continuous**

**Note**: Heat release is relatively low and may be manageable through ambient convection or minimal active cooling.

#### 2.1.2 Regeneration/Desorption Process

**Process**: Captured CO₂ released from sorbent material for return to buffer storage (closed loop)

**Thermal characteristic**: Regeneration is typically **endothermic** (heat input required to release CO₂ from sorbent)

**Heat input estimate**:
- Regeneration energy: ~60-90 kJ/mol CO₂ (slightly higher than capture due to process inefficiency)
- Regeneration rate: Same as capture rate (cyclic batch or continuous)
- Heat input: 0.00105 mol/s × 75 kJ/mol (midpoint) = **0.079 kW continuous**

**Heat rejection**: Regeneration heat input plus inefficiencies rejected to thermal system:
- Assume regeneration efficiency 70% (30% of input energy becomes waste heat)
- Additional waste heat: 0.079 kW × 0.30 = **0.024 kW**

**Total CO₂ capture subsystem thermal load**: 0.068 kW (capture) + 0.024 kW (regeneration waste) = **~0.09 kW continuous** (rounded to 0.1 kW for margin)

### 2.2 CO₂-Battery Energy Storage Module Thermal Loads

#### 2.2.1 Charge Mode Thermal Losses

**Input power**: 2.0 kW (continuous max) from ATA-24 electrical bus

**Charge efficiency**: 78.2% (from Energy Balance Report) → 21.8% thermal losses

**Thermal load (charge)**: 2.0 kW × 0.218 = **0.44 kW** (continuous at max charge power)

**Average charge thermal load** (based on representative duty cycle):
- Average charge power: ~0.8 kW (from Energy Balance Report, 24-hour cycle)
- Average thermal load: 0.8 kW × 0.218 = **0.17 kW average**

#### 2.2.2 Discharge Mode Thermal Losses

**Output power**: 1.5 kW continuous / 2.5 kW peak

**Discharge efficiency**: 79.2% (from Energy Balance Report) → 20.8% thermal losses

**Thermal load (discharge continuous)**: 1.5 kW / 0.792 - 1.5 kW = **0.39 kW**

**Thermal load (discharge peak)**: 2.5 kW / 0.792 - 2.5 kW = **0.66 kW** (for ≤60 seconds)

#### 2.2.3 Standby Mode Thermal Losses

**Power consumption**: Monitoring, control, minimal thermal management

**Thermal load (standby)**: **0.05 kW** (from IF-THM-001 in Interface Spec)

### 2.3 Combined Thermal Envelope Summary

| Operating Mode | CO₂ Capture (kW) | CO₂-Battery (kW) | Total (kW) |
|----------------|------------------|------------------|------------|
| Standby | 0.1 | 0.05 | **0.15** |
| Charge (2.0 kW) | 0.1 | 0.44 | **0.54** |
| Discharge (1.5 kW) | 0.1 | 0.39 | **0.49** |
| Discharge Peak (2.5 kW) | 0.1 | 0.66 | **0.76** |

**Peak thermal load**: **0.8 kW** (rounded with margin) during peak discharge

**Average thermal load**: **0.2-0.3 kW** based on representative duty cycle

---

## 3. Thermal Interface Requirements

### 3.1 Heat Rejection Method

**Recommendation**: Cold plate or fluid loop interface to vehicle active thermal control system (ATA-21 thermal bus)

**Rationale**:
- Thermal loads (0.5-0.8 kW) exceed capability of passive cooling (radiation/conduction) in typical space vehicle thermal environment
- Active thermal control provides reliable heat rejection across all mission phases
- Integration with ECS thermal bus simplifies vehicle-level thermal management

**Alternative**: Dedicated heat exchanger to cabin air (limited applicability due to need for heat rejection during all mission phases, including vacuum)

### 3.2 Coolant Interface Specifications

**Coolant inlet temperature**: 15-35°C (from IF-THM-001)

**Coolant flow rate**: TBD based on cold plate design and thermal resistance (preliminary estimate: 0.5-1.0 L/min for single-phase liquid coolant)

**Temperature rise**: ΔT = Q / (ṁ × Cp)
- For Q = 0.8 kW, ṁ = 0.5 L/min = 0.00833 kg/s, Cp = 4.18 kJ/kg·K (water)
- ΔT = 800 W / (0.00833 kg/s × 4180 J/kg·K) = **23°C**
- Coolant outlet temperature: 15°C + 23°C = 38°C (within typical thermal system limits)

**Pressure drop**: TBD based on cold plate design (target <50 kPa for vehicle thermal loop compatibility)

### 3.3 Module Internal Temperature Limits

**CO₂-battery module operating temperature**: TBD based on technology selection

**Preliminary limits** (representative for CO₂ systems):
- Operating range: -10°C to +60°C
- Optimal performance range: +10°C to +40°C
- Overtemperature alarm: +55°C
- Overtemperature shutdown: +60°C

**Thermal control requirement**: Active thermal management required to maintain module within operating limits across all mission phases and environmental conditions.

---

## 4. Vehicle Thermal System Impact

### 4.1 ECS Thermal Capacity Allocation

**Baseline ECS thermal rejection capacity**: 5 kW continuous (REQ-ECS-THM-002)

**CO₂ loop thermal load**: 0.8 kW peak, 0.2-0.3 kW average

**Margin analysis**:
- Reserved capacity for CO₂ loop: 0.8 kW (peak)
- Remaining ECS capacity: 5.0 - 0.8 = **4.2 kW available for other ECS loads**
- Utilization: 0.8 / 5.0 = **16% of total ECS thermal capacity** (peak)

**Conclusion**: **Adequate margin** exists within baseline ECS thermal capacity. CO₂ loop thermal load does not compromise other ECS thermal management requirements.

### 4.2 Thermal Coupling Considerations

**Intra-ATA coupling**: CO₂ loop thermal load couples to ATA-21 thermal subsystem (BLOCK-40 physics domain per ATA Impact Matrix entry)

**Critical interface**: Coordination required between:
- Operational systems (BLOCK-10): CO₂ capture and energy storage operational requirements
- Thermal physics subsystem (BLOCK-40): Heat rejection capacity and thermal control hardware

**Design constraint**: CO₂-battery discharge capacity may be limited by available thermal management capacity. If thermal system degraded or overloaded, module must reduce discharge power to prevent overtemperature (per MODE-DEG-001).

### 4.3 Mission Phase Thermal Considerations

**Launch/Landing**: High vehicle power demand → potential for CO₂-battery peak discharge → peak thermal load (0.8 kW)
- Thermal system must have capacity during dynamic flight phases
- Coordination with vehicle thermal design for worst-case thermal scenarios

**On-Orbit**: Lower average thermal load (0.2-0.3 kW) but continuous operation
- Thermal system steady-state performance critical
- Radiator capacity and sun/shade thermal cycling may affect performance

**Ground Operations**: Thermal management via ground support equipment or vehicle thermal system
- Pre-launch charging may generate thermal load requiring ground cooling
- Post-landing: Module may continue operation using vehicle or ground thermal support

---

## 5. Thermal Transient Analysis (Preliminary)

### 5.1 Mode Transition Thermal Response

**Charge → Discharge transition**:
- Thermal load change: 0.44 kW → 0.39 kW (relatively small change)
- Module thermal time constant: Estimated 5-10 minutes (depends on thermal mass and thermal resistance)
- Coolant temperature transient: ΔT change ~1-2°C over 1-2 minutes (manageable)

**Peak discharge transient** (2.5 kW for 60 seconds):
- Thermal load step: 0.39 kW → 0.66 kW (ΔQ = +0.27 kW)
- Short duration (≤60s) allows thermal mass to buffer transient
- Module temperature rise during peak: Estimated +5-10°C (depends on thermal capacitance)
- Thermal control system must accommodate transient without overtemperature shutdown

**Recommendation**: Detailed transient thermal modeling (lumped-parameter or finite-element) required during design phase to validate thermal control adequacy and size thermal mass/cold plate.

### 5.2 Thermal Startup/Shutdown

**Cold start** (module at low temperature, e.g., after extended ground storage):
- Preconditioning may be required to bring module to operational temperature before high-power operation
- Preconditioning time: Estimated 30-60 minutes (depends on heating capacity and thermal mass)

**Emergency shutdown**:
- Thermal loads cease immediately upon electrical isolation
- Module cool-down: Natural convection (if cabin atmosphere present) or conduction/radiation (vacuum)
- Cool-down time constant: Estimated 1-2 hours to ambient temperature

---

## 6. Design Recommendations

### 6.1 Thermal Management System Sizing

**Cold plate sizing**:
- Design for peak thermal load: 0.8 kW (with 20% margin → 1.0 kW)
- Thermal resistance target: <0.05 K/W (to limit module-to-coolant temperature rise to <50°C at peak load)
- Material: Aluminum or copper cold plate with embedded coolant channels
- Interface: Thermal interface material (TIM) with low thermal resistance (<0.01 K/W)

**Coolant loop integration**:
- Connection to vehicle thermal bus (ATA-21 thermal management system)
- Flow control: Passive (fixed orifice) or active (proportional valve) depending on vehicle thermal system architecture
- Isolation capability: Valves or quick-disconnects for module removal/maintenance

### 6.2 Thermal Instrumentation

**Temperature sensors**:
- Module internal temperature: 2-4 sensors at critical locations (storage medium, power electronics, coldest/hottest points)
- Coolant inlet/outlet temperatures: 1 sensor each for thermal load monitoring
- Redundancy: Consider dual sensors for safety-critical temperature monitoring (overtemperature protection)

**Flow sensors** (optional):
- Coolant flow rate monitoring for thermal system health check and leak detection

### 6.3 Thermal Control Algorithm

**Overtemperature protection**:
- Alarm threshold: Module temperature >55°C (warning to crew/ground)
- Load reduction: Module temperature >57°C → reduce charge/discharge power by 50%
- Shutdown: Module temperature >60°C → automatic isolation and shutdown

**Thermal-limited power management**:
- If thermal management capacity reduced (e.g., thermal system degradation, coolant pump failure), module automatically reduces power envelope to match available cooling
- Graceful degradation per MODE-DEG-001

---

## 7. Assumptions and Limitations

### 7.1 Key Assumptions

1. **Technology-representative values**: Thermal loads estimated using representative efficiencies and processes; actual values depend on selected CO₂-battery and capture technologies
2. **Steady-state focus**: Detailed transient thermal modeling deferred to design phase
3. **Nominal thermal system performance**: Assumes vehicle thermal management system operates at design capacity
4. **Coolant properties**: Single-phase liquid coolant (water or water-glycol) assumed for interface calculations

### 7.2 Limitations and Future Work

1. **Technology selection**: Thermal characteristics will be refined once CO₂-battery and capture technologies selected
2. **Detailed thermal modeling**: Lumped-parameter or finite-element thermal models needed for design verification
3. **Environmental testing**: Thermal vacuum testing required to validate performance in space environment
4. **Integration analysis**: Vehicle-level thermal system modeling to confirm capacity allocation and worst-case scenario analysis

---

## 8. Conclusions and Recommendations

### 8.1 Conclusions

1. **Thermal load quantified**: Peak thermal load of 0.8 kW during CO₂-battery peak discharge; average load 0.2-0.3 kW over representative mission cycle.

2. **ECS capacity adequate**: Baseline ECS thermal rejection capacity (5 kW continuous) provides sufficient margin for CO₂ loop thermal loads.

3. **Active thermal management required**: Thermal loads exceed passive cooling capability; cold plate or fluid loop interface to vehicle thermal system recommended.

4. **Thermal integration feasible**: No significant thermal constraints identified at system level; detailed design and analysis required to validate interface and control algorithms.

### 8.2 Recommendations

1. **Thermal interface design**: Proceed with cold plate design sized for 1.0 kW capacity (20% margin above peak load).

2. **Vehicle thermal budget coordination**: Allocate 0.8 kW peak / 0.3 kW average thermal load to ATA-21 thermal management system in vehicle-level thermal budget.

3. **Transient thermal analysis**: Conduct detailed transient thermal modeling during preliminary design to validate thermal time constants and control algorithm performance.

4. **Instrumentation plan**: Specify temperature and (optionally) flow sensors for thermal monitoring and overtemperature protection.

5. **Environmental qualification**: Include thermal vacuum testing in qualification test plan to verify performance across mission thermal environments.

6. **ICD development**: Document thermal interface specifications (coolant type, flow rate, pressure drop, connector type) in Interface Control Document for LC03 baseline approval.

---

## 9. Traceability

### 9.1 Parent Requirements

This analysis supports verification of:
- REQ-ECS-THM-002: ECS thermal control shall reject minimum 5 kW continuous heat load (provides margin for CO₂ loop)
- IF-THM-001: Heat rejection envelope (0.6-0.8 kW per operating mode)
- REQ-ECS-SAF-CO2-001: Thermal runaway prevention (thermal monitoring and interlocks)

### 9.2 Interface Specification

Analysis feeds thermal interface requirements in:
- `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC02_K02_STK_CEGT__co2-loop-power-support-interfaces_DELIVERABLE_SPEC_I01-R01_DRAFT.md`
  - Section 4.2 (Thermal Interface)
  - Section 7 (Safety and Fault Response - thermal runaway prevention)

### 9.3 Energy Balance Coordination

Thermal loss assumptions coordinated with:
- `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_10_LC04_K04-T010_STK_CEGT__co2-loop-energy-balance_DELIVERABLE_RPT_I01-R01_DRAFT.md`
  - Component efficiencies and thermal loss calculations
  - Round-trip efficiency verification

### 9.4 Verification Matrix

This analysis provides evidence for LC06 verification matrix:
- Objective: Demonstrate thermal management feasibility and margin
- Method of Compliance: Analysis (preliminary) + Test (qualification)
- Evidence: This report + future thermal test results

---

## 10. Approvals and Reviews

**Analysis Owner**: STK_PHM (Physical & Mechanical Engineering)

**Technical Interface**:
- STK_CEGT (Circular Economy and Green Tech) — energy balance coordination, interface requirements
- STK_SE (Systems Engineering) — vehicle thermal system coordination, requirement allocation

**Compliance Review**:
- STK_CERT (Certification) — evidence acceptability for LC06 compliance

---

## 11. Revision History

| Issue-Rev | Date | Author | Description |
|-----------|------|--------|-------------|
| I01-R01 | 2025-12-19 | STK_PHM | Initial draft thermal envelope analysis |

---

## 12. References

### 12.1 AMPEL360 Documents
- ECS Requirements: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC02_K02_STK_SE__env-control-system-requirements_DELIVERABLE_REQ_I01-R01_ACTIVE.md`
- CO₂ Interface Spec: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_10_LC02_K02_STK_CEGT__co2-loop-power-support-interfaces_DELIVERABLE_SPEC_I01-R01_DRAFT.md`
- Energy Balance Report: `21_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_10_LC04_K04-T010_STK_CEGT__co2-loop-energy-balance_DELIVERABLE_RPT_I01-R01_DRAFT.md`

### 12.2 Technical Standards
- ECSS-E-ST-50C: Space Engineering - Thermal Control
- Heat transfer fundamentals (conduction, convection, radiation)
- Thermal interface materials and cold plate design practices

### 12.3 Technology References
- CO₂ capture technology literature (amine-based sorbents, thermal regeneration processes)
- Energy storage system thermal management (battery thermal management, supercritical CO₂ systems)

---

**END OF DOCUMENT**
