# Recorded evidence

## Sequence and minimax claims

- P3.2 passed 240 randomized cases; constructed targets had exact ESD `1,2,4,8,16`.
- The valid hypercube lower bound for T3.3 was `0.4496 K sigma²`; the PC upper bound was `1.0 K sigma²` for `K=2,4,8,16`.
- P3.7 monotonicity, generalized inversion, trade-off dominance, and profile dominance all passed.
- T4.3's `K_n=floor(sqrt(n))` quota condition passed; finite lower/target ratios were `0.4496` and upper/target ratios were `1.0`.

## OP-GF and span profiles

- Equation (12) is integrated directly; there is no manual eigenvalue boost.
- At `tau=sigma²`, Figure 1 ESD paths were `10→10` (`q=1`), `22→19` (`q=1.5`), `36→26` (`q=2`), and `88→33` (`q=3`).
- Relative log-profile improvement increased with misalignment: `-0.001, 0.012, 0.060, 0.439`.
- Figure 2 used `d=5000`, `q=3`, and 20 paired replications. At seed 2509, final mean ESD was `36.25`, `34.90`, and `33.90` for `D=0,1,3`.
- Paired 95% CIs were `[-2.083,-0.617]` for D1−D0, `[-1.526,-0.474]` for D3−D1, and `[-3.314,-1.386]` for D3−D0.
- Independent seed 19 also verified the ordering: `32.85 > 31.60 > 30.30`, again with all paired intervals below zero.

## Linear, RKHS, learned-kernel, and ridge claims

- Fixed-design ESD/oracle-risk correlations were `0.9683` and `0.9864`; every PCR sandwich point passed.
- RKHS ESD/risk correlation was `0.9987`; all KPCPE risks lay within the claimed bounds using the recorded three-standard-error criterion.
- Permuting an unchanged eigenvalue multiset changed ESD from `8` (aligned) to `16` (misaligned).
- The scale-reduced four-layer path changed ESD `21→1` and risk `1.4807→0.0030`.
- Ridge ESD was `7` while ridge saturating dimension was `27`; variance, bias, and theorem lower bounds all passed.

Full machine-readable values are committed in `outputs/verdict.json` and `outputs/v4/`. The complete run log is `outputs/verify_run.log`.
