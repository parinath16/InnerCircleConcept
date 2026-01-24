from Engine.contextBuilder import build_context
from IctCoreEngine.validator import validate_setup
from RiskManagement import RiskManager

# RiskMangemennt part 
def on_new_candle(df, account): # gives a trade plan on every new candle .
    ctx = build_context(df) # wants to clarify - df = "pair should br given"

    if not validate_setup(ctx):
        return None 

    
    risk = RiskManager(ctx, account)
    trade_plan = risk.build_trade()

    return trade_plan
# bACk Testing part 
from BackTesting.engine import BacktestEngine
from BackTesting.report import generate_report
import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    df.columns = [c.lower().strip() for c in df.columns]
    return df.to_dict("records")

def run_backtest(): # this Back testing core part
    historical_data = load_csv("Data/Data/historical/EURUSD_M1.csv") 
    account = {"balance": 10000, "risk_per_trade": 0.01}
    engine = BacktestEngine(historical_data, account)
    trades = engine.run()
    print(generate_report(trades))
