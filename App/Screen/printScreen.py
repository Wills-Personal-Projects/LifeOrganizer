#!/usr/bin/python3
from ..Path.filePaths import getPath
from ..Screen.screenSource import getScreenDim

def printScreen():
    sH = int(getScreenDim()[1])
    wState = open(getPath(0),"r")
    v = 0
    while( v < sH ):
        print(wState.readline().rstrip())
        v = v + 1
    wState.close()