# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# 429. N-ary Tree Level Order Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.appendleft(root)
        l = []
        c = []
        q2 = deque()
        while (q):
            temp = q.pop()
            c.append(temp.val)

            for i in temp.children:
                q2.appendleft(i)

            if not q:
                q = q2
                q2 = deque()
                l.append(c)
                c = []
        return l

