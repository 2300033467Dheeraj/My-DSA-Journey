# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int,input().split()))
value = int(input())
first= -1
last = -1
for i in range(n) :
    if arr[i]==value:
        if first==-1:
            first=i
        last = i
print(first,last)