import os, json, csv, logging

DATA_PATH = "Data/Data/historical/EURUSD_M1.csv"
META_PATH = "Data/Data/metadata/Last_Time.json"
BUFFER_PATH = "Data/Data/temp/buffer.csv"
LOG_PATH = "Data/Data/log/DataFeed.log"

os.makedirs("Data/Data/historical", exist_ok=True)
os.makedirs("Data/Data/metadata", exist_ok=True)
os.makedirs("Data/Data/temp", exist_ok=True)
os.makedirs("Data/Data/log", exist_ok=True)

logging.basicConfig(filename=LOG_PATH, level=logging.INFO)


def load_last_time():
    if not os.path.exists(META_PATH):
        return None
    with open(META_PATH) as f:
        return json.load(f).get("last_time")


def save_last_time(t):
    with open(META_PATH, "w") as f:
        json.dump({"last_time": t}, f)


def append_candle(candle):
    exists = os.path.exists(DATA_PATH)

    with open(DATA_PATH, "a", newline="") as f:
        writer = csv.DictWriter(f, candle.keys())
        if not exists:
            writer.writeheader()
        writer.writerow(candle)


def persist_bulk(candles):
    for c in candles:
        append_candle(c)

    save_last_time(candles[-1]["time"])
    logging.info(f"Backfilled {len(candles)} candles")
