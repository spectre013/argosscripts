#!/usr/bin/env python3
#https://github.com/p-e-w/argos
import os.path
import os
from os.path import expanduser

home = expanduser("~")
print("Tilix\n---")
session_dir = home+'/tilix-spaces/'
dirs = [d for d in os.listdir(session_dir) if os.path.isdir(os.path.join(session_dir, d))]
for dir in dirs:
    print(dir)
    scripts_path = os.path.join(session_dir,dir)
    for file in os.listdir(scripts_path):
        if file.endswith(".json"):
            config = os.path.join(scripts_path, file)
            name = file.replace(".json","")
            print("--{0} | useMarkup=false iconName=tilix bash='/usr/bin/tilix --session {1}' terminal=false".format(name, config))