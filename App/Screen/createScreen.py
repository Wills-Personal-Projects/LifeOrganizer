#!/usr/bin/python3
from ..Screen.modifyScreen import modifyScreen
from ..Screen.deleteScreen import deleteScreen
from ..Screen.screenSource import getScreenDim
from ..Screen.screenSource import setScreen
from ..Path.filePaths import getPath

def createScreen():
    dims = getScreenDim()
    sH = int(dims[1])
    sW = int(dims[0])
    wState = open(getPath(0), "w")
    v = 0
    k = 0
    while( v < sH):
        k = 0
        temp = ""
        while (k < sW):
            temp = temp + '..'
            k = k + 1
        wState.write(temp + "\n")    
        v = v + 1
    wState.close()
    return