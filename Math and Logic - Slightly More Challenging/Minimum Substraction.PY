n = int(input())
power = 1 << (n.bit_length() - 1)
x = n - power
print(x)