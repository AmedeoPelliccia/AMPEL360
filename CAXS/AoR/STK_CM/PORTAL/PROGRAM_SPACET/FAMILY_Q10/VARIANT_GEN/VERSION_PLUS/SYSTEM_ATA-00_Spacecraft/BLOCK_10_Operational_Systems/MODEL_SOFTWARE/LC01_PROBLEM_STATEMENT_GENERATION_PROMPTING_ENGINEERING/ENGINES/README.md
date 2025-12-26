# ENGINES — Prompt Compilers, Orchestrators, Routers, and Policy Gates

**Parent Context:** LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING  
**Purpose:** Executable engines for prompt compilation, orchestration, routing, and policy enforcement  
**Status:** Active (Portal Baseline)

---

## 1. Purpose

This directory contains **executable engines** that:
- Compile prompt templates into executable prompts
- Orchestrate multi-step prompt workflows
- Route prompts to appropriate execution contexts
- Enforce policy gates and guardrails
- Manage prompt execution lifecycle

---

## 2. What Belongs Here

### Prompt Compilers
- Template → prompt compilation engines
- Macro expansion processors
- Variable substitution and parameterization
- YAML/JSON → executable prompt converters

### Orchestrators
- Multi-agent workflow coordinators
- Sequential and parallel prompt execution
- Context management and state tracking
- Error handling and retry logic

### Routers
- AoR-aware prompt routing
- Context-based prompt selection
- Tool access routing
- Entitlement-based routing

### Policy Gates
- Input validation and sanitization
- Output filtering and safety checks
- Constraint enforcement (AoR, KNOT, tool restrictions)
- Red team checks and restricted output filters
- Governance compliance validation

---

## 3. Engine Types

### Compilation Engines
- **Template Compiler:** Processes prompt templates with variable substitution
- **Macro Processor:** Expands macros and composition functions
- **Schema Validator:** Validates compiled prompts against schemas

### Orchestration Engines
- **Sequential Orchestrator:** Executes prompts in defined sequence
- **Parallel Orchestrator:** Manages concurrent prompt execution
- **Conditional Orchestrator:** Routes based on runtime conditions
- **Feedback Orchestrator:** Iterates prompts based on outputs

### Routing Engines
- **AoR Router:** Routes to AoR-specific execution contexts
- **Tool Router:** Selects and invokes appropriate tools
- **Context Router:** Adapts prompts to execution context

### Policy Engines
- **Access Gate:** Validates user entitlements and permissions
- **Constraint Gate:** Enforces KNOT and AoR constraints
- **Safety Gate:** Applies safety and security filters
- **Compliance Gate:** Ensures regulatory compliance

---

## 4. Engine Requirements

All engines must:
- Accept standard input format (see SCHEMAS/)
- Produce traceable outputs with metadata
- Log execution details for audit
- Handle errors gracefully
- Support dry-run/validation mode
- Integrate with CI/CD pipelines

---

## 5. Naming Conventions

Follow v6.0 nomenclature:
- `MODEL=SW`
- `PHASE=LC01`
- `CATEGORY=INTERNAL_PRODUCTION` for engine code
- `TYPE` as appropriate (script type or language extension)

**Example:**
```
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__prompt-compiler_INTERNAL_PRODUCTION_SPEC_I01-R01_ACTIVE.py
```

---

## 6. Configuration

Engines should be configurable via:
- Configuration files (YAML/JSON)
- Environment variables
- Command-line arguments
- Portal context (when available)

Configuration schemas should be stored in SCHEMAS/.

---

## 7. Integration Points

**Inputs:**
- PROMPTS/ for prompt definitions and templates
- SCHEMAS/ for validation schemas
- FIXTURES/ for test data
- Portal context (AoR, KNOT, user, entitlements)

**Outputs:**
- Compiled/executed prompts
- Execution logs and traces
- Error reports
- Evidence records for EVAL/

**Integration:**
- CI/ for automated testing
- AGENTS/ for agent wrapper integration
- EVAL/ for performance monitoring

---

## 8. Testing

All engines must have:
- Unit tests with fixtures from FIXTURES/
- Integration tests with EVAL/ harnesses
- Regression tests for critical paths
- Performance benchmarks
- Error handling tests

---

## 9. Documentation

Each engine must include:
- Purpose and scope
- Input/output specifications
- Configuration options
- Usage examples
- Error codes and handling
- Performance characteristics
- Maintenance and support contact

---

## 10. Security and Compliance

Engines must:
- Validate all inputs
- Sanitize outputs
- Enforce access controls
- Log security-relevant events
- Support audit requirements
- Follow secure coding practices

---
