#!/usr/bin/python

import os
import subprocess
import sys
import shutil

garbage_list = [
    "/var/log/journal/",
    "/var/cache/akmods/nvidia"
]

commands = [
    "sudo dnf clean all",
    "sudo dnf system-upgrade clean",
    "flatpak uninstall --unused",
    "sudo dnf autoremove"
]

def du(path):
    return int(subprocess.check_output(['du','-s', path]).split()[0].decode('utf-8'))

def list_garbage():
    sum = 0
    for item in garbage_list:
        size = du(item)
        sum += size
        print(item, size)
    print(f"TOTAL OF {len(garbage_list)} FILES CONTAINING {sum/1000}MB OF DATA")

def remove_garbage():
    for item in garbage_list:
        for subitem in os.listdir(item):
            absolute = os.path.join(item, subitem)
            if os.path.isdir(absolute):
                shutil.rmtree(absolute)
            if os.path.isfile(absolute):
                os.remove(absolute)

def run_commands():
    for command in commands:
        print(f"Running command '{command}:'")
        subprocess.call(command.split(" "))

if __name__ == "__main__":
    list_garbage()

    if len(sys.argv) > 1 and sys.argv[len(sys.argv)-1] == "clean":
        remove_garbage()
        run_commands()

