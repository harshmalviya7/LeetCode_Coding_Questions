# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        curr = head
        prev = sentinel
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev=curr
            curr = curr.next
        return sentinel.next