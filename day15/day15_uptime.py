import requests
import time
import os # 1. Import os to handle file paths

URL_TO_CHECK = "https://github.com/Deola-max" 
# 2. Define the path inside the container
LOG_FILE = "/app/data/uptime.log" 

def check_site():
    try:
        response = requests.get(URL_TO_CHECK, timeout=15)
        # 3. Create a message string
        message = "" 
        if response.status_code == 200:
            message = f"✅ {URL_TO_CHECK} is LIVE and Healthy!"
        else:
            message = f"⚠️ Alert! {URL_TO_CHECK} returned Status Code: {response.status_code}"
        
        # 4. Print to terminal
        print(message)
        
        # 5. Write to the log file in the volume!
        with open(LOG_FILE, "a") as f:
            f.write(message + "\n")

    except Exception as e:
        error_msg = f"🚨 CRITICAL: Could not reach {URL_TO_CHECK}. Error: {e}"
        print(error_msg)
        # 6. Also write errors to the log file
        with open(LOG_FILE, "a") as f:
            f.write(error_msg + "\n")

if __name__ == "__main__":
    print("🚀 Day 15: Starting Uptime Monitor...")
    check_site()