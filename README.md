AI disclosure: I used ChatGPT/Codex to assist with implementation, calculations, validation and drafting. I reviewed and understand the analysis, and the final decision to reject live adoption is mine.

Education, not investment advice.

# Project 2 — Apex Endowment investment management app
**Recommendation: reject live adoption; live allocation range 0–0%.** Research allocation: 55% SGOV / 0% BND / 45% VT, subject to unresolved policy and evidence gaps. This repository contains the Project 2 application and submission drafts, building on Lab 15.

## Start here
Use Python 3.11 or 3.12, from this repository:

```bash
git clone https://github.com/llindali/project2.git
cd project2
python -m venv .venv
```

Activate with `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows), then:

```bash
python -m pip install -r requirements.txt
python engine.py
python -m streamlit run app.py
```

Open the local URL printed by Streamlit (normally http://localhost:8501). No account, API key or network data request is needed at runtime. Compare the three portfolio rows, inspect mandate verdicts, adjust window/fees/returns/reserve, inspect stresses, and download the current results. Run tests with `python -m unittest discover -s tests -v`.

## Decision without running code
| Run | SGOV / BND / VT | Net estimate | Volatility | Stop |
|---|---|---:|---:|---|
| Base | 55 / 0 / 45 | 7.15% | 6.77% | Adoption blocked by unresolved policy |
| Last 36 months | 80 / 0 / 20 | 7.35% | 2.37% | Yes: 25-point shift |
| VT minus 1 point | 50 / 0 / 50 | 7.06% | 7.51% | No new stability breach |
| Equity ceiling 30% | Infeasible | — | — | Yes |

See [full executed output](visible_output.json). Arithmetic historical estimates are not forecasts. The equal-weight baseline misses the estimated net-return hurdle; the unbuffered 70/30 proxy fails the reserve rule. All portfolios remain unverified against unresolved issuer treatment, approved risk policy and the ten-year objective.

## Walkthrough
1. [Mandate and committee decision](docs/decision-memo.md): use the Apex mandate actually written in Lab 13, not Meridian's training constraints.
2. [Data and signal](docs/data-card.md): prospective snapshot momentum cap; no historical-vintage claim.
3. `engine.py`: validate monthly prices, estimate returns/covariance, evaluate baselines, exhaust the allocation grid, stress the result.
4. `app.py`: operate the controls, compare rule verdicts and inspect stop conditions.
5. [Validation and AI disclosure](docs/validation-and-ai-use.md): executed checks, limitations and the committed prediction with its post-run comparison.
6. [Video recording outlines](docs/video-outlines.md) and [submission manifest](docs/submission-manifest.md).

## What remains before submission
- Partner-confirmed clean cold check, supplied by Linda, is recorded in the validation file. The partner's name, elapsed time and a specific control-change observation remain unreported for Lab 20.
- Three recorded YouTube videos with corrected transcripts; replace pending manifest entries with real URLs/durations/timestamps. Draft outlines are not transcripts.
- Confirm Brightspace's enforced due date; attach the same two required Markdown documents and complete manifest. Project 2 has no Edition A or B.

Project 2 is maintained in this standalone repository. Lab 15 is retained as source provenance.

## Locked changed-input result
After the committed prediction, a VT +1.5-percentage-point adjustment changed the optimized SGOV/BND/VT mix from 55/0/45 to **60/0/40**. Net return estimate increased from **7.15% to 7.34%**, and annual volatility fell from **6.77% to 6.03%**. The model could meet the same return hurdle with less equity. See the [preserved prediction and diagnosis](docs/validation-and-ai-use.md) and [full before/after output](results/locked-change-output.json). Live adoption remains rejected.
