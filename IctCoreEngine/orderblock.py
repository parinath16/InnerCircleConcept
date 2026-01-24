def find_orderblock(ltf, bias, structure):
    if structure is None:
        return None

    for candle in reversed(ltf[:-2]):
        if bias == "bullish" and candle["close"] < candle["open"]:
            return {
                "type": "bullish_ob",
                "high": candle["high"],
                "low": candle["low"]
            }

        if bias == "bearish" and candle["close"] > candle["open"]:
            return {
                "type": "bearish_ob",
                "high": candle["high"],
                "low": candle["low"]
            }

    return None
