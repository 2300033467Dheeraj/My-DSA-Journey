n = 7
for i in range(n): # Outer loop for rows, from 0 to n-1

    # Print leading spaces
    for _ in range(n - i - 1): # Use _ if the loop variable isn't used
        print(" ", end="")

    # Print characters for the left half (inclusive of peak)
    for j in range(i + 1): # From 0 up to i
        print(chr(ord('A') + j), end="")

    # Print characters for the right half (excluding peak, as it's already printed)
    for j in range(i - 1, -1, -1): # From i-1 down to 0
        print(chr(ord('A') + j), end="")

    # Print trailing spaces (optional, as print() adds newline, but good for symmetry in concept)
    for _ in range(n - i - 1):
        print(" ", end="")

    print() # Move to the next line