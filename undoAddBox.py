#!/usr/bin/python3

def undoAddBox(screen):
    wState = open("LifeOrganizer_pkg/currentWindowState.txt","r+")
    wState.truncate(0)
    wState.close()
    wPreState = open("LifeOrganizer_pkg/previousWindowState.txt","r")
    wState = open("LifeOrganizer_pkg/currentWindowState.txt","w")
    v = 0
    while (v < len(screen)):
        p = wPreState.readline().rstrip()
        wState.write(p + "\n")
        v = v + 1
    wState.close()
    wPreState.close()
    return