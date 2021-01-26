#!/usr/bin/python3

def viewMenu():
    print("a. display to-do list")
    print("b. display calendar")
    print("c. quit")
    choice = input("type a or b: ") 
    return choice

def viewController():
    c = viewMenu()
    while(c != "c"):
        if(c == "a"):
            print("to-do list")
        elif(c == "b"):
            print("calender")
    return