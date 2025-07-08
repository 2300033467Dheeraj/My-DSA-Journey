n = input()
length = len(n)
Narcissistic = 0
for digit in n:
    
    value = pow(int(digit),length)
    Narcissistic += value
    
print("Yes" if int(n) == Narcissistic else "No")