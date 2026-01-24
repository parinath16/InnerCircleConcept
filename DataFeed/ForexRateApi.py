import requests

BASE_URL = "https://api.forexrateapi.com/v1"
API_KEY = "dc24d1bb43c19507540f75ed5700a1fb"


def fetch_candles(pair, start_time=None, limit=500):
    symbol = f"{pair[:3]}/{pair[3:]}"
    
    params = {
        "api_key": API_KEY,
        "symbol": symbol,
        "interval": "1m",
        "limit": limit
    }

    if start_time:
        params["start_time"] = start_time  # ISO or timestamp

    r = requests.get(f"{BASE_URL}/candles", params=params)
    r.raise_for_status()

    candles = r.json()["data"]
    candles.reverse()  # oldest → newest

    return [
        {
            "time": c["time"],
            "open": float(c["open"]),
            "high": float(c["high"]),
            "low": float(c["low"]),
            "close": float(c["close"]),
            "volume": float(c.get("volume", 0))
        }
        for c in candles
    ]
