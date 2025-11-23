#!/bin/bash

# Pull the latest changes from the cloned GitHub repository
git -C /bot pull

# Execute the Python bot
exec python /bot/main.py