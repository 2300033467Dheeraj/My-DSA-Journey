def rec(n):
    print("Hello")
def print_n_times(n):
    if n <= 0:
        return
    rec(n)
    print_n_times(n - 1)
n = 5
print_n_times(n)

# recusivew function is a function that calls itself
# in this case, the function print_n_times calls itself until n is 0
# and prints "Hello" n times