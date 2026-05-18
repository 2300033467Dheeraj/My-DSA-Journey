n = int(input())
arr = []
res = []
for i in range(0,n):
    a,b = map(int,input().split())
    arr.append((a,b))

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j][0] == arr[i][1] and arr[j][1] == arr[i][0]:
            res.append((arr[i][1],arr[i][0]))

print(res)