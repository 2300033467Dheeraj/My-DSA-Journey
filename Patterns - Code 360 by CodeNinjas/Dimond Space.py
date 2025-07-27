def upper_triangle(n):
    for i in range(0,n):
        for j in range(1,n-i):
            print("*", end="")
        for k in range(1,2*i+1):
            print(" ", end="")
        for j in range(1,n-i):
            print("*", end="")
        print()
def lower_triangle(n):
    iniS = 8  # Initial number of spaces between the stars
    for i in range(1, n + 1): # Outer loop for rows, from 1 to n (inclusive)
        # Print stars on the left side
        for j in range(1, i + 1): # Prints 'i' stars
            print("*", end="")

        # Print spaces in the middle
        for j in range(iniS): # Prints 'iniS' spaces
            print(" ", end="")

        # Print stars on the right side
        for j in range(1, i + 1): # Prints 'i' stars
            print("*", end="")

        iniS -= 2  # Decrease the number of spaces by 2 for the next row
        print() 
n = 6
upper_triangle(n)
lower_triangle(n)
