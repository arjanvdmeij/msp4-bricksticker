
#!/bin/bash

# Simple script to perform several steps in a row:
# 1) Collect static files and upload them to AWS
# 2) Perform a push to github in order to deploy
#
# Push can be cancelled with <CTRL>-C
#
# Created to solve collecting static files to a local directory
# due to checks in Django settings file 

# Change ENVTYPE
export ENVTYPE='production'

# Run collection of static files
python3 ~/workspace/manage.py collectstatic

# Revert the ENVTYPE variable
export ENVTYPE='development'

# Perform a push to github
git push origin master
