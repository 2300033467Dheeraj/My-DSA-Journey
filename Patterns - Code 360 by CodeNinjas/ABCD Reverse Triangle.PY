def ABCDRevTri(n):
    for i in range(n):
        for char_code in range(ord('A'), ord('A') + (n - i - 1) + 1):
            print(chr(char_code), end=" ")
        print()
ABCDRevTri(6)

# A B C D E F
# A B C D E
# A B C D
# A B C
# A B 
# A