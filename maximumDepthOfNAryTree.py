"""
559. Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    from collections import deque
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        l = 0
        if root is None:
            return l
        queue = deque()
        queue.append(root)
        while (queue):
            l += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                for i in node.children:
                    queue.append(i)
        return l
