def Divisors(n):
    div = []
    for i in range(1,n+1):
        if n % i == 0:
            div.append(i)
    return div
n = 12
print(Divisors(n))