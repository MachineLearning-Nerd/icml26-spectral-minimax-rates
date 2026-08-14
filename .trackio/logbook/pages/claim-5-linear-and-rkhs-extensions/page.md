# Claim 5 - Linear and RKHS extensions

## Canonical outcome

**SUPPORTED across the fixed-design, random-design RKHS, alignment-control, and ridge-saturation checks.**

## Anchored claims

This scoring bucket covers the paper's main extensions: Proposition B.2 and Theorem B.3 for fixed-design PCR; Proposition C.4 and Theorems C.7-C.8 for kernel principal-component projection; Appendix D's learned-eigensystem alignment mechanism; and Theorem I.6's ridge saturation lower bound.

## Predeclared tests and acceptance rules

- Fixed design (`n=300`, `p=400`): enumerate oracle PCR risk, require every Proposition B.2 sandwich point to pass, and require ESD/risk correlation above `0.9`.
- RKHS (`n=400`, `J=800`, 10 replications): require Monte Carlo KPCPE risk to remain inside its ESD bounds using the recorded three-standard-error rule and correlation above `0.9`.
- Alignment control: hold the eigenvalue multiset fixed, permute eigenvectors relative to the signal, and require ESD to change.
- Ridge: evaluate every Theorem I.6 bound term under Assumption I.2 and distinguish ridge saturating dimension from ESD.

## Raw outcomes and controls

| Check | Outcome |
| --- | --- |
| Fixed-design ESD/oracle-risk correlation | `0.9683` and `0.9864` across the recorded sweeps |
| PCR sandwich | every point passed |
| RKHS ESD/risk correlation | `0.9987` |
| KPCPE bounds | every point passed at three-standard-error tolerance |
| Equal-spectrum control | ESD `8` aligned vs `16` misaligned |
| Scale-reduced learned path | ESD `21→1`, risk `1.4807→0.0030` |
| Ridge control | ESD `7`, ridge saturating dimension `27`; all bound terms passed |

![Fixed-design evidence](https://raw.githubusercontent.com/MachineLearning-Nerd/icml26-spectral-minimax-rates/main/outputs/v4/figures/figure3_linear.png)

![RKHS evidence](https://raw.githubusercontent.com/MachineLearning-Nerd/icml26-spectral-minimax-rates/main/outputs/v4/figures/figure4_rkhs.png)

## Scope boundary

Figure 5 is deliberately scale-reduced from the paper's `p=900` to `p=64` for CPU. It verifies the pathwise mechanism and equal-spectrum alignment effect, not exact recovery of the paper's undisclosed training run.
