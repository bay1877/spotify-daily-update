#!/bin/bash

# export SPOTIPY API ENV VARIABLES (DON'T SHARE YOUR API KEYS/INFO PUBLICLY)
export SPOTIPY_CLIENT_ID='your client hash here'
export SPOTIPY_CLIENT_SECRET='your client secret hash here'
export SPOTIPY_REDIRECT_URI='your redirect uri here (ex http://localhost:9091)'

# cd to the project directory
command cd ~/PATH_TO_PROJ_DIR
# source the activate script
source ./venv/bin/activate
# run the main python script
python spotify.py

