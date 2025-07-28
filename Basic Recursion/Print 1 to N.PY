def recursion(n):
    for i in range(1, n + 1):
        print(i)
def print_1_to_n(n):
    if n <= 0:
        return
    recursion(n)
    print_1_to_n(n - 1)
n = 5
print_1_to_n(n)