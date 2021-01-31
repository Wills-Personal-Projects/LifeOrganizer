#!/usr/bin/python3
from App.Controllers.editController import editController
from App.Controllers.viewController import viewController

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