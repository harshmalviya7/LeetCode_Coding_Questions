# 617. Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:


        if root2 is None:
            return root1
        if root1 is None :
            return root2

        root1.va l =root1.va l +root2.val
        root1.lef t =self.mergeTrees(root1.left ,root2.left)
        root1.righ t =self.mergeTrees(root1.right ,root2.right)
        return root1
