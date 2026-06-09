from turtle import left


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

def leftsum(root):

    count = 0
    while root and root.left:
        root = root.left
        count += root.data

    return count

def all_left(root):
    if root is None:
        return
    
    leftval = root.left.data if root.left else 0
    return leftval + all_left(root.left) + all_left(root.right)