#!/usr/bin/python3
def deleteScreen():
    eraseFile = open("LifeOrganizer_pkg/currentWindowState.txt","r+")
    eraseFile.truncate(0)
    eraseFile.close()
    eraseFile = open("LifeOrganizer_pkg/previousWindowState.txt","r+")
    eraseFile.truncate(0)
    eraseFile.close()
    return