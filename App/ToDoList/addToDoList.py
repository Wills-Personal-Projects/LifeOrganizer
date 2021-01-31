#!/usr/bin/python3
from ..Screen.modifyScreen import modifyScreen
from ..ToDoList.saveToDoList import saveToDoList
from ..Screen.screenAPI import getScreen
from ..Screen.screenAPI import setScreen

def addToDoList(p):
    screen = getScreen()
    title = [" T"," O"," D"," O","  "," L"," I"," S"," T"]
    i = p[1]
    while(i < p[3]):#loop over each horizontal row in the screen
        j = p[0]
        while(j < p[2]):#loop over each pixel in row i
            if(len(title) > 0 and i == p[1]+1):
                screen[i][j+1] = title.pop(0)
            j = j + 1
        i = i + 1
        saveToDoList(p)
    setScreen(screen)
    return