import requests
import os
from dotenv import load_dotenv

# Load the hidden .env file
load_dotenv()

# Fetch secrets from the environment instead of hardcoding them
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_msg(message):
    if not TOKEN or not CHAT_ID:
        print("❌ Error: Secrets not found in .env file!")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"

    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("🚀 Notification sent to your phone!")
        else:
            print(f"❌ Failed to send. Error: {response.text}")
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")

if __name__ == "__main__":
    # Simulate a DevOps event
    event_msg = "🚨 *DevOps Alert: Day 14* 🚨\n\nYour System Auditor has finished. \nStatus: *All Systems Green* ✅\nLocation: *WSL-Ubuntu*"
    send_telegram_msg(event_msg)