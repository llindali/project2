import unittest
import numpy as np
from engine import run, load_prices, signal, estimates, stress_suite, measure

class FinanceChecks(unittest.TestCase):
    def test_arithmetic_against_direct_calculation(self):
        prices=load_prices()
        returns=prices.to_numpy()[1:]/prices.to_numpy()[:-1]-1
        mean,cov=estimates(prices)
        np.testing.assert_allclose(mean, returns.mean(axis=0)*12-.0025)
        np.testing.assert_allclose(cov,np.cov(returns,rowvar=False,ddof=1)*12)
        w=np.array([.55,0,.45])
        base=run()['portfolio']
        self.assertAlmostEqual(base['annualized_volatility'],np.std(returns@w,ddof=1)*np.sqrt(12))
        self.assertAlmostEqual(base['reserve_usd'],27_500_000)

    def test_base_and_baseline_rule_failures(self):
        result=run()
        self.assertEqual(result['portfolio']['weights'],{'SGOV':.55,'BND':0.,'VT':.45})
        self.assertFalse(result['baselines']['Equal weight']['estimated_net_target_met'])
        self.assertIn('cash/Treasury buffer',result['baselines']['70/30 tradable proxy']['failed_rules'])
        self.assertIn('UNVERIFIED',result['portfolio']['mandate_verdict'])

    def test_signal_branches_and_infeasibility(self):
        p=load_prices()
        self.assertEqual(signal(p)['equity_cap'],.70)
        p.iloc[-1,2]=p.iloc[-13,2]*.9
        self.assertEqual(signal(p)['equity_cap'],.30)
        self.assertIsNone(run(equity_cap=.30)['portfolio'])

    def test_stops_and_constraint_integrity(self):
        cases=stress_suite()
        self.assertTrue(cases['36-month window']['stop'])
        self.assertAlmostEqual(cases['36-month window']['largest_weight_change'],.25)
        for case in cases.values():
            x=case['portfolio']
            if x:
                self.assertTrue(all(x['checks'].values()))
                self.assertTrue(x['estimated_net_target_met'])
                self.assertAlmostEqual(sum(x['weights'].values()),1)

    def test_app_operates(self):
        from streamlit.testing.v1 import AppTest
        app=AppTest.from_file('app.py').run(timeout=30)
        self.assertEqual(len(app.exception),0)
        self.assertGreaterEqual(len(app.dataframe),2)
        app.sidebar.selectbox[0].set_value(36).run(timeout=30)
        self.assertEqual(len(app.exception),0)
        self.assertIn('80.0%', app.dataframe[0].value['SGOV'].tolist())

if __name__=='__main__':
    unittest.main()
