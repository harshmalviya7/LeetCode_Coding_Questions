# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryRecursive(self ,nums ,left ,right):
        if lef t >right:
            return
        mi d= lef t +(righ t -left )/ /2
        node = TreeNode(nums[mid])
        node.left = self.binaryRecursive(nums ,left ,mi d -1)
        node.right = self.binaryRecursive(nums ,mi d +1 ,right)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums )= =0 or num s= =None:
            return
        return self.binaryRecursive(nums ,0 ,len(nums ) -1)


