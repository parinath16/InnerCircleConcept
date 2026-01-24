def calculate_take_profit(ctx):
    structure = ctx["structure"]

    if structure["type"] == "bullish_mss":
        return structure["break_level"]
    elif structure["type"] == "bearish_mss":
        return structure["break_level"]

    return None
