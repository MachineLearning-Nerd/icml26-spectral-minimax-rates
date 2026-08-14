# Claim 4 - Theorem 5.2 OP-GF reduces ESD

## Canonical outcome

**SUPPORTED under the theorem's stated endpoint assumptions.**

## Anchored claim

For fixed factorization depth `D >= 1`, Theorem 5.2 gives a conditional weak reduction of effective signal dimension between specified OP-GF endpoints, subject to its sample-size, initialization, signal-separation, rank, and margin conditions.

## Predeclared test, metric, and acceptance rule

1. audit every stated theorem clause and preserve the weak, conditional conclusion;
2. integrate the paper's Equation (12) dynamics directly—no manual eigenvalue boost;
3. require the misaligned cases to improve their log span profiles, with greater improvement for the most misaligned `q=3` case than the mild `q=1.5` case;
4. retain aligned `q=1` as a negative control with little room for improvement.

## Raw outcome and controls

| q | ESD at `tau=sigma²`, start → finish | relative log-profile improvement |
| ---: | ---: | ---: |
| 1.0 | 10 → 10 | -0.001 |
| 1.5 | 22 → 19 | 0.012 |
| 2.0 | 36 → 26 | 0.060 |
| 3.0 | 88 → 33 | 0.439 |

- All seven audited theorem clauses passed.
- Actual OP-GF dynamics: yes.
- Manual eigenvalue modification: no.
- Stated-scale sequence dimension: `d=5000`.

![Figure 1 span-profile evidence](https://raw.githubusercontent.com/MachineLearning-Nerd/icml26-spectral-minimax-rates/main/outputs/v4/figures/figure1_span_profiles.png)

## Scope boundary

The theorem is a conditional high-probability endpoint result. The numerical trajectory illustrates its mechanism; the analytic claim is accepted only at the audited assumption scope.
