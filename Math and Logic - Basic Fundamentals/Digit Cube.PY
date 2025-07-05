n = input().strip()
total = 0
for st in n:
    digit = int(st)
    cube = digit ** 3
    total += cube
if total == int(n):
    print("Yes")
else:
    print("No")