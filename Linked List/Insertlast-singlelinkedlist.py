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
def insertlast(head,val):
    newnode= Node(val)

    if head is None:
        return newnode
    
    temp = head
    
    while temp.next:
        temp = temp.next

    temp.next = newnode
    
    return head


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