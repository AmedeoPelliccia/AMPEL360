# LC00_GENERAL

**Lifecycle Phase:** General / Cross-Phase

## Purpose

This directory contains cross-phase software artifacts, shared libraries, common utilities, and general-purpose tooling that are used across multiple lifecycle phases.

## Contents

Software artifacts in this directory include:
- Shared libraries and common modules
- General-purpose utilities and helper functions
- Cross-cutting concerns and infrastructure code
- Common configuration and constants
- Utility scripts used across multiple phases

## Naming Convention

All software artifacts follow the **v6.0 nomenclature standard** with:
- `MODEL=SW` token
- `PHASE=LC00` token
- `KNOT` binding as appropriate (K01..K14)
- Full compliance with controlled vocabulary (Section 10.2 of main README)

## Usage

Place software here when it:
- Is used by multiple lifecycle phases
- Provides general infrastructure or utilities
- Does not belong to a specific lifecycle phase
- Serves as a foundation for phase-specific tools

---

**References:**
- Main README Section 11: MODEL_SOFTWARE Directory Structure
- Nomenclature Standard: Section 10 of main README (v6.0)
