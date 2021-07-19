# 897. Increasing Order Search Tree
# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def helper(root, traversal):
            if root:
                traversal = helper(root.left, traversal)
                traversal.append(root.val)
                traversal = helper(root.right, traversal)
            return traversal

        traversal = []
        print(helper(root, traversal))
        node = TreeNode(traversal[0])
        prev = node
        for i in range(1, len(traversal)):
            prev.right = TreeNode(traversal[i])
            prev = prev.right
        return (node)
