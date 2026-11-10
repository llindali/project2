# Validation and AI use — Project 2
Analysis date: November 10, 2026. All work below is AI-assisted unless explicitly marked otherwise.

## Source boundary
Mandate: Apex section of Lab 13, not Meridian's training mandate. Frozen prices: original Lab 15 tree `10f8ffdb7936a8255c368533e576ebd257de4a62`; copied without numeric changes. See data card for custody, retrieval boundary and revision limitations. No live data or independent price authentication was performed. Prospective signal availability is November 10, not the observation month-end. Earliest proposed execution November 12. Recheck freshness before any later use.

## Modeling decisions
Annual arithmetic mean = monthly mean times 12; covariance = sample monthly covariance times 12. Independent-month scaling is assumed. Fees subtract 25bps annually from each asset mean. Target = 2.5% planning inflation + 4.5% real objective. The 5-point exhaustive grid minimizes estimated annual volatility subject to net mean >=7%, SGOV >=3%, nonnegative fully invested weights and signal equity cap. No continuous optimality is claimed. Estimated volatility is reported but no committee-approved maximum has been supplied.

SGOV and diversified funds are provisionally admitted for research; no issuer exemption is declared approved. Full issuer compliance is UNVERIFIED, not PASS. Buffer is measured against initial $50M; actual NAV/inventory/trading costs and rolling ten-year performance are unverified. VT/BND differs from the mandated indexes. The fixed analyst universe can create selection bias.

## Executed results
`python engine.py` produced `visible_output.json`: base 55/0/45, net estimate 7.1461375%, volatility 6.7698422%. Independent Lab 15 result reproduced. Window stress changes a weight by 25 points; the 30% equity ceiling is infeasible. Fees, reserve and combined stresses are included. These ordinary AI-assisted runs do **not** satisfy the Locked Changed-Input Record.

Test and application verification details are recorded after execution below. No partner meeting or student cold run is claimed.

## Material AI uses
| Tool / model as exposed | Date | Use | Disposition / check |
|---|---|---|---|
| ChatGPT / Codex; exact underlying model version not exposed | 2026-11-10 | Requirements review, implementation and tests | Compared current course requirements to actual Lab 13 mandate and Lab 15 inputs |
| ChatGPT / Codex | 2026-11-10 | Estimates and sensitivity analysis | Executed engine; independent arithmetic and constraint tests; reject adoption on instability |
| ChatGPT / Codex | 2026-11-10 | Memo, README, video outlines and practice objections | AI-assisted drafts reviewed by Linda; she confirmed understanding and ownership of the rejection recommendation; no partner event claimed |

## Locked Changed-Input Record — AI-off prediction (student-attested); result recorded
The original student-supplied prediction below is preserved verbatim. The prediction was committed before the test executed in this session. Linda confirms that she wrote the pre-run prediction with AI closed. This is a student attestation, not independent verification of the writing conditions. Pre-commit AI discussion supplied model-fact corrections and procedural feedback and remains disclosed. Post-run execution and diagnosis below are AI-assisted; Linda confirmed that she reviewed and understood the analysis and agreed with the rejection recommendation on November 10, 2026.

1. Select one previously unrun input change, with old/new values and units. Record the current baseline input set and output.
2. With AI closed, write your expected direction for weights, net estimate, volatility and recommendation, plus why. Commit and push this prediction **before** running that change.
3. Preserve the prediction commit URL. Only then run the changed input through the app or engine.
4. Save actual outputs and their commit URL; compare expected and actual directions, explain divergence and state the decision effect.

Fill before the run:
- **Analyst:** Linda Li
- **Date:** 11/10/2026
- **Input Changed:** VT return-estimate adjustment
- **Original Value:** 0.0% (0 percentage points)
- **New Value:** +1.5% (+1.5 percentage points / +150 bps)

#### Pre-Run Prediction:
- **Allocation:** The allocation will remain unchanged at **55% SGOV / 0% BND / 45% VT**. SGOV remains anchored at the 55% minimum reserve floor, BND remains unallocated (0%) due to lower risk-adjusted return relative to VT and cash, and VT stays at its 45% allowable non-reserve ceiling.
- **Return Estimate:** Expected annualized portfolio return will increase by approximately **+0.675%** (derived from the 45% VT weighting multiplied by the +1.50% return bump: $0.45 \times 1.5\% = +0.675\%$).
- **Volatility:** Annualized portfolio volatility will remain **unchanged** because adjusting the forward return estimate does not change the historical asset covariance matrix or historical standard deviations used by the model.
- **Reject Live Adoption Decision:** **Remains "Reject live adoption" (no change)**. While the nominal return increases, manually boosting the equity return estimate without fundamental historical covariance justification fails the robustness/governance checks, keeping live adoption rejected.

### Post-run evidence and comparison — AI-assisted
- **Prediction commit:** [339e59e2524ca17a64596ea05e2615c6b71a38e3](https://github.com/llindali/project2/commit/339e59e2524ca17a64596ea05e2615c6b71a38e3), committed November 10, 2026 at 1:03:48 p.m. America/Indianapolis.
- **Prediction snapshot:** [original file, unchanged](https://github.com/llindali/project2/blob/339e59e2524ca17a64596ea05e2615c6b71a38e3/docs/validation-and-ai-use.md). This contains the earlier unchanged-weights prediction, not the later 70%-VT draft discussed in chat.
- **Input change:** `equity_shift=0` to `equity_shift=0.015`: +1.5 annual percentage points, or +150 basis points, to VT only. This is additive, not a 1.5% proportional increase.
- **Other inputs unchanged:** 60 months, annual fee 0.25%, reserve floor 3%, signal equity ceiling 70%, nominal net-return hurdle 7%, initial NAV $50M, five-point allocation grid. The same frozen prices and covariance are used.
- **Exact reproduction command**, from the repository root:

```bash
python -c "import json; from engine import run; print(json.dumps({'baseline':run(),'changed':run(equity_shift=.015)}, indent=2))"
```

- **Immutable output:** [baseline and changed results](https://github.com/llindali/project2/blob/c9cbbda8c57cd27f37ee927abfcde2f55460e3ec/results/locked-change-output.json).
- **Result commit:** [c9cbbda8c57cd27f37ee927abfcde2f55460e3ec](https://github.com/llindali/project2/commit/c9cbbda8c57cd27f37ee927abfcde2f55460e3ec).

| Decision number | Baseline | Changed | Actual change |
|---|---:|---:|---:|
| SGOV | 55% | 60% | +5 percentage points |
| BND | 0% | 0% | None |
| VT | 45% | 40% | -5 percentage points |
| Net annual arithmetic return estimate | 7.1461375% | 7.3371295% | +0.1909920 percentage points |
| Annualized volatility estimate | 6.7698422% | 6.0304935% | -0.7393487 percentage points |
| Reserve dollars at initial NAV | $27.5M | $30.0M | +$2.5M |
| Live allocation range | 0–0% | 0–0% | None |

**Prediction comparison:** unchanged weights did not occur; return increased in the predicted direction but by approximately 0.191 points rather than 0.675; volatility decreased rather than remaining unchanged. BND stayed at zero and the rejection remained unchanged.

**Failure diagnosis:** the committed explanation mistakenly treated 55% SGOV and 45% VT as constraints. They are baseline outputs; the actual reserve floor is 3% (effectively 5% on this grid) and the signal equity cap is 70%. The objective minimizes volatility subject to meeting a 7% net-return hurdle; it does not maximize return or equity allocation. Raising VT's return estimate permits a lower-equity feasible mix with lower volatility. The 0.675-point calculation is correct only at the original fixed weights. Covariance stays unchanged, but portfolio volatility changes because weights change.

**Decision effect:** reject live adoption remains the committee ask. The changed portfolio passes the modeled numerical screens and shifts weights by only five points, below the proposed greater-than-ten-point stop threshold. It remains UNVERIFIED for issuer treatment, approved risk policy and the ten-year objective. Existing window instability and validation gaps remain unresolved. The sensitivity itself is not evidence of misconduct or a new governance breach.

**Verification:** independently recomputed changed return as weights times asset means and changed volatility as the square root of weights-transpose times covariance times weights; checked all modeled numerical constraints and the 7% estimated-return hurdle. The engine and price file were not modified.

**Student review and ownership — confirmed November 10, 2026:** Linda confirms that she reviewed and understands the analysis and agrees with the decision to reject live adoption. She accepts ownership of the final analysis and decision. She also attests that the pre-run prediction was written with AI closed; earlier AI discussion and the AI-assisted post-run work remain disclosed. The original prediction and its commit history are unchanged.

## Limits and outstanding checks
Five years cannot establish ten-year outcomes. No exact-index tracking error, historical vintage backtest, client-approved issuer policy, calibrated forward forecasts, live trade authority or independent student cold run is supplied. A zero live allocation is the committee ask; this is a research app with an honest rejection, not an approved trading system.

## Verification performed in this build
- `python -m unittest discover -s tests -v`: **5 tests passed**, including direct NumPy mean/covariance and portfolio-volatility checks, baseline failures, both signal branches, infeasibility, stress stop/constraint checks, and Streamlit AppTest default plus 36-month control path.
- Initial environment failure: Streamlit was missing; installing the specified version resolved it. An initial test assertion searched a truncated DataFrame display; reading the SGOV column directly corrected the test. No financial result changed.
- Streamlit AppTest executed the UI successfully; this is an automated application run, not a visual browser inspection or an independent partner cold run. Dependency installation succeeded in the existing environment; a fresh virtual-environment installation is still an independent cold-run task.
- The live-deployment stop remains active regardless of numerical feasibility. The sample contains 60 returns, too few to validate a rolling ten-year target.
