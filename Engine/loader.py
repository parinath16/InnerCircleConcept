import pandas as pd

def load_ltf(pair, limit=120):
    df = pd.read_csv(f"Data/Data/historical/{pair}_M1.csv")
    df = df.tail(limit)

    return df.to_dict("records")
