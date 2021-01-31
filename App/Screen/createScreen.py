#!/usr/bin/python3
from ..Screen.modifyScreen import modifyScreen
from ..Screen.deleteScreen import deleteScreen
from ..Screen.screenAPI import getScreenDim
from ..Screen.screenAPI import getScreen
from ..Screen.screenAPI import setScreen
from ..Path.filePaths import getPath

def createScreen(w, h):
    v = 0
    screen = []
    while(v < h):
        k = 0
        temp = []
        while(k < w):
            temp.append("..")
            k = k + 1
        screen.append(temp)
        v = v + 1
    setScreen(screen)
    return