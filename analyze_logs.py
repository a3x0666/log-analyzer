"""
analyze_logs.py
Author: Abhay Aneesh

This script analyzes Linux system logs for suspicious activity patterns
such as failed login attempts, brute-force authentication, sudo misuse, and root access attempts.
"""

import os
import re

LOG_DIR = "logs"
OUTPUT_FILE = "alerts.log"

PATTERNS = {
    "Failed SSH Login": r"Failed password for .* from (\d{1,3}\.){3}\d{1,3}",
    "Sudo Usage": r"sudo:.*",
    "Authentication Failure": r"authentication failure;.*",
    "Root Shell Access": r"session opened for user root"
}

alerts = []

print("[*] Analyzing logs...")

for log_file in os.listdir(LOG_DIR):
    path = os.path.join(LOG_DIR, log_file)
    with open(path, 'r', errors='ignore') as f:
        for line_num, line in enumerate(f, start=1):
            for alert_type, pattern in PATTERNS.items():
                if re.search(pattern, line):
                    alerts.append(f"[{alert_type}] {log_file}:{line_num} - {line.strip()}")

with open(OUTPUT_FILE, 'w') as f:
    f.write("\n".join(alerts))

print(f"[✔] Analysis complete. {len(alerts)} alerts written to '{OUTPUT_FILE}'.")
