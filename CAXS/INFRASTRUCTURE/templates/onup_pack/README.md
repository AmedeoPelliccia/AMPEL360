# ONUP Template Pack (Node Uncertainty Pack)

## Purpose
This template pack instantiates the mandatory SSOT artifacts for any OPT-INS node:
Axis (O/P/T/I/N/S) + ATA + BLOCK + PHASE within a selected Program Slice.

## How to use (operator procedure)
1) Choose: PROGRAM / FAMILY / VARIANT / VERSION
2) Choose: Axis / ATA / BLOCK / PHASE / MODEL
3) Create the ONUP artifacts in the node SSOT location (Domain view).
4) Replace placeholders:
   - {{AXIS}}, {{ATA}}, {{PROGRAM}}, {{FAMILY}}, {{VARIANT}}, {{VERSION}}, {{MODEL}}, {{BLOCK}}, {{PHASE}}
   - {{KNOT}} (typically K01 for node definition; tasks can span K01–K14)
   - {{PRIMARY_AOR}} (e.g., STK_SE)
   - {{ISSUE_REV}} (e.g., I01-R01)
   - {{STATUS}} (e.g., ACTIVE)
   - {{NODE_SUBJECT}} (kebab-case; include axis/ata/block semantics)

## Output naming (v6.0 canonical)
All governed ONUP outputs MUST be created using canonical v6.0 filenames:
[ATA]_[PROJECT=AMPEL360]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__[SUBJECT]_[CATEGORY]_[TYPE]_[ISSUE-REV]_[STATUS].[EXT]

Templates in this folder are not governed artifacts. The instantiated ONUP outputs are governed.

## Mandatory ONUP artifacts
1) Node tasklist index (REGISTRY/IDX) - MD
2) Problem statement + hypotheses (DELIVERABLE/STD or SPEC) - MD
3) ATA impact analysis matrix (REGISTRY/TAB) - CSV
4) AoR RACI matrix (REGISTRY/TAB) - CSV
5) Roadmap registry (REGISTRY/REG) - CSV
6) Task registry (REGISTRY/REG) - CSV
7) Evidence index (REGISTRY/IDX) - MD
8) Signoff index (REGISTRY/IDX) - MD

## Notes
- SIGNOFF and EXPORT_CONTROL outputs must be owned by AoR ∈ {STK_CM, STK_CERT}.
- One Official Chain uniqueness applies to (PGK, AoR, SUBJECT, CATEGORY, TYPE).

## Version
**Template Version:** 1.0  
**Last Updated:** 2025-12-19  
**Maintained By:** STK_CM + STK_DAB
