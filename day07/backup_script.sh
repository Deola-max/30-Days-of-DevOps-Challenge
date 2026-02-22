#!/bin/bash

# Where to backup FROM and TO
SOURCE="/home/lambefavour/30-days-devops/day01"
DEST="/home/lambefavour/30-days-devops/backups"

# Create backup folder if it doesn't exist
mkdir -p $DEST

# Use 'tar' to zip the files with a timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
tar -czf $DEST/backup_$TIMESTAMP.tar.gz $SOURCE

echo "✅ Backup created successfully at $DEST/backup_$TIMESTAMP.tar.gz"