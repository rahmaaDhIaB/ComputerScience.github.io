class Character:
    # Name : String
    # XPosition : Integer
    # YPosition : Integer
    def __init__(self,Name,XPosition,YPosition):
        self.__Name = Name
        self.__XPosition = XPosition
        self.__YPosition = YPosition

    def GetXPosition(self):
        return self.__XPosition
    def GetYPosition(self):
        return self.__YPosition
    
    def SetXPosition(self,value):
        self.__XPosition = self.__XPosition + value
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        elif self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self,value):
        self.__YPosition = self.__YPosition + value
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        elif self.__YPosition < 0:
            self.__YPosition = 0
    
    def Move(self,direction):
        if direction == "up":
            SetYPosition(10)
        elif direction == "down":
            SetYPosition(-10)
        elif direction == "left":
            SetXPosition(-10)
        else:
            SetXPosition(10)
        