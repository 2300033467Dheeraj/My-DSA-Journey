# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input().strip()
demoninator = 0
for st in n :
    digit = int(st)
    demoninator += digit
numerator = int(n)
if numerator % demoninator == 0:
    print("Yes")
else:
    print("No")