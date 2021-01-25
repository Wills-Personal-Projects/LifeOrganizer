#!/usr/bin/python3
from deleteScreen import deleteScreen
from savePreviousState import savePreviousState
import os

def updateState(screen):
    
    if(os.stat("editStates/currentWindowState.txt").st_size > 0):
        savePreviousState(screen)
    wState = open("editStates/currentWindowState.txt","w")
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