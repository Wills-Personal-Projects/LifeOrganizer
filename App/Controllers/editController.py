#!/usr/bin/python3
from ..Screen.modifyScreen import modifyScreen
from ..Screen.createScreen import createScreen
from ..Screen.printScreen import printScreen
from ..Screen.undoAddBox import undoAddBox
from ..ToDoList.addToDoList import addToDoList
from ..ToDoList.editToDoList import editToDoList
from ..Screen.screenAPI import getScreenDim
from ..Screen.screenAPI import setScreenDim
    
def editController():
    c = ""
    #print("\n")
    #w = int(input("how wide is this window?"))
    #print("\n")
    #h = int(input("how tall is this window?"))
    w = 60
    h = 20
    setScreenDim([w,h])
    dims = getScreenDim()
    sH = int(dims[1])
    sW = int(dims[0])
    createScreen(sW, sH)
    modifyScreen([0,0,w,h])
    while(c != "f"):
        print("\n")
        print("Life Organizer Editor")
        print("\n")
        print("a. create to-do list")
        print("b. edit to-do list")
        print("c. create calendar")
        print("d. add task to calendar")
        print("e. window preview")
        print("f. close program")
        print("\n")
        c  = input("type a, b, c, d, e, or f: ")
        if(c == "a"):
            l0 = int(input("how far from the left is the to-do list?"))
            print("\n")
            t0 = int(input("how far down from the top is the to-do list?"))
            print("\n")
            l1 = sW - int(input("how far from the right is the to-do list?"))
            print("\n")
            t1 = sH - int(input("how far up from the bottom is the to-do list?"))
            modifyScreen([l0, t0, l1, t1])
            addToDoList([l0, t0, l1, t1])
        elif(c == "b"):
             editToDoList()
        elif(c == "c"):
            print("calendar")
        elif(c == "d"):
            print("add task to calendar")
        elif(c == "e"):
            printScreen()
    return