log = []

def detect_beacons():
    # Demo simple: detectamos 3 heartbeats como alerta
    log.append("ALERT: beaconing detected")

def show_log():
    for entry in log:
        print(entry)
