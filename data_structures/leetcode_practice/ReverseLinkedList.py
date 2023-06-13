# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        currNode = head
        prevNode = None
        while currNode:
            temp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = temp
        return prevNode

ret = Solution().reverseList( ListNode(val=1, next = ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None))))))
print(ret)