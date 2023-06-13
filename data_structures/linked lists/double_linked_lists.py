class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class DoubleLinkedList:
    def __init__(self, value) -> None:
        self.head = {"value" : value, "prev": None, "next" : None}
        self.tail = self.head
        self.length = 1

    def printList(self):
        currNode = self.head
        myArr = []
        while not currNode is None:
            myArr.append(currNode["value"])
            currNode = currNode["next"]
        print(myArr)

    def Traverse(self, target):
        index = 0
        currNode = self.head

        while not index == target:
            currNode = currNode["next"]
            index += 1

        return currNode
    
    def append(self, value):
        newNode = {"value" : value, "prev": None, "next" : None}
        newNode["prev"] = self.tail
        self.tail["next"] = newNode
        self.tail = newNode

        self.length += 1
    
    def prepend(self, value):
        newNode = {"value" : value, "prev": None, "next" : None}
        self.head["prev"] = newNode
        newNode["next"] = self.head
        self.head = newNode

        self.length += 1

    def insert(self, targetI, value):        
        newNode = {"value" : value, "prev": None, "next" : None}
        target = self.Traverse(targetI)
        
        newNode["prev"] = target["prev"]
        newNode["next"] = target

        target["prev"]["next"] = newNode
        target["prev"] = newNode
        
        self.length += 1
        return

    def remove(self, index):
        target = self.Traverse(index)
        target["prev"]["next"] = target["next"]
        target["next"]["prev"] = target["prev"]

        self.length -= 1
        return
    


myll = DoubleLinkedList(10)

myll.append(5)
myll.append(16)
myll.prepend(1)
myll.insert(2,99)
myll.remove(2)
myll.remove(0)
myll.printList()