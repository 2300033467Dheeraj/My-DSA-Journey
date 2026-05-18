arr = list(map(int,input().split()))

for i in range(len(arr)):
    left = 0
    right = 0
    
    for j in range(i):
        left += arr[j]
        
    for j in range(i+1,len(arr)):
        right += arr[j]
    
    if left == right:
        print(i)
        break
    
print("-1")