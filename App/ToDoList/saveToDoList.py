#!/usr/bin/python3
from ..Path.filePaths import getPath

def saveToDoList(dim):
    toDoFile = open(getPath(2), "w")
    i = 0
    while(i < 4):
        toDoFile.write(str(dim[i])+" ")
        i = i + 1
    toDoFile.write("\n")
    toDoFile.write("0")
    toDoFile.close()
    return