#!/usr/bin/python3
from ..Screen.printScreen import printScreen

def modifyScreen( screen , newBox):
    i = 0
    j = 0
    while(i < len(screen)):#loop over each horizontal row in the screen
        j = newBox[0]
        while(j <= newBox[2]):#loop over each pixel in row i
            if(newBox[1] == i and newBox[0] <= j and j <= newBox[2]):
                screen[i][j] = '||'
            if(newBox[0] == j and newBox[1] < i and i < newBox[3]):
                screen[i][j] = '||'
            if(newBox[3] == i and  newBox[0] <= j and j <= newBox[2]):
                screen[i][j] = '||'
            if(newBox[2] == j and newBox[1] < i and i < newBox[3]):
                screen[i][j] = '||'
            j = j + 1
        i = i + 1