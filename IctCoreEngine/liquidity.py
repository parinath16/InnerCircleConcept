def liquidity_sweep(ltf):
    if len(ltf) < 2:
        return None

    last = ltf[-1]
    prev = ltf[-2]

    if last["high"] > prev["high"]:
        return "buyside"

    if last["low"] < prev["low"]:
        return "sellside"

    return None
