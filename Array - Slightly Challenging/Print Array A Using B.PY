a = int(input())
arr = list(map(int,input().split()))
b = int(input())
brr = list(map(int,input().split()))
instance = set(range(a))
for num in range (b):
        if brr[num] in instance:
            print(arr[brr[num]],end= " ")
        else:
            print("-1", end=" ")