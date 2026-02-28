import os
import shutil
import time

# --- CONFIGURATION ---
# The folder we want to clean (You can create a dummy 'logs' folder to test)
TARGET_DIR = "./logs" 
BACKUP_DIR = "./archive"
AGE_THRESHOLD_SECONDS = 3600  # 1 hour (for testing, usually it's days)

def log_janitor():
    # 1. Create directories if they don't exist
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print(f"📁 Created {TARGET_DIR}. Add some files there to test!")
        return
    
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    print(f"🧹 Janitor is starting work in {TARGET_DIR}...")
    current_time = time.time()

    # 2. Loop through files in the target directory
    for filename in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, filename)

        # Only work on files, not folders
        if os.path.isfile(file_path):
            file_age = os.path.getmtime(file_path)
            
            # 3. Check if file is older than our threshold
            if (current_time - file_age) > AGE_THRESHOLD_SECONDS:
                print(f"📦 Archiving old file: {filename}")
                # Move the file to the archive folder
                shutil.move(file_path, os.path.join(BACKUP_DIR, filename))
            else:
                print(f"✅ {filename} is still fresh. Skipping.")

    print("✨ Cleanup finished!")

if __name__ == "__main__":
    log_janitor()