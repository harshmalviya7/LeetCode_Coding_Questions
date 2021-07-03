# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        l = []
        queue = deque()
        queue.append(root)
        while (queue):
            size = len(queue)
            for i in range(size):
                current = queue.pop()
                if i == size - 1:
                    l.append(current.val)
                if current.left is not None:
                    queue.appendleft(current.left)
                if current.right is not None:
                    queue.appendleft(current.right)
        return l


