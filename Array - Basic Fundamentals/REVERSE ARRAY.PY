# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr =  list(map(int,input().split()))
reve_arr = arr[::-1]
for num in reve_arr:
    print(num , end=' ')