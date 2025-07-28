def sum (n):
    if n <= 0:
        return 0
    else:
        return n + sum(n - 1)
def sum_first_n_numbers(n):
    return sum(n)

n = 5
print(sum_first_n_numbers(n))