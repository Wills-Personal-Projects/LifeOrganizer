#!/usr/bin/python3
def getPath( name ):
    state0 = "editStates/currentWindowState.txt"
    state1 = "editStates/previousWindowState.txt"
    view0 = "views/todolist.txt"
    view1 = "views/calendar.txt"
    if(name == 0):
        return state0
    elif(name == 1):
        return state1
    elif(name == 2):
        return view0
    else:
        return view1
