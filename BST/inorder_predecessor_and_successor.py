
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
def inpre(root):
    if root.right is None:

        return root.val
    else:
        return root.right
def insuc(root):
    if root.left is None:
        return root.val
    else:
        return root.left
def findPreSuc(root,pre,suc,key):

    if root is None:
        return
    if root.val==key:

        if root.left:

            findPreSuc.pre=inpre(root.left)
        if root.right:
            findPreSuc.suc=insuc(root.right)
        return
    if root.val>key:

        findPreSuc.suc=root.val
        findPreSuc(root.left,findPreSuc.pre,findPreSuc.suc,key)
    elif root.val<key:
        findPreSuc.pre=root.val
        findPreSuc(root.right,findPreSuc.pre,findPreSuc.suc,key)





r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
# inorder(r)
findPreSuc.pre,findPreSuc.suc=0,0

findPreSuc(r,findPreSuc.pre,findPreSuc.suc,80)
print(findPreSuc.pre,findPreSuc.suc)