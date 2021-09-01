# 1302. Deepest Leaves Sum
# https://leetcode.com/problems/deepest-leaves-sum/
'''
Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque()
        q.appendleft(root)

        while (q):
            temp = len(q)
            b = 0
            for i in range(temp):
                node = q.pop()
                b += node.val
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)

        return b

