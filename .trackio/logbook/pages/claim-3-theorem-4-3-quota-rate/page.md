# Claim 3 - Theorem 4.3 quota convergence rate

## Canonical outcome

**SUPPORTED at theorem-audit and finite-rate scope.**

## Anchored claim

Under Condition 4.1, Theorem 4.3 gives minimax risk of order `sigma0² K_n / n` for the quota sequence class.

## Predeclared test, metric, and acceptance rule

Use the admissible quota `K_n = floor(sqrt(n))`, check Condition 4.1, and evaluate contained-hypercube lower and oracle-PC upper constructions for `n = 64, 144, 256, 576, 1024, 2304`. Require both bounds to track `sigma0² K_n / n` by constants independent of `n`.

## Raw outcome and controls

| n | K_n | lower / target | upper / target |
| ---: | ---: | ---: | ---: |
| 64 | 8 | 0.4496 | 1.0000 |
| 144 | 12 | 0.4496 | 1.0000 |
| 256 | 16 | 0.4496 | 1.0000 |
| 576 | 24 | 0.4496 | 1.0000 |
| 1024 | 32 | 0.4496 | 1.0000 |
| 2304 | 48 | 0.4496 | 1.0000 |

Condition 4.1 passed for the declared sequence, and the ratios remain constant over the tested range.

## Scope boundary

As with Claim 1, the computation checks a valid finite consequence and the analytic audit checks assumptions; it does not turn a finite table into a proof of a uniform minimax theorem.
