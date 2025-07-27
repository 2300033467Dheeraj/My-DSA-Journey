def Pattern(n):
    spaces = 2 * n - 2
    for i in range(1, 2 * n):
        stars = i
        if i > n:
            stars = 2 * n - i

        # stars
        for _ in range(stars):
            print("*", end="")

        # spaces
        for _ in range(spaces):
            print(" ", end="")

        # stars
        for _ in range(stars):
            print("*", end="")

        print()  # new line

        if i < n:
            spaces -= 2
        else:
            spaces += 2

# Example usage:
# Call Pattern with an integer value for 'n'
Pattern(5)