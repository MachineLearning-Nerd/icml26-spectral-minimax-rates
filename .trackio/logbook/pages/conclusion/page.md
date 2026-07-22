# Conclusion

The corrected package covers all 15 version-pinned v4 ledger items and passes all 11 internal evidence gates on CPU. Mapped to the six 2-point scoring buckets, the evidence supports **five full claims plus one partial claim: an evidence-based forecast of 11/12, not a guaranteed judge score**.

| Bucket | Treatment |
| --- | --- |
| Claims 1-5 | supported at their explicitly stated analytic or empirical scope |
| Claim 6 | Figure 1 reproduced; Figure 2 strict depth ordering remains unresolved/configuration-sensitive |

This is a clean-room reproduction, not bit-for-bit recovery of undisclosed author code. Figures 1 and 2 omit optimizer details and random seeds; Figure 5 is scale-reduced from `p=900` to `p=64`. Every such choice is disclosed.

Most importantly, proof claims are not inflated into empirical proofs. Asymptotic minimax theorems are labeled as proof/assumption audits with valid finite lower and upper checks. The complete source, tests, machine-readable verdict, claim matrix, figures, and run log are available in [GitHub draft PR #1](https://github.com/MachineLearning-Nerd/icml26-repro-4HrWo5x7YF-spectral-minimax/pull/1), and the package is reproducible without a GPU.
