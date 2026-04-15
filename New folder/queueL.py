Size = 50
GameQueue = [None] * Size
HeadPointer = -1
TailPointer = 0

def AddToQueue(GameID):
    global GameQueue,HeadPointer,TailPointer
    if TailPointer == Size -1:
        print("Queue is full")
    else:
        if HeadPointer == -1:
            HeadPointer = 0
        GameQueue[TailPointer] = GameID
        TailPointer += 1


def RemoveFromQueue():
    global GameQueue,TailPointer,HeadPointer
    if TailPointer == Size -1 or TailPointer == HeadPointer:
        print("Queue is empty")
        return "Empty"
    else:
        RemovedGame = GameQueue[HeadPointer]
        HeadPointer += 1
        return RemovedGame

