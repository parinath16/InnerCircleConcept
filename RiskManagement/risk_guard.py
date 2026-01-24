from .stop_loss import calculate_stop_loss
from .take_profit import calculate_take_profit
from .position_size import calculate_position_size


class RiskManager:
    def __init__(self, ctx, account):
        self.ctx = ctx
        self.account = account

    def build_trade(self):
        entry = self.ctx["fvg"]["low"] if self.ctx["bias"] == "bullish" else self.ctx["fvg"]["high"]

        stop = calculate_stop_loss(self.ctx)
        target = calculate_take_profit(self.ctx)

        lot_size = calculate_position_size(
            balance=self.account["balance"],
            risk_pct=self.account["risk_per_trade"],
            entry=entry,
            stop=stop
        )

        if lot_size <= 0:
            return None

        return {
            "direction": "buy" if self.ctx["bias"] == "bullish" else "sell",
            "entry": entry,
            "stop_loss": stop,
            "take_profit": target,
            "lot_size": lot_size
        }
