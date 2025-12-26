# AGENTS — Portal-Aware Assistants (AoR Routing, Tool Access Control, Guardrails)

**Parent Context:** LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING  
**Purpose:** Portal-aware agent implementations with governance and access control  
**Status:** Active (Portal Baseline)

---

## 1. Purpose

This directory contains **portal-aware agent implementations** that:
- Provide intelligent assistance within governance boundaries
- Route requests based on AoR and context
- Enforce tool access control and entitlements
- Apply guardrails and policy constraints
- Integrate with the CAXS portal framework

---

## 2. What Belongs Here

### Portal-Aware Assistants
- AoR-specific agent implementations
- KNOT-aware task assistants
- Context-sensitive help agents
- Generation assistants with governance

### Routing Logic
- AoR-based request routing
- Context-aware agent selection
- Escalation and handoff logic
- Multi-agent coordination

### Access Control
- Tool access validation
- Entitlement checking
- License management integration
- Permission enforcement

### Guardrails
- Input validation and sanitization
- Output filtering and safety checks
- Policy compliance verification
- Red team checks
- Constraint enforcement

---

## 3. Agent Types

### Task Assistants
- **Problem Statement Assistant:** Helps structure problem statements
- **Requirements Assistant:** Assists with requirements capture
- **Prompt Composition Assistant:** Guides prompt creation
- **Evaluation Assistant:** Interprets evaluation results

### Governance Assistants
- **AoR Router:** Routes requests to appropriate stakeholders
- **Policy Advisor:** Provides guidance on constraints and requirements
- **Compliance Checker:** Validates against standards
- **Evidence Linker:** Ensures traceability

### Tool Assistants
- **Tool Selector:** Recommends appropriate tools
- **Tool Launcher:** Coordinates tool execution
- **License Manager:** Manages tool access and licensing
- **Integration Helper:** Assists with tool integration

---

## 4. Agent Capabilities

All agents must:
- Understand portal context (AoR, KNOT, user, program, system)
- Respect access control and entitlements
- Apply appropriate guardrails
- Maintain traceability
- Log interactions for audit
- Handle errors gracefully

---

## 5. AoR-Aware Routing

Agents must route based on:
- **AoR ownership:** Direct to responsible stakeholder
- **KNOT context:** Align with task type
- **Tool requirements:** Consider tool access/licensing
- **Policy constraints:** Enforce boundaries
- **Expertise match:** Route to qualified personnel

---

## 6. Tool Access Control

### Access Validation
- Check user entitlements via IAM/SSO
- Verify license availability
- Validate tool permissions
- Check context appropriateness

### Tool Gating
- Enforce preflight requirements
- Apply usage policies
- Log access events
- Handle access denial gracefully

### License Management
- Check license pool availability
- Coordinate concurrent usage
- Queue requests when needed
- Release licenses properly

---

## 7. Guardrails

### Input Guardrails
- Validate input format and content
- Check for malicious input
- Enforce length/complexity limits
- Verify context appropriateness

### Output Guardrails
- Filter sensitive information
- Apply safety checks
- Validate output format
- Ensure policy compliance

### Process Guardrails
- Enforce workflow constraints
- Validate state transitions
- Check authorization at each step
- Maintain audit trail

---

## 8. Naming Conventions

Follow v6.0 nomenclature:
- `MODEL=SW`
- `PHASE=LC01`
- `CATEGORY=INTERNAL_PRODUCTION` for agent code
- `TYPE` as appropriate

**Example:**
```
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__aor-routing-agent_INTERNAL_PRODUCTION_SPEC_I01-R01_ACTIVE.py
```

---

## 9. Configuration

Agents should be configured via:
- Portal context (runtime)
- Configuration files (YAML/JSON)
- Environment variables
- User preferences (where appropriate)

Agent configurations must define:
- Scope and boundaries
- Allowed operations
- Access control rules
- Guardrail settings
- Integration endpoints

---

## 10. Integration Points

**Inputs:**
- Portal context (user, AoR, KNOT, program, system)
- User requests and queries
- PROMPTS/ for prompt access
- SCHEMAS/ for validation

**Outputs:**
- Routed requests
- Generated artifacts
- Execution logs
- Evidence records

**Integration:**
- ENGINES/ for prompt execution
- EVAL/ for quality checking
- CI/ for validation
- Portal services (TALF, IAM, etc.)

---

## 11. Testing

Agent tests must cover:
- Routing logic (all AoR/KNOT combinations)
- Access control (positive and negative cases)
- Guardrails (edge cases and violations)
- Error handling
- Multi-agent coordination
- Portal integration

---

## 12. Security

Agents must:
- Never bypass access control
- Always validate inputs
- Log security events
- Protect sensitive data
- Follow least privilege principle
- Support audit requirements

---

## 13. Performance

Agents should:
- Respond quickly (< 2s for routing decisions)
- Handle concurrent requests
- Scale with load
- Fail gracefully
- Provide progress feedback

---

## 14. Documentation

Each agent must document:
- Purpose and scope
- Capabilities and limitations
- Configuration options
- Integration requirements
- Usage examples
- Error handling
- Maintenance procedures

---
