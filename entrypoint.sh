#!/bin/bash

# Pull the latest changes from the cloned GitHub repository
if git -C /bot pull; then
  echo "Pulled latest changes from GitHub."
else
  echo "Failed to pull from GitHub repository." >&2
  exit 1
fi

# Execute the Python bot
exec python /bot/main.py
