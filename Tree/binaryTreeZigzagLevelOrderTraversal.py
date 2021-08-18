# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        l = []
        q = deque()
        q.appendleft(root)
        f = False
        while (q):
            curr = []
            size = len(q)
            for i in range(size):
                temp = q.pop()
                curr.append(temp.val)
                if temp.left:
                    q.appendleft(temp.left)
                if temp.right:
                    q.appendleft(temp.right)
            if f:
                curr.reverse()

            l.append(curr)
            f = not f

        return l