# array with 25 integers
DataArray = []

try:
    with open("Data.txt","r") as file:
        for line in file:
            DataArray.append(int(line))
except IOError:
    print("file did not exist")

def PrintArray(array):
    numbers =''
    for i in range(0,len(array)):
        numbers = numbers + " " + str(array[i])
    print(numbers)    

PrintArray(DataArray)

def LinearSearch(array,target):
    count = 0
    for i in array:
        if i == target:
            count += 1
    return count

number = int(input("Enter a number from 0-100"))
while number > 100 or number < 0:
    number = int(input("Renter a number from 0-100"))

NumberCount = LinearSearch(DataArray,number)
print("The number",number,"is found",NumberCount,"times")

class Vehicle:
    #self.__ID  string
    #self.__MaxSpeed : INTEGER
    #self.__CurrentSpeed : INTEGER
    #self.__IncreaseAmount : INTEGER
    #self.__HorizontalPosition: INTEGER
    def __init__(self,ID,MaxSpeed,CurrentSpeed,IncreaseAmount,HorizontalPosition):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__CurrentSpeed = CurrentSpeed
        self.__IncreaseAmount = IncreaseAmount
        self.__HorizontalPosition = HorizontalPosition

    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def SetCurrentSpeed(self,CurrentSpeed):
        self.__CurrentSpeed = CurrentSpeed
    def SetHorizontalPosition(self,HorizontalPosition):
        self.__HorizontalPosition = HorizontalPosition

    def IncreaseSpeed(self):
       self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
       if self.__CurrentSpeed > self.__MaxSpeed:
           self.__CurrentSpeed = self.__MaxSpeed
       self.__HorizontalPosition = self.__CurrentSpeed + self.__HorizontalPosition

    def Output(self):
        Print(self.__HorizontalPosition,self.__CurrentSpeed)

class Helicopter(Vehicle):
    #self.__VerticalPosition : Integer
    #self.__VerticalChange : Integer
    #self.__MaxHeight : Integer
    def __init__(self,VerticalPosition,VerticleChange,MaxHeight):
        super().__init__(self,ID,MaxSpeed,CurrentSpeed,IncreaseAmount,HorizontalPosition)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChange
        self.__MaxHeight = MaxHeight

    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        Vehicle.SetCurrentSpeed(self,Vehicle.GetCurrentSpeed + Vehicle.GetIncreaseAmount)
        if (Vehicle.GetCurrentSpeed(self) > Vehicle.GetMaxSpeed(self)):
            Vehicle.GetCurrentSpeed(self) = Vehicle.GetMaxSpeed(self)
        Vehicle.SetHorizontalPosition(self,Vehicle.GetCurrentSpeed(self)+Vehicle.GetHorizontalPosition(self))

    def Output(self):
        Print(Vehicle.GetHorizontalPosition,Vehicle.GetCurrentSpeed,self.__VerticlePosition)