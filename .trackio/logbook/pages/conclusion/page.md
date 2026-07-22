# Conclusion

All 15 version-pinned v4 claims are covered, and all 11 grouped evidence gates pass on CPU.

The result is a **clean-room reproduction**, not a bit-for-bit recovery of undisclosed author code. Figures 1 and 2 omit optimizer details and random seeds in the paper, so this package records its choices. Figure 5 is scale-reduced from `p=900` to `p=64` for CPU and supports the pathwise mechanism rather than claiming exact numerical replication.

Most importantly, proof claims are not inflated into empirical proofs: asymptotic minimax theorems are labeled as proof/assumption audits with valid finite lower and upper checks. The package is reproducible without a GPU using `uv` and the locked dependency file.
