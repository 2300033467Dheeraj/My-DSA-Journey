
N = int(input())
A = list(map(int, input().split()))
for i in range(N-1):
    for j in range(0, N - i - 1):    
        if A[j] > A[j+1]:        
            A[j], A[j+1] = A[j+1], A[j]            
    print(' '.join(str(x) for x in A))            
    