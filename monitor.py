import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def check_logs(log_file, keywords):
    with open(log_file, "r") as f:
        lines = f.readlines()

    alerts = []
    for line in lines:
        for keyword in keywords:
            if keyword in line:
                alerts.append(line.strip())

    return alerts

def send_alert(alerts):
    print("\nALERTS DETECTED:")
    for alert in alerts:
        print(alert)

def main():
    config = load_config()
    log_file = config["log_file"]
    keywords = config["keywords"]

    print("Monitoring logs...\n")

    alerts = check_logs(log_file, keywords)

    if alerts:
        send_alert(alerts)
    else:
        print("No issues found")

if __name__ == "__main__":
    main()