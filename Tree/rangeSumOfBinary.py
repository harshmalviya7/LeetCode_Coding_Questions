# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int,res=0) -> int:

        if root is None:
            return 0
        elif root.val<low:
            return self.rangeSumBST(root.right,low,high)
        elif root.val>high:
            return self.rangeSumBST(root.left,low,high)

        return (root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high))