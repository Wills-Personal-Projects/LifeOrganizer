#!/usr/bin/python3

def getScreenPath( name ):
    state0 = "App/Data/currentWindowState.txt"
    state1 = "App/Data/previousWindowState.txt"
    state2 = "App/Data/currentWindowDim.txt"

    if(name == 0):
        return state0
    elif(name == 1):
        return state1
    elif(name == 2):
        return state2
    else:
        return "no path"

def getBaseToDoPath():
    return "App/Data/TodoLists/"

def getToDoPath( name ):
    TDLists = open("App/Data/TDListsNames.txt", "r")
    names = TDLists.readlines()
    TDLists.close()
    for na in names:
        if(na.rstrip() == name):
            return "App/Data/TodoLists/"+name+".txt"

def getNamesPath():
    return "App/Data/TDListsNames.txt"

def getNumTDL( name ):
    numPath = "App/Data/numTDLists.txt"

    if(name == 0):
        return numPath
    else:
        return "no path"

