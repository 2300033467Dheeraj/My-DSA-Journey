# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
n = int(input())

cataln_number = math.factorial(2*n) // (math.factorial(n+1) * math.factorial(n))
print(cataln_number)