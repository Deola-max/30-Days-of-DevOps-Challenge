#!/bin/bash

# Creating a local environment variable for this session
export APP_USER="favour_admin"
export APP_ENV="production"

echo "--- Day 8: Environment Settings ---"
echo "Application User: $APP_USER"
echo "Environment: $APP_ENV"

# Check if a specific variable is set
if [ -z "$DB_PASSWORD" ]; then
    echo "⚠️ Warning: DB_PASSWORD is not set!"
fi