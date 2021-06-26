
# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        #         if head is None or head.next is None:
        #             return head

        #         else:
        #             temp=head
        #             head=head.next
        #             temp.next=head.next
        #             head.next=temp

        #             temp.next=self.swapPairs(temp.next)

        #         return head

        def linked(node):
            if node is None :
                return
            if node.next is None:
                return
            else:
                tem p =node.val
                node.va l =node.next.val
                node.next.va l =temp
                linked(node.next.next)
        linked(head)
        return head




