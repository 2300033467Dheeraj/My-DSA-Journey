n = 5 
for i in range(1,n):
    for j in range(1,n):
        if  i == 1 or i == n-1 or i + j == n+1 :
            print("* ",end="")
        else:
            print(" ",end="")
    print()