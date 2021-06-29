# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        itr1, itr2 = l1, l2
        a = ListNode(0)
        itr = a
        c = 0
        while (itr1 or itr2 or c):
            x = itr1.val if itr1 else 0

            y = itr2.val if itr2 else 0

            summ = x + y + c
            c = summ // 10
            itr.next = ListNode(summ % 10)
            itr = itr.next

            itr1 = itr1.next if itr1 else None

            itr2 = itr2.next if itr2 else None
        # if c>0:
        #     itr.next=ListNode(c)
        return a.next