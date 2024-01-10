#!/bin/sh
    
echo "RACECAR_ABSOLUTE_PATH=\"/mnt/c/Users/Chris/Documents/Github/racecar-mn-windows/racecar-student\"
RACECAR_IP=\"127.0.0.1\"
RACECAR_TEAM=\"student\"
RACECAR_CONFIG_LOADED=\"TRUE\"
export DISPLAY=localhost:42.0" > /mnt/c/Users/Chris/Documents/Github/racecar-mn-windows/racecar-student/scripts/.config

sed '/# RACECAR_ALIASES$/d' -i ~/.bashrc
echo "# Source RACECAR tool # RACECAR_ALIASES
if [ -f /mnt/c/Users/Chris/Documents/Github/racecar-mn-windows/racecar-student/scripts/.config ]; then # RACECAR_ALIASES
. /mnt/c/Users/Chris/Documents/Github/racecar-mn-windows/racecar-student/scripts/.config # RACECAR_ALIASES
fi # RACECAR_ALIASES
if [ -f /mnt/c/Users/Chris/Documents/Github/racecar-mn-windows/racecar-student/scripts/racecar_tool.sh ]; then # RACECAR_ALIASES
. /mnt/c/Users/Chris/Documents/Github/racecar-mn-windows/racecar-student/scripts/racecar_tool.sh # RACECAR_ALIASES
fi # RACECAR_ALIASES" >> ~/.bashrc

dos2unix /mnt/c/Users/Chris/Documents/Github/racecar-mn-windows/racecar-student/scripts/racecar_tool.sh
