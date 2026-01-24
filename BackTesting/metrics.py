def compute_metrics(trades):
    total = len(trades)
    wins = len([t for t in trades if t["outcome"] == "win"])
    losses = len([t for t in trades if t["outcome"] == "loss"])
    win_rate = wins / total if total else 0
    return {
        "total_trades": total,
        "wins": wins,
        "losses": losses,
        "win_rate": round(win_rate, 2)
    }
