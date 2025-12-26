# FIXTURES — small deterministic test fixtures

**Directory:** `LC03_DESIGN_MODELS/FIXTURES/`

## Purpose
This directory contains **small, deterministic test fixtures** for validating design model processing tools, ensuring consistent behavior across model generators, validators, transformers, and exporters.

## Contents

### A) Sample Models
- Minimal valid model examples
- Edge case model specimens
- Invalid model samples for negative testing
- Model sets with known structures and relationships
- Representative subsystem models

### B) Interface Test Data
- Port and signal definition samples
- Interface connection test cases
- ICD scaffold examples
- Cross-ATA coupling scenarios
- Interface validation test data

### C) Transformation Test Data
- Model format conversion samples
- Model-to-document test cases
- Export format verification data
- Transformation round-trip fixtures

### D) Integration Test Data
- End-to-end workflow test sets
- Multi-tool pipeline fixtures
- Baseline comparison test data
- Traceability validation samples
- CI gate test scenarios

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC03`
- `KNOT` binding (typically K03 for design work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Provide test data for LC03 tools and utilities
- Enable deterministic testing and regression prevention
- Serve as examples for model structure and format
- Support automated test suites

**Do not place artifacts here when they:**
- Contain actual project design models (use parent directories)
- Are large-scale test datasets (consider dedicated test data repository)
- Are production models or baselines
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
- SysML/UML metamodel specifications
- Testing frameworks (pytest, unittest, etc.)
- Validation tools (VALIDATORS/, MBSE/)

## Ownership
**AoR (owners): STK_DAB, STK_TEST, STK_SE**

## References
- Main README: `MODEL_SOFTWARE/LC03_DESIGN_MODELS/README.md`
- Testing Standards and Best Practices
- Test-Driven Development Guidelines
