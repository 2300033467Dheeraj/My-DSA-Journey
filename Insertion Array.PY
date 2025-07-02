n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
Printed=set()

for i in range(n):
    if arr1[i] in arr2 and arr1[i] not in Printed:
            print(arr1[i], end=' ')
            Printed.add(arr1[i])