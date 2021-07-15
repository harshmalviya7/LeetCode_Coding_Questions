# 19. Remove Nth Node From End of List/
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        prev = ListNode(0)
        prev.next = head
        first, sec = prev.next, prev
        for i in range(n):
            first = first.next

        while (first):
            sec = sec.next
            first = first.next
        sec.next = sec.next.next

        return prev.next
