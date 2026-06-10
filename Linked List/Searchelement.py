from sympy import true


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def display(head):    
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def search(head,key):
    if head is None or key is None:
        return
    
    temp = head
    while temp:
        if temp.data == key:
            return True
        temp = temp.next

    return False

n = int(input())
arr = list(map(int,input().split()))
head = None
tail = None
for x in arr:
    newnode = Node(x)

    if head is None:
        head = newnode
        tail = newnode
    else:
        tail.next = newnode
        tail = newnode

display(head)