#!/usr/bin/python3
from ..Screen.modifyScreen import modifyScreen
from ..Screen.createScreen import createScreen
from ..Screen.printScreen import printScreen
from ..Screen.undoAddBox import undoAddBox
from ..Screen.updateState import updateState
from ..ToDoList.addToDoList import addToDoList
from ..ToDoList.editToDoList import editToDoList
    
def editController(screen, screenW, screenH):
    c = ""
    while(c != "f"):
        if(len(screen) > 0):
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
            screenW = int(input("how wide is this window?"))
            print("\n")
            screenH = int(input("how tall is this window?"))
            createScreen(screen, screenW, screenH)
            modifyScreen(screen, [0, 0, screenW-1, screenH-1])
            updateState(screen)
        if(c == "a"):
            l0 = int(input("how far from the left is the to-do list?"))
            print("\n")
            t0 = int(input("how far down from the top is the to-do list?"))
            print("\n")
            l1 = (screenW - 1) - int(input("how far from the right is the to-do list?"))
            print("\n")
            t1 = (screenH - 1) - int(input("how far up from the bottom is the to-do list?"))
            print(l0)
            addToDoList(screen, [l0, t0, l1, t1])
            updateState(screen)
        elif(c == "b"):
             editToDoList()
        elif(c == "c"):
            l0 = int(input("how far from the left is the calendar?"))
            print("\n")
            t0 = int(input("how far down from the top is the calendar?"))
            print("\n")
            l1 = screenW - 1 - int(input("how far from the right is the calendar?"))
            print("\n")
            t1 = screenH - 1 - int(input("how far up from the bottom is the calendar?"))
            modifyScreen(screen, [l0, t0, l1, t1])
            updateState(screen)
        elif(c == "d"):
            print("add task to calendar")
        elif(c == "e"):
            printScreen(screen)
    return