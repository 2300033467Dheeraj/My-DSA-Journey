n = int(input())
for i in range(0,n+1):
    for j in range(0,i):
        print("*", end=" ")
    print("\n")  # Print a new line after each row
# *
# * *
# * * *
# * * * *