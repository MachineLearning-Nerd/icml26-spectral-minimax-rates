# Source manifest

## Paper identity

- Title: *Alignment-Sensitive Minimax Rates for Spectral Algorithms with Learned Kernels*
- Authors: Dongming Huang, Zhifan Li, Yicheng Li, and Qian Lin
- Authoritative version: arXiv 2509.20294v4
- Paper URL: https://arxiv.org/abs/2509.20294
- Competition/reproduction identifier: 4HrWo5x7YF
- Current arXiv revision: 11 May 2026
- Downloaded PDF SHA-256: b08fee1a408d90102be6af7f8193862aa198b9acbd1e5c40601da927c96e7cef

## Repository identity

- Original name: icml26-repro-4HrWo5x7YF-spectral-minimax
- Target name: icml26-spectral-minimax-rates
- Owner: MachineLearning-Nerd
- Intended default branch: main

## Evidence sources

- Claim inventory: claims/claims_v4.json
- Main verifier: repro/src/verify_spectral.py
- Grouped producers: repro/src/experiments.py
- Numerical primitives: repro/src/spectral.py
- Unit tests: tests/test_spectral.py
- Recorded log: outputs/verify_run.log
- Aggregated verdict: outputs/v4/verdict_v4.json
- Claim matrix: outputs/v4/claim_matrix.csv
- Figures: outputs/v4/figures/
- Recorded OpenResearch run: 4a067f01-3c6a-4f55-a8c1-8388cb364dc3

## Evidence interpretation

The v4 ledger distinguishes finite identities, proof audits, conditional proof
claims, and empirical reproductions. A passing output is evidence for its
declared contract only. It is not a replacement for the paper's proofs and
does not imply exact recovery of undisclosed author-side experiment settings.

## Reproducibility command

~~~bash
uv sync --frozen
uv run pytest
uv run python repro/src/verify_spectral.py
~~~
