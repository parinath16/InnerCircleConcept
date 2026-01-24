import time
from DataFeed.ForexRateApi import fetch_candles
from DataFeed.Persistance import append_candle,save_last_time


def run_live(pair="EURUSD"):
    while True:
        candles = fetch_candles(pair, limit=1)

        if candles:
            append_candle(candles[0])
            save_last_time(candles[0]["time"])


        time.sleep(60)
