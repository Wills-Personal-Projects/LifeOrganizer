#!/usr/bin/python3
from editController import editController
from viewController import viewController

def init():
    screen = []
    screenW = 0
    screenH = 0
    print("a. edit")
    print("b. view")
    print("c. quit")
    choice = input("type a, b, or c: ")
    while(choice != "c"):
        if (choice == "a"):
            editController(screen, screenW, screenH)
        else:
            viewController()
        print("a. edit")
        print("b. view")
        print("c. quit")
        choice = input("type a, b, or c: ")
init()