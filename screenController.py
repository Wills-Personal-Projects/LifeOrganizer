#!/usr/bin/python3
from modifyScreen import modifyScreen
from createScreen import createScreen
from printScreen import printScreen

screenW = 0
screenH = 0
screen = []

def menu():
    print("\n")
    print("Life Organizer Editor")
    print("\n")
    print("a. define window size")
    print("b. add a box")
    print("c. remove a box")
    print("d. print the window")
    print("e. close program")
    print("\n")
    choice  = input("type a, b, c, d, or e: ")
    return choice

c = menu
while(c != "e"):
    if(c == "a"):
        print("\n")
        screenW = int(input("how wide?"))
        print("\n")
        screenH = int(input("how tall?"))
        screen = []
        createScreen(screen, screenW, screenH)
    elif(c == "b"):
        print("\n")
        l0 = int(input("how far from the left?"))
        print("\n")
        t0 = int(input("how far down from the top?"))
        print("\n")
        l1 = screenW - 1 - int(input("how far from the right?"))
        print("\n")
        t1 = screenH - 1 - int(input("how far up from the bottom?"))
        modifyScreen(screen, [l0, t0, l1, t1])
    elif(c == "d"):
        printScreen(screen)
    c = menu()




