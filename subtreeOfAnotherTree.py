# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def check(root, subRoot):
            if root is None or subRoot is None:
                return root is None and subRoot is None

            elif root.val == subRoot.val:
                return check(root.left, subRoot.left) and check(root.right, subRoot.right)
            else:
                return False

        if root is None:
            return False
        elif check(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)






