# Python Log Analysis – Brute Force Detection

This project is a Python-based security tool designed to analyse authentication logs and identify suspicious login activity such as brute-force and password-spraying attacks.

## Features
- Parses 500+ authentication log entries
- Detects IP addresses with repeated failed login attempts
- Flags potential brute-force and password-spraying behaviour
- Simple threshold-based alerting

## How It Works
The script scans each log entry for failed password attempts, extracts the source IP address, and counts how many times each IP appears. If an IP exceeds a defined threshold, it is flagged as suspicious.

## Technologies Used
- Python
- Log analysis
- Security monitoring concepts

## Example Output
185.199.110.153 -> 140 failed attempts
45.133.1.77 -> 20 failed attempts
212.102.33.19 -> 23 failed attempts