def calculate_position_size(balance, risk_pct, entry, stop, pip_value=10):
    risk_amount = balance * risk_pct
    stop_distance = abs(entry - stop)

    if stop_distance == 0:
        return 0

    lot_size = risk_amount / (stop_distance * pip_value)
    return round(lot_size, 2)
