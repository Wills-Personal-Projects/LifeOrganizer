#!/usr/bin/python3
from ..Path.filePaths import getPath

def saveToDo(dim, tasks):
    toDoFile = open(getPath(2), "w")
    i = 0
    while(i < 4):
        toDoFile.write(str(dim[i])+".")
        i = i + 1
    i = 0
    toDoFile.write("\n")
    while(i < len(tasks)):
        j = 0
        while(j < len(tasks[i])):
            toDoFile.write(tasks[i][j])
            j = j + 1
        toDoFile.write("\n")
        i = i + 1
    toDoFile.close()
    return