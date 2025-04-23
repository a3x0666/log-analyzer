# 🛡️ Automated Log Analyzer & Threat Detection

A minimal yet effective security tool for system administrators and analysts. This project collects and analyzes Linux system logs to detect suspicious activity such as brute-force attacks, failed logins, and privilege escalation patterns.

## 📂 Project Structure

```
log-analyzer/
├── logs/                      # Collected system logs
├── collect_logs.sh            # Bash: collects logs
├── analyze_logs.py            # Python: analyzes for threats
├── alerts.log                 # Output: flagged alerts
└── README.md                  # Project documentation
```

## 🚀 How to Use

### 1. Collect Logs
```bash
chmod +x collect_logs.sh
./collect_logs.sh
```

### 2. Analyze Logs
```bash
python3 analyze_logs.py
```

### 3. View Alerts
```bash
cat alerts.log
```

## ✅ Features

- Collects common Linux logs (`syslog`, `auth.log`, `dmesg`)
- Analyzes logs using regex patterns for:
  - Failed SSH logins
  - Sudo misuse
  - Authentication failures
  - Root shell access attempts
- Outputs a clean, review-ready `alerts.log`

## 📘 Author

**Abhay Aneesh**  
[LinkedIn](https://www.linkedin.com/in/abhayaneesh) · [GitHub](https://github.com/a3x0666)

## 📄 License

MIT License – Free to use and modify.
