from IctCoreEngine.context import build_core_context
from IctCoreEngine.validator import validate_setup
from RiskManagement import RiskManager
import copy

class BacktestEngine:
    def __init__(self, historical_data, account):
        """
        historical_data: List[Dict] of candles (M1)
        account: dict {balance, risk_per_trade}
        """
        self.data = historical_data
        self.account = copy.deepcopy(account)
        self.trades = []

    def run(self):
        """
        Loop over historical data candle by candle
        """
        for i in range(20, len(self.data)):  # start after enough candles
            ltf = self.data[:i]  # slice candles up to current
            htf = self.aggregate_htf(ltf)  # optional HTF aggregation

            ctx = build_core_context(ltf, htf)

            if not validate_setup(ctx):
                continue  # no valid setup

            # Generate trade plan
            risk = RiskManager(ctx, self.account)
            trade_plan = risk.build_trade()

            if trade_plan:
                self.execute_virtual_trade(trade_plan)

        return self.trades

    def execute_virtual_trade(self, trade_plan):
        """
        Virtual execution: record trade, update equity
        """
        entry = trade_plan["entry"]
        sl = trade_plan["stop_loss"]
        tp = trade_plan["take_profit"]
        direction = trade_plan["direction"]
        lot = trade_plan["lot_size"]

        # simulate outcome (simplified: next candle hits TP or SL randomly)
        outcome = "win" if entry < tp else "loss"  # dummy logic for now

        trade_record = {
            "entry": entry,
            "stop": sl,
            "tp": tp,
            "direction": direction,
            "lot_size": lot,
            "outcome": outcome
        }
        self.trades.append(trade_record)

    def aggregate_htf(self, ltf):
        """
        Optional: convert M1 candles to H1 / D1 for bias
        For learning, simple example: take every 60 candles = H1
        """
        htf = []
        for i in range(0, len(ltf), 60):
            block = ltf[i:i+60]
            if not block:
                continue
            htf.append({
                "open": block[0]["open"],
                "high": max(c["high"] for c in block),
                "low": min(c["low"] for c in block),
                "close": block[-1]["close"]
            })
        return htf
