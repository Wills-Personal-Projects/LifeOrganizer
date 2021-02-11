#!/usr/bin/python3
from ..Screen.screenAccess import getScreen, getScreenDim

def printScreen():
    dims = getScreenDim()
    w = int(dims[0])
    h = int(dims[1])
    screen = getScreen()
    v = 0
    while( v < h ):
        k = 0
        row = ""
        while( k < w ):
            row = row + screen[v][k]
            k = k + 1
        print(row)
        v = v + 1