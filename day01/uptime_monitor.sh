#!/bin/bash
# Use a very stable site for testing
URL="example.com"

# Check if we can reach the site
if curl -sL --connect-timeout 5 "$URL" > /dev/null; then
    echo "$(date): $URL is UP ✅" >> uptime_log.txt
else
    echo "$(date): $URL is DOWN ❌" >> uptime_log.txt
fi
