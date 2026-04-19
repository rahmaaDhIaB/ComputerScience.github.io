class Record:
    def __init__(self,key,data):
        self.Key = key
        self.Data = data

HashTable = []

def InitialiseHashTable():
    HashTable = [[Record(-1,"")]*10 for i in range(100)]

def Hash(key):
    return key % 100
     
def InsertData(Record):
    global HashTable
    adress = Hash(Record.Key)
    for col in range(10):
        if HashTable[adress][col] == -1:
            HashTable[adress][col] = Record
            break
        
def ReadData():
    global
    with open("HashTableData.txt","r") as file:
        for line in file:

            KeyAndData = line.strip().split(",")
            InsertData(Record(KeyAndData))