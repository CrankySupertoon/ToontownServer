# A python script that will run as a .exe that will start the server for a windows based OS
import subprocess
import os
import main

# Change directory to where the .bat files reside
backendDir = os.chdir("dev/backend/")

# Begin a flag that will put all the .bat files into a single terminal
SW_HIDE = 0
info = subprocess.STARTUPINFO()

info.dwFlags = subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = SW_HIDE

# Opens the .bats
subprocess.Popen(r"start-astron-cluster.bat", startupinfo = info)
subprocess.Popen(r"start-ai-server.bat", startupinfo = info)
subprocess.Popen(r"start-uberdog-server.bat", startupinfo = info)
