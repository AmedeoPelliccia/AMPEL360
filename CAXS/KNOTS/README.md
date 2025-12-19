# KNOTS — Knowledge Nets and Ontology as Tasking Strategy

## Overview

**KNOTS** (Knowledge Nets and Ontology as Tasking Strategy) is the AMPEL360 CAXS method for turning **design thinking** into **certifiable, repeatable agentic work**, expressed as **SysML-consumable task structures** and enforced by governance gates.

---

## What is a KNOT?

A KNOT is a **controlled process node** that defines:

1. **What knowledge must exist** (ontology commitments)
2. **How it must connect** (knowledge net interfaces)
3. **What tasks agents may execute** (tasking strategy)
4. **What evidence must be produced** (compliance-ready outputs)

---

## KNOT IDs (Configuration-Controlled)

**Allowed IDs:** K01..K14 only  
**Optional task suffix:** `-T###` (e.g., `K06-T001`)

Any new KNOT requires a **standard upgrade + CM approval**.

---

## KNOT Directory Structure

### K01 — Initial Concept and Problem Definition
**Path:** `K01/`

**Purpose:** Problem framing, ideation, NKU generation pathways, prompting engineering baselines

**Primary AoR:** STK_DAB, STK_SE, STK_CM  
**Primary Phase:** LC01

---

### K02 — Requirements Capture and Allocation
**Path:** `K02/`

**Purpose:** Requirement capture, allocation, traceability seeding, acceptance criteria definition

**Primary AoR:** STK_SE, STK_CM  
**Primary Phase:** LC02

---

### K03 — Architecture Definition
**Path:** `K03/`

**Purpose:** System architecture definition, SysML modeling, interface design

**Primary AoR:** STK_SE, STK_DAB  
**Primary Phase:** LC03

---

### K04 — Engineering Analysis
**Path:** `K04/`

**Purpose:** Analyses, calculation models, trade studies, margins, model validation

**Primary AoR:** STK_PHM, STK_SE, STK_DAB  
**Primary Phase:** LC04

---

### K05 — Integration and Testing
**Path:** `K05/`

**Purpose:** Prototyping, integration campaigns, SIL/HIL/PIL, evidence production

**Primary AoR:** STK_TEST, STK_SE, STK_DAB  
**Primary Phase:** LC05

---

### K06 — Quality Assurance
**Path:** `K06/`

**Purpose:** QMS artifacts, process quality, audits, nonconformance management

**Primary AoR:** STK_CM, STK_PMO, STK_TEST  
**Primary Phase:** LC06

---

### K07 — Safety and Security Assurance
**Path:** `K07/`

**Purpose:** Safety case development, hazard controls, cybersecurity assurance

**Primary AoR:** STK_SAF, STK_CY, STK_SE  
**Primary Phase:** LC07

---

### K08 — Certification Planning and Execution
**Path:** `K08/`

**Purpose:** Certification planning, compliance evidence, authority submissions

**Primary AoR:** STK_CERT, STK_TEST, STK_OPS  
**Primary Phase:** LC08

---

### K09 — Sustainability and Green Initiatives (Circular Economy Governance Node)
**Path:** `K09/`

**Purpose:** Sustainability baselines, circularity KPIs, green tech evidence, ESG reporting, circular systems design validation

**Primary AoR:** STK_CEGT, STK_PMO, STK_DAB, STK_CM  
**Primary Phase:** LC09

**Semantics:** K09 serves as the governance node for circular economy initiatives, bridging sustainability requirements (LC09 Green Aircraft/Baselines) with circularity metrics, ESG compliance, and alternative technology assessments. This KNOT enforces evidence-based validation of circularity targets and social responsibility frameworks.

---

### K10 — Production and Configuration Management
**Path:** `K10/`

**Purpose:** Industrial planning, production readiness, configuration baselines

**Primary AoR:** STK_CM, STK_PMO, STK_PHM  
**Primary Phase:** LC10

---

### K11 — Operations Planning and Execution
**Path:** `K11/`

**Purpose:** ConOps, procedures, readiness, operational baselines, mission operations

**Primary AoR:** STK_OPS, STK_SPACEPORT, STK_CM  
**Primary Phase:** LC11

---

### K12 — Support and Services Delivery
**Path:** `K12/`

**Purpose:** Customer support, service processes, service tooling, support documentation

**Primary AoR:** STK_OPS, STK_MRO, STK_DAB  
**Primary Phase:** LC12

---

### K13 — Maintenance and Sustainment
**Path:** `K13/`

**Purpose:** Maintenance programs, manuals, sustainment evidence, reliability/PHM integration

**Primary AoR:** STK_MRO, STK_PHM, STK_DAB  
**Primary Phase:** LC13

---

### K14 — Retirement and Circularity
**Path:** `K14/`

**Purpose:** End-of-life, retirement procedures, recycling/return flows, circularity closure

**Primary AoR:** STK_PMO, STK_CM, STK_DAB  
**Primary Phase:** LC14

---

## KNOT Execution Model

Each KNOT has:

- **Inputs**: Required artifacts + schemas
- **Transforms**: Allowed agentic actions (generate/validate/link/package)
- **Outputs**: NKUs (implicit) + evidence bundles
- **Guards**: PLC gates that must pass (PR-blocking)
- **Trace edges**: Relations recorded into traceability graph

---

## KNOT Closure Criteria

A KNOT is "closed" only when:

1. Naming/identifier validators pass
2. Evidence links resolve
3. Exceptions are registered and approved (where allowed)
4. Release pack or checkpoint artifact is produced (when applicable)

---

## KNOT Metadata Schema

Each KNOT definition should include:

- `knot_id`: K01..K14
- `purpose`: Why this knot exists
- `inputs_required`: Artifact types + schemas
- `outputs_required`: Artifact types + evidence expectations
- `relations_required`: Required trace edges (satisfy/verify/etc.)
- `aor_owner`: Primary AoR/STK
- `dependencies`: Other STKs and required handoffs
- `gates`: Validators that must pass
- `close_criteria`: Measurable completion criteria
- `exceptions_policy`: What can be waived, by whom, and how recorded

---

## Usage Guidelines

### For Task Execution

1. **Identify the appropriate KNOT** for your work (K01-K14)
2. **Review KNOT requirements** (inputs, outputs, gates)
3. **Bind task to uncertainty node** (if applicable)
4. **Execute allowed actions** using approved templates
5. **Generate evidence** as specified by KNOT
6. **Run validators** (PLC gates)
7. **Record trace edges** in knowledge ledger
8. **Close KNOT** when criteria are met

### For Agentic Systems

Each KNOT provides:
- **Prompting specifications** for AI agents
- **Automation scripts** for task execution
- **Validation rules** for output checking
- **Trace patterns** for ledger updates

---

## Integration with CAXS

KNOTS bridge:
- **AoR entry points** → Who is accountable
- **Lifecycle phases** → When work occurs
- **ATA chapters** → What technical domain
- **Evidence ledgers** → How work is proven

---

## Governance

- **KNOT IDs are configuration-controlled** — K01..K14 only
- **No ad-hoc KNOTs** — New KNOTs require CM approval
- **KNOT definitions are normative** — Cannot be repurposed
- **KNOT closure is gated** — Must satisfy all validators

---

## Version

**KNOTS Structure Version:** 1.0  
**Controlled KNOT Range:** K01-K14  
**Last Updated:** 2025-12-19

---

## References

- [CAXS Main README](../README.md)
- [KNOTS Definition (Main README)](../../README.md#6-knots--knowledge-nets-and-ontology-as-tasking-strategy)
- [v6.0 Nomenclature](../../README.md#92-controlled-vocabulary--nomenclature-v60)
