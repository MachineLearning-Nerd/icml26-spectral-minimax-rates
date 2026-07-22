"""Numerical primitives for arXiv:2509.20294v4.

The functions in this module implement definitions and estimator risks directly.
They deliberately separate theorem statements from empirical evidence: an
experiment can validate identities, examples, and finite cases, but it cannot
prove an asymptotic minimax lower bound.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np


Array = np.ndarray


def _vectors(theta: Array, lam: Array) -> tuple[Array, Array]:
    theta = np.asarray(theta, dtype=float).reshape(-1)
    lam = np.asarray(lam, dtype=float).reshape(-1)
    if theta.size == 0 or theta.shape != lam.shape:
        raise ValueError("theta and lam must be non-empty vectors of equal length")
    if not np.all(np.isfinite(theta)) or not np.all(np.isfinite(lam)):
        raise ValueError("theta and lam must be finite")
    return theta, lam


def spectral_order(lam: Array) -> Array:
    """Decreasing spectral order with deterministic index tie-breaking."""
    lam = np.asarray(lam, dtype=float).reshape(-1)
    return np.lexsort((np.arange(lam.size), -lam))


def tail_energy(theta: Array, lam: Array) -> Array:
    """Return tail energy after k leading coordinates for k=1,...,d."""
    theta, lam = _vectors(theta, lam)
    sq = theta[spectral_order(lam)] ** 2
    suffix = np.cumsum(sq[::-1])[::-1]
    return np.r_[suffix[1:], 0.0]


def tradeoff(theta: Array, lam: Array) -> Array:
    """H_{theta,lambda}(k) for k=1,...,d (Equation 9 in v4)."""
    tails = tail_energy(theta, lam)
    return tails / np.arange(1, tails.size + 1, dtype=float)


def esd(theta: Array, lam: Array, sigma2: float) -> int:
    """Definition 3.1: min k in [d] with H(k) <= sigma^2."""
    if not np.isfinite(sigma2) or sigma2 < 0:
        raise ValueError("sigma2 must be finite and non-negative")
    h = tradeoff(theta, lam)
    feasible = np.flatnonzero(h <= sigma2 + 32 * np.finfo(float).eps)
    return int(feasible[0] + 1) if feasible.size else int(h.size)


def span_profile(theta: Array, lam: Array, taus: Iterable[float]) -> Array:
    """Definition 3.6 evaluated on a noise-level grid."""
    return np.asarray([esd(theta, lam, float(tau)) for tau in taus], dtype=int)


def pc_risk_k(theta: Array, lam: Array, sigma2: float, k: int) -> float:
    """Population sequence-model risk of PC retaining k leading coordinates."""
    theta, lam = _vectors(theta, lam)
    if not 1 <= k <= theta.size:
        raise ValueError("k must lie in [1,d]")
    order = spectral_order(lam)
    return float(k * sigma2 + np.sum(theta[order[k:]] ** 2))


def oracle_pc_risk(theta: Array, lam: Array, sigma2: float) -> float:
    return min(pc_risk_k(theta, lam, sigma2, k) for k in range(1, len(theta) + 1))


def oracle_pc_k(theta: Array, lam: Array, sigma2: float) -> int:
    risks = [pc_risk_k(theta, lam, sigma2, k) for k in range(1, len(theta) + 1)]
    return int(np.argmin(risks) + 1)


def construct_esd_signal(d: int, k: int, sigma2: float, seed: int = 0) -> Array:
    """Construct a signal whose ESD is exactly k for decreasing spectra."""
    if not 1 <= k <= d:
        raise ValueError("k must lie in [1,d]")
    rng = np.random.default_rng(seed)
    theta = np.zeros(d)
    theta[:k] = np.sqrt((4.0 * k + 1.0) * sigma2) * rng.choice([-1.0, 1.0], k)
    if k < d:
        # Strictly below the k*sigma2 crossing avoids floating-point ambiguity.
        theta[k:] = np.sqrt(0.75 * k * sigma2 / (d - k))
    return theta


def rademacher_bayes_risk(amplitude: float, sigma2: float, quadrature: int = 100) -> float:
    """Scalar Bayes MSE for theta in {-a,+a} observed in N(theta,sigma2).

    This gives a valid minimax lower bound for any parameter class containing
    the corresponding hypercube. Gauss-Hermite quadrature makes the finite-case
    calculation deterministic.
    """
    if amplitude <= 0 or sigma2 <= 0:
        raise ValueError("amplitude and sigma2 must be positive")
    nodes, weights = np.polynomial.hermite.hermgauss(quadrature)
    noise = np.sqrt(2.0 * sigma2) * nodes
    z = amplitude + noise
    posterior_mean = amplitude * np.tanh(amplitude * z / sigma2)
    loss = (amplitude - posterior_mean) ** 2
    return float(np.dot(weights, loss) / np.sqrt(np.pi))


def ridge_risk(theta: Array, lam: Array, sigma2: float, nu: float) -> tuple[float, float, float]:
    theta, lam = _vectors(theta, lam)
    shrink = lam / (lam + nu)
    bias = float(np.sum(((1.0 - shrink) * theta) ** 2))
    variance = float(sigma2 * np.sum(shrink**2))
    return bias + variance, bias, variance


def ridge_variance_proxy(lam: Array, sigma2: float, k: int) -> float:
    lam = np.asarray(lam, dtype=float).reshape(-1)[spectral_order(lam)]
    if not 1 <= k <= lam.size:
        raise ValueError("k must lie in [1,d]")
    return float(sigma2 * (k + np.sum(lam[k:] ** 2) / lam[k - 1] ** 2))


def ridge_saturating_dimension(lam: Array, sigma2: float, c_r: float) -> int:
    lam = np.asarray(lam, dtype=float).reshape(-1)[spectral_order(lam)]
    answer = 0
    for k in range(1, lam.size + 1):
        n_tilde = np.sum(lam[k:] ** 2) / (k * lam[k - 1] ** 2)
        h_bar = lam[k - 1] ** 2 / (k * (1.0 + n_tilde))
        if c_r * h_bar > sigma2:
            answer = k
    return answer


@dataclass(frozen=True)
class OPGFTrace:
    checkpoints: Array
    estimates: Array
    learned_spectra: Array


def opgf(
    observations: Array,
    initial_lam: Array,
    *,
    depth: int,
    b0: float,
    step_size: float,
    steps: int,
    checkpoints: Iterable[int],
) -> OPGFTrace:
    """Discrete gradient descent approximation of Equation (12).

    The D identical b-layers remain identical under the symmetric initialization,
    so a single b vector is sufficient. Updates are simultaneous (plain GD).
    """
    z, lam = _vectors(observations, initial_lam)
    if depth < 0 or b0 <= 0 or step_size <= 0 or steps < 0:
        raise ValueError("invalid OP-GF configuration")
    wanted = np.asarray(sorted(set(int(s) for s in checkpoints)), dtype=int)
    if wanted.size == 0 or wanted[0] < 0 or wanted[-1] > steps:
        raise ValueError("checkpoints must lie in [0,steps]")

    a = np.sqrt(np.maximum(lam, 0.0))
    beta = np.zeros_like(a)
    b = np.full_like(a, b0)
    estimates: list[Array] = []
    spectra: list[Array] = []
    next_checkpoint = 0

    def record() -> None:
        scale = a if depth == 0 else a * b**depth
        estimates.append((scale * beta).copy())
        spectra.append((scale**2).copy())

    if wanted[0] == 0:
        record()
        next_checkpoint = 1

    for step in range(1, steps + 1):
        b_power = np.ones_like(b) if depth == 0 else b**depth
        estimate = a * b_power * beta
        residual = estimate - z
        grad_a = b_power * beta * residual
        grad_beta = a * b_power * residual
        if depth:
            grad_b = depth * a * (b ** (depth - 1)) * beta * residual
        a_new = a - step_size * grad_a
        beta_new = beta - step_size * grad_beta
        if depth:
            b = b - step_size * grad_b
        a, beta = a_new, beta_new
        if not np.all(np.isfinite(a)) or not np.all(np.isfinite(beta)) or not np.all(np.isfinite(b)):
            raise FloatingPointError("OP-GF diverged; reduce step_size")
        if next_checkpoint < wanted.size and step == wanted[next_checkpoint]:
            record()
            next_checkpoint += 1

    return OPGFTrace(wanted, np.asarray(estimates), np.asarray(spectra))


def opgf_batched(
    observations: Array,
    initial_lam: Array,
    *,
    depth: int,
    b0: float,
    step_size: float,
    steps: int,
    checkpoints: Iterable[int],
) -> OPGFTrace:
    """Vectorized OP-GF for independent observations sharing one spectrum.

    This is algebraically identical to :func:`opgf`; the leading axis indexes
    Monte Carlo replications. Vectorization makes the paper-scale ``d=5000``,
    20-replication depth audit practical on CPU without changing the dynamics.
    """
    z = np.asarray(observations, dtype=float)
    lam = np.asarray(initial_lam, dtype=float).reshape(-1)
    if z.ndim != 2 or z.shape[1] != lam.size or z.shape[0] == 0:
        raise ValueError("observations must have shape (replications, dimension)")
    if not np.all(np.isfinite(z)) or not np.all(np.isfinite(lam)):
        raise ValueError("observations and initial_lam must be finite")
    if depth < 0 or b0 <= 0 or step_size <= 0 or steps < 0:
        raise ValueError("invalid OP-GF configuration")
    wanted = np.asarray(sorted(set(int(s) for s in checkpoints)), dtype=int)
    if wanted.size == 0 or wanted[0] < 0 or wanted[-1] > steps:
        raise ValueError("checkpoints must lie in [0,steps]")

    a = np.broadcast_to(np.sqrt(np.maximum(lam, 0.0)), z.shape).copy()
    beta = np.zeros_like(a)
    b = np.full_like(a, b0) if depth else None
    estimates: list[Array] = []
    spectra: list[Array] = []
    next_checkpoint = 0

    def powers() -> tuple[float | Array, float | Array]:
        if depth == 0:
            return 1.0, 0.0
        if depth == 1:
            return b, 1.0
        if depth == 3:
            b_squared = b * b
            return b_squared * b, b_squared
        return b**depth, b ** (depth - 1)

    def record() -> None:
        factor, _ = powers()
        scale = a * factor
        estimates.append((scale * beta).copy())
        spectra.append((scale**2).copy())

    if wanted[0] == 0:
        record()
        next_checkpoint = 1

    for step in range(1, steps + 1):
        factor, previous_power = powers()
        scale = a * factor
        residual = scale * beta
        residual -= z
        common = beta * residual
        if depth:
            grad_b = depth * a * previous_power * common
            grad_a = factor * common
        else:
            grad_a = common
        grad_beta = scale * residual
        a -= step_size * grad_a
        beta -= step_size * grad_beta
        if depth:
            b -= step_size * grad_b
        if step % 500 == 0 or step == steps:
            if not np.all(np.isfinite(a)) or not np.all(np.isfinite(beta)) or (
                depth and not np.all(np.isfinite(b))
            ):
                raise FloatingPointError("OP-GF diverged; reduce step_size")
        if next_checkpoint < wanted.size and step == wanted[next_checkpoint]:
            record()
            next_checkpoint += 1

    return OPGFTrace(wanted, np.asarray(estimates), np.asarray(spectra))


def misaligned_sequence(
    d: int,
    *,
    q: float,
    sparsity: int,
    signal_decay: float,
    eigen_decay: float,
    amplitude: float = 1.0,
) -> tuple[Array, Array]:
    """Section 6 data construction with ell(j)=floor(j^q), using 1-based j."""
    lam = np.arange(1, d + 1, dtype=float) ** (-eigen_decay)
    theta = np.zeros(d)
    for j in range(1, sparsity + 1):
        index = int(np.floor(j**q)) - 1
        if index >= d:
            raise ValueError("d must be at least floor(J^q)")
        theta[index] = amplitude * j ** (-(signal_decay + 1.0) / 2.0)
    return theta, lam
