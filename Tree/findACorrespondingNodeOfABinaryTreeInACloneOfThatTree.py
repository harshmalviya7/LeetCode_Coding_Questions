# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def helper(o, c):
            if o:
                if o is target:
                    self.ans = c
                    return
                helper(o.left, c.left)
                helper(o.right, c.right)

        helper(original, cloned)
        return self.ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def helper(o, c):
            if o:
                if o is target:
                    self.ans = c
                    return
                helper(o.left, c.left)
                helper(o.right, c.right)

        helper(original, cloned)
        return self.ans

