# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def height(root):
            if root is None:
                return 0
            l = height(root.left)
            r = height(root.right)
            if l == -1 or r == -1:
                return -1
            if abs(r - l) > 1:
                return -1
            return 1 + max(l, r)

        if height(root) != -1:
            return True
        else:
            return False





