# Claim 6 - Numerical OP-GF and depth validation

## Canonical outcome

**PARTIALLY REPRODUCED. Figure 1 passes; the strict Figure 2 depth endpoint ordering is configuration-sensitive.**

## Anchored claim

The numerical section reports that OP-GF improves span profiles more strongly under greater initial misalignment and that deeper parameterizations can begin improving later yet finish with lower ESD/error.

## Predeclared tests, metrics, and acceptance rules

- Figure 1: integrate Equation (12) at `d=5000`; require aligned `q=1` to remain stable, every misaligned case to improve, and `q=3` to improve more than `q=1.5`.
- Figure 2: run 20 Monte Carlo replications; require ESD and oracle-PC error to decay, and compare final endpoints for depths `D=0,1,3`.

## Raw outcome and controls

Figure 1 passes: at `tau=sigma²`, ESD changes were `10→10`, `22→19`, `36→26`, and `88→33` for `q=1,1.5,2,3`, respectively.

Our disclosed clean-room Figure 2 configuration uses `d=512`, 20 replications, step size `0.05`, and 2400 steps:

| Depth | Final mean ESD |
| ---: | ---: |
| 0 | 25.55 |
| 1 | 23.50 |
| 3 | 25.80 |

All depths reduced ESD and error, and `D=1` finished below `D=0`; however the strict ordering `D0 > D1 > D3` does **not** hold. An independent reproduction using `d=5000`, `q=3`, step size `0.01`, and longer depth-dependent runs also reported a different endpoint order (`D3 < D0 < D1`). Together these results indicate configuration sensitivity rather than a universal depth ranking.

![Figure 2 depth evidence](https://raw.githubusercontent.com/MachineLearning-Nerd/icml26-repro-4HrWo5x7YF-spectral-minimax/agent/fix-all-v4-claims/outputs/v4/figures/figure2_depth.png)

## Missing information and honest scoring treatment

The paper does not disclose Figure 2's optimizer step size, initialization scale `b0`, random seed, or stopping-time selection. Therefore the qualitative “can finish lower” statement receives partial support, but exact paper-scale depth ordering is not claimed. This is the reason the report forecasts **1/2**, rather than 2/2, for this bucket.
