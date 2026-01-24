def calculate_stop_loss(ctx):
    ob = ctx["orderblock"]

    if ob["type"] == "bullish_ob":
        return ob["low"]
    elif ob["type"] == "bearish_ob":
        return ob["high"]

    return None
