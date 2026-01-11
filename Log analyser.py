import os
log_file = "application.log"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("SCRIPT FOLDER:", BASE_DIR)
print("LOOKING FOR:", log_file)

log_file = os.path.join(BASE_DIR, "application.log")

failed_logins = {}
threshold = 5

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip_address = parts[-4]   # IP comes before "port"
            failed_logins[ip_address] = failed_logins.get(ip_address, 0) + 1

print("Suspicious IPs:")
for ip, count in failed_logins.items():
    if count >= threshold:
        print(f"{ip} -> {count} failed attempts")