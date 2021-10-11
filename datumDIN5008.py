from genericpath import isdir, isfile
import os
import re

files = [f for f in os.listdir() if os.path.isdir(f) or os.path.isfile(f)]
for f in files:
    if ".py" in str(f) or ".mp3" in str(f):
        continue
    match = re.search("..\...\.....", str(f))
    if match != None:
        date = str(f)[match.start() : match.end()].split('.')
        newName = f"{str(f)[:match.start()]}{date[2]}-{date[1]}-{date[0]}{str(f)[match.end():]}"
        #print(newName)
        os.rename(f, newName)