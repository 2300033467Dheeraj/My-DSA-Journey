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

def count(root):
    if root is None:
        return
    return 1 + count(root.left) + count(root.right)

