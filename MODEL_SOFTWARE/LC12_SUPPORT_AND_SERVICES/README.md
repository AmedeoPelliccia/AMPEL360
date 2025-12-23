# LC12_SUPPORT_AND_SERVICES
**Lifecycle Phase:** LC12 — Support and Services (Customer Support + Service Tooling)

## Purpose
This directory contains **LC12 software artifacts** that support customer support and service
processes for the `MODEL_SOFTWARE` portal node (ATA-00 / Block 10), including:
- customer support tooling and service process automation,
- support documentation generation utilities,
- ticketing and service-request integrations,
- knowledge base management tooling,
- customer support interface applications/portals (service-facing, not product runtime),
- service tooling used to manage and deliver support outcomes.

LC12 is the authoritative location for **service delivery tooling**: how support is requested,
triaged, resolved, documented, and reported.

## Contents (What belongs in LC12)
Artifacts in this directory typically include:

### A) Customer support tooling
- Customer support systems integrations (ticketing, incident/request intake)
- Case management helpers (triage workflows, escalation rules, SLA tracking)

### B) Service process automation
- Automated service workflows (intake → assign → resolve → close)
- Service reporting utilities (support KPIs, response time metrics, backlog trends)

### C) Support documentation generators
- Support documentation and knowledge article generators
- Publication utilities for service documentation baselines (program-defined formats)

### D) Knowledge base and customer support interfaces
- Knowledge base management tools (indexing, search, article lifecycle controls)
- Customer-facing support portals/interfaces used for service interaction and request tracking

> Note: LC12 is about **support and service processes**. Operational baselines and mission operations tooling
> belong to LC11. Maintenance programs, sustainment evidence, and reliability/PHM integration belong to LC13.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC12`
- `KNOT` binding **as applicable** (commonly K12 for support/services tooling)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- supports customer service activities (ticketing, case management, support workflows),
- automates service processes and service reporting,
- generates support documentation and knowledge base content (as governed artifacts),
- integrates service tooling with operational and maintenance stakeholders,
- provides customer-facing support interfaces for service interaction (requests, status, knowledge).

Do **not** place software here when it:
- primarily supports mission/operations runtime or operational baselines (use LC11),
- primarily supports maintenance programs, sustainment engineering, or PHM reliability workflows (use LC13),
- is QMS/audit/nonconformance tooling (use LC06),
- is release packaging/serialization CM tooling (use LC10),
- is cross-phase portal governance/templates/contracts (use LC00).

## Ownership
**AoR (owners): STK_OPS, STK_MRO, STK_DAB**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section
