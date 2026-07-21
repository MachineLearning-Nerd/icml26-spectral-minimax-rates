"""Clean-room implementation of the Effective Span Dimension (ESD) framework from
"Alignment-Sensitive Minimax Rates for Spectral Algorithms" (arXiv 2509.20294). numpy, CPU.

Sequence model: z_j = theta*_j + xi_j,  xi_j mean 0 var sigma^2.
ESD (Def 3.1): d†(sigma^2; theta*, lam) = min{k : (1/k) sum_{i>k} (theta*_{pi_i})^2 <= sigma^2},
  pi orders indices by DECREASING lambda.
Spectral estimators: theta_hat_j = (1 - psi_nu(lam_j)) z_j.
  PC:  psi(lam) = 1{lam < nu}   -> keep lam>=nu, drop lam<nu.
  GF:  psi(lam) = exp(-lam/nu)  -> shrink by exp(-lam/nu).
Oracle PC risk (Prop 3.2): (d†-1) sigma^2 <= R*_PC <= 2 d† sigma^2.
"""
from __future__ import annotations
import numpy as np


def esd(theta, lam, sigma2):
    """Effective Span Dimension: smallest k with tail-energy/k <= sigma^2 (ordering by decreasing lam)."""
    order = np.argsort(-lam)                 # decreasing lambda
    th = np.abs(theta[order]) ** 2
    d = len(theta)
    csum = np.concatenate([[0.0], np.cumsum(th)])      # csum[k] = sum of top-k
    total = csum[-1]
    for k in range(1, d + 1):
        tail = total - csum[k]                         # sum_{i>k} theta_{pi_i}^2
        if k * sigma2 >= tail - 1e-15:
            return k
    return d


def pc_risk(theta, lam, sigma2, nu):
    """Risk of PC estimator with threshold nu: kept(lam>=nu) contribute sigma^2 var; dropped contribute bias theta^2."""
    kept = lam >= nu
    return float(sigma2 * kept.sum() + np.sum(theta[~kept] ** 2))


def oracle_pc_risk(theta, lam, sigma2):
    """R*_PC = min over nu of pc_risk. (Optimal nu is one of the lambda values.)"""
    best = float("inf")
    for nu in np.unique(np.concatenate([lam, [lam.min() - 1, lam.max() + 1]])):
        best = min(best, pc_risk(theta, lam, sigma2, nu))
    return best


def gf_filter(theta_obs, lam, nu):
    """Gradient-flow spectral estimator: theta_hat_j = (1 - exp(-lam_j/nu)) z_j."""
    return (1 - np.exp(-lam / nu)) * theta_obs


def make_signal(d, K, sigma2, seed=0, tail_energy=None):
    """Construct a signal with ESD exactly ~K: top-K entries large, tail summing to ~K*sigma^2."""
    rng = np.random.default_rng(seed)
    theta = np.zeros(d)
    theta[:K] = 5.0 * np.sqrt(sigma2) * (1 + rng.standard_normal(K) * 0.1)   # top-K strong
    tail = tail_energy if tail_energy is not None else K * sigma2
    theta[K:] = np.sqrt(tail / max(d - K, 1)) * np.ones(d - K)               # tail sums to K*sigma^2
    return theta
