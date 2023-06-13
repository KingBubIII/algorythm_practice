# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# slow version
# class Solution:
#     def hasCycle(self, head) -> bool:
#         myArr = []
#         curr = head
        
#         while curr:
#             if not curr in myArr: 
#                 myArr.append(curr)
#                 curr = curr.next
#             else:
#                 return True
#         return False

# faster version -- learned you can use custom objects/ classes as keys for a dictionary/ hash map
class Solution:
    def hasCycle(self, head) -> bool:
        mydict = {}
        curr = head

        while curr:
            try:
                temp = mydict[curr]
                return True
            except KeyError:
                mydict[curr] = 1
                curr = curr.next
        return False



myLL = ListNode(1)
myLL.next = ListNode(2)

test = Solution()
print(test.hasCycle(myLL))