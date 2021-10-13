from genericpath import isdir, isfile
from ntpath import join
from send2trash import send2trash
import os
import re



currentPath = os
files = [f for f in currentPath.listdir() if currentPath.path.isdir(f) or currentPath.path.isfile(f)]
for f in files:
    if ".py" in str(f) or ".mp3" in str(f):
        continue
    match = re.search("..\...\.....", str(f))
    if match != None:
        filePath = join(str(currentPath.path.curdir), f)
        date = str(f)[match.start() : match.end()].split('.')
        newName = f"{str(f)[:match.start()]}{date[2]}-{date[1]}-{date[0]}{str(f)[match.end():]}"
        newFilePath = join(str(currentPath.path.curdir), newName)
        if(currentPath.path.exists(newFilePath)):
            print(send2trash(f))
            continue
        os.rename(f, newName)