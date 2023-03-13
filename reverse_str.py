class MyArray():
    def __init__(self, data):
        self.length = len(data)
        self.data = data

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data.append(item)
        self.length += 1
        return self.data

    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    def deleteAtIndex(self, index):
        item = self.data[index]
        self.shiftItems(index)
        return item

    def shiftItems(self, index):
        for i in range(index, self.length-1):
            print(i)
            self.data[i] = self.data[i + 1]
            
            print(self.data[self.length - 1])
            del self.data[self.length - 1]
            self.length -= 1


def reverse(input):
    original = MyArray(list(input))
    reverse = MyArray([])
    print(original.data)
    print(original.length)

    for i in range(original.length-1,-1,-1):
        reverse.push(original.data[i])


    print("".join(reverse.data))
    print(reverse.length)



reverse('hello world')