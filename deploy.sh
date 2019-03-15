#!/bin/bash

# Simple script to perform several steps in a row:
# 1) Collect static files and upload them to AWS
# 2) Perform a push to github in order to deploy
#
# Push can be cancelled with <CTRL>-C
#
# Created to solve collecting static files to a local directory
# due to checks in Django settings file 

clear
echo ""
# Change ENVTYPE
export ENVTYPE='production'
# Run collection of static files
echo "Collecting static files (if any) and adding to AWS"
echo ""
python3 ~/workspace/manage.py collectstatic
# Revert the ENVTYPE variable
echo ""
export ENVTYPE='development'
echo ""
echo "Pushing to GitHub"
echo ""
# Perform a push to github
git push origin master
