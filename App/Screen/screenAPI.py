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
    w = int(dims[0])
    h = int(dims[1])
    i = 0
    j = 0
    wState = open(getPath(0),"r")
    while(i < h):
        j = 0
        row = []
        t = wState.readline()
        while(j < w*2):
            row.append(t[j]+t[j+1])
            j = j + 2
        s.append(row)
        i = i + 1
    wState.close()
    return s


def setScreen(s):
    dims = getScreenDim()
    w = int(dims[0])
    h = int(dims[1])
    wState = open(getPath(0),"w")
    v = 0
    while( v < h):
        k = 0
        row = ""
        while( k < w ):
            row = row + s[v][k]
            k = k + 1
        wState.write(row + "\n")
        v = v + 1
    wState.close()

def setScreenDim(d):
    dimsFile = open(getPath(4), "w")
    i = 0
    while(i < 2):
        dimsFile.write(str(d[i])+" ")
        i = i + 1
    dimsFile.close()