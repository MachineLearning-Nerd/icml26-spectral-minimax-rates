"""Run the corrected, CPU-only v4 claim suite.

This entry point intentionally keeps the baseline run command unchanged while
replacing proxy checks with real model dynamics and honest evidence labels.
"""
from __future__ import annotations

import json
import os
import platform
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from experiments import run_all


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "v4"
LEDGER = ROOT / "claims" / "claims_v4.json"


def main() -> int:
    ledger = json.loads(LEDGER.read_text())
    print("=" * 80)
    print("ALIGNMENT-SENSITIVE MINIMAX RATES — CORRECTED V4 CLAIM SUITE")
    print("=" * 80)
    print(f"paper={ledger['paper']['arxiv_id']}")
    print(f"paper_sha256={ledger['paper']['sha256']}")
    print(f"python={platform.python_version()} numpy={np.__version__}")
    print("backend=CPU clean_room=true")
    print(f"claim_ledger_items={len(ledger['claims'])}")
    print("evidence_policy=proof claims are not reported as empirically proved")

    results = run_all(OUT)
    passed = sum(bool(result.get("passed")) for result in results.values())
    total = len(results)

    print("\n" + "=" * 80)
    print("CLAIM EVIDENCE SUMMARY")
    print("=" * 80)
    for claim, result in results.items():
        verdict = "PASS" if result.get("passed") else "FAIL"
        print(f"[{verdict}] {claim}: {result.get('status')}")
    print(f"SUMMARY passed={passed} total={total}")
    print(f"OUTPUT verdict={OUT / 'verdict_v4.json'}")
    print(f"OUTPUT matrix={OUT / 'claim_matrix.csv'}")
    print(f"OUTPUT figures={OUT / 'figures'}")
    if passed != total:
        print("PUBLICATION_GATE=FAIL")
        return 1
    print("PUBLICATION_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
