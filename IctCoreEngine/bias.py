def htf_bias(htf):
    if len(htf) < 2:
        return "neutral"

    prev = htf[-2]
    last = htf[-1]

    if last["high"] > prev["high"] and last["low"] > prev["low"]:
        return "bullish"

    if last["high"] < prev["high"] and last["low"] < prev["low"]:
        return "bearish"

    return "neutral"
