# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
even = ''
odd = ''
for i in range(len(s)):
    if i%2 == 0:
        even += s[i]
    else:
        odd += s[i]
result = odd+even
print(result)