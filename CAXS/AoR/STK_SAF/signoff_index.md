# STK_SAF Signoff Index

**AoR:** STK_SAF (Safety)  
**Status:** ACTIVE  
**Version:** 1.0  
**Last Updated:** 2025-12-19

## Purpose

This index tracks formal approvals and signoffs for STK_SAF deliverables. All CATEGORY=SIGNOFF artifacts must be listed here with approval evidence.

## Signoff Authority

**Primary Authority:** STK_SAF  
**Secondary Approval (Required):** STK_CM or STK_CERT  
**Governance:** Per category_aor_constraints.json

## Active Signoffs

Currently no signoffs. Signoffs will be indexed here as deliverables are approved.

## Signoff Template

```yaml
signoff_id: SGN-STK_SAF-XXX
deliverable_ref: ""
deliverable_path: "CAXS/..."
approver: STK_SAF
co_approver: STK_CM | STK_CERT
approval_date: YYYY-MM-DD
status: PENDING | APPROVED | REJECTED
signoff_artifact: ""
evidence_bundle: ""
audit_trail: ""
```

## Approval Workflow

1. **Preparation:** DELIVERABLE artifact reaches DRAFT status
2. **Review:** STK_SAF technical review complete
3. **Co-Review:** STK_CM or STK_CERT governance review
4. **Signoff:** Both approvers sign
5. **Registration:** Signoff registered in this index
6. **Ledger:** Signoff recorded in release-packs ledger
7. **Status Update:** DELIVERABLE status: DRAFT → ACTIVE/RELEASED

## Archived Signoffs

None yet. Historical signoffs will be preserved here.

## Version Control

**Index Version:** 1.0  
**Update Frequency:** Per signoff event
