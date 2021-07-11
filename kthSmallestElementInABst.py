# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        a = [0, 1]

        def helper(root):
            if root is None:
                return
            helper(root.left)
            if a[1] == k:
                a[1] += 1
                a[0] = root.val
                return
            a[1] += 1
            helper(root.right)

        helper(root)
        return a[0]
        # l=[]
        # def helper(root,l):
        #     if root is None:
        #         return
        #     l.append(root.val)
        #     helper(root.left,l)
        #     helper(root.right,l)
        # helper(root,l)
        # l.sort()
        # return l[k-1]

