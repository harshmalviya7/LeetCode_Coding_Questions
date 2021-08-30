# 671. Second Minimum Node In a Binary Tree
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if root:
                m.add(root.val)
                helper(root.left)
                helper(root.right)

        m = set()
        helper(root)
        mini, ans = root.val, float("inf")
        for i in m:
            if mini < i < ans:
                ans = i
        return ans if ans < float("inf") else -1