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
`96c9bb65-ace8-41ae-be09-b2a4b7c45601` on CPU: all 11 grouped checks covering
the 15-item ledger passed in 15 seconds. `outputs/verify_run.log` is the full
evidence log, while `outputs/verdict.json` is the compatibility copy of the v4
machine-readable verdict.

## Scope disclosure

Figures 1, 3, and 4 use the dimensions stated in v4. Figure 2 uses the paper's
20 replications but discloses clean-room optimizer settings because its step
size and initialization are not specified in the paper. Figure 5 is explicitly
scale-reduced for CPU and supports the pathwise mechanism; it is not presented
as an exact numerical replication of the paper's `p=900` run.

The paper also omits the Figure 1 seed, signal amplitude `C`, optimizer step
size, and stopping-time selection. The reproduction therefore records its
deterministic clean-room choices and tests the reported qualitative pattern;
it does not claim bit-for-bit recovery of undisclosed experiment settings.
