arr = list(map(int,input().split()))
sortedarr = sorted(arr)
res = []
for num in arr:
    rank = sortedarr.index(num) + 1 
    res.append(rank)
print(res)