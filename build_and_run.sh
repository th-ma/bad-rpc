#!/bin/bash

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# Run the program
python src/main.py
