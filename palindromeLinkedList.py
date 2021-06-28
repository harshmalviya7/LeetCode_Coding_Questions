# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if head is None:
            return True

        fast ,slo w =head ,head
        whil e(fast is not None and fast.next is not None):
            fas t =fast.next.next
            slo w =slow.next
        def reverse(head):
            if head is None:
                return head
            pre v =None
            it r =head
            whil e(itr):
                next_nod e =itr.next
                itr.nex t =prev
                pre v =itr
                it r =next_node
            return prev
        fas t =head
        slo w =reverse(slow)
        whil e(slow is not None):
            if slow.va l! =fast.val:
                return False
            slo w =slow.next
            fas t =fast.next
        return True




        def reverse(head):
            if head is None:
                return head
            pre v =None
            it r =head
            whil e(itr):
                next_nod e =itr.next
                itr.nex t =prev
                pre v =itr
                it r =next_node
            return prev






#solution2



#         a=[]
#         while(head):
#             a.append(head.val)
#             head=head.next
#         if a==a[::-1]:
#             return True
#         return False
