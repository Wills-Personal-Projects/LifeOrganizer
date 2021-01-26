#!/usr/bin/python3
from ..Path.filePaths import getPath

def savePreviousState(screen):
    wPreState = open(getPath(1),"w")
    wState = open(getPath(0),"r")
    v = 0
    while (v < len(screen)):
        p = wState.readline().rstrip()
        wPreState.write(p + "\n")
        v = v + 1
    wState.close()
    wPreState.close()
    