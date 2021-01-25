#!/usr/bin/python3
from modifyScreen import modifyScreen
from saveToDo import saveToDo

def addToDoList(screen, p):
    modifyScreen(screen, p)#draw outer box on screen
    title = [" T"," O"," D"," O","  "," L"," I"," S"," T"]
    tasks = [[" t"," a"," s"," k","  "," h"," e"," r"," e"]]
    i = p[1]
    j = p[0]+1
    while(i < p[3]):#loop over each horizontal row in the screen
        j = p[0]+1
        while(j < p[2]):#loop over each pixel in row i
            if(len(title) > 0 and i == p[1]+1):
                screen[i][j] = title.pop(0)
            elif(i == p[1]+1):
                screen[i][j] = "<>"
            if(i == p[1] + 2):
                screen[i][j] = "--"
            if(len(tasks[0]) > 0 and i == p[1] + 3):
                screen[i][j] = tasks[0].pop(0)
            elif(i == p[1]+3):
                screen[i][j] = "<>"
            if(i == p[1] + 4):
                screen[i][j] = "--"
            j = j + 1
        i = i + 1
        tasks = [[" t"," a"," s"," k","  "," h"," e"," r"," e"]]
        saveToDo(p, tasks)
    return