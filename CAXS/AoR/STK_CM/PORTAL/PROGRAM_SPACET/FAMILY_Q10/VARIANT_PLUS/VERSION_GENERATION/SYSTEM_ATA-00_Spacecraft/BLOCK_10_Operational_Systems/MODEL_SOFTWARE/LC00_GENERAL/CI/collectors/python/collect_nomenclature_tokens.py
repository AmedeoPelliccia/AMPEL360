#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMPEL360 v6.0 Nomenclature Token Collector.

Collects and validates nomenclature tokens from filenames according to v6.0 spec.
This collector is designed to be used in CI pipelines (GitHub Actions).
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

# Canonical v6.0 filename:
# [ATA]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__
# [SUBJECT]_[CATEGORY]_[TYPE]_[ISSUE-REV]_[STATUS].[EXT]

RE_ATA = re.compile(r"^\d{2}$")  # "00".."99"
RE_PHASE = re.compile(r"^LC\d{2}$")  # "LC00".."LC14" (range check below)
RE_KNOT = re.compile(r"^K\d{2}(-T\d{3})?$")  # "K01".."K14" optional "-T###"
RE_AOR = re.compile(r"^STK_[A-Z0-9]+$")  # conservative: STK_*
RE_SUBJECT = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")  # kebab-case
RE_BLOCK = re.compile(r"^\d{2}$")  # "00", "10", "20", etc.

RE_ISSUE_REV = re.compile(r"^I\d{2,3}-R\d{2,3}$")
RE_STATUS = re.compile(r"^(DRAFT|ACTIVE|RELEASED|SUPERSEDED|OBSOLETE)$")

# Vocabulary allowlists for core tokens
DEFAULT_PROJECT_ALLOW = {"AMPEL360"}
DEFAULT_PROGRAM_ALLOW = {"AIRT", "SPACET"}
DEFAULT_FAMILY_ALLOW = {"Q100", "Q200LR", "Q10", "QHABITAT"}
DEFAULT_VARIANT_ALLOW = {"GEN", "BASELINE", "FLIGHT_TEST", "CERT", "MSN", "CUST", "PLUS"}
DEFAULT_VERSION_ALLOW = {"PLUS", "PLUSULTRA", "GENERATION"}
DEFAULT_MODEL_ALLOW = {"BB", "HW", "SW", "PR"}

# Folder token extractors (path scope)
RE_PATH_TOKEN = {
    "PROGRAM": re.compile(r"/PROGRAM_([^/]+)/"),
    "FAMILY": re.compile(r"/FAMILY_([^/]+)/"),
    "VARIANT": re.compile(r"/VARIANT_([^/]+)/"),
    "VERSION": re.compile(r"/VERSION_([^/]+)/"),
    "SYSTEM": re.compile(r"/SYSTEM_([^/]+)/"),
    "BLOCK": re.compile(r"/BLOCK_([^/]+)/"),
}

RE_SYSTEM_ATA = re.compile(r"ATA-(\d{2})")  # e.g., SYSTEM_ATA-00_Spacecraft -> "00"
RE_BLOCK_NUM = re.compile(r"^(\d{2})\b")  # e.g., BLOCK_10_Operational... -> "10"

DEFAULT_EXT_ALLOW = {
    "md",
    "txt",
    "yml",
    "yaml",
    "json",
    "csv",
    "svg",
    "png",
    "jpg",
    "jpeg",
    "pdf",
    "docx",
    "xlsx",
    "pptx",
}

DEFAULT_TYPE_ALLOW = {
    "README",
    "STD",
    "POL",
    "PROC",
    "PLAN",
    "REQ",
    "SPEC",
    "ARCH",
    "ICD",
    "MOD",
    "MAN",
    "TST",
    "CASE",
    "LOG",
    "RPT",
    "NCR",
    "DEC",
    "MIN",
    "DIA",
    "TAB",
    "LST",
    "IDX",
    "REG",
    "CAT",
    "SCHEMA",
    "ONTO",
    "TRACE",
    "DPP",
    "SBOM",
    "BOM",
    "MAP",
    "MANIFEST",
    "EVD",
    "BADGE",
    "CERT",
    "LIC",
}

DEFAULT_CATEGORY_ALLOW = {
    "DELIVERABLE",
    "EVIDENCE",
    "REGISTRY",
    "SIGNOFF",
    "EXPORT_CONTROL",
    "INTERNAL_PRODUCTION",
}


@dataclass
class Finding:
    """Represents a validation finding."""

    level: str  # "error" | "warning"
    path: str
    code: str
    message: str


def gh_annot(level: str, path: str, message: str) -> None:
    """Emit a GitHub annotation."""
    lvl = "error" if level == "error" else "warning"
    # GitHub annotation command
    print(f"::{lvl} file={path}::{message}")


def read_lines(p: str) -> List[str]:
    """Read non-empty lines from a file."""
    with open(p, encoding="utf-8") as f:
        return [x.strip() for x in f.readlines() if x.strip()]


def is_ignored(
    rel_path: str,
    ignore_prefixes: List[str],
    ignore_basenames: List[str],
    ignore_exts: List[str],
) -> bool:
    """Check if a path should be ignored."""
    base = os.path.basename(rel_path)
    if base in ignore_basenames:
        return True
    for pref in ignore_prefixes:
        if rel_path.startswith(pref):
            return True
    # Check extension
    if "." in base:
        ext = base.rsplit(".", 1)[1].lower()
        if ext in ignore_exts:
            return True
    return False


def parse_filename(base: str) -> Tuple[Optional[Dict[str, str]], List[str]]:
    """Parse and validate a filename against v6.0 nomenclature rules.

    The canonical format is:
    [ATA]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__
    [SUBJECT]_[CATEGORY]_[TYPE]_[ISSUE-REV]_[STATUS].[EXT]

    Note: AoR contains an underscore (e.g., STK_CM, STK_DAB), so the left side
    will have 12 underscore-separated parts, with the last two forming the AoR.

    Returns:
        Tuple of (parsed_fields, errors) where parsed_fields is None if parsing failed.
    """
    errs: List[str] = []
    if "__" not in base:
        return None, ["Missing '__' separator before SUBJECT"]
    if base.count("__") != 1:
        return None, ["Filename must contain exactly one '__'"]

    left, right = base.split("__", 1)

    if "." not in right:
        return None, ["Missing extension"]
    right_noext, ext = right.rsplit(".", 1)

    left_parts = left.split("_")
    # AoR contains underscore (STK_*), so we expect 12 parts, with last 2 being AoR
    if len(left_parts) == 12:
        # Combine last two parts as AoR (e.g., STK + CM -> STK_CM)
        aor = f"{left_parts[10]}_{left_parts[11]}"
        left_parts = left_parts[:10] + [aor]
    elif len(left_parts) != 11:
        return None, [f"Left side must have 11 or 12 fields (AoR contains _), got {len(left_parts)}"]

    ata, project, program, family, variant, version, model, block, phase, knot, aor = left_parts

    right_parts = right_noext.split("_")
    if len(right_parts) != 5:
        return None, [f"Right side must have 5 fields, got {len(right_parts)}"]
    subject, category, typ, issue_rev, status = right_parts

    # Basic structural checks
    if not RE_ATA.match(ata):
        errs.append(f"ATA invalid: '{ata}' (expected 2 digits)")
    if project not in DEFAULT_PROJECT_ALLOW:
        errs.append(f"PROJECT invalid: '{project}' (allowed: {sorted(DEFAULT_PROJECT_ALLOW)})")
    if program not in DEFAULT_PROGRAM_ALLOW:
        errs.append(f"PROGRAM invalid: '{program}' (allowed: {sorted(DEFAULT_PROGRAM_ALLOW)})")
    if family not in DEFAULT_FAMILY_ALLOW:
        errs.append(f"FAMILY invalid: '{family}' (allowed: {sorted(DEFAULT_FAMILY_ALLOW)})")
    if variant not in DEFAULT_VARIANT_ALLOW:
        errs.append(f"VARIANT invalid: '{variant}' (allowed: {sorted(DEFAULT_VARIANT_ALLOW)})")
    if version not in DEFAULT_VERSION_ALLOW:
        errs.append(f"VERSION invalid: '{version}' (allowed: {sorted(DEFAULT_VERSION_ALLOW)})")
    if model not in DEFAULT_MODEL_ALLOW:
        errs.append(f"MODEL invalid: '{model}' (allowed: {sorted(DEFAULT_MODEL_ALLOW)})")
    if not RE_BLOCK.match(block):
        errs.append(f"BLOCK invalid: '{block}' (expected 2 digits)")
    if not RE_PHASE.match(phase):
        errs.append(f"PHASE invalid: '{phase}' (expected LC##)")
    else:
        # enforce LC00..LC14
        try:
            n = int(phase[2:])
            if n < 0 or n > 14:
                errs.append(f"PHASE out of range: '{phase}' (expected LC00..LC14)")
        except Exception:
            errs.append(f"PHASE invalid: '{phase}'")

    if not RE_KNOT.match(knot):
        errs.append(f"KNOT invalid: '{knot}' (expected K## or K##-T###)")
    else:
        # enforce K01..K14
        try:
            k = int(knot[1:3])
            if k < 1 or k > 14:
                errs.append(f"KNOT out of range: '{knot}' (expected K01..K14)")
        except Exception:
            errs.append(f"KNOT invalid: '{knot}'")

    if not RE_AOR.match(aor):
        errs.append(f"AoR invalid: '{aor}' (expected STK_*)")
    if not RE_SUBJECT.match(subject):
        errs.append(f"SUBJECT invalid: '{subject}' (expected kebab-case)")
    if category not in DEFAULT_CATEGORY_ALLOW:
        errs.append(f"CATEGORY invalid: '{category}'")
    if typ not in DEFAULT_TYPE_ALLOW:
        errs.append(f"TYPE not allowed: '{typ}'")
    if not RE_ISSUE_REV.match(issue_rev):
        errs.append(f"ISSUE-REV invalid: '{issue_rev}' (expected I##-R##)")
    if not RE_STATUS.match(status):
        errs.append(f"STATUS invalid: '{status}'")
    if ext.lower() not in DEFAULT_EXT_ALLOW:
        errs.append(f"EXT not allowed: '{ext}'")

    if errs:
        return None, errs

    return {
        "ATA": ata,
        "PROJECT": project,
        "PROGRAM": program,
        "FAMILY": family,
        "VARIANT": variant,
        "VERSION": version,
        "MODEL": model,
        "BLOCK": block,
        "PHASE": phase,
        "KNOT": knot,
        "AoR": aor,
        "SUBJECT": subject,
        "CATEGORY": category,
        "TYPE": typ,
        "ISSUE-REV": issue_rev,
        "STATUS": status,
        "EXT": ext.lower(),
    }, []


def expected_from_path(rel_path: str) -> Dict[str, str]:
    """Extract expected token values from the path structure."""
    p = rel_path.replace("\\", "/")
    exp: Dict[str, str] = {}

    for key, rx in RE_PATH_TOKEN.items():
        m = rx.search(f"/{p}/")
        if m:
            exp[key] = m.group(1)

    # SYSTEM -> ATA (if present)
    sys_token = exp.get("SYSTEM")
    if sys_token:
        m = RE_SYSTEM_ATA.search(sys_token)
        if m:
            exp["ATA"] = m.group(1)

    # BLOCK folder -> numeric block code
    block_token = exp.get("BLOCK")
    if block_token:
        m = RE_BLOCK_NUM.match(block_token)
        if m:
            exp["BLOCK"] = m.group(1)

    return exp


def main() -> int:
    """Main entry point for the collector."""
    ap = argparse.ArgumentParser(
        description="Collect and validate nomenclature tokens from changed files."
    )
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--changed-files", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--annotations", choices=["none", "github"], default="github")
    ap.add_argument("--check-path-scope", default="true")  # true/false
    ap.add_argument("--ignore-prefix", action="append", default=[])
    ap.add_argument("--ignore-basename", action="append", default=[])
    ap.add_argument("--ignore-ext", action="append", default=[])
    args = ap.parse_args()

    check_scope = str(args.check_path_scope).strip().lower() in {"1", "true", "yes", "y"}
    # Normalize extensions (remove leading dot if present)
    ignore_exts = [ext.lstrip(".").lower() for ext in args.ignore_ext]

    repo_root = os.path.abspath(args.repo_root)
    changed_list = os.path.abspath(args.changed_files)

    if not os.path.exists(changed_list):
        print(f"ERROR: changed files list not found: {changed_list}", file=sys.stderr)
        return 1

    rel_paths = read_lines(changed_list)

    findings: List[Finding] = []
    scanned = 0

    for rel in rel_paths:
        rel = rel.replace("\\", "/")
        if is_ignored(rel, args.ignore_prefix, args.ignore_basename, ignore_exts):
            continue

        abs_path = os.path.join(repo_root, rel)
        if not os.path.exists(abs_path):
            # deleted/renamed edge cases
            continue

        base = os.path.basename(rel)
        if base.startswith("."):
            continue  # skip dotfiles by default

        parsed, errs = parse_filename(base)
        scanned += 1

        if errs:
            for e in errs:
                findings.append(Finding("error", rel, "FILENAME", e))
            continue

        if check_scope:
            exp = expected_from_path(rel)
            # compare only if we can derive expectations
            for key in ("PROGRAM", "FAMILY", "VARIANT", "VERSION", "ATA", "BLOCK"):
                if key in exp:
                    got = parsed.get(key, "")
                    want = exp[key]
                    if got != want:
                        findings.append(
                            Finding(
                                "error",
                                rel,
                                "SCOPE_MISMATCH",
                                f"{key} mismatch: path expects '{want}' but filename has '{got}'",
                            )
                        )

    # Output artifacts
    os.makedirs(args.out_dir, exist_ok=True)
    run_id = (
        f"{os.environ.get('GITHUB_SHA', 'local')}_"
        f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}"
    )

    errors = [f for f in findings if f.level == "error"]
    warnings = [f for f in findings if f.level == "warning"]

    out = {
        "collector_id": "collect_nomenclature_tokens",
        "run_id": run_id,
        "inputs": {
            "changed_files_count": len(rel_paths),
            "scanned_files_count": scanned,
            "check_path_scope": check_scope,
            "ignore_prefixes": args.ignore_prefix,
            "ignore_basenames": args.ignore_basename,
            "ignore_exts": ignore_exts,
        },
        "counts": {
            "errors": len(errors),
            "warnings": len(warnings),
        },
        "errors": [{"path": f.path, "code": f.code, "message": f.message} for f in errors],
        "warnings": [{"path": f.path, "code": f.code, "message": f.message} for f in warnings],
        "summary": (
            f"Scanned {scanned} changed files: {len(errors)} errors, {len(warnings)} warnings."
        ),
    }

    with open(os.path.join(args.out_dir, "collector_output.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    with open(os.path.join(args.out_dir, "summary.md"), "w", encoding="utf-8") as f:
        f.write(f"## collect_nomenclature_tokens\n\n{out['summary']}\n")
        if errors:
            f.write("\n### Errors\n")
            for e in errors:
                f.write(f"- `{e.path}` — {e.code}: {e.message}\n")

    # Emit annotations
    if args.annotations == "github":
        for fnd in findings:
            gh_annot(fnd.level, fnd.path, f"{fnd.code}: {fnd.message}")

    # NOTE: Collector should not "decide" policy, but it can still return 0 and let the gate fail.
    # We return 0 always unless there is an internal execution issue.
    return 0


if __name__ == "__main__":
    sys.exit(main())
