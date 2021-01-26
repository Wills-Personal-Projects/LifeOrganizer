#!/usr/bin/python3
from ..Path.filePaths import getPath

def printScreen(screen):
    wState = open(getPath(0),"r")
    v = 0
    while( v < len(screen)):
        print(wState.readline().rstrip())
        v = v + 1
    wState.close()