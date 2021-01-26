#!/usr/bin/python3
from ..Path.filePaths import getPath

def undoAddBox(screen):
    wState = open(getPath(0),"r+")
    wState.truncate(0)
    wState.close()
    wPreState = open(getPath(1),"r")
    wState = open(getPath(0),"w")
    v = 0
    while (v < len(screen)):
        p = wPreState.readline().rstrip()
        wState.write(p + "\n")
        v = v + 1
    wState.close()
    wPreState.close()
    return