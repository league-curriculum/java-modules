#!/bin/bash

# Commit all of the level websites

# Loop through levels 0 to 5
for level in {0..5}
do
  # Execute commands for each level
  echo "======= Level$level ======="
  ( cd "_build/levels/Level$level" 
    git add -A 
    git commit -a -m'General Update' 
    git push 
    git status )
done
