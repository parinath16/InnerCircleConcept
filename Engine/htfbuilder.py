import pandas as pd
def build_htf(ltf, tf=15):
    df = pd.DataFrame(ltf)
    df["time"] = pd.to_datetime(df["time"])

    htf = (
        df
        .set_index("time")
        .resample(f"{tf}T")
        .agg({
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last"
        })
        .dropna()
        .reset_index()
    )

    return htf.to_dict("records")
