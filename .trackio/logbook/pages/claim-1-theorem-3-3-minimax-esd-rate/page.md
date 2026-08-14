# Claim 1 - Theorem 3.3 minimax ESD rate

## Canonical outcome

**SUPPORTED at theorem-audit and finite-consequence scope.**

## Anchored claim

Theorem 3.3 states that minimax risk over sequence classes with effective signal dimension bounded by `K` is of order `K sigma²`, uniformly in the theorem's stated regime.

## Predeclared test, metric, and acceptance rule

The verifier checks both directions without pretending to numerically evaluate an asymptotic infimum-supremum:

1. construct a `K`-coordinate hypercube contained in the ESD-bounded class and compute its Bayes lower bound;
2. compute the oracle-PC upper bound on the same finite instances;
3. require both ratios to `K sigma²` to remain bounded away from zero and infinity for `K = 2, 4, 8, 16`.

## Raw outcome and controls

| K | lower / `K sigma²` | PC upper / `K sigma²` | hypercube contained |
| ---: | ---: | ---: | --- |
| 2 | 0.4496 | 1.0000 | yes |
| 4 | 0.4496 | 1.0000 | yes |
| 8 | 0.4496 | 1.0000 | yes |
| 16 | 0.4496 | 1.0000 | yes |

The lower construction is explicitly checked for class membership; this avoids using a visually plausible but invalid lower-bound family. Machine-readable rows are in [`outputs/v4/verdict_v4.json`](https://github.com/MachineLearning-Nerd/icml26-spectral-minimax-rates/blob/main/outputs/v4/verdict_v4.json).

## Scope boundary

The finite experiment validates the predicted `K sigma²` scaling and the proof audit checks the theorem's quantifiers and assumptions. It is evidence for the theorem, not a numerical proof of its uniform asymptotic statement.
