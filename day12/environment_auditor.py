import os
import platform
import shutil
import json
import subprocess

# --- 1. DEFINE COLORS (Like we did in Bash!) ---
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m' # No Color

def audit_system():
    print(f"{YELLOW}🚀 Starting Smart System Audit...{NC}")
    
    info = {
        "os_name": platform.system(),
        "os_release": platform.release(),
        "disk_free_gb": shutil.disk_usage("/")[2] // (2**30),
        "internet_status": "Unknown"
    }

    # --- 2. THE HEALTH CHECK LOGIC ---
    print("\n--- 🛡️  Health Alerts ---")
    
    # Check Disk Space
    if info["disk_free_gb"] < 10:
        print(f"{RED}🚨 ALERT: Low Disk Space! Only {info['disk_free_gb']}GB left.{NC}")
    else:
        print(f"{GREEN}✅ Disk Space is Healthy: {info['disk_free_gb']}GB available.{NC}")

    # Check Internet
    try:
        status = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True)
        if status.returncode == 0:
            info["internet_status"] = "Connected"
            print(f"{GREEN}✅ Internet Connection: Active{NC}")
        else:
            info["internet_status"] = "Disconnected"
            print(f"{RED}❌ Internet Connection: OFFLINE{NC}")
    except Exception:
        print(f"{RED}⚠️  Connectivity Test Failed!{NC}")

    # --- 3. SAVE TO JSON ---
    with open("system_audit.json", "w") as f:
        json.dump(info, f, indent=4)
    
    print(f"\n{YELLOW}✨ Report saved to 'system_audit.json'{NC}")

# --- 4. THE CORRECT BOILERPLATE (Double Underscores!) ---
if __name__ == "__main__":
    audit_system()