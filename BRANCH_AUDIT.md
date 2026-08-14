# Branch audit

## Target policy

- Default branch: main
- Public branch count: 3
- Legacy refs to remove: master and agent/fix-all-v4-claims
- Purpose prefixes: baseline/* and release/*
- Reachable commit identity: MachineLearning-Nerd
  <MachineLearning-Nerd@users.noreply.github.com>

## Mapping

| Final branch | Historical source | Purpose |
| --- | --- | --- |
| main | master plus the corrected v4 release | Canonical publication surface and audit documentation |
| baseline/proxy-checks | master | Original six proxy checks, retained for historical comparison |
| release/v4-corrected-claims | agent/fix-all-v4-claims | Corrected v4 ledger, experiments, controls, and evidence |

The historical names are retained in this table for provenance only. The
GitHub migration is complete: the final remote has exactly these three
branches, default main, no master or agent/* refs, and only MachineLearning-Nerd
as a reachable author/committer identity.

Verified on 2026-08-14 with git ls-remote, the GitHub repository API, local
identity scans, published README/gate reads, and a clean worktree.
