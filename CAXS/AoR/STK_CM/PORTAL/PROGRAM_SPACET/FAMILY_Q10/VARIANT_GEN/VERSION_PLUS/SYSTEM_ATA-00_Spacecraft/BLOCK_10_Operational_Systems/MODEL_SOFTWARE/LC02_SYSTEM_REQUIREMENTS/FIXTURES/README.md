# FIXTURES — Small Deterministic Test Fixtures

**Directory:** `LC02_SYSTEM_REQUIREMENTS/FIXTURES/`

## Purpose
This directory contains **small, deterministic test fixtures** for validating requirement processing tools, ensuring consistent behavior across parsers, validators, trace builders, and exporters.

## Contents

### A) Sample Requirements
- Minimal valid requirement examples
- Edge case requirement specimens
- Invalid requirement samples for negative testing
- Requirement sets with known relationships

### B) Schema Test Data
- Valid schema instances
- Invalid schema instances for error testing
- Schema migration test cases
- Controlled vocabulary samples

### C) Traceability Test Data
- Simple trace graph fixtures
- Complex dependency networks
- Circular reference test cases
- Broken link scenarios

### D) Integration Test Data
- End-to-end workflow test sets
- Multi-tool pipeline fixtures
- Baseline comparison test data
- Export format verification samples

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC02`
- `KNOT` binding (typically K02 for requirements work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Provide test data for LC02 tools and utilities
- Enable deterministic testing and regression prevention
- Serve as examples for requirement format and structure
- Support automated test suites

**Do not place artifacts here when they:**
- Contain actual project requirements (use parent directories)
- Are large-scale test datasets (consider dedicated test data repository)
- Are production data or baselines
- Are executable test scripts (use test frameworks in respective tool directories)

## Fixture Design Principles

### Minimal and Focused
Each fixture should test one specific aspect or scenario, keeping complexity minimal and purpose clear.

### Deterministic
Fixtures must produce consistent, reproducible results across different environments and test runs.

### Self-Contained
Fixtures should include all necessary data and not depend on external resources or state.

### Well-Documented
Each fixture should have clear documentation explaining its purpose, expected behavior, and usage.

## Dependencies
- SCHEMAS/ for fixture structure
- Testing frameworks (pytest, unittest, etc.)
- Validation tools (VALIDATORS/, ENGINES/)

## Ownership
**AoR (owners): STK_DAB, STK_TEST, STK_SE**

## References
- Main README: `MODEL_SOFTWARE/LC02_SYSTEM_REQUIREMENTS/README.md`
- Testing Standards and Best Practices
- Test-Driven Development Guidelines
