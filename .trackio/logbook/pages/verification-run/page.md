# Verification run

```bash
uv run python repro/src/verify_spectral.py
```

- Recorded OpenResearch run: `4a067f01-3c6a-4f55-a8c1-8388cb364dc3`
- Commit evaluated: `1680125`
- Environment: CPython 3.12.11, NumPy 2.5.1, local CPU
- Duration: 1 minute 50 seconds
- Exit code: 0

```text
[PASS] P3.2
[PASS] P3.7
[PASS] T3.3
[PASS] T4.3
[PASS] T5.2
[PASS] F1
[PASS] F2
[PASS] PB.2-TB.3-F3
[PASS] PC.4-TC.7-C.8-F4
[PASS] D1-D2-F5
[PASS] I.6
SUMMARY passed=11 total=11
PUBLICATION_GATE=PASS
```

The deterministic unit suite separately passed `7/7` tests. Claim 6 additionally passed its paper-scale strict endpoint rule with paired confidence intervals below zero at two independent seeds.
