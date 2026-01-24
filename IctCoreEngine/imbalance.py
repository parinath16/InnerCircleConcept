def find_fvg(ltf):
    if len(ltf) < 3:
        return None

    c1, _, c3 = ltf[-3:]

    if c1["high"] < c3["low"]:
        return {
            "type": "bullish",
            "low": c1["high"],
            "high": c3["low"]
        }

    if c1["low"] > c3["high"]:
        return {
            "type": "bearish",
            "low": c3["high"],
            "high": c1["low"]
        }

    return None
