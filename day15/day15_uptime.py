import requests
import time

# The website you want to monitor
URL_TO_CHECK = "https://github.com/Deola-max" 

def check_site():
    try:
        response = requests.get(URL_TO_CHECK, timeout=15)
        if response.status_code == 200:
            print(f"✅ {URL_TO_CHECK} is LIVE and Healthy!")
        else:
            print(f"⚠️ Alert! {URL_TO_CHECK} returned Status Code: {response.status_code}")
    except Exception as e:
        print(f"🚨 CRITICAL: Could not reach {URL_TO_CHECK}. Error: {e}")

if __name__ == "__main__":
    print("🚀 Day 15: Starting Uptime Monitor...")
    check_site()