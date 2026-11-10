AI disclosure: ChatGPT/Codex assisted implementation, calculations, validation and drafting. This is an AI-assisted draft; Linda must review the analysis and own the final decision before submission.

Education, not investment advice.

# Apex Endowment — reject live adoption
**Committee ask:** reject deployment of this allocation process for live assets; authorize research and policy clarification only. Proposed live allocation range: **0–0%**, with no live rebalancing authorization. Analysis date: November 10, 2026.

## Mandate and design
Apex has $50 million initially, a CPI + 4.5% net annualized objective over rolling ten-year periods, a $1.5 million cash/Treasury payout buffer, long-only exposure and a 5% single-issuer limit. The reference benchmark is 70% MSCI World / 30% Bloomberg Aggregate. Planning inflation of 2.5% produces a 7% nominal net screening hurdle; annual operating/custody fees are assumed at 0.25%. Neither is a current observed fact or approved fee quote.

The app compares equal weight and a transparent 70/30 VT/BND proxy with the lowest-volatility feasible portfolio on a five-percentage-point grid. It uses 60 monthly arithmetic returns and covariance; a prospective snapshot momentum signal sets an equity ceiling. Minimum SGOV is 3%; the grid effectively requires at least 5%. Treasury/fund issuer exemptions and holdings look-through are unresolved. No full mandate pass or client approval is claimed. Ten-year performance cannot be established from five years of data.

## Evidence
| Scenario | SGOV / BND / VT | Net arithmetic estimate | Annual volatility |
|---|---|---:|---:|
| 60 months | 55 / 0 / 45 | 7.15% | 6.77% |
| VT estimate minus 1 point | 50 / 0 / 50 | 7.06% | 7.51% |
| 36 months | 80 / 0 / 20 | 7.35% | 2.37% |
| Annual fees 1% | 45 / 0 / 55 | 7.21% | 8.25% |
| Equity cap 30% | No feasible mix | — | — |

The base buffer is $27.5 million. A 25-point window-driven weight change exceeds the proposed 10-point stability threshold, so adoption stops. Lowering an equity estimate increases required equity to meet an unchanged return target; this is a constraint response, not evidence that equity became more attractive. The illustrative starting inventory implies 52% one-way turnover for the base allocation. Actual inventory and trading costs are missing; no Apex turnover cap was supplied.

## Monitoring and reversal
Before reconsideration, require approved issuer treatment or validated look-through holdings; a client-approved risk measure and limit; authenticated, freshly archived data; exact benchmark total returns; forward-looking estimate justification; and an independent clean run. Re-run estimates, windows, costs, reserve floors and signal branches. Reconsider only if no material case is infeasible and the largest weight shift is at most 10 points, without lowering the return hurdle to manufacture feasibility. These are necessary conditions, not automatic approval.

Stop execution for stale data over 45 days, failed data checks, deficient buffer, issuer breach or absent authority. Monitor quarterly payouts, current NAV and reserve dollars; a fixed 3% of initial assets does not prove 3% of future NAV. No maximum-loss guarantee, historical alpha or ten-year target achievement is asserted.

Sources: [original mandate](https://github.com/llindali/lab13/blob/main/lab13.md), [Lab 15 inputs](https://github.com/llindali/lab15/tree/10f8ffdb7936a8255c368533e576ebd257de4a62), `docs/data-card.md`, `visible_output.json`.
