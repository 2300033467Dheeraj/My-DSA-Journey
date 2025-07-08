# Enter your code here. Read input from STDIN. Print output to STDOUT
text = input()
n = len(text)
if n%2 != 0:
    print("No")
else:
    half = n//2
    left = text[:half]
    right = text[half:]
    if left == right:
        print("Yes")
    else:
        print("No")