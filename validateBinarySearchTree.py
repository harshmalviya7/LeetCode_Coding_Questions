# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(root, maxm, minn):

            if root is None:
                return True
            elif root.val >= maxm or root.val <= minn:
                return False
            else:
                return helper(root.left, root.val, minn) and helper(root.right, maxm, root.val)

        return helper(root, sys.maxsize, -sys.maxsize - 1)