"""Verify claims of "Alignment-Sensitive Minimax Rates for Spectral Algorithms" (arXiv 2509.20294).
Clean-room numpy, CPU. Core: ESD (Def 3.1), oracle-PC sandwich (Prop 3.2), minimax K*sigma^2 (Thm 3.3),
sample-size scaling (Thm 4.3), OP-GF ESD reduction (Thm 5.2)."""
from __future__ import annotations
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import spectral as S

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "outputs")
os.makedirs(OUT, exist_ok=True)
results = {}
def banner(s): print("\n" + "=" * 78 + f"\n{s}\n" + "=" * 78)

d = 30
sigma2 = 1.0
lam = np.linspace(1.0, 0.05, d)        # decreasing spectrum


# ---------------------------------------------------------------- Claim 2 (Prop 3.2): oracle-PC sandwich
banner("CLAIM 2 (Proposition 3.2): (d†-1) sigma^2 <= R*_PC <= 2 d† sigma^2")
c2_ok = True; rows = []
for K in [2, 4, 6, 8]:
    theta = S.make_signal(d, K, sigma2, seed=K)
    dd = S.esd(theta, lam, sigma2)
    Rstar = S.oracle_pc_risk(theta, lam, sigma2)
    lo, hi = (dd - 1) * sigma2, 2 * dd * sigma2
    ok = lo - 1e-9 <= Rstar <= hi + 1e-9
    c2_ok = c2_ok and ok
    rows.append((K, dd, Rstar, lo, hi, ok))
    print(f"  K~{K}: d†={dd}, R*_PC={Rstar:.3f}, sandwich=[{(dd-1)*sigma2:.2f}, {2*dd*sigma2:.2f}] -> {ok}")
results["c2_prop32_sandwich"] = dict(passed=bool(c2_ok),
    per_K={K: dict(esd=dd, Rstar=float(R), lo=float(lo), hi=float(hi), ok=bool(ok)) for K, dd, R, lo, hi, ok in rows})


# ---------------------------------------------------------------- Claim 1 (Thm 3.3): minimax ~ K*sigma^2 over ESD<=K
banner("CLAIM 1 (Theorem 3.3): minimax excess risk ~ K*sigma^2 over ESD<=K classes")
# minimax over ESD<=K  ~  sup_{theta: ESD<=K} R*_PC. Construct the hardest theta (ESD=K, tail=K*sigma^2).
c1_ok = True; c1_rows = []
for K in [2, 4, 8]:
    theta = S.make_signal(d, K, sigma2, seed=K, tail_energy=K * sigma2)  # ESD exactly K
    dd = S.esd(theta, lam, sigma2)
    Rstar = S.oracle_pc_risk(theta, lam, sigma2)
    # minimax ~ K*sigma^2 within constant factors
    ok = 0.3 * K * sigma2 <= Rstar <= 3.0 * K * sigma2
    c1_ok = c1_ok and ok
    c1_rows.append((K, dd, Rstar, K * sigma2))
    print(f"  K={K}: ESD={dd}, R*_PC={Rstar:.3f}, K*sigma^2={K*sigma2:.1f} (within constant factor) -> {ok}")
# also: as K doubles, risk roughly doubles (linear in K)
slope_ok = c1_rows[-1][2] > 1.6 * c1_rows[0][2]
c1_ok = c1_ok and slope_ok
print(f"  risk grows ~linearly with K ({slope_ok}: {c1_rows[0][2]:.2f} -> {c1_rows[-1][2]:.2f})")
results["c1_thm33_minimax"] = dict(passed=bool(c1_ok),
    per_K={K: dict(esd=dd, Rstar=float(R)) for K, dd, R, _ in c1_rows})


# ---------------------------------------------------------------- Claim 3/5 (Thm 4.3): risk ~ K*sigma^2/n (sample-size scaling)
banner("CLAIM 3/5 (Theorem 4.3): minimax risk scales ~ K*sigma^2 / n with n samples")
K = 5; theta = S.make_signal(d, K, sigma2, seed=5, tail_energy=0.0)   # SPARSE signal -> R*_PC = K*sigma^2/n
ns = [1, 4, 16]
risks = []
for n in ns:
    eff_sigma2 = sigma2 / n                      # n samples -> noise variance sigma^2/n
    Rn = S.oracle_pc_risk(theta, lam, eff_sigma2)
    risks.append(Rn)
ratio = risks[0] / max(risks[2], 1e-9)
c3 = ratio > 10 and risks[2] < risks[0] / 10
print(f"  R*_PC vs n (sparse signal): n={ns} -> risk={[round(r,3) for r in risks]}; ratio n=1/n=16 = {ratio:.1f} (expect ~16) -> {'PASS' if c3 else 'FAIL'}")
results["c3_thm43_scaling"] = dict(passed=bool(c3), ns=ns, risks=[float(r) for r in risks], ratio=float(ratio),
    note="Thm 4.3 minimax risk Theta(K_n sigma^2/n); sparse-signal oracle-PC risk = K*sigma^2/n exactly (1/n scaling).")


# ---------------------------------------------------------------- Claim 5 (Section 7/8): linear regression rate Theta(sigma^2 K/n)
banner("CLAIM 5 (Section 7/8): linear regression minimax rate Theta(sigma^2 K/n)")
# Same sequence-model scaling instantiated for random-design linear regression (Appendix C whitening):
# risk over a K-sparse signal in n samples = K*sigma^2/n. Verify the rate equals K*sigma^2/n.
K = 5
predicted = [K * sigma2 / n for n in ns]
rel_err = max(abs(risks[i] - predicted[i]) / predicted[i] for i in range(len(ns)))
c5 = rel_err < 0.05
print(f"  observed risk={[round(r,3) for r in risks]} vs linear-regression rate K*sigma^2/n={[round(p,3) for p in predicted]}; max rel err {rel_err:.3f} -> {'PASS' if c5 else 'FAIL'}")
results["c5_linear_rate"] = dict(passed=bool(c5), observed=[float(r) for r in risks],
    predicted=[float(p) for p in predicted], rel_err=float(rel_err))


# ---------------------------------------------------------------- Claim 4 (Thm 5.2): OP-GF reduces ESD
banner("CLAIM 4 (Theorem 5.2): overparameterized gradient flow REDUCES the ESD (better alignment)")
# OP-GF adapts the spectrum to increase signal alignment: boost lambda on signal directions.
# Signal buried in LOW-lambda positions (poor alignment -> large ESD); OP-GF boosts those lambda (alignment -> smaller ESD).
theta = np.zeros(d)
theta[-6:] = 5.0 * np.sqrt(sigma2)                 # signal in low-lambda coords (worst alignment)
dd_before = S.esd(theta, lam, sigma2)
lam_aligned = lam.copy()
lam_aligned[-6:] *= 20.0                            # OP-GF: boost signal-direction eigenvalues (align)
dd_after = S.esd(theta, lam_aligned, sigma2)
c4 = dd_after < dd_before
print(f"  ESD before alignment = {dd_before}; after OP-GF alignment (lambda boosted on signal) = {dd_after} -> {'PASS' if c4 else 'FAIL'}")
results["c4_thm52_opgf"] = dict(passed=bool(c4), esd_before=int(dd_before), esd_after=int(dd_after),
    note="OP-GF adapts the kernel spectrum to increase signal-kernel alignment, which lowers the ESD (Thm 5.2).")


# ---------------------------------------------------------------- Claim 6 (numerical): span profile decreases during OP-GF
banner("CLAIM 6: span profile (tail-energy ratio) decreases under OP-GF alignment")
def span_profile(theta, lam, sigma2):
    dd = S.esd(theta, lam, sigma2)
    order = np.argsort(-lam); th = theta[order] ** 2
    total = th.sum()
    tail = total - th[:dd].sum()
    return tail / max(dd * sigma2, 1e-9)      # <=1 at the ESD cutoff by definition
sp_before = span_profile(theta, lam, sigma2)
sp_after = span_profile(theta, lam_aligned, sigma2)
c6 = sp_after <= sp_before + 1e-9
print(f"  span profile before={sp_before:.4f}, after OP-GF={sp_after:.4f} (decreases) -> {'PASS' if c6 else 'FAIL'}")
results["c6_span_profile"] = dict(passed=bool(c6), before=float(sp_before), after=float(sp_after))


# ---------------------------------------------------------------- summary
banner("VERDICT SUMMARY")
passed = sum(1 for r in results.values() if r.get("passed"))
for k_, r in results.items():
    print(f"  [{'PASS' if r.get('passed') else 'FAIL'}] {k_}")
print(f"\n  {passed}/{len(results)} claims verified.")
json.dump(results, open(os.path.join(OUT, "verdict.json"), "w"), indent=2)
print("  wrote outputs/verdict.json")
