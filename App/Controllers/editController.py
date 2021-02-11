#!/usr/bin/python3
from ..Screen.screenChange import modifyScreen, createScreen
from ..Screen.printScreen import printScreen
from ..Screen.screenAccess import getScreenDim, setScreenDim
from ..Controllers.toDoController import toDoController
    
def editController():
    c = ""
    w = 0
    h = 0
    while(c != "f"):
        print("\n")
        print("Life Organizer Editor")
        print("\n")
        print("a. create main window")
        print("b. add/remove/edit to-do list")
        print("c. create calendar")
        print("d. add task to calendar")
        print("e. window preview")
        print("f. exit")
        print("\n")
        c  = input("type a, b, c, d, e, or f: ")
        if(c == "a"):
            dims = getScreenDim()
            if(int(dims[0]) == 0 and int(dims[1]) == 0):
                w = int(input("how wide is the window? "))
                h = int(input("how tall is the window? "))
                setScreenDim([w,h])
                createScreen(w, h)
                modifyScreen([0,0,w,h])
            else:
                print("do you want to replace the previous window?")
                r = input("type yes or no: ")
                if(r == "yes"):
                    w = int(input("how wide is the window? "))
                    h = int(input("how tall is the window? "))
                    setScreenDim([w,h])
                    createScreen(w, h)
                    modifyScreen([0,0,w,h])
        elif(c == "b"):
            dims = getScreenDim()
            if(int(dims[0]) > 0 and int(dims[1]) > 0):
                toDoController()
            else:
                print("create main window first")
        elif(c == "c"):
            print("calendar")
        elif(c == "d"):
            print("add task to calendar")
        elif(c == "e"):
            printScreen()
    return