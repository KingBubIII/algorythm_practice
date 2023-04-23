class Stack:
    def __init__(self) -> None:
        self.array = []

    def peek(self):
        if not self.isEmpty():
            return self.array[len(self.array)-1]
        else:
            return None
    
    def isEmpty(self):
        return not bool(len(self.array))
    
    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()
    
    def __len__(self):
        return len(self.array)

myStack = Stack()
print(myStack.peek())
myStack.push("google")
myStack.push("Udemy")
print(myStack.peek())
myStack.push("Discord")
myStack.pop()
print(myStack.peek())
print(myStack.array)


# //Discord
# //Udemy
# //google
