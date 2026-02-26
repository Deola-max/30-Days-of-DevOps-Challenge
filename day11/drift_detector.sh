#!/bin/bash

# --- COLOR DEFINITIONS ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color (Reset)

# --- SETUP ---
FILES_TO_WATCH=("drift_detector.sh")
DB_FILE="integrity_baseline.db"

# --- THE INITIALIZER ---
if [[ "$1" == "--init" ]]; then
    echo -e "${YELLOW}📸 Creating Golden Image fingerprints...${NC}"
    > "$DB_FILE" 
    for file in "${FILES_TO_WATCH[@]}"; do
        if [ -f "$file" ]; then
            md5sum "$file" >> "$DB_FILE"
            echo -e "${GREEN}✅ Fingerprint saved for: $file${NC}"
        else
            echo -e "${RED}⚠️  Warning: $file not found!${NC}"
        fi
    done
    echo -e "${GREEN}✨ Baseline complete. System is now SECURE.${NC}"

# --- THE AUDITOR ---
else
    echo -e "${YELLOW}--- 🕵️‍♀️ Audit Started: $(date) ---${NC}"
    
    if [ ! -f "$DB_FILE" ]; then
        echo "${RED}❌ Error: No baseline found! Run './drift_detector.sh --init' first.${NC}"
        exit 1
    fi

    # Check for drift
    if md5sum --status -c "$DB_FILE"; then
        echo -e "${GREEN}🟢 STATUS: SUCCESS. No configuration drift detected.${NC}"
    else
        echo "${RED}🚨 STATUS: DRIFT DETECTED! Unauthorized changes found!${NC}"
        echo "---------------------------------------------------"
        # We use 'sed' to turn the specific "FAILED" text red
        md5sum -c "$DB_FILE" | grep "FAILED" | sed "s/FAILED/${RED}FAILED${NC}/"
        echo "---------------------------------------------------"
    fi
fi
