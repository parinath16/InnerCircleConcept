def detect_market_structure(ltf, bias, liquidity):
    if len(ltf) < 20:
        return None

    swings = _detect_swings(ltf)

    if len(swings["highs"]) < 2 or len(swings["lows"]) < 2:
        return None

    last_high = swings["highs"][-1]
    prev_high = swings["highs"][-2]

    last_low = swings["lows"][-1]
    prev_low = swings["lows"][-2]

    last_close = ltf[-1]["close"]

    # ICT RULE:
    # Liquidity must be taken BEFORE structure shift
    if bias == "bullish" and liquidity == "sellside":
        if last_close > prev_high["price"]:
            return {
                "type": "bullish_mss",
                "break_level": prev_high["price"],
                "protected_level": last_low["price"]
            }

    if bias == "bearish" and liquidity == "buyside":
        if last_close < prev_low["price"]:
            return {
                "type": "bearish_mss",
                "break_level": prev_low["price"],
                "protected_level": last_high["price"]
            }

    return None


def _detect_swings(candles, lookback=3):
    highs = []
    lows = []

    for i in range(lookback, len(candles) - lookback):
        high = candles[i]["high"]
        low = candles[i]["low"]

        if all(high > candles[i - j]["high"] for j in range(1, lookback + 1)) and \
           all(high > candles[i + j]["high"] for j in range(1, lookback + 1)):
            highs.append({"index": i, "price": high})

        if all(low < candles[i - j]["low"] for j in range(1, lookback + 1)) and \
           all(low < candles[i + j]["low"] for j in range(1, lookback + 1)):
            lows.append({"index": i, "price": low})

    return {"highs": highs, "lows": lows}
