from tradingview_ta.main import TradingView


def test_data_interval_and_uppercase():
    data = TradingView.data(["nasdaq:aapl"], "1h", ["close"])
    assert data["symbols"]["tickers"] == ["NASDAQ:AAPL"]
    assert data["columns"] == ["close|60"]

    data = TradingView.data(["binance:btcusdt"], "1d", ["close"])
    # 1d uses empty suffix
    assert data["columns"] == ["close"]
