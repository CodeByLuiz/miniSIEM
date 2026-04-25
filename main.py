from parser.log_parser import parse_log
from detection.detector import detect_threats
from utils.storage import save_json


def generate_fake_logs():
    logs = []

    for i in range(8):
        logs.append(f"Jul 10 10:00:0{i} server sshd[123]: Failed password from 192.168.0.10")

    logs.append("Jul 10 10:01:00 server sshd[123]: Accepted password from 192.168.0.10")
    logs.append("Jul 10 10:02:00 server sshd[123]: Accepted password from 10.0.0.5")

    return logs


def run_siem():
    raw_logs = generate_fake_logs()

    parsed_logs = []
    for line in raw_logs:
        parsed = parse_log(line)
        if parsed:
            parsed_logs.append(parsed)

    alerts = detect_threats(parsed_logs)

    save_json(parsed_logs, "data/events.json")
    save_json(alerts, "data/alerts.json")

    print("\n ALERTAS :")
    for alert in alerts:
        print(f"[{alert['risk']}] {alert['type']} - {alert['ip']} ({alert['count']} tentativas)")


if __name__ == "__main__":
    run_siem()