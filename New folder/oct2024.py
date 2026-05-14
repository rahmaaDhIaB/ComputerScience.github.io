


LinkedList = []
FirstEmpty = 0
FirstNode = -1

for i in range(19):
    LinkedList.append([-1,i+1])
LinkedList.append([-1,-1])

def InsertData():
    global FirstEmpty,LinkedList,FirstNode
    for i in range(5):
            newslot = FirstEmpty
            FirstEmpty = LinkedList[newslot][1]
            LinkedList[newslot][0] = int(input("insert"))
            LinkedList[newslot][1] = FirstNode
            FirstNode = newslot
    
def OutputLinkedList():
    global FirstEmpty,LinkedList,FirstNode
    PrintNode = FirstNode
    for i in range(20):
        if PrintNode == -1:
            break
        print(LinkedList[PrintNode][0])
        PrintNode = LinkedList[PrintNode][1]
        
InsertData()
OutputLinkedList()

def RemoveData(Data):
    # SearchNode = FirstNode
    # for i in range(20):
    #     if SearchNode == -1:
    #         break
    #     if LinkSearchNode == data:
    #         LinkedList[]

    if LinkedList[FirstNode][0] == Data:
        DeletingNode = FirstNode
        FirstNode = LinkedList[DeletingNode][1]
        LinkedList[DeletingNode][1] = FirstEmpty
        FirstEmpty = DeletingNode
    else:
        previous = -1
        current = FirstNode
        while LinkedList[current][0] != Data and LinkedList[current][1] != -1:
            previous = current
            current = LinkedList[current][1]
        if LinkedList[current][0] == Data:
            LinkedList[previous][1] = LinkedList[current][1]
            LinkedList[current][1] = FirstEmpty
            LinkedList[current][0] = -1
            FirstEmpty = current
# ------------------------------------------------------------------------------------------------


def ReadData():
    try:
        array = []
        with open("Data.txt") as file:
            for line in file:
                array = file.read().split("\n")
            return array
    except IOError:
        return "file not found"

def FormatArray(Text):
    ArrayOutput = ""
    for i in range(len(text)):
        ArrayOutput = ArrayOutput + "_" + text[i]
    return ArrayOutput



def CompareStrings(string1,string2):

    for i in range(len(string1)):
        if string1[i] > string2[i]:
            return 2
        elif string1[i] < string2[i]:
            return 1
        
def Bubble(StringArray):
    n = len(StringArray)

    for i in range(n-1):
        for j in range(n-i-1):
            if  CompareStrings(StringArray[j],StringArray[j+1]) == 2:
                temp = StringArray[j]
                StringArray[j+1] = StringArray[j]
                StringArray[j] = temp
    
    return StringArray


