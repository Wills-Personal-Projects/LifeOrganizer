from ..ToDoList.addToDo import addToDo

def editToDoList(screen):
    c = ''
    while (c != 'b'):
        print("a. add to-do")
        print("b. exit")
        c = input("enter a or b")
        if(c == 'a'):
            addToDo(screen, list(input("what is the todo?")))
    return