from collections import defaultdict
from config import FAILED_THRESHOLD, HIGH_RISK_THRESHOLD

def calculate_risk(attempts):
    if attempts >= HIGH_RISK_THRESHOLD:
        return "HIGH"
    elif attempts >= FAILED_THRESHOLD:
        return "MEDIUM"
    return "LOW"


def detect_threats(parsed_logs):
    failed_attempts = defaultdict(list)
    alerts = []

    for log in parsed_logs:
        if log["event_type"] == "failed_login":
            failed_attempts[log["ip"]].append(log["timestamp"])

    for ip, attempts in failed_attempts.items():
        if len(attempts) >= FAILED_THRESHOLD:
            alerts.append({
                "type": "brute_force",
                "ip": ip,
                "count": len(attempts),
                "risk": calculate_risk(len(attempts)),
                "timestamps": attempts
            })

    return alerts