def validate_setup(ctx):
    return all([
        ctx["bias"] != "neutral",
        ctx["liquidity"] is not None,
        ctx["structure"] is not None,
        ctx["fvg"] is not None,
        ctx["orderblock"] is not None,
        ctx["session"] in ("london_killzone", "ny_killzone")
    ])
