#!/bin/bash

# Title: Log Collector Script
# Author: Abhay Aneesh
# Description: Gathers essential Linux logs for security analysis.

LOG_DIR="logs"

mkdir -p "$LOG_DIR"

declare -a FILES=("/var/log/syslog" "/var/log/auth.log" "/var/log/dmesg")

echo "[*] Collecting logs..."

for FILE in "${FILES[@]}"; do
  if [[ -f "$FILE" ]]; then
    cp "$FILE" "$LOG_DIR/$(basename "$FILE")"
    echo "[+] Copied: $FILE"
  else
    echo "[-] Not found: $FILE"
  fi
done

echo "[✔] Logs successfully copied to '$LOG_DIR/'."
