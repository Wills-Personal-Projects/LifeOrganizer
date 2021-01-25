#!/usr/bin/python3

def undoAddBox(screen):
    wState = open("editStates/currentWindowState.txt","r+")
    wState.truncate(0)
    wState.close()
    wPreState = open("editStates/previousWindowState.txt","r")
    wState = open("editStates/currentWindowState.txt","w")
    v = 0
    while (v < len(screen)):
        p = wPreState.readline().rstrip()
        wState.write(p + "\n")
        v = v + 1
    wState.close()
    wPreState.close()
    return