# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None :
            return head

        pre v =None
        curren t =head
        whil e( m >1):
            pre v =current
            curren t =current.next m-=1
            n-=1 connection= prev
        tail=cu r rent
        whil e (n>0):
            ne xt _ node=current.next
            current.next=prev
            pre v =current current=next_n ode
            n-=1
        if connection is not N on e:
            connection.next=prev
        else:
            he a d=prev
        tail.next=current
        return head
