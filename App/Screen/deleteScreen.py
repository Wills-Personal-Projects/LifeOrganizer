#!/usr/bin/python3
from ..Path.filePaths import getPath

def deleteScreen():
    eraseFile = open(getPath(0),"r+")
    eraseFile.truncate(0)
    eraseFile.close()
    eraseFile = open(getPath(1),"r+")
    eraseFile.truncate(0)
    eraseFile.close()
    return