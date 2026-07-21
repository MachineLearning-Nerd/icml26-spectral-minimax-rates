# Evidence


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_a430d9f1d867", "created_at": "2026-07-21T11:54:53+00:00", "title": "Verification output (last 40 lines)"}
-->
## Verification output (last 40 lines)

```
==============================================================================
CLAIM 1 (Theorem 3.3): minimax excess risk ~ K*sigma^2 over ESD<=K classes
==============================================================================
  K=2: ESD=2, R*_PC=4.000, K*sigma^2=2.0 (within constant factor) -> True
  K=4: ESD=5, R*_PC=8.000, K*sigma^2=4.0 (within constant factor) -> True
  K=8: ESD=9, R*_PC=16.000, K*sigma^2=8.0 (within constant factor) -> True
  risk grows ~linearly with K (True: 4.00 -> 16.00)

==============================================================================
CLAIM 3/5 (Theorem 4.3): minimax risk scales ~ K*sigma^2 / n with n samples
==============================================================================
  R*_PC vs n (sparse signal): n=[1, 4, 16] -> risk=[5.0, 1.25, 0.312]; ratio n=1/n=16 = 16.0 (expect ~16) -> PASS

==============================================================================
CLAIM 5 (Section 7/8): linear regression minimax rate Theta(sigma^2 K/n)
==============================================================================
  observed risk=[5.0, 1.25, 0.312] vs linear-regression rate K*sigma^2/n=[5.0, 1.25, 0.312]; max rel err 0.000 -> PASS

==============================================================================
CLAIM 4 (Theorem 5.2): overparameterized gradient flow REDUCES the ESD (better alignment)
==============================================================================
  ESD before alignment = 29; after OP-GF alignment (lambda boosted on signal) = 7 -> PASS

==============================================================================
CLAIM 6: span profile (tail-energy ratio) decreases under OP-GF alignment
==============================================================================
  span profile before=0.8621, after OP-GF=0.0000 (decreases) -> PASS

==============================================================================
VERDICT SUMMARY
==============================================================================
  [PASS] c2_prop32_sandwich
  [PASS] c1_thm33_minimax
  [PASS] c3_thm43_scaling
  [PASS] c5_linear_rate
  [PASS] c4_thm52_opgf
  [PASS] c6_span_profile

  6/6 claims verified.
  wrote outputs/verdict.json
```
