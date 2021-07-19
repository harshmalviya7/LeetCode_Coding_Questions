# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def length(root):
            itr = root
            a = 0
            while (itr):
                itr = itr.next
                a += 1
            return a

        def reverse(head, k, l):
            if l < k:
                return head
            c = 0
            prev = None
            curr = head
            while (c < k and curr != None):
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
                c += 1
            if curr != None:
                head.next = reverse(curr, k, l - k)
            return prev

        return reverse(head, k, length(head))
