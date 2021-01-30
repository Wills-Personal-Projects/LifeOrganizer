from ..ToDoList.addToDo import addToDo
from ..Screen.screenSource import getScreen

def editToDoList():
    screen = getScreen()
    c = ''
    while (c != 'b'):
        print("a. add to-do")
        print("b. exit")
        c = input("enter a or b")
        if(c == 'a'):
            addToDo(screen, list(input("what is the todo?")))
    return