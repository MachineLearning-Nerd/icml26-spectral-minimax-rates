# Claim 2 - Proposition 3.2 oracle-PC sandwich

## Canonical outcome

**VERIFIED in deterministic constructions and randomized finite cases.**

## Anchored claim

Proposition 3.2 bounds oracle principal-component risk by the effective signal dimension `d†`:

```text
(d† - 1) sigma² <= oracle-PC risk <= 2 d† sigma².
```

## Predeclared test, metric, and acceptance rule

For each independently generated spectrum/signal/noise instance, enumerate every PC truncation, calculate the exact oracle risk, independently compute `d†`, and require both inequalities to hold within numerical tolerance. Exact constructed targets additionally require recovered ESD values `1, 2, 4, 8, 16`.

## Raw outcome and controls

- Randomized cases: `240/240` passed.
- Failures: `0`.
- Constructed ESD targets: `1, 2, 4, 8, 16`.
- Recovered values: exact for all five targets.
- Implementation control: oracle risk is independently enumerated over all truncations rather than copied from either side of the bound.

The same run also verified Proposition 3.7's span-profile monotonicity, generalized inversion, trade-off dominance, and profile dominance properties.

## Exact reproducibility

Run `uv run python repro/src/verify_spectral.py`; inspect keys `P3.2` and `P3.7` in [`outputs/v4/verdict_v4.json`](https://github.com/MachineLearning-Nerd/icml26-repro-4HrWo5x7YF-spectral-minimax/blob/agent/fix-all-v4-claims/outputs/v4/verdict_v4.json).
