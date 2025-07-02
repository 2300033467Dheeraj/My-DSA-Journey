# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int,input().split()))
totalsum = sum(arr)
leftsum = 0
index = []

for i in range(n):
    rightsum = totalsum-leftsum-arr[i]
    index.append(abs(leftsum-rightsum))
    leftsum+=arr[i]
print(*index)
