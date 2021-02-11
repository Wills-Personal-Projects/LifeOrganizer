#!/usr/bin/python3
from ..Path.filePaths import getScreenPath, getToDoPath, getBaseToDoPath, getNamesPath
from ..Screen.screenAccess import getScreen,setScreen

def getToDoListDim(n):
    tDListFile = open(getToDoPath(n), "r")
    dim = tDListFile.readline().rstrip().split()
    return dim

def getToDoList(n):
    tDListFile = open(getToDoPath(n), "r")
    dim = tDListFile.readline().rstrip()
    numTD = int(tDListFile.readline())
    i = 0
    tDL = []
    while(i < numTD):
        tD = list(tDListFile.readline().rstrip())
        tDL.append([])
        j = 0
        while(j < len(tD)):
            tDL[i].append(tD[j])
            j = j + 1
        i = i + 1
    tDListFile.close()
    return tDL

def setToDoList(n, t, add):
    tDListFile = open(getToDoPath(n), "r")
    dim = tDListFile.readline().rstrip()
    numTD = int(tDListFile.readline())
    tDListFile.close()
    tDListFile = open(getToDoPath(n), "w")
    tDListFile.write(dim+"\n")
    if(add):
        tDListFile.write(str(numTD+1)+"\n")
    else:
        tDListFile.write(str(numTD-1)+"\n")
    i = 0 
    while(i < len(t)):
        tD = ''.join(t[i])
        tDListFile.write(tD+"\n")
        i = i + 1
    tDListFile.close()
    return

def saveToDoList(dim, name):
    nameList = open(getNamesPath(), "a")
    nameList.write(name+"\n")
    nameList.close()
    toDoFile = open(getBaseToDoPath()+name+".txt", "w")
    i = 0
    while(i < 4):
        toDoFile.write(str(dim[i])+" ")
        i = i + 1
    toDoFile.write("\n")
    toDoFile.write("0")
    toDoFile.close()
    return
