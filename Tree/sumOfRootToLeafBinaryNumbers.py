# 1022. Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.total = 0

        def helper(root, binary):
            if root is None:
                return
            helper(root.left, binary + str(root.val))
            helper(root.right, binary + str(root.val))

            if not root.left and not root.right:
                self.total += int(binary + str(root.val), 2)

        helper(root, "")
        return self.total

