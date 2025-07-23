def upper_triangle(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ", end="")
        for k in range(0,2*i+1):
            print("*", end="")
        for j in range(0,n-i-1):
            print(" ", end="")
        print()
def lower_triangle(n):
    for i in range(0,n):
        for j in range(0,i):
            print(" ", end="")
        for k in range(0,2*n-(2*i+1)):
            print("*",end="")
        for j in range(0,i):
            print(" ", end="")
        print()
n = 6
upper_triangle(n)
lower_triangle(n)
