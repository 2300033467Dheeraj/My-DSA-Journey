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

def search(root,key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    if key < root.data:
        return search (root.left,key)
    
    return search(root.right,key)

