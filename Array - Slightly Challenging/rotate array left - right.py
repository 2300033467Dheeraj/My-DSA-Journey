arr = list(map(int,input().split()))
k = int(input())
rot = input().strip()

k = k % len(arr)

if rot == "right":
    rotated = arr[- k :] + arr[:-k]
else:
    rotated = arr[k:] + arr[:k]

print(*rotated)
