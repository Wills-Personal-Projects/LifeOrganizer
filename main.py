#!/usr/bin/python3
from App.Controllers.editController import editController
from App.Controllers.viewController import viewController
from App.Screen.screenSource import getScreen
from App.Screen.printScreen import printScreen

def main():
    print("a. edit")
    print("b. view")
    print("c. quit")
    choice = input("type a, b, or c: ")
    while(choice != "c"):
        if (choice == "a"):
            editController()
        else:
            viewController()
        print("a. edit")
        print("b. view")
        print("c. quit")
        choice = input("type a, b, or c: ")
    return
main()