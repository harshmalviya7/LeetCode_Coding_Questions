# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        ans = []

        def helper(root, targetSum, curr):
            if root is None:
                return
            curr.append(root.val)
            targetSum -= root.val
            if root.left is None and root.right is None:
                if targetSum == 0:
                    ans.append(curr.copy())

            else:
                helper(root.left, targetSum, curr)
                helper(root.right, targetSum, curr)

            curr.pop()

        helper(root, targetSum, [])
        return ans