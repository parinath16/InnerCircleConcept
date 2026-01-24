from datetime import datetime, timezone

def session_context():
    hour = datetime.now(timezone.utc).hour

    if 7 <= hour <= 10:
        return "london_killzone"

    if 12 <= hour <= 15:
        return "ny_killzone"

    if 0 <= hour <= 2:
        return "asia"

    return "dead_zone"
