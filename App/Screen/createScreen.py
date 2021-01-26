#!/usr/bin/python3
from ..Screen.modifyScreen import modifyScreen
from ..Screen.deleteScreen import deleteScreen

def createScreen(screen, sW, sH):
    deleteScreen()
    v = 0
    k = 0
    while( v < sH):
        k = 0
        temp = []
        while (k < sW):
            temp.append('..')
            k = k + 1
        screen.append(temp)    
        v = v + 1
    return