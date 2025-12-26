# EVAL — Evaluation Suites, Scoring Tools, Regression Tests, and Benchmark Harnesses

**Parent Context:** LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING  
**Purpose:** Evaluation and testing infrastructure for prompts and engines  
**Status:** Active (Portal Baseline)

---

## 1. Purpose

This directory contains **evaluation and testing infrastructure** for:
- Prompt quality assessment and scoring
- Regression testing for prompt changes
- Benchmark harness for performance evaluation
- Drift detection and monitoring
- Golden set management and validation

---

## 2. What Belongs Here

### Evaluation Suites
- Prompt quality evaluation frameworks
- Rubric-based scoring systems
- Multi-dimensional assessment tools
- Comparative evaluation harnesses

### Scoring Tools
- Automated scoring engines
- Quality metrics calculators
- Performance measurement tools
- Drift detection algorithms

### Regression Tests
- Baseline output comparison
- Deterministic test suites
- Change impact analysis
- Version compatibility tests

### Benchmark Harnesses
- Performance benchmarking frameworks
- Load and stress testing tools
- Scalability assessment harnesses
- Comparative benchmarking utilities

---

## 3. Evaluation Categories

### Quality Metrics
- **Accuracy:** Output correctness and precision
- **Completeness:** Coverage of required elements
- **Consistency:** Alignment with standards and patterns
- **Clarity:** Readability and comprehensibility
- **Traceability:** Linkage to requirements and evidence

### Performance Metrics
- **Execution Time:** Prompt compilation and execution duration
- **Resource Usage:** Memory, CPU, token consumption
- **Throughput:** Prompts processed per unit time
- **Latency:** Response time characteristics

### Reliability Metrics
- **Determinism:** Output consistency across runs
- **Error Rate:** Frequency of failures or exceptions
- **Recovery:** Ability to handle and recover from errors
- **Robustness:** Performance under stress or edge cases

---

## 4. Evaluation Workflows

### Continuous Evaluation
1. Run regression suite on every prompt change
2. Compare against baseline/golden outputs
3. Calculate quality and performance metrics
4. Generate evaluation report
5. Block PR if critical metrics fail

### Periodic Benchmarking
1. Run comprehensive benchmark suite
2. Compare against historical baselines
3. Identify performance trends and drift
4. Update benchmark baselines as needed

### Ad-Hoc Evaluation
1. Interactive evaluation for development
2. Exploratory testing of new prompts
3. Comparative analysis of prompt variants
4. Root cause analysis for failures

---

## 5. Golden Set Management

Maintain golden sets for:
- **Golden Inputs:** Representative problem statements and contexts
- **Golden Outputs:** Expected/ideal prompt outputs
- **Golden Patterns:** Reference patterns for common scenarios
- **Golden Metrics:** Target quality and performance metrics

Golden sets must be:
- Version controlled
- Reviewed and approved by AoR owners
- Updated via formal change process
- Documented with rationale

---

## 6. Regression Testing

Regression suites must:
- Cover critical prompt paths
- Test all major KNOT/AoR combinations
- Validate policy gate enforcement
- Check integration points
- Run in CI pipeline
- Complete within reasonable time

---

## 7. Naming Conventions

Follow v6.0 nomenclature:
- `MODEL=SW`
- `PHASE=LC01`
- `CATEGORY=EVIDENCE` for test results
- `CATEGORY=INTERNAL_PRODUCTION` for test code
- `TYPE` as appropriate (TST, LOG, RPT for results)

**Example:**
```
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__eval-regression-suite_INTERNAL_PRODUCTION_TST_I01-R01_ACTIVE.py
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__eval-results-summary_EVIDENCE_RPT_I01-R01_ACTIVE.json
```

---

## 8. Integration Points

**Inputs:**
- PROMPTS/ for prompt definitions
- ENGINES/ for compilation/execution
- FIXTURES/ for test data
- SCHEMAS/ for validation

**Outputs:**
- Test results and reports
- Quality metrics and scores
- Drift detection alerts
- Benchmark data
- Evidence records for traceability

**Integration:**
- CI/ for automated testing
- Portal dashboards for visualization
- Traceability graph for evidence linkage

---

## 9. Reporting

Evaluation reports must include:
- Test/evaluation ID and timestamp
- Prompt/engine version tested
- Test suite and configuration
- Metrics and scores
- Pass/fail status
- Detailed findings
- Recommendations

---

## 10. Thresholds and Gates

Define thresholds for:
- Minimum quality scores (per metric)
- Maximum regression tolerance
- Performance requirements
- Error rate limits

Configure gates to:
- Block PRs on critical failures
- Warn on threshold violations
- Require manual review on significant changes
- Trigger additional testing on drift detection

---

## 11. Maintenance

Regularly:
- Review and update evaluation criteria
- Refresh golden sets
- Tune scoring algorithms
- Update performance baselines
- Add tests for new prompt patterns
- Remove obsolete tests

---
