from datetime import datetime, timedelta
from DataFeed.ForexRateApi import fetch_candles
from DataFeed.Persistance import load_last_time, persist_bulk
from DataFeed.LiveCollection import run_live
import os


def bootstrap(pair="EURUSD", initial_days=30):
    last_time = load_last_time()

    if last_time is None:
        print("No historical data found. Initial backfill")
        candles = fetch_candles(pair, limit=initial_days * 1440)
        persist_bulk(candles)

    else:
        print("Found previous state. Checking gap")
        candles = fetch_candles(pair, start_time=last_time)
        if candles:
            persist_bulk(candles)

    print("Starting live feed")
    run_live(pair)


if __name__ == "__main__":
    bootstrap(pair="EURUSD", initial_days=30)
