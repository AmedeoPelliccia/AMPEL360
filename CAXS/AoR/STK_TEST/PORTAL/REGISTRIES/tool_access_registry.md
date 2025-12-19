# STK_TEST — PORTAL Tool Access Registry

**AoR:** STK_TEST (Test & V&V)  
**Status:** ACTIVE  
**Version:** 1.0  
**Last Updated:** 2025-12-19

## Purpose

This registry documents the tools accessible through the CA360º Portal for Test & V&V activities, governed by the Tool Access & Licensing Fabric (TALF).

## Required Tools

The following tools are cataloged for STK_TEST in the portal-wide tool catalog:

- `labview-test-vdi` (see CAXS/INFRASTRUCTURE/access/tool_catalog.yaml)
- `python-jupyter-container` (see CAXS/INFRASTRUCTURE/access/tool_catalog.yaml)
- `matlab-vdi-analysis` (see CAXS/INFRASTRUCTURE/access/tool_catalog.yaml)

## Access Control

Access to these tools is governed by:
- **Tool Catalog:** `CAXS/INFRASTRUCTURE/access/tool_catalog.yaml`
- **Entitlement Matrix:** `CAXS/INFRASTRUCTURE/access/entitlement_matrix.csv`
- **License Events:** `CAXS/INFRASTRUCTURE/access/license_events_registry.md`

## Preflight Checks

Before launching any tool, the portal performs preflight checks:
1. SSO authentication valid
2. User entitlement group membership verified
3. License availability confirmed (for licensed tools)
4. Compute resource capacity checked

## Audit Trail

All tool access events are recorded per the TALF audit schema:
- Login events
- Launch events
- License checkout/failure events
- Usage tracking
- Export events

See: `CAXS/INFRASTRUCTURE/access/license_events_registry.md` for event schema

## Evidence Linkage

Tool access events can be referenced as evidence for LC gates where required.

## Related Documentation

- **TALF Overview:** `CAXS/INFRASTRUCTURE/access/README.md`
- **AoR Portal Contracts:** `CAXS/INFRASTRUCTURE/portals/README.md`
- **PHM TALF Deliverable (Reference):** `CAXS/AoR/STK_PHM/PORTAL/DELIVERABLES/00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_00_LC01_K01_STK_PHM__talf-tool-access-licensing-fabric_DELIVERABLE_PROC_I01-R01_DRAFT.md`

## Version Control

**Registry Version:** 1.0  
**Governance:** STK_CM approval required for tool additions  
**Update Frequency:** As needed when tools added/removed
