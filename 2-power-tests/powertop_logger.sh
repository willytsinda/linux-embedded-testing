#!/bin/bash
# Power consumption monitor
LOG="power_$(date +%F).csv"
echo "timestamp,power_mW" > "$LOG"

while true; do
  echo "$(date +%FT%T),$(powertop --csv=- | awk -F, '/System baseline power/{print $6*1000}')" >> "$LOG"
  sleep 10
done
