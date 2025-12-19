# {{AOR_CODE}} Evidence Index

**AoR:** {{AOR_CODE}} ({{AOR_NAME}})  
**Status:** ACTIVE  
**Version:** 1.0  
**Last Updated:** YYYY-MM-DD

## Purpose

This index catalogues evidence artifacts produced by {{AOR_CODE}} stakeholder.

## Evidence Artifacts

Currently no evidence artifacts. Evidence will be indexed here as work progresses.

## Evidence Categories

Define specific evidence categories relevant to {{AOR_CODE}} responsibilities.

## Evidence Template

```yaml
evidence_id: EVD-{{AOR_CODE}}-XXX
artifact_name: ""
artifact_path: "CAXS/..."
category: EVIDENCE
type: REPORT | ASSESSMENT | VALIDATION | ANALYSIS
related_to:
  task_id: TASK-{{AOR_CODE}}-XXX
  roadmap_id: RDM-{{AOR_CODE}}-XXX
created_date: YYYY-MM-DD
status: DRAFT | ACTIVE | SUPERSEDED
hash: sha256:...
trace_links:
  - requirement: ""
  - design: ""
  - verification: ""
```

## Trace to Ledgers

Evidence artifacts are automatically registered in:
- **Knowledge Ledger:** `CAXS/LEDGERS/knowledge-ledger/`
- **Traceability Graph:** `CAXS/LEDGERS/traceability-graph/`
- **Digital Product Passport:** `CAXS/LEDGERS/digital-product-passport/` (where applicable)

## Version Control

**Index Version:** 1.0  
**Update Frequency:** Continuous (as evidence is produced)
