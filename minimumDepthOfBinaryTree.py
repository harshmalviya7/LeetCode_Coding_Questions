# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self. c =float("inf")

        def dfs(root ,num):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                self. c =min(self.c ,num)
            dfs(root.left ,nu m +1)
            dfs(root.right ,nu m +1)
        dfs(root ,1)
        return self.c