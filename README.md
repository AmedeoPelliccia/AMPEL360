# AMPEL360
**AMPEL360** is a **unified digital lifecycle architecture** for advanced aerospace systems

**A**EROSPACE **M**ODELS, **P**LATFORMS, **E**VOLUTION, **L**EDGERS (360°)

---

## 1. Integrated Definition

**AMPEL360** is a **unified digital lifecycle architecture** for advanced aerospace systems (**AIRT / SPACET**) that binds four foundational pillars into a single **certifiable, auditable, continuously evolving knowledge system**.

---

## 2. Product Line Matrix

| PROGRAM | VERSION | FAMILY | Description |
|---------|---------|--------|-------------|
| **AIRT** | PLUS | Q100 | BWB H₂-Electric Aircraft (INTEGRA) |
| **AIRT** | PLUSULTRA | Q200LR | Long-Range Advanced Variant |
| **SPACET** | PLUS | Q10 | Space Transport Baseline |
| **SPACET** | PLUSULTRA | QHABITAT | Habitat-Class Space Vehicle |

---

## 3. The Four Pillars

### 3.1 A — AEROSPACE

**Domain scope.** Advanced Air Transport (**AIRT**) and Space Transport (**SPACET**) programs governed through tailored ATA chapter structures spanning **ATA 00–116**, integrated into the **OPT-INS framework** and exposed through role-routed portal entry points (AoR/STK).

> **Principle.** Aerospace tailoring is expressed as controlled allocations and applicability rules, not as ad-hoc folder sprawl.

### 3.2 M — MODELS

**Representational layer (governed assets).**

- **Architecture models** — SysML/MBSE under **STK_SE** governance
- **Digital twins** — ATA 101 catalog, fidelity tiers, baseline control
- **AI/ML models** — ATA 90 registry, lifecycle governance under **STK_AI**
- **Schemas / ontologies / SSOT** — ATA 91 under **STK_DAB**
- **Connectivity graphs** — ATA 92 wiring/connectivity packages under **STK_DAB**, with **STK_PHM** dependencies

> **Rule.** Every model is configuration-controlled, version-tracked, trace-linked, and evidence-addressable.

### 3.3 P — PLATFORMS

**Execution infrastructure (deterministic delivery).**

- **CAXS Portal (CA360º)** — role-routed entry points, roadmap orchestration, task-to-artifact execution spine
- **On-board compute platforms** — ATA 42 IMA/compute, partitioning, cyber-hardened under **STK_CY** with **STK_DAB** implementation dependencies
- **Off-board infrastructure** — ATA 80–89: spaceport services, GSE, test rigs, digital services
- **SIL/HIL/PIL environments** — ATA 103–105 automation benches
- **PLC validators** — process logic controllers enforcing nomenclature, identifiers, schema integrity, and evidence closure (PR-blocking)

> **Rule.** Platform outputs are only valid when produced under validator-gated CI/PR control.

### 3.4 E — EVOLUTION

**Temporal governance (controlled change, not drift).**

- **Uncertainty node resolution** — predefined unknowns reduced via structured tasks aligned to **KNOTS (K01..K14)**
- **Technology integration pathways** — new capability introduced through reserved/controlled extension points
- **Best-practice condensation** — validated patterns crystallize into reusable knowledge capsules
- **Lifecycle continuity** — from design through certification, operations, MRO, and circular return flows (incl. ATA 85)
- **Change impact analytics** (ATA 97) — deterministic propagation of effects across wiring/config/trace

> **Rule.** Evolution is governed by CM and evidenced by traceable impact and closure artifacts.

### 3.5 L — LEDGERS

**Evidence and trust fabric (audit-grade continuity).**

- **Knowledge ledger** — immutable artifact addressing (repo path + sha256 + optional commit), typed relations, approval states
- **Traceability graph** (ATA 93) — REQ ↔ DESIGN ↔ V&V ↔ OPS linkage with audit queries
- **Digital Product Passport** (ATA 94) — provenance, materials, lifecycle identity
- **SBOM/BOM exports** (ATA 95) — dependency integrity for SW/HW/Model compositions
- **Signed release packs** (ATA 98) — manifests, exports, PR-blocking compliance evidence
- **Master registers** (ATA 99) — golden records and controlled vocabulary datasets

> **Rule.** Engineering work becomes certifiable only when it is ledger-addressed, trace-linked, and release-packaged.

---

## 4. 360° Integration

The "360" signifies **full-circle lifecycle closure**:

```
DESIGN → BUILD → VERIFY → CERTIFY → OPERATE → SUSTAIN → EVOLVE → (return)
   ↑                                                              ↓
   └──────────────── Knowledge Ledger Continuity ─────────────────┘
```

Every artifact produced at any phase feeds the ledger, reduces uncertainty, and is reusable across cycles—within the same vehicle, across variants, or across programs.

---

## 5. Portal Operating Model (CAXS / CA360º)

The **CAXS Portal (CA360º)** organizes all navigation and work execution around **AoR entry points (STKs)** and **stakeholder roles**, driving delivery through **roadmaps** that decompose into **task → artifact generation → evidence closure**.

### 5.1 Entry Points Aligned to AoR

Each portal entry point corresponds to an **accountable AoR (STK)** and exposes a role-oriented view of:

- Scope (what this AoR owns)
- Canonical ATA roots / domains it governs
- Active roadmaps and open uncertainty nodes
- Mandatory artifacts, evidence, and release gates

### 5.2 Roadmaps That Generate Artifacts Deterministically

A **Roadmap** is a structured plan that:

- Is **identified** (ID + scope + owner AoR)
- Decomposes into **tasks** aligned to KNOTS (K01..K14)
- Produces **controlled artifacts** (NKU implicit) using the v6.0 naming standard
- Requires **evidence outputs** (validator logs, link-check logs, exception diffs, test results)
- Aggregates results into a **knowledge ledger** for audit, reuse, and release packaging

### 5.3 Uncertainty Nodes and Condensation

The portal treats key unknowns as **pre-defined uncertainty nodes** that are actively reduced by work:

- Each node has a measurable "unknown → known" target
- Each task must produce artifacts that **reduce uncertainty**
- Successful closure is recorded as **evidence-backed ledger entries** that become reusable "best-practice capsules"

This "condenses" activity by eliminating redundant effort and converging teams onto canonical patterns, validated schemas, verified interfaces, and repeatable evidence packs.

### 5.4 Task-to-Artifact Lifecycle (Execution Spine)

For any roadmap item, the portal enforces this spine:

1. **Select entry point (AoR)** → determines authority, templates, and gates
2. **Bind to an uncertainty node + KNOT (K01..K14)** → defines permitted actions and evidence needs
3. **Generate/modify artifacts** under v6.0 nomenclature → NKU implicit
4. **Run PLC validators and link-check** → PR-blocking evidence
5. **Register exceptions (if any)** → CM-controlled register diff included
6. **Update ledger** (paths + hashes + relations) → audit-ready trace graph
7. **Package release** (signed manifests / export packs) → certification/ops readiness reuse

### 5.5 Outcomes

This portal model provides:

- **Role-correct navigation** (stakeholder-specific, AoR-accountable)
- **Enforceable governance** (validators, CI gates, controlled KNOTS)
- **Traceable delivery** (task → artifact → evidence → release)
- **Accelerated integration** of new technology through reusable, validated knowledge capsules

---

## 6. KNOTS — Knowledge Nets and Ontology as Tasking Strategy

**KNOTS** (Knowledge Nets and Ontology as Tasking Strategy) is the AMPEL360 CAXS method for turning **design thinking** into **certifiable, repeatable agentic work**, expressed as **SysML-consumable task structures** and enforced by governance gates.

A KNOT is a **controlled process node** that:
1) defines **what knowledge must exist** (ontology commitments),
2) defines **how it must connect** (knowledge net interfaces),
3) defines **what tasks agents may execute** (tasking strategy),
4) defines **what evidence must be produced** (compliance-ready outputs).

KNOTS are the bridge between:
- **MBSE/SysML architecture** (requirements, behavior, structure, interfaces),
- **agentic execution** (task decomposition, automation, prompting/tooling),
- **configuration control** (traceability, naming standard, release packs),
- **certification evidence** (VV packs, audit queries, signed manifests).

---

### 6.1 Core Concepts

**Knowledge Net**
A directed graph where nodes are controlled artifacts (models, specs, data, test results) and edges are typed relations (e.g., *satisfies*, *verifies*, *allocatesTo*, *dependsOn*, *evidencedBy*).

**Ontology Commitments**
A governed vocabulary and schema set that makes artifacts machine-checkable:
- controlled terms (AoR/STK, TYPE/STATUS, IDENTIFIER grammars),
- schemas (SSOT) for registers, evidence, and interfaces,
- constraints (allowed ranges, required fields, invariants).

**Tasking Strategy**
A rule set that converts "what we need" into "what agents do":
- permitted actions per AoR,
- sequencing rules and dependencies,
- minimum evidence required to close a KNOT.

**SysML Expression**
KNOTS are represented as:
- **activity** flows (task decomposition),
- **state** constraints (status transitions),
- **requirements** relations (satisfy/verify),
- **interfaces/ports** (ICDs and knowledge edges),
- **allocation** to AoR/STK owners and toolchains.

---

### 6.2 Governance: Controlled KNOT IDs (K01..K14)

KNOT IDs are **configuration-controlled tokens** used in filenames and gates.
- Allowed IDs: **K01..K14 only**
- Optional task suffix: **`-T###`** (e.g., `K06-T001`)
- Any new KNOT requires a **standard upgrade + CM approval**.

This ensures:
- stable automation rules,
- predictable portal navigation,
- auditable process boundaries.

---

### 6.3 KNOT Execution Model (Agentic Systems)

Each KNOT has:
- **Inputs**: required artifacts + schemas
- **Transforms**: allowed agentic actions (generate/validate/link/package)
- **Outputs**: NKUs (implicit) + evidence bundles
- **Guards**: PLC gates that must pass (PR-blocking)
- **Trace edges**: relations recorded into the traceability graph / ontology DB

A KNOT is "closed" only when:
- naming/identifier validators pass,
- evidence links resolve,
- exceptions are registered and approved (where allowed),
- release pack or checkpoint artifact is produced (when applicable).

---

### 6.4 Practical Mapping to Your STK Split (SE vs SPE)

- **STK_SE (Architecture & Governance)**  
  Owns: SysML structure, ontology commitments, interface/ICD rules, allocation logic, process constraints.

- **STK_SPE (Software & Prompting Engineering)**  
  Owns: agentic task runners, prompting specs, automation scripts, CI gates, validators, link-checkers, packaging tools.

KNOTS is the contract between them:
- SE defines "what must be true"
- SPE implements "how it is enforced and executed"
- CM/CERT decide "what is releasable / acceptable"

---

### 6.5 Minimal KNOT Metadata (Schema-ready)

Each KNOT definition should include:

- `knot_id`: K01..K14
- `purpose`: why this knot exists
- `inputs_required`: artifact types + schemas
- `outputs_required`: artifact types + evidence expectations
- `relations_required`: required trace edges (satisfy/verify/etc.)
- `aor_owner`: primary AoR/STK
- `dependencies`: other STKs and required handoffs
- `gates`: validators that must pass
- `close_criteria`: measurable completion criteria
- `exceptions_policy`: what can be waived, by whom, and how recorded

---

### 6.6 One-sentence definition (for README/Portal)

**KNOTS is design thinking operationalized as SysML-governed, agent-executable task networks, with ontology-backed validation and CM-controlled evidence closure.**

---

## 7. OPT-INS Framework

The **OPT-INS framework** defines six canonical axes for information topology:

| Axis | Domain | ATA Range | Description |
|------|--------|-----------|-------------|
| **O** | O-OPS/ORG | 01–05, 18 | Operations / Organization policy and governance |
| **P** | P-PROGRAM | 00, 11 | Program governance, baselines, registers |
| **T** | T-TECHNOLOGY | 06, 20–79 | On-board vehicle systems and subsystems |
| **I** | I-INFRASTRUCTURES | 07–10, 12, 80–89 | Off-board / ground infrastructure |
| **N** | N-NEURAL_NETWORKS | 90–99 | AI/ML, schemas, traceability, DPP, ledgers |
| **S** | S-SIM_TEST | 100–116 | Simulation, test, V&V evidence |

---

## 8. AoR / Stakeholder Codes

### 8.1 Primary Stakeholders (STK)

| Code | Name | Responsibility |
|------|------|----------------|
| **STK_CM** | Configuration Management | Naming standard, change control, baselines, registers, release governance |
| **STK_PMO** | Program Management Office | Planning, schedule, cost, risk, gates, stakeholder/program governance |
| **STK_SE** | Systems Engineering | Architecture, SysML/MBSE governance, ICD governance, requirements structure |
| **STK_DAB** | Digital Applications & Blockchains | Software, prompting/agent specs, automation, data engineering, schemas/SSOT, traceability, DPP/SBOM, manifests/signing, ledger/blockchain |
| **STK_PHM** | Physical & Mechanical Engineering | Aerostructures, mechanisms, hydraulics, pneumatics, actuation, landing gear |
| **STK_SAF** | Safety | FHA/PSSA/SSA logic, hazard controls, safety constraints, operational limits |
| **STK_CERT** | Certification / Compliance | Compliance evidence, certification packs, authority-facing deliverables |
| **STK_TEST** | Test / V&V | Test planning/execution, benches, results, anomalies, VV evidence |
| **STK_OPS** | Operations | ConOps, procedures, readiness, operational baselines and evidence |
| **STK_MRO** | Maintenance, Repair & Overhaul | Maintenance plans, servicing, facilities/tooling, maintainability |
| **STK_AI** | AI / ML Engineering & Assurance | Model registry, AI validation, monitoring, AI governance and assurance |
| **STK_CY** | Cybersecurity | IAM, ZTA, secure networks, hardening, cyber evidence and controls |
| **STK_SPACEPORT** | Spaceport / Ground Segment | Spaceport interfaces, off-board infrastructure, range constraints |
| **STK_CEGT** | Circular Economy and Green Tech | Circular systems, ESG reporting, alternative technologies, sustainability governance, social responsibility |

### 8.2 Deprecations

| Deprecated | Replacement | Note |
|------------|-------------|------|
| `STK_DATA` | **STK_DAB** | Unified digital AoR |
| `STK_SPE` | **STK_DAB** | Unified digital AoR |

---

## 9. v6.0 Nomenclature

# 9.2 Controlled Vocabulary — Nomenclature v6.0 

## 9.1 Canonical filename format (normative)

`[ATA]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__[SUBJECT]_[CATEGORY]_[TYPE]_[ISSUE-REV]_[STATUS].[EXT]`

---

## 9.2 Field Definitions (allowed values)

| # | Field | Allowed Values | Notes |
|---:|---|---|---|
| 1 | **ATA** | `00..116` | Must be in ATA allowlist (9.2.12). |
| 2 | **PROJECT** | `AMPEL360` | Fixed. |
| 3 | **PROGRAM** | `AIRT` \| `SPACET` | Advanced transport systems tokens. |
| 4 | **FAMILY** | `Q100` \| `Q200LR` \| `Q10` \| `QHABITAT` | Must satisfy PROGRAM×VERSION matrix (9.2.6). |
| 5 | **VARIANT** | `GEN` \| `BASELINE` \| `FLIGHT_TEST` \| `CERT` \| `MSN` \| `CUST` | Operating context; must appear once only. |
| 6 | **VERSION** | `PLUS` \| `PLUSULTRA` | Branding tier. |
| 7 | **MODEL** | `BB` \| `HW` \| `SW` \| `PR` | Body-Brain / Hardware / Software / Process. |
| 8 | **BLOCK** | `00` \| `10` \| `20` \| `30` \| `40` \| `50` \| `60` \| `70` \| `80` \| `90` | Domain/subsystem segmentation (9.2.7). |
| 9 | **PHASE** | `LC01..LC14` | Lifecycle phase (14 controlled values; see 9.2.8). |
| 10 | **KNOT** | `K01..K14` with optional `-T###` | Only K01..K14 allowed; optional suffix `-T001..-T999`. |
| 11 | **AoR** | `STK_*` allowlist (9.2.9) | Portal entry point / accountable owner. |
| — | **`__`** | exactly `__` | Mandatory separator before SUBJECT. |
| 12 | **SUBJECT** | lowercase kebab-case | `a-z0-9-` only (9.2.4). |
| 13 | **CATEGORY** | allowlist (9.2.10) | Governance intent of the artifact. |
| 14 | **TYPE** | allowlist (9.2.11) | Document/artifact genre; stable and short. |
| 15 | **ISSUE-REV** | `I##-R##` | `I01..I99` and `R01..R99` (00 reserved only if explicitly approved). |
| 16 | **STATUS** | allowlist (9.2.5) | Controlled state machine. |
| 17 | **EXT** | allowlist (9.2.13) | Repo-supported extensions only. |

---

## 9.2.1 Naming invariants (normative)

1) **Double-underscore** `__` is mandatory before SUBJECT.  
2) **No KNOT outside K01..K14** may appear anywhere in filename.  
3) **AoR must be one allowlisted STK token** (9.2.9).  
4) **BLOCK is domain segmentation, not lifecycle** (LC stays in PHASE).  
5) **One Official Chain** applies to `CATEGORY=DELIVERABLE` (9.2.15).  
6) **TEKNIA credentials** are `CATEGORY=REGISTRY` with `TYPE=BADGE|CERT|LIC` and AoR restricted (9.2.16).  

---

## 9.2.2 Regex constraints (validator-grade)

- **ATA**: `^(0[0-9]|[1-9][0-9]|1[01][0-6])$`
- **PROJECT**: `^AMPEL360$`
- **PROGRAM**: `^(AIRT|SPACET)$`
- **FAMILY**: `^(Q100|Q200LR|Q10|QHABITAT)$`
- **VARIANT**: `^(GEN|BASELINE|FLIGHT_TEST|CERT|MSN|CUST)$`
- **VERSION**: `^(PLUS|PLUSULTRA)$`
- **MODEL**: `^(BB|HW|SW|PR)$`
- **BLOCK**: `^(00|10|20|30|40|50|60|70|80|90)$`
- **PHASE**: `^LC(0[1-9]|1[0-4])$`
- **KNOT**: `^K(0[1-9]|1[0-4])(-T\d{3})?$`
- **AoR**: `^(STK_CM|STK_PMO|STK_SE|STK_DAB|STK_PHM|STK_SAF|STK_CERT|STK_TEST|STK_OPS|STK_MRO|STK_AI|STK_CY|STK_SPACEPORT|STK_CEGT)$`
- **SUBJECT**: `^[a-z0-9]+(?:-[a-z0-9]+)*$`
- **CATEGORY**: `^(DELIVERABLE|EVIDENCE|REGISTRY|SIGNOFF|EXPORT_CONTROL|INTERNAL_PRODUCTION)$`
- **TYPE**: build from allowlist in 9.2.11 (exact match).
- **ISSUE-REV**: `^I(0[1-9]|[1-9][0-9])-R(0[1-9]|[1-9][0-9])$`
- **STATUS**: `^(DRAFT|ACTIVE|RELEASED|SUPERSEDED|OBSOLETE)$`
- **EXT**: build from allowlist in 9.2.13 (exact match).

---

## 9.2.5 STATUS allowlist (controlled)

| STATUS | Meaning | Allowed for CATEGORY |
|---|---|---|
| `DRAFT` | Working / not approved | all |
| `ACTIVE` | In-force but changeable | all |
| `RELEASED` | Frozen baseline / publishable | DELIVERABLE, REGISTRY, EXPORT_CONTROL |
| `SUPERSEDED` | Replaced by a newer chain | DELIVERABLE, REGISTRY |
| `OBSOLETE` | Retired without replacement | DELIVERABLE, REGISTRY |

> Interpretation rule: If you need explicit “REVIEW/FREEZE” semantics, map `ACTIVE→REVIEW` and `RELEASED→FREEZE` for gating purposes without adding new STATUS tokens.

---

## 9.2.6 PROGRAM × VERSION → FAMILY matrix (CM-controlled)

| PROGRAM | VERSION | FAMILY | Description |
|---|---|---|---|
| `AIRT` | `PLUS` | `Q100` | BWB H₂-electric aircraft (INTEGRA) |
| `AIRT` | `PLUSULTRA` | `Q200LR` | Long-range advanced variant |
| `SPACET` | `PLUS` | `Q10` | Space transport baseline |
| `SPACET` | `PLUSULTRA` | `QHABITAT` | Habitat-class space vehicle |

---

## 9.2.7 BLOCK dictionary (domain/subsystem segmentation)

| BLOCK | Domain-Subsystem | Typical environment |
|---:|---|---|
| `00` | GENERAL | all |
| `10` | OPERATIONAL SYSTEMS | onboard / offboard / simtest |
| `20` | CYBERSECURITY | digital + onboard |
| `30` | DATA, COMMS AND REGISTRY | digital + onboard |
| `40` | PHYSICS (pressure/thermal/cryo/…) | onboard + simtest |
| `50` | PHYSICAL (aerostructures + information HW) | onboard / offboard |
| `60` | DYNAMICS (thrust, drag-lift, balancing, attitude, inerting) | onboard + simtest |
| `70` | RECIPROCITY & ALTERNATIVE ENGINES | onboard + simtest |
| `80` | RENEWABLE ENERGY & CIRCULARITY | onboard + offboard |
| `90` | CONNECTIONS & MAPPING | digital + onboard |

---

## 9.2.8 PHASE allowlist (LC01..LC14) — Controlled lifecycle definitions (normative)

The lifecycle **PHASE** token is one of the following **14 controlled values**. Meanings are fixed and must not be repurposed.

| PHASE | Name (canonical) | Scope (your definition) | Primary AoR(s) |
|---|---|---|---|
| **LC01** | Problem Statement / Generation / Prompting Engineering | Problem framing, ideation, NKU generation pathways, prompting engineering baselines, initial scope statements | STK_DAB, STK_SE, STK_CM |
| **LC02** | System Requirements | Requirement capture, allocation, traceability seeding, acceptance criteria definition | STK_SE, STK_CM |
| **LC03** | Design Models | Architecture + design models (SysML, design baselines, interface modeling) | STK_SE, STK_PHM, STK_DAB |
| **LC04** | Engineering Analysis & Calculation Models | Analyses, calculation models, trade studies, margins, model validation artifacts | STK_PHM, STK_SE, STK_DAB |
| **LC05** | Integration Testing & Prototyping (V&V / V6V) | Prototyping, integration campaigns, SIL/HIL/PIL, closure evidence production | STK_TEST, STK_SE, STK_DAB |
| **LC06** | Quality | QMS artifacts, process quality, audits, nonconformance management, quality gates | STK_CM, STK_PMO, STK_TEST |
| **LC07** | Safety and Security | Safety case, hazard controls, cybersecurity assurance objectives and evidence | STK_SAF, STK_CY, STK_SE |
| **LC08** | Certification and First Flight | Certification planning/execution, authority-facing packs, first-flight/mission readiness evidence | STK_CERT, STK_TEST, STK_OPS |
| **LC09** | Green Aircraft / Baselines | Sustainability baselines, circularity KPIs, green tech evidence, ESG reporting baselines | STK_PMO, STK_DAB, STK_CM |
| **LC10** | Industrialization / Serialization / Production Plan / CM | Industrial planning, production readiness, configuration baselines, manufacturing interfaces | STK_CM, STK_PMO, STK_PHM |
| **LC11** | Operations | ConOps, procedures, readiness, operational baselines, mission operations control | STK_OPS, STK_SPACEPORT, STK_CM |
| **LC12** | Support and Services | Customer support, service processes, service tooling, support documentation | STK_OPS, STK_MRO, STK_DAB |
| **LC13** | MRO and Sustainment | Maintenance programs, manuals, sustainment evidence, reliability/PHM integration | STK_MRO, STK_PHM, STK_DAB |
| **LC14** | Retirement Management and Circularity | End-of-life, retirement procedures, recycling/return flows, circularity closure | STK_PMO, STK_CM, STK_DAB |

### Notes (normative)
- PHASE is **lifecycle only**; it must not encode domain segmentation (that is BLOCK).
- PHASE is always exactly one of `LC01..LC14` and appears once in the filename.
- “V6V” naming is treated as part of the LC05 scope (Integration Testing & Prototyping).


---

## 9.2.9 AoR allowlist (portal entry points)

| AoR | Ownership boundary |
|---|---|
| `STK_CM` | Configuration management, nomenclature, baselines, change control, releases |
| `STK_PMO` | Planning, cost, risk, reviews/gates |
| `STK_SE` | Architecture & MBSE governance (SysML, ICD governance, allocations) |
| `STK_DAB` | Digital Applications & Blockchains (unifies software + prompting + data/traceability + registries + ledgers/signing + portal automation) |
| `STK_PHM` | Physical & mechanical engineering (aerostructures, gear, hydraulics, pneumatics, actuation) |
| `STK_SAF` | Safety engineering (hazards, constraints, safety case inputs) |
| `STK_CERT` | Certification/compliance packs and authority-facing evidence |
| `STK_TEST` | Test & VV governance (campaigns, benches, results, closure) |
| `STK_OPS` | Operations (ConOps/procedures/readiness) |
| `STK_MRO` | Maintenance/servicing/MRO deliverables (manuals, procedures, task cards) |
| `STK_AI` | AI/ML engineering & assurance (models, eval, drift/monitoring) |
| `STK_CY` | Cybersecurity (IAM, hardening, ZTA, cyber evidence) |
| `STK_SPACEPORT` | Spaceport/ground segment interfaces, constraints, emergency response infra |
| `STK_CEGT` | Circular economy, ESG reporting, alternative technologies, sustainability governance, social responsibility |

---

## 9.2.10 CATEGORY allowlist (governance intent)

| CATEGORY | Meaning | Default visibility |
|---|---|---|
| `DELIVERABLE` | Official publishable artifact (one official chain) | Portal default |
| `EVIDENCE` | Change note NKUs + proofs (many allowed) | Linked from deliverables |
| `REGISTRY` | SSOT registers, indexes, catalogs, schemas, ontologies, TEKNIA | Portal default (where applicable) |
| `SIGNOFF` | Formal approvals / signature records | Restricted |
| `EXPORT_CONTROL` | Controlled export/disclosure packages | Restricted |
| `INTERNAL_PRODUCTION` | Working/internal production artifacts | Hidden by default |

---

## 9.2.11 TYPE allowlist (stable genres)

### A) Governance / engineering documents
`CHARTER`, `README`, `STD`, `POL`, `PROC`, `PLAN`, `REQ`, `SPEC`, `ARCH`, `ICD`, `MOD`

### B) Manuals / publications (MRO/OPS deliverables)
`MAN`  
> Manual subtype is encoded in SUBJECT (e.g., `amm-*`, `ipc-*`, `srm-*`, `tsm-*`, `wdm-*`, `qrh-*`, `fcom-*`).

### C) Verification / evidence documents
`TST`, `CASE`, `LOG`, `RPT`, `NCR`, `DEC`, `MIN`, `DIA`, `TAB`, `LST`

### D) Control / registries / navigation
`IDX`, `REG`, `CAT`

### E) Digital governance, ledgers, exports
`SCHEMA`, `ONTO`, `TRACE`, `DPP`, `SBOM`, `BOM`, `MAP`, `MANIFEST`, `EVD`

### F) TEKNIA credentials (if enabled)
`BADGE`, `CERT`, `LIC`

---

## 9.2.12 ATA allowlist (00–116) — canonical descriptions

| ATA | Description |
|---:|---|
| 00 | GENERAL |
| 01 | OPERATIONS/ORGANIZATION POLICY (RESERVED) |
| 02 | OPERATIONS/ORGANIZATION (RESERVED) |
| 03 | SUPPORT INFORMATION (RESERVED) |
| 04 | AIRWORTHINESS LIMITATIONS / OPERATIONAL LIMITS (RESERVED) |
| 05 | TIME LIMITS / MAINTENANCE CHECKS |
| 06 | DIMENSIONS AND AREAS |
| 07 | LIFTING AND SHORING |
| 08 | LEVELING AND WEIGHING |
| 09 | TOWING AND TAXIING |
| 10 | PARKING / MOORING / STORAGE / RETURN TO SERVICE |
| 11 | PLACARDS AND MARKINGS |
| 12 | SERVICING |
| 13 | NOT ASSIGNED / RESERVED |
| 14 | NOT ASSIGNED / RESERVED |
| 15 | NOT ASSIGNED / RESERVED |
| 16 | NOT ASSIGNED / RESERVED |
| 17 | NOT ASSIGNED / RESERVED |
| 18 | NOISE & VIBRATION MANAGEMENT |
| 19 | NOT ASSIGNED / RESERVED |
| 20 | STANDARD PRACTICES - AIRFRAME |
| 21 | AIR CONDITIONING / ENVIRONMENTAL CONTROL |
| 22 | AUTO FLIGHT / GUIDANCE-NAVIGATION-CONTROL |
| 23 | COMMUNICATIONS |
| 24 | ELECTRICAL POWER |
| 25 | EQUIPMENT / FURNISHINGS |
| 26 | FIRE PROTECTION |
| 27 | FLIGHT CONTROLS |
| 28 | FUEL / PROPELLANT SYSTEMS |
| 29 | HYDRAULIC POWER |
| 30 | ICE AND RAIN PROTECTION / ATMOSPHERIC PROTECTION |
| 31 | INDICATING / RECORDING SYSTEMS |
| 32 | LANDING GEAR |
| 33 | LIGHTS |
| 34 | NAVIGATION |
| 35 | OXYGEN / LIFE SUPPORT GAS |
| 36 | PNEUMATIC / GAS DISTRIBUTION |
| 37 | VACUUM (IF APPLICABLE) |
| 38 | WATER / WASTE (LIFE SUPPORT) |
| 39 | ELECTRICAL / ELECTRONIC PANELS & MULTIPURPOSE COMPONENTS |
| 40 | MULTI-SYSTEM / INTEGRATION SERVICES |
| 41 | WATER BALLAST / MASS TRIM (IF APPLICABLE) |
| 42 | INTEGRATED MODULAR AVIONICS / COMPUTE PLATFORM |
| 43 | RESERVED / PLATFORM INTEGRATION |
| 44 | CABIN SYSTEMS |
| 45 | CENTRAL MAINTENANCE SYSTEM / HEALTH MONITORING |
| 46 | INFORMATION SYSTEMS / DATA NETWORKS |
| 47 | INERT GAS SYSTEM / TANK INERTING |
| 48 | IN-FLIGHT FUEL DISPENSING (RESERVED) |
| 49 | AIRBORNE AUXILIARY POWER / APU / AUX POWER MODULES |
| 50 | CARGO AND ACCESSORY COMPARTMENTS |
| 51 | STANDARD PRACTICES & STRUCTURES - GENERAL |
| 52 | DOORS / HATCHES |
| 53 | FUSELAGE / PRESSURE VESSEL |
| 54 | NACELLES / PYLONS (IF APPLICABLE) |
| 55 | STABILIZERS / CONTROL SURFACES |
| 56 | WINDOWS / VIEWPORTS |
| 57 | WINGS / LIFTING SURFACES |
| 58 | RESERVED / EXTENSION |
| 59 | RESERVED / EXTENSION |
| 60 | STANDARD PRACTICES - PROPELLER / ROTOR |
| 61 | PROPELLERS / PROPULSORS (IF APPLICABLE) |
| 62 | ROTORS (IF APPLICABLE) |
| 63 | ROTOR DRIVES (IF APPLICABLE) |
| 64 | TAIL ROTOR (IF APPLICABLE) |
| 65 | TAIL ROTOR DRIVE (IF APPLICABLE) |
| 66 | FOLDING BLADES / TAIL PYLON (IF APPLICABLE) |
| 67 | ROTORS FLIGHT CONTROL (IF APPLICABLE) |
| 68 | RESERVED / EXTENSION |
| 69 | RESERVED / EXTENSION |
| 70 | STANDARD PRACTICES - ENGINE |
| 71 | POWER PLANT / PROPULSION INTEGRATION |
| 72 | ENGINE (TURBINE/ROCKET/HYBRID AS APPLICABLE) |
| 73 | ENGINE FUEL AND CONTROL |
| 74 | IGNITION |
| 75 | AIR (BLEED / INLET / APU AIR) / INTAKE |
| 76 | ENGINE CONTROLS |
| 77 | ENGINE INDICATING |
| 78 | EXHAUST / PLUME MANAGEMENT |
| 79 | OIL / LUBRICATION |
| 80 | OFF-BOARD / AIRPORT / SPACEPORT INFRASTRUCTURES (MASTER) |
| 81 | OFF-BOARD ENERGY / CRYO SERVICES |
| 82 | OFF-BOARD MRO FACILITIES / TOOLING / LOGISTICS |
| 83 | GROUND COMMS / DATA EXCHANGE INFRA (GATEWAYS, EDGE) |
| 84 | SPACEPORT SAFETY / EMERGENCY RESPONSE INFRA |
| 85 | CIRCULARITY INFRA (RETURN FLOWS, RECYCLING, CO2/H2 LOOPS) |
| 86 | OFF-BOARD DIGITAL SERVICES PLATFORM (PORTALS, ORCHESTRATION) |
| 87 | IDENTITY / ACCESS / CYBERSECURITY INFRA (PHYSICAL+DIGITAL) |
| 88 | GSE CONFIGURATION / ASSET MANAGEMENT |
| 89 | TEST RIGS / INSTRUMENTATION INFRA (GROUND) |
| 90 | AI/ML MODEL REGISTRY & MODEL LIFECYCLE |
| 91 | DATA SCHEMAS / ONTOLOGIES / SEMANTIC MODEL (SSOT) |
| 92 | WIRING / CONNECTIVITY GRAPHS & HARNESS DATA PACKAGES |
| 93 | TRACEABILITY GRAPH (REQ↔DESIGN↔VV↔OPS) & EVIDENCE LEDGERS |
| 94 | DPP CORE (DIGITAL PRODUCT PASSPORT) & PROVENANCE |
| 95 | SBOM / SWHW BOM / MODEL BOM EXPORTS |
| 96 | AI GOVERNANCE (RISK, ASSURANCE, MONITORING, DRIFT/BIAS) |
| 97 | CHANGE IMPACT ANALYTICS (WIRING/CONFIG/TRACE) |
| 98 | SIGNED RELEASE PACKS / MANIFESTS / EXPORTS |
| 99 | MASTER REGISTERS (GOLDEN RECORDS) & REFERENCE DATASETS |
| 100 | SIM/TEST GOVERNANCE (PLANS, ENVIRONMENTS, QUALITY) |
| 101 | DIGITAL TWIN CONFIGURATION & SIM MODEL CATALOG |
| 102 | SCENARIO LIBRARIES (MISSION, OFF-NOMINAL, EMERGENCY) |
| 103 | SIL (SOFTWARE-IN-THE-LOOP) AUTOMATION |
| 104 | HIL (HARDWARE-IN-THE-LOOP) BENCHES |
| 105 | PIL / TARGET EXECUTION (PROCESSOR/PLATFORM-IN-THE-LOOP) |
| 106 | TEST PROCEDURES / TEST CASES / ACCEPTANCE CRITERIA |
| 107 | TEST DATA / INPUT DECKS / STIMULI |
| 108 | TEST RESULTS / REPORTING / ANOMALY MANAGEMENT |
| 109 | VV EVIDENCE PACKS (LINKED TO TRACEABILITY) |
| 110 | QUALIFICATION / ENVIRONMENTAL TESTING (SPACE-T) |
| 111 | SYSTEM INTEGRATION TESTING (END-TO-END) |
| 112 | MISSION/FLIGHT TESTING (OPERATIONAL DEMOS) |
| 113 | UNCERTAINTY QUANTIFICATION (UQ) / MONTE CARLO / SENSITIVITY |
| 114 | AI/ML VALIDATION SUITES & MONITORING TESTS |
| 115 | CERTIFICATION TESTS (SW/HW/ECSS-DO) & COMPLIANCE REPORTS |
| 116 | SIM/TEST ARCHIVES & BASELINES (FROZEN CAMPAIGNS) |

---

## 9.2.13 EXT allowlist (repo-supported)

### Primary (GitHub-first)
`md`, `txt`, `yml`, `yaml`, `json`, `csv`, `svg`, `png`

### Optional (only if explicitly allowed in-repo)
`docx`, `xlsx`, `pptx`

---

## 9.2.14 Category/AoR constraints (normative)

1) `CATEGORY=SIGNOFF` → AoR must be `STK_CM` or `STK_CERT` only.  
2) `CATEGORY=EXPORT_CONTROL` → AoR must be `STK_CM` or `STK_CERT` only.  
3) `TYPE in {BADGE,CERT,LIC}` → AoR must be `STK_CM` or `STK_CERT` only.  

---

## 9.2.15 One Official Chain rule (normative)

Define key:
`K = (ATA,PROJECT,PROGRAM,FAMILY,VARIANT,VERSION,MODEL,BLOCK,PHASE,AoR,SUBJECT,CATEGORY,TYPE)`

- If `CATEGORY=DELIVERABLE`:
  - `COUNT(status ∈ {ACTIVE, RELEASED}) ≤ 1`  
  - (`ACTIVE` = “REVIEW-equivalent”; `RELEASED` = “FREEZE-equivalent”)
- If `CATEGORY=REGISTRY`:
  - SSOT rule applies: exactly one canonical register per scope.
- If `CATEGORY=EVIDENCE`:
  - No uniqueness constraint, but must link to impacted DELIVERABLE(s).

---

## 9.2.16 TEKNIA credential binding rule (normative)

For `TYPE in {BADGE,CERT,LIC}` (CATEGORY `REGISTRY`):
- must bind to one or more NKUs via:
  - `repo_relative_path`
  - `sha256`
  - optional `commit`
- credential schema must be versioned (`TYPE=SCHEMA`) and validated.
- issuance AoR restricted: `STK_CM` or `STK_CERT` only.

---

## 9.2.17 Examples (v6.0)

**DELIVERABLE (official)**
`00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__nomenclature-standard_DELIVERABLE_STD_I01-R01_ACTIVE.md`

**EVIDENCE (change note NKU)**
`00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K04_STK_CM__nomenclature-change-note_EVIDENCE_RPT_I01-R01_ACTIVE.md`

**REGISTRY (TEKNIA credential)**
`94_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_30_LC06_K06_STK_CERT__teknia-credential_REGISTRY_CERT_I01-R01_RELEASED.json`
