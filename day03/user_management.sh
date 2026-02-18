#!/bin/bash

# Define the group and user names
GROUP_NAME="dev_engineers"
USER_NAME="favour_dev"

echo "--- Starting User Management Task ---"

# Create the group if it doesn't exist
sudo groupadd -f $GROUP_NAME
echo "1. Group '$GROUP_NAME' ready."

# Create the user and add to the group
# -m creates a home directory, -g assigns the group
sudo useradd -m -g $GROUP_NAME $USER_NAME
echo "2. User '$USER_NAME' created and added to '$GROUP_NAME'."

# Verify the creation
echo "3. Verification:"
grep "$GROUP_NAME" /etc/group