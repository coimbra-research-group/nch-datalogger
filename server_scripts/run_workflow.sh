#!/bin/bash

# Run request file to import and store html
python request.py

# Run process file to convert html to data structure
python process.py

# Commit data
git add TBD_data_filename.csv
git commit -m "update data"

# Run plot file to generate new plots and html code
python plot.py

# Commit all changes
git add .
git commit -m "update dashboard"

# Push changes
git push origin main