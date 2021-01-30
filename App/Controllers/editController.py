#!/usr/bin/python3
from ..Screen.modifyScreen import modifyScreen
from ..Screen.createScreen import createScreen
from ..Screen.printScreen import printScreen
from ..Screen.undoAddBox import undoAddBox
from ..Screen.updateState import updateState
from ..ToDoList.addToDoList import addToDoList
from ..ToDoList.editToDoList import editToDoList
from ..Screen.screenSource import getScreenDim
from ..Screen.screenSource import setScreenDim
    
def editController():
    c = ""
    while(c != "f"):
        dims = getScreenDim()
        sH = int(dims[1])
        sW = int(dims[0])
        if(sH > 0):
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
        else:
            print("\n")
            w = int(input("how wide is this window?"))
            print("\n")
            h = int(input("how tall is this window?"))
            setScreenDim([w,h])
            createScreen()
            modifyScreen([0, 0, w-1, h-1])
        if(c == "a"):
            l0 = int(input("how far from the left is the to-do list?"))
            print("\n")
            t0 = int(input("how far down from the top is the to-do list?"))
            print("\n")
            l1 = (sW - 1) - int(input("how far from the right is the to-do list?"))
            print("\n")
            t1 = (sH - 1) - int(input("how far up from the bottom is the to-do list?"))
            print(l0)
            addToDoList([l0, t0, l1, t1])
        elif(c == "b"):
             editToDoList()
        elif(c == "c"):
            l0 = int(input("how far from the left is the calendar?"))
            print("\n")
            t0 = int(input("how far down from the top is the calendar?"))
            print("\n")
            l1 = sW - 1 - int(input("how far from the right is the calendar?"))
            print("\n")
            t1 = sH - 1 - int(input("how far up from the bottom is the calendar?"))
            modifyScreen([l0, t0, l1, t1])
        elif(c == "d"):
            print("add task to calendar")
        elif(c == "e"):
            printScreen()
    return