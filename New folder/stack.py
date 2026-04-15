Size = 30
Scores = [None] * Size
TopOfStack = -1

def AddScore(Value):
    global TopOfStack,Scores
    if TopOfStack == Size -1:
        return False
    else:
        TopOfStack += 1
        Scores[TopOfStack] = Value
        return True
        
    
def UndoScore():
    global TopOfStack,Scores
    if TopOfStack == -1:
        return -999
    else:
        ValueToPop = Scores[TopOfStack]
        TopOfStack -= 1
        return ValueToPop
