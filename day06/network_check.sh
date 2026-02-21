#!/bin/bash

# Target host
SERVER="google.com"

echo "--- Day 6: Network Port Scanner ---"

# Checking common ports: 80 (HTTP) and 443 (HTTPS)
for PORT in 80 443; do
    # we use 'nc' (netcat) or 'timeout' with 'bash' to check
    if timeout 2 bash -c "</dev/tcp/$SERVER/$PORT" &>/dev/null; then
        echo "✅ Port $PORT is OPEN on $SERVER"
    else
        echo "❌ Port $PORT is CLOSED on $SERVER"
    fi
done