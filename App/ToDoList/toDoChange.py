#!/usr/bin/python3
from ..ToDoList.toDoAccess import getToDoList, setToDoList, saveToDoList, getToDoListDim
from ..Screen.screenAccess import getScreen, setScreen
from ..Screen.screenChange import modifyScreen


def addToDo(n, tD ):
    tDList = getToDoList(n)
    #add todo to todo list n
    tDList.append(tD)
    setToDoList(n, tDList, True)
    addToScreen(n, tDList)
    return

def removeToDo( n, i ):
    tDList = getToDoList(n)
    #remove todo at i from todo list n
    tDList.pop(i-1)
    setToDoList(n, tDList, False)
    addToScreen(n, tDList)
    return

def addToScreen(n, tDList):
    screen = getScreen()
    dim = getToDoListDim(n)
    x0 = int(dim[0])
    y0 = int(dim[1])
    x1 = int(dim[2])
    y1 = int(dim[3])
    i = y0 + 3
    while(i < (y1-1)):
        j = x0 + 1
        tD = []
        if(len(tDList) > 0):
            tD = tDList.pop(0)
        while(j < (x1-1)):
            if(len(tD) > 0):
                screen[i][j] = " " + tD.pop(0)
            else:
                screen[i][j] = ".."
            j = j + 1
        i = i + 1
    setScreen(screen)
    return

def addToDoList(p, name):
    modifyScreen(p)
    screen = getScreen()
    title = list(name)
    i = p[1]
    while(i < p[3]):#loop over each horizontal row in the screen
        j = p[0]
        while(j < p[2]):#loop over each pixel in row i
            if(len(title) > 0 and i == p[1]+1):
                screen[i][j+1] = " " + title.pop(0)
                screen[i+1][j+1] = "~~"
            j = j + 1
        i = i + 1
    saveToDoList(p, name)
    setScreen(screen)
    return