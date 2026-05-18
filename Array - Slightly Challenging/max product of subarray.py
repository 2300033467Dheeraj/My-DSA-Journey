arr = list(map(int,input().split()))
maxi = 0
count = 1

for i in range(len(arr)):
    count = 1
    for j in range(i,len(arr)):
        count *= abs(arr[j])
        maxi = max(count,maxi)
print(maxi)