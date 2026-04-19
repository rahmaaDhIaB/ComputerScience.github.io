class Node:
    def __init__(self,NodeData):
        #NodeData : Integer
        #LeftNode : Integer
        #RightNode : Integer
        self.__NodeData = NodeData
        self.__LeftNode = none
        self.__RightNode = none

def GetData(self):
    return self.__NodeData

def GetLeft(self):
    return self.__LeftNode

def GetRight(slef):
    return self.__RightNode

def SetLeft(self,Node):
    self.__LeftNode = Node

def SetRight(self,Node):
    self.__RightNode = Node



class Tree:
    def __init__(self,FirstNode):
        self.__FirstNode = FirstNode

    def GetRootNode(self):
        return self.__FirstNode

    def Insert(self,Node):
        CurrentNode = self.__FirstNode
        Inserted = True
        while Inserted:
            if CurrentNode.GetData() < Node.GetData()
                if CurrentNode.GetRight() == none:
                    CurrentNode.SetRight(Node)
                    Inserted = False
                else:
                    CurrentNode = CurrentNode.GetRight()
            else:
                if CurrentNode.GetLeft() == none:
                    CurrentNode.SetLeft(Node)
                    return
                else:
                    CurrentNode = CurrentNode.Getleft()


Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)

Tree1 = Tree(Node1)
Tree1.Insert(Node2)
Tree1.Insert(Node3)
Tree1.Insert(Node4)
Tree1.Insert(Node5)
