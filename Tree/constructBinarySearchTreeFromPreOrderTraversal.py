# 1008. Construct Binary Search Tree from Preorder Traversal
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def helper(root, s):
            if root is None:
                return TreeNode(s)
            if root.val > s:
                root.left = helper(root.left, s)
            else:
                root.right = helper(root.right, s)
            return root

        root = None
        for i in range(len(preorder)):
            root = helper(root, preorder[i])
        return root
