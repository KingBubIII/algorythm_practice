# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my slow solution
# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         if not list1:
#             return list2
#         if not list2:
#             return list1

#         if list2.val < list1.val:
#             temp = list2
#             list2 = list1
#             list1 = temp
        
#         print(list1)
#         print(list2)

#         curr = list1
        
#         while list2:
#             fit = list2
#             # print(type(fit))
#             # print(type(curr))

#             if fit.val < curr.val:
#                 temp = fit.next
#                 fit.next = list1
#                 fit = temp

#             elif fit.val == curr.val:
#                 fit_temp = fit.next
#                 list_temp = curr.next

#                 curr.next = fit
#                 fit.next = list_temp
#                 list2 = fit_temp

#             elif fit.val > curr.val:
#                 if curr.next is None or fit.val < curr.next.val:
#                     list_temp = curr.next
#                     curr.next = fit
#                     fit_temp = fit.next
#                     fit.next = list_temp
#                     list2 = fit_temp
#                 elif fit.val >= curr.next.val:
#                     curr = curr.next
#         return list1
    

# Connor's fast solution
class Solution:
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1
        curr = None
        if l1.val < l2.val:
            curr = l1
            l1 = l1.next
        else:
            curr = l2
            l2 = l2.next
        ret = curr
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return ret

test1 = ListNode(2)
test2 = ListNode(1)
# test1 = ListNode(1,ListNode(2, ListNode(4)))
# test2 = ListNode(1, ListNode(3, ListNode(4)))
result = Solution().mergeTwoLists(test1, test2)
