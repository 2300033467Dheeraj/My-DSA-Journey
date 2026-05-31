def func(n):
    
    count = 0
    m = str(n)
    for num in m:
        count += int(num)
    if n % count == 0:
        return True
    else:
        return False
n = int(input())
print(func(n))