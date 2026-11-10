"""Apex research process. All rates are annual decimals; weights sum to one."""
import json
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
TICKERS = ['SGOV', 'BND', 'VT']
INITIAL_NAV = 50_000_000
BUFFER = 1_500_000
TARGET = .07  # Planning CPI .025 plus mandate real objective .045.


def load_prices():
    frame = pd.read_csv(ROOT / 'prices.csv', index_col=0, parse_dates=True)
    if list(frame.columns) != TICKERS or frame.index.has_duplicates:
        raise ValueError('Expected unique dates and SGOV, BND, VT columns.')
    if not np.isfinite(frame.values).all() or (frame <= 0).any().any():
        raise ValueError('Prices must be finite, positive and complete.')
    months = frame.index.to_period('M').asi8
    if len(frame) < 61 or not (np.diff(months) == 1).all():
        raise ValueError('Need at least 61 consecutive monthly prices.')
    return frame


def signal(prices):
    """Snapshot signal: no claim of historical vintage or historical backtest."""
    value = float(prices.VT.iloc[-1] / prices.VT.iloc[-13] - 1)
    return {'name': '12-month VT total-return proxy momentum', 'value': value,
            'observation_end': str(prices.index[-1].date()),
            'snapshot_verified_available_by': '2026-11-10',
            'earliest_proposed_execution': '2026-11-12',
            'equity_cap': .70 if value > 0 else .30,
            'rule': 'Positive momentum: VT <=70%; otherwise VT <=30%.',
            'vintage_limit': 'Vendor-adjusted snapshot retrieved from GitHub on Nov 10; not a historical vintage.'}


def estimates(prices, months=60, fee=.0025, equity_shift=0):
    returns = prices.pct_change(fill_method=None).dropna().tail(months)
    if len(returns) != months:
        raise ValueError('Insufficient observations for requested window.')
    mean = returns.mean().to_numpy() * 12 - fee
    mean[2] += equity_shift
    cov = returns.cov().to_numpy() * 12
    if not np.isfinite(cov).all() or np.linalg.eigvalsh(cov).min() < -1e-10:
        raise ValueError('Invalid covariance.')
    return mean, cov


def measure(weights, mean, cov, reserve=.03, cap=.70):
    w = np.array(weights, dtype=float)
    # Starting holdings are an explicit assumption, not an actual client inventory.
    current = np.array([.03, .291, .679])  # 3% buffer + remaining assets at 70/30.
    turnover = float(np.abs(w-current).sum()/2)
    checks = {'fully invested': bool(abs(w.sum()-1) < 1e-9),
              'long only / no leverage': bool((w >= 0).all()),
              'cash/Treasury buffer': bool(w[0] + 1e-9 >= reserve),
              'signal equity cap (design assumption)': bool(w[2] <= cap+1e-9)}
    failures = [k for k, v in checks.items() if not v]
    return {'weights': dict(zip(TICKERS, w.tolist())),
            'net_return_estimate': float(w@mean),
            'annualized_volatility': float(np.sqrt(max(0, w@cov@w))),
            'reserve_usd': float(w[0]*INITIAL_NAV), 'one_way_turnover': turnover,
            'estimated_net_target_met': bool(w@mean >= TARGET-1e-12),
            'checks': checks, 'failed_rules': failures,
            'mandate_verdict': 'FAIL: '+', '.join(failures) if failures else
                'UNVERIFIED: 5% issuer policy/look-through, risk budget and ten-year objective unresolved'}


def run(months=60, fee=.0025, equity_shift=0, reserve=.03, equity_cap=None):
    prices = load_prices()
    sig = signal(prices)
    cap = sig['equity_cap'] if equity_cap is None else equity_cap
    mean, cov = estimates(prices, months, fee, equity_shift)
    baselines = {name: measure(w, mean, cov, reserve, cap) for name, w in
                 {'Equal weight': [1/3]*3, '70/30 tradable proxy': [0,.30,.70]}.items()}
    best = None
    for bills in range(21):
        for bonds in range(21-bills):
            w = np.array([bills, bonds, 20-bills-bonds])/20
            if w[0] < reserve-1e-9 or w[2] > cap+1e-9 or w@mean < TARGET-1e-12:
                continue
            candidate = measure(w, mean, cov, reserve, cap)
            if best is None or candidate['annualized_volatility'] < best['annualized_volatility']:
                best = candidate
    return {'inputs': {'months': months, 'annual_fee': fee, 'VT_estimate_shift': equity_shift,
                       'reserve_minimum': reserve, 'equity_cap': cap, 'target': TARGET,
                       'planning_inflation': .025, 'initial_nav': INITIAL_NAV},
            'signal': sig, 'net_asset_means': dict(zip(TICKERS, mean.tolist())),
            'baselines': baselines, 'portfolio': best,
            'decision': 'REJECT live adoption; research testing only; live allocation range 0–0%'}


def stress_suite():
    cases = {'base': {}, 'VT estimate minus 1pp': {'equity_shift': -.01},
             '36-month window': {'months': 36}, 'fees 100bps': {'fee': .01},
             'buffer 20%': {'reserve': .20}, 'equity cap 30%': {'equity_cap': .30},
             'combined': {'months': 36, 'fee': .01, 'equity_shift': -.01, 'equity_cap': .30}}
    runs = {name: run(**kwargs) for name, kwargs in cases.items()}
    base = runs['base']['portfolio']
    for result in runs.values():
        other = result['portfolio']
        shift = max(abs(other['weights'][t]-base['weights'][t]) for t in TICKERS) if base and other else None
        result['largest_weight_change'] = shift
        result['stop'] = other is None or (shift is not None and shift > .10+1e-9)
    return runs


if __name__ == '__main__':
    output = stress_suite()
    (ROOT / 'visible_output.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: {'portfolio': v['portfolio'], 'stop': v['stop'],
                          'largest_weight_change': v['largest_weight_change']} for k,v in output.items()}, indent=2))
