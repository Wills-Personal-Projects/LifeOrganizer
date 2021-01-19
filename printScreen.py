def printScreen(screen):
    wState = open("LifeOrganizer_pkg/currentWindowState.txt","r")
    v = 0
    while( v < len(screen)):
        print(wState.readline().rstrip())
        v = v + 1
    wState.close()