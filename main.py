from App.Controllers.editController import editController
from App.Controllers.viewController import viewController

def main():
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
    return
main()