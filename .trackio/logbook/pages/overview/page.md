# Alignment-Sensitive Minimax Rates for Spectral Algorithms

- OpenReview: `4HrWo5x7YF`
- Paper: arXiv `2509.20294v4`
- SHA-256: `b08fee1a408d90102be6af7f8193862aa198b9acbd1e5c40601da927c96e7cef`

This is a CPU-only clean-room reproduction with a version-pinned 15-item claim ledger. The recorded OpenResearch run `4a067f01-3c6a-4f55-a8c1-8388cb364dc3` passed all 11 grouped evidence gates in 1 minute 50 seconds. Claim 6 now uses the paper-scale `d=5000` setup and 20 paired replications.

Unlike the earlier six proxy checks, this version uses the paper's actual ESD/span-profile definition, integrates the OP-GF equations, runs fixed-design PCR and random-design RKHS experiments, and separates numerical evidence from proof claims.

## Reproduce

```bash
uv sync --frozen
uv run pytest
uv run python repro/src/verify_spectral.py
```

No GPU is required.
