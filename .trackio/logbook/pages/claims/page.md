# Version-pinned claim ledger

| ID | Anchor | Evidence type | Result |
| --- | --- | --- | --- |
| P3.2 | Proposition 3.2, oracle-PC ESD sandwich | randomized finite identity | PASS |
| T3.3 | Theorem 3.3, sequence minimax rate | proof audit + contained hypercube lower/PC upper | PASS |
| P3.7 | Proposition 3.7, profile monotonicity/inversion/dominance | property tests | PASS |
| T4.3 | Theorem 4.3, quota-sequence minimax rate | condition audit + finite lower/upper curves | PASS |
| T5.2 | Theorem 5.2, conditional OP-GF endpoint reduction | assumption and proof-scope audit | PASS |
| F1 | Figure 1, OP-GF span-profile evolution | stated-scale CPU experiment | PASS |
| F2 | Figure 2, depth/ESD/error dynamics | 20-replication clean-room experiment | PASS |
| PB.2 | Proposition B.2, fixed-design PCR sandwich | SVD/PCR experiment and identity check | PASS |
| TB.3 | Theorem B.3, fixed-design minimax rate | reduction and finite hypercube audit | PASS |
| F3 | Figure 3, fixed-design alignment | `n=300`, `p=400` experiment | PASS |
| PC.4 | Proposition C.4, KPCPE bounds | random-design Monte Carlo bound check | PASS |
| TC.7-C.8 | Theorems C.7/C.8, RKHS minimax rates | assumptions + finite packing/upper audit | PASS |
| F4 | Figure 4, RKHS ESD/risk tracking | `n=400`, `J=800`, 10 replications | PASS |
| D1-D2 | Appendix D/Figure 5, learned eigensystem alignment | equal-spectrum control + scale-reduced path | PASS |
| I.6 | Theorem I.6, ridge saturation | direct finite bound evaluation | PASS |

“PASS” for a theorem means its assumptions and proof scope were audited and its finite consequences were checked. It does **not** mean a numerical script proved an asymptotic minimax theorem.
