n = 5
for i in range(0,2*n-1):
    if i > n:
        for j in range(0,2*n-i):
            print("*", end="")
    else:
        for j in range(0,i):
            print("*", end="")
    print()