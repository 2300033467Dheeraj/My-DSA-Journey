n = int(input())

divisor = [i for i in range(1,n) if n % i == 0]
if sum(divisor) == n:
    print("Perfect num")
else:
    print("Not Perfect")