#!/usr/bin/python3
from ..Screen.printScreen import printScreen
from ..Screen.screenAPI import getScreen
from ..Screen.screenAPI import setScreen

def modifyScreen( newBox ):
    screen = getScreen()
    i = newBox[1]
    while(i < newBox[3]):#loop over each horizontal row in the screen
        j = newBox[0]
        while(j < newBox[2]):#loop over each pixel in row i
            if(i == newBox[1] and newBox[0] <= j and j < newBox[2]):
                screen[i][j] = '||'
            if(j == newBox[0] and newBox[1] < i):
                screen[i][j] = '||'
            if(i+1 == newBox[3] and  newBox[0] <= j and j < newBox[2]):
                screen[i][j] = '||'
            if(newBox[2] == j+1 and newBox[1] <= i):
                screen[i][j] = '||'
            j = j + 1
        i = i + 1
    setScreen(screen)
    return