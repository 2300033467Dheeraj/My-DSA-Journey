def Armstrong(n,m):
    sum = 0 
    number = n
    while n>0:
        digit = n % 10
        sum += digit ** m
        n //= 10
    if sum == number:
        return True
    else:
        return False
n = 153
m = 3
print(Armstrong(n, m))