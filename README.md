# Reproduction — Alignment-Sensitive Minimax Rates for Spectral Algorithms

CPU-only clean-room reproduction for OpenReview `4HrWo5x7YF` and
arXiv [`2509.20294v4`](https://arxiv.org/abs/2509.20294).

This branch replaces the original six proxy checks with a version-pinned claim
ledger and genuine model implementations. In particular, it:

- computes the span profile as the function `tau -> ESD(tau)`, not as a scalar ratio;
- integrates the OP-GF parameter dynamics instead of manually boosting eigenvalues;
- runs a real fixed-design SVD/PCR experiment;
- runs a random-design cosine-basis RKHS/KPCPE experiment;
- includes equal-spectrum alignment and ridge-saturation controls;
- labels minimax theorems as proof claims with finite-case validation rather
  than claiming that a short numerical script proves an infimum-supremum result.

## Reproduce

```bash
uv sync --frozen
uv run pytest
uv run python repro/src/verify_spectral.py
```

The full suite writes machine-readable evidence to `outputs/v4/`, including a
claim matrix, JSON verdict, and five figures. The exact claim inventory and
paper checksum are in `claims/claims_v4.json`.

The committed evidence was produced by OpenResearch run
`4a067f01-3c6a-4f55-a8c1-8388cb364dc3` on CPU: all 11 grouped checks covering
the 15-item ledger passed in 1 minute 50 seconds. `outputs/verify_run.log` is the full
evidence log, while `outputs/verdict.json` is the compatibility copy of the v4
machine-readable verdict.

## Scope disclosure

Figures 1–4 use the dimensions stated in v4. Figure 2 uses `d=5000`, `q=3`,
20 paired replications, and discloses its optimizer settings because the paper
does not specify its step size, initialization, seed, or stopping rule. Two
independent seeds verify the strict endpoint ordering with paired 95% confidence
intervals below zero. Figure 5 is explicitly
scale-reduced for CPU and supports the pathwise mechanism; it is not presented
as an exact numerical replication of the paper's `p=900` run.

The paper also omits the Figure 1 seed, signal amplitude `C`, optimizer step
size, and stopping-time selection. The reproduction therefore records its
deterministic clean-room choices and tests the reported qualitative pattern;
it does not claim bit-for-bit recovery of undisclosed experiment settings.
