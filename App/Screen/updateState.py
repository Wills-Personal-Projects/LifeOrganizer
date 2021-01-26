#!/usr/bin/python3
from ..Screen.deleteScreen import deleteScreen
from ..Screen.savePreviousState import savePreviousState
from ..Path.filePaths import getPath
import os

def updateState(screen):
    
    if(os.stat(getPath(0)).st_size > 0):
        savePreviousState(screen)
    wState = open(getPath(0),"w")
    v = 0
    k = 0
    while( v < len(screen)):
        k = 0
        p = ''
        while (k < len(screen[v])):
            p = p + screen[v][k]
            k = k + 1
        wState.write(p + "\n")
        v = v + 1
    wState.close()