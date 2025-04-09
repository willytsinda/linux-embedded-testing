#!/bin/bash
# Kernel module stress test
MODULE="$1"
CYCLES="${2:-100}"

for ((i=1; i<=CYCLES; i++)); do
  echo "Cycle $i: Loading $MODULE"
  if ! insmod "$MODULE"; then exit 1; fi
  sleep 0.5
  echo "Cycle $i: Unloading $MODULE"
  if ! rmmod "$MODULE"; then exit 1; fi
done
echo "✅ $CYCLES cycles completed"
