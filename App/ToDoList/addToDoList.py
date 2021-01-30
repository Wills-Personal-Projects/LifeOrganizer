#!/usr/bin/python3
from ..Screen.modifyScreen import modifyScreen
from ..ToDoList.saveToDoList import saveToDoList
from ..Screen.screenSource import getScreen

def addToDoList(p):
    screen = getScreen()
    modifyScreen(p)#draw outer box on screen
    title = [" T"," O"," D"," O","  "," L"," I"," S"," T"]
    i = p[1]
    j = p[0]+1
    while(i < p[3]):#loop over each horizontal row in the screen
        j = p[0]+1
        while(j < p[2]):#loop over each pixel in row i
            if(len(title) > 0 and i == p[1]+1):
                screen[i][j] = title.pop(0)
            if(i == p[1] + 2):
                screen[i][j] = "~~"
            j = j + 1
        i = i + 1
        saveToDoList(p)
    return