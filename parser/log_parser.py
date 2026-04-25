import re

def classify_event(line):
    if "Failed password" in line:
        return "failed_login"
    elif "Accepted password" in line:
        return "successful_login"
    return "other"


def parse_log(line):
    pattern = r'(?P<date>\w+\s+\d+\s+\d+:\d+:\d+).*?from\s+(?P<ip>\d+\.\d+\.\d+\.\d+)'
    match = re.search(pattern, line)

    if match:
        return {
            "timestamp": match.group("date"),
            "ip": match.group("ip"),
            "raw": line.strip(),
            "event_type": classify_event(line)
        }
    return None