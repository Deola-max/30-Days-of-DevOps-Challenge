#!/bin/bash

echo "--- System Resource Report ($(date)) ---"

# Check Memory Usage (RAM)
echo "1. MEMORY USAGE:"
free -h | awk '/^Mem:/ {print "Used: " $3 " / Total: " $2}'

# Check Disk Usage
echo -e "\n2. DISK SPACE USAGE:"
df -h | grep '^/dev/' | awk '{print $1 ": " $5 " used (" $4 " available)"}'

# Check CPU Load
echo -e "\n3. CPU LOAD:"
uptime | awk -F'load average:' '{ print $2 }'