# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        it r =head
        whil e(itr.next):

            if itr.va l= =itr.next.val:
                itr.nex t =itr.next.next
            else:
                it r =itr.next

        return head