# Executive summary

## Canonical outcome

**Five scored claims are supported at their stated scope; one numerical claim is only partially reproduced. Forecast: 11/12, not a judged score.**

This report maps the six judge-facing claim buckets to a version-pinned 15-item ledger for arXiv `2509.20294v4`. The underlying CPU run passed all 11 internal evidence gates, but an internal gate is not automatically a full scoring claim. In particular, the Figure 2 depth endpoint ordering is sensitive to optimizer settings that the paper does not disclose.

| Scored claim | Fine-grained ledger coverage | Outcome |
| --- | --- | --- |
| 1. Theorem 3.3 minimax ESD rate | T3.3 | Supported by proof audit and finite lower/upper construction |
| 2. Proposition 3.2 oracle-PC sandwich | P3.2 | Verified in 240 randomized cases plus exact constructions |
| 3. Theorem 4.3 quota rate | T4.3 | Supported by condition audit and finite rate curves |
| 4. Theorem 5.2 OP-GF reduction | T5.2, P3.7 | Conditional theorem audited; actual dynamics satisfy the tested endpoint mechanism |
| 5. Linear and RKHS extensions | PB.2, TB.3, F3, PC.4, TC.7-C.8, F4, D1-D2, I.6 | Supported at the disclosed fixed-design, random-design, and finite-bound scope |
| 6. Numerical OP-GF and depth | F1, F2 | Figure 1 reproduced; Figure 2 endpoint ranking is configuration-sensitive |

## Exact reproducibility

```bash
uv sync --frozen
uv run pytest -q
uv run python repro/src/verify_spectral.py
```

- Paper: arXiv `2509.20294v4`
- Paper SHA-256: `b08fee1a408d90102be6af7f8193862aa198b9acbd1e5c40601da927c96e7cef`
- Recorded OpenResearch run: `c23993b2-b1df-47ad-b572-e18e8dc77a6f`
- Environment: CPython 3.12.11, NumPy 2.5.1, local CPU
- Result: 11/11 internal evidence gates, 6/6 unit tests, 15 seconds
- Source and raw evidence: [GitHub draft PR #1](https://github.com/MachineLearning-Nerd/icml26-repro-4HrWo5x7YF-spectral-minimax/pull/1)

No GPU is required for this package. “Supported” for an asymptotic theorem means the proof assumptions and scope were audited and valid finite consequences were checked; a numerical program does not prove an asymptotic minimax theorem.
