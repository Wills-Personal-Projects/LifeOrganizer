#!/usr/bin/python3
from ..Path.filePaths import getPath

def addToDo( tD ):
    toDo = list(tD)
    print(toDo)
    toDoFile = open(getPath(2), "a")
    i = 0
    while (i < len(toDo)):
        toDoFile.write(toDo[i]+" ")
        i = i + 1
    toDoFile.write("\n")
    toDoFile.close()
    return

def editToDoList():
    c = ''
    while (c != 'b'):
        print("a. add to-do")
        print("b. exit")
        c = input("enter a or b")
        if(c == 'a'):
            addToDo(input("what is the to-do?"))
    return