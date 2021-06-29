# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, itr1: ListNode, itr2: ListNode) -> ListNode:
        if not itr1:  return itr2
        if not itr2:  return itr1

        dump = ListNode(0)
        itr = dump

        while (itr1 and itr2):

            if itr1.val > itr2.val:
                itr.next = ListNode(itr2.val)

                itr2 = itr2.next
            else:
                itr.next = ListNode(itr1.val)

                itr1 = itr1.next
            itr = itr.next
        if itr1:
            itr.next = itr1

        if itr2:
            itr.next = itr2

        return dump.next






