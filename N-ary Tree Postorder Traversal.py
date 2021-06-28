# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        re s =[]
        if root == None:
            return res
        def order(root ,res):
            if root.children:
                for i in root.children:
                    order(i ,res)
            res.append(root.val)
        order(root ,res)
        return res


#         l_stack=[]
#         output=[]
#         if root is None:
#             return output
#         l_stack.append(root)
#         while(l_stack ):
#             a=l_stack.pop(-1)
#             output.append(a.val)
#             for i in a.children:
#                 l_stack.append(i)

#         return reversed(output)



