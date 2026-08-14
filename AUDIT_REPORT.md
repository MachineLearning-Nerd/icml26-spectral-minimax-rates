# Audit report

## Executive assessment

The corrected v4 release is a trustworthy, scope-labeled evidence package for
the paper's 15-item ledger. All 11 grouped checks and all seven deterministic
unit tests in the recorded CPU run passed. The defensible collection status is
VERIFIED_SCOPED, not an unrestricted assertion that every asymptotic theorem
has been numerically proved.

## Paper/repository association

The repository is associated with *Alignment-Sensitive Minimax Rates for
Spectral Algorithms with Learned Kernels*, arXiv 2509.20294v4, by Dongming
Huang, Zhifan Li, Yicheng Li, and Qian Lin. The identifier 4HrWo5x7YF is the
competition/reproduction identifier recorded by the repository.

## Claim production audit

| Bucket | Producer path | Evidence | Interpretation |
| --- | --- | --- | --- |
| Claim 1 | check_sequence_theory → T3.3 | Valid contained Rademacher hypercube and PC upper bound for K=2,4,8,16 | Supports the rate at finite consequence/proof-audit scope |
| Claim 2 | check_sequence_theory → P3.2, P3.7 | 240 randomized sandwich cases, exact ESD targets, profile identities | Finite identities and property checks pass |
| Claim 3 | check_quota_sequence → T4.3 | Condition audit and six quota values through n=2304 | Supports the declared finite rate curve, not the uniform theorem by itself |
| Claim 4 | run_span_profile_experiment → T5.2, F1 | Equation (12) OP-GF dynamics, controls, stated-scale d=5000 | Conditional theorem scope audited; empirical mechanism reproduced |
| Claim 5 | linear/RKHS/pathwise/ridge producers | PCR, KPCPE, equal-spectrum, learned-path, and ridge checks | Extensions pass at declared finite/empirical scope |
| Claim 6 | run_span_profile_experiment and run_depth_experiment → F1, F2 | Figure 1 and paired d=5000, 20-replication Figure 2 runs at two seeds | Numerical behavior reproduced under disclosed clean-room settings |

## Controls and limitations

- ESD is implemented as a function of the noise level tau, rather than as a
  single scalar proxy.
- OP-GF is integrated through the paper's dynamics; the evidence does not
  manually boost eigenvalues.
- Equal-spectrum permutation and aligned q=1 controls are retained.
- The paper omits several numerical settings; the v4 package records the
  clean-room choices instead of hiding them.
- The learned-kernel path is scale-reduced from p=900 to p=64.
- Theorem claims remain proof-audited/conditional because finite numerical
  checks cannot establish their asymptotic quantifiers.

## Gate interpretation

PUBLICATION_GATE_PASS means the declared evidence package is complete,
reproducible, and internally consistent. It does not mean that a CPU script
has replaced the paper's proofs. The v4 forecast of 12/12 is preserved as a
forecast only; no external judge score is invented.
