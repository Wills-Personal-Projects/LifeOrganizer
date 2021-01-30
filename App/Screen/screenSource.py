#!/usr/bin/python3
from ..Path.filePaths import getPath

def getScreenDim():
    cDimFile = open(getPath(4), "r")
    dims = cDimFile.readline().rstrip().split(" ")
    cDimFile.close()
    return dims

def getScreen():
    s = []
    dims = getScreenDim()
    wState = open(getPath(0),"r")
    v = 0
    while( v < int(dims[1])):
        k = 0
        temp = []
        while( k < int(dims[0]) ):
            temp.append(wState.read(2))
            k = k + 1
        s.append(temp)
        v = v + 1
    wState.close()
    return s


def setScreen(s):
    return

def setScreenDim(d):
    dimsFile = open(getPath(4), "w")
    i = 0
    while(i < 2):
        dimsFile.write(str(d[i])+" ")
        i = i + 1