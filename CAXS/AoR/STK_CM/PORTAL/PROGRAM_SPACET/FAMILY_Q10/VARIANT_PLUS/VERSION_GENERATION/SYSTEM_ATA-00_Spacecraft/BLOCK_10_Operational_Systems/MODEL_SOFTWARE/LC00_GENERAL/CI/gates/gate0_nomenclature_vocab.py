#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMPEL360 Gate 0 - Nomenclature Vocabulary Gate.

Evaluates collector output and determines if the PR should pass or fail
based on nomenclature validation results.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone


def main() -> int:
    """Main entry point for the gate."""
    ap = argparse.ArgumentParser(
        description="Gate 0: Evaluate nomenclature validation results."
    )
    ap.add_argument("--collector-json", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--warnings-blocking", default="false")
    args = ap.parse_args()

    warnings_blocking = str(args.warnings_blocking).strip().lower() in {"1", "true", "yes", "y"}

    if not os.path.exists(args.collector_json):
        print(f"ERROR: collector output not found: {args.collector_json}", file=sys.stderr)
        return 1

    with open(args.collector_json, encoding="utf-8") as f:
        data = json.load(f)

    errors = data.get("errors", [])
    warnings = data.get("warnings", [])

    status = "PASSED"
    exit_code = 0

    if errors:
        status = "FAILED"
        exit_code = 1
    elif warnings and warnings_blocking:
        status = "FAILED"
        exit_code = 1
    elif warnings:
        status = "WARNING"
        exit_code = 0

    # Gate is blocking if it fails (has errors or warnings with warnings_blocking=true)
    blocking = exit_code != 0

    run_id = (
        f"{os.environ.get('GITHUB_SHA', 'local')}_"
        f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}"
    )

    os.makedirs(args.out_dir, exist_ok=True)

    result = {
        "gate_id": "gate0_nomenclature_vocab",
        "run_id": run_id,
        "status": status,
        "blocking": blocking,
        "checks": [
            {
                "check_id": "nomenclature_v6_filename_and_scope",
                "status": "FAILED" if errors else ("WARNING" if warnings else "PASSED"),
                "details": data.get("summary", ""),
            }
        ],
        "summary": (
            f"Gate0 {status}: {len(errors)} errors, {len(warnings)} warnings "
            f"(warnings_blocking={warnings_blocking})."
        ),
        "recommendations": (
            ["Fix filename tokens and/or path-scope mismatches."] if (errors or warnings) else []
        ),
        "evidence": {
            "collector_outputs_consumed": ["collect_nomenclature_tokens"],
            "collector_json": args.collector_json,
            "artifacts_checked": data.get("inputs", {}).get("scanned_files_count", 0),
        },
    }

    with open(os.path.join(args.out_dir, "gate_result.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # Console summary
    print(result["summary"])
    max_items = 200
    if errors:
        print("\nErrors:")
        for e in errors[:max_items]:
            print(f"- {e['path']}: {e['code']} — {e['message']}")
        if len(errors) > max_items:
            remaining = len(errors) - max_items
            print(f"... and {remaining} more errors not shown.")
    if warnings:
        print("\nWarnings:")
        for w in warnings[:max_items]:
            print(f"- {w['path']}: {w['code']} — {w['message']}")
        if len(warnings) > max_items:
            remaining = len(warnings) - max_items
            print(f"... and {remaining} more warnings not shown.")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
