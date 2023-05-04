class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None;

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            prev = None
            curr = self.root
            while not curr is None:
                if value > curr.value:
                    prev = curr
                    curr = curr.right
                elif value < curr.value:
                    prev = curr
                    curr = curr.left
                
            if value > prev.value:
                prev.right = Node(value)
            elif value < prev.value:
                prev.left = Node(value)

        return self.root


    def lookup(self, value):
        if self.root is None:
            return False
        else:
            curr = self.root
            while not curr is None:
                if curr.value == value:
                    return curr
                elif value > curr.value:
                    curr = curr.right
                elif value < curr.value:
                    curr = curr.left
            
            return False
            

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree)
res1 = tree.lookup(5)
print(res1)

#      9
#   4     20
# 1  6  15  170