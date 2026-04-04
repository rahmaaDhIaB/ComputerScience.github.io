class Character:
    def __innit__(self,name,Xposition,YPosition):
        #Name : STRING
        #XPosition : INTEGER
        #YPOsition : INTEGER

        self.__Name = name
        self.__XPosition = Xposition
        self.__YPosition = YPosition

    def GetXPosition(self):
        return self.__XPosition
    
    def GetYPosition(self):
        return self.__YPosiition
    
    def SetXPosition(self,change):

        updatedX = self.__XPosition + change
        if updatedX < 0:
            self.__XPosition = 0
        elif updatedX > 10000:
            self.__XPosition = 10000
        else:
            self.__XPosition = updatedX
            
    def SetYPosition(self,change):
        updatedY = self.__YPosition + change
        if updatedY < 0:
            self.__YPosition = 0
        elif updatedY > 10000:
            self.__YPosition = 10000
        else:
            self.__YPosition = updatedY
    
    def Move(self,direction):
        if direction == "up":
            self.__SetYPosition(10)
        elif direction == "down":
            self.__SetYPosition(-10)
        elif direction == "left":
            self.__SetXPosition(-10)
        elif direction == "right":
            self.__SetXPosition(10)
