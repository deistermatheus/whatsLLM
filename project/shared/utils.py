def get_uptime():
    with open('/proc/uptime', 'r') as f: # unix dependency
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds