
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        length = -1
        prev_TBR = None
        TBR = head
        next_TBR = head
        curr = head
        
        while curr:
            length += 1
            offset = length-n

            curr = curr.next
            if offset-1 >= -1:
                if prev_TBR is None:
                    prev_TBR = head
                else:
                    prev_TBR = prev_TBR.next
            if offset >= 0:
                TBR = TBR.next
                print()
            if offset+1 >= 0:
                next_TBR = next_TBR.next

        if prev_TBR is None:
            if TBR.next is None:
                return None
            else:
                head = TBR.next
        else:
            prev_TBR.next = next_TBR
            
        return head

        currNode = head
        myArr = []
        while not currNode is None:
            myArr.append(currNode.val)
            currNode = currNode.next
        print(myArr)

        return head
    

# test = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# test = ListNode(1)
test = ListNode(1, ListNode(2))
result = Solution().removeNthFromEnd(test, 2)