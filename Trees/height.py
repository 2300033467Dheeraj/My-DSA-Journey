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

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left) , height(root.right))

n = int(input())
arr = list(map(int, input().split()))

root = None

for x in arr:
    root = insert(root, x)

print(height(root))