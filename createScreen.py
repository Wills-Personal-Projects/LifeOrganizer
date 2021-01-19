#!/usr/bin/python3
from modifyScreen import modifyScreen
from deleteScreen import deleteScreen

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
    modifyScreen(screen, [0, 0, sW-1, sH-1])