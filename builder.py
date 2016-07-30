#! /usr/bin/env python3
import os

for file in os.listdir():
    if file.endswith(".ui"):
        os.system("pyuic4 %s.ui -o %s.py" % (os.path.splitext(file)[0], os.path.splitext(file)[0]))
