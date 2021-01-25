#!/usr/bin/python3

def printScreen(screen):
    wState = open("editStates/currentWindowState.txt","r")
    v = 0
    while( v < len(screen)):
        print(wState.readline().rstrip())
        v = v + 1
    wState.close()