
# 589. N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        re s =[]
        if root is None:
            return res
        def order(root ,res):
            res.append(root.val)
            if root.children:
                for i in root.children:
                    order(i ,res)
        order(root ,res)
        return res