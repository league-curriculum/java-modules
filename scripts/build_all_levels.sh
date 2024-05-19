#!/bin/bash

# Rebuild all of the level websites

# Loop through levels 0 to 5
for level in {0..5}
do
  # Execute commands for each level
  echo "======= Level$level ======="
  jtl -v java web -l Level$level
  jtl -v java build -l Level$level
done
