# Claims


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_085822b1989c", "created_at": "2026-07-21T11:54:52+00:00", "title": "Claims to reproduce"}
-->
## Claims to reproduce

1. Theorem 3.3 establishes that over signal classes with Effective Span Dimension (ESD) at most K, the minimax excess risk is asymptotically equivalent to K·σ², holding without classical eigenvalue-decay or source-condition assumptions (Theorem 3.3).
2. Theorem 3.2 shows the principal-component (PC) estimator's risk is sandwiched as (d†−1)σ² ≤ Risk ≤ 2d†σ², where d† is the Effective Span Dimension defined as the smallest number of leading eigenfunctions whose remaining tail signal energy no longer exceeds the noise level σ² (Theorem 3.2).
3. Theorem 4.3 gives convergence rates for a quota sequence {K_n}: the minimax risk over populations satisfying d†(σ0²/n; θ*, λ) ≤ K_n scales as Θ(K_n σ0²/n) (Theorem 4.3).
4. Theorem 5.2 proves that overparameterized gradient flow (OP-GF) can reduce the Effective Span Dimension over training time by assigning larger adapted eigenvalues to strong signal directions with initially small eigenvalues, moving the problem into a lower minimax-risk complexity class (Theorem 5.2).
5. Section 7 and Section 8 extend the Effective Span Dimension framework to linear regression (via SVD, minimax rate Θ(σ0²K/n)) and RKHS regression (rate Θ(σ̄²K_n/n) with effective noise σ̄² = (σ0² + ||f*||²_∞)/n) (Section 7, Section 8).
6. Numerical experiments show that span profiles decrease during OP-GF training—with larger improvements when initial signal-spectrum alignment is worse—and that deeper models attain lower Effective Span Dimension than shallow variants given sufficient training iterations (Numerical Validation).
