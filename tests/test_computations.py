import pytest
from tradingview_ta.technicals import Compute, Recommendation


def test_ma_buy_sell_neutral():
    assert Compute.MA(10, 20) == Recommendation.buy
    assert Compute.MA(20, 10) == Recommendation.sell
    assert Compute.MA(10, 10) == Recommendation.neutral


def test_rsi_buy_sell_neutral():
    assert Compute.RSI(25, 20) == Recommendation.buy
    assert Compute.RSI(75, 80) == Recommendation.sell
    assert Compute.RSI(50, 50) == Recommendation.neutral


def test_stoch_buy_sell_neutral():
    # buy when k < 20, d < 20, k > d and k1 < d1
    assert Compute.Stoch(10, 5, 3, 8) == Recommendation.buy
    # sell when k > 80, d > 80, k < d and k1 > d1
    assert Compute.Stoch(90, 95, 99, 90) == Recommendation.sell
    assert Compute.Stoch(50, 50, 50, 50) == Recommendation.neutral


def test_cci20_buy_sell_neutral():
    assert Compute.CCI20(-150, -200) == Recommendation.buy
    assert Compute.CCI20(150, 200) == Recommendation.sell
    assert Compute.CCI20(0, 0) == Recommendation.neutral


def test_adx_buy_sell_neutral():
    assert Compute.ADX(25, 30, 10, 5, 15) == Recommendation.buy
    assert Compute.ADX(25, 10, 30, 15, 5) == Recommendation.sell
    assert Compute.ADX(10, 10, 10, 10, 10) == Recommendation.neutral


def test_ao_buy_sell_neutral():
    assert Compute.AO(1, -1, 0) == Recommendation.buy
    assert Compute.AO(-1, 1, 0) == Recommendation.sell
    assert Compute.AO(0, 0, 0) == Recommendation.neutral


def test_mom_buy_sell_neutral():
    assert Compute.Mom(2, 1) == Recommendation.buy
    assert Compute.Mom(1, 2) == Recommendation.sell
    assert Compute.Mom(1, 1) == Recommendation.neutral


def test_macd_buy_sell_neutral():
    assert Compute.MACD(2, 1) == Recommendation.buy
    assert Compute.MACD(1, 2) == Recommendation.sell
    assert Compute.MACD(1, 1) == Recommendation.neutral


def test_bb_buy_sell_neutral():
    assert Compute.BBBuy(5, 10) == Recommendation.buy
    assert Compute.BBSell(15, 10) == Recommendation.sell
    assert Compute.BBBuy(15, 10) == Recommendation.neutral
    assert Compute.BBSell(5, 10) == Recommendation.neutral


def test_psar_buy_sell_neutral():
    assert Compute.PSAR(5, 10) == Recommendation.buy
    assert Compute.PSAR(15, 10) == Recommendation.sell
    assert Compute.PSAR(10, 10) == Recommendation.neutral


def test_recommend_boundaries():
    assert Compute.Recommend(-0.75) == Recommendation.strong_sell
    assert Compute.Recommend(-0.25) == Recommendation.sell
    assert Compute.Recommend(0) == Recommendation.neutral
    assert Compute.Recommend(0.25) == Recommendation.buy
    assert Compute.Recommend(0.75) == Recommendation.strong_buy
    assert Compute.Recommend(1.5) == Recommendation.error


def test_simple_buy_sell_neutral():
    assert Compute.Simple(-1) == Recommendation.sell
    assert Compute.Simple(1) == Recommendation.buy
    assert Compute.Simple(0) == Recommendation.neutral
