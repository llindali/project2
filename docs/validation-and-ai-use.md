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
| ChatGPT / Codex | 2026-11-10 | Memo, README, video outlines and practice objections | AI drafts; student review still required; no fabricated personal reflection or partner event |

## Locked Changed-Input Record — PENDING, not completed
This must contain Linda's human-authored prediction with AI closed. Do not copy an AI prediction or retrofit this record to existing outputs.

1. Select one previously unrun input change, with old/new values and units. Record the current baseline input set and output.
2. With AI closed, write your expected direction for weights, net estimate, volatility and recommendation, plus why. Commit and push this prediction **before** running that change.
3. Preserve the prediction commit URL. Only then run the changed input through the app or engine.
4. Save actual outputs and their commit URL; compare expected and actual directions, explain divergence and state the decision effect.

Fill before the run:
- Author and time:
- Baseline commit:
- Input / old / new / units:
- AI-off prediction and reasoning (student only):
- Prediction commit URL:

Fill after the run:
- Exact command or app settings:
- Actual weights / return / risk / verdict:
- Result commit URL:
- Prediction comparison and diagnosis:
- Recommendation effect:

## Limits and outstanding checks
Five years cannot establish ten-year outcomes. No exact-index tracking error, historical vintage backtest, client-approved issuer policy, calibrated forward forecasts, live trade authority or independent student cold run is supplied. A zero live allocation is the committee ask; this is a research app with an honest rejection, not an approved trading system.

## Verification performed in this build
- `python -m unittest discover -s tests -v`: **5 tests passed**, including direct NumPy mean/covariance and portfolio-volatility checks, baseline failures, both signal branches, infeasibility, stress stop/constraint checks, and Streamlit AppTest default plus 36-month control path.
- Initial environment failure: Streamlit was missing; installing the specified version resolved it. An initial test assertion searched a truncated DataFrame display; reading the SGOV column directly corrected the test. No financial result changed.
- Streamlit AppTest executed the UI successfully; this is an automated application run, not a visual browser inspection or an independent partner cold run. Dependency installation succeeded in the existing environment; a fresh virtual-environment installation is still an independent cold-run task.
- The live-deployment stop remains active regardless of numerical feasibility. The sample contains 60 returns, too few to validate a rolling ten-year target.
