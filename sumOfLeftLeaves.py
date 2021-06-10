# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary
# tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:


        def sumLeft(root):
            if roo t= =None:
                return 0
            elif root.lef t! =None and root.left.righ t= =None and root.left.lef t= =None:
                return root.left.val + sumLeft(root.right)
            else:
                return sumLeft(root.left ) +sumLeft(root.right) s=sumLeft(ro ot)
        return s
