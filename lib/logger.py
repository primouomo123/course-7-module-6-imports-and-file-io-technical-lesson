from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("user_logs.txt", "a") as file:
        file.write(f"[{timestamp}] {action}\n")

def search_logs(keyword):
    try:
        with open("user_logs.txt", "r") as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found.")

log_action("User logged in")
log_action("User updated profile")

search_logs("profile")