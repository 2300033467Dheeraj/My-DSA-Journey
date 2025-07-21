# Enter your code here. Read input from STDIN. Print output to STDOUT
def linear(arr,n,m) :
    for i in range (0,n-1):
        if arr[i] == m:
            print(i)        
    return -1
       
n , m = map(int,input().split())
arr = list(map(int,input().split()))
linear(arr,n,m)