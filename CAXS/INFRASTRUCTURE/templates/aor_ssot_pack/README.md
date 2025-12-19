# AoR SSOT Registry Pack Template

This directory contains templates for creating consistent SSOT (Single Source of Truth) registries for each Area of Responsibility (AoR) stakeholder.

## Template Files

1. **roadmap_registry_template.md** - Planned work tracking
2. **task_registry_template.md** - Active task execution
3. **evidence_index_template.md** - Evidence artifact cataloguing
4. **signoff_index_template.md** - Formal approvals tracking

## Usage

To create a complete SSOT registry pack for a new AoR:

```bash
# Manual method
cp roadmap_registry_template.md ../../AoR/STK_<CODE>/roadmap_registry.md
cp task_registry_template.md ../../AoR/STK_<CODE>/task_registry.md
cp evidence_index_template.md ../../AoR/STK_<CODE>/evidence_index.md
cp signoff_index_template.md ../../AoR/STK_<CODE>/signoff_index.md

# Update placeholders:
# - {{AOR_CODE}} → STK_<CODE>
# - {{AOR_NAME}} → Full stakeholder name
# - {{PRIMARY_ATA}} → Primary ATA chapter(s)
# - {{PRIMARY_LC}} → Primary lifecycle phase(s)
```

## Validation

All AoR directories must have these 4 registries present and linked from the portal entrypoints index.

**CI Rule:** Portal gates will verify AoR pack completeness.

## Version

**Template Version:** 1.0  
**Last Updated:** 2025-12-19  
**Maintained By:** STK_CM + STK_DAB
