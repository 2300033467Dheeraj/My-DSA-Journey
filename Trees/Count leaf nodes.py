class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
def insert(root,val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    
    return root

def leafs(root):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        return 1
    
    return leafs(root.right) + leafs(root.right)