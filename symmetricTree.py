# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return root

        def binary(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return a.val == b.val and binary(a.right, b.left) and binary(a.left, b.right)

        return binary(root, root)





