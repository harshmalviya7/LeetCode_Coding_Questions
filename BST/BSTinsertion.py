
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val>key:
            root.left=insert(root.left,key)
        else:
            root.right = insert(root.right, key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r=Node(20)
r=insert(r,30)
r=insert(r,10)
r=insert(r,70)
r=insert(r,90)
r=insert(r,3)
inorder(r)