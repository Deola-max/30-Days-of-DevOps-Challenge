#!/bin/bash

# We will check the 'cron' service we used in Day 2
SERVICE="cron"

echo "--- Day 9: Service Doctor ---"

if systemctl is-active --quiet $SERVICE; then
    echo "✅ $SERVICE is running perfectly."
else
    echo "❌ $SERVICE is DOWN! Attempting to restart..."
    # In a real server, we use: sudo systemctl restart $SERVICE
    echo "⚠️ Restart command sent to $SERVICE."
fi