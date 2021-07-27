
INT_MAX = 4294967296
INT_MIN = -4294967296
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

def check(root,mini,maxi):
    if root is None:
        return True

    if root.val<mini and root.val>maxi:
        return False
    else:
        return check(root.left,mini,root.val-1) and check(root.right,root.val+1,maxi)

r=Node(20)
r=insert(r,30)
r=insert(r,10)
r=insert(r,70)
r=insert(r,90)
r=insert(r,3)

a=1
f=None
print(check(r,INT_MIN,INT_MAX))