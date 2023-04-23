class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0
    
    def printList(self):
        currNode = self.top
        myArr = []
        while not currNode is None:
            myArr.append(currNode.value)
            currNode = currNode.next
        print(myArr)

    def peek(self):
        return self.top
    
    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            temp = self.top
            self.top = newNode
            self.top.next = temp
            self.length += 1
        
    def pop(self):
        if not self.top:
            return None
        
        if self.top == self.bottom:
            self.top = None
            self.bottom = None
            return None
        
        temp = self.top.next
        ret = self.top.value
        self.top = temp
        self.length -= 1
        return ret
    
    def isEmpty(self):
        return not bool(self.length)

myStack = Stack()
myStack.push("google")
myStack.push('udemy')
myStack.push('discord')
myStack.printList()
print(myStack.isEmpty())
myStack.pop()
myStack.pop()
myStack.pop()
myStack.printList()
print(myStack.isEmpty())


# //Discord
# //Udemy
# //google
