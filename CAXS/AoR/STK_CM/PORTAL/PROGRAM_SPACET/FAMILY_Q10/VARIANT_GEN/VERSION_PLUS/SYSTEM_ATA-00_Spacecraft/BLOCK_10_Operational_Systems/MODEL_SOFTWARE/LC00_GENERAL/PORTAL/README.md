# PORTAL/ — AoR Routing, Policy Gates, and Audit/Provenance Utilities

**Location:** `LC00_GENERAL/PORTAL/`  
**Owner (AoR):** STK_DAB (Digital Applications & Blockchains)  
**Status:** ACTIVE

---

## Purpose

This directory contains **portal integration utilities** that support the CAXS Portal (CA360º) operating model, including AoR routing, policy gates, audit logging, and provenance tracking.

## Scope

### What belongs here:
- **AoR routing logic** for role-based portal navigation
- **Policy gate implementations** (validators, enforcement rules)
- **Audit logging utilities** (provenance, timestamps, hashes)
- **Portal integration adapters** (indexers, registry connectors)
- **Entitlement checking** utilities (TALF integration)
- **Notification helpers** for portal events and alerts

### What does NOT belong here:
- Frontend UI components (place in infrastructure/portals)
- Portal contracts (place in respective AoR directories)
- Schemas (place in SCHEMAS/)
- General libraries (place in LIB/)

---

## Guidelines

1. **Role-based Access**: Implement AoR-aware routing and permissions
2. **Policy Enforcement**: Gates must be PR-blocking and auditable
3. **Audit Trail**: All portal actions must be logged with provenance
4. **Determinism**: Policy decisions must be reproducible
5. **Integration**: Utilities must support backend services (TALF, indexers)

---

## Expected Utilities

Key utilities that should be developed here:

- **AoR Router**: Route requests to appropriate AoR entry points
- **Policy Gate Engine**: Evaluate and enforce governance gates
- **Audit Logger**: Log portal actions with timestamps and hashes
- **Provenance Stamper**: Generate provenance records for artifacts
- **Registry Connector**: Interface with SSOT registries and indexes
- **TALF Client**: Integrate with Tool Access & Licensing Fabric
- **Notification Service**: Send alerts and notifications to stakeholders

---

## Portal Gate Types

Gates implemented in this directory:

### Gate A — Intent Reference Validity
- Validates vision/mission/scope/outcome IDs
- Checks intent hash matches computed value
- Ensures IDs exist in SSOT registries

### Gate B — CIPP Determinism
- Validates target refs exist
- Checks hashes match
- Verifies status constraints
- Ensures dependencies resolvable

### Gate C — Outcome Trace Completeness
- Validates outcome links to evidence
- Checks deterministic target chains (CIPPs)
- Verifies task outputs and evidence (KNOTs)

### Gate F — Portal Contract Validation
- Validates AoR contracts exist and well-formed
- Checks required sections present
- Validates MUST features (F01-F09)
- Cross-validates tool references

---

## Utility Organization

```
PORTAL/
├── routing/
│   ├── aor_router.py
│   ├── context_builder.py
│   └── workspace_selector.py
├── gates/
│   ├── gate_engine.py
│   ├── intent_validator.py
│   ├── cipp_validator.py
│   └── contract_validator.py
├── audit/
│   ├── audit_logger.py
│   ├── provenance_stamper.py
│   └── event_recorder.py
├── integration/
│   ├── registry_connector.py
│   ├── talf_client.py
│   └── notification_service.py
└── reporting/
    ├── gate_reporter.py
    └── dashboard_builder.py
```

---

## Usage

Portal utilities support governance and integration:

```python
# Example Python usage
from LC00_GENERAL.PORTAL.routing import aor_router
from LC00_GENERAL.PORTAL.gates import gate_engine
from LC00_GENERAL.PORTAL.audit import audit_logger

# Route to AoR entry point
entry_point = aor_router.route(aor='STK_CM', user_role='engineer')

# Evaluate gate
gate_result = gate_engine.evaluate(
    gate='intent_validity',
    artifact='path/to/artifact.md'
)

# Log audit event
audit_logger.log_event(
    event_type='gate_evaluation',
    gate='intent_validity',
    result=gate_result,
    artifact_hash='sha256...'
)
```

---

## Maintenance

- Keep gate implementations aligned with governance policies
- Update routing logic when new AoRs are added
- Maintain audit trail retention (7-year requirement)
- Coordinate with STK_CM for policy changes
- Test gates with representative artifacts
- Document gate behavior and failure modes

---

**References:**
- See parent README: `../README.md`
- Portal Operating Model: Main README Section 5
- AoR Portal Feature Model: Main README Section 6
- TALF Service Specification: `CAXS/INFRASTRUCTURE/portals/...__talf-service-specification_...`
- Portal Contracts: `CAXS/AoR/STK_*/PORTAL/*__portal-contract_...`
