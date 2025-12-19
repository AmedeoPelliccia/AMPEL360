---
document_id: "00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-knot-graph-model_DELIVERABLE_SPEC_I01-R01_ACTIVE"
title: "CIPP and KNOT Graph Model — Two-Layer Architecture"
project: "AMPEL360"
scope: "Interaction model between Certainty Layer and Uncertainty Layer"
owner_aor: "STK_CM"
interfaces:
  required: ["STK_SE","STK_DAB","STK_PMO"]
category: "DELIVERABLE"
type: "SPEC"
status: "ACTIVE"
issue_rev: "I01-R01"
---

# CIPP and KNOT Graph Model — Two-Layer Architecture

## 1. Purpose

This document defines the **two-layer graph model** that maintains separation between:
1. **CIPP Graph (Certainty Layer)**: Deterministic integration routes
2. **KNOT Graph (Uncertainty Layer)**: Uncertainty resolution processes

These two graphs **interact but do not blur**, ensuring clear separation between "what we know" (certainty) and "what we're discovering" (uncertainty).

---

## 2. Core Architecture

### 2.1 Two-Layer Graph Model (Normative)

```
┌─────────────────────────────────────────────────────────────┐
│                   CIPP Graph (Certainty Layer)              │
│                                                             │
│  Nodes:  CIPPs (certainty objects)                         │
│  Edges:  Deterministic dependencies                        │
│          (requires, implements, exports, consumes)         │
│  Constraint: All targets must be RELEASED                  │
│             (or explicitly allowed by policy)              │
│                                                             │
│  ┌─────────┐    requires    ┌─────────┐    exports        │
│  │ CIPP-   │───────────────►│ CIPP-   │───────────┐       │
│  │  001    │                │  002    │           │       │
│  └─────────┘                └─────────┘           ▼       │
│       │                          ▲           ┌─────────┐  │
│       │ implements               │ consumes  │ CIPP-   │  │
│       │                          │           │  003    │  │
│       ▼                     ┌─────────┐      └─────────┘  │
│  ┌─────────┐    requires    │ CIPP-   │                   │
│  │ CIPP-   │───────────────►│  005    │                   │
│  │  004    │                └─────────┘                   │
│  └─────────┘                                               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                 Promotion │ (KNOT collapse → CIPP mint)
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                  KNOT Graph (Uncertainty Layer)             │
│                                                             │
│  Nodes:  KNOT states (uncertainty nodes)                   │
│  Edges:  Entanglement and coupling                         │
│          (hard, soft, conditional)                         │
│  Output: Resolution → mints/updates CIPPs                  │
│                                                             │
│  ┌─────────┐    hard        ┌─────────┐    soft           │
│  │ KNOT    │───coupling────►│ KNOT    │───coupling──┐     │
│  │  K09    │                │  K03    │             │     │
│  └─────────┘                └─────────┘             ▼     │
│       │                          ▲             ┌─────────┐ │
│       │ entangled                │ depends_on  │ KNOT    │ │
│       │                          │             │  K01    │ │
│       ▼                     ┌─────────┐        └─────────┘ │
│  ┌─────────┐    conditional │ KNOT    │                    │
│  │ KNOT    │───coupling────►│  K08    │                    │
│  │  K10    │                └─────────┘                    │
│  └─────────┘                                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. CIPP Graph (Certainty Layer)

### 3.1 Node Definition

A **CIPP node** represents a deterministic integration object:

```yaml
node:
  id: CIPP-###
  kind: POINTER | PATH | ROUTE | BINDING | EXPORT | DEPLOY
  intent_key: {vision_id, mission_id, scope_id, pathway_ids, outcome_ids}
  intent_hash: sha256:...
  target_refs: [{path, sha256, status}]
  status: DRAFT | ACTIVE | RELEASED | OBSOLETE
```

### 3.2 Edge Types (Deterministic Dependencies)

| Edge Type | Meaning | Validation |
|-----------|---------|------------|
| `requires` | CIPP A requires CIPP B to execute | B must exist and be valid before A can execute |
| `implements` | CIPP A implements interface/contract from CIPP B | A must satisfy B's interface contract |
| `exports` | CIPP A exports data/artifacts to CIPP B | A's outputs must match B's input schema |
| `consumes` | CIPP A consumes outputs from CIPP B | B must execute successfully before A |
| `extends` | CIPP A extends/builds upon CIPP B | A inherits B's constraints and adds new ones |
| `supersedes` | CIPP A replaces CIPP B | A must provide all functionality of B |

### 3.3 Graph Constraints (Normative)

1. **No cycles**: CIPP graph must be a directed acyclic graph (DAG)
2. **All targets RELEASED**: Target artifacts in `target_refs` must be RELEASED (or policy-approved)
3. **Hash integrity**: All `sha256` values must match actual file hashes
4. **Intent alignment**: All nodes must have valid `intent_key` resolving to SSOT registries
5. **Dependency resolution**: All edge targets must exist and be valid

### 3.4 Graph Operations

**Query operations**:
- `find_cipp_by_intent(intent_key)`: Find CIPPs matching intent
- `find_cipp_by_pgk_scope(pgk_scope)`: Find CIPPs for specific program slice
- `get_dependencies(cipp_id)`: Get all CIPPs that this CIPP depends on
- `get_dependents(cipp_id)`: Get all CIPPs that depend on this CIPP
- `validate_execution_path(cipp_id)`: Validate all dependencies are satisfied

**Mutation operations**:
- `add_cipp(cipp_def)`: Add new CIPP node (triggered by KNOT collapse)
- `update_cipp(cipp_id, updates)`: Update existing CIPP (requires version increment)
- `deprecate_cipp(cipp_id)`: Move CIPP to OBSOLETE (must check dependents)

---

## 4. KNOT Graph (Uncertainty Layer)

### 4.1 Node Definition

A **KNOT node** represents an uncertainty resolution process:

```yaml
node:
  id: K## (K01-K14)
  problem_statement: "..."
  intent_key: {vision_id, mission_id, scope_id, pathway_ids, outcome_ids}
  intent_hash: sha256:...
  hypotheses: [{id, statement, outcome_ids}]
  closure_criteria: [{id, test, target}]
  task_registry_ref: path/to/tasks
  status: OPEN | ACTIVE | CLOSED | OBSOLETE
```

### 4.2 Edge Types (Uncertainty Coupling)

| Edge Type | Meaning | Resolution Strategy |
|-----------|---------|---------------------|
| `hard_coupling` | KNOT A cannot close without KNOT B | B must close first; sequential resolution |
| `soft_coupling` | KNOT A benefits from KNOT B but not blocked | Parallel resolution; share results |
| `conditional_coupling` | KNOT A depends on KNOT B if condition met | Evaluate condition; resolve dependency if true |
| `entangled` | KNOT A and B share variables/constraints | Joint resolution; coordinate decisions |
| `depends_on` | KNOT A uses outputs from KNOT B | B should close first for optimal path |

### 4.3 Graph Constraints (Normative)

1. **Cycles allowed**: KNOT graph may have cycles (representing iterative refinement)
2. **Intent alignment**: All nodes must have valid `intent_key` resolving to SSOT registries
3. **Closure criteria testable**: All `closure_criteria` must be measurable
4. **Task mapping**: All nodes must have `task_registry_ref` with defined tasks
5. **Outcome linkage**: All `outcome_ids` must exist in Scope & Outcome Registry

### 4.4 Graph Operations

**Query operations**:
- `find_open_knots()`: Get all KNOTs with status=OPEN or ACTIVE
- `get_coupled_knots(knot_id)`: Get all KNOTs coupled to this KNOT
- `get_closure_blockers(knot_id)`: Identify hard-coupled KNOTs that must close first
- `find_knots_by_ata(ata_range)`: Find KNOTs impacting specific ATA range

**Mutation operations**:
- `open_knot(knot_def)`: Create new KNOT node (instantiate ONUP)
- `activate_knot(knot_id)`: Move KNOT to ACTIVE status (work in progress)
- `close_knot(knot_id, cipp_ids)`: Close KNOT and mint CIPPs (promotion)
- `reopen_knot(knot_id, reason)`: Reopen closed KNOT (e.g., new evidence, changed requirements)

---

## 5. Interaction Between Layers

### 5.1 Promotion Rule (KNOT → CIPP)

**Normative rule**: A KNOT is "collapsed" (closed) only when it yields:

1. A **released artifact chain**: All task outputs moved to ACTIVE or RELEASED status
2. **At least one CIPP**: New CIPP node(s) created in CIPP Graph pointing to released artifacts

**Promotion process**:

```
┌──────────────────────────────────────────────────────────────┐
│ KNOT K09: "DPP Circularity KPI Claim Defensible?"           │
│                                                              │
│ Tasks produce:                                               │
│  - KPI calculation method validated                          │
│  - Test results → EVIDENCE                                   │
│  - STK_CEGT + STK_CERT approval → SIGNOFF                    │
│  - KPI registry → REGISTRY (status=ACTIVE)                   │
│  - ESG reporting index → REGISTRY (status=ACTIVE)            │
└───────────────────────┬──────────────────────────────────────┘
                        │
                        │ Collapse + Mint CIPP
                        ▼
┌──────────────────────────────────────────────────────────────┐
│ CIPP-001: "DPP Circularity KPI Export Route"                │
│                                                              │
│ Target refs:                                                 │
│  - circularity-kpis_REGISTRY (sha256:d4e5f6...)             │
│  - esg-reporting_REGISTRY (sha256:e5f6g7...)                │
│  - dpp-manifest-schema_DELIVERABLE (sha256:f6g7h8...)       │
│  - circularity-validation_EVIDENCE (sha256:g7h8i9...)       │
│                                                              │
│ Result: Anyone needing this outcome uses CIPP-001 route,    │
│         not a new KNOT                                       │
└──────────────────────────────────────────────────────────────┘
```

### 5.2 Query Rule (CIPP → Skip KNOT)

**Normative rule**: Before instantiating KNOT, check CIPP Graph for existing route.

**Query process** (Step 1.5 in Main Workflow):

```python
def should_instantiate_knot(pgk_scope, ata, interface_contract, intent_key):
    # Search CIPP Graph
    matching_cipps = find_cipps(
        pgk_scope=pgk_scope,
        ata=ata,
        interface_contract=interface_contract,
        intent_key=intent_key
    )
    
    # Filter for valid CIPPs
    valid_cipps = [
        cipp for cipp in matching_cipps
        if all([
            cipp.status in ['ACTIVE', 'RELEASED'],
            all_targets_valid(cipp.target_refs),
            all_hashes_match(cipp.target_refs),
            intent_validates(cipp.intent_key)
        ])
    ]
    
    if valid_cipps:
        # Execute via CIPP (deterministic)
        return False, valid_cipps[0]
    else:
        # Instantiate KNOT (uncertainty resolution)
        return True, None
```

### 5.3 Feedback Loop (CIPP → KNOT)

**When to reopen KNOT from CIPP**:

1. **Target invalidation**: CIPP target artifact superseded or hash mismatch
2. **Intent drift**: CIPP no longer aligns with updated vision/mission/outcomes
3. **Execution failure**: CIPP execution repeatedly fails validation checks
4. **New requirements**: Scope expansion requires CIPP extension beyond current capability

**Feedback process**:

```
┌──────────────────────────────────────────────────────────────┐
│ CIPP-002 execution fails:                                    │
│  - Target artifact superseded                                │
│  - New interface contract version incompatible               │
└───────────────────────┬──────────────────────────────────────┘
                        │
                        │ Trigger reopen
                        ▼
┌──────────────────────────────────────────────────────────────┐
│ KNOT K03: "Interface Compatibility Resolution"              │
│                                                              │
│ New tasks:                                                   │
│  - Analyze breaking changes in new ICD version               │
│  - Update component interface adapters                       │
│  - Generate migration evidence                               │
│  - Obtain STK_SE approval                                    │
└───────────────────────┬──────────────────────────────────────┘
                        │
                        │ Collapse + Update CIPP
                        ▼
┌──────────────────────────────────────────────────────────────┐
│ CIPP-002 (updated):                                          │
│  - New target refs with updated hashes                       │
│  - Version constraint: >=I02-R01                             │
│  - Additional validation step for backward compatibility     │
└──────────────────────────────────────────────────────────────┘
```

---

## 6. Graph Traversal Algorithms

### 6.1 CIPP Execution Path Resolution

**Algorithm**: Find optimal execution path through CIPP Graph

```python
def resolve_execution_path(cipp_id):
    """
    Resolve all dependencies and return execution order.
    Returns: list of CIPP IDs in execution order
    """
    visited = set()
    execution_order = []
    
    def dfs(cid):
        if cid in visited:
            return
        visited.add(cid)
        
        # Get dependencies
        dependencies = get_cipp_dependencies(cid)
        for dep in dependencies:
            dfs(dep.cipp_id)
        
        # Add to execution order after dependencies
        execution_order.append(cid)
    
    dfs(cipp_id)
    return execution_order
```

### 6.2 KNOT Closure Blocker Analysis

**Algorithm**: Identify which KNOTs must close before target KNOT

```python
def get_closure_blockers(knot_id):
    """
    Find all hard-coupled KNOTs that block closure.
    Returns: list of KNOT IDs that must close first
    """
    blockers = []
    
    # Get hard-coupled edges
    hard_couplings = get_knot_edges(knot_id, edge_type='hard_coupling')
    
    for edge in hard_couplings:
        target_knot = get_knot(edge.target_id)
        if target_knot.status not in ['CLOSED', 'OBSOLETE']:
            blockers.append(target_knot.id)
            # Recursive: blockers of blockers
            blockers.extend(get_closure_blockers(target_knot.id))
    
    return list(set(blockers))  # Remove duplicates
```

### 6.3 Intent-Aligned Path Discovery

**Algorithm**: Find CIPPs or KNOTs matching intent key

```python
def find_intent_aligned_paths(intent_key):
    """
    Find all CIPPs and KNOTs matching intent key.
    Returns: {cipps: [...], knots: [...]}
    """
    results = {
        'cipps': [],
        'knots': []
    }
    
    # Search CIPP Graph
    for cipp in get_all_cipps():
        if intent_matches(cipp.intent_key, intent_key):
            results['cipps'].append(cipp)
    
    # Search KNOT Graph
    for knot in get_all_knots():
        if intent_matches(knot.intent_key, intent_key):
            results['knots'].append(knot)
    
    return results
```

---

## 7. Visualization Examples

### 7.1 Simple CIPP Chain

```
CIPP-001 (POINTER)          CIPP-002 (POINTER)
   │                            │
   │ points to                  │ points to
   │ KPI Registry               │ Schema Registry
   │                            │
   └────────────┬───────────────┘
                │
                │ both consumed by
                ▼
        CIPP-003 (ROUTE)
         DPP Export Route
```

### 7.2 KNOT to CIPP Promotion

```
Before Collapse:

KNOT K09 (ACTIVE)
 ├─ Task T01: Validate KPI method
 ├─ Task T02: Generate test evidence
 ├─ Task T03: Obtain CEGT approval
 └─ Task T04: Obtain CERT approval

After Collapse:

KNOT K09 (CLOSED) ──promotes──> CIPP-001 (ACTIVE)
                                  │
                                  ├─ Target: KPI Registry
                                  ├─ Target: ESG Index
                                  ├─ Target: DPP Schema
                                  └─ Evidence: Validation Log
```

### 7.3 KNOT Coupling Network

```
    K01 (Design)
     │
     │ soft_coupling
     ▼
    K03 (Integration) ◄─── hard_coupling ─── K09 (Validation)
     │                                          │
     │ depends_on                               │ entangled
     ▼                                          ▼
    K08 (Certification) ◄─── conditional ───  K10 (Release)
```

---

## 8. Metrics and Health Indicators

### 8.1 CIPP Graph Health

| Metric | Description | Target |
|--------|-------------|--------|
| CIPP validity rate | % of CIPPs with all targets valid | 100% |
| CIPP execution success rate | % of CIPP executions that succeed | > 95% |
| Broken reference count | Number of CIPPs with missing targets | 0 |
| Stale CIPP count | CIPPs not validated in >365 days | < 5% |
| Average dependency depth | Mean depth of CIPP dependency chains | < 5 |

### 8.2 KNOT Graph Health

| Metric | Description | Target |
|--------|-------------|--------|
| Open KNOT count | Number of KNOTs with status=OPEN or ACTIVE | Trending down |
| KNOT closure rate | KNOTs closed per month | Trending up |
| CIPP mint rate | CIPPs minted per KNOT closed | > 0.8 |
| Blocker resolution time | Mean time to resolve hard-coupled blockers | < 30 days |
| KNOT reopen rate | % of closed KNOTs reopened | < 10% |

### 8.3 Layer Interaction Health

| Metric | Description | Target |
|--------|-------------|--------|
| CIPP hit rate | % of queries finding valid CIPP (Step 1.5) | Trending up |
| KNOT instantiation rate | New KNOTs per month | Trending down |
| Promotion success rate | % of KNOT closures that mint CIPP | > 80% |
| Intent alignment rate | % of nodes with valid intent_key | 100% |

---

## 9. Governance Rules

### 9.1 Graph Integrity

1. **No orphans**: All CIPP and KNOT nodes must be reachable from root intent
2. **No broken edges**: All edge targets must exist and be valid
3. **Intent consistency**: All nodes must maintain valid intent_key references
4. **Version coherence**: Dependent nodes must satisfy version constraints

### 9.2 Evolution Policy

1. **CIPP updates**: Require version increment + impact analysis on dependents
2. **KNOT reopening**: Requires justification + new closure criteria
3. **Graph pruning**: OBSOLETE nodes archived after 365 days with no dependents
4. **Performance optimization**: Graph queries cached with 24hr TTL

---

## 10. References

- **CIPP vs KNOT Governance**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-vs-knot-governance_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **CIPP Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-registry_REGISTRY_CAT_I01-R01_ACTIVE.md`
- **CIPP Definition Schema**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-definition-schema_DELIVERABLE_SCHEMA_I01-R01_ACTIVE.md`
- **Intent Alignment Policy**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-intent-alignment-policy_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **Main Workflow SSOT**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-main-workflow-ssot_DELIVERABLE_PROC_I01-R01_ACTIVE.md`

---

**Change History**

| Issue-Rev | Date | Author | Description |
|-----------|------|--------|-------------|
| I01-R01 | 2025-12-19 | STK_CM | Initial two-layer graph model specification |
