"""
MIT BWSI Autonomous RACECAR
MIT License
bwsix RC101 - Fall 2023

File Name: setup.py

Title: RACECAR Setup Python File

Author: Christopher Lai (MITLL)

Purpose: To streamline setup process for native RACECAR version.
Asks user for information about system (absolute path, IP address,
operating system), then creates configuration file, downlaods
libraries, and sets up RACECAR command in environment.
"""

import os
import subprocess

# [VARIABLES]
op_sys = "" # Operating system for user
abs_path = "" # Absolute path for user
ip_addr = "" # IP Address used (127.0.0.1 default)

config_command = ""
tool_command = ""
lib_command = ""

# [USER INPUT LOGIC]
op_sys = input("Enter operating system (Windows, Mac, Linux): ")
ip_addr = input("Enter IP Address (leave blank if unknown): ")

# [CHECK IP]
if not ip_addr:
    ip_addr = "127.0.0.1"

# [ABS PATH WIN -> LINUX]
if op_sys.lower() == "windows":
    abs_path = os.path.dirname(os.path.abspath(__file__))
    linux_path = os.path.dirname(abs_path)
elif op_sys.lower() == "mac":
    print("NaN")
elif op_sys.lower() == "linux":
    print("NaN")
else:
    print("Invalid Input.")

# [USER CONFIRMATION]
print("\nIs this information correct?\n=============================")
print(f"Operating System: {op_sys.capitalize()}")
print(f"IP Address: {ip_addr}")
confirm = input("Confirm (Y/N): ")

if confirm.lower() == "y":
    config_command = f"""echo "RACECAR_ABSOLUTE_PATH=\\"{linux_path}\\"
RACECAR_IP=\\"{ip_addr}\\"
RACECAR_TEAM=\\"student\\"
RACECAR_CONFIG_LOADED=\\"TRUE\\"
export DISPLAY=localhost:42.0" > {linux_path}/scripts/.config"""

    tool_command = f"""sed '/# RACECAR_ALIASES$/d' -i ~/.bashrc
echo "# Source RACECAR tool # RACECAR_ALIASES
if [ -f {linux_path}/scripts/.config ]; then # RACECAR_ALIASES
. {linux_path}/scripts/.config # RACECAR_ALIASES
fi # RACECAR_ALIASES
if [ -f {linux_path}/scripts/racecar_tool.sh ]; then # RACECAR_ALIASES
. {linux_path}/scripts/racecar_tool.sh # RACECAR_ALIASES
fi # RACECAR_ALIASES" >> ~/.bashrc"""
    
    lib_command = f"""yes | apt-get update
yes | apt-get upgrade
yes | apt install python3-pip
yes | pip install -r {linux_path}/scripts/requirements.txt
yes | apt install jupyter-notebook
yes | apt-get install ffmpeg libsm6 libxext6 -y
yes | apt-get install dos2unix
"""

    print(f"Library Command: \n{lib_command}\n")
    print(f"\nConfig Command: \n{config_command}\n")
    print(f"Tool Command: \n{tool_command}\n")
    print("\nCreating Setup Script File...")

    script_file = f"""#!/bin/sh

{lib_command}
"""

    with open('libinstall.sh', 'w') as w:
        w.write(script_file)

    script_file = f"""#!/bin/sh
    
{config_command}

{tool_command}

dos2unix {linux_path}/scripts/racecar_tool.sh
"""

    with open('setup.sh', "w") as w:
        w.write(script_file)

    confirm2 = input("Script Finished. Run RACECAR Library Installation Script? (Y/N): ")

    if confirm2.lower() == "y":
        subprocess.run(["sh", 'libinstall.sh'])
    else:
        print("\nAuto script running denied. To run the setup script, cd into the scripts folder using:")
        print(f"cd {linux_path}/scripts")
        print("Then run [sh libinstall.sh] in the terminal.\n")

    confirm3 = input("Script Finished. Run RACECAR Setup Script? (Y/N): ")

    if confirm3.lower() == "y":
        subprocess.run(["sh", 'setup.sh'])
    else:
        print("\nAuto script running denied. To run the setup script, cd into the scripts folder using:")
        print(f"cd {linux_path}/scripts")
        print("Then run [sh setup.sh] in the terminal. Goodbye.\n")
    
else:
    print("Setup aborted. Goodbye.")