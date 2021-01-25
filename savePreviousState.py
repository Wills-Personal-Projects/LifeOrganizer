#!/usr/bin/python3

def savePreviousState(screen):
    wPreState = open("editStates/previousWindowState.txt","w")
    wState = open("editStates/currentWindowState.txt","r")
    v = 0
    while (v < len(screen)):
        p = wState.readline().rstrip()
        wPreState.write(p + "\n")
        v = v + 1
    wState.close()
    wPreState.close()
    