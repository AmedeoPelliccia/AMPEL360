---
title: "Signoff Index — {{AXIS}} / ATA {{ATA}} / BLOCK {{BLOCK}} / {{PHASE}}"
project: "AMPEL360"
issue_rev: "{{ISSUE_REV}}"
status: "{{STATUS}}"
node_subject: "{{NODE_SUBJECT}}"
---

# Signoff Index — {{AXIS}} / ATA {{ATA}} / BLOCK {{BLOCK}} / {{PHASE}}

## Intent
Record authoritative decisions (DEC/MIN) required to close uncertainties and/or approve releases.

## Signoff records
| Signoff ID | Decision Subject | Required By | Authority AoR | Status | Link |
|---|---|---|---|---|---|
| S-001 | {{DECISION_SUBJECT}} | Kxx-T### / Criterion C# | STK_CM or STK_CERT | DRAFT/ACTIVE/RELEASED | {{LINK}} |
| S-002 | {{DECISION_SUBJECT}} | Kxx-T### / Criterion C# | STK_CM or STK_CERT | DRAFT/ACTIVE/RELEASED | {{LINK}} |

## Constraints (normative)
- SIGNOFF artifacts must be owned by AoR ∈ {STK_CM, STK_CERT}.
- If SIGNOFF is required, node outputs cannot be RELEASED without at least one RELEASED signoff record covering the closure scope.
