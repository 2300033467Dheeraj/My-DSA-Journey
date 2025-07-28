def GCD(n, m):
    while m:
        n, m = m, n % m
    return n
n ,m = 4,6
print(GCD(n, m))