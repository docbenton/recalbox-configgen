#!/usr/bin/env python
import subprocess
import os

import videoMode

proc = None

# Set a specific video mode
def runCommand(command):
    global proc
    if command.videomode != 'default':
        videoMode.setVideoMode(command.videomode)
    command.env.update(os.environ)
    proc = subprocess.Popen(command.array, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=command.env)
    exitcode = -1
    try:
         out, err = proc.communicate()
         exitcode = proc.returncode
    except:
        print("emulator exited")

    if command.videomode != 'default':
        videoMode.setPreffered()

    return exitcode
