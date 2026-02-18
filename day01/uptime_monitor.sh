#!/bin/bash
URL="example.com"

if curl -sL --connect-timeout 5 "$URL" > /dev/null; then
    # We use the FULL PATH here so Cron knows exactly where to write
    echo "$(date): $URL is UP ✅" >> /home/lambefavour/30-days-devops/day01/uptime_log.txt
else
    echo "$(date): $URL is DOWN ❌" >> /home/lambefavour/30-days-devops/day01/uptime_log.txt
fi
# Updated Label
