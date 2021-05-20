# python pythonsearch.py <searchstring> [startingdir]

import os
import sys


def filecontains(filename, searchstring):
    with open(filename, "rt") as f:
        return f.read().find(searchstring) >= 0


# If dir not given then take current directory
if len(sys.argv) < 3:
    startdir = os.getcwd()
else:
    startdir = sys.argv[2]

# Search string
searchstring = sys.argv[1]

allfiles = os.walk(startdir)
for (dirname, dirs, files) in allfiles:
    for filename in files:
        fullname = dirname + "\\" + filename
        if filename.endswith(".py"):
            if filecontains(fullname, searchstring):
                print(fullname)
