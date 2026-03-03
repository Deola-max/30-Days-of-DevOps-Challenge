import os
import zipfile
from datetime import datetime

LOG_DIR = "/home/lambefavour/30-days-devops/day16/logs"
ARCHIVE_DIR = "/home/lambefavour/30-days-devops/day16/archives"

def rotate_logs():
    print("♻️ Starting Log Rotation...")

    # Create a timestamp for the zip file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_filename = f"logs_archive_{timestamp}.zip"
    zip_path = os.path.join(ARCHIVE_DIR, zip_filename)

    # 1. Create a zip file
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(LOG_DIR):
            for file in files:
                if file.endswith(".log"):
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=file)
                    print(f"📦 Compressed: {file}")
                    # 2. Delete the original file after compressing
                    os.remove(file_path)
                    print(f"🗑️ Deleted original: {file}")

    print(f"✅ Logs archived to: {zip_path}")

if __name__ == "__main__":
    rotate_logs()