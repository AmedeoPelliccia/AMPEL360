# Circularity KPI Registry

**Owner:** STK_CEGT  
**Co-Managed By:** STK_CM  
**Status:** ACTIVE  
**Version:** 1.0  
**Last Updated:** 2025-12-19  
**Primary Alignment:** ATA 85 (Circularity Infrastructure), LC09 (Green Aircraft Baselines)

## Purpose

This registry defines and tracks Key Performance Indicators (KPIs) for circular economy initiatives within AMPEL360 programs (AIRT and SPACET).

## Circularity KPIs

### KPI-CIRC-001: Material Circularity Index (MCI)
**Definition:** Percentage of materials that can be recycled, reused, or repurposed at end-of-life  
**Target:** ≥ 85% by 2030  
**Current Baseline:** To be established  
**Measurement Frequency:** Per aircraft/vehicle design iteration  
**Data Source:** Bill of Materials (SBOM/BOM), DPP records  
**Responsible AoR:** STK_CEGT, STK_PHM

**Formula:**
```
MCI = (Recyclable Mass + Reusable Mass) / Total Mass × 100%
```

---

### KPI-CIRC-002: End-of-Life Recovery Rate
**Definition:** Percentage of aircraft/vehicle mass recovered for circular flows at retirement  
**Target:** ≥ 90% by 2035  
**Current Baseline:** To be established  
**Measurement Frequency:** Per retired unit  
**Data Source:** MRO records, retirement documentation  
**Responsible AoR:** STK_CEGT, STK_MRO

---

### KPI-CIRC-003: Virgin Material Reduction
**Definition:** Percentage reduction in virgin material usage vs. baseline design  
**Target:** 30% reduction by 2030  
**Current Baseline:** To be established (using Q100 baseline)  
**Measurement Frequency:** Per design milestone  
**Data Source:** BOM comparison, material sourcing records  
**Responsible AoR:** STK_CEGT, STK_PHM

---

### KPI-CIRC-004: Design for Disassembly Score
**Definition:** Weighted score of design features enabling end-of-life disassembly  
**Target:** ≥ 80/100 points  
**Current Baseline:** To be established  
**Measurement Frequency:** Per design review (LC03, LC04)  
**Data Source:** Design documentation, maintainability assessments  
**Responsible AoR:** STK_CEGT, STK_SE, STK_PHM

**Scoring Criteria:**
- Modular design: 0-25 points
- Standardized fasteners: 0-20 points
- Material identification: 0-15 points
- Disassembly documentation: 0-20 points
- Tool accessibility: 0-20 points

---

### KPI-CIRC-005: Sustainable Material Content
**Definition:** Percentage of materials from sustainable or recycled sources  
**Target:** ≥ 50% by 2030  
**Current Baseline:** To be established  
**Measurement Frequency:** Per procurement cycle  
**Data Source:** Supplier declarations, material certifications  
**Responsible AoR:** STK_CEGT, STK_PMO

---

## KPI Tracking

| KPI ID | Name | Target | Baseline | Current | Status | Last Updated |
|--------|------|--------|----------|---------|--------|--------------|
| CIRC-001 | Material Circularity Index | ≥85% | TBD | TBD | 🟡 Pending | 2025-12-19 |
| CIRC-002 | End-of-Life Recovery | ≥90% | TBD | TBD | 🟡 Pending | 2025-12-19 |
| CIRC-003 | Virgin Material Reduction | 30% | TBD | TBD | 🟡 Pending | 2025-12-19 |
| CIRC-004 | Design for Disassembly | ≥80/100 | TBD | TBD | 🟡 Pending | 2025-12-19 |
| CIRC-005 | Sustainable Material Content | ≥50% | TBD | TBD | 🟡 Pending | 2025-12-19 |

**Status Legend:**
- 🟢 On Track: Meeting or exceeding target
- 🟡 Pending: Baseline not yet established
- 🟠 At Risk: Below target but recoverable
- 🔴 Off Track: Significantly below target

## Data Collection

### Required Data Sources
1. **SBOM/BOM Ledger:** `CAXS/LEDGERS/sbom-bom/`
2. **Digital Product Passport:** `CAXS/LEDGERS/digital-product-passport/`
3. **Design Documentation:** ATA 51-57 (Structures)
4. **MRO Records:** ATA 05, 12
5. **Supplier Data:** Procurement records

### Reporting Frequency
- **Quarterly:** KPI dashboard update
- **Per Milestone:** Design reviews (LC03, LC04, LC08)
- **Annually:** Circularity report to stakeholders

## Trace to Evidence

All KPI measurements must link to:
- **Evidence artifacts** in `CAXS/AoR/STK_CEGT/evidence_index.md`
- **Traceability graph** entries showing data provenance
- **Approval records** for baseline and target changes

## Governance

- **KPI Definitions:** Require STK_CEGT + STK_CM approval
- **Target Changes:** Require STK_PMO + STK_CEGT approval
- **Baseline Establishment:** Requires measurement campaign + evidence
- **Reporting:** Mandatory in LC09 phase outputs

## Integration with ESG Reporting

Circularity KPIs feed into:
- **ESG Reporting Index:** `CAXS/LEDGERS/esg_reporting_index.md`
- **Sustainability Dashboard:** External stakeholder reporting
- **Certification Packs:** Environmental compliance evidence

## Version Control

**Registry Version:** 1.0  
**Next Review:** 2026-Q1  
**Change Authority:** STK_CEGT (technical), STK_CM (governance)
