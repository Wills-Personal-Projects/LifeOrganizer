#!/usr/bin/python3
def deleteScreen():
    eraseFile = open("editStates/currentWindowState.txt","r+")
    eraseFile.truncate(0)
    eraseFile.close()
    eraseFile = open("editStates/previousWindowState.txt","r+")
    eraseFile.truncate(0)
    eraseFile.close()
    return