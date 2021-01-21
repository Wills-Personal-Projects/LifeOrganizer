#!/usr/bin/python3

def savePreviousState(screen):
    wPreState = open("LifeOrganizer_pkg/previousWindowState.txt","w")
    wState = open("LifeOrganizer_pkg/currentWindowState.txt","r")
    v = 0
    while (v < len(screen)):
        p = wState.readline().rstrip()
        wPreState.write(p + "\n")
        v = v + 1
    wState.close()
    wPreState.close()
    