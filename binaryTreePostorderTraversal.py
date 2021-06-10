# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:



        def fun(root ,traversal):
            if root:

                traversal =fun(root.left ,traversal)
                traversal =fun(root.right ,traversal)
                traversal.append(root.val)
            return traversal

        return fun(root ,[])
