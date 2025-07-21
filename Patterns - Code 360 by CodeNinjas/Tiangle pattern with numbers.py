def nTriangle(n:int) ->None:
    for i in range(1,n+2):
        for j in range(1,i):
            print(j, end=" ")
        print("\n")
    pass

# 1
# 1 2
# 1 2 3
# 1 2 3 4