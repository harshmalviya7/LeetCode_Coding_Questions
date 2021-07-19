# 965. Univalued Binary Tree
# https://leetcode.com/problems/univalued-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        a = root.val

        def helper(root, a):
            if root is None:
                return True
            if root.val != a:
                return False
            return helper(root.left, a) and helper(root.right, a)

        return helper(root, a)