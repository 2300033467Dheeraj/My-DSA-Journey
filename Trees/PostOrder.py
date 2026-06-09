def post(root):
    if root is None:
        return
    
    post(root.left)
    post(root.right)
    print(root.data,end = " ")
    