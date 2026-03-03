import requests
import time
import os

URL_TO_CHECK = "https://github.com/Deola-max" 
LOG_FILE = "/app/data/uptime.log" 
INTERVAL = 60  # <--- Added this (checks every 60 seconds)

def check_site():
    print("🚀 Day 19: Continuous Uptime Monitor Starting...")
    
    while True:  # <--- The loop goes here!
        try:
            response = requests.get(URL_TO_CHECK, timeout=15)
            timestamp = time.ctime() # Adds the time so the log is useful
            
            if response.status_code == 200:
                message = f"✅ {timestamp} - {URL_TO_CHECK} is LIVE and Healthy!"
            else:
                message = f"⚠️ {timestamp} - Alert! Status Code: {response.status_code}"
            
            print(message)

            # Ensure the directory exists before writing
            os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
            
            with open(LOG_FILE, "a") as f:
                f.write(message + "\n")

        except Exception as e:
            error_msg = f"🚨 {time.ctime()} - CRITICAL Error: {e}"
            print(error_msg)
            with open(LOG_FILE, "a") as f:
                f.write(error_msg + "\n")
        
        # Wait before the next check
        time.sleep(INTERVAL)

if __name__ == "__main__":
    check_site()