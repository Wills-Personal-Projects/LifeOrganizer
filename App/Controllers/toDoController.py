from ..ToDoList.toDoChange import addToDo, removeToDo, addToDoList, removeToDoList
from ..Screen.screenAccess import getScreenDim

def toDoController():
    dims = getScreenDim()
    w = int(dims[0])
    h = int(dims[1])
    c = ''
    while (c != 'e'):
        print("a. create a to-do list")
        print("b. add to-do")
        print("c. remove to-do")
        print("d. remove to-do list")
        print("e. exit")
        c = input("enter a, b, c, d or e: ")
        if(c == 'a'):
            x0 = int(input("how far from the left is the to-do list?: "))
            y0 = int(input("how far from the top is the to-do list?: "))
            x1 = w - int(input("how far from the right is the to-do list?: "))
            y1 = h - int(input("how far from the bottom is the to-do list?: "))
            name = input("what is the name of this to-do list? ")
            addToDoList([x0, y0, x1, y1], name)
        if(c == 'b'):
            n = input("enter the name of the to-do list: ")
            addToDo(n, list(input("what is the todo?")))
        if(c == 'c'):
            n = input("enter the name of the to-do list: ")
            print("which todo?")
            sc = input("enter integer 1 or 2 or 3 or ... or n where n > 0: ")
            removeToDo(n, int(sc))
        if(c == 'd'):
            n = input("enter the name of the to-do list: ")
            removeToDoList(n)
    return