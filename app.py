import json
import streamlit as st
import pandas as pd
from engine import run, stress_suite, ROOT

st.set_page_config(page_title='Apex | Investment Committee', layout='wide')
st.title('Apex Endowment — investment process review')
st.caption('ChatGPT/Codex assisted code, validation and drafting. Student review and ownership of the final decision are required. Education, not investment advice.')
st.error('REJECT live adoption. Proposed live allocation: 0–0%. Research testing only.')
st.write('Apex mandate: $50M initial assets; CPI + 4.5% net over rolling ten years; $1.5M cash/Treasury buffer; long-only; 5% issuer cap; 70% MSCI World / 30% Bloomberg Aggregate benchmark.')
st.warning('Issuer exemptions/look-through and risk budget await committee approval. No portfolio receives a full mandate PASS. VT/BND is a tradable benchmark proxy, not the exact mandated indexes.')
months = st.sidebar.selectbox('Estimation window (months)', [60,36])
fee = st.sidebar.slider('Annual operating/custody fee (%)', 0., 2., .25, .25)/100
shift = st.sidebar.slider('VT return estimate change (percentage points)', -5., 2., 0., .5)/100
reserve = st.sidebar.slider('Minimum reserve (%)', 3., 30., 3., 1.)/100
result = run(months=months, fee=fee, equity_shift=shift, reserve=reserve)
st.subheader('Compare portfolios and mandate verdicts')
rows=[]
items = dict(result['baselines'])
if result['portfolio']:
    items['Constrained minimum volatility (5-point grid)'] = result['portfolio']
else:
    st.error('No feasible constrained allocation. Stop; do not lower the target to force a result.')
for name, x in items.items():
    rows.append({'Portfolio':name, **{t:f'{w:.1%}' for t,w in x['weights'].items()},
                 'Net arithmetic estimate':f"{x['net_return_estimate']:.2%}",
                 'Annual volatility':f"{x['annualized_volatility']:.2%}",
                 'Reserve $M':x['reserve_usd']/1e6,
                 'Estimated 7% hurdle': 'PASS' if x['estimated_net_target_met'] else 'FAIL',
                 'Mandate verdict': x['mandate_verdict']})
st.dataframe(pd.DataFrame(rows), hide_index=True)
st.caption('Historical arithmetic means are not forecasts or evidence of achieving the ten-year objective. Fees include operating/custody only; ETF expenses are already reflected in adjusted prices. Turnover is shown in downloaded results against an assumed 3/29.1/67.9 starting mix; no Apex turnover cap was supplied.')
st.subheader('Signal and data card')
st.json(result['signal'])
st.markdown((ROOT/'docs/data-card.md').read_text())
st.subheader('Stress runs and stop rules')
runs=stress_suite()
st.dataframe(pd.DataFrame([{'Case':k,'Feasible':v['portfolio'] is not None,
 'Largest weight shift':f"{v['largest_weight_change']:.1%}" if v['largest_weight_change'] is not None else 'N/A',
 'Stop':v['stop']} for k,v in runs.items()]), hide_index=True)
st.write('Stop research allocation approval if infeasible or any single stress moves a weight by more than 10 points. Stop live adoption while policy, vintage, benchmark and independent validation gaps remain. Do not execute if the price observation is over 45 calendar days old at the proposed trade date.')
st.download_button('Download current analysis', json.dumps(result,indent=2), 'apex-analysis.json')
with st.expander('Decision memo'):
    st.markdown((ROOT/'docs/decision-memo.md').read_text())
