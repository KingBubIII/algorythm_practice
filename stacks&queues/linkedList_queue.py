class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0
    
    def printList(self):
        currNode = self.first
        myArr = []
        while not currNode is None:
            myArr.append(currNode.value)
            currNode = currNode.next
        print(myArr)

    def peek(self):
        if self.last is None:
            return None
        else:
            return self.first.value
    
    def enqueue(self, value):
        if self.last is None:
            self.last = Node(value)
            self.first = Node(value)
        else:
            curr = self.first
            while not curr.next is None:
                curr = curr.next
            curr.next = Node(value)
            self.last = curr.next

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            temp = self.first
            self.first = temp.next
            self.length -= 1

            if self.length == 1:
                self.last = self.first


myStack = Queue()
myStack.dequeue()
print(myStack.peek())
myStack.printList()
myStack.enqueue('Joy')
print(myStack.peek())
myStack.printList()
print(myStack.peek())
myStack.printList()
myStack.enqueue('Matt')
print(myStack.peek())
myStack.printList()
myStack.dequeue()
print(myStack.peek())
myStack.printList()
myStack.enqueue('Pavel')
print(myStack.peek())
myStack.printList()