#!/bin/bash

# Folder to clean (You can change this)
TARGET_DIR="/home/lambefavour/30-days-devops/day01"

echo "--- Cleaning logs older than 7 days in $TARGET_DIR ---"

# This command finds files ending in .txt modified more than 7 days ago and deletes them
# (For now, it will just 'list' them so you don't accidentally delete important stuff)
find $TARGET_DIR -name "*.txt" -mtime +7 -exec ls -l {} \;

echo "Cleanup check complete!"