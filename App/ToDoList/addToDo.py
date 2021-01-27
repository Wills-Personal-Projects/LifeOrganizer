#!/usr/bin/python3
from ..Path.filePaths import getPath

def addToDo( screen, tD ):
    toDoFile = open(getPath(2), "r")
    contents = toDoFile.readlines()
    toDoFile.close()
    toDoLoc = contents[0].rstrip().split(" ")
    numToDos = int(contents[1])
    contents[1] = str(numToDos+1)
    toDoFile = open(getPath(2), "w")
    toDoFile.writelines(contents)
    toDoFile.close()
    i = int(toDoLoc[1])+1
    j = int(toDoLoc[0])+1
    while (i < int(toDoLoc[3])):
        if(screen[i][j] == ".."):
            screen[i][j] = str(numToDos+1)+" "
            j = j + 1
            while(j < int(toDoLoc[2])):
                if(len(tD) > 0):
                    screen[i][j] = tD.pop(0) + " "
                j = j + 1
        i = i + 1     
    return