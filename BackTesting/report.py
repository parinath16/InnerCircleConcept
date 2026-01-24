from BackTesting.metrics import compute_metrics

def generate_report(trades):
    metrics = compute_metrics(trades)
    report = f"""
BACKTEST REPORT
----------------------
Total Trades: {metrics['total_trades']}
Wins: {metrics['wins']}
Losses: {metrics['losses']}
Win Rate: {metrics['win_rate']*100}%
"""
    return report
