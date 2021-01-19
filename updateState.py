#!/usr/bin/python3
from deleteScreen import deleteScreen

def updateState(screen):
    deleteScreen()
    wState = open("LifeOrganizer_pkg/currentWindowState.txt","w")
    v = 0
    k = 0
    while( v < len(screen)):
        k = 0
        p = ''
        while (k < len(screen[v])):
            p = p + screen[v][k]
            k = k + 1
        wState.write(p+"\n")
        v = v + 1
    wState.close()