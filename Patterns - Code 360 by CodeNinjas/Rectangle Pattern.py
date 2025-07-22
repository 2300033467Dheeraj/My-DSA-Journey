n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j == n-i+1:
            print("*",end="")
        else:
            print(n-j+1,end="")
    print() 

# 5432*
# 543*1
# 54*21
# 5*321
# *4321