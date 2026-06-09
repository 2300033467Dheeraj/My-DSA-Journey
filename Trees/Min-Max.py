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
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def display(root):
    if root is None:
        return
    print(root.data, end =" ")
    display(root.left)
    display(root.right)

def minimum(root):
    while root.left:
        root = root.left    
    return root.data

def maximum(root):
    while root.right:
        root = root.right
    return root.data
n = int(input())
arr = list(map(int, input().split()))

root = None

for x in arr:
    root = insert(root, x)

print(minimum(root))
print(maximum(root))