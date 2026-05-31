def func(n):
    arr = []
    for i in range(1,n):
        if n % i == 0:
            arr.append(i)
    su = sum(arr)
    
    if su >= n:
        return "abundant "
    else:
        return "not abundant "
        
n = int(input())
print(func(n))