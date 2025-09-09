def seeding(n: int) -> None:
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print("*",end=" ")
        print("\n")

seeding(5)
n = 5