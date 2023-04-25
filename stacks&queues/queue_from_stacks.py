class MyQueue:
    def __init__(self):
        self.stack = []
        self.queue = []

    def StQ(self) -> bool:
        if not self.empty():
            if self.queue == []:
                for count in range(len(self.stack)):
                    self.queue.insert(0,self.stack.pop(0))
            return True
        return False

    def push(self, x: int) -> None:
        self.stack.insert(0,x)

    def pop(self) -> int:
        if self.StQ():
            return self.queue.pop(0)
        else:
            return None

    def peek(self) -> int:
        if self.StQ():
            return self.queue[0]
        else: 
            return None

    def empty(self) -> bool:
        if self.queue == [] and self.stack == []:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
test1 = obj.push(1)
test2 = obj.push(2)
test3 = obj.push(3)
test4 = obj.push(4)
test5 = obj.pop()
test6 = obj.push(5)
test7 = obj.pop()
test8 = obj.pop()
test9 = obj.pop()
test10 = obj.pop()
test
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()