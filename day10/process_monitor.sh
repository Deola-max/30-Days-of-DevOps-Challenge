#!/bin/bash

echo "--- Day 10: Process Monitor ---"

# List the top 5 processes using the most memory
echo "Top 5 Memory-Hungry Processes:"
ps aux --sort=-%mem | head -n 6