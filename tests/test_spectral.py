from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "repro" / "src"))
import spectral as s


def test_constructed_signal_has_exact_esd() -> None:
    lam = np.linspace(2.0, 0.1, 40)
    for k in (1, 2, 7, 20, 40):
        theta = s.construct_esd_signal(40, k, 0.3, seed=k)
        assert s.esd(theta, lam, 0.3) == k


def test_pc_sandwich_randomized() -> None:
    rng = np.random.default_rng(0)
    for _ in range(100):
        theta = rng.normal(size=30)
        lam = rng.uniform(0.01, 2.0, size=30)
        sigma2 = float(10 ** rng.uniform(-3, 1))
        dd = s.esd(theta, lam, sigma2)
        risk = s.oracle_pc_risk(theta, lam, sigma2)
        assert (dd - 1) * sigma2 - 1e-10 <= risk
        assert risk <= 2 * dd * sigma2 + 1e-10


def test_span_profile_is_the_esd_function() -> None:
    theta = np.asarray([4.0, 0.0, 2.0, 0.5])
    lam = np.asarray([4.0, 3.0, 2.0, 1.0])
    taus = np.logspace(-4, 2, 50)
    profile = s.span_profile(theta, lam, taus)
    assert np.all(np.diff(profile) <= 0)
    assert np.array_equal(profile, [s.esd(theta, lam, tau) for tau in taus])


def test_opgf_runs_actual_gradient_updates() -> None:
    theta, lam = s.misaligned_sequence(
        100, q=2, sparsity=8, signal_decay=2.5, eigen_decay=1.0
    )
    trace = s.opgf(
        theta,
        lam,
        depth=0,
        b0=1.0,
        step_size=0.02,
        steps=100,
        checkpoints=[0, 100],
    )
    assert trace.learned_spectra.shape == (2, 100)
    assert not np.allclose(trace.learned_spectra[0], trace.learned_spectra[-1])
    assert np.sum((trace.estimates[-1] - theta) ** 2) < np.sum(theta**2)


def test_opgf_depth_update_includes_chain_rule_factor() -> None:
    z = np.asarray([0.7])
    lam = np.asarray([0.81])
    depth, b0, step_size = 2, 0.6, 0.03
    a = np.sqrt(lam)
    beta = np.zeros_like(a)
    b = np.full_like(a, b0)
    for _ in range(2):
        estimate = a * b**depth * beta
        residual = estimate - z
        grad_a = b**depth * beta * residual
        grad_beta = a * b**depth * residual
        grad_b = depth * a * b ** (depth - 1) * beta * residual
        a, beta, b = (
            a - step_size * grad_a,
            beta - step_size * grad_beta,
            b - step_size * grad_b,
        )
    expected_spectrum = (a * b**depth) ** 2
    trace = s.opgf(
        z,
        lam,
        depth=depth,
        b0=b0,
        step_size=step_size,
        steps=2,
        checkpoints=[2],
    )
    assert np.allclose(trace.learned_spectra[-1], expected_spectrum)


def test_batched_opgf_matches_independent_runs() -> None:
    observations = np.asarray([[0.7, -0.2], [0.1, 0.5]])
    lam = np.asarray([0.81, 0.36])
    kwargs = {
        "depth": 3,
        "b0": 0.8,
        "step_size": 0.01,
        "steps": 12,
        "checkpoints": [0, 5, 12],
    }
    batched = s.opgf_batched(observations, lam, **kwargs)
    for rep, observation in enumerate(observations):
        independent = s.opgf(observation, lam, **kwargs)
        assert np.allclose(batched.estimates[:, rep], independent.estimates)
        assert np.allclose(batched.learned_spectra[:, rep], independent.learned_spectra)


def test_rademacher_bayes_lower_bound_is_constant_order() -> None:
    sigma2 = 0.7
    risk = s.rademacher_bayes_risk(np.sqrt(sigma2), sigma2)
    assert 0.05 * sigma2 < risk < sigma2
