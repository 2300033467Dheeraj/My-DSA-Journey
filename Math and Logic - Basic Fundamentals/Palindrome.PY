def Palindrome(n):
    original_num = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    if original_num == reversed_num:
        return True
    else:
        return False

n = 123
print(Palindrome(n))  