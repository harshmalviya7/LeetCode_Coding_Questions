# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# 501. Find Mode in Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        d = defaultdict(int)

        def helper(root):
            if root is None:
                return
            d[root.val] += 1
            helper(root.left)
            helper(root.right)

        helper(root)
        m = max(d.values())
        print(m)
        return [i for i, j in d.items() if j == m]