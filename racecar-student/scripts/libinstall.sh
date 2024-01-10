#!/bin/sh

yes | apt-get update
yes | apt-get upgrade
yes | apt install python3-pip
yes | pip install -r /mnt/c/Users/Chris/Documents/Github/racecar-mn-windows/racecar-student/scripts/requirements.txt
yes | apt install jupyter-notebook
yes | apt-get install ffmpeg libsm6 libxext6 -y
yes | apt-get install dos2unix

