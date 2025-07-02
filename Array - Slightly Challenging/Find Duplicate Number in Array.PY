# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            print(arr[i])
            exit()
    