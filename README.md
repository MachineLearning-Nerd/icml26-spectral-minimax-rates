# ICML 2026 reproduction — Alignment-Sensitive Minimax Rates for Spectral Algorithms

**Collection status:** VERIFIED_SCOPED

**Evidence-release gate:** PASSED (PUBLICATION_GATE_PASS)

**Strict paper-level gate:** NOT_READY for claims that require an asymptotic
proof or undisclosed author-side experiment settings
**Owner and attribution:** MachineLearning-Nerd

This repository audits the paper *Alignment-Sensitive Minimax Rates for
Spectral Algorithms with Learned Kernels* by Dongming Huang, Zhifan Li,
Yicheng Li, and Qian Lin. The authoritative audited source is
[arXiv 2509.20294v4](https://arxiv.org/abs/2509.20294), revised 11 May 2026,
with source SHA-256
b08fee1a408d90102be6af7f8193862aa198b9acbd1e5c40601da927c96e7cef.

The repository's competition/reproduction identifier is 4HrWo5x7YF. The
original repository name was icml26-repro-4HrWo5x7YF-spectral-minimax; the
target public name is icml26-spectral-minimax-rates.

## What the paper is doing

The paper studies spectral estimators when the kernel or representation is
learned from data rather than fixed in advance. Its central complexity measure
is the effective span dimension (ESD), which combines signal alignment,
eigenvalue ordering, and noise level. The paper then:

- derives ESD-sensitive minimax rates for sequence models;
- analyzes oracle principal-component (PC/PCR) risk and quota-sequence rates;
- studies over-parameterized gradient flow (OP-GF) as a mechanism that can
  improve signal/eigenfunction alignment and reduce ESD;
- extends the framework to fixed-design linear models and random-design RKHS
  regression;
- contrasts learned-kernel alignment with ridge-regression saturation; and
- reports numerical depth and OP-GF experiments.

## Current status

The corrected v4 package contains 15 version-pinned ledger items grouped into
six paper-facing buckets. The evidence package passes all 11 grouped checks and
the seven deterministic unit tests recorded by the v4 run. PASS means the
declared finite, empirical, or proof-audit contract passed; it does not mean a
numerical program has proved an asymptotic theorem.

| Paper-facing bucket | Evidence result | Scope |
| --- | --- | --- |
| Claim 1 — Theorem 3.3 sequence minimax ESD rate | VERIFIED_SCOPED_PROOF_AUDIT | Proof assumptions plus contained hypercube lower bound and PC upper bound |
| Claim 2 — Proposition 3.2 and Proposition 3.7 | VERIFIED_SCOPED | 240 randomized finite cases, exact ESD constructions, and profile property checks |
| Claim 3 — Theorem 4.3 quota rate | VERIFIED_SCOPED_PROOF_AUDIT | Condition audit plus finite lower/upper curves for K_n=floor(sqrt(n)) |
| Claim 4 — Theorem 5.2 OP-GF reduction | VERIFIED_SCOPED_CONDITIONAL | Assumption-aware audit and actual Equation (12) dynamics |
| Claim 5 — linear/RKHS/learned-kernel/ridge extensions | VERIFIED_SCOPED | Fixed-design PCR, random-design KPCPE, alignment controls, and finite ridge bounds |
| Claim 6 — numerical OP-GF and depth behavior | VERIFIED_SCOPED_EMPIRICAL | Figure 1 reproduction and paired paper-scale Figure 2 evidence |

The recorded CPU evidence run was OpenResearch run
4a067f01-3c6a-4f55-a8c1-8388cb364dc3; it reports 11/11 grouped checks and
7/7 unit tests in 1 minute 50 seconds. The repository makes no new external
judge-score claim. The historical v4 package forecasts 12/12 at its declared
scoring scope, subject to judge review.

## Claim-to-evidence production paths

| Bucket | Fine-grained ledger items | Producer | Machine-readable evidence |
| --- | --- | --- | --- |
| Claim 1 | T3.3 | repro/src/experiments.py::check_sequence_theory | outputs/v4/verdict_v4.json → T3.3 |
| Claim 2 | P3.2, P3.7 | repro/src/experiments.py::check_sequence_theory | outputs/v4/verdict_v4.json → P3.2, P3.7 |
| Claim 3 | T4.3 | repro/src/experiments.py::check_quota_sequence | outputs/v4/verdict_v4.json → T4.3 |
| Claim 4 | T5.2, F1 | run_span_profile_experiment and repro/src/spectral.py::opgf | outputs/v4/verdict_v4.json → T5.2, F1 |
| Claim 5 | PB.2, TB.3, F3, PC.4, TC.7-C.8, F4, D1-D2, I.6 | run_linear_experiment, run_rkhs_experiment, run_pathwise_experiment, and check_ridge | outputs/v4/verdict_v4.json and outputs/v4/claim_matrix.csv |
| Claim 6 | F1, F2 | run_span_profile_experiment and run_depth_experiment | outputs/v4/verdict_v4.json → F1, F2; outputs/v4/figures/figure1_span_profiles.png and figure2_depth.png |

The complete 15-item inventory, anchor, category, method, and paper checksum
are in claims/claims_v4.json. The detailed evaluator pages under
.trackio/logbook/pages/ preserve the predeclared acceptance rules, raw
outcomes, controls, and scope boundaries.

## Repository contents

- repro/src/spectral.py — ESD, span profiles, PC/PCR risk, ridge bounds,
  OP-GF dynamics, and batched OP-GF primitives.
- repro/src/experiments.py — grouped producers for the sequence, quota,
  OP-GF, depth, fixed-design, RKHS, learned-kernel, and ridge checks.
- repro/src/verify_spectral.py — fixed entry point that runs the v4 suite and
  emits the publication-gate summary.
- tests/test_spectral.py — seven deterministic unit tests for ESD, PC risk,
  span profiles, OP-GF updates, batching, and the finite Bayes lower bound.
- claims/claims_v4.json — version-pinned paper ledger.
- outputs/v4/ — verdict JSON, claim matrix, and five generated figures.
- outputs/verify_run.log — recorded evidence log.
- GATE_READY.md, publication_gate.json, STATUS.md, and AUDIT_REPORT.md —
  gate and audit records.

## Reproduce

~~~bash
uv sync --frozen
uv run pytest
uv run python repro/src/verify_spectral.py
~~~

The verifier writes fresh output under outputs/v4/. The recorded evidence was
CPU-only and does not require a GPU.

## Scope and limitations

- T3.3, T4.3, and T5.2 are theorem or conditional-theorem claims. The package
  audits assumptions and checks finite consequences; it does not numerically
  prove their asymptotic/uniform statements.
- The paper leaves several numerical choices undisclosed, including some
  seeds, signal amplitude, optimizer settings, and stopping-time choices.
  Those clean-room choices are recorded in the v4 pages and outputs.
- Figure 2 uses a paper-scale d=5000 paired CPU experiment with disclosed
  settings and two independent seeds.
- Figure 5's learned-kernel path is deliberately scale-reduced from the
  paper's p=900 setup to p=64; it supports the mechanism and controls, not
  bit-for-bit recovery of the author run.
- Numerical evidence is tied to arXiv v4. A future paper revision should
  receive a new source hash and a new ledger review.

## Branch map

The final branch names describe purpose. Historical names are retained only in
the audit mapping and are removed from the public remote after migration.

| Final branch | Historical source | Purpose |
| --- | --- | --- |
| main | master plus the corrected release | Canonical README, audit records, v4 evidence, and default publication surface |
| baseline/proxy-checks | master | Original six proxy checks, preserved as a historical baseline |
| release/v4-corrected-claims | agent/fix-all-v4-claims | Corrected v4 15-item ledger, experiments, controls, and recorded evidence |

## Citation

~~~bibtex
@article{huang2025alignment,
  title   = {Alignment-Sensitive Minimax Rates for Spectral Algorithms with Learned Kernels},
  author  = {Huang, Dongming and Li, Zhifan and Li, Yicheng and Lin, Qian},
  journal = {arXiv preprint arXiv:2509.20294},
  year    = {2025},
  note    = {Version 4, revised 11 May 2026},
  url     = {https://arxiv.org/abs/2509.20294}
}
~~~

## Thank you

Thank you to Dongming Huang, Zhifan Li, Yicheng Li, and Qian Lin for making
the paper and its mathematical framework available for careful reproduction.
The ESD formulation, OP-GF analysis, and extension structure made it possible
to turn the initial proxy checks into a more faithful, scope-labeled audit.

## Attribution

This reproduction package and its audit documentation are maintained by
MachineLearning-Nerd. The repository is a clean-room reproduction and is not
the authors' implementation.
