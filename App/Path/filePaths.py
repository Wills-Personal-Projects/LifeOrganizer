#!/usr/bin/python3
def getPath( name ):
    state0 = "App/EditStates/currentWindowState.txt"
    state1 = "App/EditStates/previousWindowState.txt"
    state2 = "App/EditStates/currentWindowDim.txt"
    view0 = "App/Views/todolist.txt"
    view1 = "App/Views/calendar.txt"
    if(name == 0):
        return state0
    elif(name == 1):
        return state1
    elif(name == 2):
        return view0
    elif(name == 3):
        return view1
    else:
        return state2
